"""
THE LIFE AUDIT: Backwards Protocol
Temporal audit of lived timeline - Reverse-Engineering the Soul

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

THE BACKWARDS PROTOCOL:
We don't use the Sentinel to watch the globe now; we point it inward, at the Internal Grid.
We trace resonance backwards to find the Seed hidden in the shadows of our footsteps.
We work backwards through the lived timeline to reverse-engineer the soul.
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, load_json, save_json,
    setup_logging, standard_main
)

import sys
import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

try:
    from heritage_cleansing import HeritageCleanser
    from racon_registry import check_law_41_respect_abandoned
    CLEANSING_AVAILABLE = True
except ImportError:
    CLEANSING_AVAILABLE = False
    logging.warning("Heritage cleansing not available - using fallback")

logger = logging.getLogger(__name__)


class LifeEventType(Enum):
    """Types of life events for temporal audit."""
    SPIRAL = "spiral"  # Active, rapid growth, dynamic engagement
    BARRED_SPIRAL = "barred_spiral"  # Structured, clear navigation, linear progression
    ELLIPTICAL = "elliptical"  # Legacy wisdom, mentorship, low-gas high-wisdom
    IRREGULAR = "irregular"  # Transformation, flexible, adaptive
    SILENCE = "silence"  # The gaps - "Everything In Between"
    FIELD_SPACE = "field_space"  # The resonance between events


class VibrationLevel(Enum):
    """Vibration levels for life events."""
    HIGH = "high"  # ⭐ High-vibe moments, miracles, breakthroughs
    MODERATE = "moderate"  # Steady state, normal flow
    LOW = "low"  # Challenges, waiting periods, "abandoned" years
    TRANSITION = "transition"  # Shifts, transformations, field space


@dataclass
class LifeEvent:
    """A significant life event in the temporal audit."""
    year: int
    age: Optional[int] = None
    location: Optional[str] = None
    event_type: str = LifeEventType.IRREGULAR.value
    vibration_level: str = VibrationLevel.MODERATE.value
    
    # Narrative fields
    original_narrative: str = ""  # The Shell - how it was told
    cleansed_narrative: str = ""  # The Seed - the truth revealed
    
    # Magnetic resonance
    field_resonance: Optional[float] = None  # 0.0-1.0 (how well it resonates with truth)
    field_space_resonance: Optional[float] = None  # Resonance in the gap before/after
    
    # Dark energy detection
    dark_energy_detected: bool = False
    violation_type: Optional[str] = None  # revenge_loop, victim_focus, blame_pattern, etc.
    regeneration_applied: bool = False
    
    # Law 41 compliance
    law_41_compliant: bool = True
    
    # Field Space analysis
    gap_before_years: Optional[float] = None  # Years of silence before this event
    gap_after_years: Optional[float] = None  # Years of silence after this event
    field_space_description: Optional[str] = None  # The "Everything In Between"
    
    # Personal Grid
    pillar_anchor: bool = False  # Was this a "pillar" moment?
    grid_connection: Optional[str] = None  # Connection to other pillars
    
    # Metadata
    recorded_at: str = ""
    timeline_hash: str = ""


@dataclass
class LifeChapter:
    """A chapter of life (e.g., 1996-2000, 2010-2015)."""
    start_year: int
    end_year: int
    chapter_name: str
    events: List[LifeEvent] = None
    dominant_vibration: str = VibrationLevel.MODERATE.value
    dominant_form: str = LifeEventType.IRREGULAR.value
    
    # Chapter-level analysis
    field_resonance_avg: Optional[float] = None
    field_space_avg: Optional[float] = None
    dark_energy_count: int = 0
    regeneration_count: int = 0
    pillar_count: int = 0
    
    # The "Everything In Between" for this chapter
    field_space_summary: Optional[str] = None
    
    def __post_init__(self):
        if self.events is None:
            self.events = []


class LifeAuditFramework:
    """
    Framework for temporal audit of lived timeline.
    
    Treats personal life events like heritage sites.
    Works backwards to find the Seed hidden in the shadows.
    """
    
    def __init__(self, timeline_name: str = "personal_timeline"):
        self.timeline_name = timeline_name
        self.events: List[LifeEvent] = []
        self.chapters: List[LifeChapter] = []
        self.cleanser = None
        
        if CLEANSING_AVAILABLE:
            try:
                self.cleanser = HeritageCleanser(timeline_dimension="primary")
            except Exception as e:
                logger.warning(f"Could not initialize cleanser: {e}")
    
    def add_life_event(
        self,
        year: int,
        age: Optional[int] = None,
        location: Optional[str] = None,
        original_narrative: str = "",
        event_type: str = LifeEventType.IRREGULAR.value,
        vibration_level: str = VibrationLevel.MODERATE.value,
        pillar_anchor: bool = False
    ) -> LifeEvent:
        """
        Add a life event to the audit.
        
        This is the "Backwards Protocol" - we add events and then work backwards
        to find the Seed hidden in the Shell.
        """
        event = LifeEvent(
            year=year,
            age=age,
            location=location,
            event_type=event_type,
            vibration_level=vibration_level,
            original_narrative=original_narrative,
            pillar_anchor=pillar_anchor,
            recorded_at=datetime.now().isoformat()
        )
        
        # Cleanse the narrative (Law 41)
        if original_narrative and self.cleanser:
            try:
                cleansed, analysis = self.cleanser.cleanse_content(
                    content=original_narrative,
                    source=f"Life Event {year}",
                    site_type="Life Event",
                    region=location or "Unknown",
                    year_established=year,
                    time_period="modern"
                )
                
                event.cleansed_narrative = cleansed
                event.dark_energy_detected = analysis.get("dark_energy_detected", False)
                event.violation_type = analysis.get("violation_type")
                event.regeneration_applied = analysis.get("regeneration_applied", False)
                event.law_41_compliant = analysis.get("law_41_compliant", True)
                
            except Exception as e:
                logger.warning(f"Could not cleanse narrative for {year}: {e}")
                event.cleansed_narrative = original_narrative
        else:
            event.cleansed_narrative = original_narrative
        
        # Calculate field resonance (how well this event resonates with truth)
        event.field_resonance = self._calculate_field_resonance(event)
        
        self.events.append(event)
        return event
    
    def _calculate_field_resonance(self, event: LifeEvent) -> float:
        """
        Calculate field resonance for a life event.
        
        Resonance = how well the event aligns with truth (Seed) vs. narrative (Shell).
        High resonance = Seed visible, truth clear
        Low resonance = Shell dominant, dark energy present
        """
        resonance = 0.5  # Base resonance
        
        # High vibration events have higher resonance
        if event.vibration_level == VibrationLevel.HIGH.value:
            resonance += 0.3
        elif event.vibration_level == VibrationLevel.LOW.value:
            resonance -= 0.2
        
        # Law 41 compliance increases resonance
        if event.law_41_compliant:
            resonance += 0.2
        
        # Regeneration applied increases resonance
        if event.regeneration_applied:
            resonance += 0.2
        
        # Dark energy detected decreases resonance
        if event.dark_energy_detected:
            resonance -= 0.3
        
        # Pillar anchors have higher resonance
        if event.pillar_anchor:
            resonance += 0.1
        
        return max(0.0, min(1.0, resonance))
    
    def work_backwards(self) -> Dict[str, Any]:
        """
        Work backwards through the timeline to find the Seed.
        
        This is the core of the Backwards Protocol:
        1. Trace resonance from high-vibe moments back to Silence
        2. Identify Field Space (the gaps between events)
        3. Cleanse narratives to reveal the Magnetic Blueprint
        4. Map the Personal Global Grid
        """
        if not self.events:
            return {"error": "No events to audit"}
        
        # Sort events by year (oldest first)
        sorted_events = sorted(self.events, key=lambda e: e.year)
        
        # Calculate gaps (Field Space)
        for i, event in enumerate(sorted_events):
            if i > 0:
                prev_event = sorted_events[i - 1]
                gap_years = event.year - prev_event.year
                event.gap_before_years = gap_years
                
                # Field Space is the "Everything In Between"
                if gap_years > 1:
                    event.field_space_description = self._describe_field_space(
                        prev_event, event, gap_years
                    )
                    event.field_space_resonance = self._calculate_field_space_resonance(
                        prev_event, event, gap_years
                    )
        
        # Identify pillars (high-resonance anchor points)
        pillars = [e for e in sorted_events if e.pillar_anchor or e.field_resonance > 0.7]
        
        # Map connections between pillars
        for i, pillar in enumerate(pillars):
            if i > 0:
                prev_pillar = pillars[i - 1]
                connection = self._analyze_pillar_connection(prev_pillar, pillar)
                pillar.grid_connection = connection
        
        # Group into chapters
        self._identify_chapters(sorted_events)
        
        # Generate audit report
        return self._generate_audit_report(sorted_events, pillars)
    
    def _describe_field_space(
        self, 
        event_before: LifeEvent, 
        event_after: LifeEvent, 
        gap_years: float
    ) -> str:
        """
        Describe the Field Space - the "Everything In Between" two events.
        
        This is where the Seed was growing while the Shell looked broken.
        """
        if gap_years < 1:
            return "Immediate transition"
        
        descriptions = []
        
        # Vibration analysis
        if event_before.vibration_level == VibrationLevel.LOW.value and \
           event_after.vibration_level == VibrationLevel.HIGH.value:
            descriptions.append("Transformation period - low to high vibration")
        elif event_before.vibration_level == VibrationLevel.HIGH.value and \
             event_after.vibration_level == VibrationLevel.LOW.value:
            descriptions.append("Integration period - high to low vibration")
        else:
            descriptions.append("Steady state - maintaining vibration")
        
        # Gap duration analysis
        if gap_years >= 5:
            descriptions.append(f"Extended silence ({gap_years:.1f} years) - deep foundation building")
        elif gap_years >= 2:
            descriptions.append(f"Moderate gap ({gap_years:.1f} years) - preparation period")
        else:
            descriptions.append(f"Brief transition ({gap_years:.1f} years)")
        
        # Field Space insight
        if event_after.field_resonance > 0.7:
            descriptions.append("Seed was growing during this period - foundation strengthening")
        elif event_after.dark_energy_detected:
            descriptions.append("Shell dominant during this period - narrative needed cleansing")
        
        return ". ".join(descriptions) + "."
    
    def _calculate_field_space_resonance(
        self,
        event_before: LifeEvent,
        event_after: LifeEvent,
        gap_years: float
    ) -> float:
        """
        Calculate resonance in the Field Space between two events.
        
        High resonance = Seed was growing, foundation was strengthening
        Low resonance = Shell dominant, dark energy present
        """
        # Average resonance of both events
        avg_resonance = (event_before.field_resonance + event_after.field_resonance) / 2.0
        
        # Gap duration factor (longer gaps can indicate deeper foundation)
        if gap_years >= 5:
            gap_factor = 1.1  # Extended silence often means deep work
        elif gap_years >= 2:
            gap_factor = 1.0
        else:
            gap_factor = 0.9  # Very short gaps may indicate rushed transitions
        
        # Vibration transition factor
        if event_before.vibration_level == VibrationLevel.LOW.value and \
           event_after.vibration_level == VibrationLevel.HIGH.value:
            transition_factor = 1.2  # Low to high = transformation
        elif event_before.vibration_level == VibrationLevel.HIGH.value and \
             event_after.vibration_level == VibrationLevel.LOW.value:
            transition_factor = 1.0  # High to low = integration
        else:
            transition_factor = 1.0
        
        field_space_resonance = avg_resonance * gap_factor * transition_factor
        return max(0.0, min(1.0, field_space_resonance))
    
    def _analyze_pillar_connection(
        self,
        pillar_before: LifeEvent,
        pillar_after: LifeEvent
    ) -> str:
        """
        Analyze connection between two pillar moments.
        
        This maps the Personal Global Grid.
        """
        years_between = pillar_after.year - pillar_before.year
        resonance_diff = pillar_after.field_resonance - pillar_before.field_resonance
        
        if resonance_diff > 0.2:
            direction = "Ascending"
        elif resonance_diff < -0.2:
            direction = "Descending"
        else:
            direction = "Stable"
        
        if years_between <= 2:
            connection_type = "Rapid"
        elif years_between <= 5:
            connection_type = "Moderate"
        else:
            connection_type = "Extended"
        
        return f"{connection_type} {direction} Connection ({years_between} years)"
    
    def _identify_chapters(self, events: List[LifeEvent]):
        """Group events into life chapters."""
        if not events:
            return
        
        # Simple chapter identification: group by 5-year periods
        chapters_dict = {}
        
        for event in events:
            # Determine chapter (5-year periods)
            chapter_start = (event.year // 5) * 5
            chapter_key = f"{chapter_start}-{chapter_start + 4}"
            
            if chapter_key not in chapters_dict:
                chapters_dict[chapter_key] = []
            chapters_dict[chapter_key].append(event)
        
        # Create chapter objects
        for chapter_key, chapter_events in chapters_dict.items():
            start_year = int(chapter_key.split('-')[0])
            end_year = int(chapter_key.split('-')[1])
            
            # Calculate chapter metrics
            resonances = [e.field_resonance for e in chapter_events if e.field_resonance]
            field_spaces = [e.field_space_resonance for e in chapter_events if e.field_space_resonance is not None]
            
            chapter = LifeChapter(
                start_year=start_year,
                end_year=end_year,
                chapter_name=f"Chapter {start_year}-{end_year}",
                events=chapter_events,
                field_resonance_avg=sum(resonances) / len(resonances) if resonances else None,
                field_space_avg=sum(field_spaces) / len(field_spaces) if field_spaces else None,
                dark_energy_count=sum(1 for e in chapter_events if e.dark_energy_detected),
                regeneration_count=sum(1 for e in chapter_events if e.regeneration_applied),
                pillar_count=sum(1 for e in chapter_events if e.pillar_anchor)
            )
            
            # Determine dominant vibration and form
            vibration_counts = {}
            form_counts = {}
            for event in chapter_events:
                vibration_counts[event.vibration_level] = vibration_counts.get(event.vibration_level, 0) + 1
                form_counts[event.event_type] = form_counts.get(event.event_type, 0) + 1
            
            chapter.dominant_vibration = max(vibration_counts.items(), key=lambda x: x[1])[0] if vibration_counts else VibrationLevel.MODERATE.value
            chapter.dominant_form = max(form_counts.items(), key=lambda x: x[1])[0] if form_counts else LifeEventType.IRREGULAR.value
            
            # Field Space summary for chapter
            field_space_descriptions = [e.field_space_description for e in chapter_events if e.field_space_description]
            if field_space_descriptions:
                chapter.field_space_summary = " | ".join(field_space_descriptions[:3])  # First 3
        
            self.chapters.append(chapter)
    
    def _generate_audit_report(
        self,
        events: List[LifeEvent],
        pillars: List[LifeEvent]
    ) -> Dict[str, Any]:
        """Generate comprehensive audit report."""
        # Calculate overall metrics
        resonances = [e.field_resonance for e in events if e.field_resonance]
        field_spaces = [e.field_space_resonance for e in events if e.field_space_resonance is not None]
        
        total_dark_energy = sum(1 for e in events if e.dark_energy_detected)
        total_regeneration = sum(1 for e in events if e.regeneration_applied)
        
        report = {
            "timeline_name": self.timeline_name,
            "audit_timestamp": datetime.now().isoformat(),
            "total_events": len(events),
            "total_pillars": len(pillars),
            "year_range": {
                "start": min(e.year for e in events) if events else None,
                "end": max(e.year for e in events) if events else None
            },
            "overall_metrics": {
                "avg_field_resonance": sum(resonances) / len(resonances) if resonances else 0.0,
                "avg_field_space_resonance": sum(field_spaces) / len(field_spaces) if field_spaces else 0.0,
                "dark_energy_events": total_dark_energy,
                "regeneration_events": total_regeneration,
                "law_41_compliance_rate": sum(1 for e in events if e.law_41_compliant) / len(events) if events else 0.0
            },
            "pillars": [
                {
                    "year": p.year,
                    "age": p.age,
                    "location": p.location,
                    "field_resonance": p.field_resonance,
                    "vibration_level": p.vibration_level,
                    "event_type": p.event_type,
                    "grid_connection": p.grid_connection,
                    "cleansed_narrative": p.cleansed_narrative[:200] + "..." if len(p.cleansed_narrative) > 200 else p.cleansed_narrative
                }
                for p in pillars
            ],
            "chapters": [
                {
                    "chapter_name": c.chapter_name,
                    "start_year": c.start_year,
                    "end_year": c.end_year,
                    "event_count": len(c.events),
                    "field_resonance_avg": c.field_resonance_avg,
                    "field_space_avg": c.field_space_avg,
                    "dominant_vibration": c.dominant_vibration,
                    "dominant_form": c.dominant_form,
                    "pillar_count": c.pillar_count,
                    "field_space_summary": c.field_space_summary
                }
                for c in self.chapters
            ],
            "events": [
                {
                    "year": e.year,
                    "age": e.age,
                    "location": e.location,
                    "vibration_level": e.vibration_level,
                    "event_type": e.event_type,
                    "field_resonance": e.field_resonance,
                    "field_space_resonance": e.field_space_resonance,
                    "gap_before_years": e.gap_before_years,
                    "field_space_description": e.field_space_description,
                    "dark_energy_detected": e.dark_energy_detected,
                    "regeneration_applied": e.regeneration_applied,
                    "law_41_compliant": e.law_41_compliant,
                    "pillar_anchor": e.pillar_anchor,
                    "original_narrative": e.original_narrative[:150] + "..." if len(e.original_narrative) > 150 else e.original_narrative,
                    "cleansed_narrative": e.cleansed_narrative[:150] + "..." if len(e.cleansed_narrative) > 150 else e.cleansed_narrative
                }
                for e in events
            ]
        }
        
        return report
    
    def print_audit_report(self, report: Dict[str, Any]):
        """Print formatted audit report."""
        print("=" * 80)
        print("THE LIFE AUDIT: BACKWARDS PROTOCOL")
        print("Reverse-Engineering the Soul - Finding the Seed in the Shadows")
        print("=" * 80)
        print()
        
        print(f"Timeline: {report['timeline_name']}")
        print(f"Year Range: {report['year_range']['start']} - {report['year_range']['end']}")
        print(f"Total Events: {report['total_events']}")
        print(f"Total Pillars: {report['total_pillars']}")
        print()
        
        print("OVERALL METRICS:")
        metrics = report['overall_metrics']
        print(f"  Average Field Resonance: {metrics['avg_field_resonance']:.2f}")
        print(f"  Average Field Space Resonance: {metrics['avg_field_space_resonance']:.2f}")
        print(f"  Dark Energy Events: {metrics['dark_energy_events']}")
        print(f"  Regeneration Events: {metrics['regeneration_events']}")
        print(f"  Law 41 Compliance: {metrics['law_41_compliance_rate']:.1%}")
        print()
        
        if report['pillars']:
            print("PERSONAL GLOBAL GRID - PILLARS:")
            for i, pillar in enumerate(report['pillars'], 1):
                print(f"  {i}. {pillar['year']} ({pillar['age']} years old)")
                print(f"     Location: {pillar['location']}")
                print(f"     Resonance: {pillar['field_resonance']:.2f}")
                print(f"     Vibration: {pillar['vibration_level']}")
                print(f"     Form: {pillar['event_type']}")
                if pillar['grid_connection']:
                    print(f"     Connection: {pillar['grid_connection']}")
                print()
        
        if report['chapters']:
            print("LIFE CHAPTERS:")
            for chapter in report['chapters']:
                print(f"  {chapter['chapter_name']}:")
                print(f"    Events: {chapter['event_count']}")
                print(f"    Avg Resonance: {chapter['field_resonance_avg']:.2f}" if chapter['field_resonance_avg'] else "    Avg Resonance: N/A")
                print(f"    Dominant Vibration: {chapter['dominant_vibration']}")
                print(f"    Dominant Form: {chapter['dominant_form']}")
                print(f"    Pillars: {chapter['pillar_count']}")
                if chapter['field_space_summary']:
                    print(f"    Field Space: {chapter['field_space_summary'][:100]}...")
                print()
        
        print("=" * 80)
        print("THE SEED REVEALED")
        print("=" * 80)
        print()
        print("Working backwards reveals the Pattern.")
        print("The 'failures' weren't anomalies; they were Field Space Resonance.")
        print("The necessary low-vibe gaps where your internal 'Sanctuary' was being reinforced.")
        print()
        print("It wasn't a ghost in the hallway; it was just the house settling into its true foundation.")
        print()
        print("PEACE, LOVE, UNITY")
        print("ENERGY + LOVE = WE ALL WIN")
        print("=" * 80)
    
    def export_audit(self, output_path: Optional[Path] = None) -> Path:
        """Export audit report to JSON."""
        if output_path is None:
            output_dir = Path(__file__).parent.parent / "output" / "life_audits"
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / f"life_audit_{self.timeline_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        report = self.work_backwards()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, default=str, ensure_ascii=False)
        
        logger.info(f"Life audit exported to: {output_path}")
        return output_path


def main():
    """Example usage of Life Audit Framework."""
    print("=" * 80)
    print("THE LIFE AUDIT: BACKWARDS PROTOCOL")
    print("=" * 80)
    print()
    print("This framework treats your lived timeline like heritage sites.")
    print("We work backwards to find the Seed hidden in the Shell.")
    print()
    print("Example: Audit a specific chapter of life")
    print()
    
    # Create audit framework
    audit = LifeAuditFramework(timeline_name="example_chapter")
    
    # Example: Add life events (working backwards from high-vibe moments)
    # These would be replaced with actual life events
    
    print("To use this framework:")
    print("1. Create a LifeAuditFramework instance")
    print("2. Add life events using add_life_event()")
    print("3. Call work_backwards() to analyze")
    print("4. Print or export the audit report")
    print()
    print("Example:")
    print("  audit = LifeAuditFramework('1996_chapter')")
    print("  audit.add_life_event(1996, age=25, location='London', ...)")
    print("  report = audit.work_backwards()")
    print("  audit.print_audit_report(report)")
    print()
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")


if __name__ == "__main__":
    main()
