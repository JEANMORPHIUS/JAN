"""Priority Resource Allocator - Funnel to Those Who Need It Most
Priority on the Smallest and Most Vulnerable from Evil Right Now

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
REDIRECT ALL RESOURCES TO THOSE IN NEED
PRIORITY ON THE SMALLEST AND MOST VULNERABLE
FROM EVIL RIGHT NOW
ALLAH OLMAYANA VERSIN (May God give to those who don't have)

SPRAGITSO - Our Father's Royal Seal:
- All resources bear Our Father's seal
- All resources serve The Table
- All resources respect free will
- All resources prioritize the vulnerable

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import logging
from typing import Dict, List, Optional, Tuple
from enum import Enum
from dataclass import dataclass, field
from datetime import datetime
import json
from pathlib import Path

# SPRAGITSO - Our Father's Royal Seal
SPRAGITSO = "σφραγίς"  # Greek: sphragis - The Royal Seal

logger = logging.getLogger(__name__)


class VulnerabilityLevel(Enum):
    """Vulnerability levels - priority order"""
    CRITICAL = "critical"  # Immediate danger, smallest, most vulnerable
    HIGH = "high"  # High need, vulnerable
    MEDIUM = "medium"  # Moderate need
    LOW = "low"  # Lower priority


class ResourceType(Enum):
    """Types of resources to allocate"""
    CONTENT = "content"  # Educational content, scripture, teachings
    FINANCIAL = "financial"  # Financial support
    TECHNICAL = "technical"  # Technical infrastructure, access
    EMOTIONAL = "emotional"  # Emotional support, care
    PHYSICAL = "physical"  # Physical resources, housing, food
    SPIRITUAL = "spiritual"  # Spiritual guidance, prayer


@dataclass
class Recipient:
    """Recipient of resources"""
    recipient_id: str
    name: str
    vulnerability_level: VulnerabilityLevel
    needs: List[ResourceType]
    location: Optional[str] = None
    age: Optional[int] = None
    situation: Optional[str] = None
    priority_score: float = 0.0
    sealed: bool = True
    sphragitso: str = SPRAGITSO


@dataclass
class Resource:
    """Resource to be allocated"""
    resource_id: str
    resource_type: ResourceType
    quantity: float
    unit: str
    available: bool = True
    channel: Optional[str] = None
    sealed: bool = True
    sphragitso: str = SPRAGITSO


class PriorityResourceAllocator:
    """
    Priority Resource Allocator
    
    Funnels resources to those who need it most.
    Priority on the smallest and most vulnerable from evil right now.
    Redirects all resources to those in need.
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize priority resource allocator."""
        self.config_path = config_path or "data/priority_resource_allocator.json"
        self.config_path_obj = Path(self.config_path)
        self.config_path_obj.parent.mkdir(parents=True, exist_ok=True)
        
        self.recipients: Dict[str, Recipient] = {}
        self.resources: Dict[str, Resource] = {}
        self.allocations: List[Dict] = []
        self._load_config()
    
    def _load_config(self):
        """Load configuration."""
        if self.config_path_obj.exists():
            try:
                with open(self.config_path_obj, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Load recipients
                for rec_data in data.get("recipients", []):
                    recipient = Recipient(
                        recipient_id=rec_data["recipient_id"],
                        name=rec_data["name"],
                        vulnerability_level=VulnerabilityLevel(rec_data["vulnerability_level"]),
                        needs=[ResourceType(n) for n in rec_data.get("needs", [])],
                        location=rec_data.get("location"),
                        age=rec_data.get("age"),
                        situation=rec_data.get("situation"),
                        priority_score=rec_data.get("priority_score", 0.0)
                    )
                    self.recipients[recipient.recipient_id] = recipient
                
                # Load resources
                for res_data in data.get("resources", []):
                    resource = Resource(
                        resource_id=res_data["resource_id"],
                        resource_type=ResourceType(res_data["resource_type"]),
                        quantity=res_data["quantity"],
                        unit=res_data.get("unit", ""),
                        available=res_data.get("available", True),
                        channel=res_data.get("channel")
                    )
                    self.resources[resource.resource_id] = resource
                
                self.allocations = data.get("allocations", [])
            except Exception as e:
                logger.warning(f"Error loading priority resource allocator config: {e}")
    
    def _save_config(self):
        """Save configuration."""
        try:
            data = {
                "recipients": [
                    {
                        "recipient_id": r.recipient_id,
                        "name": r.name,
                        "vulnerability_level": r.vulnerability_level.value,
                        "needs": [n.value for n in r.needs],
                        "location": r.location,
                        "age": r.age,
                        "situation": r.situation,
                        "priority_score": r.priority_score
                    }
                    for r in self.recipients.values()
                ],
                "resources": [
                    {
                        "resource_id": r.resource_id,
                        "resource_type": r.resource_type.value,
                        "quantity": r.quantity,
                        "unit": r.unit,
                        "available": r.available,
                        "channel": r.channel
                    }
                    for r in self.resources.values()
                ],
                "allocations": self.allocations,
                "last_updated": datetime.now().isoformat(),
                "sphragitso": SPRAGITSO
            }
            
            with open(self.config_path_obj, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving priority resource allocator config: {e}")
    
    def calculate_priority_score(self, recipient: Recipient) -> float:
        """Calculate priority score for recipient."""
        score = 0.0
        
        # Vulnerability level weight
        vulnerability_weights = {
            VulnerabilityLevel.CRITICAL: 100.0,
            VulnerabilityLevel.HIGH: 50.0,
            VulnerabilityLevel.MEDIUM: 25.0,
            VulnerabilityLevel.LOW: 10.0
        }
        score += vulnerability_weights.get(recipient.vulnerability_level, 0.0)
        
        # Age weight (smallest = highest priority)
        if recipient.age is not None:
            if recipient.age < 5:
                score += 30.0  # Very young children
            elif recipient.age < 13:
                score += 20.0  # Children
            elif recipient.age < 18:
                score += 10.0  # Teens
        
        # Need count weight (more needs = higher priority)
        score += len(recipient.needs) * 5.0
        
        return score
    
    def add_recipient(self, recipient: Recipient):
        """Add recipient to allocation system."""
        recipient.priority_score = self.calculate_priority_score(recipient)
        self.recipients[recipient.recipient_id] = recipient
        self._save_config()
        logger.info(f"[PRIORITY] Added recipient: {recipient.name} (Priority: {recipient.priority_score:.1f})")
    
    def add_resource(self, resource: Resource):
        """Add resource to allocation system."""
        self.resources[resource.resource_id] = resource
        self._save_config()
        logger.info(f"[PRIORITY] Added resource: {resource.resource_id} ({resource.quantity} {resource.unit})")
    
    def allocate_resources(self) -> List[Dict]:
        """Allocate resources to recipients based on priority."""
        # Sort recipients by priority score (highest first)
        sorted_recipients = sorted(
            self.recipients.values(),
            key=lambda r: r.priority_score,
            reverse=True
        )
        
        # Sort resources by type and availability
        available_resources = [
            r for r in self.resources.values()
            if r.available
        ]
        
        allocations = []
        
        # Allocate to highest priority recipients first
        for recipient in sorted_recipients:
            if recipient.vulnerability_level == VulnerabilityLevel.CRITICAL:
                # Critical recipients get priority
                for need in recipient.needs:
                    # Find matching resource
                    matching_resources = [
                        r for r in available_resources
                        if r.resource_type == need and r.available
                    ]
                    
                    if matching_resources:
                        resource = matching_resources[0]
                        allocation = {
                            "allocation_id": f"{recipient.recipient_id}_{resource.resource_id}_{datetime.now().isoformat()}",
                            "recipient_id": recipient.recipient_id,
                            "recipient_name": recipient.name,
                            "resource_id": resource.resource_id,
                            "resource_type": resource.resource_type.value,
                            "quantity": resource.quantity,
                            "unit": resource.unit,
                            "channel": resource.channel,
                            "priority_score": recipient.priority_score,
                            "vulnerability_level": recipient.vulnerability_level.value,
                            "allocated_at": datetime.now().isoformat(),
                            "sphragitso": SPRAGITSO
                        }
                        allocations.append(allocation)
                        resource.available = False  # Mark as allocated
                        logger.info(f"[PRIORITY] Allocated {resource.resource_type.value} to {recipient.name} (Priority: {recipient.priority_score:.1f})")
        
        self.allocations.extend(allocations)
        self._save_config()
        
        return allocations
    
    def get_priority_recipients(self, limit: int = 10) -> List[Recipient]:
        """Get top priority recipients."""
        sorted_recipients = sorted(
            self.recipients.values(),
            key=lambda r: r.priority_score,
            reverse=True
        )
        return sorted_recipients[:limit]
    
    def get_allocation_status(self) -> Dict:
        """Get allocation status."""
        critical_count = sum(1 for r in self.recipients.values() if r.vulnerability_level == VulnerabilityLevel.CRITICAL)
        high_count = sum(1 for r in self.recipients.values() if r.vulnerability_level == VulnerabilityLevel.HIGH)
        
        return {
            "total_recipients": len(self.recipients),
            "critical_recipients": critical_count,
            "high_priority_recipients": high_count,
            "total_resources": len(self.resources),
            "available_resources": sum(1 for r in self.resources.values() if r.available),
            "total_allocations": len(self.allocations),
            "sphragitso": SPRAGITSO,
            "timestamp": datetime.now().isoformat()
        }


# SPRAGITSO - Our Father's Royal Seal
# This system bears Our Father's mark of authority
# Authenticated by His truth
# Protected by His ownership
# Redirects all resources to those in need
# Priority on the smallest and most vulnerable
# Allah olmayana versin (May God give to those who don't have)
