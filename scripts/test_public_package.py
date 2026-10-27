"""Offline regression checks; temporary byte fixtures are not user-facing images."""
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from markdown_to_wechat_html import markdown_to_html
from reailab_publish import prepare_package, replace_image_urls
from wechat_client import load_local_env


class PublicPackageTests(unittest.TestCase):
    def test_relative_image_uses_article_directory(self):
        with tempfile.TemporaryDirectory() as root:
            base = Path(root)
            (base / "fixture.bin").write_bytes(b"test fixture")
            article = base / "article.md"
            article.write_text("Body\n\n![alt](fixture.bin)", encoding="utf-8")
            body, images, cover = prepare_package(article, base / "fixture.bin", "Title")
            self.assertEqual(images["fixture.bin"], (base / "fixture.bin").resolve())

    def test_missing_inline_image_stops_before_upload(self):
        with tempfile.TemporaryDirectory() as root:
            base = Path(root)
            (base / "cover.bin").write_bytes(b"test fixture")
            (base / "article.md").write_text("Body\n![alt](missing.bin)", encoding="utf-8")
            with self.assertRaises(FileNotFoundError):
                prepare_package(base / "article.md", base / "cover.bin", "Title")

    def test_upload_failure_does_not_produce_partial_body(self):
        class FailingClient:
            def upload_temp_image(self, path):
                raise RuntimeError("upload failed")
        with self.assertRaises(RuntimeError):
            replace_image_urls('<img src="file.bin">', {"file.bin": Path("file.bin")}, FailingClient())

    def test_inline_text_is_escaped_and_links_render(self):
        result = markdown_to_html('A <script>alert(1)</script>\n[Source](https://example.com/a_b)')
        self.assertNotIn("<script>", result)
        self.assertIn("&lt;script&gt;", result)
        self.assertIn('href="https://example.com/a_b"', result)

    def test_image_attributes_are_escaped(self):
        result = markdown_to_html('![" onerror="alert(1)](image.bin)')
        self.assertNotIn(' onerror="', result)

    def test_local_env_does_not_override_process_values(self):
        with tempfile.TemporaryDirectory() as root:
            base = Path(root)
            (base / ".env").write_text("WECHAT_APPID=local\nWECHAT_APPSECRET=local-secret\nOTHER_KEY=value\n")
            with patch.dict(os.environ, {"WECHAT_APPID": "existing"}, clear=True):
                with patch("wechat_client.__file__", str(base / "wechat_client.py")):
                    load_local_env()
                self.assertEqual(os.environ["WECHAT_APPID"], "existing")
                self.assertEqual(os.environ["WECHAT_APPSECRET"], "local-secret")
                self.assertNotIn("OTHER_KEY", os.environ)


if __name__ == "__main__":
    unittest.main()
