"""
Resonance Check: Analyze Seat Activation Status and Resonance Levels
Tool for checking the energy and readiness of Seats before activation
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, json, load_json, save_json, setup_logging
    standard_main
)

import sys
from pathlib import Path
import json

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))
from round1_activation_logger import Round1ActivationLogger

def load_heritage_data():
    """Load heritage meridian data to get Seat information"""
    data_path = Path(__file__).parent.parent / 'data' / 'heritage_meridian' / 'heritage_meridian_data.json'
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def check_seat_resonance(seat_id, logger, heritage_data):
    """Check the resonance level and activation status of a specific seat"""
    
    # Get seat info from heritage data
    seats = heritage_data.get('the_13_seats', {}).get('seats', [])
    seat_info = next((s for s in seats if s.get('seat_id') == seat_id), None)
    
    if not seat_info:
        return None
    
    # Get activation status from logger
    seat_data = logger.get_seat_status(seat_id)
    
    # Calculate resonance metrics
    activations = seat_data.get('activations', [])
    unity_contributed = seat_data.get('unity_contributed', 0.0)
    activation_count = len(activations)
    
    # Resonance level calculation
    # Base resonance: 0.0 (dormant) to 1.0 (fully activated)
    # Factors: activation count, unity contributed, phase-locked status
    
    base_resonance = min(activation_count * 0.2, 0.6)  # Up to 0.6 from activations
    unity_resonance = min(unity_contributed * 10, 0.4)  # Up to 0.4 from unity
    total_resonance = min(base_resonance + unity_resonance, 1.0)
    
    # Check if phase-locked (Giza, Stonehenge, Angkor)
    phase_locked_seats = ['seat_02', 'seat_03', 'seat_04']  # Giza, Stonehenge, Angkor
    is_phase_locked = seat_id in phase_locked_seats
    
    # Resonance status
    if total_resonance >= 0.8:
        status_level = "HIGH"
        status_emoji = "[HIGH]"
    elif total_resonance >= 0.5:
        status_level = "MEDIUM"
        status_emoji = "[MEDIUM]"
    elif total_resonance >= 0.2:
        status_level = "LOW"
        status_emoji = "[LOW]"
    else:
        status_level = "DORMANT"
        status_emoji = "[DORMANT]"
    
    return {
        'seat_info': seat_info,
        'activation_count': activation_count,
        'unity_contributed': unity_contributed,
        'total_resonance': total_resonance,
        'status_level': status_level,
        'status_emoji': status_emoji,
        'is_phase_locked': is_phase_locked,
        'activations': activations
    }

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Check resonance level of a Seat')
    parser.add_argument('--seat', type=str, help='Seat ID (e.g., seat_02 for Giza)')
    parser.add_argument('--all', action='store_true', help='Check all Seats')
    args = parser.parse_args()
    
    logger = Round1ActivationLogger()
    heritage_data = load_heritage_data()
    
    print("=" * 80)
    print("RESONANCE CHECK")
    print("Seat Activation Status and Energy Levels")
    print("=" * 80)
    print()
    
    if args.all:
        # Check all seats
        seats = heritage_data.get('the_13_seats', {}).get('seats', [])
        results = []
        
        # Get all seat statuses
        all_seat_status = logger.get_seat_status()
        all_seats_data = all_seat_status.get('seats', {})
        
        for seat in seats:
            seat_id = seat.get('seat_id')
            # Get seat data from logger
            seat_data = all_seats_data.get(seat_id, {})
            resonance = check_seat_resonance(seat_id, logger, heritage_data)
            if resonance:
                results.append((seat_id, resonance))
        
        # Sort by resonance level (highest first)
        results.sort(key=lambda x: x[1]['total_resonance'], reverse=True)
        
        print("ALL SEATS RESONANCE STATUS:")
        print()
        for seat_id, resonance in results:
            seat_info = resonance['seat_info']
            print(f"{resonance['status_emoji']} {seat_info['name']} ({seat_id})")
            print(f"   Resonance: {resonance['total_resonance']:.1%}")
            print(f"   Activations: {resonance['activation_count']}")
            print(f"   Unity Contributed: +{resonance['unity_contributed']:.4f}")
            if resonance['is_phase_locked']:
                print(f"   Status: PHASE-LOCKED (High Priority)")
            print()
        
        # Summary
        high_resonance = [r for _, r in results if r['total_resonance'] >= 0.5]
        dormant = [r for _, r in results if r['total_resonance'] < 0.2]
        
        print("=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print(f"High Resonance Seats: {len(high_resonance)}")
        print(f"Dormant Seats: {len(dormant)}")
        print(f"Total Seats: {len(results)}")
        print()
        
        if dormant:
            print("RECOMMENDED FOR ACTIVATION:")
            for seat_id, resonance in results:
                if resonance['total_resonance'] < 0.2 and resonance['is_phase_locked']:
                    seat_info = resonance['seat_info']
                    print(f"  - {seat_info['name']} ({seat_id}) - PHASE-LOCKED, needs activation")
            for seat_id, resonance in results:
                if resonance['total_resonance'] < 0.2 and not resonance['is_phase_locked']:
                    seat_info = resonance['seat_info']
                    print(f"  - {seat_info['name']} ({seat_id}) - Dormant, ready for activation")
        
    elif args.seat:
        # Check specific seat
        resonance = check_seat_resonance(args.seat, logger, heritage_data)
        
        if not resonance:
            print(f"ERROR: Seat {args.seat} not found")
            return
        
        seat_info = resonance['seat_info']
        
        print(f"SEAT: {seat_info['name']} ({args.seat})")
        print(f"Location: {seat_info.get('coordinates', {})}")
        print(f"Function: {seat_info.get('function', 'N/A')}")
        print()
        print("RESONANCE STATUS:")
        print(f"  Level: {resonance['status_level']} ({resonance['status_emoji']})")
        print(f"  Resonance: {resonance['total_resonance']:.1%}")
        print(f"  Activations: {resonance['activation_count']}")
        print(f"  Unity Contributed: +{resonance['unity_contributed']:.4f}")
        if resonance['is_phase_locked']:
            print(f"  Status: PHASE-LOCKED (High Priority for activation)")
        print()
        
        if resonance['activations']:
            print("RECENT ACTIVATIONS:")
            for act_id in resonance['activations'][-5:]:  # Last 5
                print(f"  - {act_id}")
        else:
            print("No activations yet - Seat is dormant")
        
        print()
        print("=" * 80)
        print("RECOMMENDATION")
        print("=" * 80)
        
        if resonance['total_resonance'] < 0.2:
            if resonance['is_phase_locked']:
                print("HIGH PRIORITY: Phase-Locked Seat needs activation")
                print("Recommended: Meridian Activated or Rift Healed act")
            else:
                print("READY FOR ACTIVATION: Seat is dormant, ready for connection")
                print("Recommended: Bridge Built or Shared Table act")
        elif resonance['total_resonance'] < 0.5:
            print("MODERATE RESONANCE: Seat is active but could use amplification")
            print("Recommended: Additional acts to boost resonance")
        else:
            print("HIGH RESONANCE: Seat is well-activated")
            print("Consider: Focusing on other dormant seats")
        
    else:
        print("ERROR: Please specify --seat <seat_id> or --all")
        print()
        print("Examples:")
        print("  python resonance_check.py --seat seat_02  # Check Giza")
        print("  python resonance_check.py --seat seat_07  # Check Berengaria")
        print("  python resonance_check.py --all           # Check all seats")
    
    print()
    print("=" * 80)
    print("THE TRUTH")
    print("=" * 80)
    print()
    print("ENERGY + LOVE = UNITY = PEACE = WE ALL WIN")
    print()
    print("Every Seat matters.")
    print("Every activation matters.")
    print("Every breath matters.")
    print()
    print("=" * 80)

if __name__ == '__main__':
    main()
