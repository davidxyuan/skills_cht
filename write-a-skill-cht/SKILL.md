---
name: write-a-skill-cht
description: "建立新的 agent skills，包含正確結構、漸進揭露與 bundled resources。當使用者想建立、撰寫或設計新 skill 時使用。"
---

# Write a Skill

協助建立新的 agent skill。Skill 應該讓 agent 在特定工作中表現更穩定，而不是只是一段一般提示詞。

## 好 skill 的特徵

- 有清楚觸發條件。
- 描述具體工作流程。
- 包含 agent 容易忘記的重要規則。
- 使用 progressive disclosure：主檔簡潔，細節放在 companion docs。
- 若有 scripts、templates、assets，可一起 bundled。

## 結構

~~~text
skill-name/
├── SKILL.md
├── references/
├── scripts/
└── templates/
~~~

SKILL.md 必須包含 frontmatter：

~~~markdown
---
name: skill-name
description: "何時使用這個 skill。要包含觸發條件。"
---
~~~

## 工作流程

1. 訪談使用者，確認 skill 要改善哪個重複工作。
2. 定義 trigger：使用者會怎麼說？任務有什麼訊號？
3. 設計 workflow：agent 要做哪些步驟？哪些步驟可探索，哪些需要問？
4. 寫 rules：哪些錯誤一定要避免？
5. 規劃 companion docs 或 scripts，只放真正有用的資源。
6. 建立 skill 目錄與檔案。
7. 給出使用範例與安裝/重啟提示。

## 撰寫原則

- description 要像 routing rule，不只是介紹。
- 不要把所有知識塞在 SKILL.md；長參考資料拆出去。
- 不要寫模糊人格指令，要寫可執行流程。
- 如果 skill 需要 tools，清楚說明何時使用。
- 用範例展示預期行為。
