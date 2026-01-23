# Scripture Schedule - All SIYEM Entities - 2026

**Now supports all 7 SIYEM entities!**

**Mission:** "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"  
**Purpose:** Generate and schedule scripture-based social media content for 2026

---

## Overview

This system generates scripture-based social media posts for **all 7 SIYEM entities**, scheduled throughout 2026. The content integrates biblical scripture with each entity's unique voice and values.

**Supported Entities:**
- Edible London (warm London banter)
- ILVEN Sea Moss (protective, traditional craft)
- Jean Morphius (bilingual absurdist)
- Karasahin/JK (Duygu Adamı - Emotion Man)
- Pierre Pressure (fighter philosopher)
- Uncle Ray Ramiz (contemplative elder)
- Siyem Media (systems-level thinking)

---

## Quick Start

### Option 1: Generate Schedule Script

```bash
cd jan-studio/backend
python generate_scripture_schedule_2026.py
```

This will:
- Generate ~312 scripture posts for 2026 (3 posts/week × 52 weeks × 2 brands)
- Save schedule to `scripture_schedule_2026.json`
- Export 3 `.ics` calendar files:
  - `scripture_schedule_2026_all.ics` (all posts)
  - `scripture_schedule_2026_edible_london.ics` (Edible London only)
  - `scripture_schedule_2026_ilven_seamoss.ics` (ILVEN Sea Moss only)

### Option 2: Use API Endpoints

**Generate Schedule:**
```bash
POST /api/scripture-schedule/generate
{
  "year": 2026,
  "posts_per_week": 3,
  "brands": ["edible_london", "ilven_seamoss"]
}
```

**Export to iCal:**
```bash
POST /api/scripture-schedule/export/ical
{
  "schedule": { /* generated schedule */ },
  "brand": "all",  // or "edible_london" or "ilven_seamoss"
  "calendar_name": "Scripture Posts 2026"
}
```

**Export to Google Calendar:**
```bash
POST /api/scripture-schedule/export/google
{
  "schedule": { /* generated schedule */ },
  "brand": "all"
}
```

---

## Content Themes

Scripture posts are organized around these themes, aligned with brand values:

1. **Craft & Work** - Excellence, skill, diligence
2. **Heart & Purpose** - Intentionality, values, vision
3. **Community & Stewardship** - Togetherness, service, support
4. **Wisdom & Tradition** - Learning, heritage, knowledge
5. **Faith & Trust** - Belief, strength, guidance
6. **Love & Service** - Service, community, witness
7. **Patience & Process** - Timing, waiting, seasons

---

## Brand Voice Integration

### Edible London
- **Voice:** Warm London banter, older-brother energy
- **Hooks:** "Planning a global brand on the 329 bus? Scripture says..."
- **Tone:** Conversational, grounded, real talk
- **Example:**
  > "Made by heart. The Bible puts it this way:
  >
  > 'Whatever you do, work heartily, as for the Lord and not for men.' (Colossians 3:23)
  >
  > This isn't about shortcuts. It's about the work—the real, hands-on, day-in-day-out graft."

### ILVEN Sea Moss
- **Voice:** Older-brother energy, warm, protective
- **Hooks:** "Hand-prepared. Heart-first. Scripture tells us:"
- **Tone:** Authentic, caring, grounded
- **Example:**
  > "Sea moss made by hand, guided by heart. The Word says:
  >
  > 'Above all else, guard your heart, for everything you do flows from it.' (Proverbs 4:23)
  >
  > Traditional wisdom meets timeless Scripture. Ancient preparation meets eternal truth."

---

## Importing to Google Calendar

### Method 1: Manual Import

1. Generate the `.ics` files using the script or API
2. Open Google Calendar
3. Click gear icon → Settings
4. Scroll to "Import & Export"
5. Click "Import"
6. Select the `.ics` file
7. Choose which calendar to import to
8. Click "Import"

### Method 2: Direct API Export

1. Generate schedule via API
2. Authenticate with Google Calendar (if not already)
3. Call `/api/scripture-schedule/export/google`
4. Events appear directly in your calendar

---

## Schedule Details

### Optimized Configuration
- **Entity-specific frequencies:**
  - Edible London: 2 posts/week (104/year)
  - ILVEN Sea Moss: 2 posts/week (104/year)
  - Jean Morphius: 4 posts/week (208/year) - Spiral/Active
  - Karasahin (JK): 3 posts/week (156/year)
  - Pierre Pressure: 3 posts/week (156/year) - Barred Spiral/Structured
  - Uncle Ray Ramiz: 2 posts/week (104/year) - Elliptical/Legacy
  - Siyem Media: 2 posts/week (104/year)
- **Total:** ~936 posts/year (~18 posts/week)
- **Year:** 2026
- **Platforms:** Instagram, Twitter, Facebook, LinkedIn
- **Distribution:** Spread throughout the year with optimal posting times
- **Alignment:** Frequencies honor Four Forms philosophy

### Posting Times (UTC)
- **Instagram:** 09:00, 12:00, 17:00, 20:00
- **Twitter:** 08:00, 13:00, 18:00
- **Facebook:** 09:00, 15:00, 19:00
- **LinkedIn:** 08:00, 12:00, 17:00

---

## Scripture Verses Included

The system includes verses aligned with brand values:

### Craft & Work
- Proverbs 22:29 - Skill and excellence
- Colossians 3:23 - Working heartily
- Proverbs 14:23 - Real work vs. talk
- Ecclesiastes 9:10 - Doing with might

### Heart & Purpose
- Proverbs 4:23 - Guarding the heart
- Matthew 6:21 - Heart's treasure
- Jeremiah 29:11 - God's plans
- Proverbs 16:3 - Committing plans to God

### Community & Stewardship
- Galatians 6:2 - Bearing burdens
- 1 Peter 4:10 - Serving as stewards
- Hebrews 10:24-25 - Spurring one another
- Proverbs 27:17 - Iron sharpens iron

### And more themes...

---

## Customization

### Adjust Post Frequency

```python
from scripture_scheduler_2026 import generate_2026_scripture_schedule

# 2 posts per week instead of 3
schedule = generate_2026_scripture_schedule(posts_per_week=2)
```

### Single Brand

```python
from scripture_scheduler_2026 import ScriptureScheduler

scheduler = ScriptureScheduler(year=2026)
posts = scheduler.generate_yearly_schedule(
    posts_per_week=3,
    brands=['edible_london']  # Only Edible London
)
```

### Custom Year

```python
scheduler = ScriptureScheduler(year=2027)
posts = scheduler.generate_yearly_schedule(posts_per_week=3)
```

---

## Output Format

Each post includes:

```json
{
  "title": "Scripture: Proverbs 4:23 - heart_purpose",
  "content": "Full post content with scripture...",
  "scheduled_time": "2026-01-15T09:00:00+00:00",
  "platform": "Instagram",
  "hashtags": ["#MadeByHeart", "#Scripture", ...],
  "metadata": {
    "theme": "heart_purpose",
    "category": "scripture",
    "voice": "warm_london_banter",
    "scripture_reference": "Proverbs 4:23",
    "scripture_text": "...",
    "brand": "edible_london"
  }
}
```

---

## Alignment with Mission

This system honors:
- **Sacred weight of content** - Scripture integrated with brand values
- **Community stewardship** - Sharing wisdom and faith
- **Heart-first approach** - Content aligned with "Made by heart" philosophy
- **Energy efficiency** - Automated scheduling for consistent presence

**Energy + Love = We All Win** 🕊️

---

## Files Generated

After running the generator:

1. **scripture_schedule_2026.json** - Complete schedule data
2. **scripture_schedule_2026_all.ics** - All posts calendar file
3. **scripture_schedule_2026_edible_london.ics** - Edible London calendar
4. **scripture_schedule_2026_ilven_seamoss.ics** - ILVEN Sea Moss calendar

---

## Troubleshooting

**Problem:** Posts don't appear in calendar after import

**Solution:**
- Check timezone settings (posts are in UTC)
- Verify `.ics` file format is valid
- Ensure import completed successfully
- Try importing to a test calendar first

**Problem:** Want to modify existing schedule

**Solution:**
- Edit `scripture_schedule_2026.json` manually
- Regenerate with different parameters
- Use API to regenerate specific date ranges

---

**Document Version:** 1.0  
**Last Updated:** 2025-01-27  
**Aligned with:** JAN MUHARREM Core Principles, Brand Voice Guides

**Peace, Love, Unity. 🕊️**
