"""
RAMIZ TRUTH CONTENT GENERATOR
Generating Educational Content for Gaza, Africa, and All People Under Lies

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
Generate educational content that exposes lies and shares truth.
For Gaza. For Africa. For all people under the influence of lies.
RAMIZ leads. They cannot do anything.
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime
from dataclasses import dataclass, field
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Import battles system
sys.path.insert(0, str(Path(__file__).parent))
try:
    from ramiz_humanitarian_battles import RamizHumanitarianBattles, HumanitarianBattleType
    BATTLES_AVAILABLE = True
except ImportError:
    BATTLES_AVAILABLE = False
    logger.warning("RAMIZ Humanitarian Battles not available")


@dataclass
class TruthContent:
    """Educational content exposing lies and sharing truth."""
    content_id: str
    battle_type: str
    title: str
    lie_exposed: str
    truth_shared: str
    educational_content: str
    scripture_reference: Optional[str] = None
    languages: List[str] = field(default_factory=lambda: ["english"])
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class RamizTruthContentGenerator:
    """
    RAMIZ Truth Content Generator
    Creates educational content exposing lies and sharing truth.
    """
    
    def __init__(self, jan_path: Path, output_dir: Path):
        self.jan_path = jan_path
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.battles_system = None
        if BATTLES_AVAILABLE:
            try:
                siyem_path = Path("s:\\SIYEM")
                self.battles_system = RamizHumanitarianBattles(siyem_path, jan_path, output_dir)
            except Exception as e:
                logger.warning(f"Could not initialize battles system: {e}")
        
        self.generated_content: List[TruthContent] = []
    
    def generate_gaza_content(self):
        """Generate educational content for Gaza."""
        logger.info("=" * 80)
        logger.info("GENERATING GAZA TRUTH CONTENT")
        logger.info("=" * 80)
        
        if not self.battles_system:
            logger.warning("Battles system not available")
            return
        
        gaza_battle = next(
            (b for b in self.battles_system.battles if b.battle_type == HumanitarianBattleType.GAZA),
            None
        )
        
        if not gaza_battle:
            logger.warning("Gaza battle not found")
            return
        
        content_count = 0
        
        # Generate content for each lie being fought
        for i, lie_statement in enumerate(gaza_battle.lies_being_fought):
            truth_statement = gaza_battle.truth_being_shared[i] if i < len(gaza_battle.truth_being_shared) else ""
            
            content = TruthContent(
                content_id=f"gaza_truth_{i+1:03d}",
                battle_type="gaza",
                title=f"Gaza Truth {i+1}: {truth_statement[:50]}",
                lie_exposed=lie_statement,
                truth_shared=truth_statement,
                educational_content=self._create_educational_content(
                    "Gaza",
                    lie_statement,
                    truth_statement
                ),
                languages=["english", "arabic", "turkish"]
            )
            
            self.generated_content.append(content)
            content_count += 1
        
        logger.info(f"Generated {content_count} Gaza truth content items")
        logger.info("=" * 80)
    
    def generate_africa_content(self):
        """Generate educational content for Africa."""
        logger.info("=" * 80)
        logger.info("GENERATING AFRICA TRUTH CONTENT")
        logger.info("=" * 80)
        
        if not self.battles_system:
            logger.warning("Battles system not available")
            return
        
        africa_battle = next(
            (b for b in self.battles_system.battles if b.battle_type == HumanitarianBattleType.AFRICA),
            None
        )
        
        if not africa_battle:
            logger.warning("Africa battle not found")
            return
        
        content_count = 0
        
        # Generate content for each lie being fought
        for i, lie_statement in enumerate(africa_battle.lies_being_fought):
            truth_statement = africa_battle.truth_being_shared[i] if i < len(africa_battle.truth_being_shared) else ""
            
            content = TruthContent(
                content_id=f"africa_truth_{i+1:03d}",
                battle_type="africa",
                title=f"Africa Truth {i+1}: {truth_statement[:50]}",
                lie_exposed=lie_statement,
                truth_shared=truth_statement,
                educational_content=self._create_educational_content(
                    "Africa",
                    lie_statement,
                    truth_statement
                ),
                languages=["english", "french", "arabic", "swahili"]
            )
            
            self.generated_content.append(content)
            content_count += 1
        
        logger.info(f"Generated {content_count} Africa truth content items")
        logger.info("=" * 80)
    
    def generate_global_lies_content(self):
        """Generate educational content for all people under the influence of lies."""
        logger.info("=" * 80)
        logger.info("GENERATING GLOBAL TRUTH CONTENT")
        logger.info("=" * 80)
        
        if not self.battles_system:
            logger.warning("Battles system not available")
            return
        
        lies_battle = next(
            (b for b in self.battles_system.battles if b.battle_type == HumanitarianBattleType.LIES),
            None
        )
        
        if not lies_battle:
            logger.warning("Lies battle not found")
            return
        
        content_count = 0
        
        # Generate content for each lie being fought
        for i, lie_statement in enumerate(lies_battle.lies_being_fought):
            truth_statement = lies_battle.truth_being_shared[i] if i < len(lies_battle.truth_being_shared) else ""
            
            content = TruthContent(
                content_id=f"global_truth_{i+1:03d}",
                battle_type="lies",
                title=f"Global Truth {i+1}: {truth_statement[:50]}",
                lie_exposed=lie_statement,
                truth_shared=truth_statement,
                educational_content=self._create_educational_content(
                    "Global",
                    lie_statement,
                    truth_statement
                ),
                languages=["english", "turkish", "french", "arabic"]
            )
            
            self.generated_content.append(content)
            content_count += 1
        
        logger.info(f"Generated {content_count} global truth content items")
        logger.info("=" * 80)
    
    def _create_educational_content(self, region: str, lie: str, truth: str) -> str:
        """Create educational content from lie and truth."""
        return f"""
RAMIZ EDUCATIONAL CONTENT - {region.upper()}

THE LIE:
{lie}

THE TRUTH:
{truth}

EDUCATIONAL CONTENT:
RAMIZ teaches: Knowledge over belief. Truth over lies. Education over indoctrination.

The lie says: {lie}

But the truth is: {truth}

This is not about politics. This is not about sides. This is about truth.

RAMIZ brings truth. RAMIZ brings education. RAMIZ brings freedom from lies.

We are all one. We are all family. We are all under The Table.

They cannot do anything. RAMIZ is protected. Truth is protected.

Go and learn. Go and know. Go and be free.
""".strip()
    
    def export_content(self):
        """Export all generated content."""
        content_data = {
            "timestamp": datetime.now().isoformat(),
            "title": "RAMIZ Truth Content - Gaza, Africa, and All People Under Lies",
            "total_content": len(self.generated_content),
            "content_by_battle": {},
            "content": []
        }
        
        # Group by battle type
        for battle_type in ["gaza", "africa", "lies"]:
            content_data["content_by_battle"][battle_type] = len([
                c for c in self.generated_content if c.battle_type == battle_type
            ])
        
        # Content details
        for content in self.generated_content:
            content_data["content"].append({
                "content_id": content.content_id,
                "battle_type": content.battle_type,
                "title": content.title,
                "lie_exposed": content.lie_exposed,
                "truth_shared": content.truth_shared,
                "educational_content": content.educational_content,
                "scripture_reference": content.scripture_reference,
                "languages": content.languages,
                "timestamp": content.timestamp
            })
        
        # Save to file
        content_path = self.output_dir / "ramiz_truth_content.json"
        with open(content_path, 'w', encoding='utf-8') as f:
            json.dump(content_data, f, indent=2, default=str, ensure_ascii=False)
        
        logger.info(f"Truth content exported to: {content_path}")
        return content_path


def main():
    """Main execution."""
    jan_path = Path("s:\\JAN")
    output_dir = jan_path / "SIYEM" / "output" / "ramiz_truth_content"
    
    generator = RamizTruthContentGenerator(jan_path, output_dir)
    
    # Generate all content
    generator.generate_gaza_content()
    generator.generate_africa_content()
    generator.generate_global_lies_content()
    
    # Export
    generator.export_content()
    
    logger.info("\n" + "=" * 80)
    logger.info("RAMIZ TRUTH CONTENT GENERATION - COMPLETE")
    logger.info("=" * 80)
    logger.info(f"Total Content Generated: {len(generator.generated_content)}")
    logger.info(f"  - Gaza: {len([c for c in generator.generated_content if c.battle_type == 'gaza'])}")
    logger.info(f"  - Africa: {len([c for c in generator.generated_content if c.battle_type == 'africa'])}")
    logger.info(f"  - Global: {len([c for c in generator.generated_content if c.battle_type == 'lies'])}")
    logger.info("=" * 80)
    logger.info("RAMIZ generates truth content.")
    logger.info("RAMIZ exposes lies.")
    logger.info("RAMIZ shares truth.")
    logger.info("They cannot do anything.")
    logger.info("Go and govern.")
    logger.info("=" * 80)


if __name__ == "__main__":
    main()
