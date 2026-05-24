# Project Genesis Chain

[![version](https://img.shields.io/badge/version-0.1.0-blue)](SKILL.md)
[![status](https://img.shields.io/badge/status-draft-f0ad4e)](SKILL.md)
[![category](https://img.shields.io/badge/category-orchestration-0a7ea4)](SKILL.md)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![repository](https://img.shields.io/badge/repository-private-lightgrey)](#)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jovd83)

`project-genesis-chain` is an AgentSkill chain for creating a new software project from scratch using the existing skill portfolio.

It is inspired by spec-driven development workflows, but it is organized around local agent skills, existing chain definitions, human approval gates, and repository-native validation.

## What It Does

- Captures project intent, constraints, target path, and execution mode.
- Creates a project constitution.
- Generates backlog stories and acceptance criteria.
- Runs requirement clarification and testability review.
- Plans greenfield architecture.
- Produces implementation tasks.
- Bootstraps the repository.
- Implements the first vertical slice.
- Runs validation and hardening passes.
- Prepares release artifacts without publishing by default.

## Chain File

The executable chain lives in:

```text
config/chain_definition.json
```

This file follows the same phase-oriented format used by the existing chain skills in the portfolio.

## Primary Downstream Skills

- `project-constitution-skill`
- `backlog-story-generator`
- `acceptance-criteria-designer`
- `test-analysis-skill`
- `greenfield-architecture-planner`
- `implementation-task-planner-skill`
- `project-bootstrapper-skill`
- `new-feature-sdlc-skill`
- `stack-aware-unit-testing-skill`
- `api-contract-sentinel`
- `playwright-skill`
- `responsive-testing`
- `a11y-audit-agent-skill`
- `automated-test-reviewer`
- `principal-audit-refactor`
- `release-manager-skill`

## Usage

```text
Use $project-genesis-chain to create a new project for a lightweight team task board. Use Angular for the frontend, Spring Boot for the backend, Postgres for persistence, and stop before publishing anything to GitHub.
```

## License

MIT. See [LICENSE](LICENSE).
