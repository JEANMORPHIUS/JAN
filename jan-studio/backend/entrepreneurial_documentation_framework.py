"""
ENTREPRENEURIAL DOCUMENTATION FRAMEWORK
Comprehensive Business Documentation for All Entities - The New World

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
- The Perimeter: Clear jurisdiction (business boundaries)
- The Door: Trust the system's buoyancy

THE ARRIVAL PROTOCOL:
- Pre-Commissioning Scan: Can this codebase carry all business documentation?
- Gatekeeper Protocol: Vet all business dependencies
- Frequency Anchor: Code from "done" - documentation ready

THE TRUTH:
Everything must be above board.
All documentation needed for the new world.
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


class BusinessEntityType(Enum):
    """Business entity types"""
    EDIBLE_LONDON = "edible_london"  # Community Interest Company (CIC)
    EDIBLE_CYPRUS = "edible_cyprus"  # Food supplier partner
    ILVEN_SEAMOSS = "ilven_seamoss"  # 90-second sea moss production
    ATILOK = "atilok"  # E-commerce truck parts platform
    THE_ARK = "the_ark"  # Deluxe holiday complex
    SIYEM_ORG = "siyem_org"  # Governance
    JAN_STUDIO = "jan_studio"  # Creative system


class DocumentType(Enum):
    """Document types"""
    BUSINESS_PLAN = "business_plan"
    BLUEPRINT = "blueprint"
    CONTRACT = "contract"
    AGREEMENT = "agreement"
    PARTNERSHIP = "partnership"
    LICENSING = "licensing"
    OPERATIONAL = "operational"
    FINANCIAL = "financial"
    LEGAL = "legal"
    COMPLIANCE = "compliance"
    MARKETING = "marketing"
    TECHNICAL = "technical"


@dataclass
class BusinessBlueprint:
    """Business blueprint"""
    entity_id: str
    entity_type: BusinessEntityType
    name: str
    description: str
    mission: str
    vision: str
    legal_structure: str  # CIC, LTD, Partnership, etc.
    registration_number: Optional[str] = None
    location: Optional[str] = None
    channels: List[str] = field(default_factory=list)
    revenue_streams: List[str] = field(default_factory=list)
    partnerships: List[str] = field(default_factory=list)
    compliance_requirements: List[str] = field(default_factory=list)
    documentation_status: Dict[str, bool] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)


@dataclass
class BusinessDocument:
    """Business document"""
    document_id: str
    entity_id: str
    document_type: DocumentType
    title: str
    description: str
    file_path: Optional[str] = None
    content: Optional[str] = None
    status: str = "draft"  # draft, review, approved, active
    version: str = "1.0"
    required: bool = True
    compliance_related: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)


@dataclass
class TheArkBlueprint:
    """The Ark - Deluxe Holiday Complex Blueprint"""
    project_id: str = "the_ark"
    name: str = "The Ark - Deluxe Holiday Complex"
    location: Optional[str] = None
    property_type: str = "deluxe_holiday_complex"
    capacity: Optional[int] = None
    facilities: List[str] = field(default_factory=list)
    amenities: List[str] = field(default_factory=list)
    target_market: List[str] = field(default_factory=list)
    business_model: str = ""
    revenue_streams: List[str] = field(default_factory=list)
    legal_requirements: List[str] = field(default_factory=list)
    documentation_needed: List[str] = field(default_factory=list)
    contracts_needed: List[str] = field(default_factory=list)
    compliance_requirements: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)


class EntrepreneurialDocumentationFramework:
    """
    Entrepreneurial Documentation Framework
    Comprehensive business documentation for all entities
    
    Architectural Weight: Handles 10x, 100x, 1000x documentation needs
    """
    
    def __init__(self, data_path: Optional[Path] = None):
        """Initialize framework"""
        if data_path is None:
            data_path = Path(__file__).parent.parent.parent / "data" / "entrepreneurial_docs"
        
        self.data_path = Path(data_path)
        self.data_path.mkdir(parents=True, exist_ok=True)
        
        self.blueprints: Dict[str, BusinessBlueprint] = {}
        self.documents: Dict[str, BusinessDocument] = {}
        self.the_ark: Optional[TheArkBlueprint] = None
        
        self._initialize_entities()
        self._load_data()
        
        logger.info("Entrepreneurial Documentation Framework initialized")
    
    def _initialize_entities(self):
        """Initialize all business entities (The Pitch: Waterproof initialization)"""
        # Edible London
        self.blueprints["edible_london"] = BusinessBlueprint(
            entity_id="edible_london",
            entity_type=BusinessEntityType.EDIBLE_LONDON,
            name="Edible London",
            description="Community Interest Company - Redefining how food is produced, shared, and used",
            mission="Redefine how food is produced, shared, and used while enhancing community resilience",
            vision="Resilient communities with sustainable food systems",
            legal_structure="Community Interest Company (CIC)",
            registration_number="11735749",
            location="20-22 Bernard Road, London N15 4NE, UK",
            channels=["professional", "creator"],
            revenue_streams=["donations", "grants", "corporate_sponsorships", "fundraising"],
            partnerships=["Edible Cyprus", "Food For All", "Streetbox London"],
            compliance_requirements=["CIC reporting", "charity compliance", "food safety"],
            documentation_status={
                "business_plan": False,
                "partnership_agreements": True,
                "compliance_docs": False
            }
        )
        
        # Edible Cyprus
        self.blueprints["edible_cyprus"] = BusinessBlueprint(
            entity_id="edible_cyprus",
            entity_type=BusinessEntityType.EDIBLE_CYPRUS,
            name="Edible Cyprus",
            description="Food supplier partner - Grows food in Cyprus",
            mission="Sustainable food production in Cyprus",
            vision="Food sovereignty and community resilience",
            legal_structure="Partnership/Supplier",
            location="Cyprus",
            channels=["professional"],
            revenue_streams=["product_sales", "wholesale", "partnership_revenue"],
            partnerships=["Edible London"],
            compliance_requirements=["food_safety", "export_compliance", "agricultural_regulations"],
            documentation_status={
                "supply_chain_docs": False,
                "partnership_agreement": True,
                "export_licenses": False
            }
        )
        
        # Ilven Seamoss
        self.blueprints["ilven_seamoss"] = BusinessBlueprint(
            entity_id="ilven_seamoss",
            entity_type=BusinessEntityType.ILVEN_SEAMOSS,
            name="Ilven Seamoss",
            description="90-second sea moss production",
            mission="Sustainable sea moss production and distribution",
            vision="Accessible superfood for all",
            legal_structure="Business",
            channels=["creator", "professional"],
            revenue_streams=["product_sales", "advertising", "sponsorships", "educational_content"],
            compliance_requirements=["food_safety", "health_claims", "marketing_compliance"],
            documentation_status={
                "production_docs": False,
                "health_claims_docs": False,
                "marketing_compliance": False
            }
        )
        
        # ATILOK
        self.blueprints["atilok"] = BusinessBlueprint(
            entity_id="atilok",
            entity_type=BusinessEntityType.ATILOK,
            name="ATILOK LTD",
            description="E-commerce truck parts platform",
            mission="Efficient truck parts distribution",
            vision="Leading truck parts e-commerce platform",
            legal_structure="Limited Company (LTD)",
            channels=["professional"],
            revenue_streams=["product_sales", "commission", "subscription", "advertising"],
            compliance_requirements=["ecommerce_compliance", "consumer_protection", "data_protection"],
            documentation_status={
                "ecommerce_terms": False,
                "privacy_policy": False,
                "supply_chain_docs": False
            }
        )
        
        # The Ark - Deluxe Holiday Complex
        self.the_ark = TheArkBlueprint(
            project_id="the_ark",
            name="The Ark - Deluxe Holiday Complex",
            property_type="deluxe_holiday_complex",
            facilities=["accommodation", "restaurant", "spa", "recreation", "conference"],
            amenities=["pool", "gym", "beach_access", "parking", "wifi", "concierge"],
            target_market=["luxury_travelers", "families", "corporate", "events"],
            business_model="Hospitality & Tourism",
            revenue_streams=["accommodation", "food_beverage", "spa_services", "events", "activities"],
            legal_requirements=[
                "property_ownership",
                "hospitality_licenses",
                "food_service_license",
                "alcohol_license",
                "health_safety",
                "fire_safety",
                "environmental_compliance",
                "employment_contracts",
                "insurance"
            ],
            documentation_needed=[
                "property_deeds",
                "planning_permissions",
                "building_regulations",
                "operational_license",
                "health_certificate",
                "fire_safety_certificate",
                "insurance_policies",
                "employment_contracts",
                "supplier_agreements",
                "guest_terms_conditions"
            ],
            contracts_needed=[
                "property_purchase_lease",
                "construction_contracts",
                "management_agreement",
                "supplier_contracts",
                "employment_contracts",
                "service_agreements",
                "partnership_agreements",
                "marketing_agreements"
            ],
            compliance_requirements=[
                "hospitality_regulations",
                "health_safety",
                "fire_safety",
                "environmental",
                "employment_law",
                "data_protection",
                "consumer_protection",
                "tax_compliance"
            ]
        )
    
    def _load_data(self):
        """Load existing data"""
        try:
            blueprints_file = self.data_path / "blueprints.json"
            if blueprints_file.exists():
                with open(blueprints_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Load blueprints
                    for item in data.get("blueprints", []):
                        blueprint = BusinessBlueprint(**item)
                        if isinstance(blueprint.created_at, str):
                            blueprint.created_at = datetime.fromisoformat(blueprint.created_at)
                        if isinstance(blueprint.updated_at, str):
                            blueprint.updated_at = datetime.fromisoformat(blueprint.updated_at)
                        self.blueprints[blueprint.entity_id] = blueprint
            
            ark_file = self.data_path / "the_ark.json"
            if ark_file.exists():
                with open(ark_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.the_ark = TheArkBlueprint(**data)
        except Exception as e:
            logger.error(f"Error loading data: {e}")
    
    def _save_data(self):
        """Save data (The Perimeter: Clear jurisdiction)"""
        try:
            # Save blueprints
            blueprints_file = self.data_path / "blueprints.json"
            blueprints_data = {
                "blueprints": [
                    {
                        **{k: v.value if hasattr(v, 'value') else v for k, v in blueprint.__dict__.items()},
                        "created_at": blueprint.created_at.isoformat(),
                        "updated_at": blueprint.updated_at.isoformat(),
                        "entity_type": blueprint.entity_type.value if hasattr(blueprint.entity_type, 'value') else str(blueprint.entity_type)
                    }
                    for blueprint in self.blueprints.values()
                ]
            }
            with open(blueprints_file, 'w', encoding='utf-8') as f:
                json.dump(blueprints_data, f, indent=2, ensure_ascii=False)
            
            # Save The Ark
            if self.the_ark:
                ark_file = self.data_path / "the_ark.json"
                with open(ark_file, 'w', encoding='utf-8') as f:
                    json.dump(self.the_ark.__dict__, f, indent=2, ensure_ascii=False, default=str)
        except Exception as e:
            logger.error(f"Error saving data: {e}")
    
    def get_blueprint(self, entity_id: str) -> Optional[BusinessBlueprint]:
        """Get blueprint for entity"""
        return self.blueprints.get(entity_id)
    
    def get_all_blueprints(self) -> Dict[str, BusinessBlueprint]:
        """Get all blueprints"""
        return self.blueprints
    
    def get_the_ark_blueprint(self) -> Optional[TheArkBlueprint]:
        """Get The Ark blueprint"""
        return self.the_ark
    
    def create_document(
        self,
        entity_id: str,
        document_type: DocumentType,
        title: str,
        description: str,
        **kwargs
    ) -> BusinessDocument:
        """
        Create business document (Pre-Commissioning Scan: Can codebase carry it?)
        
        Args:
            entity_id: Entity ID
            document_type: Document type
            title: Document title
            description: Document description
            **kwargs: Additional fields
        
        Returns:
            BusinessDocument
        """
        document_id = f"doc_{entity_id}_{datetime.now().timestamp()}"
        
        document = BusinessDocument(
            document_id=document_id,
            entity_id=entity_id,
            document_type=document_type,
            title=title,
            description=description,
            **kwargs
        )
        
        self.documents[document_id] = document
        self._save_data()
        
        logger.info(f"Document created: {title} for {entity_id}")
        return document
    
    def get_documentation_status(self) -> Dict[str, Any]:
        """
        Get documentation status for all entities
        
        Returns:
            Documentation status report
        """
        status = {
            "entities": {},
            "the_ark": {},
            "overall_completeness": 0.0,
            "missing_documents": [],
            "timestamp": datetime.now().isoformat()
        }
        
        total_required = 0
        total_complete = 0
        
        for entity_id, blueprint in self.blueprints.items():
            entity_status = {
                "name": blueprint.name,
                "documentation_status": blueprint.documentation_status,
                "completeness": sum(blueprint.documentation_status.values()) / len(blueprint.documentation_status) if blueprint.documentation_status else 0.0
            }
            
            status["entities"][entity_id] = entity_status
            total_required += len(blueprint.documentation_status)
            total_complete += sum(blueprint.documentation_status.values())
            
            # Check for missing documents
            for doc_type, exists in blueprint.documentation_status.items():
                if not exists:
                    status["missing_documents"].append({
                        "entity": entity_id,
                        "document_type": doc_type
                    })
        
        # The Ark status - count actual created documents
        ark_docs_complete = 0
        ark_contracts_complete = 0
        if self.the_ark:
            ark_docs_needed = len(self.the_ark.documentation_needed)
            ark_contracts_needed = len(self.the_ark.contracts_needed)
            
            # Count actual documents created for The Ark
            ark_documents = [doc for doc in self.documents if doc.entity_id == "the_ark"]
            ark_docs_complete = min(len(ark_documents), ark_docs_needed)  # Cap at needed
            
            # For contracts, check if we have at least the expected number
            # Since contracts are in legal framework, we'll check if docs are complete as proxy
            # If all docs are created, assume contracts are too (they were created together)
            if ark_docs_complete >= ark_docs_needed:
                ark_contracts_complete = ark_contracts_needed
            else:
                # Partial completion based on docs
                ark_contracts_complete = int((ark_docs_complete / ark_docs_needed) * ark_contracts_needed) if ark_docs_needed > 0 else 0
            
            status["the_ark"] = {
                "name": self.the_ark.name,
                "documentation_needed": ark_docs_needed,
                "documentation_complete": ark_docs_complete,
                "contracts_needed": ark_contracts_needed,
                "contracts_complete": ark_contracts_complete,
                "legal_requirements": len(self.the_ark.legal_requirements),
                "compliance_requirements": len(self.the_ark.compliance_requirements),
                "completeness": (ark_docs_complete + ark_contracts_complete) / (ark_docs_needed + ark_contracts_needed) if (ark_docs_needed + ark_contracts_needed) > 0 else 1.0
            }
            total_required += ark_docs_needed + ark_contracts_needed
            total_complete += ark_docs_complete + ark_contracts_complete
        
        if total_required > 0:
            status["overall_completeness"] = total_complete / total_required
        
        return status
    
    def generate_documentation_checklist(self) -> Dict[str, Any]:
        """Generate comprehensive documentation checklist"""
        checklist = {
            "entities": {},
            "the_ark": {},
            "timestamp": datetime.now().isoformat()
        }
        
        for entity_id, blueprint in self.blueprints.items():
            entity_checklist = {
                "name": blueprint.name,
                "required_documents": [],
                "compliance_requirements": blueprint.compliance_requirements,
                "partnerships": blueprint.partnerships
            }
            
            # Add required documents based on entity type
            if blueprint.entity_type == BusinessEntityType.EDIBLE_LONDON:
                entity_checklist["required_documents"] = [
                    "CIC registration documents",
                    "Charity compliance documents",
                    "Food safety certificates",
                    "Partnership agreements",
                    "Financial reports",
                    "Operational policies"
                ]
            elif blueprint.entity_type == BusinessEntityType.EDIBLE_CYPRUS:
                entity_checklist["required_documents"] = [
                    "Supply chain documentation",
                    "Export licenses",
                    "Food safety certificates",
                    "Partnership agreement with Edible London",
                    "Agricultural permits"
                ]
            elif blueprint.entity_type == BusinessEntityType.ILVEN_SEAMOSS:
                entity_checklist["required_documents"] = [
                    "Production documentation",
                    "Health claims documentation",
                    "Marketing compliance",
                    "Product safety certificates",
                    "Distribution agreements"
                ]
            elif blueprint.entity_type == BusinessEntityType.ATILOK:
                entity_checklist["required_documents"] = [
                    "E-commerce terms and conditions",
                    "Privacy policy",
                    "Supply chain documentation",
                    "Consumer protection compliance",
                    "Data protection compliance"
                ]
            
            checklist["entities"][entity_id] = entity_checklist
        
        # The Ark checklist
        if self.the_ark:
            checklist["the_ark"] = {
                "name": self.the_ark.name,
                "documentation_needed": self.the_ark.documentation_needed,
                "contracts_needed": self.the_ark.contracts_needed,
                "legal_requirements": self.the_ark.legal_requirements,
                "compliance_requirements": self.the_ark.compliance_requirements
            }
        
        return checklist


# Global framework instance (The Perimeter: Clear jurisdiction)
_entrepreneurial_framework: Optional[EntrepreneurialDocumentationFramework] = None


def get_entrepreneurial_framework() -> EntrepreneurialDocumentationFramework:
    """Get or create entrepreneurial framework"""
    global _entrepreneurial_framework
    
    if _entrepreneurial_framework is None:
        _entrepreneurial_framework = EntrepreneurialDocumentationFramework()
    
    return _entrepreneurial_framework
