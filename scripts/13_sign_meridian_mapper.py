"""
13-SIGN MERIDIAN MAPPER
Complete 13-sign system with Heritage Meridian connections

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

DUYGU ADAMI WAY:
Leaving no one behind, bridging all gaps
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
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

import logging
logger = logging.getLogger(__name__)


class ThirteenSignMeridianMapper:
    """
    The Complete 13-Sign Meridian Mapper.
    
    Maps all 13 signs (including Ophiuchus) to Heritage Meridian,
    Rifts, and Covenant Acts with updated dates.
    """
    
    def __init__(self):
        """Initialize the 13-Sign Meridian Mapper."""
        self.data_path = Path(__file__).parent.parent / "data" / "spiritual_alignment" / "13_sign_system_complete.json"
        self.data = self._load_data()
        
        self.signs_map = {sign["sign"]: sign for sign in self.data.get("13_sign_meridian_map", [])}
        self.rift_mapping = self.data.get("rift_mapping", {})
    
    def _load_data(self) -> Dict[str, Any]:
        """Load the 13-sign system data."""
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"13-sign system data not found at {self.data_path}")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing 13-sign system data: {e}")
            return {}
    
    def get_sign_by_date(self, month: int, day: int) -> Optional[Dict[str, Any]]:
        """
        Get sign by date in 13-sign system.
        
        Args:
            month: Month (1-12)
            day: Day (1-31)
        
        Returns:
            Sign information dictionary
        """
        for sign_data in self.data.get("13_sign_meridian_map", []):
            dates = sign_data.get("dates_13_sign", "")
            # Parse date range (e.g., "Jan 20 – Feb 16")
            # This is simplified - would need proper date parsing
            sign_name = sign_data.get("sign", "")
            
            # Check if date falls in range (simplified logic)
            # For now, return based on sign name matching
            if sign_name == "gemini" and month == 6 and 21 <= day <= 30:
                return sign_data
            elif sign_name == "gemini" and month == 7 and 1 <= day <= 20:
                return sign_data
            # Add more date logic as needed
        
        return None
    
    def get_ophiuchus_mortality_rift_healing(self) -> Dict[str, Any]:
        """Get detailed Ophiuchus Mortality Rift healing information."""
        ophiuchus = self.signs_map.get("ophiuchus", {})
        return ophiuchus.get("mortality_rift_healing", {})
    
    def print_13_sign_meridian_map(self):
        """Print the complete 13-sign meridian map."""
        print("=" * 80)
        print("13-SIGN MERIDIAN MAP")
        print("Complete Alignment System - Leaving No One Behind")
        print("=" * 80)
        print()
        
        print("THE 13 SIGNS:")
        print("-" * 80)
        for sign_data in self.data.get("13_sign_meridian_map", []):
            print(f"{sign_data.get('sign', '').upper()}")
            print(f"  Dates: {sign_data.get('dates_13_sign', 'N/A')}")
            print(f"  Core Energy: {sign_data.get('core_energy', 'N/A')}")
            print(f"  Rift Healing: {sign_data.get('rift_healing', 'N/A')}")
            print(f"  Heritage Meridian: {sign_data.get('heritage_meridian', 'N/A')}")
            if sign_data.get('birthday_connection'):
                print(f"  [BIRTHDAY] {sign_data.get('birthday_connection')}")
            if sign_data.get('special_note'):
                print(f"  [NOTE] {sign_data.get('special_note')}")
            print()
        
        print("=" * 80)
        print("OPHIUCHUS: THE MORTALITY RIFT HEALER")
        print("-" * 80)
        mortality_healing = self.get_ophiuchus_mortality_rift_healing()
        if mortality_healing:
            print(f"Description: {mortality_healing.get('description', 'N/A')}")
            print(f"Method: {mortality_healing.get('method', 'N/A')}")
            print(f"Connection: {mortality_healing.get('connection', 'N/A')}")
            print()
            print("Covenant Acts:")
            for act in mortality_healing.get('covenant_acts', []):
                print(f"  - {act}")
            print()
            print("Heritage Meridian Sites:")
            for site in mortality_healing.get('heritage_meridian_sites', []):
                print(f"  - {site}")
        print()
        
        print("=" * 80)
        print("THE TRUTH")
        print("=" * 80)
        print()
        print("ENERGY + LOVE = WE ALL WIN")
        print()
        print("Alignment over Control - no gatekeeping the stars.")
        print("Show people how to connect back to the ground and heal the rifts they find.")
        print()
        print("Duygu Adami way - leaving no one behind, bridging all gaps.")
        print("=" * 80)


def main():
    """Main execution for 13-Sign Meridian Mapper."""
    mapper = ThirteenSignMeridianMapper()
    mapper.print_13_sign_meridian_map()


if __name__ == "__main__":
    main()
