# Out-of-Scope Knowledge Base

.out-of-scope/ 用來記錄已被拒絕或暫不處理的 enhancement concept，避免未來重複討論同一件事。

## 何時建立

只有在 enhancement 被決定為 wontfix 時建立。bug 不需要寫入 .out-of-scope/，除非它其實是 feature request。

## 檔案位置

.out-of-scope/<short-concept-name>.md

## 範本

~~~markdown
# Concept Name

## Summary

這個想法是什麼。

## Why It Was Rejected

為什麼目前不做。說明 domain、產品、技術或維護上的理由。

## Signals That Might Reopen This

未來什麼情況改變時，可以重新考慮。

## Related Issues

- #123
- #456
~~~

## Triage 時如何使用

當新 issue 與 .out-of-scope/ 中的概念相似：指出相似記錄、摘要拒絕原因、詢問 maintainer 是否仍維持、並依決定關閉或重新打開討論。

## 原則

- out-of-scope 不是垃圾桶，而是決策記憶。
- 寫清楚重新打開的條件，避免永久封死好想法。
- 不要用它羞辱 reporter；GitHub comment 要保持禮貌。
