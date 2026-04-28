# Deep Modules

deep module = 小 interface，深實作。它對 caller 隱藏大量複雜度。

## 為什麼 TDD 需要 deep modules

如果 module 很淺，測試會被迫知道很多內部步驟。deep module 讓測試透過少量 public operations 驗證高價值行為。

## 好訊號

- 一個 public method 代表完整 domain action。
- caller 不需要知道內部 orchestration。
- 測試不需要 mock 一串內部 collaborator。
- 重構內部不影響測試。

## 壞訊號

- 很多小 methods 必須固定順序呼叫。
- public API 暴露 implementation state。
- 測試要 assert 多個 internal calls。

## 做法

先用測試描述使用者想完成的行為，再讓 interface 往深模組收斂。
