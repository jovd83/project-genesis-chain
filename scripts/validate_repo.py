#!/usr/bin/env python3
"""Validate the project-genesis-chain skill repository.

The checks are intentionally dependency-free so they can run in CI and in
minimal Agent Skills environments.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}[a-z0-9]$")
PHASE_ID_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")
ALLOWED_RISKS = {"low", "medium", "high"}
REQUIRED_PHASE_KEYS = {
    "id",
    "name",
    "skill",
    "intent",
    "reason",
    "risk",
    "mandatory",
    "pass_context_forward",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def read_text(path: Path, errors: list[str]) -> str:
    if not path.exists():
        fail(errors, f"missing required file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(read_text(path, errors))
    except json.JSONDecodeError as exc:
        fail(errors, f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return None


def parse_frontmatter(skill_text: str, errors: list[str]) -> dict[str, str]:
    if not skill_text.startswith("---\n"):
        fail(errors, "SKILL.md must start with YAML frontmatter")
        return {}

    end = skill_text.find("\n---\n", 4)
    if end == -1:
        fail(errors, "SKILL.md frontmatter must close with ---")
        return {}

    frontmatter = skill_text[4:end]
    values: dict[str, str] = {}
    for line in frontmatter.splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"')
    return values


def validate_skill_md(errors: list[str]) -> str:
    text = read_text(ROOT / "SKILL.md", errors)
    if not text:
        return ""

    frontmatter = parse_frontmatter(text, errors)
    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")

    if not name:
        fail(errors, "SKILL.md frontmatter must include name")
    elif not SKILL_NAME_PATTERN.match(name):
        fail(errors, f"skill name is not valid hyphen-case: {name}")
    elif name != ROOT.name:
        fail(errors, f"skill name '{name}' must match folder name '{ROOT.name}'")

    if not description:
        fail(errors, "SKILL.md frontmatter must include description")
    elif len(description) > 900:
        fail(errors, "SKILL.md description should stay under 900 characters")
    elif "Use when" not in description:
        fail(errors, "SKILL.md description should include trigger guidance using 'Use when'")

    required_sections = [
        "## Operating Modes",
        "## Execution Workflow",
        "## Project Artifact Contract",
        "## Memory Model",
        "## Approval Gates",
        "## Guardrails",
    ]
    for section in required_sections:
        if section not in text:
            fail(errors, f"SKILL.md missing section: {section}")

    return name


def validate_chain(skill_name: str, errors: list[str]) -> None:
    chain = load_json(ROOT / "config" / "chain_definition.json", errors)
    if not isinstance(chain, dict):
        return

    if chain.get("chain_name") != skill_name:
        fail(errors, "chain_definition.json chain_name must match SKILL.md name")

    phases = chain.get("phases")
    if not isinstance(phases, list) or not phases:
        fail(errors, "chain_definition.json must contain a non-empty phases array")
        return

    seen_ids: set[str] = set()
    hitl_count = 0
    for index, phase in enumerate(phases):
        label = f"phase[{index}]"
        if not isinstance(phase, dict):
            fail(errors, f"{label} must be an object")
            continue

        missing = sorted(REQUIRED_PHASE_KEYS - phase.keys())
        if missing:
            fail(errors, f"{label} missing required keys: {', '.join(missing)}")

        phase_id = phase.get("id")
        if not isinstance(phase_id, str) or not PHASE_ID_PATTERN.match(phase_id):
            fail(errors, f"{label} has invalid id: {phase_id!r}")
        elif phase_id in seen_ids:
            fail(errors, f"duplicate phase id: {phase_id}")
        else:
            seen_ids.add(phase_id)

        risk = phase.get("risk")
        if risk not in ALLOWED_RISKS:
            fail(errors, f"{label} has invalid risk: {risk!r}")

        if not isinstance(phase.get("mandatory"), bool):
            fail(errors, f"{label} mandatory must be boolean")
        if not isinstance(phase.get("pass_context_forward"), bool):
            fail(errors, f"{label} pass_context_forward must be boolean")

        skill = phase.get("skill")
        if skill is not None and not isinstance(skill, str):
            fail(errors, f"{label} skill must be null or string")
        if skill is None and not phase.get("query_suffix"):
            fail(errors, f"{label} is agent-handled and should include query_suffix guidance")

        if phase.get("on_phase_complete") == "hitl":
            hitl_count += 1
            if not phase.get("_hitl_note"):
                fail(errors, f"{label} has a HITL gate without _hitl_note")

    if hitl_count < 2:
        fail(errors, "chain should include at least two explicit human approval gates")


def validate_evals(skill_name: str, errors: list[str]) -> None:
    evals = load_json(ROOT / "evals" / "evals.json", errors)
    if not isinstance(evals, dict):
        return

    if evals.get("skill_name") != skill_name:
        fail(errors, "evals.json skill_name must match SKILL.md name")

    cases = evals.get("evals")
    if not isinstance(cases, list) or len(cases) < 6:
        fail(errors, "evals.json should contain at least six eval cases")
        return

    ids: set[str] = set()
    for index, case in enumerate(cases):
        label = f"evals[{index}]"
        if not isinstance(case, dict):
            fail(errors, f"{label} must be an object")
            continue

        case_id = str(case.get("id", ""))
        if not case_id:
            fail(errors, f"{label} missing id")
        elif case_id in ids:
            fail(errors, f"duplicate eval id: {case_id}")
        else:
            ids.add(case_id)

        for key in ("prompt", "expected_output"):
            if not isinstance(case.get(key), str) or not case[key].strip():
                fail(errors, f"{label} missing non-empty {key}")

        if not isinstance(case.get("files", []), list):
            fail(errors, f"{label} files must be an array")

        expectations = case.get("expectations", [])
        if expectations and not isinstance(expectations, list):
            fail(errors, f"{label} expectations must be an array when present")
        elif len(expectations) < 4:
            fail(errors, f"{label} should include at least four discriminating expectations")

    required_eval_ids = {
        "unavailable-planning-skills",
        "memory-boundary-promotion",
        "full-run-approval-boundaries",
        "ambiguous-regulated-product",
        "evidence-honesty",
        "existing-directory-collision",
    }
    missing_required = sorted(required_eval_ids - ids)
    if missing_required:
        fail(errors, f"evals.json missing required regression evals: {', '.join(missing_required)}")


def validate_trigger_evals(errors: list[str]) -> None:
    trigger_evals = load_json(ROOT / "evals" / "trigger-evals.json", errors)
    if not isinstance(trigger_evals, list):
        fail(errors, "trigger-evals.json must contain a JSON array")
        return

    if len(trigger_evals) < 16:
        fail(errors, "trigger-evals.json should contain at least 16 trigger eval queries")

    positive = 0
    negative = 0
    for index, item in enumerate(trigger_evals):
        label = f"trigger-evals[{index}]"
        if not isinstance(item, dict):
            fail(errors, f"{label} must be an object")
            continue

        query = item.get("query")
        should_trigger = item.get("should_trigger")
        if not isinstance(query, str) or len(query.strip()) < 40:
            fail(errors, f"{label} query should be a realistic non-empty prompt")
        if not isinstance(should_trigger, bool):
            fail(errors, f"{label} should_trigger must be boolean")
        elif should_trigger:
            positive += 1
        else:
            negative += 1

    if positive < 8 or negative < 8:
        fail(errors, "trigger-evals.json should include at least eight positive and eight negative cases")


def validate_packaging(skill_name: str, errors: list[str]) -> None:
    read_text(ROOT / "README.md", errors)
    read_text(ROOT / "LICENSE", errors)

    for template in (
        "references/constitution-template.md",
        "references/product-spec-template.md",
        "references/architecture-template.md",
        "references/tasks-template.md",
        "references/traceability-template.json",
    ):
        read_text(ROOT / template, errors)

    grader = read_text(ROOT / "scripts" / "grade_evals.py", errors)
    if grader and not all(field in grader for field in ("text", "passed", "evidence")):
        fail(errors, "scripts/grade_evals.py should write viewer-compatible expectation fields")

    openai_yaml = read_text(ROOT / "agents" / "openai.yaml", errors)
    if openai_yaml:
        if f"${skill_name}" not in openai_yaml:
            fail(errors, "agents/openai.yaml default_prompt should mention the skill as $skill-name")
        for required in ("display_name:", "short_description:", "default_prompt:"):
            if required not in openai_yaml:
                fail(errors, f"agents/openai.yaml missing {required}")

    workflow = read_text(ROOT / ".github" / "workflows" / "validate.yml", errors)
    if workflow and "scripts/validate_repo.py" not in workflow:
        fail(errors, "GitHub workflow should run scripts/validate_repo.py")


def main() -> int:
    errors: list[str] = []
    skill_name = validate_skill_md(errors)
    if skill_name:
        validate_chain(skill_name, errors)
        validate_evals(skill_name, errors)
        validate_trigger_evals(errors)
        validate_packaging(skill_name, errors)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed: project-genesis-chain repository is structurally sound.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
