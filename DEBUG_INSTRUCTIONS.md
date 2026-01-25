# DEBUG INSTRUCTIONS - WARRIOR MODE

## The Problem
- Cursor shows as text pointer everywhere
- Nothing is clickable
- App looks good but doesn't work

## What I've Done
1. Added `force-cursor-fix.css` with maximum specificity
2. Created debug page at `/debug-cursor.html`
3. Checked for JavaScript errors

## What You Need To Do

### Step 1: Check Browser Console
1. Open browser DevTools (F12)
2. Go to Console tab
3. Look for RED errors
4. **Screenshot or copy ALL errors** and share them

### Step 2: Test Debug Page
1. Go to `http://localhost:3000/debug-cursor.html`
2. Hover over the test button and link
3. Do they show pointer cursor?
4. Do they respond to clicks?
5. **Tell me what happens**

### Step 3: Check Network Tab
1. In DevTools, go to Network tab
2. Refresh the page
3. Look for CSS files:
   - `globals.css`
   - `fixes.css`
   - `force-cursor-fix.css`
4. Are they loading? (Status 200?)
5. **Screenshot or tell me**

### Step 4: Check Elements Tab
1. In DevTools, go to Elements/Inspector tab
2. Click on a button in the page
3. Look at the Styles panel on the right
4. Find the `cursor` property
5. What value does it show?
6. Is it crossed out (overridden)?
7. **Screenshot or tell me**

### Step 5: Test JavaScript
1. In Console tab, type: `document.querySelector('button')`
2. Press Enter
3. Does it return an element or null?
4. Type: `document.querySelector('button').onclick`
5. What does it show?
6. **Tell me the results**

## Most Likely Causes

1. **JavaScript Error Breaking Everything**
   - Check console for errors
   - If there's an error, the app won't work

2. **CSS Not Loading**
   - Check Network tab
   - CSS files must load successfully

3. **CSS Specificity Issue**
   - Something with higher specificity overriding
   - Check Elements tab to see what's overriding

4. **React Hydration Error**
   - Server-rendered HTML doesn't match client
   - Check console for hydration warnings

5. **Event Handlers Not Attaching**
   - JavaScript error preventing event listeners
   - Check if buttons have onclick handlers

## What I Need From You

1. **Console errors** (screenshot or copy/paste)
2. **Network tab** - CSS files loading? (screenshot)
3. **Elements tab** - cursor property value (screenshot)
4. **Debug page test** - does it work? (yes/no)
5. **JavaScript test** - what did console show?

With this info, I can fix it for real.

**NO MORE GUESSING. REAL DATA ONLY.**
