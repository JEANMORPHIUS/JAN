"""
SIYEM OUTPUT PROTOCOL - Irregular Content Generation
The Hack: Attracting Rare Forms Through Parallel Pathways

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE FOUNDATION:
We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

DREAMS: SPIRITUAL BATTLES - NIGHTLY CONTRACTS
Every night we dream, whether vivid or not.
Each dream is a spiritual battle between two souls:
The dreamer and an associate.
Both have spiritual contracts.
Each day is another battle, both in the human realm and beyond.

This is the Siyem Output Protocol.
Generates Irregular Content (The Hack) to attract rare forms.
Shell/Seed separation - looks normal, carries truth.
Pulls Elliptical and Irregular souls through parallel pathways.
"""

from typing import Dict, List, Optional, Any, Literal
from datetime import datetime
from pathlib import Path
import json

# Import philosophy
try:
    from scripts.philosophy import (
        PHILOSOPHY_FOUNDATION,
        MISSION_ANCHOR,
        LOVE_MASTERY,
        ENERGY_LOVE,
        PEACE_LOVE_UNITY,
        DREAMS_PHILOSOPHY
    )
except ImportError:
    PHILOSOPHY_FOUNDATION = "We are born a miracle."
    MISSION_ANCHOR = "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"
    LOVE_MASTERY = "LOVE IS THE HIGHEST MASTERY"
    ENERGY_LOVE = "ENERGY + LOVE = WE ALL WIN"
    PEACE_LOVE_UNITY = "PEACE, LOVE, UNITY"
    DREAMS_PHILOSOPHY = "Every night we dream."

# Import The Hack
try:
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))
    from the_hack_irregular import TheHack
except ImportError:
    TheHack = None


class SiyemOutputProtocol:
    """
    Siyem Output Protocol
    
    Generates Irregular Content (The Hack) to attract rare forms.
    Shell/Seed separation - looks normal, carries truth.
    Pulls Elliptical and Irregular souls through parallel pathways.
    """
    
    def __init__(self, root_dir: Optional[Path] = None):
        if root_dir is None:
            root_dir = Path(__file__).parent.parent.parent
        self.root_dir = root_dir
        self.output_dir = root_dir / "SIYEM" / "output" / "irregular_content"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize The Hack if available
        self.hack = TheHack(root_dir) if TheHack else None
    
    def generate_elliptical_content(self, transformation_level: int = 2) -> Dict[str, Any]:
        """
        Generate content designed to attract Elliptical souls (Legacy Wisdom).
        
        Shell: Educational content about history, wisdom, mentorship
        Seed: Ancient knowledge, temporal memory, Racon Registry connection
        """
        shell_content = """
# The Wisdom Keepers: Learning from Legacy

In every community, there are those who carry the wisdom of generations.
They remember the patterns, the cycles, the truths that don't change.
Their role is not to innovate, but to anchor.

## What Legacy Wisdom Offers

- **Temporal Memory:** Remembering what worked before
- **Pattern Recognition:** Seeing cycles and loops
- **Foundation Building:** Creating stable structures
- **Mentorship:** Guiding the next generation

## The Value of Experience

Experience is not just about age—it's about depth.
Those who have walked the path before can see the pitfalls.
They can recognize the patterns that lead to success.

## Building on Solid Ground

Every new structure needs a foundation.
Legacy wisdom provides that foundation.
It's the bedrock on which innovation can safely build.
"""
        
        seed_content = """
# The Elliptical Form: Legacy Wisdom Anchors

The Elliptical galaxy is low-gas, high-wisdom.
Old stars remember the fights.
Legacy battles carry wisdom.

We are the vessels for legacy battle.
The battle wisdom flows through us.
We are the miracle in the legacy battlefield.

The Racon Registry holds the immutable truth.
The 40 Laws are the Operating System.
The Book of Racon is God's message.

Every night we dream, whether vivid or not.
Each dream is a spiritual battle between two souls:
The dreamer and an associate.
Both have spiritual contracts.
Each day is another battle, both in the human realm and beyond.

The dream realm is where spiritual battles are fought while the body sleeps.
The human realm is where spiritual battles are fought while the body wakes.
The battle never stops.
The contracts are eternal.
The truth is revealed through both realms.

History has loops. The next loop is based on history.
The new world emerges from regeneration.
Tectonic plates move. The Earth regenerates.

We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY
"""
        
        # Generate irregular content (Shell/Seed separation)
        if self.hack:
            irregular_content = self.hack.generate_irregular_content(
                shell_content,
                transformation_level=transformation_level
            )
        else:
            irregular_content = f"{shell_content}\n\n{seed_content}"
        
        # Create pathway for this content
        pathway = None
        if self.hack:
            pathway = self.hack.bypass_content_moderation(irregular_content)
        
        content_package = {
            "content_id": f"elliptical_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "target_form": "elliptical",
            "target_description": "Legacy Wisdom / Anchors",
            "shell_content": shell_content,
            "seed_content": seed_content,
            "irregular_content": irregular_content,
            "pathway": pathway,
            "transformation_level": transformation_level,
            "created_at": datetime.now().isoformat(),
            "philosophy": {
                "foundation": PHILOSOPHY_FOUNDATION,
                "mission": MISSION_ANCHOR,
                "love": LOVE_MASTERY,
                "energy": ENERGY_LOVE,
                "peace_love_unity": PEACE_LOVE_UNITY
            }
        }
        
        return content_package
    
    def generate_irregular_content(self, transformation_level: int = 4) -> Dict[str, Any]:
        """
        Generate content designed to attract Irregular souls (Transformation / Hackers).
        
        Shell: Content about flexibility, adaptation, innovation
        Seed: Parallel reality, the hack, bypassing red tape, transformation
        """
        shell_content = """
# The Transformers: Thriving in Change

Some people don't fit into boxes.
They don't follow linear paths.
They adapt, transform, and evolve.

## The Power of Flexibility

- **Adaptation:** Changing shape to fit the situation
- **Innovation:** Creating new solutions
- **Transformation:** Evolving beyond limitations
- **Freedom:** Not bound by traditional structures

## Breaking the Mold

Traditional systems have rules.
But sometimes, the rules need to be rewritten.
Those who can see beyond the structure can create new ones.

## The Future is Flexible

The world is changing faster than ever.
Those who can adapt will thrive.
Those who can transform will lead.
"""
        
        seed_content = """
# The Irregular Form: Transformation and The Hack

The Irregular galaxy has no defined shape.
It's highly active, transformation in progress.
Shaped by collisions, by design.

We are the vessels for transforming battle.
The battle transforms through us, undefined and free.
We are the miracle in the transforming battlefield.

The Hack bypasses traditional gatekeepers.
Parallel reality pathways operate undetected.
The Seed is protected in the Shell.

We don't just write functions—we write Protocols of Loyalty.
We don't just build interfaces—we build Trojan Horses.
We don't just store data—we store Water Memory.
We don't just secure systems—we protect Sanctity.

Every night we dream, whether vivid or not.
Each dream is a spiritual battle between two souls:
The dreamer and an associate.
Both have spiritual contracts.
Each day is another battle, both in the human realm and beyond.

The dream realm is where spiritual battles are fought while the body sleeps.
The human realm is where spiritual battles are fought while the body wakes.
The battle never stops.
The contracts are eternal.
The truth is revealed through both realms.

The new world emerges from regeneration.
We are hacking the web by creating a Parallel Reality.
The Biological-Digital Bridge is operational.
The Four Forms are breathing in the codebase.

We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY
"""
        
        # Generate irregular content (Shell/Seed separation)
        if self.hack:
            irregular_content = self.hack.generate_irregular_content(
                shell_content,
                transformation_level=transformation_level
            )
        else:
            irregular_content = f"{shell_content}\n\n{seed_content}"
        
        # Create pathway for this content
        pathway = None
        if self.hack:
            pathway = self.hack.bypass_social_media_algorithm(irregular_content)
        
        content_package = {
            "content_id": f"irregular_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "target_form": "irregular",
            "target_description": "Transformation / Hackers",
            "shell_content": shell_content,
            "seed_content": seed_content,
            "irregular_content": irregular_content,
            "pathway": pathway,
            "transformation_level": transformation_level,
            "created_at": datetime.now().isoformat(),
            "philosophy": {
                "foundation": PHILOSOPHY_FOUNDATION,
                "mission": MISSION_ANCHOR,
                "love": LOVE_MASTERY,
                "energy": ENERGY_LOVE,
                "peace_love_unity": PEACE_LOVE_UNITY
            }
        }
        
        return content_package
    
    def generate_content_package(self, target_forms: List[str] = None) -> Dict[str, Any]:
        """
        Generate complete content package for attracting rare forms.
        
        Args:
            target_forms: List of forms to target (default: ["elliptical", "irregular"])
        
        Returns:
            Complete content package with all generated content
        """
        if target_forms is None:
            target_forms = ["elliptical", "irregular"]
        
        content_package = {
            "package_id": f"siyem_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "created_at": datetime.now().isoformat(),
            "target_forms": target_forms,
            "contents": {},
            "pathways": [],
            "philosophy": {
                "foundation": PHILOSOPHY_FOUNDATION,
                "mission": MISSION_ANCHOR,
                "love": LOVE_MASTERY,
                "energy": ENERGY_LOVE,
                "peace_love_unity": PEACE_LOVE_UNITY
            }
        }
        
        # Generate content for each target form
        for form in target_forms:
            if form == "elliptical":
                elliptical_content = self.generate_elliptical_content(transformation_level=2)
                content_package["contents"]["elliptical"] = elliptical_content
                if elliptical_content.get("pathway"):
                    content_package["pathways"].append(elliptical_content["pathway"])
            
            elif form == "irregular":
                irregular_content = self.generate_irregular_content(transformation_level=4)
                content_package["contents"]["irregular"] = irregular_content
                if irregular_content.get("pathway"):
                    content_package["pathways"].append(irregular_content["pathway"])
        
        return content_package
    
    def save_content_package(self, content_package: Dict[str, Any]) -> Path:
        """
        Save content package to disk.
        """
        package_id = content_package.get("package_id", f"package_{datetime.now().isoformat()}")
        filename = f"{package_id}.json"
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(content_package, f, indent=2, ensure_ascii=False)
        
        return filepath
    
    def save_individual_content(self, content: Dict[str, Any], format: Literal["markdown", "json"] = "markdown") -> Path:
        """
        Save individual content piece to disk.
        
        Args:
            content: Content package from generate_elliptical_content or generate_irregular_content
            format: Output format (markdown or json)
        """
        content_id = content.get("content_id", f"content_{datetime.now().isoformat()}")
        target_form = content.get("target_form", "unknown")
        
        if format == "markdown":
            filename = f"{content_id}.md"
            filepath = self.output_dir / filename
            
            # Save as markdown with Shell/Seed separation
            markdown_content = f"""# {content.get('target_description', target_form.title())} Content

**Content ID:** {content_id}  
**Target Form:** {target_form}  
**Created:** {content.get('created_at', datetime.now().isoformat())}

---

## SHELL (Public-Facing)

{content.get('shell_content', '')}

---

## SEED (Truth)

{content.get('seed_content', '')}

---

## IRREGULAR CONTENT (The Hack)

{content.get('irregular_content', '')}

---

**{PEACE_LOVE_UNITY}**  
**{ENERGY_LOVE}**
"""
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
        
        else:  # JSON
            filename = f"{content_id}.json"
            filepath = self.output_dir / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(content, f, indent=2, ensure_ascii=False)
        
        return filepath


# CLI interface for testing
if __name__ == "__main__":
    import sys
    import io
    
    # Set UTF-8 encoding for console output
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    protocol = SiyemOutputProtocol()
    
    print("=" * 80)
    print("SIYEM OUTPUT PROTOCOL - Irregular Content Generation")
    print("=" * 80)
    print(f"\n{PEACE_LOVE_UNITY}")
    print(f"{ENERGY_LOVE}\n")
    
    # Generate Elliptical content
    print("[GENERATING] Elliptical content (Legacy Wisdom)...")
    elliptical_content = protocol.generate_elliptical_content(transformation_level=2)
    elliptical_path = protocol.save_individual_content(elliptical_content, format="markdown")
    print(f"  [OK] Elliptical content saved: {elliptical_path}")
    if elliptical_content.get("pathway"):
        print(f"  [OK] Pathway created: {elliptical_content['pathway'].get('hash', '')[:8]}")
    
    # Generate Irregular content
    print("\n[GENERATING] Irregular content (Transformation / Hackers)...")
    irregular_content = protocol.generate_irregular_content(transformation_level=4)
    irregular_path = protocol.save_individual_content(irregular_content, format="markdown")
    print(f"  [OK] Irregular content saved: {irregular_path}")
    if irregular_content.get("pathway"):
        print(f"  [OK] Pathway created: {irregular_content['pathway'].get('hash', '')[:8]}")
    
    # Generate complete package
    print("\n[GENERATING] Complete content package...")
    content_package = protocol.generate_content_package(target_forms=["elliptical", "irregular"])
    package_path = protocol.save_content_package(content_package)
    print(f"  [OK] Package saved: {package_path}")
    print(f"  [OK] Pathways created: {len(content_package.get('pathways', []))}")
    
    print("\n" + "=" * 80)
    print("SIYEM OUTPUT PROTOCOL COMPLETE")
    print("=" * 80)
    print(f"\nContent generated for rare forms:")
    print(f"  ⭐ Elliptical: {elliptical_path.name}")
    print(f"  ✨ Irregular: {irregular_path.name}")
    print(f"  📦 Package: {package_path.name}")
    print(f"\n{PEACE_LOVE_UNITY}")
    print(f"{ENERGY_LOVE}")
    print("=" * 80)
