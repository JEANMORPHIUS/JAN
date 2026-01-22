# Technical Specifications: Listen İlven Video Production

## VIDEO FORMAT

### Primary Specifications
- **Resolution:** 1080x1920 (9:16 aspect ratio, vertical)
- **Frame Rate:** 30fps
- **Codec:** H.264 or H.265
- **Bitrate:** Minimum 8 Mbps (recommended 12-15 Mbps)
- **Color Space:** Rec. 709
- **Audio:** AAC, 48kHz, stereo, 192 kbps minimum

### Platform Optimizations
- **Instagram Reels:** 1080x1920, max 90 seconds
- **TikTok:** 1080x1920, max 10 minutes (but targeting 90s)
- **YouTube Shorts:** 1080x1920, max 60 seconds (consider 60s cut)
- **Meta/Facebook Reels:** 1080x1920, max 90 seconds

---

## VISUAL SPECIFICATIONS

### Color Grading
- **Primary Tone:** Warm highlights (#fbe5b2 / RGB: 251, 229, 178)
- **Look:** Natural, enhanced warmth
- **Consistency:** Unified color across real footage and AI-generated content
- **Style:** Documentary realism with slight cinematic enhancement

### Composition
- **Safe Zones:** Keep important content within center 80% (avoid extreme edges)
- **Text Overlays:** Minimum 48pt font, high contrast, readable without sound
- **Focus:** Depth of field effects for visual interest

### Animation Style
- **Transitions:** Soft, organic, particle-based
- **AI Icons:** Glowing light bursts, "friendly fireflies" effect
- **Motion:** Cinematic depth, smooth eases
- **Particles:** Soft, warm-toned, atmospheric

---

## AUDIO SPECIFICATIONS

### Voice-Over
- **Sample Rate:** 48kHz
- **Bit Depth:** 24-bit
- **Format:** WAV or high-quality MP3
- **Recording:** Clean, minimal room tone
- **Processing:** Light compression, EQ for warmth

### Sound Design Layers

#### Layer 1: Base Soundtrack
- **Type:** Lo-fi oceanic/ambient
- **Volume:** -18dB to -20dB (background)
- **Mood:** Calming, organic, textured

#### Layer 2: Real-World Sounds
- **Bus Sounds:** Engine, bell, air brakes, door sounds
- **Workshop Sounds:** Water, cutting, stirring, packaging
- **London Ambience:** Traffic, street sounds, city hum
- **Volume:** -12dB to -15dB (supporting)

#### Layer 3: Digital/AI Sounds
- **Type:** Light electronic chimes, digital tones
- **Timing:** During AI animation segments
- **Volume:** -15dB to -18dB (subtle)
- **Style:** Warm, organic-sounding, not harsh

#### Layer 4: Voice-Over
- **Volume:** -6dB to -9dB (foreground)
- **Ducking:** Ambient sounds duck slightly when VO speaks

### Audio Mixing
- **Overall LUFS:** -16 LUFS (social media standard)
- **Peak Level:** -1dB maximum
- **Dynamic Range:** Preserve natural dynamics, avoid over-compression

---

## AI GENERATION SPECIFICATIONS

### Tool Icons (Segment 4)
- **Style:** Minimalist, recognizable
- **Animation:** Orbit product, glow effect
- **Speed:** Gentle, organic motion (not mechanical)
- **Color:** Warm tones, consistent with palette
- **Icons Needed:**
  1. Gemini
  2. Claude
  3. ChatGPT
  4. NotebookLM
  5. Google AI Studio
  6. Nano Banana

### Map Animation (Segment 5)
- **Style:** Clean, modern, warm
- **Cities to Highlight:**
  - London (origin)
  - Paris
  - Lagos
  - Toronto
  - Istanbul
- **Effect:** Cities "light up" sequentially with warm glow
- **Connection Lines:** Subtle, if any (avoid clutter)

---

## PRODUCTION EQUIPMENT

### Camera
- **Primary:** iPhone (latest model preferred for quality)
- **Stabilization:** Gimbal or handheld for authentic feel
- **Lens:** Native, avoid digital zoom (maintain quality)

### Audio
- **Voice-Over:** External microphone (lapel or shotgun)
- **Ambient:** On-camera mic or separate recorder
- **Environment:** Quiet, controlled for VO

### Lighting
- **Natural Light:** Preferred for authentic feel
- **Supplement:** Soft fill light if needed
- **Consistency:** Maintain warm tone across shots

### Post-Production
- **Editing:** Premiere Pro, Final Cut Pro, or DaVinci Resolve
- **Animation:** After Effects, or AI tools for overlays
- **Color Grading:** Match warm palette consistently
- **Audio:** Pro Tools, Audition, or similar for mixing

---

## FILE ORGANIZATION

### Naming Convention
```
ILVEN_[SEGMENT]_[SHOT]_[DESCRIPTION]_[VERSION].ext
```

**Examples:**
- `ILVEN_INTRO_01_NARRATOR_CLOSE_v01.mp4`
- `ILVEN_JOURNEY_02_BUS_WINDOW_v01.mp4`
- `ILVEN_WORK_03_SEA_MOSS_MACRO_v01.mp4`

### Folder Structure
```
assets/
├── footage/
│   ├── raw/
│   ├── selects/
│   └── edited/
├── audio/
│   ├── voiceover/
│   ├── music/
│   ├── sfx/
│   └── ambience/
├── graphics/
│   ├── icons/
│   ├── animations/
│   └── text_overlays/
└── exports/
    ├── final/
    └── platform_specific/
```

---

## QUALITY CHECKLIST

### Pre-Export
- [ ] Color grading consistent throughout
- [ ] Audio levels balanced (no clipping, proper LUFS)
- [ ] Text readable on mobile devices
- [ ] Safe zones respected
- [ ] Transitions smooth
- [ ] Animation timing matches narrative
- [ ] Branding appears correctly
- [ ] Duration: 90 seconds (±2 seconds acceptable)

### Platform-Specific Checks
- [ ] Vertical format maintained (1080x1920)
- [ ] No black bars or letterboxing
- [ ] Audio synced properly
- [ ] Captions/CC available (for accessibility)
- [ ] Thumbnail optimized for platform

---

## DELIVERABLES

### Final Outputs
1. **Master File:** 1080x1920, 30fps, high bitrate (for archive)
2. **Social Media Version:** Optimized for each platform
3. **60-Second Cut:** For YouTube Shorts (if needed)
4. **Text Overlay Version:** For silent viewing
5. **Captions File:** SRT format for platform upload

### Supporting Assets
- Individual segments (for repurposing)
- Still frames for thumbnails
- Audio stems (for future edits)
- Graphics package (icons, animations)

---

**Remember:** Technical excellence serves the narrative. Every technical choice should amplify the heart of the craft, not distract from it.
