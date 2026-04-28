#!/usr/bin/env python3
"""Block dangerous git commands from Codex PreToolUse hook input."""

from __future__ import annotations

import json
import re
import sys


GIT_PREFIX = r"\bgit(?:\s+(?:-[A-Za-z]|--[A-Za-z0-9-]+)(?:[=\s]\S+)*)*"

DANGEROUS_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("git push", re.compile(GIT_PREFIX + r"\s+push\b", re.IGNORECASE)),
    (
        "git reset --hard",
        re.compile(GIT_PREFIX + r"\s+reset\b(?=.*(?:^|\s)--hard(?:\s|$))", re.IGNORECASE),
    ),
    (
        "git clean -f",
        re.compile(GIT_PREFIX + r"\s+clean\b(?=.*(?:^|\s)-[A-Za-z]*f[A-Za-z]*(?:\s|$))", re.IGNORECASE),
    ),
    (
        "git branch -D",
        re.compile(GIT_PREFIX + r"\s+branch\b(?=.*(?:^|\s)-D(?:\s|$))", re.IGNORECASE),
    ),
    (
        "git checkout .",
        re.compile(GIT_PREFIX + r"\s+checkout\b(?:\s+--)?\s+\.(?:\s|$)", re.IGNORECASE),
    ),
    (
        "git restore .",
        re.compile(GIT_PREFIX + r"\s+restore\b(?:\s+--)?\s+\.(?:\s|$)", re.IGNORECASE),
    ),
]


def read_payload() -> dict:
    try:
        return json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        return {}


def command_from_payload(payload: dict) -> str:
    if payload.get("tool_name") not in (None, "Bash"):
        return ""

    tool_input = payload.get("tool_input")
    if not isinstance(tool_input, dict):
        return ""

    command = tool_input.get("command")
    return command if isinstance(command, str) else ""


def main() -> int:
    command = command_from_payload(read_payload())
    if not command:
        return 0

    for label, pattern in DANGEROUS_PATTERNS:
        if pattern.search(command):
            print(
                f"BLOCKED: '{command}' matches dangerous pattern '{label}'. "
                "The user has prevented Codex from running this git command.",
                file=sys.stderr,
            )
            return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
