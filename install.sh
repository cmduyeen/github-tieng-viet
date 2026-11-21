#!/usr/bin/env sh
set -eu

echo "[vgh] Dang kiem tra moi truong..."

if ! command -v gh >/dev/null 2>&1; then
    echo "[Loi] May chua co GitHub CLI (gh). Hay cai tai https://cli.github.com roi chay lai."
    exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
    echo "[Loi] May chua co Python 3. Hay cai Python 3 truoc roi chay lai."
    exit 1
fi

REPO_URL="${VGH_REPO_URL:-git+https://github.com/cmduyeen/github-tieng-viet.git}"

if command -v pipx >/dev/null 2>&1; then
    pipx install --force "$REPO_URL"
else
    python3 -m pip install --user --upgrade "$REPO_URL"
fi

echo "[OK] Cai dat thanh cong! Hay go: vgh huongdan"
