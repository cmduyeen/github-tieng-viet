"""Cai dat cac lenh Viet hoa cho GitHub CLI (vgh)."""

from typing import Callable, Dict, List

from . import config, error_translator, gh_runner, ui


def _bridge_enabled() -> bool:
    return bool(config.load_config().get("bridge_mode", True))


def cmd_dangnhap(args: List[str]) -> int:
    """Dang nhap vao tai khoan GitHub (gh auth login)."""
    ui.info("Huong dan nhanh khi dang nhap:")
    print("  1. Chon: GitHub.com")
    print("  2. Chon: HTTPS")
    print("  3. Chon: Login with a web browser (dang nhap qua trinh duyet)")
    print()
    res = gh_runner.run_gh(["auth", "login", *args], interactive=True)
    if res.ok:
        ui.success("Dang nhap GitHub thanh cong!")
        ui.show_bridge(res.cmd_str, _bridge_enabled())
    return res.returncode


def cmd_taikhoan(args: List[str]) -> int:
    """Xem tai khoan GitHub dang dang nhap (gh auth status)."""
    res = gh_runner.run_gh(["auth", "status", *args])
    if not res.ok:
        error_translator.translate_and_print_error(res)
        return res.returncode

    if res.stdout:
        print(res.stdout)
    elif res.stderr:
        print(res.stderr)
    ui.show_bridge(res.cmd_str, _bridge_enabled())
    return 0


def cmd_taorepo(args: List[str]) -> int:
    """Tao du an (repository) moi tren GitHub (gh repo create)."""
    name = ""
    visibility_flag = ""

    for arg in args:
        low = arg.lower()
        if low in ("congkhai", "--public", "public"):
            visibility_flag = "--public"
        elif low in ("riengtu", "--private", "private"):
            visibility_flag = "--private"
        elif not name and not arg.startswith("-"):
            name = arg

    if not name:
        name = ui.ask_text("Dat ten cho du an moi tren GitHub (vd: game-ran-san-moi)")
        if not name:
            ui.error("Chua co ten du an.")
            return 1

    if not visibility_flag:
        is_public = ui.ask_yes_no("Ban muon du an nay CONG KHAI (ai cung xem duoc) hay khong? (chon 'k' de de Rieng tu)", default=True)
        visibility_flag = "--public" if is_public else "--private"

    gh_args = ["repo", "create", name, visibility_flag]

    if gh_runner.is_git_repo_here():
        if ui.ask_yes_no("Thu muc nay da co san code Git. Day code len luon khong?", default=True):
            gh_args.extend(["--source=.", "--remote=origin", "--push"])
    else:
        if ui.ask_yes_no("Tai thu muc du an moi nay ve may luon khong?", default=True):
            gh_args.append("--clone")

    ui.info(f"Dang tao du an '{name}' tren GitHub...")
    res = gh_runner.run_gh(gh_args)
    if not res.ok:
        error_translator.translate_and_print_error(res)
        return res.returncode

    if res.stdout:
        print(res.stdout)
    ui.success(f"Da tao du an '{name}' tren GitHub thanh cong!")
    ui.show_bridge(res.cmd_str, _bridge_enabled())
    return 0


def cmd_tai(args: List[str]) -> int:
    """Tai du an tu GitHub ve may theo ten 'tac-gia/ten-repo' (gh repo clone)."""
    if not args:
        repo = ui.ask_text("Nhap ten du an can tai (vd: ten-ban/du-an)")
        if not repo:
            ui.error("Chua nhap ten du an.")
            return 1
        args = [repo]

    ui.info("Dang tai du an tu GitHub...")
    res = gh_runner.run_gh(["repo", "clone", *args])
    if not res.ok:
        error_translator.translate_and_print_error(res)
        return res.returncode

    ui.success("Tai du an thanh cong!")
    ui.show_bridge(res.cmd_str, _bridge_enabled())
    return 0


def cmd_fork(args: List[str]) -> int:
    """Sao chep (fork) du an cua nguoi khac ve tai khoan minh."""
    if not args:
        repo = ui.ask_text("Nhap ten du an muon sao chep (vd: tac-gia/ten-repo)")
        if not repo:
            ui.error("Chua nhap ten du an.")
            return 1
        args = [repo]

    res = gh_runner.run_gh(["repo", "fork", args[0], "--clone"])
    if not res.ok:
        error_translator.translate_and_print_error(res)
        return res.returncode

    if res.stdout:
        print(res.stdout)
    ui.success("Da sao chep du an ve tai khoan cua ban va tai ve may!")
    ui.show_bridge(res.cmd_str, _bridge_enabled())
    return 0


def cmd_mo(args: List[str]) -> int:
    """Mo trang GitHub cua du an hien tai tren trinh duyet (gh browse)."""
    res = gh_runner.run_gh(["browse", *args])
    if not res.ok:
        error_translator.translate_and_print_error(res)
        return res.returncode
    ui.success("Da mo du an tren trinh duyet web!")
    ui.show_bridge(res.cmd_str, _bridge_enabled())
    return 0


def cmd_pr(args: List[str]) -> int:
    """Quan ly Pull Request: xem, tao, gop."""
    sub = args[0].lower() if args else "xem"
    rest = args[1:]

    if sub in ("xem", "list"):
        res = gh_runner.run_gh(["pr", "list", "--limit", "10", *rest])
        if not res.ok:
            error_translator.translate_and_print_error(res)
            return res.returncode
        if not res.stdout:
            ui.info("Hien khong co Pull Request nao dang mo.")
        else:
            print(ui.paint("Cac Pull Request dang mo:", ui.Color.CYAN, ui.Color.BOLD))
            print(res.stdout)
        ui.show_bridge(res.cmd_str, _bridge_enabled())
        return 0

    if sub in ("tao", "create"):
        title = " ".join(rest).strip()
        if not title:
            title = ui.ask_text("Tieu de Pull Request (vd: Them chuc nang dang nhap)")
            if not title:
                ui.warn("Da huy tao Pull Request vi chua co tieu de.")
                return 1
        body = ui.ask_text("Mo ta ngan (co the bo trong va nhan Enter)")
        res = gh_runner.run_gh(["pr", "create", "--title", title, "--body", body])
        if not res.ok:
            error_translator.translate_and_print_error(res)
            return res.returncode
        if res.stdout:
            print(res.stdout)
        ui.success("Da tao Pull Request thanh cong!")
        ui.show_bridge(res.cmd_str, _bridge_enabled())
        return 0

    if sub in ("gop", "merge"):
        pr_num = rest[0] if rest else ui.ask_text("Nhap so thu tu Pull Request muon gop (vd: 1)")
        if not pr_num:
            ui.error("Chua co so thu tu PR.")
            return 1
        if not ui.ask_yes_no(f"Xac nhan gop Pull Request #{pr_num} vao nhanh chinh?", default=False):
            ui.info("Da huy thao tac gop.")
            return 0
        res = gh_runner.run_gh(["pr", "merge", pr_num, "--merge"])
        if not res.ok:
            error_translator.translate_and_print_error(res)
            return res.returncode
        ui.success(f"Da gop Pull Request #{pr_num} thanh cong!")
        ui.show_bridge(res.cmd_str, _bridge_enabled())
        return 0

    # Fallback sang gh pr <sub...>
    res = gh_runner.run_gh(["pr", *args], interactive=True)
    return res.returncode


def cmd_issue(args: List[str]) -> int:
    """Quan ly Issue (van de / cong viec): xem, tao, dong."""
    sub = args[0].lower() if args else "xem"
    rest = args[1:]

    if sub in ("xem", "list"):
        res = gh_runner.run_gh(["issue", "list", "--limit", "10", *rest])
        if not res.ok:
            error_translator.translate_and_print_error(res)
            return res.returncode
        if not res.stdout:
            ui.info("Hien khong co Issue nao dang mo.")
        else:
            print(ui.paint("Cac Issue dang mo:", ui.Color.CYAN, ui.Color.BOLD))
            print(res.stdout)
        ui.show_bridge(res.cmd_str, _bridge_enabled())
        return 0

    if sub in ("tao", "create"):
        title = " ".join(rest).strip()
        if not title:
            title = ui.ask_text("Tieu de Issue/cong viec (vd: Sua loi nut bam)")
            if not title:
                ui.warn("Da huy tao Issue vi chua co tieu de.")
                return 1
        body = ui.ask_text("Mo ta chi tiet (co the bo trong va nhan Enter)")
        res = gh_runner.run_gh(["issue", "create", "--title", title, "--body", body])
        if not res.ok:
            error_translator.translate_and_print_error(res)
            return res.returncode
        if res.stdout:
            print(res.stdout)
        ui.success("Da tao Issue thanh cong!")
        ui.show_bridge(res.cmd_str, _bridge_enabled())
        return 0

    if sub in ("dong", "close"):
        issue_num = rest[0] if rest else ui.ask_text("Nhap so thu tu Issue muon dong (vd: 1)")
        if not issue_num:
            ui.error("Chua co so thu tu Issue.")
            return 1
        res = gh_runner.run_gh(["issue", "close", issue_num])
        if not res.ok:
            error_translator.translate_and_print_error(res)
            return res.returncode
        ui.success(f"Da dong Issue #{issue_num}!")
        ui.show_bridge(res.cmd_str, _bridge_enabled())
        return 0

    res = gh_runner.run_gh(["issue", *args], interactive=True)
    return res.returncode


def cmd_caidat(args: List[str]) -> int:
    """Quan ly cai dat cho vgh (bridge mode)."""
    cfg = config.load_config()
    if not args:
        state = "BAT" if cfg.get("bridge_mode", True) else "TAT"
        print(ui.paint("Cai dat hien tai cua vgh:", ui.Color.CYAN, ui.Color.BOLD))
        print(f"  - Che do Cau noi (hien lenh gh goc): {state}")
        print("Cach doi:")
        print("  vgh caidat bridge bat   -> Hien lenh gh goc de hoc dan")
        print("  vgh caidat bridge tat   -> An lenh gh goc cho gon man hinh")
        return 0

    if args[0].lower() == "bridge" and len(args) >= 2:
        val = args[1].lower() in ("bat", "on", "true", "1", "co")
        cfg["bridge_mode"] = val
        config.save_config(cfg)
        ui.success(f"Da {'BAT' if val else 'TAT'} che do Cau noi (Bridge Mode).")
        return 0

    ui.warn("Hay dung: 'vgh caidat bridge bat' hoac 'vgh caidat bridge tat'.")
    return 1


def cmd_huongdan(args: List[str]) -> int:
    """Hien thi bang lenh vgh de hieu."""
    print(ui.paint("=== vgh - GitHub CLI tieng Viet cho nguoi moi ===", ui.Color.CYAN, ui.Color.BOLD))
    rows = [
        ("vgh dangnhap", "Dang nhap tai khoan GitHub (gh auth login)"),
        ("vgh taikhoan", "Xem tai khoan dang dang nhap (gh auth status)"),
        ("vgh taorepo [ten]", "Tao du an moi tren GitHub (gh repo create)"),
        ("vgh tai <tac-gia/ten>", "Tai du an tu GitHub ve may (gh repo clone)"),
        ("vgh fork <tac-gia/ten>", "Sao chep du an cua nguoi khac ve tai khoan minh"),
        ("vgh mo", "Mo nhanh trang GitHub cua du an tren trinh duyet"),
        ("vgh pr xem | tao | gop", "Xem, tao hoac gop Pull Request"),
        ("vgh issue xem | tao | dong", "Xem, tao hoac dong Issue (cong viec/loi)"),
        ("vgh caidat", "Bat/tat che do hien lenh gh goc"),
    ]
    for cmd, desc in rows:
        print(f"  {ui.paint(cmd.ljust(28), ui.Color.GREEN)} {desc}")
    print()
    print(ui.paint("Meo: Ban cung co the go lenh gh goc nhu 'vgh gist list' hoac 'vgh release list'.", ui.Color.GRAY))
    return 0


COMMAND_MAP: Dict[str, Callable[[List[str]], int]] = {
    "dangnhap": cmd_dangnhap,
    "taikhoan": cmd_taikhoan,
    "taorepo": cmd_taorepo,
    "tai": cmd_tai,
    "fork": cmd_fork,
    "saochep": cmd_fork,
    "mo": cmd_mo,
    "pr": cmd_pr,
    "issue": cmd_issue,
    "vande": cmd_issue,
    "caidat": cmd_caidat,
    "huongdan": cmd_huongdan,
    "help": cmd_huongdan,
    "-h": cmd_huongdan,
    "--help": cmd_huongdan,
}
