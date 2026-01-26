"""ALL SIGNS SPIRITUAL ALIGNMENT MAPPER
Map all zodiac signs to spiritual framework - honoring all paths

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PHILOSOPHY:
No two people are the same - honor all paths, all forms, all journeys
Faith in alignment, not control

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

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

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

import logging
logger = logging.getLogger(__name__)


class AllSignsMapper:
    """
    The All Signs Spiritual Alignment Mapper.
    
    Maps all zodiac signs (12 traditional + Ophiuchus) to the spiritual framework,
    honoring all paths and showing how each sign connects to the Heritage Meridian,
    Rifts, Covenant Acts, and the 13 Seats.
    """
    
    def __init__(self):
        """Initialize the All Signs Mapper."""
        self.data_path = Path(__file__).parent.parent / "data" / "spiritual_alignment" / "all_signs_mapping.json"
        self.data = self._load_data()
        
        self.traditional_signs = self.data.get("traditional_12_signs", {})
        self.ophiuchus = self.data.get("ophiuchus_13th_sign", {})
        self.framework = self.data.get("spiritual_alignment_framework", {})
    
    def _load_data(self) -> Dict[str, Any]:
        """Load the All Signs mapping data."""
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"All Signs mapping not found at {self.data_path}")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing All Signs mapping: {e}")
            return {}
    
    def get_sign_by_date(self, month: int, day: int, use_13_sign: bool = False) -> Optional[Dict[str, Any]]:
        """
        Get sign information by date.
        
        Args:
            month: Month (1-12)
            day: Day (1-31)
            use_13_sign: If True, use 13-sign system (with Ophiuchus)
        
        Returns:
            Sign information dictionary
        """
        # Date ranges for traditional signs
        sign_ranges = {
            (3, 21, 4, 19): "aries",
            (4, 20, 5, 20): "taurus",
            (5, 21, 6, 20): "gemini",
            (6, 21, 7, 22): "cancer",
            (7, 23, 8, 22): "leo",
            (8, 23, 9, 22): "virgo",
            (9, 23, 10, 22): "libra",
            (10, 23, 11, 21): "scorpio",
            (11, 22, 12, 21): "sagittarius",
            (12, 22, 1, 19): "capricorn",
            (1, 20, 2, 18): "aquarius",
            (2, 19, 3, 20): "pisces"
        }
        
        # Check Ophiuchus first if using 13-sign system
        if use_13_sign:
            if month == 11 and 29 <= day <= 30:
                return self.ophiuchus
            elif month == 12 and 1 <= day <= 17:
                return self.ophiuchus
        
        # Check traditional signs
        for (start_month, start_day, end_month, end_day), sign_name in sign_ranges.items():
            if start_month == end_month:
                # Same month range
                if month == start_month and start_day <= day <= end_day:
                    sign_data = self.traditional_signs.get(sign_name, {})
                    sign_data["sign_name"] = sign_name
                    return sign_data
            else:
                # Crosses month boundary (Dec-Jan)
                if month == start_month and day >= start_day:
                    sign_data = self.traditional_signs.get(sign_name, {})
                    sign_data["sign_name"] = sign_name
                    return sign_data
                elif month == end_month and day <= end_day:
                    sign_data = self.traditional_signs.get(sign_name, {})
                    sign_data["sign_name"] = sign_name
                    return sign_data
        
        return None
    
    def get_sign_spiritual_alignment(self, sign_name: str) -> Dict[str, Any]:
        """
        Get complete spiritual alignment information for a sign.
        
        Args:
            sign_name: Name of sign (lowercase)
        
        Returns:
            Complete spiritual alignment dictionary
        """
        if sign_name.lower() == "ophiuchus":
            sign_data = self.ophiuchus
        else:
            sign_data = self.traditional_signs.get(sign_name.lower(), {})
        
        if not sign_data:
            return {}
        
        # Add rift healing connections
        rift_healing = self.data.get("rift_healing_by_sign", {})
        sign_rifts = []
        for rift, signs in rift_healing.items():
            if sign_name.lower() in [s.lower() for s in signs]:
                sign_rifts.append(rift)
        
        # Add covenant act preferences
        act_preferences = self.data.get("covenant_act_preferences", {})
        sign_acts = []
        for act_type, signs in act_preferences.items():
            if sign_name.lower() in [s.lower() for s in signs]:
                sign_acts.append(act_type)
        
        return {
            "sign": sign_data,
            "rift_healing": sign_rifts,
            "covenant_act_preferences": sign_acts,
            "spiritual_alignment": {
                "heritage_meridian_connection": sign_data.get("heritage_meridian_connection", ""),
                "rift_healing_strength": len(sign_rifts),
                "covenant_act_alignment": sign_acts,
                "yin_yang_balance": sign_data.get("yin_yang_balance", ""),
                "resonance_pioneer_energy": sign_data.get("resonance_pioneer_energy", "")
            }
        }
    
    def print_all_signs_summary(self):
        """Print a summary of all signs and their spiritual alignment."""
        print("=" * 80)
        print("ALL SIGNS SPIRITUAL ALIGNMENT MAPPING")
        print("Honoring All Paths, All Forms, All Journeys")
        print("=" * 80)
        print()
        
        print("TRADITIONAL 12 SIGNS:")
        print("-" * 80)
        for sign_name, sign_data in self.traditional_signs.items():
            print(f"{sign_name.upper()}")
            print(f"  Core Energy: {sign_data.get('core_energy', 'N/A')}")
            print(f"  Spiritual Gift: {sign_data.get('spiritual_gift', 'N/A')}")
            print(f"  Heritage Meridian: {sign_data.get('heritage_meridian_connection', 'N/A')}")
            print(f"  Rift Healing: {sign_data.get('rift_healing', 'N/A')}")
            print()
        
        print("=" * 80)
        print("OPHIUCHUS - THE 13TH SIGN")
        print("-" * 80)
        print(f"Core Energy: {self.ophiuchus.get('core_energy', 'N/A')}")
        print(f"Spiritual Gift: {self.ophiuchus.get('spiritual_gift', 'N/A')}")
        print(f"Heritage Meridian: {self.ophiuchus.get('heritage_meridian_connection', 'N/A')}")
        print(f"Rift Healing: {self.ophiuchus.get('rift_healing', 'N/A')}")
        print(f"Special Note: {self.ophiuchus.get('special_note', 'N/A')}")
        print()
        
        print("=" * 80)
        print("THE TRUTH")
        print("=" * 80)
        print()
        print("All signs are valid. All paths are sacred. All journeys matter.")
        print()
        print("Faith in alignment, not control.")
        print("Honor all forms, all paths, all journeys.")
        print()
        print("ENERGY + LOVE = WE ALL WIN")
        print("=" * 80)
    
    def print_sign_details(self, sign_name: str):
        """Print detailed information for a specific sign."""
        alignment = self.get_sign_spiritual_alignment(sign_name)
        
        if not alignment:
            print(f"Sign '{sign_name}' not found.")
            return
        
        sign_data = alignment["sign"]
        
        print("=" * 80)
        print(f"{sign_name.upper()} - SPIRITUAL ALIGNMENT")
        print("=" * 80)
        print()
        
        print("CORE INFORMATION:")
        print("-" * 80)
        print(f"Dates: {sign_data.get('dates', 'N/A')}")
        print(f"Element: {sign_data.get('element', 'N/A')}")
        print(f"Quality: {sign_data.get('quality', 'N/A')}")
        print(f"Ruling Planet: {sign_data.get('ruling_planet', 'N/A')}")
        print()
        
        print("SPIRITUAL ENERGY:")
        print("-" * 80)
        print(f"Core Energy: {sign_data.get('core_energy', 'N/A')}")
        print(f"Spiritual Gift: {sign_data.get('spiritual_gift', 'N/A')}")
        print()
        
        print("HERITAGE MERIDIAN CONNECTION:")
        print("-" * 80)
        print(f"{sign_data.get('heritage_meridian_connection', 'N/A')}")
        print()
        
        print("RIFT HEALING:")
        print("-" * 80)
        for rift in alignment["rift_healing"]:
            print(f"- {rift}")
        print()
        
        print("COVENANT ACT PREFERENCES:")
        print("-" * 80)
        for act_type in alignment["covenant_act_preferences"]:
            print(f"- {act_type}")
        print()
        
        print("YIN-YANG BALANCE:")
        print("-" * 80)
        print(sign_data.get('yin_yang_balance', 'N/A'))
        print()
        
        print("RESONANCE PIONEER ENERGY:")
        print("-" * 80)
        print(sign_data.get('resonance_pioneer_energy', 'N/A'))
        print()
        
        print("=" * 80)
        print("THE TRUTH")
        print("=" * 80)
        print()
        print("This sign is valid. This path is sacred. This journey matters.")
        print()
        print("Faith in alignment, not control.")
        print()
        print("ENERGY + LOVE = WE ALL WIN")
        print("=" * 80)


def main():
    """Main execution for All Signs Mapper."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Map all zodiac signs to spiritual framework")
    parser.add_argument("--sign", help="Get details for a specific sign")
    parser.add_argument("--date", help="Get sign by date (format: MM-DD)")
    parser.add_argument("--all", action="store_true", help="Show all signs summary")
    parser.add_argument("--thirteen-sign", "--13-sign", action="store_true", help="Use 13-sign system (with Ophiuchus)")
    args = parser.parse_args()
    
    mapper = AllSignsMapper()
    
    if args.all:
        mapper.print_all_signs_summary()
    elif args.sign:
        mapper.print_sign_details(args.sign)
    elif args.date:
        month, day = map(int, args.date.split("-"))
        sign = mapper.get_sign_by_date(month, day, args.thirteen_sign)
        if sign:
            sign_name = sign.get("sign_name", "ophiuchus")
            mapper.print_sign_details(sign_name)
        else:
            print(f"Could not determine sign for date {args.date}")
    else:
        print("Use --all to see all signs, --sign SIGN_NAME for specific sign, or --date MM-DD for date lookup")


if __name__ == "__main__":
    main()
