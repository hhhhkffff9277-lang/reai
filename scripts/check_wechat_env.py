"""Check only this package's credential presence. No network or credential values."""
import os
from wechat_client import load_local_env

if __name__ == "__main__":
    load_local_env()
    for key in ("WECHAT_APPID", "WECHAT_APPSECRET"):
        print(key + ": " + ("SET" if os.getenv(key) else "NOT SET"))
    print("This check does not verify account permissions or IP allowlisting.")
