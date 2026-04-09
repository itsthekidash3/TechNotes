# /plan — Plan Architecture Before Coding
# Decompose your problem into components, define interfaces, and identify risks before writing a line of code. Prevents the "build first, think later" trap.

# /tdd — Test-Driven Development
# Write tests first, then implement. Catches silent failures early — exactly the kind of bugs that plague agent systems.

# /code-review — Review Your Changes
#nAutomated quality review before you commit. Spots logic errors, missing edge cases, and code that should be deterministic vs. LLM-driven.

# /security — Security Audit
# Scan for prompt injection, leaked secrets, insecure tool use, and OWASP vulnerabilities. Essential when your agents have tool access.

# /build-fix — Fix Build Errors
# Automatically diagnose and fix build failures. Reads error output, traces the root cause, and applies the fix — so you stay in flow.

# chub — Context Hub: Curated API Docs
# Agents fetch verified API docs instead of guessing. Annotates gaps it discovers so the next session starts smarter.

# Install: npx ecc-install python  |  npm i -g @aisuite/chub  |  Source: github.com/affaan-m/everything-claude-code

# # First thing you type inside the session:
# /init

# /init scans your repo and generates a CLAUDE.md with build commands, file structure, and conventions. Review it, tweak it, commit it.

# Instructions that only load when Claude touches matching files

# .claude/rules/frontend.md - These live in .claude/rules/. Unlike CLAUDE.md (always loaded), rules only consume context when relevant files are touched. Keeps things lean.

# file:///Users/ash/Downloads/hackathon-claude-tips-FIXED.html


