"""Entry point cho lenh `vgh`."""

import sys
from typing import List, Optional

from . import __version__, commands, gh_runner, ui


def main(argv: Optional[List[str]] = None) -> int:
    ui.enable_windows_ansi()
    args = sys.argv[1:] if argv is None else argv

    if not args:
        return commands.cmd_huongdan([])

    if args[0] in ("-v", "--version", "phienban"):
        print(f"vgh phien ban {__version__}")
        return 0

    if not gh_runner.is_gh_installed():
        ui.error("May ban chua cai dat GitHub CLI (gh)!")
        ui.info("Hay cai tai: https://cli.github.com (hoac go 'winget install GitHub.cli' tren Windows).")
        return 1

    cmd_name = args[0].lower()
    rest = args[1:]

    handler = commands.COMMAND_MAP.get(cmd_name)
    if handler is not None:
        return handler(rest)

    # Pass-through: chuyen thang sang gh goc
    res = gh_runner.run_gh(args, interactive=True)
    return res.returncode


if __name__ == "__main__":
    sys.exit(main())
