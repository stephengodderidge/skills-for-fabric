#!/usr/bin/env python3
"""Validate skill structure, references, routing metadata, and content quality."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = ROOT / "skills"
REPORT_PATH = ROOT / "quality-report.json"
ACTION_VERBS = {
    "analyze", "automate", "build", "check", "configure", "create", "deploy",
    "develop", "execute", "explore", "generate", "implement", "manage",
    "monitor", "query", "run", "validate",
}
TECHNOLOGIES = {
    "api", "azure", "cli", "dax", "delta", "fabric", "kql", "lakehouse",
    "livy", "mcp", "notebook", "pipeline", "power bi", "pyspark", "rest",
    "spark", "sql", "sqlcmd", "t-sql", "tmdl", "warehouse",
}
IGNORED_WORDS = {
    "a", "an", "and", "against", "for", "from", "in", "inside", "of", "on",
    "or", "the", "to", "use", "using", "via", "when", "with",
}


def parse_skill(path: Path) -> tuple[dict, str, list[str]]:
    content = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return {}, content, ["Missing or invalid YAML frontmatter"]
    try:
        frontmatter = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        return {}, content, [f"Invalid YAML frontmatter: {exc}"]
    return frontmatter, content, []


def extract_triggers(description: str) -> list[str]:
    match = re.search(r"\bTriggers?:\s*(.+)$", description, re.IGNORECASE | re.DOTALL)
    if not match:
        return []
    quoted = re.findall(r'"([^"]+)"|\'([^\']+)\'', match.group(1))
    return [next(value for value in pair if value).strip().lower() for pair in quoted]


def description_words(description: str) -> set[str]:
    description = re.sub(r"\bTriggers?:.*$", "", description, flags=re.IGNORECASE | re.DOTALL)
    return {
        word for word in re.findall(r"[a-z0-9+#-]+", description.lower())
        if len(word) > 1 and word not in IGNORED_WORDS
    }


def validate_links(path: Path, content: str) -> list[str]:
    issues = []
    for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", content):
        target = target.strip().split(maxsplit=1)[0].strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        relative_path = target.split("#", 1)[0]
        if relative_path and not (path.parent / relative_path).resolve().exists():
            issues.append(f"Broken reference: {target}")
    return sorted(set(issues))


def find_untagged_fences(content: str) -> list[int]:
    issues = []
    in_fence = False
    for line_number, line in enumerate(content.splitlines(), start=1):
        if not re.match(r"\s*```", line):
            continue
        if in_fence:
            in_fence = False
        else:
            in_fence = True
            if re.fullmatch(r"\s*```\s*", line):
                issues.append(line_number)
    return issues


def main() -> int:
    report = {
        "overall_status": "PASSED",
        "critical_count": 0,
        "warning_count": 0,
        "semantic_conflicts": [],
        "duplicate_triggers": [],
        "broken_references": [],
        "structural_issues": [],
        "content_warnings": [],
        "skills": {},
    }
    parsed_skills = {}
    triggers = defaultdict(list)

    print("📋 skills-for-fabric QUALITY CHECK")
    print("=" * 50)

    for path in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        name = path.parent.name
        print(f"📂 Scanning: {name}")
        frontmatter, content, critical = parse_skill(path)
        description = str(frontmatter.get("description", "")).strip()

        if not frontmatter.get("name"):
            critical.append("Missing frontmatter name")
        elif frontmatter["name"] != name:
            critical.append(
                f"Frontmatter name '{frontmatter['name']}' does not match folder '{name}'"
            )
        if not description:
            critical.append("Missing frontmatter description")
        elif len(description) > 1023:
            critical.append(f"Description exceeds 1023 characters ({len(description)})")
        if name != "check-updates" and not re.search(
            r"^>\s*\*\*Update Check", content, re.MULTILINE
        ):
            critical.append("Missing required update-check notice")

        broken_links = validate_links(path, content)
        critical.extend(broken_links)
        report["broken_references"].extend(
            {"skill": name, "issue": issue} for issue in broken_links
        )

        warnings = []
        for heading in ("must", "prefer", "avoid"):
            if not re.search(rf"^###?\s+.*\b{heading}\b", content, re.IGNORECASE | re.MULTILINE):
                warnings.append(f"Missing {heading.title()} guidance section")
        if not re.search(r"^##\s+Examples?\b", content, re.IGNORECASE | re.MULTILINE):
            warnings.append("Missing Examples section")
        untagged = find_untagged_fences(content)
        if untagged:
            warnings.append(f"Untagged code fences at lines: {', '.join(map(str, untagged))}")
        if description:
            first_word = re.match(r"[A-Za-z]+", description)
            if not first_word or first_word.group(0).lower() not in ACTION_VERBS:
                warnings.append("Description should start with a recognized action verb")
            if not any(term in description.lower() for term in TECHNOLOGIES):
                warnings.append("Description should mention a supported technology")
            if len(description) >= 900:
                warnings.append(f"Description is approaching the 1023-character limit ({len(description)})")

        skill_triggers = extract_triggers(description)
        for trigger in skill_triggers:
            triggers[trigger].append(name)

        report["skills"][name] = {
            "path": str(path.relative_to(ROOT)),
            "critical": critical,
            "warnings": warnings,
            "triggers": skill_triggers,
        }
        report["structural_issues"].extend(
            {"skill": name, "issue": issue} for issue in critical
            if not issue.startswith("Broken reference:")
        )
        report["content_warnings"].extend(
            {"skill": name, "issue": warning} for warning in warnings
        )
        parsed_skills[name] = description_words(description)

    for trigger, names in sorted(triggers.items()):
        if len(names) > 1:
            conflict = {"trigger": trigger, "skills": names}
            report["duplicate_triggers"].append(conflict)
            issue = f"Duplicate trigger '{trigger}' shared by {', '.join(names)}"
            for name in names:
                report["skills"][name]["critical"].append(issue)

    names = sorted(parsed_skills)
    for index, left in enumerate(names):
        for right in names[index + 1:]:
            union = parsed_skills[left] | parsed_skills[right]
            similarity = len(parsed_skills[left] & parsed_skills[right]) / len(union) if union else 0
            if similarity >= 0.20:
                severity = "critical" if similarity >= 0.30 else "warning"
                conflict = {
                    "skills": [left, right],
                    "similarity": round(similarity, 3),
                    "severity": severity,
                }
                report["semantic_conflicts"].append(conflict)
                issue = f"Description similarity with {right}: {similarity:.1%}"
                if severity == "critical":
                    report["skills"][left]["critical"].append(issue)
                    report["skills"][right]["critical"].append(
                        f"Description similarity with {left}: {similarity:.1%}"
                    )
                else:
                    report["skills"][left]["warnings"].append(issue)
                    report["skills"][right]["warnings"].append(
                        f"Description similarity with {left}: {similarity:.1%}"
                    )

    report["critical_count"] = sum(
        len(result["critical"]) for result in report["skills"].values()
    )
    report["warning_count"] = sum(
        len(result["warnings"]) for result in report["skills"].values()
    )
    if report["critical_count"]:
        report["overall_status"] = "CRITICAL"
    elif report["warning_count"]:
        report["overall_status"] = "WARNING"

    REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("\n" + "=" * 50)
    print("📊 QUALITY CHECK SUMMARY")
    print(f"Files scanned: {len(report['skills'])}")
    print(f"Critical issues: {report['critical_count']}")
    print(f"Warnings: {report['warning_count']}")
    print(f"📄 Report saved to: {REPORT_PATH.relative_to(ROOT)}")
    if report["critical_count"]:
        print("\n❌ RESULT: CRITICAL")
        for name, result in report["skills"].items():
            for issue in result["critical"]:
                print(f"  - {name}: {issue}")
        return 1
    print(f"\n✅ RESULT: {'PASSED with warnings' if report['warning_count'] else 'PASSED'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
