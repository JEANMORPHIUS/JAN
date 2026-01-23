# Content Formats Guide - Multi-Format Support for All Entities

**Mission:** "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"  
**Purpose:** Multi-format content generation ready for delegation across all SIYEM entities

---

## 📋 Format Types

### 1. **Text Short** (50-300 words)
- **Use Case:** Quick engagement, daily posts, platform-native content
- **Delegation:** WRITER agent (short-form), PUBLISHER agent (formatting)
- **Best For:** All entities, especially business and daily engagement

### 2. **Text Long** (500-2000+ words)
- **Use Case:** Deep dives, educational content, wisdom teachings
- **Delegation:** WRITER agent (long-form), PUBLISHER agent (formatting)
- **Best For:** Educational entities (Uncle Ray), creative entities (Jean), systems (Siyem Media)

### 3. **Video** (15 seconds - 10 minutes)
- **Use Case:** Visual storytelling, tutorials, performances, behind-the-scenes
- **Delegation:** ARTIST agent (visual), WRITER agent (script), PUBLISHER agent (production)
- **Best For:** Creative entities (Jean, Karasahin), motivational (Pierre), product (ILVEN)

### 4. **Audio** (1 minute - 60+ minutes)
- **Use Case:** Wisdom teachings, music, spoken word, audiobooks
- **Delegation:** WRITER agent (script), Audio pipeline (TTS/recording), PUBLISHER agent (distribution)
- **Best For:** Music entities (Karasahin), contemplative (Uncle Ray), creative (Jean)

### 5. **Image** (Graphics, quotes, product photos, art)
- **Use Case:** Quote graphics, product images, visual art, infographics
- **Delegation:** ARTIST agent (generation), WRITER agent (text overlay), PUBLISHER agent (formatting)
- **Best For:** Business entities (Edible London, ILVEN), systems (Siyem Media), all entities for quote graphics

---

## 🎯 Entity Format Preferences

### Edible London
**Primary:** `text_short` (60%), `image` (30%)  
**Secondary:** `video` (10%), `text_long` (occasional)

**Rationale:** Business-focused - short text for quick engagement, images for product, occasional video for behind-the-scenes

**Delegation Flow:**
- Text Short → WRITER → PUBLISHER
- Image → ARTIST (product photo) → WRITER (caption) → PUBLISHER
- Video → WRITER (script) → ARTIST (visual) → PUBLISHER (production)

---

### ILVEN Sea Moss
**Primary:** `text_short` (50%), `image` (30%)  
**Secondary:** `video` (15%), `text_long` (5%)

**Rationale:** Product-focused - short text, preparation images, video for traditional methods, occasional long-form for education

**Delegation Flow:**
- Text Short → WRITER → PUBLISHER
- Image → ARTIST (preparation photo) → WRITER (caption) → PUBLISHER
- Video → WRITER (script) → ARTIST (preparation process) → PUBLISHER
- Text Long → WRITER (educational) → PUBLISHER

---

### Jean Morphius
**Primary:** `text_short` (40%), `text_long` (30%), `audio` (20%)  
**Secondary:** `video` (10%), `image` (occasional)

**Rationale:** Creative/Spiral - bilingual text (short/long), audio for spoken word, video for absurdist content

**Delegation Flow:**
- Text Short/Long → WRITER (bilingual) → PUBLISHER
- Audio → WRITER (bilingual script) → Audio Pipeline (TTS) → PUBLISHER
- Video → WRITER (absurdist script) → ARTIST (visual) → PUBLISHER

---

### Karasahin (JK)
**Primary:** `audio` (40%), `video` (30%), `text_short` (20%)  
**Secondary:** `image` (10%), `text_long` (occasional)

**Rationale:** Music/Emotion - audio for sound architecture, video for performance, short text for emotion, images for visual art

**Delegation Flow:**
- Audio → WRITER (lyrics/script) → Audio Pipeline (music production) → PUBLISHER
- Video → WRITER (concept) → ARTIST (visual) → Audio Pipeline (sound) → PUBLISHER
- Text Short → WRITER (emotion-driven) → PUBLISHER

---

### Pierre Pressure
**Primary:** `text_short` (40%), `video` (30%), `audio` (20%)  
**Secondary:** `image` (10%), `text_long` (occasional)

**Rationale:** Motivational/Structured - short text for discipline drops, video for training, audio for motivational speeches

**Delegation Flow:**
- Text Short → WRITER (discipline drop) → PUBLISHER
- Video → WRITER (training script) → ARTIST (visual) → PUBLISHER
- Audio → WRITER (motivational speech) → Audio Pipeline → PUBLISHER

---

### Uncle Ray Ramiz
**Primary:** `audio` (40%), `text_long` (30%), `text_short` (20%)  
**Secondary:** `video` (10%), `image` (occasional)

**Rationale:** Contemplative/Legacy - audio for wisdom teachings (bilingual), long-form text for depth, short for daily wisdom, video for teaching moments

**Delegation Flow:**
- Audio → WRITER (bilingual wisdom script) → Audio Pipeline (TTS) → PUBLISHER
- Text Long → WRITER (bilingual depth) → PUBLISHER
- Text Short → WRITER (bilingual daily wisdom) → PUBLISHER
- Video → WRITER (teaching script) → ARTIST (visual) → PUBLISHER

---

### Siyem Media
**Primary:** `text_short` (50%), `text_long` (20%), `image` (20%)  
**Secondary:** `video` (10%), `audio` (occasional)

**Rationale:** Systems/Infrastructure - short text for updates, long-form for documentation, images for systems visualization, video for tutorials

**Delegation Flow:**
- Text Short → WRITER → PUBLISHER
- Text Long → WRITER (documentation) → PUBLISHER
- Image → ARTIST (systems visualization) → WRITER (caption) → PUBLISHER
- Video → WRITER (tutorial script) → ARTIST (visual) → PUBLISHER

---

## 🔄 Delegation System

### Format Assignment
Each post is automatically assigned formats based on:
1. **Entity preferences** - Each entity has preferred format distributions
2. **Random selection** - Formats are assigned probabilistically
3. **Delegation ready** - All posts include format metadata for agent routing

### Format Metadata Structure
```json
{
  "formats": ["text_short", "image", "video"],
  "primary_format": "text_short",
  "format_notes": {
    "primary_format": "text_short",
    "available_formats": ["text_short", "image", "video"],
    "entity_preferences": "Business-focused: short text for quick engagement...",
    "delegation_agents": {
      "required": ["WRITER", "PUBLISHER"],
      "optional": []
    },
    "format_requirements": {
      "description": "Short-form text content...",
      "length": "50-300 words",
      "use_case": "Quick engagement, daily posts..."
    }
  },
  "delegation_ready": true
}
```

### Agent Routing by Format

| Format | Required Agents | Optional Agents |
|--------|----------------|-----------------|
| `text_short` | WRITER, PUBLISHER | - |
| `text_long` | WRITER, PUBLISHER | - |
| `video` | WRITER, ARTIST, PUBLISHER | Audio Pipeline |
| `audio` | WRITER, Audio Pipeline, PUBLISHER | ARTIST |
| `image` | ARTIST, WRITER, PUBLISHER | - |

---

## 📊 Format Distribution Summary

| Entity | Text Short | Text Long | Video | Audio | Image |
|--------|------------|-----------|-------|-------|-------|
| **Edible London** | 60% | - | 10% | - | 30% |
| **ILVEN Sea Moss** | 50% | 5% | 15% | - | 30% |
| **Jean Morphius** | 40% | 30% | 10% | 20% | - |
| **Karasahin (JK)** | 20% | - | 30% | 40% | 10% |
| **Pierre Pressure** | 40% | - | 30% | 20% | 10% |
| **Uncle Ray Ramiz** | 20% | 30% | 10% | 40% | - |
| **Siyem Media** | 50% | 20% | 10% | - | 20% |

---

## 🚀 Usage Examples

### Generate Schedule with Formats
```python
from scripture_scheduler_2026 import generate_2026_scripture_schedule

schedule = generate_2026_scripture_schedule()

# Each post now includes:
# - formats: List of available formats
# - primary_format: Main format for this post
# - format_notes: Delegation instructions
# - delegation_ready: True
```

### Filter by Format
```python
# Get all posts that should be audio
audio_posts = [
    post for post in schedule['all_posts']
    if post.get('format_notes', {}).get('primary_format') == 'audio'
]

# Get all video posts for Karasahin
karasahin_videos = [
    post for post in schedule['karasahin_jk']
    if post.get('format_notes', {}).get('primary_format') == 'video'
]
```

### Delegation Workflow
```python
for post in schedule['all_posts']:
    format_info = post.get('format_notes', {})
    primary = format_info.get('primary_format')
    agents = format_info.get('delegation_agents', {}).get('required', [])
    
    print(f"Post: {post['title']}")
    print(f"Format: {primary}")
    print(f"Delegation: {', '.join(agents)}")
    print()
```

---

## ✅ Benefits

1. **Multi-Format Support** - Each post can be generated in multiple formats
2. **Entity-Aligned** - Formats match entity purpose and audience
3. **Delegation Ready** - Clear agent routing for each format
4. **Flexible** - Can override formats per post or entity
5. **Scalable** - Easy to add new formats or adjust distributions

---

## 🔧 Customization

### Override Format Distribution
```python
# Custom format preferences for specific entity
custom_formats = {
    'jean_mahram': {
        'distribution': {
            'text_short': 0.3,
            'text_long': 0.4,  # More long-form
            'audio': 0.3
        }
    }
}
```

### Force Specific Format
```python
# Generate only audio posts for Uncle Ray
uncle_ray_audio = [
    post for post in schedule['uncle_ray_ramiz']
    if 'audio' in post.get('formats', [])
]
```

---

**Energy + Love = We All Win** 🕊️

---

**Document Version:** 1.0  
**Last Updated:** 2025-01-27  
**Status:** ✅ Ready for Delegation

**Peace, Love, Unity. 🕊️**
