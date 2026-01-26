"""
LEGAL CONTRACTUAL API
API endpoints for legal and contractual framework

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
Everything must be above board.
Even if it's not X (external), it must be above board.
Connect the yin with the yang.
"""

from fastapi import APIRouter, HTTPException, Body
from typing import Optional, Dict, List, Any
from pydantic import BaseModel
import logging

from legal_contractual_framework import (
    get_legal_framework,
    AgreementType,
    ChannelType,
    EntityType
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/legal", tags=["Legal & Contractual"])


class PRSRegistrationRequest(BaseModel):
    """PRS registration request"""
    song_title: str
    composer: str
    channel: str = "creator"
    entity: Optional[str] = None
    publisher: Optional[str] = None
    copyright_year: Optional[int] = None
    copyright_holder: str = ""
    usage_rights: Dict[str, Any] = {}


class AgreementCreateRequest(BaseModel):
    """Agreement creation request"""
    agreement_type: str
    title: str
    description: str
    parties: List[str]
    channel: str
    entity: Optional[str] = None
    project: Optional[str] = None
    effective_date: Optional[str] = None
    expiration_date: Optional[str] = None
    document_path: Optional[str] = None
    prs_registration: Optional[str] = None
    copyright_holder: Optional[str] = None
    licensing_terms: Dict[str, Any] = {}


@router.post("/prs/register")
async def register_prs_copyright(request: PRSRegistrationRequest):
    """Register PRS copyright"""
    try:
        framework = get_legal_framework()
        channel = ChannelType(request.channel)
        
        record = framework.register_prs_copyright(
            song_title=request.song_title,
            composer=request.composer,
            channel=channel,
            entity=request.entity,
            publisher=request.publisher,
            copyright_year=request.copyright_year,
            copyright_holder=request.copyright_holder,
            usage_rights=request.usage_rights
        )
        
        return {
            "status": "success",
            "message": "PRS copyright registered",
            "record": {
                "song_id": record.song_id,
                "song_title": record.song_title,
                "composer": record.composer,
                "channel": record.channel.value,
                "compliance_verified": record.compliance_verified
            }
        }
    except Exception as e:
        logger.error(f"Error registering PRS copyright: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/prs/records")
async def get_prs_records(channel: Optional[str] = None, entity: Optional[str] = None):
    """Get PRS records"""
    try:
        framework = get_legal_framework()
        
        records = list(framework.prs_records.values())
        
        if channel:
            channel_type = ChannelType(channel)
            records = [r for r in records if r.channel == channel_type]
        
        if entity:
            records = [r for r in records if r.entity == entity]
        
        return {
            "status": "success",
            "count": len(records),
            "records": [
                {
                    "song_id": r.song_id,
                    "song_title": r.song_title,
                    "composer": r.composer,
                    "channel": r.channel.value,
                    "entity": r.entity,
                    "prs_registration": r.prs_registration,
                    "licensing_status": r.licensing_status,
                    "compliance_verified": r.compliance_verified
                }
                for r in records
            ]
        }
    except Exception as e:
        logger.error(f"Error getting PRS records: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/agreements/create")
async def create_agreement(request: AgreementCreateRequest):
    """Create agreement"""
    try:
        framework = get_legal_framework()
        
        agreement_type = AgreementType(request.agreement_type)
        channel = ChannelType(request.channel)
        
        from datetime import datetime
        effective_date = None
        if request.effective_date:
            effective_date = datetime.fromisoformat(request.effective_date)
        
        expiration_date = None
        if request.expiration_date:
            expiration_date = datetime.fromisoformat(request.expiration_date)
        
        agreement = framework.create_agreement(
            agreement_type=agreement_type,
            title=request.title,
            description=request.description,
            parties=request.parties,
            channel=channel,
            entity=request.entity,
            project=request.project,
            effective_date=effective_date,
            expiration_date=expiration_date,
            document_path=request.document_path,
            prs_registration=request.prs_registration,
            copyright_holder=request.copyright_holder,
            licensing_terms=request.licensing_terms
        )
        
        return {
            "status": "success",
            "message": "Agreement created",
            "agreement": {
                "agreement_id": agreement.agreement_id,
                "title": agreement.title,
                "agreement_type": agreement.agreement_type.value,
                "channel": agreement.channel.value,
                "status": agreement.status
            }
        }
    except Exception as e:
        logger.error(f"Error creating agreement: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/agreements")
async def get_agreements(
    channel: Optional[str] = None,
    entity: Optional[str] = None,
    project: Optional[str] = None
):
    """Get agreements"""
    try:
        framework = get_legal_framework()
        
        agreements = list(framework.agreements.values())
        
        if channel:
            channel_type = ChannelType(channel)
            agreements = [a for a in agreements if a.channel == channel_type]
        
        if entity:
            agreements = [a for a in agreements if a.entity == entity]
        
        if project:
            agreements = [a for a in agreements if a.project == project]
        
        return {
            "status": "success",
            "count": len(agreements),
            "agreements": [
                {
                    "agreement_id": a.agreement_id,
                    "title": a.title,
                    "agreement_type": a.agreement_type.value,
                    "channel": a.channel.value,
                    "entity": a.entity,
                    "project": a.project,
                    "status": a.status,
                    "compliance_status": a.compliance_status
                }
                for a in agreements
            ]
        }
    except Exception as e:
        logger.error(f"Error getting agreements: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/compliance/verify")
async def verify_compliance(
    agreement_id: Optional[str] = None,
    song_id: Optional[str] = None
):
    """Verify compliance"""
    try:
        framework = get_legal_framework()
        report = framework.verify_compliance(agreement_id=agreement_id, song_id=song_id)
        
        return {
            "status": "success",
            "report": report
        }
    except Exception as e:
        logger.error(f"Error verifying compliance: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/summary")
async def get_summary():
    """Get framework summary"""
    try:
        framework = get_legal_framework()
        summary = framework.get_summary()
        
        return {
            "status": "success",
            "summary": summary
        }
    except Exception as e:
        logger.error(f"Error getting summary: {e}")
        raise HTTPException(status_code=500, detail=str(e))
