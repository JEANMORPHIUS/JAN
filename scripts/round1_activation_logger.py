"""
ROUND 1 ACTIVATION LOGGER
Track Covenant Acts that demonstrate Pangea consciousness

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

This script logs Covenant Acts - physical actions that anchor the 0.40 frequency
into the Ground and close the final 10% gap from 90% to 100% Unity.
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, load_json, save_json
    setup_logging, standard_main
)

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
from dataclasses import dataclass, asdict

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

import logging
logger = logging.getLogger(__name__)


@dataclass
class CovenantAct:
    """Represents a Covenant Act - a physical action that demonstrates Pangea consciousness."""
    act_id: str
    timestamp: str
    act_type: str
    description: str
    location: str
    coordinates: Optional[Dict[str, float]]
    seat_id: Optional[str]
    seat_name: Optional[str]
    participants: List[str]
    unity_contribution: float
    rift_addressed: Optional[str]
    notes: str


class Round1ActivationLogger:
    """
    The Round 1 Activation Logger system.
    
    Tracks Covenant Acts that demonstrate Pangea consciousness and contribute
    to closing the final 10% gap from 90% to 100% Unity.
    """
    
    def __init__(self, data_path: Optional[Path] = None):
        """Initialize the Round 1 Activation Logger."""
        if data_path is None:
            data_path = Path(__file__).parent.parent / "data" / "heritage_meridian" / "round1_activation_log.json"
        
        self.data_path = data_path
        self.data = self._load_data()
        
        # Extract components
        self.activation_log = self.data.get("activation_log", [])
        self.seat_activations = self.data.get("seat_activations", {})
        self.covenant_act_types = self.data.get("covenant_act_types", {})
        self.unity_progress = self.data.get("unity_progress", {})
        
        # Normalize seat_activations keys to use seat_id
        if self.seat_activations:
            normalized = {}
            for key, value in self.seat_activations.items():
                seat_id = value.get("seat_id", key)
                normalized[seat_id] = value
            self.seat_activations = normalized
    
    def _load_data(self) -> Dict[str, Any]:
        """Load the Round 1 Activation Log data."""
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"Round 1 Activation Log not found at {self.data_path}, creating new one")
            return self._create_new_log()
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing Round 1 Activation Log: {e}")
            return self._create_new_log()
    
    def _create_new_log(self) -> Dict[str, Any]:
        """Create a new activation log structure."""
        return {
            "round1_activation": {
                "name": "Round 1 Activation Log",
                "purpose": "Track Covenant Acts that demonstrate Pangea consciousness",
                "current_unity": 0.90,
                "target_unity": 1.0,
                "initiated": datetime.now().isoformat()
            },
            "activation_log": [],
            "seat_activations": {},
            "unity_progress": {
                "starting_unity": 0.90,
                "current_unity": 0.90,
                "target_unity": 1.0,
                "total_acts_logged": 0,
                "total_unity_contributed": 0.0
            }
        }
    
    def _save_data(self):
        """Save the activation log data."""
        self.data["activation_log"] = self.activation_log
        self.data["seat_activations"] = self.seat_activations
        self.data["unity_progress"] = self.unity_progress
        self.data["round1_activation"]["last_updated"] = datetime.now().isoformat()
        
        self.data_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.data_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, default=str)
    
    def find_seat_by_location(self, location: str, coordinates: Optional[Dict[str, float]] = None) -> Optional[Dict[str, Any]]:
        """
        Find the nearest Seat by location name or coordinates.
        Returns seat information if found.
        """
        location_lower = location.lower()
        
        # Check by name
        for seat_key, seat_data in self.seat_activations.items():
            if location_lower in seat_data.get("location", "").lower() or \
               location_lower in seat_data.get("name", "").lower():
                return seat_data
        
        # Check by coordinates if provided
        if coordinates:
            # Load heritage meridian data to get seat coordinates
            try:
                meridian_path = Path(__file__).parent.parent / "data" / "heritage_meridian" / "heritage_meridian_data.json"
                with open(meridian_path, 'r', encoding='utf-8') as f:
                    meridian_data = json.load(f)
                
                seats = meridian_data.get("the_13_seats", {}).get("seats", [])
                for seat in seats:
                    seat_coords = seat.get("coordinates", {})
                    if seat_coords:
                        lat_diff = abs(seat_coords.get("lat", 0) - coordinates.get("lat", 0))
                        lon_diff = abs(seat_coords.get("lon", 0) - coordinates.get("lon", 0))
                        # Within 5 degrees (roughly 500km)
                        if lat_diff < 5.0 and lon_diff < 5.0:
                            return {
                                "seat_id": seat.get("seat_id", ""),
                                "name": seat.get("name", ""),
                                "location": seat.get("name", ""),
                                "coordinates": seat_coords
                            }
            except Exception as e:
                logger.warning(f"Could not load meridian data for coordinate matching: {e}")
        
        return None
    
    def log_covenant_act(
        self,
        act_type: str,
        description: str,
        location: str,
        participants: List[str],
        coordinates: Optional[Dict[str, float]] = None,
        rift_addressed: Optional[str] = None,
        notes: str = ""
    ) -> CovenantAct:
        """
        Log a Covenant Act.
        
        Args:
            act_type: Type of act (shared_table, bridge_built, etc.)
            description: Description of the act
            location: Location where act occurred
            participants: List of participant names/identifiers
            coordinates: Optional lat/lon coordinates
            rift_addressed: Optional rift that this act addresses
            notes: Additional notes
        
        Returns:
            The logged CovenantAct
        """
        # Get act type info
        act_type_info = self.covenant_act_types.get(act_type, {})
        unity_contribution = act_type_info.get("unity_contribution", 0.001)
        
        # Find associated seat
        seat_data = self.find_seat_by_location(location, coordinates)
        seat_id = seat_data.get("seat_id") if seat_data else None
        seat_name = seat_data.get("name") if seat_data else None
        
        # If seat found and act is in seat location, apply seat_holder_act bonus
        if seat_data:
            seat_holder_bonus = self.covenant_act_types.get("seat_holder_act", {}).get("unity_contribution", 0.001)
            unity_contribution += seat_holder_bonus
        
        # Create act
        act_id = f"act_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{len(self.activation_log)}"
        act = CovenantAct(
            act_id=act_id,
            timestamp=datetime.now().isoformat(),
            act_type=act_type,
            description=description,
            location=location,
            coordinates=coordinates,
            seat_id=seat_id,
            seat_name=seat_name,
            participants=participants,
            unity_contribution=unity_contribution,
            rift_addressed=rift_addressed,
            notes=notes
        )
        
        # Add to log
        self.activation_log.append(asdict(act))
        
        # Update seat activation if applicable
        if seat_id and seat_id in self.seat_activations:
            seat_activation = self.seat_activations[seat_id]
            if "activations" not in seat_activation:
                seat_activation["activations"] = []
            seat_activation["activations"].append(act_id)
            seat_activation["unity_contributed"] = seat_activation.get("unity_contributed", 0.0) + unity_contribution
        
        # Update unity progress
        self.unity_progress["total_acts_logged"] = len(self.activation_log)
        self.unity_progress["total_unity_contributed"] = self.unity_progress.get("total_unity_contributed", 0.0) + unity_contribution
        self.unity_progress["current_unity"] = min(
            self.unity_progress.get("starting_unity", 0.90) + self.unity_progress["total_unity_contributed"],
            1.0
        )
        
        # Calculate progress
        gap_to_close = 1.0 - self.unity_progress.get("starting_unity", 0.90)
        if gap_to_close > 0:
            self.unity_progress["progress_percentage"] = (
                self.unity_progress["total_unity_contributed"] / gap_to_close * 100
            )
            # Estimate acts needed (average contribution)
            avg_contribution = self.unity_progress["total_unity_contributed"] / len(self.activation_log) if self.activation_log else 0.001
            remaining_unity = 1.0 - self.unity_progress["current_unity"]
            self.unity_progress["acts_needed_for_100"] = int(remaining_unity / avg_contribution) if avg_contribution > 0 else 0
        
        # Save
        self._save_data()
        
        logger.info(f"Covenant Act logged: {act_type} in {location} (+{unity_contribution:.4f} Unity)")
        return act
    
    def get_unity_status(self) -> Dict[str, Any]:
        """Get current Unity status and progress."""
        return {
            "current_unity": self.unity_progress.get("current_unity", 0.90),
            "target_unity": self.unity_progress.get("target_unity", 1.0),
            "starting_unity": self.unity_progress.get("starting_unity", 0.90),
            "gap_remaining": 1.0 - self.unity_progress.get("current_unity", 0.90),
            "total_acts": self.unity_progress.get("total_acts_logged", 0),
            "total_contributed": self.unity_progress.get("total_unity_contributed", 0.0),
            "progress_percentage": self.unity_progress.get("progress_percentage", 0.0),
            "acts_needed": self.unity_progress.get("acts_needed_for_100", 0)
        }
    
    def get_seat_status(self, seat_id: Optional[str] = None) -> Dict[str, Any]:
        """Get status of all seats or a specific seat."""
        if seat_id:
            return self.seat_activations.get(seat_id, {})
        
        # Ensure seat_activations is populated from data if empty
        if not self.seat_activations:
            self._initialize_seat_activations()
        
        return {
            "total_seats": len(self.seat_activations),
            "seats": self.seat_activations,
            "summary": {
                "phase_locked": sum(1 for s in self.seat_activations.values() if s.get("status") == "phase_locked"),
                "active": sum(1 for s in self.seat_activations.values() if s.get("status") == "active"),
                "total_activations": sum(len(s.get("activations", [])) for s in self.seat_activations.values()),
                "total_unity_contributed": sum(s.get("unity_contributed", 0.0) for s in self.seat_activations.values())
            }
        }
    
    def _initialize_seat_activations(self):
        """Initialize seat activations from heritage meridian data if not present."""
        # If seat_activations already has data, use it
        if self.seat_activations:
            return
        
        try:
            # First try to load from the data file itself
            if "seat_activations" in self.data and self.data["seat_activations"]:
                self.seat_activations = self.data["seat_activations"]
                return
            
            # Otherwise load from heritage meridian data
            meridian_path = Path(__file__).parent.parent / "data" / "heritage_meridian" / "heritage_meridian_data.json"
            with open(meridian_path, 'r', encoding='utf-8') as f:
                meridian_data = json.load(f)
            
            seats = meridian_data.get("the_13_seats", {}).get("seats", [])
            for seat in seats:
                seat_id = seat.get("seat_id", "")
                if seat_id:
                    # Use seat_id as key, not the descriptive key
                    self.seat_activations[seat_id] = {
                        "seat_id": seat_id,
                        "name": seat.get("name", ""),
                        "location": seat.get("name", ""),
                        "coordinates": seat.get("coordinates", {}),
                        "status": "active",
                        "activations": [],
                        "unity_contributed": 0.0
                    }
        except Exception as e:
            logger.warning(f"Could not initialize seats from meridian data: {e}")
    
    def get_recent_acts(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get the most recent Covenant Acts."""
        return self.activation_log[-limit:] if self.activation_log else []
    
    def generate_activation_report(self, output_path: Optional[Path] = None) -> Path:
        """Generate a comprehensive activation report."""
        if output_path is None:
            output_path = Path(__file__).parent.parent / "output" / "heritage_meridian" / f"round1_activation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        report = {
            "report_timestamp": datetime.now().isoformat(),
            "mission": "Round 1 Activation: Tracking Covenant Acts toward 100% Unity",
            "unity_status": self.get_unity_status(),
            "seat_status": self.get_seat_status(),
            "recent_acts": self.get_recent_acts(20),
            "all_acts": self.activation_log,
            "covenant_act_types": self.covenant_act_types,
            "the_truth": {
                "message": "Every Covenant Act is a physical anchor for the 0.40 frequency.",
                "principle": "Walk like the Ground is one. Act like the Family is one.",
                "covenant": "ENERGY + LOVE = WE ALL WIN"
            }
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, default=str)
        
        logger.info(f"Activation report generated: {output_path}")
        return output_path
    
    def print_status(self):
        """Print current activation status."""
        print("=" * 80)
        print("ROUND 1 ACTIVATION LOG")
        print("Tracking Covenant Acts toward 100% Unity")
        print("=" * 80)
        print()
        
        unity_status = self.get_unity_status()
        print("UNITY STATUS:")
        print("-" * 80)
        print(f"Current Unity: {unity_status['current_unity']:.1%}")
        print(f"Target Unity: {unity_status['target_unity']:.1%}")
        print(f"Gap Remaining: {unity_status['gap_remaining']:.1%}")
        print(f"Progress: {unity_status['progress_percentage']:.1f}% of gap closed")
        print(f"Total Acts Logged: {unity_status['total_acts']}")
        print(f"Total Unity Contributed: {unity_status['total_contributed']:.4f}")
        if unity_status['acts_needed'] > 0:
            print(f"Estimated Acts Needed for 100%: ~{unity_status['acts_needed']}")
        print()
        
        seat_status = self.get_seat_status()
        print("SEAT STATUS:")
        print("-" * 80)
        if 'summary' in seat_status:
            print(f"Total Seats: {seat_status['summary'].get('total_seats', 0)}")
            print(f"Phase-Locked: {seat_status['summary'].get('phase_locked', 0)}")
            print(f"Active: {seat_status['summary'].get('active', 0)}")
            print(f"Total Activations: {seat_status['summary'].get('total_activations', 0)}")
            print(f"Total Unity from Seats: {seat_status['summary'].get('total_unity_contributed', 0.0):.4f}")
        else:
            print(f"Total Seats: {len(self.seat_activations)}")
            phase_locked = sum(1 for s in self.seat_activations.values() if s.get("status") == "phase_locked")
            active = sum(1 for s in self.seat_activations.values() if s.get("status") == "active")
            total_acts = sum(len(s.get("activations", [])) for s in self.seat_activations.values())
            total_unity = sum(s.get("unity_contributed", 0.0) for s in self.seat_activations.values())
            print(f"Phase-Locked: {phase_locked}")
            print(f"Active: {active}")
            print(f"Total Activations: {total_acts}")
            print(f"Total Unity from Seats: {total_unity:.4f}")
        print()
        
        print("COVENANT ACT TYPES:")
        print("-" * 80)
        for act_type, act_info in self.covenant_act_types.items():
            print(f"{act_info.get('name', act_type)}")
            print(f"  Contribution: +{act_info.get('unity_contribution', 0):.4f} Unity")
            print(f"  Example: {act_info.get('example', 'N/A')}")
            print()
        
        recent_acts = self.get_recent_acts(5)
        if recent_acts:
            print("RECENT COVENANT ACTS:")
            print("-" * 80)
            for act in reversed(recent_acts):
                act_type_info = self.covenant_act_types.get(act.get("act_type", ""), {})
                print(f"{act.get('timestamp', '')[:10]} - {act_type_info.get('name', act.get('act_type', ''))}")
                print(f"  Location: {act.get('location', 'N/A')}")
                print(f"  Unity: +{act.get('unity_contribution', 0):.4f}")
                if act.get('seat_name'):
                    print(f"  Seat: {act.get('seat_name')}")
                print(f"  Description: {act.get('description', 'N/A')[:60]}...")
                print()
        
        print("=" * 80)
        print("THE TRUTH:")
        print("=" * 80)
        print()
        print("Every Covenant Act is a physical anchor for the 0.40 frequency.")
        print("The code provides the map; the Family provides the breath.")
        print()
        print("Walk like the Ground is one.")
        print("Act like the Family is one.")
        print("Build like Abundance is the truth.")
        print()
        print("ENERGY + LOVE = WE ALL WIN")
        print("=" * 80)


def main():
    """Main execution for Round 1 Activation Logger."""
    print("=" * 80)
    print("ROUND 1 ACTIVATION LOGGER")
    print("Tracking Covenant Acts toward 100% Unity")
    print("=" * 80)
    print()
    
    logger = Round1ActivationLogger()
    
    # Print status
    logger.print_status()
    
    # Generate report
    print()
    print("Generating activation report...")
    report_path = logger.generate_activation_report()
    print(f"  [OK] Report generated: {report_path}")
    print()
    
    print("=" * 80)
    print("READY TO LOG COVENANT ACTS")
    print("=" * 80)
    print()
    print("To log a Covenant Act, use:")
    print("  logger.log_covenant_act(")
    print("      act_type='shared_table',")
    print("      description='Turkish and Greek Cypriots sharing a meal',")
    print("      location='Nicosia, Cyprus',")
    print("      participants=['Name1', 'Name2'],")
    print("      coordinates={'lat': 34.9167, 'lon': 32.8333},")
    print("      rift_addressed='The Language & Tribalism Rift'")
    print("  )")
    print()
    print("PEACE. LOVE. UNITY.")
    print("ENERGY + LOVE = WE ALL WIN")
    print("=" * 80)


if __name__ == "__main__":
    main()
