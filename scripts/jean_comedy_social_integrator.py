"""JEAN MORPHIUS - COMEDY SOCIAL INTEGRATOR
Integrate Comedy Material with Social Media Content Generation

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PURPOSE:
Integrate comedy material into social media content
Generate comedy posts for all platforms
Connect with content auto-populator
Asset management integration

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import json
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import random

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from jean_comedy_material_generator import generate_comedy_collection, ComedyStyle, ComedyMaterial
    from jean_comedy_template_library import COMEDY_TEMPLATE_LIBRARY
    COMEDY_AVAILABLE = True
except ImportError:
    COMEDY_AVAILABLE = False
    print("Warning: Comedy system not available.")


class JeanComedySocialIntegrator:
    """Integrate comedy material with social media content"""
    
    def __init__(self):
        self.platforms = {
            "instagram": {
                "max_length": 2200,
                "hashtags": 30,
                "supports_video": True,
                "supports_carousel": True
            },
            "twitter": {
                "max_length": 280,
                "hashtags": 5,
                "supports_video": True,
                "supports_threads": True
            },
            "tiktok": {
                "max_length": 2200,
                "hashtags": 10,
                "supports_video": True,
                "video_focused": True
            },
            "facebook": {
                "max_length": 5000,
                "hashtags": 10,
                "supports_video": True,
                "supports_long_form": True
            },
            "youtube": {
                "max_length": 5000,
                "hashtags": 15,
                "supports_video": True,
                "video_platform": True
            }
        }
    
    def format_comedy_for_platform(self, material: ComedyMaterial, platform: str) -> Dict[str, Any]:
        """Format comedy material for specific platform"""
        
        platform_specs = self.platforms.get(platform, self.platforms["instagram"])
        
        # Build content based on style
        if material.style == ComedyStyle.PETER_KAY:
            content = self._format_peter_kay(material, platform_specs)
        elif material.style == ComedyStyle.HASAN_CAN_KAYA:
            content = self._format_hasan_can_kaya(material, platform_specs)
        elif material.style in [ComedyStyle.MILTON_JONES, ComedyStyle.GARY_DELANEY]:
            content = self._format_one_liner(material, platform_specs)
        elif material.style == ComedyStyle.EDDIE_IZZARD:
            content = self._format_surreal(material, platform_specs)
        elif material.style == ComedyStyle.BILL_BAILEY:
            content = self._format_musical(material, platform_specs)
        elif material.style == ComedyStyle.SEAN_LOCK:
            content = self._format_deadpan(material, platform_specs)
        else:
            content = self._format_generic(material, platform_specs)
        
        # Add hashtags
        hashtags = self._generate_hashtags(material, platform_specs)
        
        return {
            "content": content,
            "hashtags": hashtags,
            "content_type": "text",
            "platform": platform,
            "comedy_style": material.style.value,
            "metadata": {
                "category": material.category,
                "delivery_notes": material.delivery_notes,
                "tags": material.tags
            }
        }
    
    def _format_peter_kay(self, material: ComedyMaterial, specs: Dict) -> str:
        """Format Peter Kay style for platform"""
        content = f"{material.setup}\n\n{material.observation}\n\n{material.bilingual_delivery}\n\n{material.punchline}"
        
        if len(content) > specs["max_length"]:
            content = content[:specs["max_length"] - 3] + "..."
        
        return content
    
    def _format_hasan_can_kaya(self, material: ComedyMaterial, specs: Dict) -> str:
        """Format Hasan Can Kaya style for platform"""
        content = f"{material.setup}\n\n{material.observation}\n\n{material.bilingual_delivery}\n\n{material.punchline}"
        
        if len(content) > specs["max_length"]:
            content = content[:specs["max_length"] - 3] + "..."
        
        return content
    
    def _format_one_liner(self, material: ComedyMaterial, specs: Dict) -> str:
        """Format one-liner for platform"""
        content = f"{material.setup}\n\n{material.wordplay}\n\n{material.punchline}"
        
        if len(content) > specs["max_length"]:
            content = material.punchline  # Just the punchline for short platforms
        
        return content
    
    def _format_surreal(self, material: ComedyMaterial, specs: Dict) -> str:
        """Format surreal stream-of-consciousness for platform"""
        content = f"{material.setup}\n\n{material.observation}\n\n{material.bilingual_delivery}\n\n{material.punchline}"
        
        if len(content) > specs["max_length"]:
            # For short platforms, condense
            content = f"{material.setup} {material.punchline}"
        
        return content
    
    def _format_musical(self, material: ComedyMaterial, specs: Dict) -> str:
        """Format musical comedy for platform"""
        content = f"{material.setup}\n\n{material.observation}\n\n{material.bilingual_delivery}\n\n{material.punchline}"
        
        if len(content) > specs["max_length"]:
            content = content[:specs["max_length"] - 3] + "..."
        
        return content
    
    def _format_deadpan(self, material: ComedyMaterial, specs: Dict) -> str:
        """Format deadpan for platform"""
        content = f"{material.setup}\n\n{material.observation}\n\n{material.punchline}"
        
        if len(content) > specs["max_length"]:
            content = f"{material.setup} {material.punchline}"
        
        return content
    
    def _format_generic(self, material: ComedyMaterial, specs: Dict) -> str:
        """Format generic comedy material"""
        content = f"{material.setup}\n\n{material.observation}\n\n{material.punchline}"
        
        if len(content) > specs["max_length"]:
            content = content[:specs["max_length"] - 3] + "..."
        
        return content
    
    def _generate_hashtags(self, material: ComedyMaterial, specs: Dict) -> List[str]:
        """Generate hashtags for platform"""
        
        base_hashtags = [
            "#JeanMorphius",
            "#Comedy",
            "#Bilingual"
        ]
        
        style_hashtags = {
            ComedyStyle.PETER_KAY: ["#ObservationalComedy", "#FamilyComedy"],
            ComedyStyle.HASAN_CAN_KAYA: ["#ConversationalComedy", "#TurkishComedy"],
            ComedyStyle.MILTON_JONES: ["#OneLiner", "#Wordplay"],
            ComedyStyle.GARY_DELANEY: ["#DarkHumor", "#OneLiner"],
            ComedyStyle.EDDIE_IZZARD: ["#SurrealComedy", "#StreamOfConsciousness"],
            ComedyStyle.BILL_BAILEY: ["#MusicalComedy", "#IntellectualComedy"],
            ComedyStyle.SEAN_LOCK: ["#Deadpan", "#Absurdism"]
        }
        
        hashtags = base_hashtags + style_hashtags.get(material.style, [])
        hashtags.extend([f"#{tag.replace('_', '')}" for tag in material.tags[:5]])
        
        return hashtags[:specs["hashtags"]]
    
    def generate_comedy_social_schedule(self, posts_per_week: int = 4, weeks: int = 52) -> Dict[str, Any]:
        """Generate comedy social media schedule"""
        
        if not COMEDY_AVAILABLE:
            return {"error": "Comedy system not available"}
        
        schedule = {
            "timestamp": datetime.now().isoformat(),
            "entity": "jean_morphius",
            "posts_per_week": posts_per_week,
            "weeks": weeks,
            "total_posts": posts_per_week * weeks,
            "posts": []
        }
        
        # Generate materials
        total_materials = posts_per_week * weeks
        materials = generate_comedy_collection(total_materials)
        
        # Create posts
        start_date = datetime.now()
        post_index = 0
        
        for week in range(weeks):
            for day in range(posts_per_week):
                if post_index >= len(materials):
                    break
                
                material = materials[post_index]
                scheduled_time = start_date + timedelta(weeks=week, days=day)
                
                # Generate for each platform
                for platform in ["instagram", "twitter", "tiktok"]:
                    formatted = self.format_comedy_for_platform(material, platform)
                    
                    post = {
                        "post_id": f"jean_comedy_{post_index}_{platform}_{week}_{day}",
                        "entity": "jean_morphius",
                        "channel": "creator",
                        "platform": platform,
                        "content": formatted["content"],
                        "content_type": formatted["content_type"],
                        "hashtags": formatted["hashtags"],
                        "scheduled_time": scheduled_time.isoformat(),
                        "metadata": formatted["metadata"]
                    }
                    
                    schedule["posts"].append(post)
                
                post_index += 1
        
        return schedule
    
    def save_schedule(self, schedule: Dict[str, Any], output_dir: Path):
        """Save schedule to file"""
        
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / f"jean_comedy_social_schedule_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(schedule, f, indent=2, ensure_ascii=False)
        
        return output_file


if __name__ == "__main__":
    print("=== JEAN MORPHIUS - COMEDY SOCIAL INTEGRATOR ===")
    print("\nGenerating comedy social media schedule...")
    
    integrator = JeanComedySocialIntegrator()
    schedule = integrator.generate_comedy_social_schedule(posts_per_week=4, weeks=52)
    
    print(f"\nTotal Posts: {schedule['total_posts']}")
    print(f"Posts Generated: {len(schedule['posts'])}")
    
    # Save schedule
    output_dir = Path(__file__).parent.parent / "data" / "jean_comedy"
    output_file = integrator.save_schedule(schedule, output_dir)
    
    print(f"\nSchedule saved to: {output_file}")
    print("\nComedy social integration complete!")
