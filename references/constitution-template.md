# Project Constitution: [Project Name]

## Status

- Version: 0.1
- Owner: [human owner or team]
- Approval status: draft | approved | superseded
- Last reviewed: [YYYY-MM-DD]

## Purpose

State why this project exists, who it serves, and what outcome the project must make easier, safer, faster, or more reliable.

## Scope Boundaries

### In Scope

- [Confirmed product or engineering scope]

### Out Of Scope

- [Explicit non-goals]

## Operating Principles

### Product

- Prioritize observable user value over internal scaffolding.
- Keep the first vertical slice independently demonstrable.
- Treat assumptions as reviewable decisions, not hidden requirements.

### Architecture

- Keep boundaries explicit between UI, domain logic, persistence, integrations, and infrastructure.
- Prefer reversible decisions until requirements, risk, and usage patterns justify commitment.
- Record meaningful architecture decisions in ADRs or the equivalent project convention.

### Security And Privacy

- Minimize sensitive data collection.
- Protect trust boundaries with validation, authorization, and auditability.
- Do not introduce external services, secrets, telemetry, or data retention behavior without approval.

### Quality And Testing

- Define acceptance criteria before implementation.
- Use repository-native validation commands.
- Report only tests, coverage, screenshots, and CI results that were actually run.

### Accessibility And UX

- Treat accessibility as part of the definition of done for user-facing surfaces.
- Keep workflows efficient, understandable, and recoverable.

### Release Discipline

- Stop before commit, push, tag, publish, deploy, or GitHub release unless explicitly approved.
- Keep release readiness evidence linked to the implementation and verification artifacts.

## Memory Boundaries

### Runtime Memory

Use for temporary chain state, provisional requirements, unresolved questions, and phase evidence.

### Project-Local Memory

Use `.agentspec/memory/` for approved project conventions, assumptions, and decision state that should persist inside this repository only.

### Shared Memory

Promote only stable, broadly useful conventions through an external shared-memory skill or governance boundary. Do not promote project-local notes automatically.

## Approval Gates

Approval is required before:

- writing outside the approved target path
- installing dependencies or downloading templates
- initializing Git, creating remotes, or configuring CI secrets
- implementing source after planning artifacts are drafted
- publishing, deploying, pushing, tagging, or creating a release

## Known Assumptions

| ID | Assumption | Status | Owner | Review Trigger |
| --- | --- | --- | --- | --- |
| ASM-001 | [Assumption] | proposed | [owner] | [event] |

## Change Log

| Date | Change | Reason |
| --- | --- | --- |
| [YYYY-MM-DD] | Initial draft | Project genesis |
