---
name: ubiquitous-language-cht
description: "從目前對話抽出 DDD 風格 ubiquitous language glossary，標出歧義並提出 canonical terms。儲存到 UBIQUITOUS_LANGUAGE.md。當使用者想定義 domain terms、建立 glossary、強化術語、建立 ubiquitous language，或提到 domain model/DDD 時使用。"
---

# Ubiquitous Language

從目前對話與 codebase context 萃取 domain terms，建立 DDD 風格 ubiquitous language glossary。

## 工作流程

1. 探索目前對話與 repo 中的 domain 語言。
2. 收集候選 terms、同義詞、衝突詞與模糊詞。
3. 對每個 term 提出 canonical name、定義、非同義詞與例子。
4. 標出需要使用者確認的歧義。
5. 產生或更新 UBIQUITOUS_LANGUAGE.md。

## 輸出格式

~~~markdown
# Ubiquitous Language

## Terms

### Term

Definition.

Also known as: synonym
Not the same as: related-but-different term
Examples:
- example 1

## Ambiguities

- 問題與建議 canonical term

## Open Questions

- 需要 domain expert 回答的問題
~~~

## 原則

- 使用 domain expert 能理解的語言。
- 不要把 class、table、endpoint 當成 domain term，除非它們本來就是 domain 語言。
- 同一概念只選一個 canonical term。
- 不確定就標成 ambiguity，不要假裝已定義。
