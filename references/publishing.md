# Article formatting and optional draft upload

Use this reference only when the user explicitly requests an article draft or local package.

## Before any upload

Finish and review the text. Preserve actual supplied or explicitly requested generated images. An image generation request is separate from conversion and upload.

Check that the body does not duplicate the platform title or begin with its paraphrase. Use clear headings and a final 参考资料 section. Resolve local image paths relative to article.md, and stop on any missing referenced file. Never upload an incomplete body silently.

## Local use

Commands below run on the reader's own Mac/Linux machine; real API calls must run from an environment permitted by their WeChat account.

Install optional dependencies with a virtual environment and requirements.txt. Pure conversion does not require requests.

Convert only:
~~~bash
python3 scripts/markdown_to_wechat_html.py package/article.md > package/article.html
~~~

Validate without credentials or network:
~~~bash
python3 scripts/reailab_publish.py --markdown package/article.md --title "标题" --digest "摘要" --cover package/images/cover.png --validate-only
~~~

Only after explicit upload authorization and with the reader's own account configured:
~~~bash
python3 scripts/reailab_publish.py --markdown package/article.md --title "标题" --digest "摘要" --cover package/images/cover.png
~~~

## Configuration

Use WECHAT_APPID and WECHAT_APPSECRET in the process environment, or an untracked scripts/.env based on .env.example. Existing environment values take precedence. No other skill's credential file is searched.

The client ignores proxy environment variables for its own WeChat requests. It does not change the user's global proxy configuration. Configure account permissions and the actual API host's IP allowlist yourself. No server or account access is included.

A validation result only confirms local content and paths; it does not confirm API permissions, image acceptance, or mobile layout.

## Platform references and limits

Official draft reference:
https://developers.weixin.qq.com/doc/service/api/draftbox/draftmanage/api_draft_add

The public package uses the existing article-draft request structure. Current account eligibility, limits, and platform behavior must be checked against official documentation and an actual preview. The release preparation did not verify a reader's account.

## Failures and retry boundary

Do not print secrets, access tokens, or credential-bearing request URLs. If an image upload or draft call fails, stop and explain the failed stage. Uploaded materials may remain after a failure. Before retrying after a timeout during draft creation, check the account's draft box to avoid duplicates.

The helper creates one draft. It does not call a public-send API.
