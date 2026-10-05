#!/usr/bin/env python3
"""Generate marketplace.json for the ZCodium community plugins repository.

Each entry points at an in-repo plugin directory (relative path source, no zip,
no release assets). Plugin name/version/description are read from the plugin
manifest inside the directory; store listing metadata (display names, Chinese
translations, categories, icons) is configured per entry below.

Run from the repository root:  python3 scripts/generate_marketplace.py
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_BASE = (
    "https://raw.githubusercontent.com/ZCodium-project/"
    "zcodium-community-famous-plugins-and-skills/main"
)

MARKETPLACE_NAME = "zcodium-community-famous-plugins-and-skills"
MARKETPLACE_DESCRIPTION = (
    "ZCodium community hub for famous plugins and skills: curated Claude Code plugins, "
    "Codex plugins, ZCode ecosystem plugins and standalone skills, vendored with licence "
    "and provenance notes."
)
MARKETPLACE_DESCRIPTION_I18N = {
    "en": MARKETPLACE_DESCRIPTION,
    "zh-CN": "ZCodium 社区知名插件与技能聚合：精选 Claude Code 插件、Codex 插件、ZCode 生态插件与独立技能，均注明来源与许可。",
}

# Manifest probe order matches the ZCodium runtime (zcode > claude > codex > root).
MANIFEST_PATHS = (
    ".zcode-plugin/plugin.json",
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    "plugin.json",
)

# (directory, listing overrides). Keep in sync with the folders on disk.
ENTRIES: list[tuple[str, dict]] = [
    # ---- claude-code-plugins ----
    (
        "claude-code-plugins/superpowers",
        {
            "category": "developer-tools",
            "icon": f"{RAW_BASE}/assets/superpowers.png",
            "displayName_i18n": {"en": "Superpowers", "zh-CN": "Superpowers"},
            "description_i18n": {
                "en": "Agentic skills framework and software development methodology: brainstorming, planning, TDD, systematic debugging, code review and delivery workflows.",
                "zh-CN": "智能体技能框架与软件开发方法论：头脑风暴、计划、TDD、系统化调试、代码审查与交付工作流。",
            },
        },
    ),
    (
        "claude-code-plugins/code-review",
        {"category": "developer-tools", "displayName_i18n": {"en": "Code Review", "zh-CN": "代码审查"}},
    ),
    (
        "claude-code-plugins/commit-commands",
        {"category": "developer-tools", "displayName_i18n": {"en": "Commit Commands", "zh-CN": "提交命令"}},
    ),
    (
        "claude-code-plugins/security-guidance",
        {"category": "developer-tools", "displayName_i18n": {"en": "Security Guidance", "zh-CN": "安全指导"}},
    ),
    (
        "claude-code-plugins/pr-review-toolkit",
        {"category": "developer-tools", "displayName_i18n": {"en": "PR Review Toolkit", "zh-CN": "PR 审查工具包"}},
    ),
    (
        "claude-code-plugins/skill-creator",
        {"category": "utilities", "displayName_i18n": {"en": "Skill Creator", "zh-CN": "技能创建器"}},
    ),
    (
        "claude-code-plugins/frontend-design",
        {"category": "developer-tools", "displayName_i18n": {"en": "Frontend Design", "zh-CN": "前端设计"}},
    ),
    (
        "claude-code-plugins/plugin-dev",
        {"category": "developer-tools", "displayName_i18n": {"en": "Plugin Dev", "zh-CN": "插件开发"}},
    ),
    (
        "claude-code-plugins/claude-code-setup",
        {"category": "utilities", "displayName_i18n": {"en": "Claude Code Setup", "zh-CN": "配置推荐"}},
    ),
    # ---- codex-plugins ----
    (
        "codex-plugins/compound-engineering",
        {
            "category": "developer-tools",
            "displayName": "Compound Engineering",
            "displayName_i18n": {"en": "Compound Engineering", "zh-CN": "复合工程"},
            "description_i18n": {
                "en": "Brainstorm, plan, debug, review, and compound learnings with AI agents. 36 skills covering the full engineering loop.",
                "zh-CN": "用 AI 智能体完成头脑风暴、计划、调试、审查与经验沉淀，36 个技能覆盖完整工程闭环。",
            },
        },
    ),
    # ---- zcodium-plugins (vendored from zai-org/zcode-plugins, paid-plan plugins excluded) ----
    (
        "zcodium-plugins/github",
        {
            "category": "developer-tools",
            "icon": f"{RAW_BASE}/assets/github.png",
            "displayName_i18n": {"en": "GitHub", "zh-CN": "GitHub"},
            "description_i18n": {
                "en": "GitHub CLI workflows for commits, pull requests, issues, releases, Actions, repositories, Codespaces, and other GitHub resources.",
                "zh-CN": "基于 GitHub CLI 的 GitHub 工作流，覆盖提交、Pull Request、Issue、Release、Actions、仓库、Codespaces 等资源。",
            },
        },
    ),
    (
        "zcodium-plugins/gitlab",
        {
            "category": "developer-tools",
            "icon": f"{RAW_BASE}/assets/gitlab.png",
            "displayName_i18n": {"en": "GitLab", "zh-CN": "GitLab"},
            "description_i18n": {
                "en": "GitLab CLI workflows based on GitLab's official Agent Skills for merge requests, issues, CI/CD, repositories, releases, and API operations.",
                "zh-CN": "基于官方 GitLab CLI 的 Merge Request、Issue、CI/CD、仓库、Release 与 API 工作流。",
            },
        },
    ),
    (
        "zcodium-plugins/alibaba-cloud-cli",
        {
            "category": "developer-tools",
            "icon": f"{RAW_BASE}/assets/alibaba-cloud-cli.png",
            "displayName_i18n": {"en": "Alibaba Cloud CLI", "zh-CN": "阿里云 CLI"},
            "description_i18n": {
                "en": "Alibaba Cloud CLI workflows for credential setup, profile checks, and safe cloud resource operations.",
                "zh-CN": "阿里云 CLI 工作流：配置凭证与 profile，并安全执行云资源查询和操作。",
            },
        },
    ),
    (
        "zcodium-plugins/lark-cli",
        {
            "category": "productivity",
            "icon": f"{RAW_BASE}/assets/lark-cli.png",
            "displayName_i18n": {"en": "Lark CLI", "zh-CN": "飞书 CLI"},
            "description_i18n": {
                "en": "Lark CLI workflows for docs, sheets, Base, calendar, messaging, and other SaaS resources with guided setup and OAuth login.",
                "zh-CN": "飞书 CLI 工作流：覆盖文档、表格、多维表格、日历、消息等 SaaS 资源，并引导应用配置与 OAuth 登录。",
            },
        },
    ),
    (
        "zcodium-plugins/tencent-meeting-cli",
        {
            "category": "productivity",
            "icon": f"{RAW_BASE}/assets/tencent-meeting-cli.png",
            "displayName_i18n": {"en": "Tencent Meeting CLI", "zh-CN": "腾讯会议 CLI"},
            "description_i18n": {
                "en": "Tencent Meeting CLI workflows with OAuth2 setup, meeting management, recordings, and attendee reports.",
                "zh-CN": "腾讯会议 CLI 工作流：OAuth2 授权、会议管理、录制管理和参会报告查询。",
            },
        },
    ),
    (
        "zcodium-plugins/dingtalk-cli",
        {
            "category": "productivity",
            "icon": f"{RAW_BASE}/assets/dingtalk-cli.png",
            "displayName_i18n": {"en": "DingTalk CLI", "zh-CN": "钉钉 CLI"},
            "description_i18n": {
                "en": "DingTalk Workspace CLI workflows with OAuth/device authorization, profile checks, and optional upstream Skills.",
                "zh-CN": "钉钉 Workspace CLI 工作流：OAuth/设备授权、验证组织账号，并按需安装上游 Skills。",
            },
        },
    ),
    (
        "zcodium-plugins/wecom-cli",
        {
            "category": "productivity",
            "icon": f"{RAW_BASE}/assets/wecom-cli.png",
            "displayName_i18n": {"en": "WeCom CLI", "zh-CN": "企业微信 CLI"},
            "description_i18n": {
                "en": "WeCom CLI workflows for messages, docs, sheets, mail, calendar, meetings, contacts, and todos with QR authentication.",
                "zh-CN": "企业微信 CLI 工作流：覆盖消息、文档、表格、邮件、日历、会议、通讯录和待办，并支持扫码授权与状态检查。",
            },
        },
    ),
    (
        "zcodium-plugins/obsidian",
        {
            "category": "productivity",
            "icon": f"{RAW_BASE}/assets/obsidian.png",
            "displayName_i18n": {"en": "Obsidian", "zh-CN": "Obsidian"},
            "description_i18n": {
                "en": "Obsidian authoring skills: Flavored Markdown notes, Bases views, JSON Canvas boards, CLI vault automation, web extraction and Mermaid/Excalidraw visualizations.",
                "zh-CN": "Obsidian 创作技能：风格化 Markdown 笔记、Bases 数据库视图、JSON Canvas 白板、CLI 库操作、网页正文提取与 Mermaid/Excalidraw 可视化。",
            },
        },
    ),
    (
        "zcodium-plugins/mimosa",
        {
            "category": "developer-tools",
            "icon": f"{RAW_BASE}/assets/mimosa.png",
            "displayName_i18n": {"en": "Code Security Protection", "zh-CN": "代码安全防护"},
            "description_i18n": {
                "en": "Local-first security guardrails: pre-write hooks, end-of-turn review, Git gates, commands, a security-scan skill, and an optional MCP server for sealed deep scans.",
                "zh-CN": "本地优先的代码安全防线：写入前 Hook、任务收尾复查、Git 门禁、命令、安全扫描 Skill，以及可选的密封深扫 MCP 服务。",
            },
        },
    ),
    (
        "zcodium-plugins/cloudbase-skills",
        {
            "category": "developer-tools",
            "icon": "https://docs.cloudbase.net/en/img/favicon.png",
            "displayName_i18n": {"en": "CloudBase", "zh-CN": "腾讯云 CloudBase"},
            "description_i18n": {
                "en": "CloudBase development skills and MCP integration for building, deploying, and troubleshooting Web, WeChat Mini Program, database, cloud function, CloudRun, storage, and AI projects.",
                "zh-CN": "腾讯云 CloudBase 开发技能与 MCP 集成，覆盖 Web、微信小程序、数据库、云函数、云托管、云存储和 AI 项目的开发、部署与排障。",
            },
        },
    ),
    (
        "zcodium-plugins/video2code",
        {
            "category": "productivity",
            "icon": f"{RAW_BASE}/assets/video2code.png",
            "displayName_i18n": {"en": "Video2Code", "zh-CN": "录屏复刻网页"},
            "description_i18n": {
                "en": "Records WebM through ZCode's built-in Browser Use WebView and converts it to MP4 with ffmpeg for video/URL replication; no Playwright or external Chromium required.",
                "zh-CN": "基于 ZCode 内置 Browser Use WebView 录制 WebM 并用 ffmpeg 转成 MP4/URL 复刻；无需 Playwright 或外部 Chromium。",
            },
        },
    ),
    # ---- skills ----
    (
        "skills",
        {
            "category": "utilities",
            "displayName": "Community Skills",
            "displayName_i18n": {"en": "Community Skills", "zh-CN": "社区技能合集"},
            "description_i18n": {
                "en": "Curated community skills bundle: Matt Pocock's engineering skills (TDD, code review, debugging, research, specs and more).",
                "zh-CN": "精选社区技能合集：Matt Pocock 的工程技能（TDD、代码审查、调试、调研、规格等）。",
            },
        },
    ),
]


def read_manifest(plugin_dir: Path) -> dict:
    for relative in MANIFEST_PATHS:
        manifest_path = plugin_dir / relative
        if manifest_path.is_file():
            return json.loads(manifest_path.read_text(encoding="utf-8"))
    raise SystemExit(f"no plugin manifest found under {plugin_dir}")


def build_entry(directory: str, listing: dict) -> dict:
    plugin_dir = ROOT / directory
    manifest = read_manifest(plugin_dir)
    entry: dict = {
        "name": manifest["name"],
        "version": manifest.get("version", "0.0.0"),
        "source": f"./{directory}",
    }
    description = listing.get("description") or manifest.get("description")
    if description:
        entry["description"] = description
    entry["author"] = manifest.get("author") or {"name": "ZCodium Community"}
    for key in ("displayName", "displayName_i18n", "description_i18n", "icon", "category"):
        if key in listing:
            entry[key] = listing[key]
    return entry


def main() -> None:
    entries = []
    seen_names: set[str] = set()
    for directory, listing in ENTRIES:
        entry = build_entry(directory, listing)
        if entry["name"] in seen_names:
            raise SystemExit(f"duplicate plugin name in marketplace: {entry['name']}")
        seen_names.add(entry["name"])
        entries.append(entry)

    marketplace = {
        "name": MARKETPLACE_NAME,
        "description": MARKETPLACE_DESCRIPTION,
        "description_i18n": MARKETPLACE_DESCRIPTION_I18N,
        "owner": {"name": "ZCodium Project", "url": "https://github.com/ZCodium-project"},
        "plugins": entries,
    }
    output_path = ROOT / "marketplace.json"
    output_path.write_text(
        json.dumps(marketplace, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {output_path.relative_to(ROOT)} with {len(entries)} plugins")


if __name__ == "__main__":
    main()
