# Interface Design for Testability

可測的 interface 不代表暴露 internals。好的 interface 讓測試能用外部行為驗證系統。

## 原則

- 測試 public interface。
- interface 應以 domain action 表達。
- 回傳值或 observable effect 要足以驗證結果。
- 不要為了測試新增 production-only 不需要的 getter。
- 把 time、random、network 等外部邊界設計成可替換。

## 好設計

caller 可以說 checkout(cart)、cancelOrder(orderId)、measure(cameraSettings)。測試可以安排情境、呼叫 public method、驗證結果。

## 壞設計

caller 必須知道先呼叫 A，再 B，再手動 flush C，最後讀 internal state D。這表示 module boundary 太淺。
