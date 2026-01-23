# Content Auto-Population Guide - AI Service Integration

**Mission:** "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"  
**Purpose:** Automatically generate content in assigned formats using aligned AI services

---

## 🚀 Overview

The Content Auto-Populator automatically generates content for scheduled posts using AI services aligned with entity voices and formats. It routes posts to appropriate services (WRITER, ARTIST, PUBLISHER, Audio Pipeline) based on format assignments.

---

## 🔄 How It Works

### 1. **Format Detection**
- Reads `primary_format` from post's `format_notes`
- Identifies required agents from `delegation_agents`

### 2. **Service Routing**
- **Text Short/Long** → WRITER agent
- **Video** → WRITER (script) + ARTIST (visual)
- **Audio** → WRITER (script) + Audio Pipeline (generation)
- **Image** → ARTIST (generation)

### 3. **Entity Voice Alignment**
- Uses entity-specific voice profiles
- Maintains brand consistency
- Supports bilingual content where applicable

### 4. **Content Generation**
- Generates content in assigned format
- Stores in `generated_content` field
- Marks post as `content_populated: true`

---

## 📋 Supported Formats

### **Text Short** (50-300 words)
- **Service:** WRITER agent
- **Input:** Scripture reference, theme, entity voice
- **Output:** Short-form social media post

### **Text Long** (500-2000+ words)
- **Service:** WRITER agent
- **Input:** Scripture reference, theme, entity voice
- **Output:** Long-form article/essay

### **Video** (15 seconds - 10 minutes)
- **Services:** WRITER (script) + ARTIST (visual)
- **Input:** Scripture reference, theme, entity voice
- **Output:** Video script + visual prompt

### **Audio** (1 minute - 60+ minutes)
- **Services:** WRITER (script) + Audio Pipeline (generation)
- **Input:** Scripture reference, theme, entity voice, languages
- **Output:** Audio script + audio file

### **Image** (Graphics, quotes, art)
- **Service:** ARTIST agent
- **Input:** Scripture reference, theme, entity style
- **Output:** Image prompt + generated image

---

## 🎯 Entity Voice Profiles

| Entity | Voice Profile | Bilingual | Languages |
|--------|--------------|-----------|-----------|
| **Edible London** | warm_london_banter | No | en |
| **ILVEN Sea Moss** | older_brother_energy | No | en |
| **Jean Morphius** | bilingual_absurdist | Yes | en, fr |
| **Karasahin (JK)** | emotion_man | Yes | en, tr |
| **Pierre Pressure** | fighter_philosopher | No | en |
| **Uncle Ray Ramiz** | contemplative_elder | Yes | en, tr |
| **Siyem Media** | systems_level | No | en |

---

## 🚀 API Usage

### Populate Entire Schedule
```python
POST /api/content-population/populate-schedule
{
  "schedule": {...},  # Generated schedule
  "limit": 10,  # Optional: limit number of posts
  "base_url": "http://localhost:8000"  # AI services URL
}
```

### Populate Single Post
```python
POST /api/content-population/populate-post
{
  "post": {...},  # Post dictionary
  "base_url": "http://localhost:8000"
}
```

### Populate by Format
```python
POST /api/content-population/populate-by-format/video
{
  "schedule": {...},
  "limit": 5,
  "base_url": "http://localhost:8000"
}
```

### Populate by Entity
```python
POST /api/content-population/populate-by-entity/jean_mahram
{
  "schedule": {...},
  "limit": 10,
  "base_url": "http://localhost:8000"
}
```

### Get Population Status
```python
GET /api/content-population/status
{
  "schedule": {...}
}
```

---

## 📊 Generated Content Structure

After population, each post includes:

```json
{
  "generated_content": {
    "text_short": {
      "content": "Generated short-form text...",
      "generated_at": "2025-01-27T12:00:00",
      "service": "WRITER",
      "word_count": 150
    },
    "video": {
      "script": "Video script content...",
      "visual_prompt": "Visual description...",
      "generated_at": "2025-01-27T12:00:00",
      "service": "WRITER + ARTIST"
    },
    "audio": {
      "script": "Audio script content...",
      "audio_file": "/path/to/audio.mp3",
      "languages": ["en", "tr"],
      "generated_at": "2025-01-27T12:00:00",
      "service": "WRITER + Audio Pipeline"
    },
    "image": {
      "prompt": "Image generation prompt...",
      "image_path": "/path/to/image.jpg",
      "style_preset": "Absurdist Comedy",
      "generated_at": "2025-01-27T12:00:00",
      "service": "ARTIST"
    }
  },
  "content_populated": true,
  "content_populated_at": "2025-01-27T12:00:00"
}
```

---

## 🔧 AI Service Integration

### Required Services

1. **WRITER Agent**
   - Endpoint: `POST /strategy` (role: WRITER)
   - Generates: Text content (short/long), scripts

2. **ARTIST Agent**
   - Endpoint: `POST /visual/generate-prompt`
   - Alternative: `POST /generate-image`
   - Generates: Visual prompts, images

3. **Audio Pipeline**
   - Endpoint: `POST /generate-audio`
   - Alternative: `POST /audio/generate-batch`
   - Generates: Audio files from scripts

4. **PUBLISHER Agent**
   - Endpoint: `POST /transform-content`
   - Alternative: `POST /export-campaign`
   - Formats: Content for publishing

### Service Configuration

Update `AI_SERVICES` in `content_auto_populator.py` to match your service endpoints:

```python
AI_SERVICES = {
    'WRITER': {
        'endpoint': '/strategy',
        'method': 'POST',
        'role': 'WRITER'
    },
    'ARTIST': {
        'endpoint': '/visual/generate-prompt',
        'method': 'POST'
    },
    # ... etc
}
```

---

## ✅ Workflow Example

### Complete Workflow

1. **Generate Schedule**
   ```python
   POST /api/scripture-schedule/generate
   # Returns schedule with format assignments
   ```

2. **Populate Content**
   ```python
   POST /api/content-population/populate-schedule
   {
     "schedule": schedule_from_step_1
   }
   # Generates all content using AI services
   ```

3. **Check Status**
   ```python
   GET /api/content-population/status
   {
     "schedule": populated_schedule
   }
   # Returns population status
   ```

4. **Export to Calendar**
   ```python
   POST /api/scripture-schedule/export/google
   {
     "schedule": populated_schedule
   }
   # Exports populated schedule to calendar
   ```

---

## 🎯 Benefits

1. **Automatic Content Generation** - No manual content creation needed
2. **Entity-Aligned** - Maintains brand voice and consistency
3. **Format-Aware** - Generates appropriate content for each format
4. **Bilingual Support** - Handles bilingual entities automatically
5. **Scalable** - Can populate entire schedules or individual posts
6. **Service Integration** - Works with existing AI service infrastructure

---

## 🔧 Customization

### Custom Voice Profiles
Update `ENTITY_SERVICE_MAPPING` in `content_auto_populator.py`:

```python
ENTITY_SERVICE_MAPPING = {
    'your_entity': {
        'voice_profile': 'your_voice',
        'bilingual': True,
        'languages': ['en', 'xx']
    }
}
```

### Custom Prompts
Modify prompt building methods:
- `_build_writer_prompt()`
- `_build_video_script_prompt()`
- `_build_audio_script_prompt()`
- `_build_visual_prompt()`
- `_build_image_prompt()`

---

## 📊 Population Statistics

After population, check status:

```json
{
  "total_posts": 941,
  "populated": 900,
  "errors": 5,
  "pending": 36,
  "completion_percentage": 95.64,
  "format_breakdown": {
    "text_short": {
      "total": 500,
      "populated": 495,
      "errors": 2
    },
    "video": {
      "total": 100,
      "populated": 95,
      "errors": 1
    }
  }
}
```

---

**Energy + Love = We All Win** 🕊️

---

**Document Version:** 1.0  
**Last Updated:** 2025-01-27  
**Status:** ✅ Ready for Auto-Population

**Peace, Love, Unity. 🕊️**
