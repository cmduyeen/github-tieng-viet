# vgh — GitHub CLI (`gh`) tiếng Việt cho người mới học & trẻ em

[Tiếng Việt](README.md) · [English](README.en.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Buy%20me%20a%20coffee-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/cmduyeen)

`vgh` là công cụ dòng lệnh (CLI) Việt hóa các thao tác GitHub (`gh`), tự động dịch lỗi sang tiếng Việt và kèm **Chế độ Cầu nối** hiển thị lệnh `gh` gốc sau mỗi thao tác.

## Cài đặt nhanh

### Thử nghiệm ngay tại máy (Local)
```powershell
cd D:\Brain2nd\06-Code\vgh
pip install -e .
```

### Cài 1 dòng từ GitHub
**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/cmduyeen/github-tieng-viet/main/install.ps1 | iex
```

**macOS / Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/cmduyeen/github-tieng-viet/main/install.sh | sh
```

## Bảng lệnh cơ bản

| Lệnh `vgh` | Ý nghĩa | Lệnh `gh` gốc |
| :--- | :--- | :--- |
| `vgh dangnhap` | Đăng nhập tài khoản GitHub | `gh auth login` |
| `vgh taikhoan` | Xem tài khoản đang đăng nhập | `gh auth status` |
| `vgh taorepo [tên]` | Tạo dự án mới trên GitHub | `gh repo create` |
| `vgh tai <tac-gia/ten>` | Tải dự án từ GitHub về máy | `gh repo clone` |
| `vgh fork <tac-gia/ten>` | Sao chép dự án người khác về tài khoản mình | `gh repo fork --clone` |
| `vgh mo` | Mở trang GitHub của dự án trên trình duyệt | `gh browse` |
| `vgh pr xem \| tao \| gop` | Xem, tạo hoặc gộp Pull Request | `gh pr list/create/merge` |
| `vgh issue xem \| tao \| dong` | Xem, tạo hoặc đóng Issue | `gh issue list/create/close` |
| `vgh caidat` | Bật/tắt chế độ hiển thị lệnh gốc | — |
| `vgh huongdan` | Xem bảng hướng dẫn | — |

## Bộ công cụ lập trình tiếng Việt

| Công cụ | Mô tả | Link |
| :--- | :--- | :--- |
| **vpy** | Python tiếng Việt (`.vpy`) & trình soạn thảo `vide` | [cmduyeen/python-tieng-viet](https://github.com/cmduyeen/python-tieng-viet) |
| **vgit** | Git tiếng Việt cho người mới học | [cmduyeen/git-tieng-viet](https://github.com/cmduyeen/git-tieng-viet) |
| **vgh** *(đang xem)* | GitHub CLI (`gh`) tiếng Việt | [cmduyeen/github-tieng-viet](https://github.com/cmduyeen/github-tieng-viet) |
| **vwt** | Windows Terminal / PowerShell tiếng Việt | [cmduyeen/terminal-tieng-viet](https://github.com/cmduyeen/terminal-tieng-viet) |

---

Phát triển bởi [cmduyeen](https://github.com/cmduyeen) · ☕ [Mời mình 1 ly cà phê (Ko-fi)](https://ko-fi.com/cmduyeen)
