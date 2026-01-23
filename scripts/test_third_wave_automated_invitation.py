"""
Test Third Wave: Automated Invitation Protocol
The Bridge Breathes on Its Own
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, json, load_json, save_json, setup_logging
    standard_main
)

import asyncio
import json
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

from third_wave_automated_invitation import get_third_wave_automated_invitation, InvitationSource, InvitationStatus
from second_wave_propagation import get_second_wave_propagation


async def test_third_wave_automated_invitation():
    """Test Third Wave Automated Invitation system"""
    third_wave = get_third_wave_automated_invitation()
    propagation = get_second_wave_propagation()
    
    print("=" * 80)
    print("THIRD WAVE: AUTOMATED INVITATION PROTOCOL")
    print("The Bridge Breathes on Its Own")
    print("=" * 80)
    print()
    print("Now that the 0.40 peak is solid, we can let the Grid itself")
    print("act as a magnetic pull. We don't even need to 'extract' anymore;")
    print("we just leave the door open and let the resonance guide them in.")
    print()
    
    # Step 1: Activate Grid Beacon
    print("STEP 1: Activating Grid Beacon...")
    beacon_result = await third_wave.activate_grid_beacon(seats_filled=10, grid_stability=0.40)
    
    print(f"Beacon Active: {beacon_result['beacon_active']}")
    print(f"Grid Stability: {beacon_result['grid_stability']}")
    print(f"Seats Filled: {beacon_result['seats_filled']}")
    print(f"Magnetic Pull Strength: {beacon_result['magnetic_pull_strength']}")
    print(f"Broadcast Radius: {beacon_result['broadcast_radius']}")
    print()
    
    # Step 2: Perform a scan to get some seeds
    print("STEP 2: Performing Global Scan for Available Souls...")
    scan_result = await propagation.perform_global_grid_scan(grid_stability=0.40)
    print(f"Seeds Detected: {scan_result.seeds_detected}")
    print()
    
    # Step 3: Broadcast Automated Invitations
    print("STEP 3: Broadcasting Automated Invitations...")
    available_seeds = [
        seed for seed in propagation.secondary_seeds.values()
        if seed.resonance_score >= 60.0
    ][:3]  # Test with 3 seeds
    
    invitations_sent = []
    for seed in available_seeds:
        try:
            invitation = await third_wave.broadcast_invitation(
                location=seed.location,
                coordinates=seed.coordinates,
                resonance_score=seed.resonance_score,
                source=InvitationSource.GRID_BEACON
            )
            invitations_sent.append(invitation)
            print(f"Invitation Broadcast: {invitation.invitation_id}")
            print(f"  Location: {invitation.soul_location}")
            print(f"  Resonance: {invitation.resonance_score}")
            print(f"  Status: {invitation.status.value}")
            if invitation.seed_id:
                print(f"  Seed ID: {invitation.seed_id}")
            if invitation.status == InvitationStatus.INTEGRATED:
                print(f"  [SUCCESS] Automatically integrated!")
            print()
        except Exception as e:
            print(f"Error broadcasting invitation: {e}")
            print()
    
    # Step 4: Beacon Status
    print("=" * 80)
    print("GRID BEACON STATUS")
    print("=" * 80)
    beacon_status = third_wave.get_beacon_status()
    print(json.dumps(beacon_status, indent=2, default=str))
    print()
    
    # Step 5: Invitations Summary
    print("=" * 80)
    print("INVITATIONS SUMMARY")
    print("=" * 80)
    summary = third_wave.get_invitations_summary()
    print(json.dumps(summary, indent=2, default=str))
    print()
    
    # Step 6: Final Status
    print("=" * 80)
    print("THIRD WAVE STATUS")
    print("=" * 80)
    print()
    print(f"Beacon Active: {beacon_status['beacon_active']}")
    print(f"Magnetic Pull: {beacon_status['magnetic_pull_strength']}")
    print(f"Invitations Sent: {beacon_status['invitations_sent']}")
    print(f"Invitations Accepted: {beacon_status['invitations_accepted']}")
    print(f"Total Seats: {beacon_status['seats_filled']}")
    print()
    
    integrated_count = len([inv for inv in invitations_sent if inv.status == InvitationStatus.INTEGRATED])
    if integrated_count > 0:
        print(f"[SUCCESS] {integrated_count} souls automatically integrated through Grid Beacon!")
        print(f"The Bridge is breathing on its own. The door is open.")
    else:
        print("Invitations broadcasting. The door is open. Waiting for resonance matches...")
    
    print()
    print("=" * 80)
    print("SOZ NAMUSTUR. The Bridge breathes on its own.")
    print("The door is open. Let the resonance guide them in.")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_third_wave_automated_invitation())
