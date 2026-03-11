#!/usr/bin/env python3
"""Create a Git worktree for a selected local branch."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


def _run_git(*args: str) -> str:
    """Run a git command and return stdout as text."""
    result = subprocess.run(
        ["git", *args],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def _resolve_post_command(post_command_choice: str) -> str | None:
    """Resolve post-command from LazyGit prompt values.

    Args:
        post_command_choice (str): One of default or nothing.

    Returns:
        str | None: Command to run, or None to skip.
    """
    normalized_choice = post_command_choice.strip().lower()
    if normalized_choice == "default":
        return "uv sync --dev"
    if normalized_choice == "nothing":
        return None

    print(
        f"Unknown post-command option '{post_command_choice}'. "
        "Falling back to default: uv sync --dev"
    )
    return "uv sync --dev"


def _should_open_worktree(open_worktree_raw: str) -> bool:
    """Parse LazyGit confirm value into a boolean.

    Args:
        open_worktree_raw (str): Confirm prompt value from LazyGit.

    Returns:
        bool: True if the worktree should be opened.
    """
    return open_worktree_raw.strip().lower() in {"true", "y", "yes", "1"}


def _run_post_command(command: str, cwd: Path) -> int:
    """Run a post-worktree command in the new worktree directory.

    Args:
        command (str): Shell command to run.
        cwd (Path): Worktree path where command is executed.

    Returns:
        int: Exit code from the command.
    """
    print(f"Running post-command in {cwd}: {command}")
    result = subprocess.run(command, cwd=str(cwd), shell=True)
    return result.returncode


def _open_worktree(path: Path) -> int:
    """Open the worktree in VS Code using subprocess.

    Args:
        path (Path): Worktree path to open.

    Returns:
        int: Exit code from opening command.
    """
    code_candidates: list[str] = []

    code_in_path = shutil.which("code") or shutil.which("code.cmd")
    if code_in_path:
        code_candidates.append(code_in_path)

    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        code_candidates.append(
            str(
                Path(local_app_data)
                / "Programs"
                / "Microsoft VS Code"
                / "bin"
                / "code.cmd"
            )
        )

    program_files = os.environ.get("ProgramFiles")
    if program_files:
        code_candidates.append(
            str(Path(program_files) / "Microsoft VS Code" / "bin" / "code.cmd")
        )

    for candidate in code_candidates:
        if not Path(candidate).exists():
            continue
        result = subprocess.run([candidate, str(path)], check=False)
        if result.returncode == 0:
            return 0

    # Fallback so user still gets the folder opened even if VS Code CLI is unavailable.
    if os.name == "nt":
        os.startfile(str(path))  # type: ignore[attr-defined]
        return 0

    print(
        "Could not locate VS Code command. Install the 'code' shell command and retry.",
        file=sys.stderr,
    )
    return 1


def main() -> int:
    """Create ../{repo_name}-wt/{branch} and check out that branch there."""
    if len(sys.argv) != 4:
        print(
            "Usage: uv run create_worktree.py "
            "<local-branch-name> <post-command-option>",
            file=sys.stderr,
        )
        return 2

    selected_branch = sys.argv[1].strip()
    post_command_choice = sys.argv[2]
    open_worktree_raw = sys.argv[3]

    if not selected_branch:
        print("Error: branch name cannot be empty.", file=sys.stderr)
        return 2

    try:
        repo_root = Path(_run_git("rev-parse", "--show-toplevel"))
        repo_name = repo_root.name

        target_path = repo_root.parent / f"{repo_name}-wt" / selected_branch
        target_path.parent.mkdir(parents=True, exist_ok=True)

        subprocess.run(
            ["git", "worktree", "add", str(target_path), "--", selected_branch],
            check=True,
        )

        print(f"Created worktree: {target_path}")
        print(f"Checked out branch: {selected_branch}")

        post_command = _resolve_post_command(post_command_choice)
        if post_command is not None:
            post_code = _run_post_command(post_command, target_path)
            if post_code != 0:
                print(
                    f"Post-command failed with exit code {post_code}.",
                    file=sys.stderr,
                )
                return post_code

        if _should_open_worktree(open_worktree_raw):
            open_code = _open_worktree(target_path)
            if open_code != 0:
                print(
                    f"Failed to open worktree (exit code {open_code}).",
                    file=sys.stderr,
                )
                return open_code

        return 0
    except subprocess.CalledProcessError as exc:
        if exc.stderr:
            print(exc.stderr.strip(), file=sys.stderr)
        elif exc.stdout:
            print(exc.stdout.strip(), file=sys.stderr)
        return exc.returncode or 1


if __name__ == "__main__":
    raise SystemExit(main())
