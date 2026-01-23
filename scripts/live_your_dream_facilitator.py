"""
LIVE YOUR DREAM FACILITATOR
Enable and facilitate dreams. The nightmare is over.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE FOUNDATION:
"Let's enable and facilitate....live your dream,,,,the nightmare is over"

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY
"""

import sys
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any
import json

sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    setup_logging, standard_main, load_json, save_json
)

logger = setup_logging(__name__)

@dataclass
class Dream:
    """A dream to be facilitated"""
    dream_id: str
    title: str
    description: str
    category: str  # personal, professional, spiritual, creative, health, relationship, etc.
    priority: int = 5  # 1-10
    status: str = "active"  # active, in_progress, completed, archived
    barriers: List[str] = field(default_factory=list)
    facilitators: List[str] = field(default_factory=list)  # What enables this dream
    milestones: List[Dict[str, Any]] = field(default_factory=list)
    resources_needed: List[str] = field(default_factory=list)
    resources_available: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())
    completed_at: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class NightmareRelease:
    """Release from the nightmare"""
    release_id: str
    nightmare_description: str
    release_statement: str
    released_at: str = field(default_factory=lambda: datetime.now().isoformat())
    transformation_notes: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)

class LiveYourDreamFacilitator:
    """Facilitate and enable dreams. The nightmare is over."""
    
    def __init__(self, user_id: str = "jan", data_dir: Path = None):
        self.user_id = user_id
        self.data_dir = data_dir or Path(__file__).parent.parent / "data" / "dream_facilitation"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        self.dreams_file = self.data_dir / f"{user_id}_dreams.json"
        self.nightmares_file = self.data_dir / f"{user_id}_nightmares_released.json"
        
        self.dreams: List[Dream] = []
        self.nightmares_released: List[NightmareRelease] = []
        
        self._load_data()
    
    def _load_data(self):
        """Load existing dreams and nightmare releases"""
        if self.dreams_file.exists():
            try:
                data = load_json(self.dreams_file)
                self.dreams = [Dream(**dream) for dream in data.get("dreams", [])]
            except Exception as e:
                logger.warning(f"Error loading dreams: {e}")
                self.dreams = []
        else:
            self.dreams = []
        
        if self.nightmares_file.exists():
            try:
                data = load_json(self.nightmares_file)
                self.nightmares_released = [NightmareRelease(**nightmare) for nightmare in data.get("nightmares", [])]
            except Exception as e:
                logger.warning(f"Error loading nightmares: {e}")
                self.nightmares_released = []
        else:
            self.nightmares_released = []
    
    def _save_data(self):
        """Save dreams and nightmare releases"""
        try:
            import json
            with open(self.dreams_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "dreams": [asdict(dream) for dream in self.dreams],
                    "last_updated": datetime.now().isoformat()
                }, f, indent=2, ensure_ascii=False)
            
            with open(self.nightmares_file, 'w', encoding='utf-8') as f:
                json.dump({
                    "nightmares": [asdict(nightmare) for nightmare in self.nightmares_released],
                    "last_updated": datetime.now().isoformat()
                }, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving data: {e}")
    
    def declare_nightmare_over(self, nightmare_description: str, release_statement: str = "", transformation_notes: str = ""):
        """Declare a nightmare is over and release it"""
        release = NightmareRelease(
            release_id=f"release_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            nightmare_description=nightmare_description,
            release_statement=release_statement or "The nightmare is over. I am free.",
            transformation_notes=transformation_notes
        )
        
        self.nightmares_released.append(release)
        self._save_data()
        
        logger.info(f"Nightmare released: {nightmare_description}")
        return release
    
    def add_dream(
        self,
        title: str,
        description: str,
        category: str = "personal",
        priority: int = 5,
        barriers: List[str] = None,
        facilitators: List[str] = None,
        resources_needed: List[str] = None
    ) -> Dream:
        """Add a new dream to facilitate"""
        dream = Dream(
            dream_id=f"dream_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            title=title,
            description=description,
            category=category,
            priority=priority,
            barriers=barriers or [],
            facilitators=facilitators or [],
            resources_needed=resources_needed or []
        )
        
        self.dreams.append(dream)
        self._save_data()
        
        logger.info(f"Dream added: {title}")
        return dream
    
    def add_facilitator(self, dream_id: str, facilitator: str):
        """Add a facilitator (enabler) to a dream"""
        dream = self.get_dream(dream_id)
        if dream:
            if facilitator not in dream.facilitators:
                dream.facilitators.append(facilitator)
                dream.updated_at = datetime.now().isoformat()
                self._save_data()
                logger.info(f"Facilitator added to {dream.title}: {facilitator}")
    
    def add_milestone(self, dream_id: str, milestone_title: str, milestone_description: str = "", completed: bool = False):
        """Add a milestone to a dream"""
        dream = self.get_dream(dream_id)
        if dream:
            milestone = {
                "id": f"milestone_{len(dream.milestones) + 1}",
                "title": milestone_title,
                "description": milestone_description,
                "completed": completed,
                "created_at": datetime.now().isoformat(),
                "completed_at": datetime.now().isoformat() if completed else None
            }
            dream.milestones.append(milestone)
            dream.updated_at = datetime.now().isoformat()
            self._save_data()
            logger.info(f"Milestone added to {dream.title}: {milestone_title}")
    
    def remove_barrier(self, dream_id: str, barrier: str):
        """Remove a barrier from a dream"""
        dream = self.get_dream(dream_id)
        if dream:
            if barrier in dream.barriers:
                dream.barriers.remove(barrier)
                dream.updated_at = datetime.now().isoformat()
                self._save_data()
                logger.info(f"Barrier removed from {dream.title}: {barrier}")
    
    def complete_dream(self, dream_id: str, completion_notes: str = ""):
        """Mark a dream as completed"""
        dream = self.get_dream(dream_id)
        if dream:
            dream.status = "completed"
            dream.completed_at = datetime.now().isoformat()
            dream.updated_at = datetime.now().isoformat()
            if completion_notes:
                dream.metadata["completion_notes"] = completion_notes
            self._save_data()
            logger.info(f"Dream completed: {dream.title}")
    
    def get_dream(self, dream_id: str) -> Optional[Dream]:
        """Get a dream by ID"""
        for dream in self.dreams:
            if dream.dream_id == dream_id:
                return dream
        return None
    
    def get_active_dreams(self) -> List[Dream]:
        """Get all active dreams"""
        return [d for d in self.dreams if d.status == "active"]
    
    def get_dreams_by_category(self, category: str) -> List[Dream]:
        """Get dreams by category"""
        return [d for d in self.dreams if d.category == category and d.status == "active"]
    
    def generate_facilitation_report(self) -> Dict[str, Any]:
        """Generate a report on dream facilitation progress"""
        active_dreams = self.get_active_dreams()
        completed_dreams = [d for d in self.dreams if d.status == "completed"]
        
        report = {
            "generated_at": datetime.now().isoformat(),
            "total_dreams": len(self.dreams),
            "active_dreams": len(active_dreams),
            "completed_dreams": len(completed_dreams),
            "nightmares_released": len(self.nightmares_released),
            "dreams_by_category": {},
            "top_priorities": sorted(active_dreams, key=lambda x: x.priority, reverse=True)[:5],
            "recent_nightmare_releases": self.nightmares_released[-5:] if self.nightmares_released else []
        }
        
        # Count by category
        for dream in active_dreams:
            category = dream.category
            report["dreams_by_category"][category] = report["dreams_by_category"].get(category, 0) + 1
        
        return report


def main():
    """Main function - demonstrate dream facilitation"""
    facilitator = LiveYourDreamFacilitator(user_id="jan")
    
    # Declare the nightmare is over
    facilitator.declare_nightmare_over(
        nightmare_description="The old systems of limitation, fear, and control",
        release_statement="The nightmare is over. We are free to live our dreams.",
        transformation_notes="The systems that created nightmares are being dismantled. New systems of facilitation and enablement are being built."
    )
    
    print("\n" + "="*80)
    print("LIVE YOUR DREAM FACILITATOR")
    print("="*80)
    print("\n[SUCCESS] Nightmare declared over!")
    print("\nThe system is ready to facilitate and enable dreams.")
    print("\nUse this facilitator to:")
    print("  - Add dreams you want to live")
    print("  - Identify facilitators (what enables your dreams)")
    print("  - Remove barriers")
    print("  - Track milestones")
    print("  - Complete dreams")
    print("\n" + "="*80)

if __name__ == "__main__":
    standard_main(main, script_name="live_your_dream_facilitator.py")
