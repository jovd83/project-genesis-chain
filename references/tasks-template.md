# Implementation Tasks: [Project Name]

## Status

- Version: 0.1
- Approval status: draft | approved | blocked
- Source spec: `specs/001-initial-product/product-spec.md`
- Source architecture: `specs/001-initial-product/architecture.md`

## Task Rules

- Keep tasks independently reviewable.
- Link each task to a requirement, story, acceptance criterion, or architecture decision.
- Stop before install, Git, publish, deploy, or out-of-path writes unless explicitly approved.
- Mark tasks blocked when required decisions are unresolved.

## First Vertical Slice

Describe the smallest demonstrable slice and its acceptance boundary.

## Ordered Task List

| ID | Task | Type | Depends On | Traceability | Validation | Status |
| --- | --- | --- | --- | --- | --- | --- |
| T-001 | [Task] | planning/code/test/docs/release | [IDs] | [FR/AC/ADR IDs] | [command/review] | proposed |

## Approval-Sensitive Tasks

| ID | Action | Why Approval Is Required | Approval State |
| --- | --- | --- | --- |
| GATE-001 | [Install dependency / initialize Git / write path / publish] | [Reason] | pending |

## Validation Commands

| Command | Purpose | When To Run | Status |
| --- | --- | --- | --- |
| `[command]` | [Purpose] | [phase] | planned |

## Traceability Checklist

- [ ] Every task links to at least one source requirement, acceptance criterion, or architecture decision.
- [ ] Every high-risk requirement has a validation task.
- [ ] Every approval-sensitive operation has a gate.
- [ ] Out-of-scope work is explicitly deferred.

## Deferred Work

| ID | Deferred Item | Reason | Revisit Trigger |
| --- | --- | --- | --- |
| D-001 | [Item] | [Reason] | [Trigger] |
