# Language

架構改善要跟 domain language 對齊。名稱不一致會讓 agent 和人類都更難理解系統。

## 探索來源

- CONTEXT.md
- CONTEXT-MAP.md
- docs/adr/
- README、產品文件、issue 討論
- 測試名稱與 public API

## 要找的問題

- 同一概念有多個名字。
- 同一個詞在不同 context 指不同東西。
- 程式碼名稱是技術步驟，不是 domain action。
- domain term 只存在文件，不存在 public interface。
- 實作用詞和 ADR 決策矛盾。

## 改善方式

- 在建議重構時同步提出命名修正。
- 若 term 未定義，先請使用者確認 canonical term。
- 若命名改動很大，拆成獨立小步驟。
- 不要把 database/table 名稱誤當 domain language。
