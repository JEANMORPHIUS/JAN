"""
LEGAL CONTRACTUAL FRAMEWORK
Comprehensive Legal & Contractual System for All Channels, Entities, Projects

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE NOAH PROTOCOL:
- Architectural Weight: Built for 10x, 100x, 1000x scale
- The Pitch: Waterproof error handling
- The Perimeter: Clear jurisdiction (legal boundaries)
- The Door: Trust the system's buoyancy

THE ARRIVAL PROTOCOL:
- Pre-Commissioning Scan: Can this codebase carry legal compliance?
- Gatekeeper Protocol: Vet all legal dependencies
- Frequency Anchor: Code from "done" - legal framework ready

THE TRUTH:
Everything must be above board.
Even if it's not X (external), it must be above board.
Connect the yin with the yang.
"""

from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime, timedelta
from pathlib import Path
import json
import logging

logger = logging.getLogger(__name__)


class AgreementType(Enum):
    """Types of agreements"""
    PRS_COPYRIGHT = "prs_copyright"  # PRS copyright licensing
    MUSIC_LICENSING = "music_licensing"  # General music licensing
    CONTENT_LICENSING = "content_licensing"  # Content licensing
    PARTNERSHIP = "partnership"  # Partnership agreements
    SERVICE = "service"  # Service agreements
    EMPLOYMENT = "employment"  # Employment contracts
    CONSULTING = "consulting"  # Consulting agreements
    DISTRIBUTION = "distribution"  # Distribution agreements
    PUBLISHING = "publishing"  # Publishing agreements
    OTHER = "other"  # Other agreements


class ChannelType(Enum):
    """Channel types"""
    PROFESSIONAL = "professional"  # Channel 1: Professional Platform
    CREATOR = "creator"  # Channel 2: Creator Economy
    EDUCATIONAL = "educational"  # Channel 3: Educational Platform
    SIYEM = "siyem"  # SIYEM internal
    ATILOK = "atilok"  # ATILOK project
    JAN_STUDIO = "jan_studio"  # JAN Studio


class EntityType(Enum):
    """Entity types"""
    CREATIVE_PERSONA = "creative_persona"  # Jean, Karasahin, Pierre, Ramiz, Siyem Media
    BUSINESS_PROJECT = "business_project"  # Edible London, Ilven Seamoss, Edible Cyprus, ATILOK
    GOVERNANCE = "governance"  # Siyem.org, JAN Studio


@dataclass
class Agreement:
    """Legal agreement"""
    agreement_id: str
    agreement_type: AgreementType
    title: str
    description: str
    parties: List[str]  # Parties involved
    channel: ChannelType
    entity: Optional[str] = None
    project: Optional[str] = None
    effective_date: Optional[datetime] = None
    expiration_date: Optional[datetime] = None
    status: str = "draft"  # draft, active, expired, terminated
    document_path: Optional[str] = None
    prs_registration: Optional[str] = None  # PRS registration number
    copyright_holder: Optional[str] = None
    licensing_terms: Dict[str, Any] = field(default_factory=dict)
    compliance_status: str = "pending"  # pending, compliant, non_compliant
    notes: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)


@dataclass
class PRSCopyrightRecord:
    """PRS copyright record"""
    song_id: str
    song_title: str
    composer: str
    publisher: Optional[str] = None
    prs_registration: Optional[str] = None
    copyright_year: Optional[int] = None
    copyright_holder: str = ""
    licensing_status: str = "pending"  # pending, licensed, unlicensed
    channel: ChannelType = ChannelType.CREATOR
    entity: Optional[str] = None
    usage_rights: Dict[str, Any] = field(default_factory=dict)
    compliance_verified: bool = False
    compliance_date: Optional[datetime] = None
    notes: str = ""
    created_at: datetime = field(default_factory=datetime.now)


class LegalContractualFramework:
    """
    Legal Contractual Framework
    Comprehensive legal and contractual system for all channels, entities, projects
    
    Architectural Weight: Handles 10x, 100x, 1000x agreements
    """
    
    def __init__(self, data_path: Optional[Path] = None):
        """Initialize legal framework"""
        if data_path is None:
            data_path = Path(__file__).parent.parent.parent / "data" / "legal_contracts"
        
        self.data_path = Path(data_path)
        self.data_path.mkdir(parents=True, exist_ok=True)
        
        self.agreements: Dict[str, Agreement] = {}
        self.prs_records: Dict[str, PRSCopyrightRecord] = {}
        self.channels: Set[ChannelType] = set()
        self.entities: Set[str] = set()
        self.projects: Set[str] = set()
        
        self._load_data()
        
        logger.info("Legal Contractual Framework initialized")
    
    def _load_data(self):
        """Load existing data (The Pitch: Waterproof error handling)"""
        try:
            # Load agreements
            agreements_file = self.data_path / "agreements.json"
            if agreements_file.exists():
                with open(agreements_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for item in data.get("agreements", []):
                        agreement = Agreement(**item)
                        # Convert string dates to datetime
                        if isinstance(agreement.effective_date, str):
                            agreement.effective_date = datetime.fromisoformat(agreement.effective_date)
                        if isinstance(agreement.expiration_date, str):
                            agreement.expiration_date = datetime.fromisoformat(agreement.expiration_date)
                        if isinstance(agreement.created_at, str):
                            agreement.created_at = datetime.fromisoformat(agreement.created_at)
                        if isinstance(agreement.updated_at, str):
                            agreement.updated_at = datetime.fromisoformat(agreement.updated_at)
                        self.agreements[agreement.agreement_id] = agreement
            
            # Load PRS records
            prs_file = self.data_path / "prs_copyrights.json"
            if prs_file.exists():
                with open(prs_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for item in data.get("prs_records", []):
                        record = PRSCopyrightRecord(**item)
                        if isinstance(record.compliance_date, str):
                            record.compliance_date = datetime.fromisoformat(record.compliance_date)
                        if isinstance(record.created_at, str):
                            record.created_at = datetime.fromisoformat(record.created_at)
                        self.prs_records[record.song_id] = record
        except Exception as e:
            logger.error(f"Error loading legal data: {e}")
    
    def _save_data(self):
        """Save data (The Perimeter: Clear jurisdiction)"""
        try:
            # Save agreements
            agreements_file = self.data_path / "agreements.json"
            agreements_data = {
                "agreements": [
                    {
                        **agreement.__dict__,
                        "effective_date": agreement.effective_date.isoformat() if agreement.effective_date else None,
                        "expiration_date": agreement.expiration_date.isoformat() if agreement.expiration_date else None,
                        "created_at": agreement.created_at.isoformat(),
                        "updated_at": agreement.updated_at.isoformat(),
                        "agreement_type": agreement.agreement_type.value,
                        "channel": agreement.channel.value
                    }
                    for agreement in self.agreements.values()
                ]
            }
            with open(agreements_file, 'w', encoding='utf-8') as f:
                json.dump(agreements_data, f, indent=2, ensure_ascii=False)
            
            # Save PRS records
            prs_file = self.data_path / "prs_copyrights.json"
            prs_data = {
                "prs_records": [
                    {
                        **record.__dict__,
                        "compliance_date": record.compliance_date.isoformat() if record.compliance_date else None,
                        "created_at": record.created_at.isoformat(),
                        "channel": record.channel.value
                    }
                    for record in self.prs_records.values()
                ]
            }
            with open(prs_file, 'w', encoding='utf-8') as f:
                json.dump(prs_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving legal data: {e}")
    
    def register_prs_copyright(
        self,
        song_title: str,
        composer: str,
        channel: ChannelType = ChannelType.CREATOR,
        entity: Optional[str] = None,
        **kwargs
    ) -> PRSCopyrightRecord:
        """
        Register PRS copyright (The Gatekeeper Protocol: Input Control)
        
        Args:
            song_title: Title of the song
            composer: Composer name
            channel: Channel type
            entity: Entity name (optional)
            **kwargs: Additional fields
        
        Returns:
            PRSCopyrightRecord
        """
        song_id = f"prs_{datetime.now().timestamp()}"
        
        record = PRSCopyrightRecord(
            song_id=song_id,
            song_title=song_title,
            composer=composer,
            channel=channel,
            entity=entity,
            **kwargs
        )
        
        self.prs_records[song_id] = record
        self._save_data()
        
        logger.info(f"PRS copyright registered: {song_title} by {composer}")
        return record
    
    def create_agreement(
        self,
        agreement_type: AgreementType,
        title: str,
        description: str,
        parties: List[str],
        channel: ChannelType,
        entity: Optional[str] = None,
        project: Optional[str] = None,
        **kwargs
    ) -> Agreement:
        """
        Create agreement (Pre-Commissioning Scan: Can codebase carry it?)
        
        Args:
            agreement_type: Type of agreement
            title: Agreement title
            description: Agreement description
            parties: List of parties
            channel: Channel type
            entity: Entity name (optional)
            project: Project name (optional)
            **kwargs: Additional fields
        
        Returns:
            Agreement
        """
        agreement_id = f"agreement_{datetime.now().timestamp()}"
        
        agreement = Agreement(
            agreement_id=agreement_id,
            agreement_type=agreement_type,
            title=title,
            description=description,
            parties=parties,
            channel=channel,
            entity=entity,
            project=project,
            **kwargs
        )
        
        self.agreements[agreement_id] = agreement
        self.channels.add(channel)
        if entity:
            self.entities.add(entity)
        if project:
            self.projects.add(project)
        
        self._save_data()
        
        logger.info(f"Agreement created: {title} ({agreement_type.value})")
        return agreement
    
    def verify_compliance(self, agreement_id: Optional[str] = None, song_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Verify compliance (The Door: Trust the system's buoyancy)
        
        Args:
            agreement_id: Agreement ID (optional)
            song_id: Song ID (optional)
        
        Returns:
            Compliance report
        """
        report = {
            "timestamp": datetime.now().isoformat(),
            "agreements_checked": 0,
            "prs_records_checked": 0,
            "compliant": 0,
            "non_compliant": 0,
            "pending": 0,
            "issues": []
        }
        
        if agreement_id:
            agreement = self.agreements.get(agreement_id)
            if agreement:
                report["agreements_checked"] = 1
                if agreement.compliance_status == "compliant":
                    report["compliant"] = 1
                elif agreement.compliance_status == "non_compliant":
                    report["non_compliant"] = 1
                    report["issues"].append(f"Agreement {agreement_id} is non-compliant: {agreement.title}")
                else:
                    report["pending"] = 1
        
        if song_id:
            record = self.prs_records.get(song_id)
            if record:
                report["prs_records_checked"] = 1
                if record.compliance_verified:
                    report["compliant"] += 1
                else:
                    report["pending"] += 1
                    report["issues"].append(f"PRS record {song_id} not verified: {record.song_title}")
        
        if not agreement_id and not song_id:
            # Check all
            for agreement in self.agreements.values():
                report["agreements_checked"] += 1
                if agreement.compliance_status == "compliant":
                    report["compliant"] += 1
                elif agreement.compliance_status == "non_compliant":
                    report["non_compliant"] += 1
                    report["issues"].append(f"Agreement {agreement.agreement_id} is non-compliant: {agreement.title}")
                else:
                    report["pending"] += 1
            
            for record in self.prs_records.values():
                report["prs_records_checked"] += 1
                if record.compliance_verified:
                    report["compliant"] += 1
                else:
                    report["pending"] += 1
                    if not record.prs_registration:
                        report["issues"].append(f"PRS record {record.song_id} missing PRS registration: {record.song_title}")
        
        return report
    
    def get_channel_agreements(self, channel: ChannelType) -> List[Agreement]:
        """Get all agreements for a channel"""
        return [a for a in self.agreements.values() if a.channel == channel]
    
    def get_entity_agreements(self, entity: str) -> List[Agreement]:
        """Get all agreements for an entity"""
        return [a for a in self.agreements.values() if a.entity == entity]
    
    def get_project_agreements(self, project: str) -> List[Agreement]:
        """Get all agreements for a project"""
        return [a for a in self.agreements.values() if a.project == project]
    
    def get_summary(self) -> Dict[str, Any]:
        """Get framework summary"""
        return {
            "total_agreements": len(self.agreements),
            "total_prs_records": len(self.prs_records),
            "channels": [c.value for c in self.channels],
            "entities": list(self.entities),
            "projects": list(self.projects),
            "compliance": self.verify_compliance(),
            "timestamp": datetime.now().isoformat()
        }


# Global framework instance (The Perimeter: Clear jurisdiction)
_legal_framework: Optional[LegalContractualFramework] = None


def get_legal_framework() -> LegalContractualFramework:
    """Get or create legal framework"""
    global _legal_framework
    
    if _legal_framework is None:
        _legal_framework = LegalContractualFramework()
    
    return _legal_framework
