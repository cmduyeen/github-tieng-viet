"""Dich cac loi pho bien cua GitHub CLI (gh) sang tieng Viet."""

from . import ui
from .gh_runner import GhResult


def translate_and_print_error(res: GhResult) -> None:
    text = res.combined
    lower = text.lower()

    if "gh auth login" in lower or "not logged into any github" in lower or "authentication" in lower:
        ui.error("Ban chua dang nhap vao tai khoan GitHub.")
        ui.info("Goi y: Go 'vgh dangnhap' va lam theo huong dan tren man hinh.")
        return

    if "not a git repository" in lower or "no git remotes found" in lower or "none of the git remotes" in lower:
        ui.error("Thu muc nay chua ket noi voi du an nao tren GitHub.")
        ui.info("Goi y: Go 'vgh taorepo' de tao du an moi tren GitHub, hoac 'vgit ketnoi <link>'.")
        return

    if "name already exists on this account" in lower:
        ui.error("Ten du an nay da ton tai tren tai khoan GitHub cua ban.")
        ui.info("Goi y: Hay chon mot ten khac cho du an.")
        return

    if "no commits between" in lower or "must have at least one commit" in lower or "head branch" in lower and "not found" in lower:
        ui.error("Chua co thay doi nao duoc day len nhanh moi de tao Pull Request.")
        ui.info("Goi y: Hay luu code ('vgit luu \"...\"') va day len ('vgit day') truoc.")
        return

    if "could not resolve to a repository" in lower or "http 404" in lower or "not found" in lower:
        ui.error("Khong tim thay du an hoac muc nay tren GitHub (404).")
        ui.info("Goi y: Kiem tra lai ten 'tac-gia/ten-repo' hoac quyen truy cap neu la repo rieng tu.")
        return

    if "http 403" in lower or "forbidden" in lower:
        ui.error("Ban khong co quyen thuc hien thao tac nay tren du an.")
        return

    if "dial tcp" in lower or "connection refused" in lower or "no such host" in lower or "timeout" in lower:
        ui.error("Khong ket noi duoc toi GitHub.")
        ui.info("Goi y: Kiem tra lai ket noi mang Wi-Fi/Internet.")
        return

    ui.error("GitHub CLI bao loi:")
    if text:
        print(text)
