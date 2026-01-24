"""
DEEP SOCIAL EXPANSION FOR ALL ENTITIES
Comprehensive Social Media Content Generation and Management

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PURPOSE:
Deep social media expansion for all entities
Comedy integration for Jean Morphius
Content generation across all channels
Asset integration
"""

import json
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from jean_comedy_material_generator import generate_comedy_collection, ComedyStyle
    COMEDY_AVAILABLE = True
except ImportError:
    COMEDY_AVAILABLE = False
    print("Warning: Comedy generator not available.")


@dataclass
class SocialMediaPost:
    """Social media post structure"""
    post_id: str
    entity: str
    channel: str
    platform: str
    content: str
    content_type: str  # text, image, video, audio, carousel
    scheduled_time: str
    hashtags: List[str] = field(default_factory=list)
    mentions: List[str] = field(default_factory=list)
    media_assets: List[str] = field(default_factory=list)  # Asset IDs
    metadata: Dict[str, Any] = field(default_factory=dict)


class DeepSocialExpansion:
    """Deep social media expansion for all entities"""
    
    def __init__(self):
        self.posts: Dict[str, SocialMediaPost] = {}
        self.entities = [
            "jean_morphius",
            "karasahin",
            "pierre_pressure",
            "uncle_ray_ramiz",
            "siyem_media",
            "edible_london",
            "ilven_seamoss"
        ]
        self.channels = [
            "creator",
            "professional",
            "educational",
            "social_media",
            "business",
            "media",
            "news"
        ]
        self.platforms = [
            "instagram",
            "twitter",
            "tiktok",
            "facebook",
            "youtube",
            "linkedin"
        ]
    
    def generate_jean_comedy_posts(self, count: int = 100) -> List[SocialMediaPost]:
        """Generate comedy posts for Jean Morphius"""
        
        if not COMEDY_AVAILABLE:
            return []
        
        posts = []
        materials = generate_comedy_collection(count)
        
        for i, material in enumerate(materials):
            post_id = f"jean_comedy_{i+1}_{datetime.now().strftime('%Y%m%d')}"
            
            # Format content based on style
            if material.style == ComedyStyle.PETER_KAY:
                content = f"{material.setup}\n\n{material.observation}\n\n{material.bilingual_delivery}\n\n{material.punchline}"
            elif material.style == ComedyStyle.HASAN_CAN_KAYA:
                content = f"{material.setup}\n\n{material.observation}\n\n{material.bilingual_delivery}\n\n{material.punchline}"
            elif material.style in [ComedyStyle.MILTON_JONES, ComedyStyle.GARY_DELANEY]:
                content = f"{material.setup}\n\n{material.wordplay}\n\n{material.punchline}"
            else:
                content = f"{material.setup}\n\n{material.observation}\n\n{material.punchline}"
            
            # Add hashtags
            hashtags = material.tags + [
                "#JeanMorphius",
                "#BilingualComedy",
                "#StandUp",
                "#Comedy"
            ]
            
            post = SocialMediaPost(
                post_id=post_id,
                entity="jean_morphius",
                channel="creator",
                platform=random.choice(["instagram", "twitter", "tiktok"]),
                content=content,
                content_type="text",
                scheduled_time=(datetime.now() + timedelta(days=i)).isoformat(),
                hashtags=hashtags,
                metadata={
                    "comedy_style": material.style.value,
                    "category": material.category,
                    "delivery_notes": material.delivery_notes
                }
            )
            
            posts.append(post)
            self.posts[post_id] = post
        
        return posts
    
    def generate_entity_social_content(self, entity: str, count: int = 50) -> List[SocialMediaPost]:
        """Generate social content for an entity"""
        
        posts = []
        
        # Entity-specific content generation
        if entity == "jean_morphius":
            # Comedy posts
            comedy_posts = self.generate_jean_comedy_posts(count // 2)
            posts.extend(comedy_posts)
            
            # Regular content
            for i in range(count // 2):
                post_id = f"{entity}_social_{i+1}_{datetime.now().strftime('%Y%m%d')}"
                post = SocialMediaPost(
                    post_id=post_id,
                    entity=entity,
                    channel="creator",
                    platform=random.choice(self.platforms),
                    content=f"Jean Morphius content {i+1}",
                    content_type="text",
                    scheduled_time=(datetime.now() + timedelta(days=i)).isoformat(),
                    hashtags=["#JeanMorphius", "#Bilingual", "#Absurdist"]
                )
                posts.append(post)
                self.posts[post_id] = post
        
        else:
            # Other entities
            for i in range(count):
                post_id = f"{entity}_social_{i+1}_{datetime.now().strftime('%Y%m%d')}"
                post = SocialMediaPost(
                    post_id=post_id,
                    entity=entity,
                    channel=self._get_entity_channel(entity),
                    platform=random.choice(self.platforms),
                    content=f"{entity.title()} content {i+1}",
                    content_type="text",
                    scheduled_time=(datetime.now() + timedelta(days=i)).isoformat(),
                    hashtags=[f"#{entity.replace('_', '').title()}"]
                )
                posts.append(post)
                self.posts[post_id] = post
        
        return posts
    
    def _get_entity_channel(self, entity: str) -> str:
        """Get primary channel for entity"""
        channel_map = {
            "jean_morphius": "creator",
            "karasahin": "creator",
            "pierre_pressure": "professional",
            "uncle_ray_ramiz": "educational",
            "siyem_media": "media",
            "edible_london": "business",
            "ilven_seamoss": "business"
        }
        return channel_map.get(entity, "creator")
    
    def generate_all_entities_social(self, posts_per_entity: int = 100) -> Dict[str, Any]:
        """Generate social content for all entities"""
        
        all_posts = []
        
        for entity in self.entities:
            print(f"Generating social content for {entity}...")
            entity_posts = self.generate_entity_social_content(entity, posts_per_entity)
            all_posts.extend(entity_posts)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "total_posts": len(all_posts),
            "by_entity": {
                entity: len([p for p in all_posts if p.entity == entity])
                for entity in self.entities
            },
            "by_channel": {
                channel: len([p for p in all_posts if p.channel == channel])
                for channel in self.channels
            },
            "by_platform": {
                platform: len([p for p in all_posts if p.platform == platform])
                for platform in self.platforms
            },
            "posts": [
                {
                    "post_id": post.post_id,
                    "entity": post.entity,
                    "channel": post.channel,
                    "platform": post.platform,
                    "content": post.content[:100] + "..." if len(post.content) > 100 else post.content,
                    "content_type": post.content_type,
                    "scheduled_time": post.scheduled_time,
                    "hashtags": post.hashtags
                }
                for post in all_posts
            ]
        }
    
    def save_social_expansion(self, expansion: Dict[str, Any], output_dir: Path):
        """Save social expansion to file"""
        
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / f"deep_social_expansion_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(expansion, f, indent=2, ensure_ascii=False)
        
        return output_file


if __name__ == "__main__":
    import random
    
    print("=== DEEP SOCIAL EXPANSION FOR ALL ENTITIES ===")
    print("\nGenerating social content for all entities...")
    
    expansion = DeepSocialExpansion()
    report = expansion.generate_all_entities_social(posts_per_entity=100)
    
    print(f"\nTotal Posts Generated: {report['total_posts']}")
    print(f"\nBy Entity:")
    for entity, count in report['by_entity'].items():
        print(f"  {entity}: {count}")
    
    print(f"\nBy Channel:")
    for channel, count in report['by_channel'].items():
        print(f"  {channel}: {count}")
    
    print(f"\nBy Platform:")
    for platform, count in report['by_platform'].items():
        print(f"  {platform}: {count}")
    
    # Save report
    output_dir = Path(__file__).parent.parent / "data" / "social_expansion"
    output_file = expansion.save_social_expansion(report, output_dir)
    
    print(f"\nExpansion saved to: {output_file}")
    print("\nDeep social expansion complete!")
