---
name: migrate-to-shoehorn-cht
description: "把測試檔中的 as 型別斷言遷移到 @total-typescript/shoehorn。當使用者提到 shoehorn、想替換測試中的 as，或需要 partial test data 時使用。"
---

# 遷移到 @total-typescript/shoehorn

將 TypeScript 測試中的不安全 as 型別斷言改成 @total-typescript/shoehorn，讓 partial test data 更清楚且更安全。

## 何時使用

- 測試中有大量 as SomeType。
- 測試只需要建立部分物件，卻被完整型別逼迫補很多無關欄位。
- 使用者要求導入 @total-typescript/shoehorn。

## 工作流程

1. 檢查 package manager 與測試環境。
2. 確認是否已安裝 @total-typescript/shoehorn；若沒有，規劃新增依賴。
3. 搜尋測試檔中的 as type assertions。
4. 優先處理 test data builders、fixtures、inline test objects。
5. 將不安全 cast 改成 shoehorn helper。
6. 跑 typecheck 與相關測試。

## 原則

- 只遷移測試與 test utilities，不要碰 production code，除非使用者明確要求。
- 不要把所有 as const 或必要 narrowing 盲目移除。
- 保留測試意圖，避免因遷移改變測試行為。
- 若 cast 是在掩蓋 production type 設計問題，指出來，不要只機械替換。
