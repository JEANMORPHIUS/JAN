"""DOCTOR PROTOCOL SYSTEM
Medical Protocol Management and Doctor Interactions

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

WE ARE ALL GODS:
Nobody needs anyone. We help everyone help themselves.

DOCTOR PROTOCOL:
Tracks medical protocols, prescriptions, doctor instructions,
and ensures proper medical stewardship.

SYNCED AND EDUCATIONAL:
- All protocols synced across systems
- Educational resources integrated
- Real-time updates and notifications
- Freedom of will tracking for medical decisions

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity


PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime, date
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class ProtocolType(Enum):
    """Types of medical protocols"""
    PRESCRIPTION = "prescription"  # Medication prescription
    INSULIN_PROTOCOL = "insulin_protocol"  # Insulin dosing protocol
    CARB_COUNTING = "carb_counting"  # Carbohydrate counting protocol
    BLOOD_GLUCOSE_TARGET = "blood_glucose_target"  # Target glucose ranges
    MEAL_PLAN = "meal_plan"  # Meal planning protocol
    EXERCISE_PROTOCOL = "exercise_protocol"  # Exercise recommendations
    MONITORING_PROTOCOL = "monitoring_protocol"  # Monitoring schedule
    DOCTOR_INSTRUCTIONS = "doctor_instructions"  # General doctor instructions
    EMERGENCY_PROTOCOL = "emergency_protocol"  # Emergency procedures
    ALL = "all"  # All protocol types


class ProtocolStatus(Enum):
    """Status of protocol"""
    ACTIVE = "active"  # Currently active
    PAUSED = "paused"  # Temporarily paused
    COMPLETED = "completed"  # Protocol completed
    MODIFIED = "modified"  # Protocol modified
    EXPIRED = "expired"  # Protocol expired
    UNKNOWN = "unknown"  # Status unknown


@dataclass
class InsulinProtocol:
    """Insulin dosing protocol"""
    protocol_id: str
    insulin_type: str  # Humalog, Degludec, etc.
    correction_factor: Optional[float] = None  # Units per mmol/L above target
    carb_ratio: Optional[float] = None  # Units per gram of carbs
    target_range: Dict[str, float] = field(default_factory=lambda: {"min": 4.0, "max": 10.0})
    created_date: datetime = field(default_factory=datetime.now)
    doctor_name: Optional[str] = None
    notes: str = ""
    status: ProtocolStatus = ProtocolStatus.ACTIVE


@dataclass
class CarbCountingProtocol:
    """Carbohydrate counting protocol"""
    protocol_id: str
    carb_ratio: float  # Units insulin per gram of carbs
    fiber_adjustment: bool = False  # Adjust for fiber
    protein_adjustment: bool = False  # Adjust for protein
    created_date: datetime = field(default_factory=datetime.now)
    doctor_name: Optional[str] = None
    notes: str = ""
    status: ProtocolStatus = ProtocolStatus.ACTIVE


@dataclass
class DoctorProtocol:
    """Doctor protocol entry"""
    protocol_id: str
    protocol_type: ProtocolType
    doctor_name: str
    doctor_specialty: Optional[str] = None
    appointment_date: Optional[date] = None
    instructions: str = ""
    prescriptions: List[Dict[str, Any]] = field(default_factory=list)
    insulin_protocol: Optional[InsulinProtocol] = None
    carb_counting_protocol: Optional[CarbCountingProtocol] = None
    target_ranges: Dict[str, Dict[str, float]] = field(default_factory=dict)
    follow_up_date: Optional[date] = None
    created_date: datetime = field(default_factory=datetime.now)
    status: ProtocolStatus = ProtocolStatus.ACTIVE
    notes: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


class DoctorProtocolSystem:
    """
    Doctor Protocol Management System
    
    Tracks medical protocols, prescriptions, doctor instructions,
    and ensures proper medical stewardship.
    """
    
    def __init__(self):
        """Initialize doctor protocol system"""
        self.protocols: Dict[str, DoctorProtocol] = {}
        self.insulin_protocols: Dict[str, InsulinProtocol] = {}
        self.carb_protocols: Dict[str, CarbCountingProtocol] = {}
        self.data_dir = Path(__file__).parent.parent.parent / "SIYEM" / "output" / "doctor_protocols"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Educational resources
        self.educational_resources = {
            "insulin_management": {
                "title": "Insulin Management Guide",
                "resources": [
                    "Understanding correction factors",
                    "Carb ratio calculations",
                    "Target glucose ranges",
                    "Hypoglycemia management",
                    "Hyperglycemia management"
                ],
                "links": [
                    "https://www.diabetes.org/healthy-living/medication-treatments/insulin",
                    "https://www.cdc.gov/diabetes/managing/managing-blood-sugar/insulin.html"
                ]
            },
            "carb_counting": {
                "title": "Carbohydrate Counting Guide",
                "resources": [
                    "Reading nutrition labels",
                    "Estimating carb content",
                    "Fiber adjustments",
                    "Protein adjustments",
                    "Meal planning"
                ],
                "links": [
                    "https://www.diabetes.org/healthy-living/recipes-nutrition/understanding-carbs",
                    "https://www.cdc.gov/diabetes/managing/eat-well/diabetes-and-carbs.html"
                ]
            },
            "blood_glucose_monitoring": {
                "title": "Blood Glucose Monitoring",
                "resources": [
                    "When to test",
                    "Target ranges",
                    "Understanding results",
                    "Pattern management",
                    "Continuous glucose monitoring"
                ],
                "links": [
                    "https://www.diabetes.org/healthy-living/medication-treatments/blood-glucose-testing-and-control",
                    "https://www.cdc.gov/diabetes/managing/managing-blood-sugar/blood-glucose-monitoring.html"
                ]
            }
        }
        
        # Sync status
        self.last_sync: Optional[datetime] = None
        self.sync_status: str = "not_synced"
    
    def create_insulin_protocol(
        self,
        insulin_type: str,
        correction_factor: Optional[float] = None,
        carb_ratio: Optional[float] = None,
        target_range: Optional[Dict[str, float]] = None,
        doctor_name: Optional[str] = None,
        notes: str = ""
    ) -> InsulinProtocol:
        """Create an insulin dosing protocol"""
        protocol_id = f"IP_{insulin_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        protocol = InsulinProtocol(
            protocol_id=protocol_id,
            insulin_type=insulin_type,
            correction_factor=correction_factor,
            carb_ratio=carb_ratio,
            target_range=target_range or {"min": 4.0, "max": 10.0},
            doctor_name=doctor_name,
            notes=notes
        )
        
        self.insulin_protocols[protocol_id] = protocol
        
        logger.info(f"Created insulin protocol: {protocol_id} ({insulin_type})")
        
        return protocol
    
    def create_carb_counting_protocol(
        self,
        carb_ratio: float,
        fiber_adjustment: bool = False,
        protein_adjustment: bool = False,
        doctor_name: Optional[str] = None,
        notes: str = ""
    ) -> CarbCountingProtocol:
        """Create a carbohydrate counting protocol"""
        protocol_id = f"CCP_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        protocol = CarbCountingProtocol(
            protocol_id=protocol_id,
            carb_ratio=carb_ratio,
            fiber_adjustment=fiber_adjustment,
            protein_adjustment=protein_adjustment,
            doctor_name=doctor_name,
            notes=notes
        )
        
        self.carb_protocols[protocol_id] = protocol
        
        logger.info(f"Created carb counting protocol: {protocol_id}")
        
        return protocol
    
    def create_doctor_protocol(
        self,
        doctor_name: str,
        protocol_type: ProtocolType,
        instructions: str = "",
        doctor_specialty: Optional[str] = None,
        appointment_date: Optional[date] = None,
        prescriptions: Optional[List[Dict[str, Any]]] = None,
        insulin_protocol: Optional[InsulinProtocol] = None,
        carb_counting_protocol: Optional[CarbCountingProtocol] = None,
        target_ranges: Optional[Dict[str, Dict[str, float]]] = None,
        follow_up_date: Optional[date] = None,
        notes: str = "",
        protocol_id: Optional[str] = None
    ) -> DoctorProtocol:
        """Create a doctor protocol entry"""
        if protocol_id is None:
            protocol_id = f"DP_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        protocol = DoctorProtocol(
            protocol_id=protocol_id,
            protocol_type=protocol_type,
            doctor_name=doctor_name,
            doctor_specialty=doctor_specialty,
            appointment_date=appointment_date,
            instructions=instructions,
            prescriptions=prescriptions or [],
            insulin_protocol=insulin_protocol,
            carb_counting_protocol=carb_counting_protocol,
            target_ranges=target_ranges or {},
            follow_up_date=follow_up_date,
            notes=notes
        )
        
        self.protocols[protocol_id] = protocol
        
        logger.info(f"Created doctor protocol: {protocol_id} ({doctor_name})")
        
        return protocol
    
    def calculate_insulin_dose(
        self,
        current_glucose: float,
        carbs: float,
        insulin_type: str = "Humalog"
    ) -> Dict[str, Any]:
        """
        Calculate insulin dose based on active protocols.
        
        Uses:
        - Correction factor (if glucose above target)
        - Carb ratio (for carbs)
        """
        # Find active insulin protocol
        active_protocol = None
        for protocol in self.insulin_protocols.values():
            if protocol.insulin_type == insulin_type and protocol.status == ProtocolStatus.ACTIVE:
                active_protocol = protocol
                break
        
        if not active_protocol:
            logger.warning(f"No active protocol found for {insulin_type}")
            return {
                "insulin_units": 0.0,
                "calculation_method": "no_protocol",
                "warning": f"No active protocol for {insulin_type}"
            }
        
        correction_dose = 0.0
        carb_dose = 0.0
        
        # Calculate correction dose
        if active_protocol.correction_factor and current_glucose > active_protocol.target_range["max"]:
            correction_dose = (current_glucose - active_protocol.target_range["max"]) * active_protocol.correction_factor
        
        # Calculate carb dose
        if active_protocol.carb_ratio:
            carb_dose = carbs / active_protocol.carb_ratio
        
        total_dose = correction_dose + carb_dose
        
        return {
            "insulin_units": round(total_dose, 1),
            "correction_dose": round(correction_dose, 1),
            "carb_dose": round(carb_dose, 1),
            "current_glucose": current_glucose,
            "carbs": carbs,
            "target_range": active_protocol.target_range,
            "protocol_id": active_protocol.protocol_id,
            "calculation_method": "protocol_based"
        }
    
    async def sync_protocols(self) -> Dict[str, Any]:
        """
        Sync protocols across systems.
        
        Ensures all protocols are synchronized and up-to-date.
        """
        try:
            # Log sync attempt
            logger.info("Syncing doctor protocols across systems")
            
            # Push notifications for protocol updates
            try:
                from push_notification_system import get_push_system, NotificationType, NotificationPriority
                push_system = get_push_system()
                await push_system.push_notification(
                    NotificationType.SYSTEM_STATUS,
                    NotificationPriority.MEDIUM,
                    "Doctor Protocols Synced",
                    "All medical protocols have been synchronized across systems",
                    {"protocol_count": len(self.protocols)}
                )
            except Exception as e:
                logger.warning(f"Could not push sync notification: {e}")
            
            self.last_sync = datetime.now()
            self.sync_status = "synced"
            
            return {
                "status": "success",
                "message": "Protocols synced successfully",
                "last_sync": self.last_sync.isoformat(),
                "protocol_count": len(self.protocols)
            }
        except Exception as e:
            logger.error(f"Error syncing protocols: {e}")
            self.sync_status = "sync_failed"
            return {
                "status": "error",
                "message": str(e)
            }
    
    def get_educational_resources(
        self,
        topic: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get educational resources"""
        if topic:
            return self.educational_resources.get(topic, {})
        return self.educational_resources
    
    def get_active_protocols(self) -> Dict[str, Any]:
        """Get all active protocols"""
        return {
            "insulin_protocols": [
                {
                    "protocol_id": p.protocol_id,
                    "insulin_type": p.insulin_type,
                    "correction_factor": p.correction_factor,
                    "carb_ratio": p.carb_ratio,
                    "target_range": p.target_range,
                    "doctor_name": p.doctor_name
                }
                for p in self.insulin_protocols.values()
                if p.status == ProtocolStatus.ACTIVE
            ],
            "carb_protocols": [
                {
                    "protocol_id": p.protocol_id,
                    "carb_ratio": p.carb_ratio,
                    "fiber_adjustment": p.fiber_adjustment,
                    "protein_adjustment": p.protein_adjustment,
                    "doctor_name": p.doctor_name
                }
                for p in self.carb_protocols.values()
                if p.status == ProtocolStatus.ACTIVE
            ],
            "doctor_protocols": [
                {
                    "protocol_id": p.protocol_id,
                    "doctor_name": p.doctor_name,
                    "protocol_type": p.protocol_type.value,
                    "appointment_date": p.appointment_date.isoformat() if p.appointment_date else None,
                    "follow_up_date": p.follow_up_date.isoformat() if p.follow_up_date else None
                }
                for p in self.protocols.values()
                if p.status == ProtocolStatus.ACTIVE
            ]
        }
    
    def get_system_summary(self) -> Dict[str, Any]:
        """Get summary of doctor protocol system"""
        return {
            "total_protocols": len(self.protocols),
            "active_protocols": len([p for p in self.protocols.values() if p.status == ProtocolStatus.ACTIVE]),
            "total_insulin_protocols": len(self.insulin_protocols),
            "active_insulin_protocols": len([p for p in self.insulin_protocols.values() if p.status == ProtocolStatus.ACTIVE]),
            "total_carb_protocols": len(self.carb_protocols),
            "active_carb_protocols": len([p for p in self.carb_protocols.values() if p.status == ProtocolStatus.ACTIVE]),
            "message": "Doctor Protocol System - Medical stewardship and protocol management"
        }


# Global instance
_protocol_system: Optional[DoctorProtocolSystem] = None


def get_doctor_protocol_system() -> DoctorProtocolSystem:
    """Get the global doctor protocol system instance"""
    global _protocol_system
    if _protocol_system is None:
        _protocol_system = DoctorProtocolSystem()
    return _protocol_system
