# Claude CLI Notes (TechNotes)

Personal cheat sheet for Claude (and related) CLI commands, workflows, and small terminal shortcuts.

Use by stage: **Plan → Test → Review → Secure → Fix → Summarize**

---

## Prompt template (high-signal)

- **Role**: who the assistant should be
- **Context**: repo/background/constraints
- **Task**: what you want done
- **Constraints**: rules (e.g., no network, specific libs)
- **Output format**: bullets / JSON / patch / etc.

---

## Workflow slash commands

- **/plan** — design first (components, interfaces, risks)
- **/tdd** — write tests first, then implement
- **/code-review** — catch logic/edge cases/nondeterminism
- **/security** — audit for secrets, unsafe tool use, OWASP-style issues
- **/build-fix** — diagnose build failures from logs/errors
- **/compact** — summarize to save context

---

## Keybind reminders

- **Ctrl+G** — open prompt in `$EDITOR`
- **Ctrl+J** — insert newline without sending
- **Cmd+P** — model picker
- **Ctrl+T** — toggle task list
- **Ctrl+B** — run separate features (note: verify exact behavior in your setup)

---

## Setup / install references

- `npx ecc-install python`
- `npm i -g @aisuite/chub`

Reference: https://github.com/affaan-m/everything-claude-code

---

## Project initialization

- **/init** — scans a repo and generates `CLAUDE.md`:
  - build commands
  - file structure
  - conventions

Review, tweak, and commit.

---

## Rules + subagents (file conventions)

- **Always-on instructions**: `CLAUDE.md`
- **Conditional rules**: `.claude/rules/*.md` (e.g. `.claude/rules/frontend.md`)
- **Subagents**: `.claude/agents/*.md`

---

## Hooks / guardrails (concepts)

Hooks you noted:
- `pretooluse`
- `posttooluse`
- notifications (e.g., `osascript`)

Guardrail idea: restrict allowed tools + required output formats to reduce unsafe/hallucinated actions.

---

## CLI flags / patterns (concepts)

- Headless / print:
  - `-p` / `--print` (depends on wrapper)

Examples:
- `claude --bare -p "prompt" --allowedtools "allowedTools"`
- `claude --worktree feature-auth`

---

## Terminal reminders

- Pipes: `cmd | grep ... | jq ...`
- `cat` prints file contents to stdout

---

## Reasoning keyword you noted

- **Ultrathink** — one-word “go deep” instruction
