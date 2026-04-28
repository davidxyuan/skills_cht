---
name: setup-pre-commit-cht
description: "在目前 repo 設定 Husky pre-commit hooks，包含 lint-staged、Prettier、type checking 與 tests。當使用者想加入 pre-commit hooks、設定 Husky、設定 lint-staged，或在 commit 時跑 formatting/typechecking/testing 時使用。"
---

# Setup Pre-Commit

為 repo 設定 commit 前檢查，讓格式、型別與測試問題更早被發現。

## 工作流程

1. 偵測 package manager：npm、pnpm、yarn、bun。
2. 檢查是否已有 Husky、lint-staged、Prettier、typecheck/test scripts。
3. 依 repo 既有慣例新增或更新設定。
4. 設定 pre-commit hook：對 staged files 跑 Prettier 或 lint-staged，跑 typecheck，跑快速且適合 commit-time 的 tests。
5. 避免加入過慢或需要外部服務的檢查。
6. 跑一次驗證命令，確認 hook script 可執行。

## 原則

- 不要覆蓋既有 hooks，先讀再合併。
- 使用 repo 既有 script 名稱，不硬塞新命名。
- commit-time 檢查要快；完整 E2E 更適合 CI。
- 若 repo 不是 Node 專案，先說明 Husky 是否適合。
