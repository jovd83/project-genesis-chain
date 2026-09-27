# Changelog

All notable changes to this repository are documented here. The format follows Keep a Changelog, and the repository uses semantic versioning.

## [1.1.0] - 2026-09-27

### Changed
- `SKILL.md` rewritten around operating modes (dry-run, planning-only, full-run), an execution workflow, skill routing rules, a project artifact contract, a phase output contract and a final response contract.
- `config/chain_definition.json` has 19 phases (was 18), with phase-specific instructions and approval gates after the requirement review (phase 6) and after the task plan (phase 8).
- README rewritten; `evals/evals.json` expanded.
- `disable-model-invocation: true`: the chain runs as a Claude Code agent (`project-genesis`) instead of being picked from its description.
- New "Chain Phases" section, generated from `config/chain_definition.json`: engine phase, skill, gate, and the matching step of this SKILL.md's workflow.
- Phase 9 calls `project-bootstrapper-skill`, the bootstrapper's name again since its 2.0.0.

### Added
- Templates in `references/`: constitution, product spec, architecture, tasks and traceability.
- `scripts/validate_repo.py`, `scripts/grade_evals.py`, `evals/trigger-evals.json` and `agents/openai.yaml`.
- CI workflow `.github/workflows/validate.yml` (`actions/checkout@v7`, `actions/setup-python@v7`) and a `.gitignore`.

## Earlier versions

Up to 1.0.0; see the git history.
