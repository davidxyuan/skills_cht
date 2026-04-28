---
name: improve-codebase-architecture-cht
description: "根據 CONTEXT.md 的 domain language 與 docs/adr/ 的決策，找出 codebase 的 deepening 機會。當使用者想改善架構、找重構機會、整合高耦合模組，或讓 codebase 更可測、更容易被 AI 導覽時使用。"
---

# 改善 Codebase 架構

尋找能讓 codebase 更清楚、更深、更可測、更容易被 agent 理解的重構機會。

## 核心觀點

好的架構不是檔案變多，而是 module boundary 更有意義。優先找出可形成 deep module 的地方：小而穩定的 interface，內部封裝大量複雜度。

## 工作流程

1. 探索 repo 結構、主要入口、測試、README、CONTEXT.md、docs/adr/。
2. 理解 domain language，找出程式碼是否使用相同詞彙。
3. 找出高耦合、重複流程、薄 wrapper、跨 module 泄漏細節的區域。
4. 對每個機會提出：問題、為何重要、建議 boundary、測試方式、風險。
5. 只提出值得做的重構，不要為了整理而整理。

## 評估面向

- 是否能減少呼叫端需要知道的細節？
- 是否能讓測試透過 public interface 驗證行為？
- 是否能把 domain 概念用一致詞彙表達？
- 是否能降低跨模組修改的連鎖反應？
- 是否符合既有 ADR 或明確指出需要新 ADR？

## 輸出

用少量高價值建議，而不是長清單。每個建議都要能被拆成小步驟，並說明第一個安全切片。

參考：DEEPENING.md、INTERFACE-DESIGN.md、LANGUAGE.md。
