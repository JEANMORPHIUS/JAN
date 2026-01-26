"""Visual Asset Generation Pipeline
Generates images for 376 scripture lessons + 208 social media posts

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Visual beauty serving spiritual truth

THE FOUNDATION:
We are born a miracle.
Visual art must reflect divine beauty.
Every image serves the mission.

THE MISSION:
Generate 584+ images total:
- 376 scripture lesson visuals (age-appropriate)
- 208 social media post graphics
- Marketing materials
- Entity profile images

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, load_json, save_json,
    setup_logging, standard_main
)

import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
import subprocess
import sys

class VisualAssetGenerator:
    """
    Generates visual assets using AI image generation

    Supports:
    - Scripture lesson visuals (376 lessons)
    - Social media graphics (208 posts)
    - Marketing materials
    - Entity profile images
    """

    def __init__(self, project_root: str = "S:/JAN"):
        self.project_root = Path(project_root)
        self.scripture_dir = self.project_root / "jan-studio" / "curriculum" / "scripture_schedule_2026"
        self.social_dir = self.project_root / "data" / "2026_social_content"
        self.output_dir = self.project_root / "output" / "visual_assets"
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.generation_log: List[Dict] = []

    def load_scripture_prompts(self) -> List[Dict[str, Any]]:
        """Load all 376 scripture lesson visual prompts"""

        prompts = []

        if not self.scripture_dir.exists():
            print(f"Warning: Scripture directory not found: {self.scripture_dir}")
            return prompts

        # Load all lesson JSON files
        for lesson_file in self.scripture_dir.glob("*.json"):
            try:
                with open(lesson_file, 'r', encoding='utf-8') as f:
                    lesson = json.load(f)

                    if 'visual_prompt' in lesson:
                        prompts.append({
                            'type': 'scripture_lesson',
                            'lesson_id': lesson.get('lesson_id', lesson_file.stem),
                            'law_number': lesson.get('law_number'),
                            'age_group': lesson.get('age_group'),
                            'language': lesson.get('language', 'en'),
                            'prompt': lesson['visual_prompt'],
                            'output_filename': f"scripture_{lesson_file.stem}.png"
                        })
            except Exception as e:
                print(f"Error loading {lesson_file}: {e}")

        print(f"Loaded {len(prompts)} scripture lesson visual prompts")
        return prompts

    def load_social_media_prompts(self) -> List[Dict[str, Any]]:
        """Load all 208 social media post visual prompts"""

        prompts = []

        # Check for social content files
        social_files = [
            self.social_dir / "2026_edible_london_posts.json",
            self.social_dir / "2026_ilven_seamoss_posts.json",
            self.social_dir / "2026_karasahin_posts.json",
            self.social_dir / "2026_pierre_pressure_posts.json"
        ]

        for social_file in social_files:
            if not social_file.exists():
                print(f"Warning: Social file not found: {social_file}")
                continue

            try:
                with open(social_file, 'r', encoding='utf-8') as f:
                    posts = json.load(f)

                    for post in posts:
                        if 'visual_prompt' in post:
                            entity = social_file.stem.replace('2026_', '').replace('_posts', '')
                            prompts.append({
                                'type': 'social_media',
                                'entity': entity,
                                'post_number': post.get('post_number'),
                                'platform': post.get('platform', 'instagram'),
                                'prompt': post['visual_prompt'],
                                'output_filename': f"social_{entity}_post_{post.get('post_number', 'unknown')}.png"
                            })
            except Exception as e:
                print(f"Error loading {social_file}: {e}")

        print(f"Loaded {len(prompts)} social media visual prompts")
        return prompts

    def generate_prompt_batch_file(self, prompts: List[Dict[str, Any]], batch_name: str) -> Path:
        """
        Generate a batch file for external image generation tools

        Creates a text file with prompts that can be used with:
        - Stable Diffusion
        - DALL-E
        - Midjourney
        - Other image generation tools
        """

        batch_file = self.output_dir / f"{batch_name}_prompts.txt"

        with open(batch_file, 'w', encoding='utf-8') as f:
            f.write(f"# {batch_name.upper()} - Visual Asset Generation Prompts\n")
            f.write(f"# Generated: {datetime.now().isoformat()}\n")
            f.write(f"# Total Prompts: {len(prompts)}\n")
            f.write("\n" + "="*80 + "\n\n")

            for i, prompt_data in enumerate(prompts, 1):
                f.write(f"## Prompt {i}/{len(prompts)}\n")
                f.write(f"Type: {prompt_data['type']}\n")
                f.write(f"Output File: {prompt_data['output_filename']}\n")

                if prompt_data['type'] == 'scripture_lesson':
                    f.write(f"Lesson ID: {prompt_data['lesson_id']}\n")
                    f.write(f"Law Number: {prompt_data['law_number']}\n")
                    f.write(f"Age Group: {prompt_data['age_group']}\n")
                    f.write(f"Language: {prompt_data['language']}\n")
                elif prompt_data['type'] == 'social_media':
                    f.write(f"Entity: {prompt_data['entity']}\n")
                    f.write(f"Post Number: {prompt_data['post_number']}\n")
                    f.write(f"Platform: {prompt_data['platform']}\n")

                f.write(f"\nPrompt:\n{prompt_data['prompt']}\n")
                f.write("\n" + "-"*80 + "\n\n")

        print(f"Generated prompt batch file: {batch_file}")
        return batch_file

    def generate_json_manifest(self, prompts: List[Dict[str, Any]], manifest_name: str) -> Path:
        """
        Generate JSON manifest for programmatic image generation

        Can be used with APIs like:
        - OpenAI DALL-E API
        - Stability AI API
        - Replicate API
        """

        manifest_file = self.output_dir / f"{manifest_name}_manifest.json"

        manifest = {
            "generation_info": {
                "created": datetime.now().isoformat(),
                "total_prompts": len(prompts),
                "manifest_name": manifest_name,
                "output_directory": str(self.output_dir)
            },
            "prompts": prompts
        }

        with open(manifest_file, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

        print(f"Generated JSON manifest: {manifest_file}")
        return manifest_file

    def generate_stable_diffusion_script(self, prompts: List[Dict[str, Any]], script_name: str) -> Path:
        """
        Generate Python script for Stable Diffusion local generation

        Requires: diffusers, torch, transformers
        """

        script_file = self.output_dir / f"{script_name}_sd_generator.py"

        script_content = f'''"""
Stable Diffusion Image Generation Script
Generated: {datetime.now().isoformat()}
Total Images: {len(prompts)}

Requirements:
pip install diffusers transformers torch pillow accelerate
"""

from diffusers import StableDiffusionPipeline
import torch
from pathlib import Path
import json

# Configuration
MODEL_ID = "runwayml/stable-diffusion-v1-5"  # Or other SD model
OUTPUT_DIR = Path("{self.output_dir}")
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Load prompts
prompts = {json.dumps(prompts, indent=2)}

# Initialize pipeline
print(f"Loading Stable Diffusion model: {{MODEL_ID}}")
pipe = StableDiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.float16)
pipe = pipe.to(DEVICE)

# Generate images
for i, prompt_data in enumerate(prompts, 1):
    print(f"\\nGenerating image {{i}}/{{len(prompts)}}")
    print(f"Type: {{prompt_data['type']}}")
    print(f"Output: {{prompt_data['output_filename']}}")

    try:
        # Generate image
        image = pipe(
            prompt=prompt_data['prompt'],
            num_inference_steps=50,
            guidance_scale=7.5
        ).images[0]

        # Save image
        output_path = OUTPUT_DIR / prompt_data['output_filename']
        image.save(output_path)
        print(f"Saved: {{output_path}}")

    except Exception as e:
        print(f"Error generating image: {{e}}")

print("\\nGeneration complete!")
'''

        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(script_content)

        print(f"Generated Stable Diffusion script: {script_file}")
        return script_file

    def generate_all_assets(self):
        """
        Generate all visual assets

        Creates:
        1. Prompt batch files (for manual generation)
        2. JSON manifests (for API integration)
        3. Stable Diffusion scripts (for local generation)
        """

        print("="*80)
        print("VISUAL ASSET GENERATION PIPELINE")
        print("="*80)
        print()

        # Load all prompts
        print("1. Loading prompts...")
        scripture_prompts = self.load_scripture_prompts()
        social_prompts = self.load_social_media_prompts()
        all_prompts = scripture_prompts + social_prompts

        print(f"\nTotal prompts loaded: {len(all_prompts)}")
        print(f"  - Scripture lessons: {len(scripture_prompts)}")
        print(f"  - Social media: {len(social_prompts)}")
        print()

        # Generate scripture lesson assets
        print("2. Generating scripture lesson asset files...")
        if scripture_prompts:
            self.generate_prompt_batch_file(scripture_prompts, "scripture_lessons")
            self.generate_json_manifest(scripture_prompts, "scripture_lessons")
            self.generate_stable_diffusion_script(scripture_prompts, "scripture_lessons")
        print()

        # Generate social media assets
        print("3. Generating social media asset files...")
        if social_prompts:
            self.generate_prompt_batch_file(social_prompts, "social_media")
            self.generate_json_manifest(social_prompts, "social_media")
            self.generate_stable_diffusion_script(social_prompts, "social_media")
        print()

        # Generate combined assets
        print("4. Generating combined asset files...")
        if all_prompts:
            self.generate_prompt_batch_file(all_prompts, "all_visual_assets")
            self.generate_json_manifest(all_prompts, "all_visual_assets")
            self.generate_stable_diffusion_script(all_prompts, "all_visual_assets")
        print()

        # Summary
        print("="*80)
        print("GENERATION COMPLETE")
        print("="*80)
        print(f"\nOutput directory: {self.output_dir}")
        print(f"\nFiles generated:")
        print("  - Prompt batch files (.txt) - For manual/Midjourney generation")
        print("  - JSON manifests (.json) - For API integration")
        print("  - SD Python scripts (.py) - For local Stable Diffusion generation")
        print()
        print("NEXT STEPS:")
        print("  1. Choose generation method:")
        print("     a) Manual: Use batch .txt files with DALL-E/Midjourney")
        print("     b) API: Use JSON manifests with OpenAI/Stability APIs")
        print("     c) Local: Run SD Python scripts (requires GPU)")
        print()
        print("  2. Generate images")
        print("  3. Move generated images to output directory")
        print("  4. Verify all images created")
        print()

    def create_example_generation_readme(self):
        """Create README with generation instructions"""

        readme_file = self.output_dir / "README_VISUAL_GENERATION.md"

        content = """# Visual Asset Generation Guide

## Overview

This directory contains all files needed to generate visual assets for the JAN/SIYEM system.

**Total Assets Needed:**
- 376 scripture lesson visuals
- 208 social media post graphics
- Marketing materials
- Entity profile images

## Generation Methods

### Method 1: OpenAI DALL-E API (Recommended for Quality)

```python
import openai
import json

# Load manifest
manifest = load_json('all_visual_assets_manifest.json')

# Generate images
for prompt_data in manifest['prompts']:
    response = openai.Image.create(
        prompt=prompt_data['prompt'],
        n=1,
        size="1024x1024"
    )

    image_url = response['data'][0]['url']
    # Download and save image as prompt_data['output_filename']
```

### Method 2: Stable Diffusion Local (Recommended for Cost)

```bash
# Install dependencies
pip install diffusers transformers torch pillow accelerate

# Run generation script
python all_visual_assets_sd_generator.py
```

### Method 3: Midjourney (Recommended for Artistic Quality)

1. Open `all_visual_assets_prompts.txt`
2. Copy each prompt to Midjourney Discord
3. Save generated images with corresponding output filenames

### Method 4: Stability AI API

```python
import requests
import json

# Load manifest
manifest = load_json('all_visual_assets_manifest.json')

# API endpoint
url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

for prompt_data in manifest['prompts']:
    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "text_prompts": [{"text": prompt_data['prompt']}],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "steps": 30
        }
    )

    # Save image as prompt_data['output_filename']
```

## Budget Estimates

### DALL-E 3 (OpenAI)
- Cost: $0.04 per 1024x1024 image
- Total: ~$23 for 584 images
- Quality: Excellent
- Speed: Fast (API)

### Stable Diffusion (Local)
- Cost: $0 (requires GPU)
- Total: Free
- Quality: Very Good
- Speed: Moderate (depends on GPU)

### Midjourney
- Cost: $10/month Basic Plan (limited generations)
- Cost: $30/month Standard Plan (unlimited in relaxed mode)
- Quality: Excellent (artistic)
- Speed: Moderate (queue-based)

### Stability AI API
- Cost: $0.002 per image (SDXL 1.0)
- Total: ~$1.17 for 584 images
- Quality: Very Good
- Speed: Fast (API)

## Recommended Approach

**For Budget:** Stability AI API ($1.17 total)
**For Quality:** Mix of DALL-E for key images + Stable Diffusion for bulk
**For Artistic:** Midjourney for social media, Stable Diffusion for lessons

## Quality Guidelines

### Scripture Lessons (Ages 5-16)
- Age-appropriate imagery
- Cultural sensitivity
- Positive, uplifting tone
- Clear visual metaphors
- No violence, fear, or negativity

### Social Media Posts
- Platform-optimized dimensions
- Brand-consistent styling
- Eye-catching composition
- Text-overlay ready
- High engagement potential

### Marketing Materials
- Professional quality
- Brand alignment
- Multi-format support
- Print and digital ready

## Verification Checklist

After generation, verify:
- [ ] All 376 scripture lesson images created
- [ ] All 208 social media images created
- [ ] Images match output filenames
- [ ] Quality meets standards
- [ ] Age-appropriate content
- [ ] Cultural sensitivity maintained
- [ ] No copyright violations

## Support

For questions or issues with generation, check:
1. Prompt quality in source files
2. API rate limits
3. GPU memory (for local generation)
4. Output directory permissions

## Philosophy

Every image serves the mission:
- Visual beauty reflecting divine truth
- Accessibility for all ages
- Cultural respect and sensitivity
- Love as the highest mastery

**We are born a miracle. Every image must reflect that miracle.**
"""

        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Created generation README: {readme_file}")


def main():
    """Generate all visual asset files"""

    generator = VisualAssetGenerator()
    generator.generate_all_assets()
    generator.create_example_generation_readme()

    print("\nVisual asset generation pipeline ready!")
    print("Check S:/JAN/output/visual_assets/ for all files.")


if __name__ == "__main__":
    main()
