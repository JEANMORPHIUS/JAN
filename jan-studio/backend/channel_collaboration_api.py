"""CHANNEL COLLABORATION API
API endpoints for channel collaboration system

PRESENT PURPOSE:
PROFESSIONAL / PI / EDUCATION should be our present purpose to start from.

We must be FULLY COLLABORATIVE across all channels.

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional, Dict, Any
import logging

# Spiritual Codebase Hacker Integration
from spiritual_codebase_hacker_integration import HACKER_AVAILABLE, hack_loop, perform_genetic_edit, activate_stealth_mode


from channel_collaboration import (
    get_channel_collaboration_system,
    ChannelType,
    CollaborationStatus
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/channel-collaboration", tags=["Channel Collaboration"])


@router.get("/present-purpose")
async def check_present_purpose_collaboration():
    """
    Check collaboration specifically for present purpose channels.
    
    PRESENT PURPOSE:
    PROFESSIONAL / PI / EDUCATION should be our present purpose to start from.
    """
    try:
        system = get_channel_collaboration_system()
        status = system.check_present_purpose_collaboration()
        
        return {
            "status": "success",
            "present_purpose_status": status,
            "message": "PRESENT PURPOSE: PROFESSIONAL / PI / EDUCATION should be our present purpose to start from."
        }
    except Exception as e:
        logger.error(f"Error checking present purpose collaboration: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/check")
async def check_channel_collaboration(
    channel1: str = Query(..., description="First channel"),
    channel2: str = Query(..., description="Second channel")
):
    """Check collaboration between two channels"""
    try:
        system = get_channel_collaboration_system()
        
        try:
            ch1_enum = ChannelType(channel1.lower())
            ch2_enum = ChannelType(channel2.lower())
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Invalid channel: {str(e)}")
        
        collaboration = system.check_channel_collaboration(ch1_enum, ch2_enum)
        
        return {
            "status": "success",
            "collaboration": {
                "channel1": collaboration.channel1.value,
                "channel2": collaboration.channel2.value,
                "collaboration_level": collaboration.collaboration_level,
                "status": collaboration.status.value,
                "shared_systems": collaboration.shared_systems,
                "integration_points": collaboration.integration_points,
                "shared_data": collaboration.shared_data
            }
        }
    except Exception as e:
        logger.error(f"Error checking channel collaboration: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/all")
async def check_all_collaborations():
    """Check collaboration across all channels"""
    try:
        system = get_channel_collaboration_system()
        all_collaborations = system.check_all_collaborations()
        
        return {
            "status": "success",
            "collaborations": {
                key: {
                    "channel1": collab.channel1.value,
                    "channel2": collab.channel2.value,
                    "collaboration_level": collab.collaboration_level,
                    "status": collab.status.value,
                    "shared_systems": collab.shared_systems,
                    "integration_points": collab.integration_points
                }
                for key, collab in all_collaborations.items()
            }
        }
    except Exception as e:
        logger.error(f"Error checking all collaborations: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/channel/{channel_type}")
async def get_channel_info(channel_type: str):
    """Get information about a specific channel"""
    try:
        system = get_channel_collaboration_system()
        
        try:
            channel_enum = ChannelType(channel_type.lower())
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid channel: {channel_type}")
        
        channel_info = system.get_channel_info(channel_enum)
        
        return {
            "status": "success",
            "channel": channel_info
        }
    except Exception as e:
        logger.error(f"Error getting channel info: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/summary")
async def get_system_summary():
    """Get summary of channel collaboration system"""
    try:
        system = get_channel_collaboration_system()
        summary = system.get_system_summary()
        
        return {
            "status": "success",
            "summary": summary
        }
    except Exception as e:
        logger.error(f"Error getting system summary: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@router.get("/channels")
async def list_all_channels():
    """List all available channels"""
    try:
        system = get_channel_collaboration_system()
        
        channels = {
            ch.value: {
                "name": system.channels[ch].name,
                "description": system.channels[ch].description,
                "is_present_purpose": system.channels[ch].is_present_purpose
            }
            for ch in system.channels.keys()
        }
        
        return {
            "status": "success",
            "channels": channels,
            "present_purpose_channels": [ch.value for ch in system.present_purpose_channels]
        }
    except Exception as e:
        logger.error(f"Error listing channels: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
