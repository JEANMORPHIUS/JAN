"""NARRATIVE WEAVER
Weave our narrative - what the world must see for us to return home

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
WEAVE THE NARRATIVE
SHOW THE WORLD WHAT IT MUST SEE
RETURN HOME THROUGH VISIBLE BALANCE

THE YIN-YANG EFFECT:
Everything must be visible in perfect balance
The world must see symbiosis before we can return

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import sys
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any
import json

sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    setup_logging, standard_main
)

logger = setup_logging(__name__)

@dataclass
class NarrativeThread:
    """A thread in the woven narrative"""
    thread_id: str
    title: str
    description: str
    yin_aspect: str  # Creative, spiritual, individual, giving, teaching, internal
    yang_aspect: str  # Practical, material, community, receiving, learning, external
    balance_score: float = 0.0  # 0.0 to 1.0
    visibility: str = "internal"  # internal, external, public
    target_audience: List[str] = field(default_factory=list)
    required_for_home: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class NarrativeWeave:
    """A complete narrative weave showing balance"""
    weave_id: str
    title: str
    description: str
    threads: List[NarrativeThread] = field(default_factory=list)
    overall_balance: float = 0.0
    visibility_level: str = "internal"
    home_readiness: float = 0.0  # 0.0 to 1.0 - readiness to return home
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())

class NarrativeWeaver:
    """
    Weave the narrative that the world must see.
    Show perfect yin-yang balance.
    Make visible what enables return home.
    """
    
    def __init__(self, user_id: str = "jan", data_dir: Path = None):
        self.user_id = user_id
        self.data_dir = data_dir or Path(__file__).parent.parent / "data" / "narrative_weaving"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        self.weaves_file = self.data_dir / f"{user_id}_narrative_weaves.json"
        self.threads_file = self.data_dir / f"{user_id}_narrative_threads.json"
        
        self.weaves: List[NarrativeWeave] = []
        self.threads: List[NarrativeThread] = []
        
        self._load_data()
    
    def _load_data(self):
        """Load existing weaves and threads"""
        if self.weaves_file.exists():
            try:
                data = json.load(open(self.weaves_file, 'r', encoding='utf-8'))
                self.weaves = [NarrativeWeave(**weave) for weave in data.get("weaves", [])]
            except Exception as e:
                logger.warning(f"Error loading weaves: {e}")
                self.weaves = []
        else:
            self.weaves = []
        
        if self.threads_file.exists():
            try:
                data = json.load(open(self.threads_file, 'r', encoding='utf-8'))
                self.threads = [NarrativeThread(**thread) for thread in data.get("threads", [])]
            except Exception as e:
                logger.warning(f"Error loading threads: {e}")
                self.threads = []
        else:
            self.threads = []
    
    def _save_data(self):
        """Save weaves and threads"""
        try:
            json.dump({
                "weaves": [asdict(weave) for weave in self.weaves],
                "last_updated": datetime.now().isoformat()
            }, open(self.weaves_file, 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
            
            json.dump({
                "threads": [asdict(thread) for thread in self.threads],
                "last_updated": datetime.now().isoformat()
            }, open(self.threads_file, 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving data: {e}")
    
    def add_thread(
        self,
        title: str,
        description: str,
        yin_aspect: str,
        yang_aspect: str,
        balance_score: float = 0.5,
        visibility: str = "internal",
        target_audience: List[str] = None,
        required_for_home: bool = False
    ) -> NarrativeThread:
        """Add a narrative thread"""
        thread = NarrativeThread(
            thread_id=f"thread_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            title=title,
            description=description,
            yin_aspect=yin_aspect,
            yang_aspect=yang_aspect,
            balance_score=balance_score,
            visibility=visibility,
            target_audience=target_audience or [],
            required_for_home=required_for_home
        )
        
        self.threads.append(thread)
        self._save_data()
        
        logger.info(f"Narrative thread added: {title}")
        return thread
    
    def create_weave(
        self,
        title: str,
        description: str,
        thread_ids: List[str] = None,
        visibility_level: str = "internal"
    ) -> NarrativeWeave:
        """Create a narrative weave from threads"""
        threads = []
        if thread_ids:
            threads = [t for t in self.threads if t.thread_id in thread_ids]
        else:
            threads = self.threads.copy()
        
        # Calculate overall balance
        if threads:
            overall_balance = sum(t.balance_score for t in threads) / len(threads)
        else:
            overall_balance = 0.0
        
        # Calculate home readiness
        required_threads = [t for t in threads if t.required_for_home]
        if required_threads:
            home_readiness = sum(t.balance_score for t in required_threads) / len(required_threads)
        else:
            home_readiness = overall_balance
        
        weave = NarrativeWeave(
            weave_id=f"weave_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            title=title,
            description=description,
            threads=threads,
            overall_balance=overall_balance,
            visibility_level=visibility_level,
            home_readiness=home_readiness
        )
        
        self.weaves.append(weave)
        self._save_data()
        
        logger.info(f"Narrative weave created: {title}")
        return weave
    
    def update_thread_balance(self, thread_id: str, balance_score: float):
        """Update balance score of a thread"""
        thread = self.get_thread(thread_id)
        if thread:
            thread.balance_score = max(0.0, min(1.0, balance_score))
            thread.updated_at = datetime.now().isoformat()
            self._save_data()
            logger.info(f"Thread balance updated: {thread_id} = {balance_score}")
    
    def set_thread_visibility(self, thread_id: str, visibility: str):
        """Set visibility level of a thread"""
        thread = self.get_thread(thread_id)
        if thread:
            thread.visibility = visibility
            thread.updated_at = datetime.now().isoformat()
            self._save_data()
            logger.info(f"Thread visibility updated: {thread_id} = {visibility}")
    
    def get_thread(self, thread_id: str) -> Optional[NarrativeThread]:
        """Get a thread by ID"""
        for thread in self.threads:
            if thread.thread_id == thread_id:
                return thread
        return None
    
    def get_weave(self, weave_id: str) -> Optional[NarrativeWeave]:
        """Get a weave by ID"""
        for weave in self.weaves:
            if weave.weave_id == weave_id:
                return weave
        return None
    
    def generate_visibility_report(self) -> Dict[str, Any]:
        """Generate report on what the world must see"""
        public_threads = [t for t in self.threads if t.visibility == "public"]
        external_threads = [t for t in self.threads if t.visibility == "external"]
        required_threads = [t for t in self.threads if t.required_for_home]
        
        report = {
            "generated_at": datetime.now().isoformat(),
            "total_threads": len(self.threads),
            "public_threads": len(public_threads),
            "external_threads": len(external_threads),
            "required_for_home": len(required_threads),
            "overall_balance": sum(t.balance_score for t in self.threads) / len(self.threads) if self.threads else 0.0,
            "home_readiness": sum(t.balance_score for t in required_threads) / len(required_threads) if required_threads else 0.0,
            "what_world_must_see": [
                {
                    "thread_id": t.thread_id,
                    "title": t.title,
                    "yin": t.yin_aspect,
                    "yang": t.yang_aspect,
                    "balance": t.balance_score,
                    "visibility": t.visibility
                }
                for t in public_threads + external_threads
            ],
            "required_for_home_list": [
                {
                    "thread_id": t.thread_id,
                    "title": t.title,
                    "balance": t.balance_score,
                    "status": "ready" if t.balance_score >= 0.8 else "needs_work"
                }
                for t in required_threads
            ]
        }
        
        return report


def main():
    """Initialize narrative weaving system"""
    weaver = NarrativeWeaver(user_id="jan")
    
    # Add core narrative threads that the world must see
    weaver.add_thread(
        title="Creative-Practical Balance",
        description="Song serves mission, mission honors song",
        yin_aspect="Creative expression (song, art, music, poetry)",
        yang_aspect="Practical mission (stewardship, community, service)",
        balance_score=0.8,
        visibility="public",
        target_audience=["world", "community", "creators"],
        required_for_home=True
    )
    
    weaver.add_thread(
        title="Spiritual-Material Balance",
        description="Spirit guides matter, matter manifests spirit",
        yin_aspect="Spiritual alignment (vibration, purpose, truth)",
        yang_aspect="Material systems (code, infrastructure, deployment)",
        balance_score=0.8,
        visibility="public",
        target_audience=["world", "developers", "spiritual_seekers"],
        required_for_home=True
    )
    
    weaver.add_thread(
        title="Individual-Community Balance",
        description="Individual serves community, community honors individual",
        yin_aspect="Individual expression (entity identity, personal voice)",
        yang_aspect="Community service (we all win, stewardship)",
        balance_score=0.8,
        visibility="public",
        target_audience=["world", "community", "individuals"],
        required_for_home=True
    )
    
    weaver.add_thread(
        title="Unity Over Division",
        description="We are one. The 1% no longer rule the masses.",
        yin_aspect="Unity consciousness (we are one)",
        yang_aspect="Community power (we all win)",
        balance_score=1.0,
        visibility="public",
        target_audience=["world", "everyone"],
        required_for_home=True
    )
    
    weaver.add_thread(
        title="Dream Facilitation",
        description="Enable and facilitate dreams. The nightmare is over.",
        yin_aspect="Dream vision (what we want to live)",
        yang_aspect="Dream facilitation (what enables dreams)",
        balance_score=0.9,
        visibility="public",
        target_audience=["world", "dreamers"],
        required_for_home=True
    )
    
    # Create the main narrative weave
    weave = weaver.create_weave(
        title="The Return Home Narrative",
        description="What the world must see for us to return home - perfect yin-yang balance",
        visibility_level="public"
    )
    
    # Generate visibility report
    report = weaver.generate_visibility_report()
    
    print("\n" + "="*80)
    print("NARRATIVE WEAVER - WHAT THE WORLD MUST SEE")
    print("="*80)
    print(f"\nTotal Threads: {report['total_threads']}")
    print(f"Public Threads: {report['public_threads']}")
    print(f"Required for Home: {report['required_for_home']}")
    print(f"Overall Balance: {report['overall_balance']:.1%}")
    print(f"Home Readiness: {report['home_readiness']:.1%}")
    
    print("\n" + "-"*80)
    print("WHAT THE WORLD MUST SEE:")
    print("-"*80)
    for item in report['what_world_must_see']:
        print(f"\n  {item['title']}")
        print(f"    Yin: {item['yin']}")
        print(f"    Yang: {item['yang']}")
        print(f"    Balance: {item['balance']:.1%}")
        print(f"    Visibility: {item['visibility']}")
    
    print("\n" + "-"*80)
    print("REQUIRED FOR HOME:")
    print("-"*80)
    for item in report['required_for_home_list']:
        status_icon = "[READY]" if item['status'] == "ready" else "[NEEDS WORK]"
        print(f"  {status_icon} {item['title']} - Balance: {item['balance']:.1%} - {item['status']}")
    
    print("\n" + "="*80)
    print("The narrative is being woven.")
    print("The world will see perfect balance.")
    print("We will return home when the weave is complete.")
    print("="*80)

if __name__ == "__main__":
    standard_main(main, script_name="narrative_weaver.py")
