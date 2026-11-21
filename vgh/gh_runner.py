"""Thuc thi lenh GitHub CLI (gh) voi moi truong chuan LC_ALL=C."""

import os
import shutil
import subprocess
from dataclasses import dataclass
from typing import List


@dataclass
class GhResult:
    returncode: int
    stdout: str
    stderr: str
    cmd_str: str

    @property
    def ok(self) -> bool:
        return self.returncode == 0

    @property
    def combined(self) -> str:
        return f"{self.stdout}\n{self.stderr}".strip()


def is_gh_installed() -> bool:
    return shutil.which("gh") is not None


def format_cmd(args: List[str]) -> str:
    parts = ["gh"]
    for arg in args:
        if " " in arg or "\t" in arg or arg == "":
            escaped = arg.replace('"', '\\"')
            parts.append(f'"{escaped}"')
        else:
            parts.append(arg)
    return " ".join(parts)


def run_gh(args: List[str], interactive: bool = False) -> GhResult:
    env = os.environ.copy()
    env["LC_ALL"] = "C"
    env["LANG"] = "C"
    env["GH_PAGER"] = "cat"
    cmd = ["gh", *args]
    cmd_str = format_cmd(args)

    if interactive:
        proc = subprocess.run(cmd, env=env)
        return GhResult(
            returncode=proc.returncode,
            stdout="",
            stderr="",
            cmd_str=cmd_str,
        )

    proc = subprocess.run(
        cmd,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return GhResult(
        returncode=proc.returncode,
        stdout=proc.stdout.strip(),
        stderr=proc.stderr.strip(),
        cmd_str=cmd_str,
    )


def is_git_repo_here() -> bool:
    if shutil.which("git") is None:
        return False
    proc = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        capture_output=True,
        text=True,
    )
    return proc.returncode == 0 and proc.stdout.strip() == "true"
