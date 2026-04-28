# ADR 格式

ADR 用來記錄難以反悔、沒有脈絡會令人意外、且來自真實取捨的決策。

## 檔名

使用：docs/adr/0001-short-kebab-case-title.md

多 context repo 中，context-specific ADR 放在該 context 的 docs/adr/ 底下。

## 範本

~~~markdown
# 0001: Short Decision Title

## Status

Accepted

## Context

描述造成此決策的背景。說明有哪些力量互相拉扯，以及為什麼這不是顯而易見的選擇。

## Decision

說明我們決定做什麼。語氣要清楚直接。

## Consequences

說明這個決策帶來的好處、代價與後續限制。要包含不好的部分，ADR 不是宣傳稿。

## Alternatives Considered

列出重要替代方案，以及沒有選擇它們的原因。
~~~

## 原則

- 不要為顯而易見或容易改的事情寫 ADR。
- 不要記錄純粹實作細節，除非它代表重大的 domain 或架構取捨。
- 保留決策理由，而不是只保留結論。
