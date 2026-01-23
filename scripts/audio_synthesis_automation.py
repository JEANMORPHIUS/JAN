"""
Audio Synthesis Automation
Generates audio files for all 376 scripture lessons

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Voice serving divine truth

THE FOUNDATION:
We are born a miracle.
Every voice must carry love.
Uncle Ray Ramiz speaks to souls.

THE MISSION:
Generate 376+ audio files:
- All scripture lessons (bilingual)
- Uncle Ray Ramiz voice for Turkish
- Clear, compassionate delivery
- Age-appropriate pacing
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, load_json, save_json
    setup_logging, standard_main
)

import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
import subprocess
import sys

class AudioSynthesisAutomation:
    """
    Automated audio generation for all scripture lessons

    Supports multiple TTS engines:
    - Coqui TTS (local, free)
    - Google Cloud TTS (API, paid)
    - Azure TTS (API, paid)
    - Amazon Polly (API, paid)
    """

    def __init__(self, project_root: str = "S:/JAN"):
        self.project_root = Path(project_root)
        self.scripture_dir = self.project_root / "jan-studio" / "curriculum" / "scripture_schedule_2026"
        self.output_dir = self.project_root / "output" / "audio_assets"
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.generation_log: List[Dict] = []

    def load_audio_scripts(self) -> List[Dict[str, Any]]:
        """Load all 376 scripture lesson audio scripts"""

        scripts = []

        if not self.scripture_dir.exists():
            print(f"Warning: Scripture directory not found: {self.scripture_dir}")
            return scripts

        # Load all lesson JSON files
        for lesson_file in self.scripture_dir.glob("*.json"):
            try:
                with open(lesson_file, 'r', encoding='utf-8') as f:
                    lesson = json.load(f)

                    if 'audio_script' in lesson:
                        scripts.append({
                            'lesson_id': lesson.get('lesson_id', lesson_file.stem),
                            'law_number': lesson.get('law_number'),
                            'age_group': lesson.get('age_group'),
                            'language': lesson.get('language', 'en'),
                            'script': lesson['audio_script'],
                            'output_filename': f"scripture_{lesson_file.stem}.mp3",
                            'voice_profile': self._determine_voice_profile(lesson)
                        })
            except Exception as e:
                print(f"Error loading {lesson_file}: {e}")

        print(f"Loaded {len(scripts)} audio scripts")
        return scripts

    def _determine_voice_profile(self, lesson: Dict) -> Dict[str, Any]:
        """Determine appropriate voice settings for lesson"""

        language = lesson.get('language', 'en')
        age_group = lesson.get('age_group', '8-10')

        # Uncle Ray Ramiz voice for Turkish
        # Gentle, compassionate English for English

        if language == 'tr':
            return {
                'engine': 'google',  # Best Turkish support
                'language_code': 'tr-TR',
                'voice_name': 'tr-TR-Wavenet-B',  # Male voice
                'speaking_rate': 0.9,  # Slightly slower for comprehension
                'pitch': 0,
                'character': 'Uncle Ray Ramiz - Turkish Dayı'
            }
        else:  # English
            # Adjust for age group
            if age_group == '5-7':
                speaking_rate = 0.85  # Slower for younger
            elif age_group == '8-10':
                speaking_rate = 0.9
            elif age_group == '11-13':
                speaking_rate = 0.95
            else:  # 14-16
                speaking_rate = 1.0

            return {
                'engine': 'google',
                'language_code': 'en-US',
                'voice_name': 'en-US-Wavenet-D',  # Male voice
                'speaking_rate': speaking_rate,
                'pitch': 0,
                'character': 'Uncle Ray Ramiz - English'
            }

    def generate_coqui_tts_script(self, scripts: List[Dict[str, Any]]) -> Path:
        """
        Generate Python script for Coqui TTS (free, local)

        Requires: pip install TTS
        """

        script_file = self.output_dir / "generate_audio_coqui.py"

        script_content = f'''"""
Coqui TTS Audio Generation Script
Generated: {datetime.now().isoformat()}
Total Audio Files: {len(scripts)}

Requirements:
pip install TTS
"""

from TTS.api import TTS
from pathlib import Path
import json

# Configuration
OUTPUT_DIR = Path("{self.output_dir}")
MODEL_NAME = "tts_models/en/ljspeech/tacotron2-DDC"  # English model

# Initialize TTS
print(f"Loading Coqui TTS model: {{MODEL_NAME}}")
tts = TTS(model_name=MODEL_NAME)

# Audio scripts
scripts = {json.dumps(scripts, indent=2)}

# Generate audio files
for i, script_data in enumerate(scripts, 1):
    print(f"\\nGenerating audio {{i}}/{{len(scripts)}}")
    print(f"Lesson: {{script_data['lesson_id']}}")
    print(f"Language: {{script_data['language']}}")
    print(f"Output: {{script_data['output_filename']}}")

    try:
        # Generate audio
        output_path = OUTPUT_DIR / script_data['output_filename']

        tts.tts_to_file(
            text=script_data['script'],
            file_path=str(output_path)
        )

        print(f"Saved: {{output_path}}")

    except Exception as e:
        print(f"Error generating audio: {{e}}")

print("\\nGeneration complete!")
'''

        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(script_content)

        print(f"Generated Coqui TTS script: {script_file}")
        return script_file

    def generate_google_tts_script(self, scripts: List[Dict[str, Any]]) -> Path:
        """
        Generate Python script for Google Cloud TTS (paid, high quality)

        Requires: pip install google-cloud-texttospeech
        """

        script_file = self.output_dir / "generate_audio_google.py"

        script_content = f'''"""
Google Cloud TTS Audio Generation Script
Generated: {datetime.now().isoformat()}
Total Audio Files: {len(scripts)}

Requirements:
pip install google-cloud-texttospeech
export GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json"
"""

from google.cloud import texttospeech
from pathlib import Path
import json

# Configuration
OUTPUT_DIR = Path("{self.output_dir}")

# Initialize client
print("Initializing Google Cloud TTS client")
client = texttospeech.TextToSpeechClient()

# Audio scripts
scripts = {json.dumps(scripts, indent=2)}

# Generate audio files
for i, script_data in enumerate(scripts, 1):
    print(f"\\nGenerating audio {{i}}/{{len(scripts)}}")
    print(f"Lesson: {{script_data['lesson_id']}}")
    print(f"Language: {{script_data['language']}}")
    print(f"Voice: {{script_data['voice_profile']['voice_name']}}")
    print(f"Output: {{script_data['output_filename']}}")

    try:
        # Set text input
        synthesis_input = texttospeech.SynthesisInput(text=script_data['script'])

        # Voice configuration
        voice = texttospeech.VoiceSelectionParams(
            language_code=script_data['voice_profile']['language_code'],
            name=script_data['voice_profile']['voice_name']
        )

        # Audio configuration
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=script_data['voice_profile']['speaking_rate'],
            pitch=script_data['voice_profile']['pitch']
        )

        # Generate audio
        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )

        # Save audio
        output_path = OUTPUT_DIR / script_data['output_filename']
        with open(output_path, 'wb') as f:
            f.write(response.audio_content)

        print(f"Saved: {{output_path}}")

    except Exception as e:
        print(f"Error generating audio: {{e}}")

print("\\nGeneration complete!")
'''

        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(script_content)

        print(f"Generated Google Cloud TTS script: {script_file}")
        return script_file

    def generate_audio_manifest(self, scripts: List[Dict[str, Any]]) -> Path:
        """Generate JSON manifest for audio generation"""

        manifest_file = self.output_dir / "audio_generation_manifest.json"

        manifest = {
            "generation_info": {
                "created": datetime.now().isoformat(),
                "total_scripts": len(scripts),
                "output_directory": str(self.output_dir)
            },
            "scripts": scripts,
            "voice_profiles": {
                "uncle_ray_ramiz_turkish": {
                    "engine": "google",
                    "language": "Turkish",
                    "character": "Uncle Ray Ramiz - Turkish Dayı",
                    "voice_name": "tr-TR-Wavenet-B",
                    "description": "Warm, compassionate Turkish uncle voice"
                },
                "uncle_ray_ramiz_english": {
                    "engine": "google",
                    "language": "English",
                    "character": "Uncle Ray Ramiz - English",
                    "voice_name": "en-US-Wavenet-D",
                    "description": "Gentle, wise English narrator voice"
                }
            }
        }

        with open(manifest_file, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

        print(f"Generated audio manifest: {manifest_file}")
        return manifest_file

    def create_batch_scripts_file(self, scripts: List[Dict[str, Any]]) -> Path:
        """Create text file with all scripts for manual recording"""

        scripts_file = self.output_dir / "audio_scripts_for_recording.txt"

        with open(scripts_file, 'w', encoding='utf-8') as f:
            f.write(f"# Audio Scripts for Manual Recording\n")
            f.write(f"# Generated: {datetime.now().isoformat()}\n")
            f.write(f"# Total Scripts: {len(scripts)}\n")
            f.write(f"# Voice Character: Uncle Ray Ramiz\n")
            f.write("\n" + "="*80 + "\n\n")

            for i, script_data in enumerate(scripts, 1):
                f.write(f"## Script {i}/{len(scripts)}\n")
                f.write(f"Lesson ID: {script_data['lesson_id']}\n")
                f.write(f"Law Number: {script_data['law_number']}\n")
                f.write(f"Age Group: {script_data['age_group']}\n")
                f.write(f"Language: {script_data['language']}\n")
                f.write(f"Output File: {script_data['output_filename']}\n")
                f.write(f"Voice Character: {script_data['voice_profile']['character']}\n")
                f.write(f"\nScript:\n{script_data['script']}\n")
                f.write("\n" + "-"*80 + "\n\n")

        print(f"Generated scripts file for manual recording: {scripts_file}")
        return scripts_file

    def estimate_costs(self, scripts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Estimate costs for different TTS services"""

        # Average script length (characters)
        total_chars = sum(len(s['script']) for s in scripts)
        avg_chars = total_chars / len(scripts) if scripts else 0

        estimates = {
            "total_scripts": len(scripts),
            "total_characters": total_chars,
            "average_characters_per_script": avg_chars,
            "engines": {
                "coqui_tts": {
                    "cost": 0,
                    "description": "Free, local generation",
                    "quality": "Good",
                    "requirements": "GPU recommended",
                    "pros": ["Free", "Unlimited", "Privacy"],
                    "cons": ["Lower quality", "Slower", "Requires setup"]
                },
                "google_cloud_tts": {
                    "cost_per_million_chars": 4.00,  # Standard voices
                    "cost_wavenet_per_million_chars": 16.00,
                    "estimated_cost_standard": (total_chars / 1_000_000) * 4.00,
                    "estimated_cost_wavenet": (total_chars / 1_000_000) * 16.00,
                    "quality": "Excellent (WaveNet)",
                    "requirements": "Google Cloud account, API key",
                    "pros": ["High quality", "Multiple languages", "Fast"],
                    "cons": ["Paid", "Requires account"]
                },
                "amazon_polly": {
                    "cost_per_million_chars": 4.00,  # Standard voices
                    "cost_neural_per_million_chars": 16.00,
                    "estimated_cost_standard": (total_chars / 1_000_000) * 4.00,
                    "estimated_cost_neural": (total_chars / 1_000_000) * 16.00,
                    "quality": "Excellent (Neural)",
                    "requirements": "AWS account, API key",
                    "pros": ["High quality", "Multiple voices", "Reliable"],
                    "cons": ["Paid", "Requires AWS"]
                },
                "azure_tts": {
                    "cost_per_million_chars": 4.00,  # Standard
                    "cost_neural_per_million_chars": 16.00,
                    "estimated_cost_standard": (total_chars / 1_000_000) * 4.00,
                    "estimated_cost_neural": (total_chars / 1_000_000) * 16.00,
                    "quality": "Excellent (Neural)",
                    "requirements": "Azure account, API key",
                    "pros": ["High quality", "Good Turkish support"],
                    "cons": ["Paid", "Requires Azure"]
                },
                "manual_recording": {
                    "cost_per_hour": 50,  # Voice actor rate
                    "estimated_hours": len(scripts) * 2 / 60,  # 2 min per script avg
                    "estimated_cost": (len(scripts) * 2 / 60) * 50,
                    "quality": "Excellent (Human)",
                    "requirements": "Voice actor, recording equipment",
                    "pros": ["Best quality", "Authentic", "Uncle Ray Ramiz himself"],
                    "cons": ["Expensive", "Time-consuming", "Requires talent"]
                }
            },
            "recommendation": "Google Cloud TTS WaveNet for quality/cost balance"
        }

        return estimates

    def generate_all_automation(self):
        """Generate all audio automation files"""

        print("="*80)
        print("AUDIO SYNTHESIS AUTOMATION")
        print("="*80)
        print()

        # Load scripts
        print("1. Loading audio scripts...")
        scripts = self.load_audio_scripts()
        print(f"Total scripts loaded: {len(scripts)}")
        print()

        if not scripts:
            print("No scripts found. Check scripture directory location.")
            print(f"Expected: {self.scripture_dir}")
            return

        # Generate automation files
        print("2. Generating automation files...")
        self.generate_coqui_tts_script(scripts)
        self.generate_google_tts_script(scripts)
        self.generate_audio_manifest(scripts)
        self.create_batch_scripts_file(scripts)
        print()

        # Cost estimates
        print("3. Calculating cost estimates...")
        costs = self.estimate_costs(scripts)

        # Save cost estimates
        cost_file = self.output_dir / "audio_generation_cost_estimates.json"
        with open(cost_file, 'w', encoding='utf-8') as f:
            json.dump(costs, f, indent=2, ensure_ascii=False)
        print(f"Saved cost estimates: {cost_file}")
        print()

        # Display estimates
        print("="*80)
        print("COST ESTIMATES")
        print("="*80)
        print(f"Total Scripts: {costs['total_scripts']}")
        print(f"Total Characters: {costs['total_characters']:,}")
        print()

        for engine, data in costs['engines'].items():
            if engine == 'coqui_tts':
                print(f"{engine.upper()}:")
                print(f"  Cost: FREE")
                print(f"  Quality: {data['quality']}")
            elif engine == 'manual_recording':
                print(f"{engine.upper()}:")
                print(f"  Estimated Cost: ${data['estimated_cost']:.2f}")
                print(f"  Quality: {data['quality']}")
            else:
                if 'estimated_cost_wavenet' in data:
                    print(f"{engine.upper()} (WaveNet/Neural):")
                    print(f"  Estimated Cost: ${data['estimated_cost_wavenet']:.2f}")
                    print(f"  Quality: {data['quality']}")

        print()
        print(f"Recommendation: {costs['recommendation']}")
        print()

        # Create README
        self.create_audio_generation_readme(costs)

        print("="*80)
        print("GENERATION COMPLETE")
        print("="*80)
        print(f"\nOutput directory: {self.output_dir}")
        print("\nFiles generated:")
        print("  - Coqui TTS script (.py) - Free, local generation")
        print("  - Google Cloud TTS script (.py) - High quality, paid")
        print("  - Audio manifest (.json) - Complete metadata")
        print("  - Scripts for manual recording (.txt) - Human voice option")
        print("  - Cost estimates (.json) - Budget planning")
        print("  - README - Complete instructions")
        print()

    def create_audio_generation_readme(self, costs: Dict):
        """Create README with generation instructions"""

        readme_file = self.output_dir / "README_AUDIO_GENERATION.md"

        content = f"""# Audio Generation Guide

## Overview

Generate audio files for all {costs['total_scripts']} scripture lessons.

**Voice Character:** Uncle Ray Ramiz
- Turkish Dayı (uncle) voice for Turkish lessons
- Gentle, compassionate English for English lessons
- Age-appropriate pacing and tone

## Generation Methods

### Method 1: Google Cloud TTS (Recommended)

**Quality:** Excellent (WaveNet voices)
**Cost:** ~${costs['engines']['google_cloud_tts']['estimated_cost_wavenet']:.2f}
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
**Cost:** ~${costs['engines']['manual_recording']['estimated_cost']:.2f}
**Time:** ~{costs['engines']['manual_recording']['estimated_hours']:.1f} hours

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
| Google Cloud TTS (Standard) | ${costs['engines']['google_cloud_tts']['estimated_cost_standard']:.2f} | Very Good | Fast |
| Google Cloud TTS (WaveNet) | ${costs['engines']['google_cloud_tts']['estimated_cost_wavenet']:.2f} | Excellent | Fast |
| Amazon Polly (Neural) | ${costs['engines']['amazon_polly']['estimated_cost_neural']:.2f} | Excellent | Fast |
| Azure TTS (Neural) | ${costs['engines']['azure_tts']['estimated_cost_neural']:.2f} | Excellent | Fast |
| Manual Recording | ${costs['engines']['manual_recording']['estimated_cost']:.2f} | Best | Very Long |

**Recommendation:** Google Cloud TTS WaveNet for quality/cost balance.

## Verification Checklist

After generation:
- [ ] All {costs['total_scripts']} audio files created
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
"""

        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Created audio generation README: {readme_file}")


def main():
    """Generate all audio automation files"""

    generator = AudioSynthesisAutomation()
    generator.generate_all_automation()

    print("\nAudio synthesis automation ready!")
    print("Check S:/JAN/output/audio_assets/ for all files.")


if __name__ == "__main__":
    main()
