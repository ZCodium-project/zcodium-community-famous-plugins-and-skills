# Provenance & Licenses

本仓库聚合的插件均为上游开源项目的 vendor（复制）版本，按下表登记来源、revision 与许可。
更新上游内容时，请同步更新本表。

## 来源登记

| 目录 | 来源仓库 | Revision | 许可 | 覆盖范围 |
| --- | --- | --- | --- | --- |
| `claude-code-plugins/superpowers` | https://github.com/obra/superpowers | `8ca22dba9a94f28898bbce59f2537ff4d87c747d` | MIT | 该仓库完整内容（排除 `.git` / `.github`） |
| `claude-code-plugins/code-review` | https://github.com/anthropics/claude-plugins-official | `d182ca456ca09d31d139f7d3818d1d333b103cce` | Apache-2.0 | `plugins/code-review` |
| `claude-code-plugins/commit-commands` | https://github.com/anthropics/claude-plugins-official | `d182ca456ca09d31d139f7d3818d1d333b103cce` | Apache-2.0 | `plugins/commit-commands` |
| `claude-code-plugins/security-guidance` | https://github.com/anthropics/claude-plugins-official | `d182ca456ca09d31d139f7d3818d1d333b103cce` | Apache-2.0 | `plugins/security-guidance` |
| `claude-code-plugins/pr-review-toolkit` | https://github.com/anthropics/claude-plugins-official | `d182ca456ca09d31d139f7d3818d1d333b103cce` | Apache-2.0 | `plugins/pr-review-toolkit` |
| `claude-code-plugins/skill-creator` | https://github.com/anthropics/claude-plugins-official | `d182ca456ca09d31d139f7d3818d1d333b103cce` | Apache-2.0 | `plugins/skill-creator` |
| `claude-code-plugins/frontend-design` | https://github.com/anthropics/claude-plugins-official | `d182ca456ca09d31d139f7d3818d1d333b103cce` | Apache-2.0 | `plugins/frontend-design` |
| `claude-code-plugins/plugin-dev` | https://github.com/anthropics/claude-plugins-official | `d182ca456ca09d31d139f7d3818d1d333b103cce` | Apache-2.0 | `plugins/plugin-dev` |
| `claude-code-plugins/claude-code-setup` | https://github.com/anthropics/claude-plugins-official | `d182ca456ca09d31d139f7d3818d1d333b103cce` | Apache-2.0 | `plugins/claude-code-setup` |
| `codex-plugins/compound-engineering` | https://github.com/EveryInc/compound-engineering-plugin | `030188b4ba27f2dc33fbc4d5a112d3c8cc893e8c` | MIT | 该仓库内容（排除 `.git`；`index.js` 引用的 `.opencode/` 目录未包含，ZCodium 运行时不使用该入口） |
| `zcodium-plugins/github` | https://github.com/zai-org/zcode-plugins | `c94279c9a449235fd5991f7903a6c7e4fdc3ab7e` | Apache-2.0 | `plugins/github` |
| `zcodium-plugins/gitlab` | https://github.com/zai-org/zcode-plugins | `c94279c9a449235fd5991f7903a6c7e4fdc3ab7e` | Apache-2.0 | `plugins/gitlab` |
| `zcodium-plugins/alibaba-cloud-cli` | https://github.com/zai-org/zcode-plugins | `c94279c9a449235fd5991f7903a6c7e4fdc3ab7e` | Apache-2.0 | `plugins/alibaba-cloud-cli` |
| `zcodium-plugins/lark-cli` | https://github.com/zai-org/zcode-plugins | `c94279c9a449235fd5991f7903a6c7e4fdc3ab7e` | Apache-2.0 | `plugins/lark-cli` |
| `zcodium-plugins/tencent-meeting-cli` | https://github.com/zai-org/zcode-plugins | `c94279c9a449235fd5991f7903a6c7e4fdc3ab7e` | Apache-2.0 | `plugins/tencent-meeting-cli` |
| `zcodium-plugins/dingtalk-cli` | https://github.com/zai-org/zcode-plugins | `c94279c9a449235fd5991f7903a6c7e4fdc3ab7e` | Apache-2.0 | `plugins/dingtalk-cli` |
| `zcodium-plugins/wecom-cli` | https://github.com/zai-org/zcode-plugins | `c94279c9a449235fd5991f7903a6c7e4fdc3ab7e` | Apache-2.0 | `plugins/wecom-cli` |
| `zcodium-plugins/obsidian` | https://github.com/zai-org/zcode-plugins | `c94279c9a449235fd5991f7903a6c7e4fdc3ab7e` | Apache-2.0 | `plugins/obsidian`（技能内容源自 kepano/obsidian-skills 与 axtonliu/axton-obsidian-visual-skills，见插件内说明） |
| `zcodium-plugins/mimosa` | https://github.com/zai-org/zcode-plugins | `c94279c9a449235fd5991f7903a6c7e4fdc3ab7e` | Apache-2.0 | `plugins/mimosa` |
| `zcodium-plugins/cloudbase-skills` | https://github.com/zai-org/zcode-plugins | `c94279c9a449235fd5991f7903a6c7e4fdc3ab7e` | Apache-2.0 | `plugins/cloudbase-skills` |
| `zcodium-plugins/video2code` | https://github.com/zai-org/zcode-plugins | `c94279c9a449235fd5991f7903a6c7e4fdc3ab7e` | Apache-2.0 | `plugins/video2code` |
| `skills/` | https://github.com/mattpocock/skills | `4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d` | MIT | `skills/engineering` 下 9 个技能：`tdd`、`code-review`、`diagnosing-bugs`、`research`、`to-spec`、`implement`、`pr`、`prototype`、`improve-codebase-architecture` |

## 说明

- 各来源的完整许可文本保存在对应插件目录（及上游仓库）中；本仓库未修改或移除任何版权声明。
- `zcodium-plugins/` 迁移自 ZCode 官方公开市场仓库 `zai-org/zcode-plugins`（Apache-2.0），未收录依赖官方付费套餐或官方平台认证的插件（财务与市场数据 MCP 系列）。
- 已审核但**未收录**的来源：`openai/skills`（已废弃）、`openai/plugins`、`anthropics/skills`、`vercel-labs/agent-skills` —— 这些仓库当前未声明再分发许可，待上游明确许可后再评估收录。
- 新增 vendor 内容时：登记来源与 revision、保留 LICENSE、在 `scripts/generate_marketplace.py` 中登记条目并重新生成 `marketplace.json`。
