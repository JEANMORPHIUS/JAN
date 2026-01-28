"""
CAMPAIGN AUTOMATION API
API endpoints for campaign automation system

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

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X.
"""

from fastapi import APIRouter, HTTPException, UploadFile, File, Query
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
import logging
import sys
from pathlib import Path

# Add SIYEM services to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "SIYEM" / "services"))

from campaign_automation import (
    ContactManager,
    EmailCampaign,
    SocialMediaScheduler,
    ResponseTracker,
    CampaignAnalytics
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/campaign", tags=["campaign-automation"])


# Request/Response Models
class ContactRequest(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    organization: Optional[str] = None
    role: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = None
    source: Optional[str] = None
    notes: Optional[str] = None


class EmailCampaignRequest(BaseModel):
    campaign_name: str
    subject: str
    body_html: str
    body_text: Optional[str] = None
    sender_email: Optional[str] = None
    sender_name: Optional[str] = None


class SendCampaignRequest(BaseModel):
    campaign_id: int
    contact_ids: Optional[List[int]] = None
    categories: Optional[List[str]] = None
    tags: Optional[List[str]] = None


class SocialPostRequest(BaseModel):
    platform: str = Field(..., description="twitter, instagram, linkedin, facebook, tiktok")
    content: str
    media_url: Optional[str] = None
    scheduled_at: Optional[str] = None


class ResponseRequest(BaseModel):
    email: Optional[str] = None
    contact_id: Optional[int] = None
    source: str = "email"
    response_type: str = "reply"
    content: Optional[str] = None
    metadata: Optional[dict] = None


# Contact Management Endpoints
@router.post("/contacts")
async def add_contact(contact: ContactRequest):
    """Add a contact to the campaign database."""
    try:
        result = ContactManager.add_contact(
            email=contact.email,
            name=contact.name,
            organization=contact.organization,
            role=contact.role,
            category=contact.category,
            tags=contact.tags,
            source=contact.source,
            notes=contact.notes
        )
        return result
    except Exception as e:
        logger.error(f"Error adding contact: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/contacts/import")
async def import_contacts(file: UploadFile = File(...)):
    """Import contacts from CSV file."""
    try:
        # Save uploaded file temporarily
        import tempfile
        with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name
        
        result = ContactManager.import_contacts_from_csv(tmp_path)
        
        # Clean up
        import os
        os.unlink(tmp_path)
        
        return result
    except Exception as e:
        logger.error(f"Error importing contacts: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/contacts")
async def get_contacts(
    category: Optional[str] = Query(None),
    status: str = Query("active"),
    tags: Optional[str] = Query(None)  # Comma-separated
):
    """Get contacts matching criteria."""
    try:
        tag_list = tags.split(",") if tags else None
        contacts = ContactManager.get_contacts(
            category=category,
            status=status,
            tags=tag_list
        )
        return {
            "contacts": contacts,
            "count": len(contacts)
        }
    except Exception as e:
        logger.error(f"Error getting contacts: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


# Email Campaign Endpoints
@router.post("/email/create")
async def create_email_campaign(campaign: EmailCampaignRequest):
    """Create an email campaign."""
    try:
        email_campaign = EmailCampaign()
        result = email_campaign.create_campaign(
            campaign_name=campaign.campaign_name,
            subject=campaign.subject,
            body_html=campaign.body_html,
            body_text=campaign.body_text,
            sender_email=campaign.sender_email,
            sender_name=campaign.sender_name
        )
        return result
    except Exception as e:
        logger.error(f"Error creating campaign: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/email/send")
async def send_email_campaign(request: SendCampaignRequest):
    """Send email campaign to contacts."""
    try:
        email_campaign = EmailCampaign()
        result = email_campaign.send_campaign(
            campaign_id=request.campaign_id,
            contact_ids=request.contact_ids,
            categories=request.categories,
            tags=request.tags
        )
        return result
    except Exception as e:
        logger.error(f"Error sending campaign: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


# Social Media Endpoints
@router.post("/social/create")
async def create_social_post(post: SocialPostRequest):
    """Create a social media post."""
    try:
        from datetime import datetime
        
        scheduler = SocialMediaScheduler()
        scheduled_at = None
        if post.scheduled_at:
            scheduled_at = datetime.fromisoformat(post.scheduled_at.replace('Z', '+00:00'))
        
        result = scheduler.create_post(
            platform=post.platform,
            content=post.content,
            media_url=post.media_url,
            scheduled_at=scheduled_at
        )
        return result
    except Exception as e:
        logger.error(f"Error creating social post: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/social/export")
async def export_to_scheduler(
    scheduler: str = Query(..., description="later, metricool, publer, buffer"),
    post_ids: Optional[str] = Query(None, description="Comma-separated post IDs"),
    platform: Optional[str] = Query(None)
):
    """Export posts to scheduling service."""
    try:
        scheduler_obj = SocialMediaScheduler()
        post_id_list = [int(id) for id in post_ids.split(",")] if post_ids else None
        result = scheduler_obj.export_to_scheduler(
            scheduler=scheduler,
            post_ids=post_id_list,
            platform=platform
        )
        return result
    except Exception as e:
        logger.error(f"Error exporting to scheduler: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


# Response Tracking Endpoints
@router.post("/responses")
async def record_response(response: ResponseRequest):
    """Record a campaign response."""
    try:
        result = ResponseTracker.record_response(
            email=response.email,
            contact_id=response.contact_id,
            source=response.source,
            response_type=response.response_type,
            content=response.content,
            metadata=response.metadata
        )
        return result
    except Exception as e:
        logger.error(f"Error recording response: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/responses")
async def get_responses(
    contact_id: Optional[int] = Query(None),
    response_type: Optional[str] = Query(None),
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None)
):
    """Get campaign responses."""
    try:
        from datetime import datetime
        
        start = datetime.fromisoformat(start_date.replace('Z', '+00:00')) if start_date else None
        end = datetime.fromisoformat(end_date.replace('Z', '+00:00')) if end_date else None
        
        responses = ResponseTracker.get_responses(
            contact_id=contact_id,
            response_type=response_type,
            start_date=start,
            end_date=end
        )
        return {
            "responses": responses,
            "count": len(responses)
        }
    except Exception as e:
        logger.error(f"Error getting responses: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))


# Analytics Endpoints
@router.get("/analytics/{campaign_id}")
async def get_campaign_analytics(campaign_id: int):
    """Get campaign analytics."""
    try:
        stats = CampaignAnalytics.get_campaign_stats(campaign_id)
        return stats
    except Exception as e:
        logger.error(f"Error getting analytics: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
