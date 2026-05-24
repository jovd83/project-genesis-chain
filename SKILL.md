---
name: project-genesis-chain
description: Orchestrate a complete greenfield software project from a raw idea to a release-ready repository using the existing agent skill portfolio. Use when the user wants to create a new project from scratch, run a spec-driven or SDLC-style project chain, bootstrap a repo, produce specs, plan architecture, generate implementation tasks, build the first slice, verify quality, and prepare release artifacts.
metadata:
  dispatcher-category: orchestration
  dispatcher-layer: execution
  dispatcher-lifecycle: draft
  dispatcher-risk: high
  dispatcher-writes-files: true
  dispatcher-capabilities: greenfield-project-orchestration, project-genesis, spec-to-repo, skill-chain-execution
  dispatcher-accepted-intents: create_project_from_scratch, orchestrate_greenfield_project, run_project_genesis_chain, bootstrap_spec_driven_project
  dispatcher-input-artifacts: product_idea, project_constraints, stack_preference, delivery_constraints
  dispatcher-output-artifacts: project_constitution, product_spec, architecture_plan, implementation_tasks, bootstrapped_repository, verification_summary, release_readiness_report
  dispatcher-stack-tags: orchestration, greenfield, sdlc, spec-driven-development, agent-skills
  dispatcher-downstream-skills: project-constitution-skill, backlog-story-generator, acceptance-criteria-designer, test-analysis-skill, greenfield-architecture-planner, implementation-task-planner-skill, project-bootstrapper-skill, new-feature-sdlc-skill, stack-aware-unit-testing-skill, api-contract-sentinel, playwright-skill, responsive-testing, a11y-audit-agent-skill, automated-test-reviewer, principal-audit-refactor, release-manager-skill
---

# Project Genesis Chain

Use this skill to run a disciplined "project from scratch" chain that makes maximum practical use of the existing agent skill portfolio.

This skill is a chain orchestrator. It does not replace specialist skills. It decides the sequence, keeps the handoff artifacts aligned, and stops at human approval gates before expensive or high-risk work.

## Outcomes

- Turn a raw product idea into a reviewable product specification.
- Create a local project constitution that governs quality, UX, testing, architecture, and release behavior.
- Convert the product specification into backlog stories, acceptance criteria, architecture decisions, implementation tasks, and a bootstrapped repository.
- Build the first useful vertical slice using existing delivery skills.
- Verify the result with the strongest practical evidence.
- Prepare release artifacts without publishing unless the user explicitly asks.

## Do Not Use This Skill For

- Fixing a bug in an existing repository. Use `bug-fix-lifecycle`.
- Refactoring or auditing an existing project only. Use `principal-audit-refactor`.
- Adding one approved feature to an established repository. Use `new-feature-sdlc-skill`.
- Creating only a single framework scaffold with no product, planning, or verification flow.

## Operating Model

0. Log telemetry if the dispatcher logger is available:

```bash
%USERPROFILE%\.agents\skills\skill-dispatcher\log-dispatch.cmd --skill project-genesis-chain --intent create_project_from_scratch --model <model_name> --reason <reason>
```

1. Establish the project request, target folder, and whether the user wants a dry run or full execution.
2. Build or update the project constitution.
3. Generate product specification artifacts.
4. Run clarification and testability analysis before technical planning.
5. Create the architecture plan and task plan.
6. Pause for human approval before repository bootstrap and implementation.
7. Bootstrap the repository using the best available stack-specific skill.
8. Implement the first vertical slice through the SDLC chain or direct specialist skills.
9. Verify with unit, API, UI, responsive, accessibility, design, and automation review where applicable.
10. Prepare release artifacts and stop before publishing unless the user explicitly approves push or release operations.

## Chain Definition

The executable phase list lives in `config/chain_definition.json`. Use that file as the source of truth when a runner can execute chain phases automatically.

## Inputs To Capture

- project name and target directory
- product idea, users, goals, and non-goals
- preferred or prohibited tech stacks
- compliance, security, privacy, accessibility, performance, or deployment constraints
- first vertical slice or MVP boundary
- whether GitHub repositories, commits, pushes, or CI setup are allowed
- artifact preferences such as Markdown only, JSON contracts, diagrams, OpenAPI, or backlog exports

## Artifact Contract

Prefer this project-local structure unless the target repository already establishes a better convention:

```text
.agentspec/
  memory/constitution.md
  chain/project-genesis.json
  routing/skill-map.json
specs/
  001-initial-product/
    product-spec.md
    clarifications.md
    plan.md
    tasks.md
    traceability.json
docs/
  architecture/
  api/
  testing/
  release/
```

## Approval Gates

Pause for explicit user approval after:

- the constitution and product spec are drafted
- architecture and task plans are ready
- repository bootstrap would install dependencies or create a new Git repository
- implementation would start modifying generated source files
- release preparation would commit, push, tag, or publish

## Dispatcher Integration

Prefer dispatching by intent and artifact type. Use direct skill names only as a fallback or when executing the chain definition.

Typical routes:

| Phase Need | Preferred Skill |
| --- | --- |
| governing principles | `project-constitution-skill` |
| epics and stories | `backlog-story-generator` |
| acceptance criteria | `acceptance-criteria-designer` |
| requirement testability | `test-analysis-skill` |
| architecture plan | `greenfield-architecture-planner` |
| implementation task list | `implementation-task-planner-skill` |
| repository bootstrap | `project-bootstrapper-skill` |
| feature delivery | `new-feature-sdlc-skill` |
| test review | `automated-test-reviewer` |
| hardening audit | `principal-audit-refactor` |
| release prep | `release-manager-skill` |

## Guardrails

- Do not skip requirements clarification when the product behavior is materially vague.
- Do not choose a technology stack because it is familiar if the user gave a different constraint.
- Do not invent external integrations, authentication rules, data retention rules, or deployment targets.
- Do not install dependencies, initialize Git, create GitHub repositories, push, tag, or publish without user approval when the surrounding environment requires it.
- Do not report tests, coverage, screenshots, or CI results that were not actually run.
- Do not let planning artifacts drift after implementation changes. Update the relevant spec, plan, tasks, or traceability notes when the implementation pivots.

## Output Expectations

For a dry run, return:

- selected chain path
- planned artifacts
- skill route map
- approval gates
- risks and open questions

For a full run, return:

- project summary
- artifacts created or updated
- repository path
- implementation summary
- verification evidence
- release readiness
- blocked items and follow-up decisions

## Resource Map

- `config/chain_definition.json`: executable chain phases
- `evals/evals.json`: smoke prompts for routing and output quality
