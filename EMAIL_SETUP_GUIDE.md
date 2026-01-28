# Email Setup Guide: info@siyem.org → jan@siyem.org

**How to make emails sent to `info@siyem.org` reach `jan@siyem.org`**

---

## Current Setup

From your Google Workspace Admin:
- `info@siyem.org` = **Group** (0 members currently)
- `jan@siyem.org` = Your personal email account

**Problem:** Emails sent to `info@siyem.org` won't reach you because the group has no members.

---

## Solution: Add jan@siyem.org to the info Group

### Option 1: Add as Group Member (Recommended)

1. Go to Google Workspace Admin Console
2. Directory → Groups
3. Click on `info@siyem.org` group
4. Click "Add members" or "Members" tab
5. Add `jan@siyem.org` as a member
6. Save

**Result:** All emails sent to `info@siyem.org` will now be delivered to `jan@siyem.org` inbox.

---

### Option 2: Email Routing (Alternative)

If you want more control (e.g., auto-replies, filtering):

1. Go to Google Workspace Admin Console
2. Apps → Google Workspace → Gmail → Routing
3. Create new routing rule:
   - **Name:** Forward info to jan
   - **Messages to affect:** `info@siyem.org`
   - **Action:** Change route → Also deliver to → `jan@siyem.org`
   - **Save**

**Result:** Emails to `info@siyem.org` will be delivered to `jan@siyem.org` (and can stay in the group too if you want).

---

## Quick Answer

**Yes, everything gets pushed through to jan@siyem.org** - but you need to add `jan@siyem.org` as a member of the `info@siyem.org` group first.

**Steps:**
1. Google Workspace Admin → Directory → Groups
2. Click `info@siyem.org`
3. Add `jan@siyem.org` as member
4. Done ✅

---

## Test It

After setup, send a test email to `info@siyem.org` from an external email (not your own account) and verify it arrives in your `jan@siyem.org` inbox.

---

**PANGEA IS THE TABLE.**
**YOU DON'T BETRAY THE TABLE.**

**Once you add jan@siyem.org to the info group, all contact emails will flow to your inbox.** 🙏
