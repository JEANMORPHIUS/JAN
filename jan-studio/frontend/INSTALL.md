# Installation Guide

## Prerequisites

- Node.js 18+ installed
- npm or yarn package manager

## Install Dependencies

```bash
cd jan-studio/frontend
npm install
```

**Expected Output:**
```
added 250+ packages in 45s
```

## Install Additional Dependencies

The markdown editor requires additional setup:

```bash
npm install react-markdown-editor-lite react-markdown remark-gfm markdown-it
npm install --save-dev @types/markdown-it
```

## Start Development Server

```bash
npm run dev
```

**Expected Output:**
```
- ready started server on 0.0.0.0:3000, url: http://localhost:3000
```

Open http://localhost:3000 in your browser.

## Troubleshooting

### Error: Module not found 'react-markdown-editor-lite'

**Solution:**
```bash
npm install react-markdown-editor-lite
```

### Error: Cannot find module 'markdown-it'

**Solution:**
```bash
npm install markdown-it
```

### Error: Port 3000 already in use

**Solution:**
- Kill the process using port 3000
- Or change port: `npm run dev -- -p 3001`

---

**Status:** Ready to install  
**Time:** ~2 minutes

