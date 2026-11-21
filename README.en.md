# vgh — Vietnamese GitHub CLI (`gh`) for Beginners & Kids

[Tiếng Việt](README.md) · [English](README.en.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Buy%20me%20a%20coffee-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/cmduyeen)

`vgh` is a Vietnamese CLI wrapper for GitHub CLI (`gh`), translating errors into Vietnamese and offering a **Bridge Mode** that displays the original `gh` command after each operation.

## Quick Install

### Windows (PowerShell)
```powershell
irm https://raw.githubusercontent.com/cmduyeen/github-tieng-viet/main/install.ps1 | iex
```

### macOS / Linux
```bash
curl -fsSL https://raw.githubusercontent.com/cmduyeen/github-tieng-viet/main/install.sh | sh
```

### From Source
```powershell
git clone https://github.com/cmduyeen/github-tieng-viet.git
cd github-tieng-viet
pip install -e .
```

## Command Reference

| Command | Meaning | Original `gh` Command |
| :--- | :--- | :--- |
| `vgh dangnhap` | Sign in to GitHub | `gh auth login` |
| `vgh taikhoan` | Check active account | `gh auth status` |
| `vgh taorepo [name]` | Create a new GitHub repo | `gh repo create` |
| `vgh tai <owner/repo>` | Clone a repo from GitHub | `gh repo clone` |
| `vgh fork <owner/repo>` | Fork and clone a repo | `gh repo fork --clone` |
| `vgh mo` | Open repo on GitHub in browser | `gh browse` |
| `vgh pr xem \| tao \| gop` | List, create, or merge Pull Requests | `gh pr list/create/merge` |
| `vgh issue xem \| tao \| dong` | List, create, or close Issues | `gh issue list/create/close` |
| `vgh caidat` | Toggle Bridge Mode | — |
| `vgh huongdan` | Show help guide | — |

## Vietnamese CLI Ecosystem

| Tool | Description | Repository |
| :--- | :--- | :--- |
| **vpy** | Vietnamese Python (`.vpy`) & `vide` editor | [cmduyeen/python-tieng-viet](https://github.com/cmduyeen/python-tieng-viet) |
| **vgit** | Vietnamese Git CLI for beginners | [cmduyeen/git-tieng-viet](https://github.com/cmduyeen/git-tieng-viet) |
| **vgh** *(current)* | Vietnamese GitHub CLI (`gh`) | [cmduyeen/github-tieng-viet](https://github.com/cmduyeen/github-tieng-viet) |
| **vwt** | Vietnamese Windows Terminal / PowerShell commands | [cmduyeen/terminal-tieng-viet](https://github.com/cmduyeen/terminal-tieng-viet) |

---

Developed by [cmduyeen](https://github.com/cmduyeen) · ☕ [Buy me a coffee (Ko-fi)](https://ko-fi.com/cmduyeen)
