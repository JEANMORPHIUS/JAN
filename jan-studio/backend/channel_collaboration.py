"""
CHANNEL COLLABORATION SYSTEM
Full Collaboration Across All Channels

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PRESENT PURPOSE:
PROFESSIONAL / PI / EDUCATION should be our present purpose to start from.

We must be FULLY COLLABORATIVE across all channels.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import json
import logging

logger = logging.getLogger(__name__)


class ChannelType(Enum):
    """Types of channels"""
    PROFESSIONAL = "professional"  # Professional services, business, career
    PI = "pi"  # Private Investigation / Personal Intelligence
    EDUCATION = "education"  # Educational services, learning, teaching
    CREATIVE = "creative"  # Creative expression, art, music
    SPIRITUAL = "spiritual"  # Spiritual alignment, connection ritual
    FINANCIAL = "financial"  # Financial systems, dirty money cleaning
    COMMUNITY = "community"  # Community building, stewardship
    ALL = "all"  # All channels


class CollaborationStatus(Enum):
    """Status of collaboration"""
    FULLY_COLLABORATIVE = "fully_collaborative"  # Full integration
    PARTIALLY_COLLABORATIVE = "partially_collaborative"  # Some integration
    NOT_COLLABORATIVE = "not_collaborative"  # No integration
    UNKNOWN = "unknown"  # Status unknown


@dataclass
class Channel:
    """A channel in the system"""
    channel_type: ChannelType
    name: str
    description: str
    is_present_purpose: bool = False  # Is this part of present purpose?
    systems: List[str] = field(default_factory=list)  # Systems in this channel
    api_endpoints: List[str] = field(default_factory=list)  # API endpoints
    integrations: List[str] = field(default_factory=list)  # Integrated channels
    collaboration_status: CollaborationStatus = CollaborationStatus.UNKNOWN
    last_updated: datetime = field(default_factory=datetime.now)


@dataclass
class ChannelCollaboration:
    """Collaboration between channels"""
    channel1: ChannelType
    channel2: ChannelType
    collaboration_level: float = 0.0  # 0-100
    integration_points: List[str] = field(default_factory=list)
    shared_systems: List[str] = field(default_factory=list)
    shared_data: List[str] = field(default_factory=list)
    status: CollaborationStatus = CollaborationStatus.UNKNOWN
    last_checked: datetime = field(default_factory=datetime.now)


class ChannelCollaborationSystem:
    """
    System for managing full collaboration across all channels.
    
    PRESENT PURPOSE:
    PROFESSIONAL / PI / EDUCATION should be our present purpose to start from.
    """
    
    def __init__(self):
        """Initialize channel collaboration system"""
        self.present_purpose_channels = [
            ChannelType.PROFESSIONAL,
            ChannelType.PI,
            ChannelType.EDUCATION
        ]
        
        self.channels: Dict[ChannelType, Channel] = {
            ChannelType.PROFESSIONAL: Channel(
                channel_type=ChannelType.PROFESSIONAL,
                name="Professional",
                description="Professional services, business, career development",
                is_present_purpose=True,
                systems=[
                    "marketplace_api",
                    "unified_api",
                    "care_package_system",
                    "educational_api",  # Shared with Education
                    "heritage_api",  # Shared with PI
                    "spirit_alignment"  # Shared with PI
                ],
                api_endpoints=[
                    "/api/marketplace",
                    "/api/unified",
                    "/api/care-package",
                    "/api/educational",  # Shared with Education
                    "/api/heritage",  # Shared with PI
                    "/api/spirit-alignment"  # Shared with PI
                ],
                integrations=[ChannelType.PI.value, ChannelType.EDUCATION.value]
            ),
            ChannelType.PI: Channel(
                channel_type=ChannelType.PI,
                name="PI (Private Investigation / Personal Intelligence)",
                description="Private investigation, personal intelligence, research",
                is_present_purpose=True,
                systems=[
                    "heritage_api",
                    "racon_registry",
                    "connection_ritual",
                    "spirit_alignment",
                    "care_package_system",  # Shared with Professional
                    "educational_api"  # Shared with Education
                ],
                api_endpoints=[
                    "/api/heritage",
                    "/api/racon",
                    "/api/connection-ritual",
                    "/api/spirit-alignment",
                    "/api/care-package",  # Shared with Professional
                    "/api/educational"  # Shared with Education
                ],
                integrations=[ChannelType.PROFESSIONAL.value, ChannelType.EDUCATION.value]
            ),
            ChannelType.EDUCATION: Channel(
                channel_type=ChannelType.EDUCATION,
                name="Education",
                description="Educational services, learning, teaching",
                is_present_purpose=True,
                systems=[
                    "educational_api",
                    "care_package_system",
                    "yin_yang_symbiosis",
                    "heritage_api",  # Shared with PI
                    "spirit_alignment",  # Shared with PI
                    "unified_api"  # Shared with Professional
                ],
                api_endpoints=[
                    "/api/educational",
                    "/api/care-package",
                    "/api/yin-yang",
                    "/api/heritage",  # Shared with PI
                    "/api/spirit-alignment",  # Shared with PI
                    "/api/unified"  # Shared with Professional
                ],
                integrations=[ChannelType.PROFESSIONAL.value, ChannelType.PI.value]
            ),
            ChannelType.CREATIVE: Channel(
                channel_type=ChannelType.CREATIVE,
                name="Creative",
                description="Creative expression, art, music",
                is_present_purpose=False,
                systems=[
                    "jan_generation_api",
                    "jan_templates_api"
                ],
                api_endpoints=[
                    "/api/generation",
                    "/api/templates"
                ],
                integrations=[ChannelType.EDUCATION.value]
            ),
            ChannelType.SPIRITUAL: Channel(
                channel_type=ChannelType.SPIRITUAL,
                name="Spiritual",
                description="Spiritual alignment, connection ritual",
                is_present_purpose=False,
                systems=[
                    "connection_ritual",
                    "vibration_map",
                    "spirit_alignment"
                ],
                api_endpoints=[
                    "/api/connection-ritual",
                    "/api/vibration-map",
                    "/api/spirit-alignment"
                ],
                integrations=[ChannelType.PI.value, ChannelType.EDUCATION.value]
            ),
            ChannelType.FINANCIAL: Channel(
                channel_type=ChannelType.FINANCIAL,
                name="Financial",
                description="Financial systems, dirty money cleaning",
                is_present_purpose=False,
                systems=[
                    "dirty_money_cleaning",
                    "care_package_system"
                ],
                api_endpoints=[
                    "/api/dirty-money-cleaning",
                    "/api/care-package"
                ],
                integrations=[ChannelType.PROFESSIONAL.value]
            ),
            ChannelType.COMMUNITY: Channel(
                channel_type=ChannelType.COMMUNITY,
                name="Community",
                description="Community building, stewardship",
                is_present_purpose=False,
                systems=[
                    "care_package_system",
                    "yin_yang_symbiosis",
                    "industry_explorer"
                ],
                api_endpoints=[
                    "/api/care-package",
                    "/api/yin-yang",
                    "/api/industry-explorer"
                ],
                integrations=[ChannelType.PROFESSIONAL.value, ChannelType.EDUCATION.value]
            )
        }
        
        self.collaborations: Dict[str, ChannelCollaboration] = {}
    
    def check_channel_collaboration(
        self,
        channel1: ChannelType,
        channel2: ChannelType
    ) -> ChannelCollaboration:
        """
        Check collaboration between two channels.
        
        Ensures full collaboration across all channels.
        """
        key = f"{channel1.value}_{channel2.value}"
        if key in self.collaborations:
            return self.collaborations[key]
        
        ch1 = self.channels.get(channel1)
        ch2 = self.channels.get(channel2)
        
        if not ch1 or not ch2:
            raise ValueError(f"Channel not found: {channel1} or {channel2}")
        
        # Find shared systems
        shared_systems = list(set(ch1.systems) & set(ch2.systems))
        
        # Find integration points
        integration_points = []
        if channel2.value in ch1.integrations:
            integration_points.append(f"{ch1.name} -> {ch2.name}")
        if channel1.value in ch2.integrations:
            integration_points.append(f"{ch2.name} -> {ch1.name}")
        
        # Calculate collaboration level
        collaboration_level = 0.0
        
        # Base points for being present purpose
        if ch1.is_present_purpose and ch2.is_present_purpose:
            collaboration_level += 30.0
        
        # Points for shared systems
        if shared_systems:
            collaboration_level += min(30.0, len(shared_systems) * 10.0)
        
        # Points for integration
        if integration_points:
            collaboration_level += min(20.0, len(integration_points) * 10.0)
        
        # Points for API integration
        shared_apis = list(set(ch1.api_endpoints) & set(ch2.api_endpoints))
        if shared_apis:
            collaboration_level += min(20.0, len(shared_apis) * 10.0)
        
        # Determine status
        if collaboration_level >= 80.0:
            status = CollaborationStatus.FULLY_COLLABORATIVE
        elif collaboration_level >= 40.0:
            status = CollaborationStatus.PARTIALLY_COLLABORATIVE
        else:
            status = CollaborationStatus.NOT_COLLABORATIVE
        
        collaboration = ChannelCollaboration(
            channel1=channel1,
            channel2=channel2,
            collaboration_level=collaboration_level,
            integration_points=integration_points,
            shared_systems=shared_systems,
            status=status
        )
        
        self.collaborations[key] = collaboration
        
        return collaboration
    
    def check_all_collaborations(self) -> Dict[str, ChannelCollaboration]:
        """Check collaboration across all channels"""
        all_collaborations = {}
        
        channels_list = list(self.channels.keys())
        
        for i, ch1 in enumerate(channels_list):
            for ch2 in channels_list[i+1:]:
                key = f"{ch1.value}_{ch2.value}"
                collaboration = self.check_channel_collaboration(ch1, ch2)
                all_collaborations[key] = collaboration
        
        return all_collaborations
    
    def check_present_purpose_collaboration(self) -> Dict[str, Any]:
        """
        Check collaboration specifically for present purpose channels.
        
        PRESENT PURPOSE:
        PROFESSIONAL / PI / EDUCATION should be our present purpose to start from.
        """
        present_purpose = {}
        
        # Check all pairs of present purpose channels
        for i, ch1 in enumerate(self.present_purpose_channels):
            for ch2 in self.present_purpose_channels[i+1:]:
                key = f"{ch1.value}_{ch2.value}"
                collaboration = self.check_channel_collaboration(ch1, ch2)
                present_purpose[key] = {
                    "channel1": ch1.value,
                    "channel2": ch2.value,
                    "collaboration_level": collaboration.collaboration_level,
                    "status": collaboration.status.value,
                    "shared_systems": collaboration.shared_systems,
                    "integration_points": collaboration.integration_points
                }
        
        # Overall present purpose status
        all_collaborations = list(present_purpose.values())
        avg_collaboration = sum(c["collaboration_level"] for c in all_collaborations) / len(all_collaborations) if all_collaborations else 0.0
        
        fully_collaborative = all(
            c["status"] == CollaborationStatus.FULLY_COLLABORATIVE.value
            for c in all_collaborations
        )
        
        return {
            "present_purpose_channels": [ch.value for ch in self.present_purpose_channels],
            "collaborations": present_purpose,
            "average_collaboration": avg_collaboration,
            "fully_collaborative": fully_collaborative,
            "status": "fully_collaborative" if fully_collaborative else "needs_improvement",
            "message": "PRESENT PURPOSE: PROFESSIONAL / PI / EDUCATION should be our present purpose to start from."
        }
    
    def get_channel_info(self, channel_type: ChannelType) -> Dict[str, Any]:
        """Get information about a specific channel"""
        channel = self.channels.get(channel_type)
        if not channel:
            raise ValueError(f"Channel not found: {channel_type}")
        
        return {
            "channel_type": channel.channel_type.value,
            "name": channel.name,
            "description": channel.description,
            "is_present_purpose": channel.is_present_purpose,
            "systems": channel.systems,
            "api_endpoints": channel.api_endpoints,
            "integrations": channel.integrations,
            "collaboration_status": channel.collaboration_status.value,
            "last_updated": channel.last_updated.isoformat()
        }
    
    def get_system_summary(self) -> Dict[str, Any]:
        """Get summary of channel collaboration system"""
        all_collaborations = self.check_all_collaborations()
        
        present_purpose_status = self.check_present_purpose_collaboration()
        
        fully_collaborative_count = sum(
            1 for c in all_collaborations.values()
            if c.status == CollaborationStatus.FULLY_COLLABORATIVE
        )
        
        total_collaborations = len(all_collaborations)
        
        return {
            "total_channels": len(self.channels),
            "present_purpose_channels": [ch.value for ch in self.present_purpose_channels],
            "total_collaborations": total_collaborations,
            "fully_collaborative_count": fully_collaborative_count,
            "collaboration_rate": (fully_collaborative_count / total_collaborations * 100) if total_collaborations > 0 else 0.0,
            "present_purpose_status": present_purpose_status,
            "channels": {
                ch.value: self.get_channel_info(ch)
                for ch in self.channels.keys()
            },
            "message": "PRESENT PURPOSE: PROFESSIONAL / PI / EDUCATION should be our present purpose to start from. We must be FULLY COLLABORATIVE across all channels."
        }


# Global instance
_collaboration_system: Optional[ChannelCollaborationSystem] = None


def get_channel_collaboration_system() -> ChannelCollaborationSystem:
    """Get the global channel collaboration system instance"""
    global _collaboration_system
    if _collaboration_system is None:
        _collaboration_system = ChannelCollaborationSystem()
    return _collaboration_system
