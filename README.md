# REAI

把一个选题，整理成有判断、有证据、能被读者复述的公众号长文。

REAI 是一套可阅读、可修改的写作 skill：主文件规定任务边界，参考资料保存研究、立意、表达和审查方法，可选脚本处理排版与草稿上传。仓库不提供在线模型服务、个人公众号账号或固定服务器。

[完整介绍页](https://ai.run-linux.com/s/mjrGbzjPHs7pAN_1fSdMGA) · [反馈与交流](https://github.com/hhhhkffff9277-lang/reai/issues) · [使用范围](USAGE.md)

## 适合做什么

- 从行业变化、产品、论文或具体场景中发现选题。
- 解释能源、AI、产业和社会议题中的成本、责任与资源变化。
- 把材料整理成有立意、有证据链、有阅读节奏的文章。
- 修改已有文章，检查过度推断、空话、重复标题和不当情绪放大。
- 在明确需要时，准备图片资产与公众号文章草稿包。

原生“公众号贴图”请使用 [WeChat Image Note](https://github.com/hhhhkffff9277-lang/wechat-image-note)。它以主图为内容本身，输出结构不同。

## 方法

选题与读者 → 原始资料 → 一句核心判断 → 具体案例和机制 → 文章 → 审查。

先回答“发生了什么、谁承担了成本或责任、证据支持到哪里”，再组织文字。不要凭空补造作者经历或精确数据，也不要用刺激标题替代证据。

## 安装或加载

请先获取整个仓库，保留 SKILL.md、references、agents 和需要的 scripts。只复制主文件会丢失参考资料。

Codex 项目级使用的一种目录结构：

~~~text
你的项目/
  .agents/
    skills/
      reai/
        SKILL.md
        references/
        agents/
        scripts/
~~~

将本仓库内容放入 reai 目录，并在支持的技能入口中选择 REAI。不同工具的加载方式和可用能力不同，参见 [OpenAI 官方技能说明](https://learn.chatgpt.com/docs/build-skills)。不要把作者本机路径当作通用安装位置。

这份分享是普通 skill 文件目录，不声称已经上架插件商店或适配全部 AI 产品。

## 先试一次文字任务

复制到已经加载本 skill 的工具中：

~~~text
请使用 REAI，围绕【主题】为【目标读者】准备公众号文章。
先明确一个核心判断，核对会变化的事实。
交付立意说明、标题备选、摘要、正文和审查记录。
来源不足的精确数据不要使用，个人经历只采用我提供的信息。
现在只完成文字和配图方案，不生成图片，不上传公众号。
材料如下：【材料或链接】
~~~

修稿时：

~~~text
请按 REAI 审查下面的文章：
判断是否清楚、证据是否足够、机制是否具体，
以及是否存在套话、重复标题和过度推断。
先指出最影响理解的问题，再给修改稿。
保留作者真实立场，不编造个人经历。
暂不生成图片，不上传公众号。
文章如下：【正文】
~~~

## 输出和文件

常见文字交付：标题备选、摘要、Markdown 正文、立意说明、配图方案、事实核验与审查记录。

完整本地包可以包含 article.md、title.txt、digest.txt、redteam_notes.md。
images/ 只放真实提供或明确要求生成的资产；不制造占位图片冒充成品。

## 图片与草稿箱是可选环节

写作在当前模型会话中完成；新图片只在明确要求时使用 Image 2／宿主内置生图。没有该能力的环境仍可完成文字与方案，但不能宣称已经生成图片。

可选 Python 脚本只处理文字转换、文件验证和微信上传，不会调用其他生成 API。创建草稿需要你自己的公众号权限、凭据与符合账号要求的运行环境。创建草稿不等于公开群发。

### 本地转换和验证（读者自己的 Mac/Linux）

纯 Markdown 转换可直接执行：
~~~bash
python3 scripts/markdown_to_wechat_html.py package/article.md > package/article.html
~~~

使用上传辅助脚本时，建议先建虚拟环境：
~~~bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
~~~

离线验证不读凭据、不调用微信：
~~~bash
python3 scripts/reailab_publish.py --markdown package/article.md --title "标题" --digest "摘要" --cover package/images/cover.png --validate-only
~~~

相对文内图片路径以 article.md 所在目录为基准；封面参数以当前执行目录为基准。缺图会阻止上传。

真实上传前阅读 [发布说明](references/publishing.md)，只使用你自己的配置。不要把 .env 发到仓库或 Issues，也不需要借用作者服务器。

## 本公开版的整理

已移除作者专用的绝对路径、固定服务器和远程包装命令；当前环境配置优先于本地 .env。新增离线验证，缺失图片与上传失败会停止流程；来源链接和普通文本按安全 HTML 处理。

已做本地回归检查，不代表已验证每位读者的微信账号或所有平台预览。基础转换器只支持本项目常用 Markdown，不处理任意 HTML、复杂表格或完整代码高亮。正式交付前仍需预览。

## 来源、效果与权利

规则描述来自本仓库的 SKILL.md 和参考文件。官方技能文档仅说明组织与加载方式，不能证明写作效果。不提供阅读量、收益或事实准确率保证。

写作结构曾参考 khazix-writer 的部分原则；原始说明保留在 writing-playbook.md。本仓库未打包其源代码或素材，不宣称获得其背书。未打包第三方图片、字体、模型或私人草稿。

允许 Fork 并修改自己的 Fork；原仓库不接收 PR，反馈请走 Issues。其他授权事项见 [USAGE.md](USAGE.md)；当前未采用 MIT 等标准许可证。
