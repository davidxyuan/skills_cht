---
name: tdd-cht
description: "使用 red-green-refactor loop 進行測試驅動開發。當使用者想用 TDD 建功能或修 bug、提到 red-green-refactor、想要 integration tests，或要求 test-first development 時使用。"
---

# Test-Driven Development

## 核心哲學

測試應透過 public interface 驗證行為，而不是綁定 implementation details。程式碼可以徹底重構，測試仍應保持有效。

好的測試偏 integration-style：透過 public API 執行真實 code path，描述系統做什麼，而不是怎麼做。壞測試會 mock 內部 collaborator、測 private method，或透過外部方式驗證內部狀態。

參考：tests.md、mocking.md、interface-design.md、deep-modules.md、refactoring.md。

## 反模式：Horizontal Slices

不要先寫全部測試，再寫全部實作。這會讓測試基於想像中的行為，而不是剛完成的真實垂直切片。

正確做法是 tracer bullets：一個測試、一個最小實作、再下一個測試。

~~~text
錯誤：
RED:   test1, test2, test3, test4
GREEN: impl1, impl2, impl3, impl4

正確：
RED -> GREEN: test1 -> impl1
RED -> GREEN: test2 -> impl2
RED -> GREEN: test3 -> impl3
~~~

## 工作流程

### 1. Planning

寫 code 前先確認 public interface、最重要行為、deep module 機會、interface 可測性，以及行為測試清單。

詢問：public interface 應該長什麼樣？哪些行為最重要？

### 2. Tracer Bullet

先寫一個測試確認一件事：RED 寫第一個行為測試並確認失敗，GREEN 寫最小程式讓它通過。

### 3. Incremental Loop

對每個剩餘行為：RED 寫下一個測試並確認失敗，GREEN 最小實作讓測試通過，REFACTOR 在測試保護下整理設計。

## 規則

- 不要測 private details。
- 不要過度 mock 內部 collaborator。
- 每次只新增一個行為測試。
- 先看測試失敗，避免假綠。
- 重構時保持測試綠燈。
- 測試名稱要讀起來像規格。

## 完成標準

關鍵行為被測試覆蓋、測試透過 public interface 驗證、相關測試通過、實作沒有為了測試暴露不必要 internals。
