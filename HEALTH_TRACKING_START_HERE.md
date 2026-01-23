# Health Tracking - Quick Start

**Your Homeostasis Sentinel Dashboard**

---

## Start Dashboard

### Option 1: PowerShell Script (Easiest)
```powershell
cd S:\JAN\homeostasis-sentinel
.\START.ps1
```

### Option 2: Manual
```powershell
cd S:\JAN\homeostasis-sentinel
npm run dev
```

Then open: `http://127.0.0.1:3001`

---

## Record Your Data

1. Create markdown file in `Obsidian_Vault/` (e.g., `2025-01-14.md`)
2. Fill in frontmatter with your metrics
3. Load files into dashboard using "Select Files" button

See `homeostasis-sentinel/README.md` for complete guide.

---

## Daily Workflow

1. **Morning**: Record Zero-Point baseline (vision, glucose, tension, breath)
2. **During Day**: Record metrics hourly or after key events
3. **Evening**: Load all files into dashboard, review alerts and trends

---

## Quick Reference

- **Dashboard**: `http://127.0.0.1:3001`
- **Data Location**: `S:\JAN\homeostasis-sentinel\Obsidian_Vault\`
- **Templates**: `Obsidian_Vault/DAY1_TEMPLATE.md`
- **Checklist**: `DAY1_ZERO_POINT_CHECKLIST.md`
- **Quick Ref**: `DAY1_QUICK_REFERENCE.md`

---

## Other Systems (Separate)

- **SIYEM** (Content Creation): `S:\SIYEM\` - Runs on port 8000
- **jan-studio** (Marketplace): `S:\JAN\jan-studio\` - Runs on port 8000

**Note**: Don't run SIYEM and jan-studio simultaneously (port conflict).

