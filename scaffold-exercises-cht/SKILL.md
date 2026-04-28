---
name: scaffold-exercises-cht
description: "建立 exercise directory structures，包含 sections、problems、solutions 與 explainers，並確保通過 linting。當使用者想 scaffold exercises、建立 exercise stubs 或新增 course section 時使用。"
---

# Scaffold Exercises

建立課程練習結構，讓每個題目都有清楚的 problem、solution 與 explainer。

## 工作流程

1. 先理解既有課程目錄慣例與命名格式。
2. 確認 section、exercise 數量、題目主題與難度排序。
3. 建立每個 exercise 的 problem starter、solution、explainer。
4. 若 repo 有 lint、typecheck、測試或 course validation，跑相關檢查。
5. 修正 scaffold 後的格式與 lint 問題。

## 結構原則

- 題目應循序漸進，前一題教會下一題需要的概念。
- problem 只給必要線索，不洩漏 solution。
- solution 要是可執行、可檢查的完整答案。
- explainer 要說明為什麼這樣做，而不只是貼答案。
- 遵循 repo 既有檔名與資料夾格式，不發明新框架。
