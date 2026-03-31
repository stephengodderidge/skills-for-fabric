# Internal References Audit

> **Purpose**: This document catalogs every instance across the repository that references documentation, APIs, workspaces, or resources that most people (non-Microsoft employees) do not have access to. Each entry includes the file, line number(s), exact content, and a recommended action.

---

## Table of Contents

1. [SharePoint Links](#1-sharepoint-links)
2. [Internal API Endpoints](#2-internal-api-endpoints)
3. [Internal GIM Policy Links](#3-internal-gim-policy-links)
4. [MSIT Environment References](#4-msit-environment-references)
5. [Internal Workspace Names](#5-internal-workspace-names)
6. [Hardcoded GUIDs](#6-hardcoded-guids)
7. [Internal Dataset and Table Names](#7-internal-dataset-and-table-names)
8. [Internal OAuth Client ID](#8-internal-oauth-client-id)
9. [Internal Service Accounts and Team Names](#9-internal-service-accounts-and-team-names)
10. [Microsoft Employee Emails](#10-microsoft-employee-emails)
11. [Internal Teams Channel Reference](#11-internal-teams-channel-reference)
12. [Personal GitHub Accounts and Branch Names](#12-personal-github-accounts-and-branch-names)
13. ["Internal" Labels in Issue Templates](#13-internal-labels-in-issue-templates)

---

## 1. SharePoint Links

Personal OneDrive/SharePoint links tied to a Microsoft employee account. Completely inaccessible outside Microsoft.

| File | Line(s) | Content | Action |
|------|---------|---------|--------|
| `docs/README.md` | 17 | `https://microsoft-my.sharepoint.com/:p:/p/cristp/IQAMk2UjpXoHRqh6YXPYdh0lASTthBCKK90RiExuHcsfBkQ?e=LlH489` — "Fabric Skills Creator Guidelines" presentation | Replace with public documentation or remove |
| `docs/README.md` | 18 | `https://microsoft-my.sharepoint.com/:w:/p/cristp/IQAWcfOxwVSYSKsUel3j7V5ZAbUSkh-idunkJ-buXMhDKck?e=VrwpnB` — "AISkillsGuide" Word document | Replace with public documentation or remove |

---

## 2. Internal API Endpoints

The `msitapi.fabric.microsoft.com` domain is a Microsoft-internal (MSIT) endpoint, not the public `api.fabric.microsoft.com`.

| File | Line(s) | Content | Action |
|------|---------|---------|--------|
| `.mcp.json` | 5 | `"url": "https://msitapi.fabric.microsoft.com/v1/mcp/powerbi"` | Replace with public API endpoint or make configurable via environment variable |

---

## 3. Internal GIM Policy Links

`aka.ms/gim/` links resolve to Microsoft-internal GitHub Infrastructure Management documentation.

| File | Line(s) | Content | Action |
|------|---------|---------|--------|
| `.github/acl/access.yml` | 1 | `# Documentation for ACL policy: https://aka.ms/gim/docs/policy/acl` | Replace with public documentation link or remove comment |
| `.github/policies/jit.yml` | 1 | `# Documentation for JIT policy: https://aka.ms/gim/docs/policy/jit` | Replace with public documentation link or remove comment |

---

## 4. MSIT Environment References

References to Microsoft's internal Fabric environment (MSIT) that external users cannot access.

| File | Line(s) | Content | Action |
|------|---------|---------|--------|
| `tests/tests.json` | 4 | `"in my msit fabric, i have a lakehouse in the CristianTest workspace..."` | Replace with generic prompt (e.g., "in my Fabric environment") |
| `tests/tests.json` | 10 | `"in my msit fabric, i have a lakehouse in the CristianTest workspace..."` | Same as above |
| `tests/tests.json` | 16 | `"in my msit fabric, i have a lakehouse in the CristianTest workspace..."` | Same as above |
| `tests/full-eval-tests/executive-summary.md` | 5 | `**Environment:** Microsoft Fabric (MSIT), Starter Pool capacity` | Generalize to "Microsoft Fabric" or note environment is configurable |
| `tests/full-eval-tests/eval-results.md` | 6 | `**Environment:** Microsoft Fabric (MSIT), Starter Pool capacity` | Same as above |
| `tests/full-eval-tests/result/eval-results.md` | 6 | `**Environment:** Microsoft Fabric (MSIT), Starter Pool capacity` | Same as above |
| `tests/full-eval-tests/plan/04-combined-skills/eval-spark-authoring-plus-consumption.md` | 24 | `"(MSIT environments may be slower)"` | Generalize wording |
| `CHANGELOG.md` | 54 | `"Livy endpoints with versioned paths and MSIT authentication"` | Clarify what authentication method is used publicly |

---

## 5. Internal Workspace Names

These reference specific workspaces in Microsoft-internal Fabric environments that external users cannot access.

### In `tests/tests.json`

| Line(s) | Workspace Name | Context |
|---------|---------------|---------|
| 4, 10, 16, 22 | `CristianTest` | Test prompts for SQL DW consumption, Spark, and notebook tests |
| 28, 34 | `FabricCLIDemo` | Test prompts for workspace documentation and PowerBI consumption |
| 40, 46 | `EventhouseFabricSkillTest` | Test prompts for Eventhouse consumption |
| 52 | `FabricCLITest` | Test prompt for Eventhouse authoring |
| 58 | `FabricCLI-PowerBI-Tests` | Test prompt for PowerBI authoring |

### In `prompt_examples/`

| File | Line(s) | Workspace Name | Context |
|------|---------|---------------|---------|
| `prompt_examples/DocumentMyWorkspace.txt` | 1 | `FabricCLIDemo` | Example prompt |
| `prompt_examples/DashboardApp.txt` | 1 | `FabricCLIDemo` | Example prompt |
| `prompt_examples/NYC_AnalyzeExistingDataCreatePDF.txt` | 1 | `FabricCLIDemo` | Example prompt |

### In `tests/full-eval-tests/`

| File | Line(s) | Workspace Name | Context |
|------|---------|---------------|---------|
| `tests/full-eval-tests/plan/00-overview.md` | 31, 216 | `FabricCLITest` | Default `EVAL_WORKSPACE` value |
| `tests/full-eval-tests/plan/03-individual-skills/eval-powerbi-authoring.md` | 11, 20, 53 | `FabricCLI-PowerBI-Tests` | Pre-configured test workspace |
| `tests/full-eval-tests/plan/03-individual-skills/eval-powerbi-consumption.md` | 9, 11, 23 | `FabricCLI-PowerBI-Tests` | Pre-configured test workspace |
| `tests/full-eval-tests/plan/04-combined-skills/eval-powerbi-authoring-plus-consumption.md` | 16, 24 | `FabricCLI-PowerBI-Tests` | Test workspace |
| `tests/full-eval-tests/plan/04-combined-skills/eval-full-pipeline.md.TOO_LONG_TO_RUN` | 35 | `FabricCLITest` | Default workspace |
| `tests/full-eval-tests/result/regression_analysis.md` | 3, 6, 63, 104 | `FabricCLITest` | Test results workspace |

**Action**: Replace all internal workspace names with placeholder names (e.g., `<your-workspace>`) or make them configurable via environment variables.

---

## 6. Hardcoded GUIDs

Workspace and item IDs for specific resources in internal Microsoft Fabric environments.

### Workspace IDs

| File | Line(s) | GUID | Resource |
|------|---------|------|----------|
| `tests/tests.json` | 30 | `bb69f14a-ffa1-4160-b63b-99e60c816ffb` | FabricCLIDemo workspace ID |
| `tests/full-eval-tests/eval-results.md` | 4, 179 | `c92c724b-cca6-4b91-b330-548b482c3800` | skills-for-fabric workspace |
| `tests/full-eval-tests/result/eval-results.md` | 4, 179 | `c92c724b-cca6-4b91-b330-548b482c3800` | skills-for-fabric workspace |
| `tests/full-eval-tests/result/regression_analysis.md` | 3 | `f092f1bd-8c2d-4ac4-bd1b-84226d4bba58` | FabricCLITest workspace |
| `tests/full-eval-tests/result/regression_analysis.md` | 4 | `c92c724b-cca6-4b91-b330-548b482c3800` | Baseline workspace |

### Item/Resource IDs

| File | Line(s) | GUID | Resource |
|------|---------|------|----------|
| `tests/full-eval-tests/eval-results.md` | 57, 180 | `a0e5a3a4-5626-458e-9c18-23f8c0997846` | eval_sales_lh (Lakehouse) |
| `tests/full-eval-tests/eval-results.md` | 58, 184 | `6989ed3d-9d8c-432c-b838-3a65176edf01` | eval_ingest_sales (Notebook) |
| `tests/full-eval-tests/eval-results.md` | 59, 186 | `d2f9d019-a6fb-400a-ad59-d5843c8206eb` | eval-session (Livy session) |
| `tests/full-eval-tests/eval-results.md` | 61, 185 | `12b6769d-1787-4372-8105-6865e4aa2b55` | eval_sales_pipeline (Pipeline) |
| `tests/full-eval-tests/eval-results.md` | 181 | `197101ea-5480-4173-a974-b2f4cf0457f6` | EvalWarehouse (Warehouse) |
| `tests/full-eval-tests/eval-results.md` | 182 | `7dad5ca8-4533-4432-becc-50ec0bc88db4` | EvalEventhouse (Eventhouse) |
| `tests/full-eval-tests/eval-results.md` | 183 | `a9b3d74a-7074-43e8-b793-e150e62d696a` | EvalEventhouse (KQL Database) |
| `tests/full-eval-tests/result/eval-results.md` | 57, 180 | `a0e5a3a4-5626-458e-9c18-23f8c0997846` | eval_sales_lh (Lakehouse) |
| `tests/full-eval-tests/result/eval-results.md` | 58, 184 | `6989ed3d-9d8c-432c-b838-3a65176edf01` | eval_ingest_sales (Notebook) |
| `tests/full-eval-tests/result/eval-results.md` | 59, 186 | `d2f9d019-a6fb-400a-ad59-d5843c8206eb` | eval-session (Livy session) |
| `tests/full-eval-tests/result/eval-results.md` | 61, 185 | `12b6769d-1787-4372-8105-6865e4aa2b55` | eval_sales_pipeline (Pipeline) |
| `tests/full-eval-tests/result/eval-results.md` | 181 | `197101ea-5480-4173-a974-b2f4cf0457f6` | EvalWarehouse (Warehouse) |
| `tests/full-eval-tests/result/eval-results.md` | 182 | `7dad5ca8-4533-4432-becc-50ec0bc88db4` | EvalEventhouse (Eventhouse) |
| `tests/full-eval-tests/result/eval-results.md` | 183 | `a9b3d74a-7074-43e8-b793-e150e62d696a` | EvalEventhouse (KQL Database) |

**Action**: Replace hardcoded GUIDs with placeholders (e.g., `<workspace-id>`) or load from environment variables for tests.

---

## 7. Internal Dataset and Table Names

Names of specific datasets, lakehouses, warehouses, and tables that exist only in internal environments.

| File | Line(s) | Name | Type |
|------|---------|------|------|
| `tests/tests.json` | 4, 10, 16 | `LSEGDemo` | Lakehouse name |
| `tests/tests.json` | 4 | `nyctlc` | Table name |
| `tests/tests.json` | 40, 46 | `RavitEventhouse` | KQL Database name |
| `tests/tests.json` | 40, 46 | `Weather` | KQL Table name |
| `tests/tests.json` | 58 | `nyctaxi_yellow_directlake` | Semantic Model name |
| `tests/tests.json` | 22 | `sparkauthoring_notebook_check` | Notebook name |
| `prompt_examples/DashboardApp.txt` | 1 | `DemoDW` | Warehouse name |
| `prompt_examples/NYC_AnalyzeExistingDataCreatePDF.txt` | 1 | `DemoDW` | Warehouse name |

**Action**: Replace with generic placeholder names or document that users must substitute their own resource names.

---

## 8. Internal OAuth Client ID

Application registration ID that may be specific to an internal Microsoft Entra tenant.

| File | Line(s) | Content | Action |
|------|---------|---------|--------|
| `.mcp.json` | 10 | `"oauthClientId": "aebc6443-996d-45c2-90f0-388ff96faa56"` | Replace with a public/community app registration or make configurable |

---

## 9. Internal Service Accounts and Team Names

### Service Accounts

| File | Line(s) | Content | Action |
|------|---------|---------|--------|
| `.github/ISSUE_TEMPLATE/JitAccess.yml` | 6 | `gimsvc_microsoft` — GIM service account for JIT access | Note: This is part of Microsoft's GitHub governance infrastructure |

### Internal Team Names

| File | Line(s) | Team Name | Role | Action |
|------|---------|-----------|------|--------|
| `.github/acl/access.yml` | 19 | `adfteall` | Pull | These are Microsoft-internal GitHub teams |
| `.github/acl/access.yml` | 21 | `fabricskillsdev` | Write | that external contributors cannot join |
| `.github/acl/access.yml` | 25 | `gbodegasdirects` | Pull | |
| `.github/acl/access.yml` | 27 | `microsoft/all-employees` | Pull | Grants all Microsoft employees Pull access |

### Individual Members in ACL

| File | Line(s) | Username | Role |
|------|---------|----------|------|
| `.github/acl/access.yml` | 9 | `bocrivat` | Maintain |
| `.github/acl/access.yml` | 11 | `cristp` | Maintain |
| `.github/acl/access.yml` | 13 | `saravi` | Maintain |
| `.github/acl/access.yml` | 15 | `jewang` | Maintain |
| `.github/acl/access.yml` | 17 | `evanboyle` | Pull |
| `.github/acl/access.yml` | 23 | `alihamud` | Write |

---

## 10. Microsoft Employee Emails

### SECURITY.md

| Line(s) | Content | Context |
|---------|---------|---------|
| 11 | `Bogdan.Crivat@microsoft.com`, `Santhosh.Ravindran@microsoft.com`, `jewang@microsoft.com`, `cristp@microsoft.com` | Security report recipients |
| 179-182 | Same emails with `@` prefix as "Security Champions" | Maintainer listing |

### SUPPORT.md

| Line(s) | Content | Context |
|---------|---------|---------|
| 55 | `Bogdan.Crivat@microsoft.com` | Direct contact |
| 56 | `Santhosh.Ravindran@microsoft.com` | Direct contact |

### .github/compliance/inventory.yml

| Line(s) | Content |
|---------|---------|
| 4 | `bocrivat@microsoft.com` |
| 5 | `cristp@microsoft.com` |
| 6 | `saravi@microsoft.com` |
| 7 | `jewang@microsoft.com` |
| 8 | `xuancao@microsoft.com` |

### .github/dependabot.yml.disabled

| Line(s) | Content |
|---------|---------|
| 15-16, 33-34, 51-52 | `Bogdan.Crivat@microsoft.com`, `Santhosh.Ravindran@microsoft.com` |

### Plugin Marketplace Files

| File | Line(s) | Content |
|------|---------|---------|
| `.claude-plugin/marketplace.json` | 9 | `bocrivat@microsoft.com` |
| `.github/plugin/marketplace.json` | 9 | `bocrivat@microsoft.com` |

### docs/compliance/ Files

| File | Line(s) | Content |
|------|---------|---------|
| `docs/compliance/REPO_GUARDRAILS.md` | 12-15, 27-30, 46-49, 350-351 | Multiple maintainer `@microsoft.com` emails |
| `docs/compliance/SECURITY_BASELINE.md` | 120, 298, 311 | Maintainer names and emails |
| `docs/compliance/RAI_THREAT_MODEL.md` | 447 | `Bogdan Crivat`, `Santhosh Ravindran` as risk owners |

**Action**: Employee emails in `SECURITY.md` and `SUPPORT.md` are appropriate for a Microsoft open-source project. Review whether emails in compliance/plugin files should be generic aliases instead.

---

## 11. Internal Teams Channel Reference

| File | Line(s) | Content | Action |
|------|---------|---------|--------|
| `SECURITY.md` | 12 | `"Internal Teams channel: skills-for-fabric Security"` | Acceptable in SECURITY.md context; no action needed unless the channel should be public |

---

## 12. Personal GitHub Accounts and Branch Names

References to specific Microsoft employee GitHub usernames and personal branch names.

### GitHub Usernames

| File | Line(s) | Content | Context |
|------|---------|---------|---------|
| `skills/check-updates/SKILL.md` | 59 | `bocrivat_microsoft` | Owner name used for GitHub API calls |
| `skills/check-updates/SKILL.md` | 88 | `get_file_contents(owner: "bocrivat_microsoft", ...)` | Example API call |
| `.claude-plugin/marketplace.json` | 8 | `"name": "bocrivat_microsoft"` | Plugin owner |
| `.github/plugin/marketplace.json` | 8 | `"name": "bocrivat_microsoft"` | Plugin owner |
| `.github/CODEOWNERS` | 6, 9-12 | `@bocrivat_microsoft @saravi_microsoft @jewang_microsoft @cristp_microsoft` | Code ownership |

### Personal Branch Names

| File | Line(s) | Content | Context |
|------|---------|---------|---------|
| `SECURITY.md` | 104 | `"main/bocrivat_main"` | Branch protection reference |
| `docs/compliance/REPO_GUARDRAILS.md` | 115, 239 | `bocrivat_main` | Branch protection configuration |
| `docs/compliance/SECURITY_BASELINE.md` | 125, 298 | `bocrivat_main` | Branch protection status |

**Action**: If the repo is being forked/transferred to a different org, these would all need to be updated to the new owner/branch names.

---

## 13. "Internal" Labels in Issue Templates

| File | Line(s) | Content | Action |
|------|---------|---------|--------|
| `.github/ISSUE_TEMPLATE/config.yml` | 3 | `"Fabric Skills Internal User Guide"` (link name; URL actually points to the public repo) | Consider renaming to remove "Internal" since the URL is public |

---

## Summary by Severity

### 🔴 High Priority — Content is completely inaccessible to external users

| Category | Instance Count | Files Affected |
|----------|---------------|----------------|
| SharePoint links | 2 | 1 |
| Internal API endpoint (msitapi) | 1 | 1 |
| Internal GIM policy links | 2 | 2 |
| Internal OAuth Client ID | 1 | 1 |
| **Subtotal** | **6** | **5** |

### 🟠 Medium Priority — References internal environments that users cannot reproduce

| Category | Instance Count | Files Affected |
|----------|---------------|----------------|
| MSIT environment references | 8 | 6 |
| Internal workspace names | ~25 | 11 |
| Hardcoded GUIDs | ~22 | 5 |
| Internal dataset/table names | ~10 | 3 |
| **Subtotal** | **~65** | **~15** |

### 🟡 Low Priority — Expected in an open-source Microsoft project or cosmetic

| Category | Instance Count | Files Affected |
|----------|---------------|----------------|
| Microsoft employee emails | ~30 | 8 |
| Internal team names / ACL | 6 | 1 |
| Service accounts | 1 | 1 |
| Personal GitHub accounts / branches | ~12 | 6 |
| "Internal" labels | 1 | 1 |
| Internal Teams channel | 1 | 1 |
| **Subtotal** | **~51** | **~14** |

### Grand Total: ~122 instances across ~25 files
