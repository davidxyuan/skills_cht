---
name: design-an-interface-cht
description: "使用平行子代理為模組產生多個差異很大的 interface 設計。當使用者想設計 API、探索 interface 選項、比較模組形狀，或提到 design it twice 時使用。"
---

# 設計 Interface

依據 A Philosophy of Software Design 的 Design It Twice 精神：第一個想法通常不是最好的。請產生多個差異很大的設計，再比較取捨。

## 工作流程

### 1. 收集需求

設計前先理解：

- 這個模組要解決什麼問題？
- 呼叫者是誰？其他模組、外部使用者、測試？
- 核心操作有哪些？
- 有哪些限制？效能、相容性、既有模式？
- 什麼應該藏在內部，什麼應該暴露？

詢問：這個模組需要做什麼？誰會使用它？

### 2. 產生設計

使用 Task tool 同時啟動 3 個以上子代理。每個子代理都必須產生一個明顯不同的方案。

~~~text
替下列模組設計 interface：[module description]
需求：[gathered requirements]
本設計的限制：[每個代理指定不同限制]
- Agent 1：方法數最少，目標 1 到 3 個 methods
- Agent 2：彈性最大，支援多種 use cases
- Agent 3：針對最常見情境最佳化
- Agent 4：參考 [specific paradigm/library]

輸出格式：
1. Interface signature（types/methods）
2. 使用範例（caller 如何使用）
3. 這個設計在內部隱藏什麼
4. 此方案的取捨
~~~

### 3. 呈現設計

每個設計都要包含 interface signature、使用範例，以及它隱藏的複雜度。依序呈現，讓使用者先理解每個方案，再進入比較。

### 4. 比較設計

比較 interface 簡潔度、通用 vs 專用、實作效率、深度、正確使用是否容易、誤用是否困難。用自然語言討論，不要只丟表格。

### 5. 綜合

最佳設計常常結合多個方案的洞見。詢問哪個設計最符合主要 use case，以及其他方案是否有值得納入的元素。

## 反模式

- 不要讓子代理產生相似設計。
- 不要跳過比較。
- 不要開始實作，此 skill 只討論 interface 形狀。
- 不要只依實作工作量評估設計。
