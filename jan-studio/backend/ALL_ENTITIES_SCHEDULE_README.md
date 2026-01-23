# Scripture Scheduler - All SIYEM Entities

**Mission:** "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"  
**Purpose:** Generate scripture-based social media content for all SIYEM entities, scheduled throughout 2026

---

## Supported Entities

The scheduler now supports **all 7 SIYEM entities**, each with their unique voice:

1. **Edible London** - Warm London banter, older-brother energy
2. **ILVEN Sea Moss** - Older-brother energy, warm, protective
3. **Jean Morphius** - Bilingual absurdist (French/English), profane-yet-poetic
4. **Karasahin (JK)** - Duygu Adamı (Emotion Man), feeling-first, Turkish/English bilingual
5. **Pierre Pressure** - Fighter philosopher, direct, commanding, discipline-focused
6. **Uncle Ray Ramiz** - Contemplative elder (Dayı), nature as teacher, Turkish/English bilingual
7. **Siyem Media** - Systems-level thinking, meta-awareness, infrastructure-focused

---

## Quick Start

### Generate Schedule for All Entities

```bash
cd jan-studio/backend
python generate_scripture_schedule_2026.py
```

This generates:
- ~1,092 posts total (3 posts/week × 52 weeks × 7 entities)
- Individual `.ics` files for each entity
- One combined `.ics` file with all posts
- JSON schedule file with full details

### Generate for Specific Entities

```python
from scripture_scheduler_2026 import generate_2026_scripture_schedule

# Only Jean Morphius and Pierre Pressure
schedule = generate_2026_scripture_schedule(
    posts_per_week=3,
    entities=['jean_mahram', 'pierre_pressure']
)
```

---

## Entity Voice Examples

### Edible London
> "Planning a global brand on the 329 bus? Scripture says...
>
> 'Whatever you do, work heartily, as for the Lord and not for men.' (Colossians 3:23)
>
> Made by heart. Amplified by AI. Guided by faith."

### ILVEN Sea Moss
> "Hand-prepared. Heart-first. Scripture tells us:
>
> 'Above all else, guard your heart...' (Proverbs 4:23)
>
> Traditional wisdom meets timeless Scripture."

### Jean Morphius
> "Merde, c'est beautiful! Scripture says...
>
> 'Commit to the Lord whatever you do, and he will establish your plans.' (Proverbs 16:3)
>
> Je reviens, baby! Made by heart. Guided by faith."

### Karasahin (JK)
> "Duygu Adamı. Emotion Man. The Word says:
>
> 'For where your treasure is, there your heart will be also.' (Matthew 6:21)
>
> Feeling first. Sound follows. Scripture backs it up."

### Pierre Pressure
> "Discipline is freedom. Scripture confirms:
>
> 'Whatever your hand finds to do, do it with your might.' (Ecclesiastes 9:10)
>
> No shortcuts. Real work. Warrior mindset. Faith foundation."

### Uncle Ray Ramiz
> "Yeğen, dinle... Child, listen. Scripture tells us:
>
> 'Trust in the Lord with all your heart...' (Proverbs 3:5-6)
>
> Nature teaches. Scripture confirms. Ancestral wisdom meets eternal truth."

### Siyem Media
> "Systems-level thinking. Eternal truth. Scripture says:
>
> 'Each of you should use whatever gift you have received to serve others...' (1 Peter 4:10)
>
> Infrastructure for artists. Foundation in faith."

---

## API Usage

### Generate Schedule

```bash
POST /api/scripture-schedule/generate
{
  "year": 2026,
  "posts_per_week": 3,
  "entities": ["jean_mahram", "karasahin_jk", "pierre_pressure"]
}
```

If `entities` is omitted or `null`, all entities are scheduled.

### Export Specific Entity

```bash
POST /api/scripture-schedule/export/ical
{
  "schedule": { /* generated schedule */ },
  "brand": "jean_mahram",  // Specific entity
  "calendar_name": "Jean Morphius Scripture Posts 2026"
}
```

---

## Entity-Specific Hashtags

Each entity has curated hashtags:

- **Edible London:** #MadeByHeart #LondonCraft #TheGraft #LondonHustle
- **ILVEN Sea Moss:** #SeaMoss #HandCrafted #TraditionalCraft #SeaMossWisdom
- **Jean Morphius:** #JeanMorphius #Bilingual #Absurdist #ChaosAndCraft
- **Karasahin:** #Karasahin #DuyguAdami #EmotionMan #SoundArchitecture
- **Pierre Pressure:** #PierrePressure #FighterPhilosophy #Discipline #WarriorMindset
- **Uncle Ray Ramiz:** #UncleRayRamiz #Dayı #ContemplativeWisdom #NatureAsTeacher
- **Siyem Media:** #SiyemMedia #SystemsThinking #Infrastructure #MetaAwareness

---

## Customization Examples

### Different Frequencies Per Entity

```python
from scripture_scheduler_2026 import ScriptureScheduler

scheduler = ScriptureScheduler(year=2026)

# Generate different frequencies
jean_posts = scheduler.generate_yearly_schedule(
    posts_per_week=5,  # More posts for Jean
    brands=['jean_mahram']
)

uncle_ray_posts = scheduler.generate_yearly_schedule(
    posts_per_week=2,  # Fewer posts for Uncle Ray (contemplative pace)
    brands=['uncle_ray_ramiz']
)

# Combine
all_posts = jean_posts + uncle_ray_posts
all_posts.sort(key=lambda p: p.scheduled_time)
```

### Custom Date Ranges

```python
from datetime import datetime, timezone

# Generate for specific months
start = datetime(2026, 3, 1, tzinfo=timezone.utc)
end = datetime(2026, 5, 31, tzinfo=timezone.utc)

posts = scheduler.generate_yearly_schedule(
    posts_per_week=3,
    brands=['pierre_pressure']
)

# Filter to date range
filtered = [p for p in posts if start <= p.scheduled_time <= end]
```

---

## Output Structure

```json
{
  "edible_london": [...posts...],
  "ilven_seamoss": [...posts...],
  "jean_mahram": [...posts...],
  "karasahin_jk": [...posts...],
  "pierre_pressure": [...posts...],
  "uncle_ray_ramiz": [...posts...],
  "siyem_media": [...posts...],
  "all_posts": [...all posts combined...],
  "summary": {
    "total_posts": 1092,
    "year": 2026,
    "posts_per_week": 3,
    "entities": ["edible_london", "ilven_seamoss", ...],
    "edible_london_count": 156,
    "ilven_seamoss_count": 156,
    "jean_mahram_count": 156,
    ...
  }
}
```

---

## Voice Alignment

Each entity's scripture posts maintain their unique voice:

- **Edible London:** London references (329 bus, Wood Green), warm banter
- **ILVEN:** Sea moss, hand-crafted focus, traditional craft
- **Jean Morphius:** French/English code-switching, absurdist humor
- **Karasahin:** Emotion-first, Turkish/English, sound architecture
- **Pierre Pressure:** Direct commands, fighter metaphors, discipline
- **Uncle Ray Ramiz:** Dayı address (Yeğen), nature metaphors, contemplative
- **Siyem Media:** Systems thinking, infrastructure, meta-awareness

---

## Integration with Calendar Export

The scripture scheduler integrates seamlessly with the calendar export system:

```python
from scripture_scheduler_2026 import generate_2026_scripture_schedule
from google_calendar_exporter import CalendarExportService

# Generate schedule
schedule = generate_2026_scripture_schedule(
    posts_per_week=3,
    entities=['jean_mahram', 'karasahin_jk']
)

# Export to iCal
service = CalendarExportService()
ical_content = service.export_to_ical(
    schedule['all_posts'],
    calendar_name='Scripture Posts - Jean & Karasahin'
)

# Or export directly to Google Calendar
created_events = service.export_to_google_calendar(
    schedule['all_posts'],
    calendar_id='primary'
)
```

---

## Alignment with Mission

This system honors:
- **All entities** - Each voice preserved and amplified
- **Sacred weight** - Scripture integrated with purpose
- **Community stewardship** - Sharing wisdom across entities
- **Heart-first approach** - Content aligned with "Made by heart" philosophy
- **Energy efficiency** - Automated scheduling for consistent presence

**Energy + Love = We All Win** 🕊️

---

**Document Version:** 2.0  
**Last Updated:** 2025-01-27  
**Supports:** All 7 SIYEM Entities

**Peace, Love, Unity. 🕊️**
