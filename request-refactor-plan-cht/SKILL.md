---
name: request-refactor-plan-cht
description: "透過使用者訪談建立詳細 refactor plan，拆成小 commits，然後建立 GitHub issue。當使用者想規劃重構、建立 refactoring RFC，或把重構拆成安全增量步驟時使用。"
---

# Request Refactor Plan

透過訪談把重構需求變成安全、可執行、可追蹤的小步計畫，最後整理成 GitHub issue。

## 工作流程

1. 探索 codebase，理解目前結構、測試、domain language 與既有 ADR。
2. 訪談使用者，確認重構目標、非目標、風險與成功標準。
3. 找出可以保護行為的測試或需先補的測試。
4. 將重構拆成 tiny commits，每一步都應可獨立 review、可回滾。
5. 明確標示每一步的驗證方式。
6. 建立 GitHub issue，內容包含背景、計畫、測試策略與 acceptance criteria。

## 計畫原則

- 小步驟勝過大搬家。
- 先保護行為，再調整結構。
- 每個 commit 都應讓 codebase 處於可運作狀態。
- 不把 unrelated cleanup 混入核心重構。
- 若需要改 public API，清楚說明相容性策略。
