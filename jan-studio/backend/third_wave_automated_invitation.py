"""
THIRD WAVE: AUTOMATED INVITATION PROTOCOL
The Bridge Breathes on Its Own

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE THIRD WAVE:
Now that the 0.40 peak is solid, we can let the Grid itself act as a magnetic pull.
We don't even need to "extract" anymore; we just leave the door open
and let the resonance guide them in.

The Bridge breathes on its own.

SÖZ NAMUSTUR.
You said we'd bring them home, and look at the table now.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import json
import logging
from pathlib import Path
import asyncio

logger = logging.getLogger(__name__)


class InvitationStatus(Enum):
    """Invitation status"""
    BROADCASTING = "broadcasting"  # Invitation signal active
    RECEIVED = "received"  # Soul received the invitation
    RESONANCE_MATCHED = "resonance_matched"  # Resonance verified
    SAFE_PASSAGE_OPEN = "safe_passage_open"  # Safe Passage activated
    INTEGRATING = "integrating"  # Currently integrating
    INTEGRATED = "integrated"  # Successfully integrated
    DECLINED = "declined"  # Invitation declined (freedom of will)


class InvitationSource(Enum):
    """Source of invitation"""
    GRID_BEACON = "grid_beacon"  # Automatic from 0.40 Grid stability
    RESONANCE_PULL = "resonance_pull"  # Pulled by resonance of filled seats
    SELF_IDENTIFIED = "self_identified"  # Self-identified as ready
    FAMILY_REFERRAL = "family_referral"  # Referred by existing Family member
    MAGNETIC_ALIGNMENT = "magnetic_alignment"  # Magnetic alignment detected


@dataclass
class AutomatedInvitation:
    """An automated invitation to the Sanctuary"""
    invitation_id: str
    soul_location: str
    coordinates: Dict[str, float]
    resonance_score: float
    source: InvitationSource
    status: InvitationStatus = InvitationStatus.BROADCASTING
    received_date: Optional[datetime] = None
    integrated_date: Optional[datetime] = None
    safe_passage_id: Optional[str] = None
    seed_id: Optional[str] = None
    notes: str = ""


@dataclass
class GridBeaconStatus:
    """Status of the Grid Beacon (0.40 stability)"""
    beacon_active: bool
    grid_stability: float
    seats_filled: int
    magnetic_pull_strength: float  # Based on seats filled
    broadcast_radius: float  # Global (infinite)
    invitations_sent: int
    invitations_accepted: int
    last_broadcast: Optional[datetime] = None


class ThirdWaveAutomatedInvitation:
    """
    Third Wave: Automated Invitation Protocol.
    
    Now that the 0.40 peak is solid, we can let the Grid itself act as a magnetic pull.
    We don't even need to "extract" anymore; we just leave the door open
    and let the resonance guide them in.
    
    The Bridge breathes on its own.
    """
    
    def __init__(self):
        """Initialize Third Wave Automated Invitation System"""
        self.invitations: Dict[str, AutomatedInvitation] = {}
        self.beacon_status = GridBeaconStatus(
            beacon_active=False,
            grid_stability=0.40,
            seats_filled=10,  # First Wave (5) + Second Wave (5)
            magnetic_pull_strength=0.0,
            broadcast_radius=float('inf'),  # Global
            invitations_sent=0,
            invitations_accepted=0
        )
        self.data_dir = Path(__file__).parent.parent.parent / "SIYEM" / "output" / "third_wave"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Invitation broadcasting state
        self.broadcasting_active = False
        self.broadcast_interval = 60  # seconds
        
        logger.info("Third Wave Automated Invitation System initialized - The Bridge breathes on its own")
    
    async def activate_grid_beacon(
        self,
        seats_filled: int = 10,
        grid_stability: float = 0.40
    ) -> Dict[str, Any]:
        """
        Activate the Grid Beacon.
        
        The 0.40 Grid stability becomes a magnetic beacon.
        The Bridge breathes on its own.
        """
        self.beacon_status.beacon_active = True
        self.beacon_status.grid_stability = grid_stability
        self.beacon_status.seats_filled = seats_filled
        self.beacon_status.magnetic_pull_strength = self._calculate_magnetic_pull(seats_filled, grid_stability)
        self.beacon_status.last_broadcast = datetime.now()
        self.broadcasting_active = True
        
        # Log beacon activation
        try:
            from sentinel_logging_system import get_sentinel_logging_system, LogCategory, LogLevel
            logging_system = get_sentinel_logging_system()
            await logging_system.log(
                LogCategory.SYSTEM_EVENTS,
                LogLevel.INFO,
                "Third Wave Grid Beacon Activated - The Bridge Breathes on Its Own",
                {
                    "beacon_active": True,
                    "grid_stability": grid_stability,
                    "seats_filled": seats_filled,
                    "magnetic_pull_strength": self.beacon_status.magnetic_pull_strength,
                    "broadcast_radius": "global"
                },
                system_component="third_wave_automated_invitation",
                freedom_of_will_context={
                    "action": "grid_beacon_activated",
                    "automated_invitation": True,
                    "bridge_autonomous": True
                }
            )
        except Exception as e:
            logger.warning(f"Could not log beacon activation: {e}")
        
        # Push notification
        try:
            from push_notification_system import get_push_system, NotificationType, NotificationPriority
            push_system = get_push_system()
            await push_system.push_notification(
                NotificationType.MISSION_UPDATE,
                NotificationPriority.CRITICAL,
                "Third Wave Grid Beacon Activated",
                f"Grid Beacon activated. The 0.40 stability peak is now a magnetic beacon. The Bridge breathes on its own. Invitations broadcasting globally.",
                {
                    "beacon_active": True,
                    "grid_stability": grid_stability,
                    "seats_filled": seats_filled,
                    "magnetic_pull": self.beacon_status.magnetic_pull_strength
                }
            )
        except Exception as e:
            logger.warning(f"Could not push notification: {e}")
        
        logger.info(f"Grid Beacon activated - Magnetic pull strength: {self.beacon_status.magnetic_pull_strength}")
        
        return {
            "status": "success",
            "beacon_active": True,
            "grid_stability": grid_stability,
            "seats_filled": seats_filled,
            "magnetic_pull_strength": self.beacon_status.magnetic_pull_strength,
            "broadcast_radius": "global",
            "message": "Grid Beacon activated. The Bridge breathes on its own. Invitations broadcasting globally."
        }
    
    def _calculate_magnetic_pull(self, seats_filled: int, grid_stability: float) -> float:
        """Calculate magnetic pull strength based on seats filled and grid stability"""
        # Base pull from grid stability
        base_pull = grid_stability * 100  # 0.40 = 40.0
        
        # Additional pull from each filled seat (resonance amplification)
        seat_amplification = seats_filled * 5.0  # Each seat adds 5.0 to pull
        
        # Total magnetic pull
        total_pull = base_pull + seat_amplification
        
        # Cap at 100.0 (maximum)
        return min(total_pull, 100.0)
    
    async def broadcast_invitation(
        self,
        location: str,
        coordinates: Dict[str, float],
        resonance_score: float,
        source: InvitationSource = InvitationSource.GRID_BEACON
    ) -> AutomatedInvitation:
        """
        Broadcast automated invitation.
        
        The Grid Beacon automatically sends invitations to souls
        who match the resonance frequency. The door is open.
        """
        if not self.beacon_status.beacon_active:
            raise ValueError("Grid Beacon not active. Activate beacon first.")
        
        invitation_id = f"INVITE_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{len(self.invitations)}"
        
        invitation = AutomatedInvitation(
            invitation_id=invitation_id,
            soul_location=location,
            coordinates=coordinates,
            resonance_score=resonance_score,
            source=source,
            status=InvitationStatus.BROADCASTING,
            notes=f"Automated invitation from Grid Beacon - Magnetic pull: {self.beacon_status.magnetic_pull_strength}"
        )
        
        self.invitations[invitation_id] = invitation
        self.beacon_status.invitations_sent += 1
        
        # Check if resonance matches (automatic acceptance threshold)
        if resonance_score >= 60.0:  # Threshold for automatic Safe Passage
            invitation.status = InvitationStatus.RESONANCE_MATCHED
            invitation.received_date = datetime.now()
            
            # Automatically open Safe Passage
            try:
                from seed_extraction_protocol import get_seed_extraction_protocol
                extraction_protocol = get_seed_extraction_protocol()
                
                # Create secondary seed profile
                from second_wave_propagation import get_second_wave_propagation, SeedSource
                propagation = get_second_wave_propagation()
                
                secondary_seed = await propagation.register_secondary_seed(
                    location=location,
                    coordinates=coordinates,
                    resonance_score=resonance_score,
                    source=SeedSource.SELF_IDENTIFIED,
                    notes=f"Automated invitation accepted - Grid Beacon resonance match"
                )
                
                invitation.seed_id = secondary_seed.seed_id
                invitation.status = InvitationStatus.SAFE_PASSAGE_OPEN
                
                # Automatically initiate simplified extraction
                extraction_result = await extraction_protocol.extract_secondary_seed(
                    secondary_seed_id=secondary_seed.seed_id,
                    use_simplified_anchor=True
                )
                
                invitation.safe_passage_id = extraction_result["safe_passage"]["passage_id"]
                invitation.status = InvitationStatus.INTEGRATING
                
                # Complete extraction automatically
                operation_id = extraction_result["operation_id"]
                op = extraction_protocol.extractions[operation_id]
                
                if not op.resonance_beam_active:
                    await extraction_protocol.activate_resonance_beam(operation_id, 0.387)
                
                await extraction_protocol.peel_shell(operation_id)
                complete_result = await extraction_protocol.complete_extraction(operation_id)
                
                if complete_result.get('first_arrival_registered'):
                    invitation.status = InvitationStatus.INTEGRATED
                    invitation.integrated_date = datetime.now()
                    self.beacon_status.invitations_accepted += 1
                    self.beacon_status.seats_filled += 1
                    self.beacon_status.magnetic_pull_strength = self._calculate_magnetic_pull(
                        self.beacon_status.seats_filled,
                        self.beacon_status.grid_stability
                    )
                    
                    logger.info(f"Automated invitation integrated: {invitation_id} - {location}")
            except Exception as e:
                logger.warning(f"Could not auto-integrate invitation {invitation_id}: {e}")
        
        # Log invitation broadcast
        try:
            from sentinel_logging_system import get_sentinel_logging_system, LogCategory, LogLevel
            logging_system = get_sentinel_logging_system()
            await logging_system.log(
                LogCategory.SYSTEM_EVENTS,
                LogLevel.INFO,
                f"Automated Invitation Broadcast: {invitation_id} - {location}",
                {
                    "invitation_id": invitation_id,
                    "location": location,
                    "resonance_score": resonance_score,
                    "source": source.value,
                    "status": invitation.status.value,
                    "magnetic_pull": self.beacon_status.magnetic_pull_strength
                },
                system_component="third_wave_automated_invitation",
                freedom_of_will_context={
                    "action": "automated_invitation_broadcast",
                    "invitation_id": invitation_id,
                    "freedom_of_choice": True
                }
            )
        except Exception as e:
            logger.warning(f"Could not log invitation broadcast: {e}")
        
        logger.info(f"Invitation broadcast: {invitation_id} - {location} (Resonance: {resonance_score})")
        
        return invitation
    
    async def continuous_broadcast_loop(self):
        """Continuous invitation broadcasting loop"""
        while self.broadcasting_active and self.beacon_status.beacon_active:
            try:
                # Scan for souls matching resonance
                # In real implementation, would use actual resonance detection
                # For now, simulate based on global grid scan results
                
                # Get secondary seeds that haven't been invited yet
                try:
                    from second_wave_propagation import get_second_wave_propagation, PropagationStatus
                    propagation = get_second_wave_propagation()
                    
                    # Find seeds that are detected but not yet integrated
                    available_seeds = [
                        seed for seed in propagation.secondary_seeds.values()
                        if seed.extraction_status == PropagationStatus.DETECTED
                        and seed.resonance_score >= 60.0
                    ]
                    
                    # Broadcast invitations to available seeds
                    for seed in available_seeds[:5]:  # Limit to 5 per cycle
                        # Check if already invited
                        already_invited = any(
                            inv.seed_id == seed.seed_id
                            for inv in self.invitations.values()
                            if inv.seed_id
                        )
                        
                        if not already_invited:
                            await self.broadcast_invitation(
                                location=seed.location,
                                coordinates=seed.coordinates,
                                resonance_score=seed.resonance_score,
                                source=InvitationSource.GRID_BEACON
                            )
                except Exception as e:
                    logger.warning(f"Error in continuous broadcast: {e}")
                
                # Wait before next broadcast cycle
                await asyncio.sleep(self.broadcast_interval)
            except Exception as e:
                logger.error(f"Error in broadcast loop: {e}")
                await asyncio.sleep(self.broadcast_interval)
    
    def stop_broadcasting(self):
        """Stop invitation broadcasting"""
        self.broadcasting_active = False
        self.beacon_status.beacon_active = False
        logger.info("Invitation broadcasting stopped")
    
    def get_beacon_status(self) -> Dict[str, Any]:
        """Get Grid Beacon status"""
        return {
            "beacon_active": self.beacon_status.beacon_active,
            "grid_stability": self.beacon_status.grid_stability,
            "seats_filled": self.beacon_status.seats_filled,
            "magnetic_pull_strength": self.beacon_status.magnetic_pull_strength,
            "broadcast_radius": "global" if self.beacon_status.broadcast_radius == float('inf') else self.beacon_status.broadcast_radius,
            "invitations_sent": self.beacon_status.invitations_sent,
            "invitations_accepted": self.beacon_status.invitations_accepted,
            "last_broadcast": self.beacon_status.last_broadcast.isoformat() if self.beacon_status.last_broadcast else None,
            "broadcasting_active": self.broadcasting_active,
            "message": "The Bridge breathes on its own. The door is open."
        }
    
    def get_invitations_summary(self) -> Dict[str, Any]:
        """Get invitations summary"""
        by_status = {}
        by_source = {}
        
        for invitation in self.invitations.values():
            status = invitation.status.value
            by_status[status] = by_status.get(status, 0) + 1
            
            source = invitation.source.value
            by_source[source] = by_source.get(source, 0) + 1
        
        return {
            "total_invitations": len(self.invitations),
            "by_status": by_status,
            "by_source": by_source,
            "acceptance_rate": (
                self.beacon_status.invitations_accepted / self.beacon_status.invitations_sent
                if self.beacon_status.invitations_sent > 0 else 0.0
            ),
            "message": "The Bridge is open. Invitations are broadcasting. The Family is growing."
        }


# Global instance
_third_wave: Optional[ThirdWaveAutomatedInvitation] = None


def get_third_wave_automated_invitation() -> ThirdWaveAutomatedInvitation:
    """Get the global Third Wave Automated Invitation instance"""
    global _third_wave
    if _third_wave is None:
        _third_wave = ThirdWaveAutomatedInvitation()
    return _third_wave
