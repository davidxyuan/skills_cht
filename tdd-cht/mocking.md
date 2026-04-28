# Mocking 指南

Mock 是工具，不是預設。過度 mock 會讓測試驗證 implementation，而不是 behavior。

## 可以 mock 的東西

- 外部服務：payment provider、email service、third-party API。
- 不穩定或昂貴的邊界：network、filesystem、clock、randomness。
- 難以在測試環境安全執行的 side effects。

## 避免 mock 的東西

- 同一 module 內部 functions。
- private methods。
- 你可以直接透過 public interface 執行的 collaborator。
- 只是為了讓測試容易寫而切出來的 fake boundary。

## 判斷問題

如果重構內部 collaborator 名稱會讓測試失敗，這是壞訊號。如果測試主要在 assert calledWith，而不是 assert 行為結果，要小心。如果 mock setup 比行為本身還長，測試可能太貼 implementation。

## 建議

優先使用真實 collaborator，直到碰到真正外部邊界。把 mock 集中在系統邊界，而不是每一層內部。
