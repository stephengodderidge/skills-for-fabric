# Internal References Audit

> **Purpose**: This document catalogs every instance across the repository that references documentation, APIs, workspaces, or resources that most people (non-Microsoft employees) do not have access to. Each entry includes the file, line number(s), exact content, and a recommended action.
>
> **Audited against**: `main` branch (rebased 2026-03-31)

---

## Table of Contents

1. [SharePoint Links](#1-sharepoint-links)
2. [Internal GIM Policy Links](#2-internal-gim-policy-links)
3. [MSIT Environment References](#3-msit-environment-references)
4. [Internal Workspace Names in Prompt Examples](#4-internal-workspace-names-in-prompt-examples)
5. [Internal OAuth Client ID](#5-internal-oauth-client-id)
6. [Internal Service Accounts](#6-internal-service-accounts)
7. [Microsoft Employee Emails](#7-microsoft-employee-emails)
8. [Personal GitHub Accounts and Branch Names](#8-personal-github-accounts-and-branch-names)
9. ["Internal" Labels in Issue Templates](#9-internal-labels-in-issue-templates)

---

## Already Fixed on `main` ✅

The following items from the initial sync were **already resolved** before this audit and require no further action:

| Item | Status |
|------|--------|
| `.mcp.json` API endpoint (`msitapi.fabric.microsoft.com`) | ✅ Changed to `api.fabric.microsoft.com` |
| `.github/acl/access.yml` (internal team names, ACL config) | ✅ File removed from `main` |
| `tests/tests.json` (MSIT prompts, internal workspace names, hardcoded GUIDs, internal dataset names) | ✅ File removed from `main` |
| `tests/full-eval-tests/` (eval results with GUIDs, MSIT references, workspace names) | ✅ Files remain but are test artifacts — see note below |

> **Note on `tests/full-eval-tests/`**: These files contain hardcoded workspace names (`FabricCLITest`, `FabricCLI-PowerBI-Tests`), GUIDs, and MSIT references in test result artifacts. They describe past evaluation runs against internal environments. If these are intended to ship as documentation rather than executable tests, they are acceptable as historical records. If they should be reproducible by external users, they need to be parameterized.

---

## 1. SharePoint Links

Personal OneDrive/SharePoint links tied to a Microsoft employee account. Completely inaccessible outside Microsoft.

| File | Line(s) | Content | Action |
|------|---------|---------|--------|
| `docs/README.md` | 17 | `https://microsoft-my.sharepoint.com/:p:/p/cristp/IQAMk2UjpXoHRqh6YXPYdh0lASTthBCKK90RiExuHcsfBkQ?e=LlH489` — "Fabric Skills Creator Guidelines" presentation | Replace with public documentation or remove |
| `docs/README.md` | 18 | `https://microsoft-my.sharepoint.com/:w:/p/cristp/IQAWcfOxwVSYSKsUel3j7V5ZAbUSkh-idunkJ-buXMhDKck?e=VrwpnB` — "AISkillsGuide" Word document | Replace with public documentation or remove |

---

## 2. Internal GIM Policy Links

`aka.ms/gim/` links resolve to Microsoft-internal GitHub Infrastructure Management documentation.

| File | Line(s) | Content | Action |
|------|---------|---------|--------|
| `.github/policies/jit.yml` | 1 | `# Documentation for JIT policy: https://aka.ms/gim/docs/policy/jit` | Replace with public documentation link or remove comment |

---

## 3. MSIT Environment References

A single remaining reference to "MSIT" in the changelog.

| File | Line(s) | Content | Action |
|------|---------|---------|--------|
| `CHANGELOG.md` | 54 | `"Livy endpoints with versioned paths and MSIT authentication"` | Clarify what authentication method is used (e.g., "Azure AD authentication") |

---

## 4. Internal Workspace Names in Prompt Examples

These reference specific workspaces and resources in Microsoft-internal Fabric environments.

| File | Line(s) | Workspace/Resource | Action |
|------|---------|-------------------|--------|
| `prompt_examples/DocumentMyWorkspace.txt` | 1 | `FabricCLIDemo` | Replace with `<your-workspace-name>` or a generic example name |
| `prompt_examples/DashboardApp.txt` | 1 | `DemoDW` warehouse in `FabricCLIDemo` workspace | Same |
| `prompt_examples/NYC_AnalyzeExistingDataCreatePDF.txt` | 1 | `DemoDW` warehouse in `FabricCLIDemo` workspace | Same |

---

## 5. Internal OAuth Client ID

Application registration ID that may be specific to an internal Microsoft Entra tenant.

| File | Line(s) | Content | Action |
|------|---------|---------|--------|
| `.mcp.json` | 10 | `"oauthClientId": "aebc6443-996d-45c2-90f0-388ff96faa56"` | Verify this is a public multi-tenant app registration; if internal-only, replace or make configurable |

---

## 6. Internal Service Accounts

| File | Line(s) | Content | Action |
|------|---------|---------|--------|
| `.github/ISSUE_TEMPLATE/JitAccess.yml` | 6 | `gimsvc_microsoft` — GIM service account for JIT access | Part of Microsoft's GitHub governance; acceptable for Microsoft-owned repos |

---

## 7. Microsoft Employee Emails

### SECURITY.md

| Line(s) | Content | Context |
|---------|---------|---------|
| 11 | `Bogdan.Crivat@microsoft.com`, `Santhosh.Ravindran@microsoft.com`, `jewang@microsoft.com`, `cristp@microsoft.com` | Security report recipients |
| 179-182 | Same emails as "Security Champions" | Maintainer listing |

### SUPPORT.md

| Line(s) | Content | Context |
|---------|---------|---------|
| 55 | `Bogdan.Crivat@microsoft.com` | Direct contact |
| 56 | `Santhosh.Ravindran@microsoft.com` | Direct contact |

### .github/compliance/inventory.yml

| Line(s) | Content |
|---------|---------|
| 4-8 | `bocrivat@microsoft.com`, `cristp@microsoft.com`, `saravi@microsoft.com`, `jewang@microsoft.com`, `xuancao@microsoft.com` |

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

**Action**: Employee emails in `SECURITY.md` and `SUPPORT.md` are standard and appropriate for a Microsoft open-source project. No change required unless the team prefers a shared alias.

---

## 8. Personal GitHub Accounts and Branch Names

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

**Action**: These are correct for the current repo location (`bocrivat_microsoft/skills-for-fabric`). If the repo moves to a different org (e.g., `microsoft/skills-for-fabric`), all of these would need to be updated.

---

## 9. "Internal" Labels in Issue Templates

| File | Line(s) | Content | Action |
|------|---------|---------|--------|
| `.github/ISSUE_TEMPLATE/config.yml` | 3 | `"Fabric Skills Internal User Guide"` (link name; URL actually points to the public repo) | Consider renaming to remove "Internal" since the URL is public |

---

## Summary by Severity

### 🔴 High Priority — Content is completely inaccessible to external users

| Category | Instance Count | Files Affected |
|----------|---------------|----------------|
| SharePoint links | 2 | 1 |
| **Subtotal** | **2** | **1** |

### 🟠 Medium Priority — References internal environments or resources

| Category | Instance Count | Files Affected |
|----------|---------------|----------------|
| Internal workspace names in prompt examples | 3 | 3 |
| MSIT reference in changelog | 1 | 1 |
| Internal GIM policy link | 1 | 1 |
| OAuth Client ID (needs verification) | 1 | 1 |
| **Subtotal** | **6** | **6** |

### 🟡 Low Priority — Expected in a Microsoft open-source project or cosmetic

| Category | Instance Count | Files Affected |
|----------|---------------|----------------|
| Microsoft employee emails | ~25 | 8 |
| Service accounts (GIM) | 1 | 1 |
| Personal GitHub accounts / branches | ~12 | 6 |
| "Internal" label | 1 | 1 |
| **Subtotal** | **~39** | **~14** |

### Grand Total: ~47 instances across ~21 files

> **Compared to pre-sync**: The sync to `main` resolved ~75 instances (removal of `tests/tests.json`, `.github/acl/access.yml`, and the `.mcp.json` endpoint fix).
