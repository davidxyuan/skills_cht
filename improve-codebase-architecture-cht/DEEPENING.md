# Deepening

deep module 的特徵是 interface 小、功能深。呼叫端只需要知道很少事情，內部卻能處理大量複雜度。

## 好訊號

- 多個呼叫端重複同一段協調流程。
- 呼叫端需要知道太多順序、flag 或內部資料形狀。
- 測試必須 mock 很多內部 collaborator 才能驗證一個行為。
- domain 概念分散在多個低階 helper 中。

## 重構方向

- 將重複 orchestration 收斂成單一 public operation。
- 把 implementation details 留在 module 內部。
- 讓 public interface 以 domain action 命名，而不是以資料搬運步驟命名。
- 用行為測試保護外部 contract，再重排內部。

## 避免

- 只為了檔案乾淨而切更多 shallow modules。
- 替每個小 helper 建 interface。
- 在沒有測試保護時做大型搬移。
