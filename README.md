# 🐙 github-tieng-viet (`vgh`) — Làm việc với GitHub ngay trên Terminal bằng tiếng Việt

[Tiếng Việt](README.md) · [English](README.en.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Buy%20me%20a%20coffee-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/cmduyeen)

**`vgh`** Việt hóa các thao tác của GitHub CLI (`gh`) giúp bạn đăng nhập, tạo repo, gửi Pull Request và quản lý Issue ngay trong terminal bằng tiếng Việt — không cần bấm qua lại nhiều tab trình duyệt.

## ✨ Điểm nổi bật

- **Thao tác GitHub siêu nhanh bằng tiếng Việt:** Tạo repo mới (`vgh taorepo`), tải code (`vgh tai`), tạo Pull Request (`vgh pr tao`) chỉ với 1 dòng lệnh ngắn.
- **Chế độ Cầu nối học `gh` gốc:** Luôn hiển thị lệnh `gh` gốc tương ứng sau mỗi lần chạy để bạn tự tin chuyển sang dùng GitHub CLI chuyên nghiệp bất kỳ lúc nào.
- **Dịch lỗi sang tiếng Việt:** Tự động giải thích nguyên nhân nếu bạn chưa đăng nhập, thiếu quyền repo hoặc sai cú pháp.
- **Kết hợp hoàn hảo với `vgit`:** Dùng `vgit` để lưu code dưới máy và `vgh` để tạo repo, mở PR trên GitHub.

---

## ⚡ Cài đặt trong 30 giây

### Windows (PowerShell)
```powershell
irm https://raw.githubusercontent.com/cmduyeen/github-tieng-viet/main/install.ps1 | iex
```

### macOS / Linux
```bash
curl -fsSL https://raw.githubusercontent.com/cmduyeen/github-tieng-viet/main/install.sh | sh
```

### Hoặc cài từ mã nguồn
```powershell
git clone https://github.com/cmduyeen/github-tieng-viet.git
cd github-tieng-viet
pip install -e .
```

*(Yêu cầu máy đã cài sẵn [GitHub CLI (`gh`)](https://cli.github.com/).)*

---

## 🚀 Thực hành nhanh

```powershell
# 1. Đăng nhập GitHub lần đầu
vgh dangnhap

# 2. Tạo dự án mới trên GitHub ngay từ terminal
vgh taorepo du-an-dau-tien

# 3. Xem nhanh các Pull Request hoặc Issue
vgh pr xem
vgh issue xem

# 4. Mở trang GitHub của dự án trên trình duyệt
vgh mo
```

---

## 📖 Bảng lệnh `vgh`

| Lệnh `vgh` | Ý nghĩa | Lệnh `gh` gốc tương đương |
| :--- | :--- | :--- |
| `vgh dangnhap` | Đăng nhập tài khoản GitHub | `gh auth login` |
| `vgh taikhoan` | Xem tài khoản đang đăng nhập | `gh auth status` |
| `vgh taorepo [tên]` | Tạo repo mới trên GitHub | `gh repo create` |
| `vgh tai <tác-giả/tên>` | Tải repo từ GitHub về máy | `gh repo clone` |
| `vgh fork <tác-giả/tên>` | Sao chép repo người khác về tài khoản mình | `gh repo fork --clone` |
| `vgh mo` | Mở trang GitHub của dự án trên trình duyệt | `gh browse` |
| `vgh pr xem \| tao \| gop` | Xem, tạo hoặc gộp Pull Request | `gh pr list/create/merge` |
| `vgh issue xem \| tao \| dong` | Xem, tạo hoặc đóng Issue | `gh issue list/create/close` |
| `vgh caidat` | Bật/tắt chế độ hiển thị lệnh `gh` gốc | — |
| `vgh huongdan` | Xem bảng hướng dẫn nhanh | — |

---

## 🧰 Bộ công cụ lập trình tiếng Việt

| Công cụ | Mô tả | Link |
| :--- | :--- | :--- |
| **python-tieng-viet** | Python tiếng Việt (`vpy`) & trình soạn thảo `vide` | [cmduyeen/python-tieng-viet](https://github.com/cmduyeen/python-tieng-viet) |
| **git-tieng-viet** | Git tiếng Việt (`vgit`) cho người mới học | [cmduyeen/git-tieng-viet](https://github.com/cmduyeen/git-tieng-viet) |
| **github-tieng-viet** *(đang xem)* | GitHub CLI tiếng Việt (`vgh`) | [cmduyeen/github-tieng-viet](https://github.com/cmduyeen/github-tieng-viet) |
| **terminal-tieng-viet** | Windows Terminal / PowerShell tiếng Việt (`vwt`) | [cmduyeen/terminal-tieng-viet](https://github.com/cmduyeen/terminal-tieng-viet) |

---

[MIT License](LICENSE) · Phát triển bởi [cmduyeen](https://github.com/cmduyeen) · ☕ [Mời mình 1 ly cà phê (Ko-fi)](https://ko-fi.com/cmduyeen)
