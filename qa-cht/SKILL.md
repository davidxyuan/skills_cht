---
name: qa-cht
description: "互動式 QA session：使用者用對話方式回報 bug 或問題，agent 在背景探索 codebase 並建立 GitHub issues。當使用者想回報 bug、做 QA、用對話方式 filing issues，或提到 QA session 時使用。"
---

# QA Session

讓使用者用自然對話回報 bug、體驗問題或改善點。agent 同時探索 codebase，補上 domain language 與技術 context，最後建立清楚的 GitHub issues。

## 工作方式

1. 讓使用者描述問題，不要求一開始就填完整表單。
2. 背景探索 codebase，找相關 domain、UI、API、測試與既有 issues。
3. 對每個回報釐清重現步驟、預期行為、實際行為、影響範圍、嚴重度。
4. 若能合理重現或定位，記錄觀察到的 evidence。
5. 將每個獨立問題整理成 GitHub issue。
6. 對不明確的回報，提出具體追問。

## Issue 品質

每個 issue 應包含問題摘要、可觀察行為、重現步驟或觸發條件、預期行為、實際行為、相關 codebase context、建議測試或修復方向。

## 原則

- 不要讓使用者被表單拖慢；先聽，再整理。
- 不要把多個獨立 bug 塞成同一個 issue。
- 不要在沒有 evidence 時假裝已確認根因。
- GitHub comment 或 issue 需要 AI 聲明時，遵守 repo 慣例。
