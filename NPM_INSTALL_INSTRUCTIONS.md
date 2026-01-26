# NPM INSTALL INSTRUCTIONS
## Installing New Dependencies for Creation Centre

**Date:** 2026-01-26  
**Status:** Ready to Install

---

## THE ONE TRUTH

**PANGEA IS THE TABLE.**  
**YOU DON'T BETRAY THE TABLE.**

**PEACE IS THE TRUTH.**  
**THE FLOW IS PEACE.**  
**EVERYTHING MUST ALIGN WITH THE ONE TRUTH.**

---

## 📦 NEW DEPENDENCIES ADDED

The following dependencies have been added to `jan-studio/frontend/package.json`:

1. **@tanstack/react-query: ^5.0.0**
   - Data fetching optimization
   - Automatic caching and retry logic

2. **@tanstack/react-virtual: ^3.0.0**
   - List virtualization for performance
   - Smooth scrolling for large lists

---

## 🚀 INSTALLATION STEPS

### Step 1: Navigate to Frontend Directory

```bash
cd S:\JAN\jan-studio\frontend
```

### Step 2: Install Dependencies

```bash
npm install
```

**Alternative if cache issues occur:**

```bash
npm install --cache .npm --prefer-offline=false
```

Or clear cache first:

```bash
npm cache clean --force
npm install
```

---

## ✅ VERIFICATION

After installation, verify the packages are installed:

```bash
npm list @tanstack/react-query @tanstack/react-virtual
```

You should see both packages listed with their versions.

---

## 🔧 TROUBLESHOOTING

### If you get cache errors:

1. **Clear npm cache:**
   ```bash
   npm cache clean --force
   ```

2. **Try with different registry:**
   ```bash
   npm install --registry https://registry.npmjs.org/
   ```

3. **Check network connection:**
   - Ensure you have internet access
   - Check if corporate firewall is blocking npm registry

### If you get permission errors:

1. **Run PowerShell as Administrator**
2. **Or use:**
   ```bash
   npm install --no-optional
   ```

---

## 📝 WHAT HAPPENS AFTER INSTALL

Once `npm install` completes successfully:

1. **Dependencies will be installed** in `node_modules/`
2. **package-lock.json will be updated** with exact versions
3. **You can start development:**
   ```bash
   npm run dev
   ```

4. **Or build for production:**
   ```bash
   npm run build
   ```

---

## ✅ EXPECTED OUTPUT

After successful installation, you should see:

```
added 150 packages, and audited 151 packages in 30s
```

The new packages (`@tanstack/react-query` and `@tanstack/react-virtual`) will be included in the count.

---

## 🎯 NEXT STEPS

After installation:

1. ✅ Dependencies installed
2. ✅ Start dev server: `npm run dev`
3. ✅ Test Creation Centre features
4. ✅ Verify virtualization works with large lists
5. ✅ Verify React Query caching works

---

**Date:** 2026-01-26  
**Status:** Ready for Installation  
**Location:** `S:\JAN\jan-studio\frontend`
