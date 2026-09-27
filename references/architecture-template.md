# Architecture Plan: [Project Name]

## Status

- Version: 0.1
- Approval status: draft | approved | blocked
- Source spec: `specs/001-initial-product/product-spec.md`

## Executive Summary

Summarize the selected architecture, why it fits the first vertical slice, and which decisions remain open.

## Context And Constraints

- Product context: [summary]
- Stack constraints: [confirmed or TBD]
- Compliance/security constraints: [confirmed, proposed, unresolved]
- Deployment constraints: [confirmed or TBD]
- Budget/time constraints: [confirmed or TBD]

## Decision Log

| ADR | Decision | Status | Rationale | Revisit Trigger |
| --- | --- | --- | --- | --- |
| ADR-001 | [Decision] | proposed | [Why] | [Trigger] |

## System Boundaries

Describe boundaries between:

- user interface
- application/domain logic
- persistence
- external integrations
- background jobs or async processing
- observability and operations

## Component Model

| Component | Responsibility | Inputs | Outputs | Owner |
| --- | --- | --- | --- | --- |
| [Component] | [Responsibility] | [Input] | [Output] | [team/agent] |

## Data Model

| Entity | Purpose | Key Fields | Sensitive Data | Retention Notes |
| --- | --- | --- | --- | --- |
| [Entity] | [Purpose] | [Fields] | yes/no/TBD | [Notes] |

## API Or Service Boundaries

| Boundary | Consumer | Contract | Auth/Authorization | Validation |
| --- | --- | --- | --- | --- |
| [Endpoint/event/module] | [Consumer] | [Shape] | [Rules] | [Rules] |

## UI Architecture

Describe routes, screens, state ownership, form behavior, accessibility expectations, and responsive surfaces.

## Security And Privacy Posture

- Trust boundaries:
- Authentication:
- Authorization:
- Input validation:
- Secrets management:
- Logging and audit:
- Data minimization:
- Retention/deletion:

## Validation Strategy

| Layer | Purpose | Candidate Tooling | Required Before Release |
| --- | --- | --- | --- |
| Unit/component | [purpose] | [tool] | yes/no |
| API/contract | [purpose] | [tool] | yes/no |
| Browser/E2E | [purpose] | [tool] | yes/no |
| Accessibility | [purpose] | [tool] | yes/no |
| Responsive | [purpose] | [tool] | yes/no |

## Alternatives Considered

| Option | Pros | Cons | Decision |
| --- | --- | --- | --- |
| [Option] | [Pros] | [Cons] | selected/rejected/deferred |

## Open Architecture Questions

| ID | Question | Impact | Required Before |
| --- | --- | --- | --- |
| AQ-001 | [Question] | [Impact] | [gate] |
