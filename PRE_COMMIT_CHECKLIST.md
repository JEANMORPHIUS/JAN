# Pre-Commit Checklist

**Run this before staging and committing changes**

## Quick Check (Recommended)

```powershell
# From project root
.\scripts\pre_commit_check.ps1
```

Or manually:

```powershell
# 1. Verify no secrets
python scripts\verify_no_secrets.py

# 2. Check git status
git status

# 3. Verify sensitive files are ignored
git check-ignore -v world-history-app/.env.local
```

## Full Checklist

### ✅ Security Checks (REQUIRED)

- [ ] Run `python scripts\verify_no_secrets.py` - No secrets found
- [ ] Verify `.env` files are ignored: `git status --ignored | grep .env`
- [ ] Check sensitive files are ignored:
  - `world-history-app/.env.local`
  - `SIYEM/output/financial_data.json`
  - `SIYEM/output/free_will_data.json`

### ✅ Git Status (REQUIRED)

- [ ] Review `git status` - Only intended files staged
- [ ] No accidental large files or build artifacts
- [ ] No `node_modules/` or `__pycache__/` directories

### ⚠️ Build Verification (OPTIONAL - Only if you modified code)

**Only run builds if you changed code in these projects:**

#### Next.js Projects (if modified):
```bash
# jan-studio/frontend
cd jan-studio/frontend
npm run build

# ATILOK
cd ATILOK
npm run build

# world-history-app
cd world-history-app
npm run build
```

#### React Native (if modified):
```bash
# heritage-mobile-app
cd heritage-mobile-app
# Expo doesn't require pre-build, but verify TypeScript:
npx tsc --noEmit
```

#### Python Backend (if modified):
```bash
# Check syntax
python -m py_compile jan-studio/backend/main.py
```

### 📋 What Gets Committed

**✅ Safe to commit:**
- Source code (`.ts`, `.tsx`, `.py`, `.js`, `.json`)
- Configuration files (`.json`, `.yml`, `.md`)
- Documentation (`.md` files)
- Data files in `data/` (if not sensitive)

**❌ Never commit:**
- `.env` files
- `node_modules/`
- `__pycache__/` or `*.pyc`
- Build artifacts (`dist/`, `.next/`, `build/`)
- API keys, tokens, secrets
- `SIYEM/output/*.json` (financial data)

## Quick Commands

```powershell
# Full pre-commit check
.\scripts\pre_commit_check.ps1

# If all checks pass, stage and commit:
git add .
git commit -m "Your commit message"
```

## Notes

- **Builds are optional** - Only run if you modified code that needs compilation
- **Secret verification is REQUIRED** - Always run before committing
- **Git status review is REQUIRED** - Always check what you're committing

---

**Mission:** THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
