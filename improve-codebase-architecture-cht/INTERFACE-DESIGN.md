# Interface Design

好的 interface 讓正確使用變容易，讓錯誤使用變困難。

## 檢查問題

- Caller 真正想完成的工作是什麼？
- Caller 是否被迫傳入它不該知道的低階資料？
- 是否有合法狀態可用 type 或 API 形狀表達？
- 是否有多個 methods 必須按固定順序呼叫？如果有，能否收斂？
- 回傳值是否讓下一步操作自然且安全？

## 建議

- 先設計使用範例，再決定 signature。
- 優先暴露 domain operation，而不是 persistence 或 transport 細節。
- 把可變狀態和生命週期藏在 module 內部。
- 為常見路徑最佳化，但保留必要 escape hatch。

## 反模式

- interface 只是把內部 class 原樣暴露。
- 每個 collaborator 都被注入，caller 需要知道整個組裝方式。
- API 允許大量無效組合，靠 runtime error 補救。
