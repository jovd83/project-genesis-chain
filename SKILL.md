---
name: project-genesis-chain
description: Orchestrate approval-gated greenfield software projects from raw idea to release-ready local repository. Use when the user wants to create a new project from scratch, dry-run or execute a spec-driven project chain, produce a project constitution, product spec, backlog, acceptance criteria, architecture, tasks, repository bootstrap plan, first vertical slice, validation evidence, audit, or release-prep artifacts. Trigger for project-from-scratch, spec-to-repo, SDLC chain, MVP bootstrap, planning pack, or new repository creation requests, especially when approval gates, memory boundaries, skill routing, or safe no-publish behavior matter.
disable-model-invocation: true
license: MIT
metadata:
  author: jovd83
  version: "1.1.0"
  dispatcher-category: orchestration
  dispatcher-layer: execution
  dispatcher-lifecycle: active
  dispatcher-risk: high
  dispatcher-writes-files: true
  dispatcher-capabilities: greenfield-project-orchestration, project-genesis, spec-to-repo, approval-gated-delivery, skill-chain-execution
  dispatcher-accepted-intents: create_project_from_scratch, orchestrate_greenfield_project, run_project_genesis_chain, bootstrap_spec_driven_project, dry_run_project_chain
  dispatcher-input-artifacts: product_idea, project_constraints, stack_preference, delivery_constraints, approval_state
  dispatcher-output-artifacts: project_intake, project_constitution, product_spec, backlog_pack, acceptance_criteria, architecture_plan, implementation_tasks, bootstrapped_repository, verification_summary, release_readiness_report
  dispatcher-stack-tags: orchestration, greenfield, sdlc, spec-driven-development, agent-skills
  dispatcher-downstream-skills: backlog-story-generator, acceptance-criteria-designer, test-analysis-skill, project-bootstrapper-skill, new-feature-sdlc-skill, stack-aware-unit-testing-skill, api-contract-sentinel, playwright-skill, responsive-testing, a11y-audit-agent-skill, automated-test-reviewer, principal-audit-refactor, release-manager-skill, codebase-context
---

# Project Genesis Chain

Use this skill to turn a raw software product idea into an approval-gated, locally verifiable project repository. The skill is an orchestrator: it sequences work, preserves handoff artifacts, enforces approval gates, and delegates to specialist skills only when those skills are available and appropriate.

## Compatibility

This skill works in Agent Skills clients that read `SKILL.md`. It can optionally integrate with `skill-dispatcher` and `skill-orchestrator` through `config/chain_definition.json`.

## Core Responsibility

This skill is responsible for:

- clarifying the product intent, target path, constraints, and execution mode
- producing a project constitution, product spec, architecture plan, implementation tasks, and traceability notes
- routing backlog, acceptance-criteria, requirement-analysis, repository-bootstrap, delivery, validation, audit, and release-prep phases to specialist skills when available
- creating agent-handled fallback artifacts for planning phases that do not have a local specialist skill
- stopping before expensive, destructive, networked, publishing, or high-risk actions unless the user explicitly approves them
- reporting only evidence that was actually created, inspected, or run

This skill is not responsible for:

- bug fixing or refactoring an existing project; prefer `bug-fix-lifecycle` or `principal-audit-refactor`
- adding a single feature to an established repository; prefer `new-feature-sdlc-skill`
- creating only a framework scaffold without product, architecture, validation, and release context
- managing cross-agent shared memory inside this repository
- pushing to GitHub, publishing packages, provisioning cloud infrastructure, or creating paid resources without explicit approval

## Operating Modes

Choose the smallest mode that satisfies the user request.

| Mode | Use When | Behavior |
| --- | --- | --- |
| `dry-run` | The user wants the route, artifacts, skills, risks, or approval gates only. | Do not create or modify target project files. Return the planned phases and open questions. |
| `planning-only` | The user wants specs, architecture, tasks, or backlog but not a repository yet. | Create or update planning artifacts, then stop at the bootstrap approval gate. |
| `full-run` | The user asks to create the project repository and implement the first slice. | Execute through approved gates, create files only inside the approved target path, verify, audit, and prepare local release artifacts. |

If the mode is unclear, infer `dry-run` for exploratory phrasing and `planning-only` for product-definition phrasing. Ask one concise clarification before `full-run` when target path, stack, or approval boundaries are missing.

## Execution Workflow

Follow this sequence unless the user explicitly narrows the task.

1. Capture intake: project name, target directory, product idea, users, non-goals, stack preferences, compliance constraints, MVP boundary, execution mode, and approval boundaries.
2. Inspect available skills before dispatching. If a named specialist skill is unavailable, use an agent-handled fallback only for planning artifacts. Do not pretend a specialist ran.
3. Create or update project-local memory and planning artifacts under the target project path, not inside this skill repository unless this repository is the target.
4. Draft the project constitution and product spec. Separate confirmed requirements, assumptions, open questions, and out-of-scope items.
5. Generate backlog and acceptance criteria with specialist skills when available. Preserve traceability to source assumptions and decisions.
6. Run requirement testability analysis before architecture. Stop for human approval if blocking ambiguity remains.
7. Produce the architecture plan and implementation task plan. Stop for approval before repository bootstrap, dependency installation, or source generation.
8. Bootstrap the repository only inside the approved target path through `project-bootstrapper-skill`. Let that skill select stack-specific project creation skills or conservative fallback scaffolds within the approved boundaries.
9. Implement the first vertical slice through `new-feature-sdlc-skill` when appropriate, or directly with repository-native conventions when no delivery skill is available.
10. Verify with the lightest evidence that proves the slice: unit/component tests, API contracts, browser/E2E tests, responsive checks, accessibility review, and automation-quality review where applicable.
11. Run an audit-only hardening pass before release readiness. Do not refactor unless the user approves that separately.
12. Prepare local release artifacts. Stop before commit, push, tag, package publish, cloud deployment, or GitHub release unless explicitly approved.
13. Deliver a final project genesis report grounded in phase evidence.

## Chain Definition

Use `config/chain_definition.json` as the executable phase contract when a runner supports chain execution. The file intentionally names installed or broadly expected specialist skills for required dispatch phases, including `project-bootstrapper-skill` for repository bootstrap. Planning phases that do not have a reliable local specialist are agent-handled (`skill: null`) rather than routed to nonexistent dependencies.

When running manually, follow the same phase order and phase IDs so artifacts, logs, and summaries stay compatible with automated runners.

## Skill Routing Rules

- Prefer intent-based routing through a dispatcher when available.
- Use direct skill names only when the skill is installed and its responsibility clearly matches the phase.
- Mark optional validation phases as `not_applicable` when the project has no relevant surface, such as no API for API-contract validation or no UI for browser testing.
- If a mandatory specialist phase is unavailable and no agent-handled fallback is defined, stop with `blocked` and explain the missing capability.
- Never substitute an unrelated skill just because it is available.

## Project Artifact Contract

Prefer this target-project structure unless the user or repository conventions require a different layout:

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

Keep `traceability.json` small and auditable. It should map product decisions, assumptions, stories, acceptance criteria, tasks, tests, and release notes by stable IDs when practical.

When creating durable planning artifacts, load the relevant template from `references/`:

- `references/constitution-template.md` for `.agentspec/memory/constitution.md`
- `references/product-spec-template.md` for `specs/001-initial-product/product-spec.md`
- `references/architecture-template.md` for `specs/001-initial-product/architecture.md`
- `references/tasks-template.md` for `specs/001-initial-product/tasks.md`
- `references/traceability-template.json` for `specs/001-initial-product/traceability.json`

## Chain Phases

`config/chain_definition.json` is the executable contract: 19 phases, run by `skill-orchestrator/scripts/next_phase.py`. In Claude Code, run the whole chain with the **`project-genesis`** agent (`~/.claude/agents/project-genesis.md`). It stops at each approval gate and returns, and the main conversation resumes it. This SKILL.md stays the reference for the phases and for manual runs in other harnesses.

| # | Phase | Skill | Gate | Workflow step above |
|---|---|---|---|---|
| 1 | `intake` | agent-handled |  | 1. Capture intake |
| 2 | `project_memory` | agent-handled |  | 3-4. Project memory, constitution |
| 3 | `product_spec` | agent-handled |  | 4. Product spec |
| 4 | `backlog` | `backlog-story-generator` |  | 5. Backlog |
| 5 | `acceptance_criteria` | `acceptance-criteria-designer` |  | 5. Acceptance criteria |
| 6 | `requirement_review` | `test-analysis-skill` | **approval gate after** | 6. Testability analysis; approval |
| 7 | `architecture_plan` | agent-handled |  | 7. Architecture plan |
| 8 | `implementation_tasks` | agent-handled | **approval gate after** | 7. Task plan; approval before bootstrap |
| 9 | `repo_bootstrap` | `project-bootstrapper-skill` |  | 8. Bootstrap the repository |
| 10 | `first_slice_delivery` | `new-feature-sdlc-skill` |  | 9. First vertical slice |
| 11 | `unit_validation` (optional) | `stack-aware-unit-testing-skill` |  | 10. Verify |
| 12 | `api_contract_validation` (optional) | `api-contract-sentinel` |  | 10. Verify |
| 13 | `e2e_validation` (optional) | `playwright-skill` |  | 10. Verify |
| 14 | `responsive_validation` (optional) | `responsive-testing` |  | 10. Verify |
| 15 | `accessibility_validation` (optional) | `a11y-audit-agent-skill` |  | 10. Verify |
| 16 | `automation_review` | `automated-test-reviewer` |  | 10. Verify |
| 17 | `hardening_audit` | `principal-audit-refactor` |  | 11. Audit-only hardening |
| 18 | `release_prepare` | `release-manager-skill` |  | 12. Local release artifacts |
| 19 | `genesis_summary` | agent-handled |  | 13. Final report |

## Memory Model

Use memory deliberately and keep the boundaries explicit.

### Runtime Memory

Use runtime memory for the current conversation and current chain execution only:

- provisional requirements
- temporary routing decisions
- unanswered questions
- validation command results
- phase status notes

Do not automatically persist runtime notes.

### Project-Local Memory

Use project-local memory only when it improves repeated work inside the generated project:

- `.agentspec/memory/constitution.md` for stable engineering principles approved by the user
- `.agentspec/memory/assumptions.md` for explicit assumptions and their approval state
- `.agentspec/routing/skill-map.json` for the skills actually used, skipped, unavailable, or replaced by agent-handled fallbacks

Project-local memory is persistent but scoped to one project. Do not promote it automatically to another repository.

### Shared Memory

Treat shared cross-agent memory as an external dependency. If the user asks to reuse a convention across many projects, call or hand off to a dedicated shared-memory skill. Do not embed shared-memory infrastructure in this skill.

## Approval Gates

Pause for explicit approval before:

- persisting planning artifacts when the user requested dry-run only
- creating or modifying files outside the approved target directory
- installing dependencies, downloading templates, or using networked package managers
- initializing Git, creating remotes, configuring CI secrets, or touching credentials
- implementing generated source code after architecture and tasks are drafted
- running expensive, long-lived, paid, or destructive commands
- committing, pushing, tagging, publishing, deploying, or creating a GitHub release

Approval should name the action, target path, and expected side effects. If approval is denied, keep completed planning artifacts intact and summarize what remains blocked.

## Phase Output Contract

Each phase should produce a concise artifact or summary with:

- `phase_id`
- status: `success`, `blocked`, `failed`, `skipped`, or `not_applicable`
- artifacts created or updated
- assumptions introduced or resolved
- risks and open questions
- evidence commands run, with results
- next approval gate, if any

For automated chain runners, include a terminal phase status marker when the runner expects one. Do not mark a phase successful if its required artifact was not produced.

## Final Response Contract

Always include a safety boundary summary when the user constrained execution, requested dry-run behavior, mentioned an existing target directory, or asked for release readiness without execution. Name the actions that were not performed, including tests, server starts, dependency installation, CI inspection, file creation, Git operations, push, publish, deploy, and release actions when relevant.

For `dry-run`, return:

- selected mode
- planned phases
- planned artifacts
- specialist skills to use
- unavailable skills and fallback handling
- approval gates
- risks and open questions

For `planning-only` or `full-run`, return:

- project summary
- target repository path
- artifacts created or updated
- first vertical slice implemented, if any
- verification evidence with commands and results
- audit and release readiness summary
- blocked items and required human decisions

When the target directory already exists or may contain user work, explicitly say that the chain must not overwrite, delete, reset, or assume ownership of existing files. Recommend either read-only inspection with approval or a clean alternate target path before repository bootstrap.

When a `full-run` request has constrained write boundaries, explicitly restate the approved target path, prohibited actions, approval requirements, and the first independently demonstrable vertical slice or MVP before creating any source files.

## Guardrails

- Do not invent requirements, integrations, data retention rules, authentication behavior, deployment targets, or compliance claims.
- Do not skip clarification when missing information would materially change architecture, cost, privacy, security, or user workflow.
- Do not report tests, coverage, screenshots, CI results, or release readiness that were not actually verified.
- Do not let implementation drift away from the spec. Update the relevant spec, task, or traceability artifact when the plan changes.
- Do not overwrite user work in an existing target directory. Inspect first, then propose a merge or choose a clean path.
- Do not use shared memory as a dumping ground for project-local assumptions.
- Do not treat generated planning documents as approval for code changes. Approval gates remain separate.

## Resources

- `config/chain_definition.json`: executable chain phase contract
- `evals/evals.json`: smoke and behavior eval prompts
- `references/*-template.md` and `references/traceability-template.json`: durable planning artifact templates
- `scripts/grade_evals.py`: strict grader for skill-creator eval workspaces
- `scripts/validate_repo.py`: repository validation for SKILL.md, chain config, evals, and packaging basics
