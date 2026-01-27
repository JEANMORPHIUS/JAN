"""
RAMIZ HUMANITARIAN COMMUNICATIONS
Communication system for humanitarian operations

THE NOAH PROTOCOL:
- Architectural Weight: Built for 10x, 100x, 1000x communications
- The Pitch: Waterproof error handling
- The Perimeter: Clear communication boundaries

THE TRUTH:
NO ONE GETS LEFT BEHIND.
Gaza as priority.
Communication is critical for coordination.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field
import logging

logger = logging.getLogger(__name__)


class CommunicationType(Enum):
    """Communication types"""
    ALERT = "alert"
    UPDATE = "update"
    COORDINATION = "coordination"
    EMERGENCY = "emergency"
    STATUS = "status"
    FUNDING = "funding"
    VOLUNTEER = "volunteer"
    SUPPLY = "supply"
    OTHER = "other"


class CommunicationPriority(Enum):
    """Communication priority"""
    CRITICAL = "critical"  # Gaza, immediate
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass
class HumanitarianCommunication:
    """Humanitarian communication"""
    communication_id: str
    communication_type: CommunicationType
    priority: CommunicationPriority
    title: str
    message: str
    region: Optional[str] = None
    project_id: Optional[str] = None
    gaza_priority: bool = False
    recipients: List[str] = field(default_factory=list)
    sent_at: Optional[datetime] = None
    created_at: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)


class RamizHumanitarianCommunications:
    """
    Ramiz Humanitarian Communications
    Manages communications for humanitarian operations
    
    Gaza priority for all critical communications.
    """
    
    def __init__(self):
        """Initialize communications system"""
        self.communications: Dict[str, HumanitarianCommunication] = {}
        self.gaza_communications: List[str] = []  # communication_ids for Gaza
        
        logger.info("Ramiz Humanitarian Communications initialized")
    
    def send_communication(self, communication_type: CommunicationType,
                          priority: CommunicationPriority, title: str, message: str,
                          region: Optional[str] = None, project_id: Optional[str] = None,
                          gaza_priority: bool = False, recipients: List[str] = None,
                          metadata: Dict[str, Any] = None) -> HumanitarianCommunication:
        """Send communication"""
        communication_id = f"comm_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Auto-detect Gaza priority
        if region and region.lower() == "gaza":
            gaza_priority = True
        
        communication = HumanitarianCommunication(
            communication_id=communication_id,
            communication_type=communication_type,
            priority=priority,
            title=title,
            message=message,
            region=region,
            project_id=project_id,
            gaza_priority=gaza_priority,
            recipients=recipients or [],
            metadata=metadata or {},
            sent_at=datetime.now()
        )
        
        self.communications[communication_id] = communication
        
        if gaza_priority:
            if communication_id not in self.gaza_communications:
                self.gaza_communications.append(communication_id)
        
        logger.info(f"Communication sent: {communication_id}, Type: {communication_type.value}, Priority: {priority.value}, Gaza: {gaza_priority}")
        
        return communication
    
    def send_gaza_alert(self, title: str, message: str, project_id: Optional[str] = None,
                       metadata: Dict[str, Any] = None) -> HumanitarianCommunication:
        """Send Gaza priority alert"""
        return self.send_communication(
            communication_type=CommunicationType.ALERT,
            priority=CommunicationPriority.CRITICAL,
            title=title,
            message=message,
            region="Gaza",
            project_id=project_id or "gaza_comprehensive_aid",
            gaza_priority=True,
            metadata=metadata or {}
        )
    
    def get_gaza_communications(self) -> List[Dict[str, Any]]:
        """Get Gaza communications"""
        gaza_comms = []
        for comm_id in self.gaza_communications:
            if comm_id in self.communications:
                comm = self.communications[comm_id]
                gaza_comms.append({
                    "communication_id": comm.communication_id,
                    "type": comm.communication_type.value,
                    "priority": comm.priority.value,
                    "title": comm.title,
                    "message": comm.message,
                    "sent_at": comm.sent_at.isoformat() if comm.sent_at else None,
                    "metadata": comm.metadata
                })
        
        return sorted(gaza_comms, key=lambda x: x["sent_at"] or "", reverse=True)
    
    def get_communications_analytics(self) -> Dict[str, Any]:
        """Get communications analytics"""
        total_communications = len(self.communications)
        gaza_communications = len(self.gaza_communications)
        
        by_type = {}
        by_priority = {}
        
        for comm in self.communications.values():
            comm_type = comm.communication_type.value
            priority = comm.priority.value
            
            by_type[comm_type] = by_type.get(comm_type, 0) + 1
            by_priority[priority] = by_priority.get(priority, 0) + 1
        
        critical_communications = len([c for c in self.communications.values() 
                                      if c.priority == CommunicationPriority.CRITICAL])
        
        return {
            "total_communications": total_communications,
            "gaza_communications": gaza_communications,
            "critical_communications": critical_communications,
            "by_type": by_type,
            "by_priority": by_priority
        }


# Global communications instance
_communications: Optional[RamizHumanitarianCommunications] = None


def get_humanitarian_communications() -> RamizHumanitarianCommunications:
    """Get global humanitarian communications instance"""
    global _communications
    if _communications is None:
        _communications = RamizHumanitarianCommunications()
    return _communications
