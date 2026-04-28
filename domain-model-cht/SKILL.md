---
name: domain-model-cht
description: "以追問方式檢查計畫是否符合既有 domain model，精煉術語，並在決策成形時更新 CONTEXT.md 與 ADR。當使用者想用專案語言和既有決策壓力測試計畫時使用。"
disable-model-invocation: true
---

# Domain Model 壓力測試

針對計畫的每個面向持續訪談，直到雙方有共同理解。沿著設計決策樹逐步往下走，一次解決一個決策依賴。每個問題都提供你的建議答案。

一次只問一個問題，等使用者回覆後再繼續。如果問題可透過探索 codebase 回答，就先探索，不要問使用者。

## Domain awareness

探索 codebase 時，同時尋找既有文件。

多數 repo 只有單一 context：

~~~text
/
├── CONTEXT.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
~~~

若根目錄有 CONTEXT-MAP.md，代表 repo 有多個 contexts。map 會指出各 context 位置。

只在有東西要寫時才建立檔案。若沒有 CONTEXT.md，在第一個 term 被確認時建立。若沒有 docs/adr/，在第一個 ADR 需要時建立。

## 訪談期間

### 對照 glossary 挑戰

當使用者用的詞和 CONTEXT.md 既有語言衝突，立即指出。例如：你的 glossary 把 cancellation 定義為 X，但你現在似乎指 Y；哪個才對？

### 精煉模糊語言

當使用者使用模糊或多義詞時，提出精準 canonical term。例如：你說 account，是指 Customer 還是 User？這兩者不同。

### 討論具體情境

討論 domain 關係時，用具體 scenario 壓力測試。發明可探測邊界的 edge cases，逼出概念之間的界線。

### 與程式碼交叉檢查

使用者描述系統行為時，檢查程式碼是否一致。若有矛盾，提出來：程式碼取消的是整張 Order，但你剛說可以部分取消；哪個才是正確 domain 行為？

### 即時更新 CONTEXT.md

term 一旦確認，就立刻更新 CONTEXT.md。不要批次累積。格式使用 CONTEXT-FORMAT.md。

不要讓 CONTEXT.md 綁死實作細節。只放 domain expert 有意義的詞。

### 謹慎提出 ADR

只有同時符合三項才提出建立 ADR：

1. 難以反悔：未來改變主意成本明顯。
2. 沒有 context 會令人意外：未來讀者會想知道為什麼這樣做。
3. 真正取捨的結果：有真實替代方案，而且基於具體理由選了一個。

任何一項不符合，就跳過 ADR。格式使用 ADR-FORMAT.md。
