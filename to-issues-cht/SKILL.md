---
name: to-issues-cht
description: "把 plan、spec 或 PRD 拆成可獨立認領的 GitHub issues，使用 tracer-bullet vertical slices。當使用者想把計畫轉成 issues、建立 implementation tickets，或把工作拆成 issues 時使用。"
---

# Convert Plan to Issues

把已確認的 plan、spec 或 PRD 拆成可獨立認領、可驗證、適合 agent 或工程師執行的 GitHub issues。

## 核心原則

使用 vertical slices，而不是 horizontal tasks。每個 issue 都應交付一小段可觀察價值，並讓系統維持可運作。

不要這樣拆：建 schema、建 API、建 UI、寫測試。

應該這樣拆：使用者可以建立最小可用資源、使用者可以看到列表、使用者可以處理錯誤狀態。

## 工作流程

1. 讀目前計畫與 codebase context。
2. 找出第一個 tracer bullet：最小端到端切片。
3. 將後續能力拆成獨立 vertical slices。
4. 每個 issue 包含 problem、scope、acceptance criteria、test plan。
5. 明確標示相依順序，但避免過度序列化。
6. 建立 GitHub issues。

## Issue 品質

每個 issue 應可由一個 agent 或工程師獨立處理，有明確完成條件，有測試或驗證方式，不需要再做重大產品決策，且不與其他 issue 大量重疊。
