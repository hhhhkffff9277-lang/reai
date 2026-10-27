"""Validate an article package, then create one explicitly authorized WeChat draft."""
from __future__ import annotations

import argparse
import html as html_lib
import json
import os
import re
from pathlib import Path

from markdown_to_wechat_html import markdown_to_html
from wechat_client import WeChatClient, load_local_env

IMAGE_SRC = re.compile(r'(<img\b[^>]*\bsrc=")([^"]+)(")', re.IGNORECASE)


def resolve_images(body, base_dir):
    images = {}
    for match in IMAGE_SRC.finditer(body):
        src = html_lib.unescape(match.group(2))
        if src.startswith(("https://", "http://")):
            continue
        path = Path(src).expanduser()
        if not path.is_absolute():
            path = base_dir / path
        path = path.resolve()
        if not path.is_file():
            raise FileNotFoundError("Missing article image: " + str(path))
        images[src] = path
    return images


def prepare_package(markdown_path, cover_path, title):
    markdown_path = Path(markdown_path).expanduser().resolve()
    cover_path = Path(cover_path).expanduser().resolve()
    if not cover_path.is_file():
        raise FileNotFoundError("Missing cover image: " + str(cover_path))
    text = markdown_path.read_text(encoding="utf-8")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        raise ValueError("Article must not be empty")
    if lines[0].startswith("# "):
        raise ValueError("Remove the in-body H1; the platform already displays the title")
    if lines[0] == title:
        raise ValueError("The first body line duplicates the title")
    if re.search(r"^\s*\|.*\|\s*$", text, re.MULTILINE):
        raise ValueError("Replace pipe tables with readable prose or explicitly requested table images")
    body = markdown_to_html(text)
    images = resolve_images(body, markdown_path.parent)
    return body, images, cover_path


def replace_image_urls(body, images, client):
    # Finish all image uploads before creating any draft; never continue after failure.
    uploaded = {src: client.upload_temp_image(str(path)) for src, path in images.items()}

    def replace(match):
        original = html_lib.unescape(match.group(2))
        replacement = uploaded.get(original)
        if replacement is None:
            return match.group(0)
        return match.group(1) + html_lib.escape(replacement, quote=True) + match.group(3)

    return IMAGE_SRC.sub(replace, body)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--markdown", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--author", default="")
    parser.add_argument("--digest", required=True)
    parser.add_argument("--cover", required=True)
    parser.add_argument("--validate-only", action="store_true",
                        help="Check local files without reading credentials or calling WeChat")
    args = parser.parse_args()
    if not args.title.strip():
        raise ValueError("Title must not be empty")
    body, images, cover = prepare_package(args.markdown, args.cover, args.title.strip())
    if args.validate_only:
        print(json.dumps({"status": "validated", "local_inline_images": len(images)}))
        return
    load_local_env()
    app_id, app_secret = os.getenv("WECHAT_APPID"), os.getenv("WECHAT_APPSECRET")
    if not app_id or not app_secret:
        raise ValueError("Set WECHAT_APPID and WECHAT_APPSECRET in your own environment")
    client = WeChatClient(app_id, app_secret)
    body = replace_image_urls(body, images, client)
    cover_id = client.upload_permanent_image(str(cover))
    draft = client.create_draft(args.title, args.author, args.digest, body, cover_id)
    print(json.dumps({"status": "draft_created", "media_id": draft["media_id"]}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, FileNotFoundError, RuntimeError) as exc:
        raise SystemExit(str(exc)) from None
