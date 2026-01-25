# Audio Generation Guide

## Overview

Generate audio files for all 655 scripture lessons.

**Voice Character:** Uncle Ray Ramiz
- Turkish Dayı (uncle) voice for Turkish lessons
- Gentle, compassionate English for English lessons
- Age-appropriate pacing and tone

## Generation Methods

### Method 1: Google Cloud TTS (Recommended)

**Quality:** Excellent (WaveNet voices)
**Cost:** ~$16.31
**Time:** ~2-4 hours

```bash
# Install dependencies
pip install google-cloud-texttospeech

# Set up credentials
export GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json"

# Run generation
python generate_audio_google.py
```

### Method 2: Coqui TTS (Free)

**Quality:** Good
**Cost:** FREE
**Time:** ~4-8 hours (GPU), ~12-24 hours (CPU)

```bash
# Install dependencies
pip install TTS

# Run generation
python generate_audio_coqui.py
```

### Method 3: Manual Recording

**Quality:** Excellent (Human)
**Cost:** ~$1091.67
**Time:** ~21.8 hours

1. Open `audio_scripts_for_recording.txt`
2. Record each script with appropriate voice
3. Save as corresponding output filename
4. Process audio (normalize, compress)

## Voice Guidelines

### Uncle Ray Ramiz Character

**Turkish (Dayı - Uncle):**
- Warm, caring tone
- Traditional Turkish uncle persona
- Patient and wise delivery
- Terms of endearment: "Yeğen" (nephew/niece), "Evlat" (child), "Canım" (my dear)

**English:**
- Gentle, compassionate
- Clear enunciation
- Wise, experienced narrator
- Grandfatherly warmth

### Age-Appropriate Pacing

- **Ages 5-7:** 15% slower, simpler language
- **Ages 8-10:** 10% slower, clear pacing
- **Ages 11-13:** 5% slower, normal delivery
- **Ages 14-16:** Normal pacing, mature tone

## Quality Standards

### Technical Requirements
- Format: MP3, 128-192 kbps
- Sample Rate: 44.1 kHz
- Mono audio
- Normalized volume (-3dB peak)
- Silence trimmed from start/end

### Content Requirements
- Clear pronunciation
- Appropriate emotional tone
- Natural pauses at sentence breaks
- Emphasis on key spiritual concepts
- Cultural authenticity (Turkish vs English)

## Budget Breakdown

| Method | Cost | Quality | Time |
|--------|------|---------|------|
| Coqui TTS | FREE | Good | Long |
| Google Cloud TTS (Standard) | $4.08 | Very Good | Fast |
| Google Cloud TTS (WaveNet) | $16.31 | Excellent | Fast |
| Amazon Polly (Neural) | $16.31 | Excellent | Fast |
| Azure TTS (Neural) | $16.31 | Excellent | Fast |
| Manual Recording | $1091.67 | Best | Very Long |

**Recommendation:** Google Cloud TTS WaveNet for quality/cost balance.

## Verification Checklist

After generation:
- [ ] All 655 audio files created
- [ ] Audio quality meets standards
- [ ] File names match output_filename
- [ ] Age-appropriate pacing verified
- [ ] Cultural authenticity maintained (Turkish voice)
- [ ] Spiritual content respected
- [ ] No technical glitches or artifacts

## Philosophy

Every voice serves the mission:
- Uncle Ray Ramiz embodies wisdom and love
- Voices must carry compassion and truth
- Audio serves souls, not just ears
- Quality reflects divine care

**We are born a miracle. Every word must reflect that miracle.**
