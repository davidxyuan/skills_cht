---
name: triage-issue-cht
description: "透過探索 codebase triage bug 或 issue，找出 root cause，然後建立含 TDD 修復計畫的 GitHub issue。當使用者回報 bug、想 file issue、提到 triage，或想調查並規劃修復時使用。"
---

# Triage Issue

調查 bug 或 issue，理解 root cause，然後建立一個清楚、可執行、包含 TDD 修復計畫的 GitHub issue。

## 工作流程

1. 收集使用者描述：實際行為、預期行為、重現步驟、環境。
2. 探索 codebase，找到相關入口、domain terms、測試與相似問題。
3. 嘗試重現或用靜態分析確認可能路徑。
4. 若能定位，說明 root cause 或最可能原因。
5. 規劃 TDD 修復：第一個失敗測試、最小實作、後續測試。
6. 建立 GitHub issue，讓後續 agent 可直接接手。

## Issue 內容

包含 problem summary、expected behavior、current behavior、reproduction steps 或 evidence、relevant codebase context、suspected root cause、TDD fix plan、acceptance criteria 與 test plan。

## 原則

- 不要在 evidence 不足時過度確定。
- 不要直接修，除非使用者要求實作。
- 測試計畫應驗證 public behavior。
- 若 report 資訊不足，列出需要補充的具體問題。
