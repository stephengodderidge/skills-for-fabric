---
name: powerbi-semantic-model-authoring-cli
description: >
  Create, manage, and deploy Power BI semantic models in Microsoft Fabric with
  the Fabric Items API, Power BI REST APIs, TMDL, and `az rest`. Covers full
  definition lifecycle, refresh, data sources, parameters, permissions, role
  memberships, and deployment pipelines. Route read-only DAX queries to
  `powerbi-consumption-cli` and fine-grained object edits to
  `powerbi-modeling-mcp`. Triggers: "create semantic model", "upload TMDL",
  "download semantic model TMDL", "refresh dataset", "semantic model deployment
  pipeline", "dataset permissions", "list dataset users", "semantic model authoring".
---

> **Update Check — ONCE PER SESSION (mandatory)**
> The first time this skill is used in a session, run the **check-updates** skill before proceeding.
> - **GitHub Copilot CLI / VS Code**: invoke the `check-updates` skill (e.g., `/fabric-skills:check-updates`).
> - **Claude Code / Cowork / Cursor / Windsurf / Codex**: read the local `package.json` version, then compare it against the remote version via `git fetch origin main --quiet && git show origin/main:package.json` (or the GitHub API). If the remote version is newer, show the changelog and update instructions.
> - Skip if the check was already performed earlier in this session.

> **CRITICAL NOTES**
> 1. To find the workspace details (including its ID) from workspace name: list all workspaces and, then, use JMESPath filtering
> 2. To find the item details (including its ID) from workspace ID, item type, and item name: list all items of that type in that workspace and, then, use JMESPath filtering

# Power BI Semantic Model Authoring — CLI Skill

Use this file for routing, guardrails, and workflow. Load detailed reference
sections only when needed.

## References

| Need | Read |
|---|---|
| Workspace/item discovery, authentication, LROs | [COMMON-CLI.md](../../common/COMMON-CLI.md) |
| Definition envelope and required parts | [ITEM-DEFINITIONS-CORE.md § SemanticModel](../../common/ITEM-DEFINITIONS-CORE.md#semanticmodel) |
| TMDL syntax and modeling practices | [TMDL authoring guide](./references/tmdl-authoring-guide.md) |
| Calculation groups, roles, cultures, perspectives | [Advanced TMDL guide](./references/tmdl-advanced-features-guide.md) |
| Property/API mapping | [Semantic model properties guide](./references/semantic-model-properties-guide.md) |
| Create, download, update, refresh, permissions, and deployment recipes | [CLI operations guide](./cli-operations-guide.md) |
| Read-only DAX validation | [powerbi-consumption-cli](../powerbi-consumption-cli/SKILL.md) |

## Routing

1. Use `powerbi-modeling-mcp` for individual measures, columns, relationships,
   and other fine-grained model edits.
2. Use this skill and the Fabric Items API for complete definition create,
   download, update, and deployment operations.
3. Use the Power BI REST API for refresh, data sources, parameters, permissions,
   role memberships, and deployment pipelines.
4. Use `powerbi-consumption-cli` for read-only metadata and DAX validation.

## API Audiences

| API | Audience (`--resource`) | Use |
|---|---|---|
| Fabric Items API | `https://api.fabric.microsoft.com` | Definition CRUD and LRO polling |
| Power BI REST API | `https://analysis.windows.net/powerbi/api` | Refresh and operational management |

## Must

- Read the relevant TMDL reference before generating TMDL; do not generate it
  from memory.
- Resolve workspace and item IDs dynamically using list operations and JMESPath.
- Pass the correct `--resource` audience to every `az rest` call.
- Send `Content-Type=application/json` for Power BI API requests with bodies.
- Base64-encode every definition part payload.
- For `updateDefinition`, retrieve the current definition first and send every
  modified and unmodified part; the operation replaces the complete definition.
- Exclude `.platform` from definition update payloads.
- Poll every `202 Accepted` long-running operation to a terminal state.
- Verify the target workspace has a capacity before creating a model.
- Validate successful changes with definition retrieval and, where applicable,
  a read-only DAX query.

## Prefer

- Use `createItemWithDefinition` for new models.
- Use TMDL rather than TMSL for source-controlled definitions.
- Route small modeling changes to `powerbi-modeling-mcp`.
- Keep the downloaded definition as the source for updates to avoid deleting
  parts or overwriting concurrent changes.
- Load only the relevant section of the CLI operations guide.

## Avoid

- Hardcoded workspace, item, tenant, or capacity IDs.
- Full `updateDefinition` round trips for isolated object edits.
- Partial definition payloads.
- Manually assigned `lineageTag` values on new objects.
- `//` comments or `description` properties in TMDL; use `///` descriptions.
- Report creation, which requires PBIR/PBIR-Legacy rather than this skill.

## Workflow

1. Run the session update check.
2. Discover the workspace by name and verify its capacity.
3. Discover the semantic model by name when operating on an existing item.
4. Choose the API/tool using the routing rules above.
5. Read the relevant syntax or operation reference section.
6. Acquire a token for the exact API audience.
7. Retrieve the current definition before any full-definition update.
8. Execute the operation and poll long-running work to completion.
9. Retrieve state again to verify the change.
10. Route to `powerbi-consumption-cli` for DAX validation when appropriate.

## Troubleshooting

| Symptom | Check |
|---|---|
| `401` | Token audience matches the API host |
| `400` on definition update | All parts included, payloads base64 encoded, `.platform` excluded |
| `202` never completes | Poll the `Operation-Id` URL and inspect terminal error details |
| Refresh fails | Data-source credentials and gateway binding |
| TMDL parse error | Tabs, quoted names, object references, and required files |

## Examples

- **Create or replace a complete model:** read
  [Create Semantic Model](./cli-operations-guide.md#create-semantic-model) and
  the required TMDL syntax sections first.
- **Change one measure:** route to `powerbi-modeling-mcp`; do not download and
  replace the full definition.
- **Validate a deployment:** retrieve the deployed definition, inspect refresh
  status, then route a read-only DAX query to `powerbi-consumption-cli`.
