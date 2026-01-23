"""
SPIRITUAL CONTRACTS REGISTRY
Deep Search: Narratives of All Spiritual Contracts Throughout Timelines Across All Dimensions

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE SPIRITUAL BATTLEFIELD:
Spiritual battlefields are full of gods, angels fighting dark energies.
DNA tests give us the ability to link each soul to each individual.
We need to deep search the narratives of all spiritual contracts throughout our timelines across all dimensions.
Time to start putting names to faces.
"""

import sys
import json
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field, asdict
from datetime import datetime, date
from enum import Enum

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "jan-studio" / "backend"))

try:
    from temporal_heritage_registry import TimelineDimension, get_temporal_heritage_db
    from racon_registry import log_immutable_audit
    CONTRACTS_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import required modules: {e}")
    CONTRACTS_AVAILABLE = False

import logging
logger = logging.getLogger(__name__)


class ContractType(Enum):
    """Types of spiritual contracts."""
    SOUL_AGREEMENT = "soul_agreement"  # Pre-birth soul contracts
    KARMIC_CONTRACT = "karmic_contract"  # Karmic agreements
    DIVINE_COVENANT = "divine_covenant"  # Covenants with divine
    DARK_PACT = "dark_pact"  # Contracts with dark energies
    PROTECTION_CONTRACT = "protection_contract"  # Angelic protection
    SERVICE_CONTRACT = "service_contract"  # Service agreements
    HEALING_CONTRACT = "healing_contract"  # Healing agreements
    TRANSFORMATION_CONTRACT = "transformation_contract"  # Transformation pacts


class EntityType(Enum):
    """Types of spiritual entities."""
    GOD = "god"  # Divine beings
    ANGEL = "angel"  # Angelic beings
    ARCHANGEL = "archangel"  # Archangels
    DARK_ENERGY = "dark_energy"  # Dark forces
    DEMON = "demon"  # Demonic entities
    SOUL = "soul"  # Human souls
    ASCENDED_MASTER = "ascended_master"  # Ascended masters
    SPIRIT_GUIDE = "spirit_guide"  # Spirit guides
    ANCESTOR = "ancestor"  # Ancestral spirits
    ELEMENTAL = "elemental"  # Elemental beings


class BattlefieldType(Enum):
    """Types of spiritual battlefields."""
    HERITAGE_SITE = "heritage_site"  # Battle at heritage sites
    TECTONIC_BOUNDARY = "tectonic_boundary"  # Battle at plate boundaries
    SUBDUCTION_ZONE = "subduction_zone"  # Battle at subduction zones
    FIELD_SPACE = "field_space"  # Battle in field space
    TEMPORAL_BATTLE = "temporal_battle"  # Battle across timelines
    DIMENSIONAL_BATTLE = "dimensional_battle"  # Battle across dimensions
    PERSONAL_BATTLE = "personal_battle"  # Personal spiritual battle
    GLOBAL_BATTLE = "global_battle"  # Global spiritual battle


@dataclass
class SpiritualEntity:
    """A spiritual entity (god, angel, dark energy, etc.)."""
    entity_id: str
    entity_name: str
    entity_type: str
    aliases: List[str] = field(default_factory=list)
    description: str = ""
    
    # DNA/Soul connection
    dna_marker: Optional[str] = None  # DNA sequence marker
    soul_signature: Optional[str] = None  # Unique soul signature
    linked_individuals: List[str] = field(default_factory=list)  # Individual IDs
    
    # Timeline/Dimension presence
    timelines: List[str] = field(default_factory=list)
    dimensions: List[str] = field(default_factory=list)
    
    # Battlefield presence
    battlefields: List[str] = field(default_factory=list)
    
    # Metadata
    first_encountered: Optional[datetime] = None
    last_encountered: Optional[datetime] = None
    sources: List[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class SpiritualContract:
    """A spiritual contract across timelines and dimensions."""
    contract_id: str
    contract_type: str
    contract_name: str
    
    # Parties involved
    parties: List[Dict[str, str]] = field(default_factory=list)  # [{entity_id, role}]
    
    # Contract details
    terms: str = ""
    purpose: str = ""
    conditions: List[str] = field(default_factory=list)
    
    # Timeline/Dimension
    timeline_dimension: str = TimelineDimension.PRIMARY.value
    established_date: Optional[date] = None
    expiration_date: Optional[date] = None
    active: bool = True
    
    # Battlefield connection
    battlefield_id: Optional[str] = None
    battlefield_type: Optional[str] = None
    
    # DNA/Soul connection
    dna_markers: List[str] = field(default_factory=list)
    soul_signatures: List[str] = field(default_factory=list)
    linked_individuals: List[str] = field(default_factory=list)
    
    # Narrative
    narrative: str = ""
    dark_energy_detected: bool = False
    light_energy_detected: bool = False
    
    # Metadata
    sources: List[str] = field(default_factory=list)
    documented_at: datetime = field(default_factory=datetime.now)
    notes: str = ""


@dataclass
class SpiritualBattlefield:
    """A spiritual battlefield where gods, angels fight dark energies."""
    battlefield_id: str
    battlefield_name: str
    battlefield_type: str
    
    # Location
    location: Dict[str, float] = field(default_factory=dict)  # lat, lon
    heritage_site_id: Optional[int] = None
    tectonic_plate: Optional[str] = None
    
    # Entities involved
    light_entities: List[str] = field(default_factory=list)  # Entity IDs
    dark_entities: List[str] = field(default_factory=list)  # Entity IDs
    
    # Battle status
    active: bool = True
    battle_intensity: float = 0.0  # 0.0-1.0
    light_prevailing: Optional[bool] = None
    
    # Contracts at battlefield
    contracts: List[str] = field(default_factory=list)  # Contract IDs
    
    # Timeline/Dimension
    timelines: List[str] = field(default_factory=list)
    dimensions: List[str] = field(default_factory=list)
    
    # Field resonance
    field_resonance: Optional[float] = None
    field_space_activity: Optional[float] = None
    
    # Metadata
    first_documented: datetime = field(default_factory=datetime.now)
    last_updated: datetime = field(default_factory=datetime.now)
    sources: List[str] = field(default_factory=list)
    notes: str = ""


class SpiritualContractsRegistry:
    """
    Registry for spiritual contracts across all timelines and dimensions.
    
    Deep searches narratives to identify:
    - Spiritual contracts
    - Entities (gods, angels, dark energies)
    - Battlefields
    - DNA/soul connections
    """
    
    def __init__(self, data_dir: Optional[Path] = None):
        """Initialize Spiritual Contracts Registry."""
        self.data_dir = data_dir or (Path(__file__).parent.parent / "data" / "spiritual_contracts")
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Data storage files
        self.entities_file = self.data_dir / "spiritual_entities.json"
        self.contracts_file = self.data_dir / "spiritual_contracts.json"
        self.battlefields_file = self.data_dir / "spiritual_battlefields.json"
        self.dna_soul_map_file = self.data_dir / "dna_soul_mapping.json"
        
        # Load existing data
        self.entities: Dict[str, SpiritualEntity] = self._load_entities()
        self.contracts: Dict[str, SpiritualContract] = self._load_contracts()
        self.battlefields: Dict[str, SpiritualBattlefield] = self._load_battlefields()
        self.dna_soul_map: Dict[str, Dict[str, Any]] = self._load_dna_soul_map()
    
    def _load_entities(self) -> Dict[str, SpiritualEntity]:
        """Load spiritual entities."""
        if not self.entities_file.exists():
            return {}
        try:
            with open(self.entities_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return {
                entity_id: SpiritualEntity(**entity_data)
                for entity_id, entity_data in data.items()
            }
        except Exception as e:
            logger.error(f"Error loading entities: {e}")
            return {}
    
    def _save_entities(self):
        """Save entities to storage."""
        try:
            data = {
                entity_id: asdict(entity)
                for entity_id, entity in self.entities.items()
            }
            # Convert datetime to string
            for entity_data in data.values():
                if entity_data.get('first_encountered'):
                    entity_data['first_encountered'] = entity_data['first_encountered'].isoformat() if isinstance(entity_data['first_encountered'], datetime) else entity_data['first_encountered']
                if entity_data.get('last_encountered'):
                    entity_data['last_encountered'] = entity_data['last_encountered'].isoformat() if isinstance(entity_data['last_encountered'], datetime) else entity_data['last_encountered']
            
            with open(self.entities_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, default=str)
        except Exception as e:
            logger.error(f"Error saving entities: {e}")
    
    def _load_contracts(self) -> Dict[str, SpiritualContract]:
        """Load spiritual contracts."""
        if not self.contracts_file.exists():
            return {}
        try:
            with open(self.contracts_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            contracts = {}
            for contract_id, contract_data in data.items():
                # Convert date strings to date objects
                if isinstance(contract_data.get('established_date'), str):
                    contract_data['established_date'] = date.fromisoformat(contract_data['established_date'])
                if isinstance(contract_data.get('expiration_date'), str):
                    contract_data['expiration_date'] = date.fromisoformat(contract_data['expiration_date'])
                if isinstance(contract_data.get('documented_at'), str):
                    contract_data['documented_at'] = datetime.fromisoformat(contract_data['documented_at'])
                contracts[contract_id] = SpiritualContract(**contract_data)
            return contracts
        except Exception as e:
            logger.error(f"Error loading contracts: {e}")
            return {}
    
    def _save_contracts(self):
        """Save contracts to storage."""
        try:
            data = {
                contract_id: asdict(contract)
                for contract_id, contract in self.contracts.items()
            }
            # Convert dates/datetimes to strings
            for contract_data in data.values():
                if contract_data.get('established_date'):
                    contract_data['established_date'] = contract_data['established_date'].isoformat() if isinstance(contract_data['established_date'], date) else contract_data['established_date']
                if contract_data.get('expiration_date'):
                    contract_data['expiration_date'] = contract_data['expiration_date'].isoformat() if isinstance(contract_data['expiration_date'], date) else contract_data['expiration_date']
                if contract_data.get('documented_at'):
                    contract_data['documented_at'] = contract_data['documented_at'].isoformat() if isinstance(contract_data['documented_at'], datetime) else contract_data['documented_at']
            
            with open(self.contracts_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, default=str)
        except Exception as e:
            logger.error(f"Error saving contracts: {e}")
    
    def _load_battlefields(self) -> Dict[str, SpiritualBattlefield]:
        """Load spiritual battlefields."""
        if not self.battlefields_file.exists():
            return {}
        try:
            with open(self.battlefields_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            battlefields = {}
            for battlefield_id, battlefield_data in data.items():
                if isinstance(battlefield_data.get('first_documented'), str):
                    battlefield_data['first_documented'] = datetime.fromisoformat(battlefield_data['first_documented'])
                if isinstance(battlefield_data.get('last_updated'), str):
                    battlefield_data['last_updated'] = datetime.fromisoformat(battlefield_data['last_updated'])
                battlefields[battlefield_id] = SpiritualBattlefield(**battlefield_data)
            return battlefields
        except Exception as e:
            logger.error(f"Error loading battlefields: {e}")
            return {}
    
    def _save_battlefields(self):
        """Save battlefields to storage."""
        try:
            data = {
                battlefield_id: asdict(battlefield)
                for battlefield_id, battlefield in self.battlefields.items()
            }
            # Convert datetimes to strings
            for battlefield_data in data.values():
                if battlefield_data.get('first_documented'):
                    battlefield_data['first_documented'] = battlefield_data['first_documented'].isoformat() if isinstance(battlefield_data['first_documented'], datetime) else battlefield_data['first_documented']
                if battlefield_data.get('last_updated'):
                    battlefield_data['last_updated'] = battlefield_data['last_updated'].isoformat() if isinstance(battlefield_data['last_updated'], datetime) else battlefield_data['last_updated']
            
            with open(self.battlefields_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, default=str)
        except Exception as e:
            logger.error(f"Error saving battlefields: {e}")
    
    def _load_dna_soul_map(self) -> Dict[str, Dict[str, Any]]:
        """Load DNA to soul mapping."""
        if not self.dna_soul_map_file.exists():
            return {}
        try:
            with open(self.dna_soul_map_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading DNA/soul map: {e}")
            return {}
    
    def _save_dna_soul_map(self):
        """Save DNA to soul mapping."""
        try:
            with open(self.dna_soul_map_file, 'w', encoding='utf-8') as f:
                json.dump(self.dna_soul_map, f, indent=2, default=str)
        except Exception as e:
            logger.error(f"Error saving DNA/soul map: {e}")
    
    def register_entity(
        self,
        entity_name: str,
        entity_type: str,
        aliases: Optional[List[str]] = None,
        description: str = "",
        dna_marker: Optional[str] = None,
        soul_signature: Optional[str] = None,
        timelines: Optional[List[str]] = None,
        dimensions: Optional[List[str]] = None,
        sources: Optional[List[str]] = None
    ) -> SpiritualEntity:
        """
        Register a spiritual entity.
        
        Args:
            entity_name: Name of the entity
            entity_type: EntityType value
            aliases: Alternative names
            description: Entity description
            dna_marker: DNA sequence marker
            soul_signature: Unique soul signature
            timelines: Timelines where entity appears
            dimensions: Dimensions where entity appears
            sources: Research sources
        
        Returns:
            SpiritualEntity object
        """
        entity_id = f"{entity_type}_{hashlib.sha256(entity_name.encode()).hexdigest()[:8]}"
        
        entity = SpiritualEntity(
            entity_id=entity_id,
            entity_name=entity_name,
            entity_type=entity_type,
            aliases=aliases or [],
            description=description,
            dna_marker=dna_marker,
            soul_signature=soul_signature,
            timelines=timelines or [],
            dimensions=dimensions or [],
            first_encountered=datetime.now(),
            last_encountered=datetime.now(),
            sources=sources or []
        )
        
        self.entities[entity_id] = entity
        self._save_entities()
        
        logger.info(f"Registered entity: {entity_name} ({entity_id})")
        return entity
    
    def register_contract(
        self,
        contract_name: str,
        contract_type: str,
        parties: List[Dict[str, str]],
        terms: str = "",
        purpose: str = "",
        timeline_dimension: str = TimelineDimension.PRIMARY.value,
        established_date: Optional[date] = None,
        battlefield_id: Optional[str] = None,
        dna_markers: Optional[List[str]] = None,
        soul_signatures: Optional[List[str]] = None,
        narrative: str = "",
        sources: Optional[List[str]] = None
    ) -> SpiritualContract:
        """
        Register a spiritual contract.
        
        Args:
            contract_name: Name of the contract
            contract_type: ContractType value
            parties: List of parties [{entity_id, role}]
            terms: Contract terms
            purpose: Contract purpose
            timeline_dimension: Timeline dimension
            established_date: When contract was established
            battlefield_id: Associated battlefield
            dna_markers: DNA markers of parties
            soul_signatures: Soul signatures of parties
            narrative: Contract narrative
            sources: Research sources
        
        Returns:
            SpiritualContract object
        """
        contract_id = f"{contract_type}_{hashlib.sha256(contract_name.encode()).hexdigest()[:8]}"
        
        # Detect dark/light energy in narrative
        narrative_lower = narrative.lower()
        dark_energy_detected = any(term in narrative_lower for term in [
            "dark", "evil", "demonic", "cursed", "binding", "enslaved", "sacrifice"
        ])
        light_energy_detected = any(term in narrative_lower for term in [
            "light", "divine", "angelic", "blessed", "protection", "healing", "love"
        ])
        
        contract = SpiritualContract(
            contract_id=contract_id,
            contract_type=contract_type,
            contract_name=contract_name,
            parties=parties,
            terms=terms,
            purpose=purpose,
            timeline_dimension=timeline_dimension,
            established_date=established_date,
            expiration_date=None,
            active=True,
            battlefield_id=battlefield_id,
            dna_markers=dna_markers or [],
            soul_signatures=soul_signatures or [],
            narrative=narrative,
            dark_energy_detected=dark_energy_detected,
            light_energy_detected=light_energy_detected,
            sources=sources or []
        )
        
        self.contracts[contract_id] = contract
        self._save_contracts()
        
        # Link to battlefield if provided
        if battlefield_id and battlefield_id in self.battlefields:
            if contract_id not in self.battlefields[battlefield_id].contracts:
                self.battlefields[battlefield_id].contracts.append(contract_id)
                self._save_battlefields()
        
        logger.info(f"Registered contract: {contract_name} ({contract_id})")
        return contract
    
    def register_battlefield(
        self,
        battlefield_name: str,
        battlefield_type: str,
        location: Optional[Dict[str, float]] = None,
        heritage_site_id: Optional[int] = None,
        tectonic_plate: Optional[str] = None,
        light_entities: Optional[List[str]] = None,
        dark_entities: Optional[List[str]] = None,
        battle_intensity: float = 0.0,
        timelines: Optional[List[str]] = None,
        dimensions: Optional[List[str]] = None,
        sources: Optional[List[str]] = None
    ) -> SpiritualBattlefield:
        """
        Register a spiritual battlefield.
        
        Args:
            battlefield_name: Name of the battlefield
            battlefield_type: BattlefieldType value
            location: Location coordinates
            heritage_site_id: Associated heritage site
            tectonic_plate: Associated tectonic plate
            light_entities: Light entity IDs
            dark_entities: Dark entity IDs
            battle_intensity: Battle intensity (0.0-1.0)
            timelines: Timelines where battle occurs
            dimensions: Dimensions where battle occurs
            sources: Research sources
        
        Returns:
            SpiritualBattlefield object
        """
        battlefield_id = f"{battlefield_type}_{hashlib.sha256(battlefield_name.encode()).hexdigest()[:8]}"
        
        # Determine if light is prevailing
        light_prevailing = None
        if light_entities and dark_entities:
            light_prevailing = len(light_entities) > len(dark_entities)
        elif battle_intensity > 0:
            light_prevailing = battle_intensity < 0.5  # Lower intensity = light prevailing
        
        battlefield = SpiritualBattlefield(
            battlefield_id=battlefield_id,
            battlefield_name=battlefield_name,
            battlefield_type=battlefield_type,
            location=location or {},
            heritage_site_id=heritage_site_id,
            tectonic_plate=tectonic_plate,
            light_entities=light_entities or [],
            dark_entities=dark_entities or [],
            active=True,
            battle_intensity=battle_intensity,
            light_prevailing=light_prevailing,
            contracts=[],
            timelines=timelines or [],
            dimensions=dimensions or [],
            first_documented=datetime.now(),
            last_updated=datetime.now(),
            sources=sources or []
        )
        
        self.battlefields[battlefield_id] = battlefield
        self._save_battlefields()
        
        logger.info(f"Registered battlefield: {battlefield_name} ({battlefield_id})")
        return battlefield
    
    # ------------------------------------------------------------------
    # PANGEA / TABLE HELPERS FOR RESTORATION FRAMEWORK
    # ------------------------------------------------------------------

    def get_or_create_entity(
        self,
        entity_name: str,
        entity_type: str,
        **kwargs: Any,
    ) -> SpiritualEntity:
        """
        Get an existing spiritual entity by (type, name) or create it.
        
        This is used by the restoration framework so that repeated runs
        are idempotent (no duplicate entities).
        """
        # Deterministic ID logic mirrors register_entity
        entity_id = f"{entity_type}_{hashlib.sha256(entity_name.encode()).hexdigest()[:8]}"
        if entity_id in self.entities:
            return self.entities[entity_id]
        return self.register_entity(
            entity_name=entity_name,
            entity_type=entity_type,
            aliases=kwargs.get("aliases"),
            description=kwargs.get("description", ""),
            dna_marker=kwargs.get("dna_marker"),
            soul_signature=kwargs.get("soul_signature"),
            timelines=kwargs.get("timelines"),
            dimensions=kwargs.get("dimensions"),
            sources=kwargs.get("sources"),
        )

    def get_or_create_battlefield(
        self,
        battlefield_name: str,
        battlefield_type: str,
        **kwargs: Any,
    ) -> SpiritualBattlefield:
        """
        Get an existing spiritual battlefield by (type, name) or create it.
        
        Idempotent helper for the restoration framework.
        """
        battlefield_id = f"{battlefield_type}_{hashlib.sha256(battlefield_name.encode()).hexdigest()[:8]}"
        if battlefield_id in self.battlefields:
            return self.battlefields[battlefield_id]
        return self.register_battlefield(
            battlefield_name=battlefield_name,
            battlefield_type=battlefield_type,
            location=kwargs.get("location"),
            heritage_site_id=kwargs.get("heritage_site_id"),
            tectonic_plate=kwargs.get("tectonic_plate"),
            light_entities=kwargs.get("light_entities"),
            dark_entities=kwargs.get("dark_entities"),
            battle_intensity=kwargs.get("battle_intensity", 0.0),
            timelines=kwargs.get("timelines"),
            dimensions=kwargs.get("dimensions"),
            sources=kwargs.get("sources"),
        )

    def create_pangea_unified_covenant(self) -> SpiritualContract:
        """
        Create (or fetch) the Pangea Unified Covenant / Table Covenant.
        
        This is the master DIVINE_COVENANT that re-unifies all
        light-aligned contracts above plate boundaries, back to The Table.
        """
        target_name = "Pangea Unified Covenant (The Table Covenant)"

        # Return existing if already created
        for contract in self.contracts.values():
            if (
                contract.contract_type == ContractType.DIVINE_COVENANT.value
                and contract.contract_name == target_name
            ):
                return contract

        parties = [
            {"entity_id": "GOD_MOST_HIGH", "role": "origin"},
            {"entity_id": "ALL_LIGHT_ENTITIES", "role": "witnesses"},
            {"entity_id": "ALL_SOULS_WILLING", "role": "beneficiaries"},
        ]

        terms = (
            "All soul agreements, healing contracts, protection contracts and service contracts that align with love, "
            "truth, stewardship and community are hereby lifted above plate boundaries and re-anchored to Pangea as "
            "The Table. No dark pact may override this covenant where a soul freely withdraws agreement with fear, "
            "hatred, exploitation or separation."
        )
        purpose = (
            "To re-unify all light-aligned contracts across all plates and timelines under the original harmony of The Table."
        )
        narrative = (
            "This covenant does not erase history; it rescues it. What was fragmented by separation is remembered as "
            "one under God's authority. Where natural movement was twisted into fear and division, this covenant "
            "restores movement as sacred breath and reconnects all willing souls to the original unity of The Table."
        )

        return self.register_contract(
            contract_name=target_name,
            contract_type=ContractType.DIVINE_COVENANT.value,
            parties=parties,
            terms=terms,
            purpose=purpose,
            timeline_dimension=TimelineDimension.REGENERATION.value,
            established_date=date.today(),
            battlefield_id=None,
            dna_markers=None,
            soul_signatures=None,
            narrative=narrative,
            sources=["RestoreTheTable", "PangeaIntegration", "ManifestGodsWord"],
        )

    def link_contracts_to_master_covenant(self, master_contract_id: str) -> int:
        """
        Link all light-aligned contracts to the master Pangea covenant.
        
        This does NOT overwrite existing data; it appends a note so that
        every compatible contract is logically \"hung\" from the master.
        
        Returns:
            Number of contracts linked.
        """
        linked_count = 0
        for contract in self.contracts.values():
            if contract.contract_id == master_contract_id:
                continue

            if contract.contract_type not in {
                ContractType.SOUL_AGREEMENT.value,
                ContractType.HEALING_CONTRACT.value,
                ContractType.PROTECTION_CONTRACT.value,
                ContractType.SERVICE_CONTRACT.value,
                ContractType.TRANSFORMATION_CONTRACT.value,
            }:
                continue

            # Ensure we only link light-aligned ones
            if contract.dark_energy_detected and not contract.light_energy_detected:
                continue

            note_line = f"Linked to master covenant: {master_contract_id}"
            if note_line not in (contract.notes or ""):
                contract.notes = (contract.notes + "\n" if contract.notes else "") + note_line
                linked_count += 1

        if linked_count:
            self._save_contracts()

        logger.info(
            f"Linked {linked_count} contracts to master covenant {master_contract_id}"
        )
        return linked_count
    
    def link_dna_to_soul(
        self,
        individual_id: str,
        dna_sequence: str,
        soul_signature: str,
        entity_connections: Optional[List[str]] = None,
        contract_connections: Optional[List[str]] = None
    ):
        """
        Link DNA to soul signature.
        
        Args:
            individual_id: Individual identifier
            dna_sequence: DNA sequence marker
            soul_signature: Unique soul signature
            entity_connections: Connected entity IDs
            contract_connections: Connected contract IDs
        """
        self.dna_soul_map[individual_id] = {
            "dna_sequence": dna_sequence,
            "soul_signature": soul_signature,
            "entity_connections": entity_connections or [],
            "contract_connections": contract_connections or [],
            "linked_at": datetime.now().isoformat()
        }
        self._save_dna_soul_map()
        
        logger.info(f"Linked DNA to soul for individual: {individual_id}")
    
    def deep_search_contracts(
        self,
        search_term: Optional[str] = None,
        timeline_dimension: Optional[str] = None,
        entity_id: Optional[str] = None,
        contract_type: Optional[str] = None,
        dark_energy_only: bool = False,
        light_energy_only: bool = False
    ) -> List[SpiritualContract]:
        """
        Deep search spiritual contracts across all timelines and dimensions.
        
        Args:
            search_term: Search term in narrative/name
            timeline_dimension: Filter by timeline dimension
            entity_id: Filter by entity involved
            contract_type: Filter by contract type
            dark_energy_only: Only dark energy contracts
            light_energy_only: Only light energy contracts
        
        Returns:
            List of matching contracts
        """
        results = list(self.contracts.values())
        
        # Filter by search term
        if search_term:
            search_lower = search_term.lower()
            results = [
                c for c in results
                if search_lower in c.contract_name.lower() or
                   search_lower in c.narrative.lower() or
                   search_lower in c.terms.lower()
            ]
        
        # Filter by timeline dimension
        if timeline_dimension:
            results = [c for c in results if c.timeline_dimension == timeline_dimension]
        
        # Filter by entity
        if entity_id:
            results = [
                c for c in results
                if any(p.get('entity_id') == entity_id for p in c.parties)
            ]
        
        # Filter by contract type
        if contract_type:
            results = [c for c in results if c.contract_type == contract_type]
        
        # Filter by energy type
        if dark_energy_only:
            results = [c for c in results if c.dark_energy_detected]
        if light_energy_only:
            results = [c for c in results if c.light_energy_detected]
        
        return results
    
    def get_entity_by_name(self, entity_name: str) -> Optional[SpiritualEntity]:
        """Get entity by name or alias."""
        for entity in self.entities.values():
            if entity.entity_name.lower() == entity_name.lower():
                return entity
            if entity_name.lower() in [alias.lower() for alias in entity.aliases]:
                return entity
        return None
    
    def export_all_data(self, output_path: Optional[Path] = None) -> Path:
        """Export all spiritual contracts data."""
        if output_path is None:
            output_path = self.data_dir / f"spiritual_contracts_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        export_data = {
            "export_timestamp": datetime.now().isoformat(),
            "total_entities": len(self.entities),
            "total_contracts": len(self.contracts),
            "total_battlefields": len(self.battlefields),
            "total_dna_soul_mappings": len(self.dna_soul_map),
            "entities": {
                entity_id: asdict(entity)
                for entity_id, entity in self.entities.items()
            },
            "contracts": {
                contract_id: asdict(contract)
                for contract_id, contract in self.contracts.items()
            },
            "battlefields": {
                battlefield_id: asdict(battlefield)
                for battlefield_id, battlefield in self.battlefields.items()
            },
            "dna_soul_mapping": self.dna_soul_map
        }
        
        # Convert dates/datetimes to strings
        for entity_data in export_data["entities"].values():
            if entity_data.get('first_encountered'):
                entity_data['first_encountered'] = entity_data['first_encountered'].isoformat() if isinstance(entity_data['first_encountered'], datetime) else entity_data['first_encountered']
            if entity_data.get('last_encountered'):
                entity_data['last_encountered'] = entity_data['last_encountered'].isoformat() if isinstance(entity_data['last_encountered'], datetime) else entity_data['last_encountered']
        
        for contract_data in export_data["contracts"].values():
            if contract_data.get('established_date'):
                contract_data['established_date'] = contract_data['established_date'].isoformat() if isinstance(contract_data['established_date'], date) else contract_data['established_date']
            if contract_data.get('expiration_date'):
                contract_data['expiration_date'] = contract_data['expiration_date'].isoformat() if isinstance(contract_data['expiration_date'], date) else contract_data['expiration_date']
            if contract_data.get('documented_at'):
                contract_data['documented_at'] = contract_data['documented_at'].isoformat() if isinstance(contract_data['documented_at'], datetime) else contract_data['documented_at']
        
        for battlefield_data in export_data["battlefields"].values():
            if battlefield_data.get('first_documented'):
                battlefield_data['first_documented'] = battlefield_data['first_documented'].isoformat() if isinstance(battlefield_data['first_documented'], datetime) else battlefield_data['first_documented']
            if battlefield_data.get('last_updated'):
                battlefield_data['last_updated'] = battlefield_data['last_updated'].isoformat() if isinstance(battlefield_data['last_updated'], datetime) else battlefield_data['last_updated']
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, default=str)
        
        logger.info(f"Exported spiritual contracts data to {output_path}")
        return output_path


def main():
    """Example: Register spiritual entities, contracts, and battlefields."""
    print("=" * 80)
    print("SPIRITUAL CONTRACTS REGISTRY")
    print("=" * 80)
    print()
    print("Deep search: Narratives of all spiritual contracts throughout timelines")
    print("Time to start putting names to faces")
    print()
    
    registry = SpiritualContractsRegistry()
    
    # Example: Register entities
    print("Registering spiritual entities...")
    print("-" * 80)
    
    # Light entities
    archangel_michael = registry.register_entity(
        entity_name="Archangel Michael",
        entity_type=EntityType.ARCHANGEL.value,
        aliases=["Michael", "Saint Michael", "Mikhael"],
        description="Archangel of protection, warrior against dark forces",
        timelines=[TimelineDimension.PRIMARY.value, TimelineDimension.PARALLEL.value],
        dimensions=["Physical", "Astral", "Etheric", "Mental", "Causal", "Divine"],
        sources=["Biblical texts", "Spiritual traditions"]
    )
    print(f"  [OK] {archangel_michael.entity_name} ({archangel_michael.entity_id})")
    
    # Dark entities
    dark_energy_entity = registry.register_entity(
        entity_name="Dark Energy Entity",
        entity_type=EntityType.DARK_ENERGY.value,
        aliases=["The Opposer", "Dark Force"],
        description="Dark energy entity fighting against light",
        timelines=[TimelineDimension.PRIMARY.value, TimelineDimension.PAST_LOOP.value],
        dimensions=["Astral", "Etheric", "Mental"],
        sources=["Spiritual battle narratives"]
    )
    print(f"  [OK] {dark_energy_entity.entity_name} ({dark_energy_entity.entity_id})")
    
    print()
    
    # Example: Register battlefield
    print("Registering spiritual battlefields...")
    print("-" * 80)
    
    machu_picchu_battlefield = registry.register_battlefield(
        battlefield_name="Machu Picchu Spiritual Battlefield",
        battlefield_type=BattlefieldType.HERITAGE_SITE.value,
        location={"lat": -13.163, "lon": -72.545},
        heritage_site_id=10,  # Assuming Machu Picchu is site ID 10
        tectonic_plate="nazca",
        light_entities=[archangel_michael.entity_id],
        dark_entities=[dark_energy_entity.entity_id],
        battle_intensity=0.3,  # Light prevailing
        timelines=[TimelineDimension.PRIMARY.value],
        dimensions=["Physical", "Astral", "Etheric"],
        sources=["Heritage site analysis", "Field resonance data"]
    )
    print(f"  [OK] {machu_picchu_battlefield.battlefield_name} ({machu_picchu_battlefield.battlefield_id})")
    
    print()
    
    # Example: Register contract
    print("Registering spiritual contracts...")
    print("-" * 80)
    
    protection_contract = registry.register_contract(
        contract_name="Machu Picchu Protection Covenant",
        contract_type=ContractType.PROTECTION_CONTRACT.value,
        parties=[
            {"entity_id": archangel_michael.entity_id, "role": "protector"},
            {"entity_id": dark_energy_entity.entity_id, "role": "opposer"}
        ],
        terms="Archangel Michael protects Machu Picchu from dark energy influence",
        purpose="Maintain light energy at heritage site",
        timeline_dimension=TimelineDimension.PRIMARY.value,
        battlefield_id=machu_picchu_battlefield.battlefield_id,
        narrative="At Machu Picchu, a spiritual battle rages. Archangel Michael and his angelic forces protect this sacred site from dark energy entities seeking to corrupt its field resonance. The protection covenant ensures the site remains a beacon of light energy.",
        sources=["Spiritual analysis", "Field resonance data"]
    )
    print(f"  [OK] {protection_contract.contract_name} ({protection_contract.contract_id})")
    print(f"      Dark Energy Detected: {protection_contract.dark_energy_detected}")
    print(f"      Light Energy Detected: {protection_contract.light_energy_detected}")
    
    print()
    
    # Deep search
    print("Deep searching contracts...")
    print("-" * 80)
    
    search_results = registry.deep_search_contracts(
        search_term="Machu Picchu",
        light_energy_only=True
    )
    print(f"  Found {len(search_results)} contracts matching search")
    
    # Export
    export_path = registry.export_all_data()
    print()
    print(f"Exported all data to: {export_path}")
    print()
    
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("TIME TO PUT NAMES TO FACES")
    print("=" * 80)


if __name__ == "__main__":
    main()
