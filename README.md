# Agent Skills For Real Engineers 繁體中文翻譯版

這個 repo 是 mattpocock/skills 的繁體中文翻譯與改作版本，目標是讓繁體中文使用者更快理解每個 agent skill 的用途與工作流程。

原專案是 Matt Pocock 日常使用的工程 agent skills。此 repo 保留原本的 MIT License，並將 skill 說明、流程、輔助文件翻成繁體中文。技術字串、指令、package 名稱、API 名稱、檔名與 shell script 盡量保留原文。

## 來源與授權

- 原始專案：https://github.com/mattpocock/skills
- 原作者：Matt Pocock
- 原授權：MIT License
- 翻譯維護者：davidxyuan
- 正式授權條款請以本 repo 的 LICENSE 為準。
- 此版本不是原作者維護或背書的版本，翻譯內容可能與上游更新不同步。

更多說明請見 TRANSLATION_NOTICE.md。

## 安裝方式

每個 skill 目錄都加上 -cht 後綴，方便與英文版共存。例如英文版 $tdd 可和中文版 $tdd-cht 同時存在。

使用 Codex 內建 installer 一次安裝全部 skills：

~~~powershell
python "C:\Users\david.yuan\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --repo davidxyuan/skills_cht --path caveman-cht design-an-interface-cht domain-model-cht edit-article-cht git-guardrails-claude-code-cht git-guardrails-codex-cht github-triage-cht grill-me-cht improve-codebase-architecture-cht migrate-to-shoehorn-cht obsidian-vault-cht qa-cht request-refactor-plan-cht scaffold-exercises-cht setup-pre-commit-cht tdd-cht to-issues-cht to-prd-cht triage-issue-cht ubiquitous-language-cht write-a-skill-cht zoom-out-cht
~~~

安裝完成後請重啟 Codex。

## Planning & Design

這些 skills 幫你在寫程式前把問題想清楚。

- **to-prd-cht** — 把目前對話整理成 PRD，並準備成 GitHub issue。
- **to-issues-cht** — 把 plan、spec 或 PRD 切成可獨立認領的 GitHub issues。
- **grill-me-cht** — 以嚴格訪談方式追問計畫或設計，直到決策樹每個分支都被釐清。
- **design-an-interface-cht** — 為模組產生多個差異很大的 interface 設計，並比較取捨。
- **request-refactor-plan-cht** — 透過訪談建立小步提交的重構計畫，再整理成 GitHub issue。

## Development

這些 skills 幫你寫程式、重構與修 bug。

- **tdd-cht** — 使用 red-green-refactor 的 TDD 流程，一次完成一個垂直切片。
- **triage-issue-cht** — 探索 codebase、找出 bug 根因，並建立含 TDD 修復計畫的 GitHub issue。
- **improve-codebase-architecture-cht** — 根據 CONTEXT.md 與 docs/adr/ 找出 codebase 的架構深化機會。
- **migrate-to-shoehorn-cht** — 把測試中的 TypeScript as 型別斷言遷移到 @total-typescript/shoehorn。
- **scaffold-exercises-cht** — 建立課程練習目錄、題目、解答與說明文件。

## Tooling & Setup

- **setup-pre-commit-cht** — 設定 Husky pre-commit hooks、lint-staged、Prettier、型別檢查與測試。
- **git-guardrails-claude-code-cht** — 設定 Claude Code hooks，在危險 git 指令執行前阻擋。
- **git-guardrails-codex-cht** — 設定 Codex hooks，在危險 git 指令執行前阻擋。

## Writing & Knowledge

- **write-a-skill-cht** — 建立新的 agent skill，包含正確結構、漸進揭露與附加資源。
- **edit-article-cht** — 編輯文章草稿，重整段落、改善清晰度並精煉文字。
- **ubiquitous-language-cht** — 從目前對話抽出 DDD 風格 ubiquitous language 詞彙表。
- **obsidian-vault-cht** — 搜尋、建立與整理 Obsidian vault 筆記，支援 wikilinks 與 index notes。
