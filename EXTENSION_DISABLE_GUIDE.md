# HOW TO DISABLE THE BROWSER EXTENSION

## The Problem
You have a browser extension that's interfering with cursor behavior. The element with `data-cursor-link-preview="true"` is from this extension.

## Quick Fix: Disable the Extension

### Chrome/Edge:
1. Click the **puzzle piece icon** (extensions) in the toolbar
2. Find the extension (likely called something like "Link Preview", "Cursor", "Hover Preview", etc.)
3. Click the **toggle** to disable it
4. Refresh the page

### Firefox:
1. Click the **menu** (three lines) → **Add-ons and Themes**
2. Find the extension
3. Click **Disable**
4. Refresh the page

### Safari:
1. **Safari** → **Preferences** → **Extensions**
2. Find the extension
3. **Uncheck** it
4. Refresh the page

## Alternative: Test in Incognito Mode

Extensions are usually disabled in incognito/private mode:

1. Open **incognito/private window** (Ctrl+Shift+N or Cmd+Shift+N)
2. Go to `http://localhost:3000`
3. If it works in incognito → **Extension confirmed as problem**
4. Disable the extension permanently

## Find the Extension

Look for extensions with names like:
- "Link Preview"
- "Hover Preview" 
- "Cursor Enhancement"
- "Link Hover"
- "URL Preview"
- Anything with "preview" or "cursor" in the name

## After Disabling

1. **Hard refresh** the page (Ctrl+Shift+R)
2. **Test** cursor and clicks
3. Should work immediately

---

**The app will work once the extension is disabled.**
