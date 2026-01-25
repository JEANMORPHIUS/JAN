# Visual Asset Generation Guide

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
