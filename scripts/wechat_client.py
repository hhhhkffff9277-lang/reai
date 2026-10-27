"""Optional WeChat draft client. No generation APIs and no public-send API."""
from __future__ import annotations

import json
import os
from pathlib import Path

import requests


def load_local_env() -> None:
    """Read only this package's local .env; process values take precedence."""
    env_path = Path(__file__).resolve().parent / ".env"
    if not env_path.is_file():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if key in {"WECHAT_APPID", "WECHAT_APPSECRET"}:
            os.environ.setdefault(key, value.strip().strip('"').strip("'"))


class WeChatClient:
    def __init__(self, app_id: str, app_secret: str):
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = None
        self.session = requests.Session()
        self.session.trust_env = False

    def _request(self, method, endpoint, *, require_token=True, **kwargs):
        params = dict(kwargs.pop("params", {}))
        if require_token:
            params["access_token"] = self.get_access_token()
        try:
            response = self.session.request(
                method, "https://api.weixin.qq.com/cgi-bin/" + endpoint,
                params=params, timeout=30, **kwargs
            )
            response.raise_for_status()
            data = json.loads(response.content.decode("utf-8"))
        except (requests.RequestException, ValueError) as exc:
            raise RuntimeError("WeChat request failed: " + type(exc).__name__) from None
        if not isinstance(data, dict):
            raise RuntimeError("Unexpected WeChat response")
        if data.get("errcode", 0) != 0:
            raise RuntimeError("WeChat error code: " + str(data.get("errcode")))
        return data

    def get_access_token(self):
        if self.access_token:
            return self.access_token
        data = self._request("GET", "token", require_token=False, params={
            "grant_type": "client_credential", "appid": self.app_id, "secret": self.app_secret
        })
        if not data.get("access_token"):
            raise RuntimeError("WeChat did not return an access token")
        self.access_token = data["access_token"]
        return self.access_token

    def upload_temp_image(self, image_path):
        """Upload an inline image with uploadimg; return its hosted URL."""
        with open(image_path, "rb") as image_file:
            data = self._request("POST", "media/uploadimg", files={"media": image_file})
        if not data.get("url"):
            raise RuntimeError("WeChat did not return an inline-image URL")
        return data["url"]

    def upload_permanent_image(self, image_path):
        with open(image_path, "rb") as image_file:
            data = self._request("POST", "material/add_material",
                                 params={"type": "image"}, files={"media": image_file})
        if not data.get("media_id"):
            raise RuntimeError("WeChat did not return an image identifier")
        return data["media_id"]

    def create_draft(self, title, author, digest, content, cover_media_id):
        article = {"title": title, "author": author, "digest": digest,
                   "content": content, "thumb_media_id": cover_media_id,
                   "content_source_url": "", "need_open_comment": 0}
        data = self._request("POST", "draft/add",
                             data=json.dumps({"articles": [article]}, ensure_ascii=False).encode("utf-8"),
                             headers={"Content-Type": "application/json; charset=utf-8"})
        if not data.get("media_id"):
            raise RuntimeError("WeChat did not return a draft identifier")
        return data
