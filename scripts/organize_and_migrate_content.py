"""
Content Organization and Migration Script
Organizes all existing content for asset generation pipelines

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Organize what exists, prepare for generation

THE MISSION:
- Locate all existing scripture content
- Locate all existing social media content
- Organize into proper directory structure
- Extract prompts for asset generation
- Prepare content for pipelines

PEACE. LOVE. UNITY.
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
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

class ContentOrganizer:
    """Organize and migrate all content for asset generation"""

    def __init__(self, project_root: str = "S:/JAN"):
        self.project_root = Path(project_root)
        self.jan_studio = self.project_root / "jan-studio"
        self.backend = self.jan_studio / "backend"

        # Target directories
        self.scripture_dir = self.jan_studio / "curriculum" / "scripture_schedule_2026"
        self.social_dir = self.project_root / "data" / "2026_social_content"
        self.visual_prompts_dir = self.project_root / "output" / "visual_prompts"
        self.audio_scripts_dir = self.project_root / "output" / "audio_scripts"

        # Create directories
        self.scripture_dir.mkdir(parents=True, exist_ok=True)
        self.social_dir.mkdir(parents=True, exist_ok=True)
        self.visual_prompts_dir.mkdir(parents=True, exist_ok=True)
        self.audio_scripts_dir.mkdir(parents=True, exist_ok=True)

    def load_scripture_schedule(self) -> Dict[str, Any]:
        """Load the populated scripture schedule"""

        print("\n" + "="*80)
        print("LOADING SCRIPTURE SCHEDULE")
        print("="*80 + "\n")

        # Try populated first, then base schedule
        schedule_files = [
            self.backend / "scripture_schedule_2026_populated.json",
            self.backend / "scripture_schedule_2026.json"
        ]

        for schedule_file in schedule_files:
            if schedule_file.exists():
                with open(schedule_file, 'r', encoding='utf-8') as f:
                    schedule = json.load(f)

                # Check for posts in different structures
                posts = schedule.get('posts', [])
                if not posts:
                    posts = schedule.get('all_posts', [])

                print(f"[OK] Loaded: {schedule_file.name}")
                print(f"     Total posts: {len(posts)}\n")

                # Normalize structure
                schedule['posts'] = posts
                return schedule

        print("[ERROR] No scripture schedule found\n")
        return {}

    def extract_scripture_lessons(self, schedule: Dict[str, Any]) -> int:
        """Extract individual scripture lessons from schedule"""

        print("="*80)
        print("EXTRACTING SCRIPTURE LESSONS")
        print("="*80 + "\n")

        posts = schedule.get('posts', [])

        if not posts:
            print("[WARNING] No posts found in schedule\n")
            return 0

        # Group by lesson (filter unique by title)
        # Posts may not have scripture_reference, use title and content hash
        unique_lessons = {}
        for post in posts:
            title = post.get('title', '')
            content = post.get('content', '')[:100]  # First 100 chars for uniqueness
            key = f"{title}_{hash(content)}"

            if key not in unique_lessons and title:  # Only add if has title
                unique_lessons[key] = post

        print(f"Found {len(unique_lessons)} unique scripture lessons\n")
        print(f"Total scheduled posts: {len(posts)}")
        print(f"(Posts are scheduled multiple times across entities)\n")

        # Extract each unique lesson
        lesson_count = 0
        for i, (key, post) in enumerate(unique_lessons.items(), 1):
            # Extract metadata if present
            metadata = post.get('metadata', {})

            # Extract teaching components from content if structured
            content_text = post.get('content', '')

            lesson_data = {
                "lesson_id": f"lesson_{i:03d}",
                "scripture_reference": metadata.get('scripture_reference', ''),
                "title": post.get('title', ''),
                "content": content_text,
                "key_teaching": metadata.get('key_teaching', self._extract_key_teaching(content_text)),
                "practical_application": metadata.get('practical_application', ''),
                "reflection_question": metadata.get('reflection_question', ''),
                "age_group": metadata.get('age_group', '5-7'),
                "language": "en",
                "hashtags": post.get('hashtags', []),
                "scheduled_time": post.get('scheduled_time', ''),

                # Visual prompt
                "visual_prompt": self._generate_visual_prompt(post),

                # Audio script
                "audio_script": self._generate_audio_script(post),

                # Metadata
                "created": datetime.now().isoformat(),
                "source": "scripture_schedule_2026"
            }

            # Save individual lesson file
            lesson_file = self.scripture_dir / f"{lesson_data['lesson_id']}.json"
            with open(lesson_file, 'w', encoding='utf-8') as f:
                json.dump(lesson_data, f, indent=2, ensure_ascii=False)

            lesson_count += 1

            if lesson_count % 50 == 0:
                print(f"  Extracted {lesson_count} lessons...")

        print(f"\n[OK] Extracted {lesson_count} unique scripture lessons")
        print(f"     Saved to: {self.scripture_dir}\n")

        return lesson_count

    def _extract_key_teaching(self, content: str) -> str:
        """Extract or summarize key teaching from content"""

        if not content:
            return "Love, unity, and service to humanity"

        # Take first sentence or first 150 chars as key teaching
        sentences = content.split('.')
        if sentences:
            key_teaching = sentences[0].strip() + '.'
            if len(key_teaching) > 150:
                key_teaching = key_teaching[:147] + "..."
            return key_teaching

        return content[:150] + "..." if len(content) > 150 else content

    def _generate_visual_prompt(self, post: Dict[str, Any]) -> str:
        """Generate visual prompt for image generation"""

        metadata = post.get('metadata', {})
        scripture_ref = metadata.get('scripture_reference', '')
        title = post.get('title', '')
        content = post.get('content', '')
        key_teaching = metadata.get('key_teaching', self._extract_key_teaching(content))
        age_group = metadata.get('age_group', '5-7')

        # Age-appropriate visual style
        if age_group in ['5-7', '8-10']:
            style = "warm, gentle, child-friendly illustration"
        elif age_group in ['11-13']:
            style = "inspiring, uplifting digital art"
        else:  # 14-16
            style = "meaningful, contemplative artistic rendering"

        prompt = f"""Create a {style} depicting the teaching from {scripture_ref}: "{title}".

Key message: {key_teaching}

Style guidelines:
- Age-appropriate for {age_group} years old
- Warm, peaceful colors
- Universal symbols (no specific religious imagery)
- Inclusive representation
- Inspiring and uplifting
- Clear central focus

Technical: High resolution, suitable for social media and educational materials."""

        return prompt

    def _generate_audio_script(self, post: Dict[str, Any]) -> str:
        """Generate audio script for Uncle Ray Ramiz voice"""

        metadata = post.get('metadata', {})
        title = post.get('title', '')
        scripture_ref = metadata.get('scripture_reference', '')
        content = post.get('content', '')
        key_teaching = metadata.get('key_teaching', self._extract_key_teaching(content))
        practical_application = metadata.get('practical_application', 'Think about how you can share love and kindness with others today.')
        reflection_question = metadata.get('reflection_question', 'How can you use this teaching in your life?')
        age_group = metadata.get('age_group', '5-7')

        # Uncle Ray Ramiz persona (warm, wise, caring Turkish uncle)
        script = f"""[Uncle Ray Ramiz - Warm, caring tone]

Hello my dear young friends. Uncle Ray here, and today we're going to talk about something beautiful.

[Pause]

Our lesson today is called "{title}" and it comes from {scripture_ref}.

[Pause]

{content}

[Slower, more thoughtful]

The important thing to remember is this: {key_teaching}

[Warmer, encouraging tone]

Now, how can we use this in our lives? {practical_application}

[Pause]

And here's something for you to think about: {reflection_question}

[Warm closing]

Remember, you are loved, you are valued, and you have everything you need inside you to live a beautiful life.

This is Uncle Ray Ramiz, sending you peace, love, and unity.

[End]

[VOICE NOTES]
- Age group: {age_group}
- Tone: Warm, caring, wise
- Pace: {"Slower, very gentle" if age_group in ['5-7'] else "Moderate, clear" if age_group in ['8-10', '11-13'] else "Natural, thoughtful"}
- Character: Turkish Dayı (uncle) - caring, wise, humble
- Language: English (with slight warm accent acceptable)
"""

        return script

    def organize_social_content(self, schedule: Dict[str, Any]) -> int:
        """Organize social media content by entity"""

        print("="*80)
        print("ORGANIZING SOCIAL MEDIA CONTENT")
        print("="*80 + "\n")

        posts = schedule.get('posts', [])

        if not posts:
            print("[WARNING] No posts to organize\n")
            return 0

        # Group by entity (extract from metadata or scheduled_time platform info)
        entities = {}
        for post in posts:
            # Try to extract entity from metadata or platform
            metadata = post.get('metadata', {})
            entity = metadata.get('entity', '')

            # If no entity in metadata, try to extract from platform/location
            if not entity:
                platform = post.get('platform', '')
                if 'edible_london' in platform.lower():
                    entity = 'edible_london'
                elif 'ilven' in platform.lower():
                    entity = 'ilven_seamoss'
                elif 'jean' in platform.lower() or 'mahram' in platform.lower():
                    entity = 'jean_mahram'
                elif 'karasahin' in platform.lower() or 'jk' in platform.lower():
                    entity = 'karasahin_jk'
                elif 'pierre' in platform.lower():
                    entity = 'pierre_pressure'
                elif 'uncle' in platform.lower() or 'ray' in platform.lower() or 'ramiz' in platform.lower():
                    entity = 'uncle_ray_ramiz'
                elif 'siyem' in platform.lower():
                    entity = 'siyem_media'
                else:
                    entity = 'all_entities'

            if entity not in entities:
                entities[entity] = []
            entities[entity].append(post)

        print(f"Found posts for {len(entities)} entities:\n")

        total_saved = 0
        for entity, entity_posts in entities.items():
            entity_dir = self.social_dir / entity
            entity_dir.mkdir(parents=True, exist_ok=True)

            for i, post in enumerate(entity_posts, 1):
                metadata = post.get('metadata', {})

                post_data = {
                    "post_id": f"{entity}_{i:03d}",
                    "entity": entity,
                    "scheduled_date": post.get('scheduled_time', ''),
                    "title": post.get('title', ''),
                    "content": post.get('content', ''),
                    "scripture_reference": metadata.get('scripture_reference', ''),
                    "hashtags": post.get('hashtags', []),
                    "platform": post.get('platform', ''),
                    "format": metadata.get('format', 'scripture_lesson'),

                    # Visual prompt for social media graphic
                    "visual_prompt": self._generate_social_visual_prompt(post),

                    # Metadata
                    "created": datetime.now().isoformat()
                }

                post_file = entity_dir / f"{post_data['post_id']}.json"
                with open(post_file, 'w', encoding='utf-8') as f:
                    json.dump(post_data, f, indent=2, ensure_ascii=False)

                total_saved += 1

            print(f"  {entity}: {len(entity_posts)} posts")

        print(f"\n[OK] Organized {total_saved} social media posts")
        print(f"     Saved to: {self.social_dir}\n")

        return total_saved

    def _generate_social_visual_prompt(self, post: Dict[str, Any]) -> str:
        """Generate visual prompt for social media graphic"""

        metadata = post.get('metadata', {})
        title = post.get('title', '')
        scripture_ref = metadata.get('scripture_reference', '')
        entity = metadata.get('entity', post.get('platform', '').split('_')[0] if '_' in post.get('platform', '') else 'generic')

        prompt = f"""Create a social media graphic for: "{title}" ({scripture_ref})

Style: Clean, modern, inspiring
Format: Square (1080x1080) for Instagram/Facebook
Entity: {entity}

Visual elements:
- Prominent quote or key message
- Beautiful background (abstract, nature, or geometric)
- Readable typography
- Entity branding (subtle, tasteful)
- Inspiring and uplifting aesthetic
- Professional quality

Colors: Warm, peaceful palette
Typography: Clean, readable, modern
Overall: Eye-catching, shareable, inspiring"""

        return prompt

    def extract_visual_prompts(self) -> int:
        """Extract all visual prompts for batch generation"""

        print("="*80)
        print("EXTRACTING VISUAL PROMPTS")
        print("="*80 + "\n")

        all_prompts = []

        # Scripture lesson visuals
        print("1. Scripture lesson visuals...")
        scripture_prompts = []
        for lesson_file in self.scripture_dir.glob("*.json"):
            with open(lesson_file, 'r', encoding='utf-8') as f:
                lesson = json.load(f)

            scripture_prompts.append({
                'id': lesson['lesson_id'],
                'type': 'scripture_lesson',
                'prompt': lesson['visual_prompt'],
                'output_file': f"scripture_{lesson['lesson_id']}.png"
            })

        print(f"   Found {len(scripture_prompts)} scripture prompts\n")

        # Social media visuals
        print("2. Social media visuals...")
        social_prompts = []
        for post_file in self.social_dir.rglob("*.json"):
            with open(post_file, 'r', encoding='utf-8') as f:
                post = json.load(f)

            social_prompts.append({
                'id': post['post_id'],
                'type': 'social_media',
                'entity': post['entity'],
                'prompt': post['visual_prompt'],
                'output_file': f"social_{post['post_id']}.png"
            })

        print(f"   Found {len(social_prompts)} social media prompts\n")

        all_prompts = scripture_prompts + social_prompts

        # Save master prompt list
        prompts_file = self.visual_prompts_dir / "all_visual_prompts.json"
        with open(prompts_file, 'w', encoding='utf-8') as f:
            json.dump(all_prompts, f, indent=2, ensure_ascii=False)

        print(f"[OK] Extracted {len(all_prompts)} total visual prompts")
        print(f"     Saved to: {prompts_file}\n")

        return len(all_prompts)

    def extract_audio_scripts(self) -> int:
        """Extract all audio scripts for batch generation"""

        print("="*80)
        print("EXTRACTING AUDIO SCRIPTS")
        print("="*80 + "\n")

        all_scripts = []

        for lesson_file in self.scripture_dir.glob("*.json"):
            with open(lesson_file, 'r', encoding='utf-8') as f:
                lesson = json.load(f)

            all_scripts.append({
                'id': lesson['lesson_id'],
                'title': lesson['title'],
                'scripture_reference': lesson['scripture_reference'],
                'age_group': lesson['age_group'],
                'script': lesson['audio_script'],
                'output_file': f"audio_{lesson['lesson_id']}.mp3"
            })

        # Save master script list
        scripts_file = self.audio_scripts_dir / "all_audio_scripts.json"
        with open(scripts_file, 'w', encoding='utf-8') as f:
            json.dump(all_scripts, f, indent=2, ensure_ascii=False)

        print(f"[OK] Extracted {len(all_scripts)} audio scripts")
        print(f"     Saved to: {scripts_file}\n")

        return len(all_scripts)

    def generate_summary_report(self, lessons: int, social: int, visuals: int, audio: int):
        """Generate migration summary report"""

        report = f"""# Content Organization and Migration Complete

## Date: {datetime.now().isoformat()}

---

## MIGRATION SUMMARY

### Scripture Lessons
- **Total Unique Lessons:** {lessons}
- **Location:** `{self.scripture_dir.relative_to(self.project_root)}`
- **Status:** READY

### Social Media Content
- **Total Posts:** {social}
- **Location:** `{self.social_dir.relative_to(self.project_root)}`
- **Status:** ORGANIZED

### Visual Prompts
- **Total Prompts:** {visuals}
- **Location:** `{self.visual_prompts_dir.relative_to(self.project_root)}/all_visual_prompts.json`
- **Status:** READY FOR GENERATION

### Audio Scripts
- **Total Scripts:** {audio}
- **Location:** `{self.audio_scripts_dir.relative_to(self.project_root)}/all_audio_scripts.json`
- **Status:** READY FOR GENERATION

---

## DIRECTORY STRUCTURE

```
{self.jan_studio.name}/
  curriculum/
    scripture_schedule_2026/
      lesson_001.json ... lesson_{lessons:03d}.json

data/
  2026_social_content/
    <entity_name>/
      <entity_name>_001.json ...

output/
  visual_prompts/
    all_visual_prompts.json ({visuals} prompts)
  audio_scripts/
    all_audio_scripts.json ({audio} scripts)
```

---

## NEXT STEPS

### 1. Generate Visual Assets
```bash
python scripts/visual_asset_generator.py
```

### 2. Generate Audio Files
```bash
python scripts/audio_synthesis_automation.py
```

### 3. Build Raspberry Pi Packages
```bash
python scripts/raspberry_pi_package_builder.py
```

---

## PHILOSOPHY

**Purpose Not Performance** - Content serves souls, not metrics
**Love Is The Highest Mastery** - Every lesson carries love
**Pangea Is The Table** - Education for all humanity

**PEACE. LOVE. UNITY.**

---

*Migration complete: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
*Ready for asset generation and deployment*
"""

        report_file = self.project_root / "CONTENT_MIGRATION_COMPLETE.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)

        print(f"Migration report saved: {report_file}")

    def run_complete_migration(self):
        """Run complete content migration"""

        print("\n" + "="*80)
        print("CONTENT ORGANIZATION AND MIGRATION")
        print("JAN/SIYEM Complete System")
        print("="*80)

        # Load scripture schedule
        schedule = self.load_scripture_schedule()

        if not schedule:
            print("\n[ERROR] No scripture schedule found. Cannot migrate.\n")
            return

        # Extract scripture lessons
        lessons_count = self.extract_scripture_lessons(schedule)

        # Organize social content
        social_count = self.organize_social_content(schedule)

        # Extract prompts and scripts
        visual_count = self.extract_visual_prompts()
        audio_count = self.extract_audio_scripts()

        # Generate summary
        print("="*80)
        print("MIGRATION COMPLETE")
        print("="*80 + "\n")

        print(f"Scripture Lessons: {lessons_count}")
        print(f"Social Media Posts: {social_count}")
        print(f"Visual Prompts: {visual_count}")
        print(f"Audio Scripts: {audio_count}\n")

        self.generate_summary_report(lessons_count, social_count, visual_count, audio_count)

        print("\n" + "="*80)
        print("READY FOR ASSET GENERATION")
        print("="*80 + "\n")

        print("PEACE. LOVE. UNITY.")
        print("CONTENT ORGANIZED. SYSTEMS READY.\n")


def main():
    """Run content organization and migration"""

    organizer = ContentOrganizer()
    organizer.run_complete_migration()


if __name__ == "__main__":
    main()
