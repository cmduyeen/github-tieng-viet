"""Unit tests cho vgh."""

import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

from vgh import cli, config, error_translator, gh_runner


class TestVGh(unittest.TestCase):
    def _run_cli(self, args: list[str]) -> tuple[int, str, str]:
        out = io.StringIO()
        err = io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = cli.main(args)
        return code, out.getvalue(), err.getvalue()

    def test_huongdan_and_version(self) -> None:
        code, out, _ = self._run_cli(["huongdan"])
        self.assertEqual(code, 0)
        self.assertIn("vgh dangnhap", out)

        code_v, out_v, _ = self._run_cli(["--version"])
        self.assertEqual(code_v, 0)
        self.assertIn("0.1.0", out_v)

    def test_taorepo_mocked(self) -> None:
        fake_res = gh_runner.GhResult(
            returncode=0,
            stdout="https://github.com/demo/game-vui",
            stderr="",
            cmd_str="gh repo create game-vui --public --clone",
        )
        with (
            mock.patch("vgh.gh_runner.is_gh_installed", return_value=True),
            mock.patch("vgh.gh_runner.is_git_repo_here", return_value=False),
            mock.patch("vgh.ui.ask_yes_no", return_value=True),
            mock.patch("vgh.gh_runner.run_gh", return_value=fake_res) as m_run,
        ):
            code, out, _ = self._run_cli(["taorepo", "game-vui", "congkhai"])

        self.assertEqual(code, 0)
        self.assertIn("game-vui", out)
        self.assertIn("Lenh gh goc:", out)
        m_run.assert_called_once_with(["repo", "create", "game-vui", "--public", "--clone"])

    def test_pr_tao_mocked(self) -> None:
        fake_res = gh_runner.GhResult(
            returncode=0,
            stdout="https://github.com/demo/repo/pull/1",
            stderr="",
            cmd_str='gh pr create --title "Them menu" --body ""',
        )
        with (
            mock.patch("vgh.gh_runner.is_gh_installed", return_value=True),
            mock.patch("vgh.ui.ask_text", return_value=""),
            mock.patch("vgh.gh_runner.run_gh", return_value=fake_res) as m_run,
        ):
            code, out, _ = self._run_cli(["pr", "tao", "Them", "menu"])

        self.assertEqual(code, 0)
        self.assertIn("Da tao Pull Request thanh cong", out)
        m_run.assert_called_once_with(["pr", "create", "--title", "Them menu", "--body", ""])

    def test_error_translation_not_logged_in(self) -> None:
        res = gh_runner.GhResult(
            returncode=1,
            stdout="",
            stderr="To get started with GitHub CLI, please run:  gh auth login",
            cmd_str="gh repo list",
        )
        out = io.StringIO()
        err = io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            error_translator.translate_and_print_error(res)
        self.assertIn("chua dang nhap", err.getvalue())
        self.assertIn("vgh dangnhap", out.getvalue())

    def test_bridge_config_toggle(self) -> None:
        with tempfile.TemporaryDirectory() as cfg_tmp:
            cfg_file = Path(cfg_tmp) / "config.json"
            with mock.patch("vgh.config.get_config_path", return_value=cfg_file):
                code, _, _ = self._run_cli(["caidat", "bridge", "tat"])
                self.assertEqual(code, 0)
                self.assertFalse(config.load_config()["bridge_mode"])


if __name__ == "__main__":
    unittest.main()
