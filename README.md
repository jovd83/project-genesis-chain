# Project Genesis Chain

[![version](https://img.shields.io/badge/version-1.1.0-blue)](SKILL.md)
[![status](https://img.shields.io/badge/status-stable--beta-f0ad4e)](SKILL.md)
[![category](https://img.shields.io/badge/category-orchestration-0a7ea4)](SKILL.md)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)

`project-genesis-chain` is an AgentSkill for creating a new software project from a raw idea through an approval-gated, spec-driven delivery chain. It coordinates intake, project constitution, product specification, backlog, acceptance criteria, architecture, task planning, repository bootstrap, first vertical slice delivery, validation, audit, and release preparation.

It is designed for Agent Skills compatible runtimes and can optionally be executed by a chain runner that understands `config/chain_definition.json`.

## What This Skill Owns

- Orchestrating the greenfield project workflow end to end.
- Creating reviewable planning artifacts before code generation.
- Preserving approval gates before expensive or high-risk actions.
- Delegating to specialist skills when they are available.
- Producing agent-handled fallback artifacts for planning phases that do not have a local specialist.
- Maintaining clear runtime, project-local, and shared-memory boundaries.

## What It Does Not Own

- Fixing bugs or refactoring existing codebases.
- Adding a single feature to an established repository.
- Publishing, pushing, deploying, creating paid resources, or provisioning cloud infrastructure without explicit approval.
- Embedding cross-agent shared-memory infrastructure.
- Guaranteeing that every optional downstream skill exists in a given runtime.

## Install

Clone or copy this folder into an Agent Skills directory:

```bash
git clone <repository-url> project-genesis-chain
cp -R project-genesis-chain ~/.agents/skills/project-genesis-chain
```

For Codex-style skill directories, use the configured skill root for your runtime. The required skill entry point is `SKILL.md`.

## Quick Use

```text
Use $project-genesis-chain to dry-run the project genesis chain for a lightweight team task board. Show the planned artifacts, approval gates, and skills before creating files.
```

```text
Use $project-genesis-chain to create a local project for an AI document classifier. Use Python, FastAPI, and Postgres. Create planning artifacts first, then stop before repository bootstrap for approval.
```

```text
Use $project-genesis-chain to create a small task board app from scratch. Use Angular for the frontend, Spring Boot for the backend, and stop before pushing anything to GitHub.
```

## Execution Modes

| Mode | Purpose | File Changes |
| --- | --- | --- |
| `dry-run` | Route map, artifacts, risks, approval gates, and open questions. | None. |
| `planning-only` | Product spec, backlog, criteria, architecture, tasks, and traceability. | Planning artifacts only. |
| `full-run` | Approved repository bootstrap, first vertical slice, validation, audit, and release prep. | Approved target project path only. |

When the user is exploring, prefer `dry-run`. When source generation or dependency installation would start, ask for explicit approval.

## Chain Overview

The executable phase list lives in [config/chain_definition.json](config/chain_definition.json).

| Phase | Handler |
| --- | --- |
| Intake, constitution, product spec | Agent-handled |
| Backlog | `backlog-story-generator` |
| Acceptance criteria | `acceptance-criteria-designer` |
| Requirement quality review | `test-analysis-skill` |
| Architecture and implementation tasks | Agent-handled |
| Repository bootstrap | `project-bootstrapper-skill` |
| First slice delivery | `new-feature-sdlc-skill` |
| Unit, API, browser, responsive, accessibility validation | Optional specialist skills |
| Automation evidence review | `automated-test-reviewer` |
| Hardening audit | `principal-audit-refactor` in audit-only mode |
| Release prep | `release-manager-skill` without publishing |
| Final summary | Agent-handled |

The chain intentionally avoids required dependencies on unavailable planning skills. Repository bootstrap is delegated to `project-bootstrapper-skill`; where no reliable planning specialist exists, the phase is explicit and agent-handled rather than hidden behind a phantom skill name.

## Artifact Contract

For generated projects, prefer this structure unless the target repository already has a stronger convention:

```text
.agentspec/
  chain/project-genesis.json
  memory/constitution.md
  memory/assumptions.md
  routing/skill-map.json
specs/
  001-initial-product/
    product-spec.md
    clarifications.md
    architecture.md
    tasks.md
    traceability.json
docs/
  architecture/
  api/
  testing/
  release/
```

Planning artifacts should distinguish confirmed requirements, assumptions, open questions, non-goals, risks, and source traceability.

## Memory Model

Runtime memory is temporary working state for the current chain execution.

Project-local memory is stored in the generated project under `.agentspec/` when persistence is useful and approved. It is scoped to one generated project.

Shared memory is out of scope for this repository. If a convention should be reused across many projects or agents, integrate through a dedicated shared-memory skill instead of embedding that infrastructure here.

## Current Implementation

This repository currently provides:

- [SKILL.md](SKILL.md): the AgentSkill instruction contract.
- [config/chain_definition.json](config/chain_definition.json): executable phase contract for compatible runners.
- [evals/evals.json](evals/evals.json): smoke and behavior evaluation prompts.
- [evals/trigger-evals.json](evals/trigger-evals.json): discovery checks for description-trigger accuracy.
- [references/](references): artifact templates for constitution, product spec, architecture, tasks, and traceability.
- [scripts/grade_evals.py](scripts/grade_evals.py): strict grader for skill-creator eval workspaces.
- [scripts/validate_repo.py](scripts/validate_repo.py): local repository validation.
- [agents/openai.yaml](agents/openai.yaml): UI metadata for runtimes that consume it.
- [.github/workflows/validate.yml](.github/workflows/validate.yml): GitHub Actions validation.

## Optional Integrations

These are intentionally external dependencies, not embedded infrastructure:

- `skill-dispatcher` for intent-based routing.
- `skill-orchestrator` for executing `config/chain_definition.json`.
- `project-bootstrapper-skill` for the approval-gated repository skeleton phase.
- Stack-specific project creation skills such as Angular, React, Java, Python, or API specialists, usually selected inside the bootstrapper.
- A shared-memory skill for durable cross-project conventions.
- GitHub tooling for repository creation, pull requests, and releases after explicit approval.

## Future Ideas

The following are conceptual and not implemented in this repository:

- A dynamic skill-availability scanner that rewrites phase routing for a specific runtime.
- Project templates for common stacks.
- A generated reviewer UI for comparing dry-run plans.
- Formal benchmark scoring beyond the smoke evals.

These should be added only when they reduce repeated work or improve reliability in real usage.

## Validate

Run the local validation script:

```bash
python scripts/validate_repo.py
```

The validator checks skill metadata, chain phase structure, eval shape, UI metadata, and basic GitHub packaging files.
It also guards the regression eval suite so it continues to cover unavailable-skill fallback, memory-boundary promotion, approval gates, evidence honesty, regulated-product ambiguity, and existing-directory safety.

You can also run the Agent Skills quick validator if available:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

For benchmark iterations created with `skill-creator`, grade all runs with:

```bash
python scripts/grade_evals.py .eval-workspace/iteration-N
```

## Contributing

Keep changes aligned with the core contract:

- Make required phases executable or explicitly agent-handled.
- Do not add required downstream skills unless they are real, documented, and broadly installable.
- Keep approval gates visible and conservative.
- Add eval prompts when behavior changes.
- Run `python scripts/validate_repo.py` before opening a pull request.

## License

MIT. See [LICENSE](LICENSE).
