---
name: git-guardrails-codex-cht
description: "設定 Codex hooks，在 push、reset --hard、clean、branch -D 等危險 git 指令執行前阻擋。當使用者想防止破壞性 git 操作、加入 git 安全 hooks，或在 Codex 中阻擋 git push/reset 時使用。"
---

# Codex Git Guardrails 設定

設定 Codex `PreToolUse` hook，在 Codex 執行危險 git 指令前先攔截並阻擋。

## 預設阻擋

- `git push`，包含 force push
- `git reset --hard`
- `git clean -f` / `git clean -fd` / `git clean -xfd`
- `git branch -D`
- `git checkout .` / `git checkout -- .`
- `git restore .` / `git restore -- .`

被阻擋時，hook 會回傳 exit code `2`，並把阻擋原因寫到 stderr。

## 步驟

### 1. 詢問安裝範圍

詢問使用者要安裝到哪裡：

- **只套用目前專案**：`<repo>/.codex/`
- **套用所有專案**：`~/.codex/`

除非使用者明確要求，不要兩邊都安裝。

### 2. 檢查 Codex Hooks 支援

執行：

```bash
codex --version
codex features list
```

Codex hooks 需要 `codex_hooks` feature。若功能存在但未啟用，請在選定的 `config.toml` 中啟用。

### 3. 複製 Hook Script

內附 script 位於 [scripts/block-dangerous-git.py](scripts/block-dangerous-git.py)。

依安裝範圍複製：

- **專案**：`<repo>/.codex/hooks/block-dangerous-git.py`
- **全域**：`~/.codex/hooks/block-dangerous-git.py`

### 4. 啟用 `codex_hooks`

將下列設定合併到選定的 `config.toml`：

```toml
[features]
codex_hooks = true
```

專案範圍使用 `<repo>/.codex/config.toml`。全域範圍使用 `~/.codex/config.toml`。

若 `[features]` 已存在，只新增或更新 `codex_hooks`，不要覆蓋其他設定。

### 5. 新增 PreToolUse Hook

若同一個 config layer 尚未在 `config.toml` 中定義 hooks，優先使用 `hooks.json`。若該 layer 已有 `[hooks]`，請合併到既有 TOML hooks，不要在同一層同時建立第二種 hook 表示方式。

`hooks.json` 範例：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "^Bash$",
        "hooks": [
          {
            "type": "command",
            "command": "python \"<absolute-path-to>/block-dangerous-git.py\"",
            "statusMessage": "checking git guardrails"
          }
        ]
      }
    ]
  }
}
```

若檔案已存在，將此 matcher group 合併進 `hooks.PreToolUse`，不要覆蓋其他 hooks。

### 6. 詢問是否客製規則

詢問使用者是否要新增或移除 blocked patterns。若有需求，修改複製後的 script。

### 7. 驗證

直接測試 script：

```bash
echo '{"tool_name":"Bash","tool_input":{"command":"git push origin main"}}' | python <path-to-script>
echo '{"tool_name":"Bash","tool_input":{"command":"git status"}}' | python <path-to-script>
```

預期：

- `git push origin main` 回傳 exit code `2`，stderr 出現 `BLOCKED`。
- `git status` 回傳 exit code `0`。

## 注意事項

- 此 skill 是給 Codex 使用，不是 Claude Code。不要寫入 `.claude/settings.json`。
- 保留既有 Codex hooks，不要覆蓋。
- hook command 使用絕對路徑，避免不同工作目錄造成歧義。
- 若使用者的 Codex 版本沒有 `codex_hooks`，請回報需要先升級 Codex。
