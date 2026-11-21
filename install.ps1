$ErrorActionPreference = "Stop"

Write-Host "[vgh] Dang kiem tra moi truong..." -ForegroundColor Cyan

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Host "[!] May chua co GitHub CLI (gh). Dang thu cai qua winget..." -ForegroundColor Yellow
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        winget install --id GitHub.cli -e --source winget --accept-package-agreements --accept-source-agreements
    } else {
        Write-Host "[Loi] Vui long cai GitHub CLI tai https://cli.github.com roi chay lai lenh nay." -ForegroundColor Red
        exit 1
    }
}

$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py) { $py = Get-Command py -ErrorAction SilentlyContinue }
if (-not $py) {
    Write-Host "[!] May chua co Python. Dang thu cai Python 3 qua winget..." -ForegroundColor Yellow
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        winget install --id Python.Python.3.12 -e --source winget --accept-package-agreements --accept-source-agreements
    } else {
        Write-Host "[Loi] Vui long cai Python tai https://www.python.org/downloads/ roi chay lai." -ForegroundColor Red
        exit 1
    }
}

$RepoUrl = if ($env:VGH_REPO_URL) { $env:VGH_REPO_URL } else { "git+https://github.com/cmduyeen/github-tieng-viet.git" }
Write-Host "[vgh] Dang cai dat vgh..." -ForegroundColor Cyan
python -m pip install --user --upgrade $RepoUrl

$UserScripts = python -c "import sysconfig; print(sysconfig.get_path('scripts', 'nt_user'))"
$CurrentUserPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($UserScripts -and ($CurrentUserPath -notlike "*$UserScripts*")) {
    [Environment]::SetEnvironmentVariable("Path", "$CurrentUserPath;$UserScripts", "User")
    $env:Path += ";$UserScripts"
    Write-Host "[vgh] Da tu dong them thu muc lenh vao PATH." -ForegroundColor Green
}

Write-Host "[OK] Cai dat thanh cong! Hay mo terminal moi va go: vgh huongdan" -ForegroundColor Green
