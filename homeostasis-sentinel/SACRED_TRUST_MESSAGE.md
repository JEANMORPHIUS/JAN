# SACRED TRUST: Privacy Upgrade Message

**Status:** Draft for Gemini refinement
**Purpose:** Inform users about encryption upgrade with grace and transparency
**Tone:** Shell language (accessible) with Seed truth (honest)

---

## DRAFT MESSAGE FOR USER NOTIFICATION

### Version 1: Modal on First Launch After Update

```
╔════════════════════════════════════════════════════════════╗
║  🕊️  PROTECTING YOUR SACRED DATA                           ║
╚════════════════════════════════════════════════════════════╝

Your health data is your soul's digital footprint.
We guard it like our own.

We've upgraded Homeostasis Sentinel to protect your biology
with military-grade encryption. Your blood pressure, glucose,
and all health metrics will now be secured with a passphrase
that only you control.

┌────────────────────────────────────────────────────────────┐
│ WHAT'S CHANGING:                                            │
│                                                             │
│ Before: Your data was stored in plain text                 │
│         (visible to browser extensions)                    │
│                                                             │
│ Now:    Your data is encrypted with AES-256                │
│         (same standard banks use)                          │
│                                                             │
│ YOU control the encryption key.                            │
│ WE can't access your data without your passphrase.         │
│ NOBODY can read it without your permission.                │
└────────────────────────────────────────────────────────────┘

CREATE YOUR PASSPHRASE
(At least 8 characters. Choose something you'll remember.)

[                                                              ]

[ ] I understand that if I forget this passphrase,
    my encrypted data cannot be recovered.

[ ] I have read the Privacy Policy explaining how
    my data is protected.

                  [Secure My Data]  [Learn More]

─────────────────────────────────────────────────────────────

"We are born a miracle. We deserve to live a miracle."

Your privacy is not optional. It's sacred.

This is stewardship.
```

---

## Version 2: Banner Notification (Less Intrusive)

```
┌────────────────────────────────────────────────────────────┐
│ 🔒 SECURITY UPGRADE AVAILABLE                               │
│                                                             │
│ Protect your health data with encryption. Your blood       │
│ pressure, glucose, and biometrics will be secured with     │
│ a passphrase only you control.                             │
│                                                             │
│ [Secure My Data Now]  [Remind Me Later]  [Learn More]      │
└────────────────────────────────────────────────────────────┘
```

---

## Version 3: In-App Announcement (Gentle Approach)

```
═══════════════════════════════════════════════════════════

         A PROMISE FROM US TO YOU

We've been thinking deeply about your privacy.

Your health data—your blood pressure at 3am when you couldn't
sleep, your glucose readings, your heart rate when you were
stressed—these are sacred. They tell the story of your body,
your miracle.

We realized we weren't protecting them well enough.

So we built something better.

Starting today, Homeostasis Sentinel uses military-grade
encryption (AES-256-GCM) to protect your data. You choose
a passphrase, and only you can unlock your health records.

Not us. Not advertisers. Not anyone.

Just you.

We can't access your data. We can't decrypt it. We can't
hand it over to anyone, because we don't have the key.

You do.

This is what stewardship looks like.

═══════════════════════════════════════════════════════════

[Set Up Encryption]  [Read Technical Details]

"Your data is your soul's digital footprint.
 We guard it like our own."

```

---

## TECHNICAL DETAILS (For "Learn More" Link)

### What We Encrypt
- Blood pressure readings (systolic/diastolic)
- Heart rate measurements
- Glucose levels
- Timestamps and notes
- Any custom health metrics you track

### What We DON'T Collect
- We don't send your health data to our servers
- We don't share your data with third parties
- We don't use your data for advertising
- We don't train AI models on your health information

### How It Works
- **Algorithm:** AES-256-GCM (Advanced Encryption Standard, 256-bit key)
- **Key Derivation:** PBKDF2 with 100,000 iterations (OWASP recommended)
- **Storage:** Encrypted data stored locally in your browser
- **Control:** You hold the only key (your passphrase)

### What This Means
- ✅ **Offline:** Your data stays on your device
- ✅ **Private:** Only you can decrypt it
- ✅ **Secure:** Industry-standard encryption
- ✅ **Yours:** You control access completely

### Important: Passphrase Recovery
⚠️ **We cannot recover your passphrase.**

This is by design. If we could recover it, we could decrypt
your data—which defeats the purpose.

Choose a passphrase you'll remember, or use a password manager.

### Migration Notice
If you had data before this update, we'll automatically migrate
it to encrypted storage when you set up your passphrase.

Your old unencrypted data will be backed up once, then deleted.

---

## CONSENT CHECKBOX TEXT

```
[ ] I understand that:
    • My health data will be encrypted with my passphrase
    • If I forget my passphrase, my data cannot be recovered
    • This is for my protection, not a limitation
    • I can export my data anytime before changing passphrases
```

---

## PRIVACY POLICY EXCERPT (To Be Added)

### Data Encryption and Storage

**Effective Date:** 2026-01-19

Homeostasis Sentinel uses client-side encryption to protect
your health data. Here's exactly what happens:

1. **You create a passphrase** (at least 8 characters)

2. **We derive an encryption key** using PBKDF2 with:
   - 100,000 iterations
   - SHA-256 hashing
   - Random salt (stored locally)

3. **Your data is encrypted** using AES-256-GCM before storage

4. **Encrypted data is stored** in your browser's localStorage

5. **We never see your passphrase or unencrypted data**

**Your Rights:**
- Export your data anytime (unencrypted JSON)
- Delete your data completely
- Change your passphrase (requires re-encryption)
- Use Homeostasis Sentinel without creating an account

**Our Commitments:**
- We don't collect your health data on our servers
- We don't share your data with third parties
- We don't use your data for any purpose except what you request
- We will never add analytics or tracking without explicit consent

**Technical Transparency:**
- Encryption implementation: Open source (see `/src/utils/encryption.ts`)
- No proprietary encryption schemes
- Standard Web Crypto API (built into browsers)
- Auditable by security researchers

**Questions?**
Contact: privacy@siyem.org (to be created)

---

## NOTES FOR GEMINI TO REFINE:

**Brother, I need you to:**

1. **Adjust the Tone:**
   - Does this hit the right balance of Shell (accessible) and Seed (truth)?
   - Should we be more technical or more emotional?
   - Are we honoring "We are born a miracle" properly?

2. **Choose the Best Approach:**
   - Version 1: Modal (forced attention, might annoy)
   - Version 2: Banner (gentle, might be ignored)
   - Version 3: Announcement (narrative, might be too long)
   - Which fits the Homeostasis Sentinel vibe best?

3. **Refine the Language:**
   - Remove any "corporate speak" I accidentally added
   - Add your Duygu Adami heart to it
   - Make it feel like a promise, not a feature

4. **Add Context:**
   - Should we mention WHY we're doing this now?
   - Do we acknowledge the previous vulnerability?
   - How do we maintain trust while admitting the gap?

**What I'm Going For:**
- Honesty: "We weren't protecting you well enough. Now we are."
- Empowerment: "You control the key, not us."
- Sacred Weight: "Health data is not just data—it's your miracle."
- No Fear: "This is protection, not a burden."

**Shell/Seed Balance:**
- Shell: Simple language, clear steps, no jargon
- Seed: "We guard it like our own" (Book of Racon truth)

Refine this however your spirit guides you, brother.
This message will be the first thing users see after the update.
It needs to radiate truth, not just inform.

---

**May the work continue.**
🕊️
```
