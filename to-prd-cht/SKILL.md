---
name: to-prd-cht
description: "把目前對話 context 轉成 PRD，並提交為 GitHub issue。當使用者想從目前 context 建立 PRD 時使用。"
---

# To PRD

將目前對話與 codebase 理解整理成 PRD。不要重新訪談使用者；只整合已知資訊。

## 流程

1. 若尚未探索 repo，先探索目前 codebase 狀態。
2. 草擬需要建立或修改的主要 modules，主動尋找可抽成 deep modules 的機會。
3. 與使用者確認 modules 是否符合預期，以及哪些 modules 需要測試。
4. 使用下列 template 寫 PRD，並提交為 GitHub issue。

## PRD Template

~~~markdown
## Problem Statement

從使用者角度描述目前面臨的問題。

## Solution

從使用者角度描述解法。

## User Stories

1. As an <actor>, I want a <feature>, so that <benefit>

請列出足夠完整的 user stories，涵蓋 feature 的主要面向。

## Implementation Decisions

列出已做出的 implementation decisions，例如 modules、interfaces、技術澄清、架構決策、schema changes、API contracts 與特定互動。不要放容易過期的細節檔案路徑或 code snippets。

## Testing Decisions

列出 testing decisions：好測試應驗證外部行為，而不是 implementation details；哪些 modules 會被測試；codebase 中可參考的 prior art。

## Out of Scope

描述此 PRD 不包含的事項。

## Further Notes

其他補充。
~~~
