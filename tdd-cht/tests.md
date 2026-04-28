# 測試指南

好的測試描述外部行為。它們應該像規格，而不是像 implementation snapshot。

## 好測試

- 透過 public API 或使用者可觸發入口執行。
- 驗證使用者可觀察結果。
- 名稱描述行為，例如 user can checkout with a valid cart。
- 重構內部時不應失敗。

## 壞測試

- 測 private method。
- mock 太多內部 collaborator。
- 驗證內部呼叫次數而非結果。
- 只檢查資料結構形狀，沒有驗證行為。

## 寫測試流程

1. 選一個最重要行為。
2. 寫測試名稱，像一句規格。
3. 透過 public interface 安排情境。
4. 執行行為。
5. 驗證外部結果。
6. 確認測試先失敗，再寫實作。

## Mocking

mock 外部邊界可以，例如 network、filesystem、payment provider。不要 mock 你正在設計的內部 collaborator，否則測試會綁死 implementation。
