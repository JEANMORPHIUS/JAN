"""ALL ENTITIES - DEEP SOCIAL EXPANSION
Comprehensive Social Media Content for All Entities

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PURPOSE:
Deep social media expansion for ALL entities
Comedy integration for Jean
Content generation across all channels
Asset integration
Don't stop until we drop

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
    from jean_comedy_social_integrator import JeanComedySocialIntegrator
    COMEDY_INTEGRATOR_AVAILABLE = True
except ImportError:
    COMEDY_INTEGRATOR_AVAILABLE = False


class AllEntitiesSocialDeepExpansion:
    """Deep social expansion for all entities"""
    
    def __init__(self):
        self.entities = {
            "jean_morphius": {
                "channels": ["creator", "social_media"],
                "platforms": ["instagram", "twitter", "tiktok", "facebook"],
                "posts_per_week": 4,
                "special": "comedy_integration"
            },
            "karasahin": {
                "channels": ["creator", "social_media"],
                "platforms": ["instagram", "twitter", "youtube"],
                "posts_per_week": 3,
                "special": "music_focus"
            },
            "pierre_pressure": {
                "channels": ["professional", "social_media"],
                "platforms": ["instagram", "twitter", "tiktok", "linkedin"],
                "posts_per_week": 3,
                "special": "motivational"
            },
            "uncle_ray_ramiz": {
                "channels": ["educational", "social_media"],
                "platforms": ["facebook", "instagram", "youtube"],
                "posts_per_week": 2,
                "special": "wisdom_teaching"
            },
            "siyem_media": {
                "channels": ["media", "social_media"],
                "platforms": ["instagram", "twitter", "linkedin"],
                "posts_per_week": 2,
                "special": "systems_level"
            },
            "edible_london": {
                "channels": ["business", "social_media"],
                "platforms": ["instagram", "facebook", "twitter"],
                "posts_per_week": 2,
                "special": "food_production"
            },
            "ilven_seamoss": {
                "channels": ["business", "social_media"],
                "platforms": ["instagram", "facebook", "tiktok"],
                "posts_per_week": 2,
                "special": "product_focus"
            }
        }
        
        self.channels = [
            "creator",
            "professional",
            "educational",
            "social_media",
            "business",
            "media",
            "news"
        ]
    
    def generate_entity_deep_social(self, entity: str, weeks: int = 52) -> Dict[str, Any]:
        """Generate deep social content for an entity"""
        
        entity_config = self.entities.get(entity, {})
        posts_per_week = entity_config.get("posts_per_week", 2)
        platforms = entity_config.get("platforms", ["instagram"])
        channels = entity_config.get("channels", ["social_media"])
        special = entity_config.get("special", "")
        
        posts = []
        start_date = datetime.now()
        
        # Special handling for Jean Morphius (comedy)
        if entity == "jean_morphius" and COMEDY_INTEGRATOR_AVAILABLE:
            integrator = JeanComedySocialIntegrator()
            comedy_schedule = integrator.generate_comedy_social_schedule(posts_per_week, weeks)
            posts.extend(comedy_schedule.get("posts", []))
        
        # Generate regular content
        total_posts = posts_per_week * weeks
        for i in range(total_posts):
            week = i // posts_per_week
            day_in_week = i % posts_per_week
            scheduled_time = start_date + timedelta(weeks=week, days=day_in_week)
            
            for platform in platforms:
                for channel in channels:
                    post_id = f"{entity}_{channel}_{platform}_{i}_{datetime.now().strftime('%Y%m%d')}"
                    
                    # Generate content based on entity
                    content = self._generate_entity_content(entity, channel, platform, special)
                    
                    post = {
                        "post_id": post_id,
                        "entity": entity,
                        "channel": channel,
                        "platform": platform,
                        "content": content,
                        "content_type": self._get_content_type(entity, platform),
                        "scheduled_time": scheduled_time.isoformat(),
                        "hashtags": self._generate_hashtags(entity, channel),
                        "metadata": {
                            "special": special,
                            "week": week + 1,
                            "day": day_in_week + 1
                        }
                    }
                    
                    posts.append(post)
        
        return {
            "entity": entity,
            "total_posts": len(posts),
            "posts_per_week": posts_per_week,
            "weeks": weeks,
            "platforms": platforms,
            "channels": channels,
            "posts": posts
        }
    
    def _generate_entity_content(self, entity: str, channel: str, platform: str, special: str) -> str:
        """Generate content for entity"""
        
        templates = {
            "jean_morphius": "Ma mère, elle... she does this thing where... [comedy content]",
            "karasahin": "Duygu her şeydir. Emotion is everything. [music/emotion content]",
            "pierre_pressure": "Discipline. Focus. Action. [motivational content]",
            "uncle_ray_ramiz": "Yeğen, dinle. Listen, child. [wisdom content]",
            "siyem_media": "Systems-level thinking. [infrastructure content]",
            "edible_london": "Made by heart. Amplified by AI. [food production content]",
            "ilven_seamoss": "Hand-prepared. Heart-first. [sea moss content]"
        }
        
        base_content = templates.get(entity, f"{entity.title()} content")
        
        # Platform-specific formatting
        if platform == "twitter":
            if len(base_content) > 280:
                base_content = base_content[:277] + "..."
        elif platform == "instagram":
            if len(base_content) > 2200:
                base_content = base_content[:2197] + "..."
        
        return base_content
    
    def _get_content_type(self, entity: str, platform: str) -> str:
        """Get content type for entity/platform"""
        
        if platform == "tiktok" or platform == "youtube":
            return "video"
        elif entity in ["edible_london", "ilven_seamoss"]:
            return "image"
        else:
            return "text"
    
    def _generate_hashtags(self, entity: str, channel: str) -> List[str]:
        """Generate hashtags for entity/channel"""
        
        base_hashtags = {
            "jean_morphius": ["#JeanMorphius", "#Bilingual", "#Comedy", "#Absurdist"],
            "karasahin": ["#Karasahin", "#DuyguAdami", "#EmotionMan", "#Music"],
            "pierre_pressure": ["#PierrePressure", "#Discipline", "#Motivation", "#Fighter"],
            "uncle_ray_ramiz": ["#UncleRayRamiz", "#Wisdom", "#Teaching", "#Spiritual"],
            "siyem_media": ["#SiyemMedia", "#Systems", "#Infrastructure"],
            "edible_london": ["#EdibleLondon", "#FoodProduction", "#Community"],
            "ilven_seamoss": ["#IlvenSeamoss", "#SeaMoss", "#NaturalHealth"]
        }
        
        channel_hashtags = {
            "creator": ["#Creator", "#Creative"],
            "professional": ["#Professional", "#Business"],
            "educational": ["#Education", "#Teaching"],
            "social_media": ["#SocialMedia"],
            "business": ["#Business", "#Entrepreneurship"],
            "media": ["#Media", "#Content"],
            "news": ["#News", "#Updates"]
        }
        
        hashtags = base_hashtags.get(entity, []) + channel_hashtags.get(channel, [])
        return hashtags[:10]  # Limit to 10
    
    def generate_all_entities_deep_social(self, weeks: int = 52) -> Dict[str, Any]:
        """Generate deep social content for all entities"""
        
        all_expansions = {}
        total_posts = 0
        
        for entity in self.entities.keys():
            print(f"Generating deep social for {entity}...")
            expansion = self.generate_entity_deep_social(entity, weeks)
            all_expansions[entity] = expansion
            total_posts += expansion["total_posts"]
        
        return {
            "timestamp": datetime.now().isoformat(),
            "total_entities": len(self.entities),
            "total_posts": total_posts,
            "weeks": weeks,
            "expansions": all_expansions,
            "summary": {
                "by_entity": {
                    entity: exp["total_posts"]
                    for entity, exp in all_expansions.items()
                },
                "by_channel": self._summarize_by_channel(all_expansions),
                "by_platform": self._summarize_by_platform(all_expansions)
            }
        }
    
    def _summarize_by_channel(self, expansions: Dict[str, Dict]) -> Dict[str, int]:
        """Summarize posts by channel"""
        channel_counts = {}
        for entity_exp in expansions.values():
            for post in entity_exp.get("posts", []):
                channel = post.get("channel", "unknown")
                channel_counts[channel] = channel_counts.get(channel, 0) + 1
        return channel_counts
    
    def _summarize_by_platform(self, expansions: Dict[str, Dict]) -> Dict[str, int]:
        """Summarize posts by platform"""
        platform_counts = {}
        for entity_exp in expansions.values():
            for post in entity_exp.get("posts", []):
                platform = post.get("platform", "unknown")
                platform_counts[platform] = platform_counts.get(platform, 0) + 1
        return platform_counts
    
    def save_deep_expansion(self, expansion: Dict[str, Any], output_dir: Path):
        """Save deep expansion to file"""
        
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / f"all_entities_deep_social_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(expansion, f, indent=2, ensure_ascii=False)
        
        return output_file


if __name__ == "__main__":
    print("=== ALL ENTITIES - DEEP SOCIAL EXPANSION ===")
    print("\nGenerating deep social content for all entities...")
    print("Don't stop until we drop...\n")
    
    expansion = AllEntitiesSocialDeepExpansion()
    report = expansion.generate_all_entities_deep_social(weeks=52)
    
    print(f"\nTotal Posts Generated: {report['total_posts']}")
    print(f"\nBy Entity:")
    for entity, count in report['summary']['by_entity'].items():
        print(f"  {entity}: {count}")
    
    print(f"\nBy Channel:")
    for channel, count in report['summary']['by_channel'].items():
        print(f"  {channel}: {count}")
    
    print(f"\nBy Platform:")
    for platform, count in report['summary']['by_platform'].items():
        print(f"  {platform}: {count}")
    
    # Save report
    output_dir = Path(__file__).parent.parent / "data" / "social_expansion"
    output_file = expansion.save_deep_expansion(report, output_dir)
    
    print(f"\nDeep expansion saved to: {output_file}")
    print("\nDeep social expansion complete. We didn't stop. We built until we couldn't.")
