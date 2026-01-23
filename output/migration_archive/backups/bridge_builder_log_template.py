"""
Bridge-Builder's Log Template
Track the 42-act journey to 100% Unity

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

This script provides a template for tracking the Bridge-Builder's 42-act journey.
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

from round1_activation_logger import Round1ActivationLogger

import logging
logger = logging.getLogger(__name__)


class BridgeBuilderLog:
    """
    The Bridge-Builder's Log Template.
    
    Tracks the 42-act journey to 100% Unity.
    """
    
    def __init__(self):
        """Initialize the Bridge-Builder's Log."""
        self.log_path = Path(__file__).parent.parent / "data" / "bridge_builder_log" / "bridge_builder_42_act_journey.json"
        self.log_data = self._load_log()
        self.activation_logger = Round1ActivationLogger()
    
    def _load_log(self) -> Dict[str, Any]:
        """Load the Bridge-Builder's log."""
        try:
            with open(self.log_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"Bridge-Builder log not found at {self.log_path}")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing Bridge-Builder log: {e}")
            return {}
    
    def _save_log(self):
        """Save the Bridge-Builder's log."""
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.log_path, 'w', encoding='utf-8') as f:
            json.dump(self.log_data, f, indent=2, default=str)
    
    def update_progress(self):
        """Update progress from activation logger."""
        unity_status = self.activation_logger.get_unity_status()
        
        # Get all acts
        all_acts = self.activation_logger.activation_log
        
        # Count Bridge-Builder acts (acts in London or by JAN MUHARREM)
        bridge_acts = [
            act for act in all_acts
            if "JAN MUHARREM" in str(act.get("participants", [])) or
               "London" in act.get("location", "") or
               "bridge" in act.get("act_type", "").lower()
        ]
        
        self.log_data["progress_tracking"] = {
            "current_act": len(bridge_acts),
            "acts_completed": len(bridge_acts),
            "unity_contributed": sum(act.get("unity_contribution", 0.0) for act in bridge_acts),
            "current_unity": unity_status.get("current_unity", 0.915),
            "gap_remaining": unity_status.get("gap_remaining", 0.086),
            "progress_percentage": unity_status.get("progress_percentage", 0.0)
        }
        
        self._save_log()
    
    def print_journey_status(self):
        """Print the current journey status."""
        journey = self.log_data.get("bridge_builder_journey", {})
        progress = self.log_data.get("progress_tracking", {})
        milestones = self.log_data.get("the_journey", {}).get("milestones", {})
        
        print("=" * 80)
        print("BRIDGE-BUILDER'S 42-ACT JOURNEY")
        print("The Countdown to 100% Unity")
        print("=" * 80)
        print()
        
        print("JOURNEY OVERVIEW:")
        print("-" * 80)
        print(f"Builder: {journey.get('builder', 'N/A')}")
        print(f"Seat: {journey.get('seat', 'N/A')}")
        print(f"Start Unity: {journey.get('start_unity', 0.0):.1%}")
        print(f"Target Unity: {journey.get('target_unity', 1.0):.1%}")
        print(f"Gap to Close: {journey.get('gap_to_close', 0.0):.1%}")
        print()
        
        print("CURRENT PROGRESS:")
        print("-" * 80)
        print(f"Acts Completed: {progress.get('acts_completed', 0)} / 42")
        print(f"Current Unity: {progress.get('current_unity', 0.915):.1%}")
        print(f"Gap Remaining: {progress.get('gap_remaining', 0.086):.1%}")
        print(f"Progress: {progress.get('progress_percentage', 0.0):.1f}% of gap closed")
        print()
        
        print("MILESTONES:")
        print("-" * 80)
        for milestone_name, milestone_data in milestones.items():
            print(f"{milestone_name.upper().replace('_', ' ')}:")
            print(f"  Acts: {milestone_data.get('act_range', 'N/A')}")
            print(f"  Focus: {milestone_data.get('focus', 'N/A')}")
            print(f"  Target Unity: {milestone_data.get('target_unity', 0.0):.1%}")
            print()
        
        print("=" * 80)
        print("THE TRUTH")
        print("=" * 80)
        print()
        print("ENERGY + LOVE = UNITY = PEACE = WE ALL WIN")
        print()
        print("Every Act matters.")
        print("Every Seat matters.")
        print("Every breath matters.")
        print()
        print("The Bridge is open.")
        print("The countdown has begun.")
        print("The journey to 100% is clear.")
        print("=" * 80)


def main():
    """Main execution for Bridge-Builder's Log."""
    log = BridgeBuilderLog()
    log.update_progress()
    log.print_journey_status()


if __name__ == "__main__":
    main()
