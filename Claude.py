"""
Claude / CLI Notes (TechNotes)

What this is:
- A personal cheat sheet of Claude (and related) CLI commands + workflow tips.

Why it exists:
- To quickly recall "what to type" during a coding session (planning, TDD, review, security, fixing builds),
  and to document small productivity shortcuts (keybinds, flags, file conventions).

How to use:
- Skim the sections below depending on what stage you’re in:
  Plan → Test → Review → Secure → Fix → Summarize/Manage context.
"""

# -----------------------------------------------------------------------------
# 1) Prompt structure (for better results)
# -----------------------------------------------------------------------------
# A simple template for writing strong prompts:
# - Role: who the assistant should act as
# - Context: relevant background (repo, constraints, environment)
# - Task: what you want done
# - Constraints: rules (no network, specific libraries, etc.)
# - Format: exact output format you want (bullets, JSON, patch, etc.)

# -----------------------------------------------------------------------------
# 2) High-signal slash commands (workflow)
# -----------------------------------------------------------------------------
# /plan
#   Plan architecture before coding:
#   break the problem into components, define interfaces, and identify risks.

# /tdd
#   Test-driven development:
#   write tests first, then implement to catch silent failures early.

# /code-review
#   Automated review before commit:
#   spot logic errors, missing edge cases, and nondeterministic code paths.

# /security
#   Security audit:
#   check for prompt injection, leaked secrets, insecure tool use, OWASP-style issues.

# /build-fix
#   Diagnose and fix build failures from error output; trace root cause and apply a fix.

# /compact
#   Summarize the conversation to free up context window.

# ----------------------------------------------------------------------------
# 3) Useful shortcuts / keybind reminders
# ----------------------------------------------------------------------------
# Ctrl+G  : Open prompt in $EDITOR
# Ctrl+J  : Insert newline without sending
# Cmd+P   : Open model picker
# Ctrl+T  : Toggle task list

# -----------------------------------------------------------------------------
# 4) Setup / install references
# -----------------------------------------------------------------------------
# Install helpers (examples you’ve referenced):
# - npx ecc-install python
# - npm i -g @aisuite/chub
#
# Source you noted:
# - github.com/affaan-m/everything-claude-code

# -----------------------------------------------------------------------------
# 5) Project initialization
# -----------------------------------------------------------------------------
# /init
#   Scans a repo and generates CLAUDE.md with:
#   - build commands
#   - file structure
#   - conventions
#   Review, tweak, and commit it.

# -----------------------------------------------------------------------------
# 6) Rules + subagents (file conventions)
# -----------------------------------------------------------------------------
# Always-on project instructions:
# - CLAUDE.md (loaded for the whole repo/session)

# Conditional rules (loaded only when relevant files are touched):
# - .claude/rules/*.md
# Example:
# - .claude/rules/frontend.md

# Subagents:
# - Markdown files in .claude/agents/

# -----------------------------------------------------------------------------
# 7) Hooks / guardrails (concept notes)
# -----------------------------------------------------------------------------
# Hooks you noted:
# - pretooluse
# - posttooluse
# - notifications (e.g., osascript)

# Guardrails idea:
# - constrain allowed tools and output format to reduce hallucinations / unsafe actions.

# -----------------------------------------------------------------------------
# 8) CLI flags / patterns you noted
# -----------------------------------------------------------------------------
# Headless / print usage (conceptual):
# - "-p" / "--print": run headless, print output, and exit (depending on the CLI wrapper)

# Example patterns you wrote down:
# - claude --bare -p "prompt" --allowedtools "allowedTools"
# - claude --worktree feature-auth

# -----------------------------------------------------------------------------
# 9) Misc terminal reminders
# -----------------------------------------------------------------------------
# grep / jq + pipes:
# - use pipes to filter output: cmd | grep ... | jq ...

# cat:
# - "concatenate" → prints file contents to stdout

# -----------------------------------------------------------------------------
# 10) Reasoning mode keyword you noted
# -----------------------------------------------------------------------------
# "Ultrathink"
# - One-word instruction you noted for maximum reasoning depth.
