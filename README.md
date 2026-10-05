# ZCodium Community — Famous Plugins & Skills

ZCodium 社区维护的**知名插件与技能聚合仓库**：精选 Claude Code 插件、Codex 插件、ZCode 生态插件与独立技能。所有内容均 vendor 自上游开源仓库，逐一登记来源 revision 与许可（见 [NOTICE.md](./NOTICE.md)）。

## 在 ZCodium 中使用

1. 打开 **设置 → 插件（商店）**；
2. 点击 **New**（添加市场），输入：

   ```
   ZCodium-project/zcodium-community-famous-plugins-and-skills
   ```

3. 市场出现在「个人」分段，即可浏览、安装、启停与更新。

CLI 等效操作：

```sh
zcode plugins marketplace add ZCodium-project/zcodium-community-famous-plugins-and-skills
zcode plugins install superpowers@zcodium-community-famous-plugins-and-skills
```

## 目录结构

```
.
├── marketplace.json          # 市场清单（由 scripts/generate_marketplace.py 生成）
├── claude-code-plugins/      # Claude Code 生态插件（含多生态插件）
├── codex-plugins/            # Codex 生态插件
├── zcodium-plugins/          # ZCode / ZCodium 生态插件（迁移自官方公开市场仓库）
├── skills/                   # 独立技能合集（作为单一插件分发）
├── assets/                   # 市场图标（marketplace.json 经 raw 链接引用）
└── scripts/                  # 维护脚本
```

## 收录清单（22）

### claude-code-plugins

| 插件 | 说明 |
| --- | --- |
| `superpowers` | 智能体技能框架与软件开发方法论（TDD、调试、协作模式） |
| `code-review` | 自动化代码审查（多智能体 + 置信度评分） |
| `commit-commands` | Git 提交/推送/PR 工作流命令 |
| `security-guidance` | 安全审查：编辑警告、Stop 复查、提交审查 |
| `pr-review-toolkit` | PR 审查智能体集合 |
| `skill-creator` | 创建、改进与评测技能 |
| `frontend-design` | 生产级前端界面设计 |
| `plugin-dev` | 插件开发工具包（hooks/MCP/命令/智能体） |
| `claude-code-setup` | 自动化配置推荐 |

### codex-plugins

| 插件 | 说明 |
| --- | --- |
| `compound-engineering` | 复合工程：从头脑风暴到交付的完整闭环（36 个技能） |

### zcodium-plugins

| 插件 | 说明 |
| --- | --- |
| `github` / `gitlab` | GitHub / GitLab CLI 工作流 |
| `alibaba-cloud-cli` | 阿里云 CLI 工作流 |
| `lark-cli` | 飞书 CLI 工作流 |
| `tencent-meeting-cli` | 腾讯会议 CLI |
| `dingtalk-cli` / `wecom-cli` | 钉钉 / 企业微信 CLI |
| `obsidian` | Obsidian 创作与可视化技能 |
| `mimosa` | 代码安全防护（hooks + 扫描） |
| `cloudbase-skills` | 腾讯云 CloudBase 开发技能 |
| `video2code` | 录屏/URL 复刻网页 |

### skills

| 插件 | 说明 |
| --- | --- |
| `zcodium-community-skills` | 精选技能合集（首批：Matt Pocock 工程技能 9 个） |

## 收录政策

- **知名且活跃**：优先社区高认可度、持续维护的插件；
- **许可明确**：仅收录允许再分发的许可（MIT / Apache-2.0 等），保留原 LICENSE 与版权声明；
- **运行时兼容**：仅收录 skills / commands / agents / hooks / mcpServers 组件，跳过 ZCodium 不支持的组件（LSP、outputStyles、channels 等）；
- **无官方依赖**：排除依赖官方付费套餐或官方平台认证的插件（如 ZCode 财务系列）。

## 维护

- 同步上游：按 [NOTICE.md](./NOTICE.md) 中的来源仓库与 revision 更新目录内容；
- 更新清单：新增插件后在 `scripts/generate_marketplace.py` 的 `ENTRIES` 中登记并运行：

  ```sh
  python3 scripts/generate_marketplace.py
  ```

- 本地验证（在 ZCodium 仓库中）：

  ```sh
  zcode plugins marketplace add /path/to/this/repo
  zcode plugins install <plugin>@zcodium-community-famous-plugins-and-skills
  zcode plugins list --json
  ```

## 许可

- 各插件版权归原作者所有，许可见各插件目录内的 `LICENSE` 文件与 [NOTICE.md](./NOTICE.md)；
- 本仓库新增的整理脚本与文档采用 MIT。
