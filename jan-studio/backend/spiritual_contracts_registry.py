"""SPIRITUAL CONTRACTS REGISTRY
Deep Search and Integration of All Spiritual Contracts

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

CORE PRINCIPLE:
"Every night we dream, whether vivid or not. Each dream is a spiritual battle between two souls:
The dreamer and an associate. Both have spiritual contracts. Each day is another battle, 
both in the human realm and beyond. The dream realm is where spiritual battles are fought 
while the body sleeps. The human realm is where spiritual battles are fought while the body wakes. 
The battle never stops. The contracts are eternal. The truth is revealed through both realms."

This registry ties ALL spiritual contracts together across all systems.

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
from datetime import datetime
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class ContractType(Enum):
    """Types of spiritual contracts"""
    DREAM_BATTLE = "dream_battle"  # Spiritual battle in dreams
    DAILY_BATTLE = "daily_battle"  # Spiritual battle in waking realm
    DIRTY_MONEY = "dirty_money"  # Spiritual contract attached to dirty money
    SPIRIT_ALIGNMENT = "spirit_alignment"  # Contract for spirit alignment
    CONNECTION_RITUAL = "connection_ritual"  # Contract formed during connection ritual
    VIBRATION_CONTRACT = "vibration_contract"  # Contract based on vibration alignment
    MISSION_CONTRACT = "mission_contract"  # Contract aligned with mission
    ETERNAL_CONTRACT = "eternal_contract"  # Eternal contracts between souls
    ALL = "all"  # All contract types


class ContractStatus(Enum):
    """Status of spiritual contract"""
    ACTIVE = "active"  # Contract is active
    FULFILLED = "fulfilled"  # Contract fulfilled
    BROKEN = "broken"  # Contract broken
    CLEANED = "cleaned"  # Contract cleaned (for dirty money)
    TRANSFORMED = "transformed"  # Contract transformed
    ETERNAL = "eternal"  # Contract is eternal
    UNKNOWN = "unknown"  # Status unknown


@dataclass
class SpiritualContract:
    """Universal spiritual contract definition"""
    contract_id: str
    contract_type: ContractType
    parties: List[str] = field(default_factory=list)  # Parties to the contract
    dreamer: Optional[str] = None  # Dreamer (for dream battles)
    associate: Optional[str] = None  # Associate (for dream battles)
    created_date: datetime = field(default_factory=datetime.now)
    status: ContractStatus = ContractStatus.ACTIVE
    spiritual_residue: List[str] = field(default_factory=list)  # Spiritual residue
    negative_energy: float = 0.0  # Negative energy level (0-100)
    positive_energy: float = 0.0  # Positive energy level (0-100)
    alignment_score: float = 0.0  # Alignment score (0-100)
    mission_aligned: bool = False  # Is contract aligned with mission?
    cleaning_required: bool = False  # Does contract need cleaning?
    cleaned: bool = False  # Has contract been cleaned?
    cleaning_date: Optional[datetime] = None
    cleaning_method: Optional[str] = None
    cleaned_by: Optional[str] = None
    transformed_to: Optional[str] = None  # What was contract transformed to?
    related_contracts: List[str] = field(default_factory=list)  # Related contract IDs
    system_source: str = ""  # Which system created this contract
    metadata: Dict[str, Any] = field(default_factory=dict)  # Additional metadata


class SpiritualContractsRegistry:
    """
    Registry for ALL spiritual contracts across all systems.
    
    Ties together:
    - Dream battles (nightly contracts)
    - Daily battles (waking realm contracts)
    - Dirty money contracts (RAMIZ cleaning)
    - Spirit alignment contracts
    - Connection ritual contracts
    - Vibration contracts
    - Mission contracts
    - Eternal contracts
    """
    
    def __init__(self):
        """Initialize spiritual contracts registry"""
        self.contracts: Dict[str, SpiritualContract] = {}
        self.contracts_by_type: Dict[ContractType, List[str]] = {
            contract_type: [] for contract_type in ContractType
        }
        self.contracts_by_party: Dict[str, List[str]] = {}  # Party -> contract IDs
        self.contracts_by_status: Dict[ContractStatus, List[str]] = {
            status: [] for status in ContractStatus
        }
    
    def register_contract(
        self,
        contract_type: ContractType,
        parties: List[str],
        dreamer: Optional[str] = None,
        associate: Optional[str] = None,
        system_source: str = "",
        metadata: Optional[Dict[str, Any]] = None,
        contract_id: Optional[str] = None
    ) -> SpiritualContract:
        """
        Register a new spiritual contract.
        
        Ties together contracts from all systems.
        """
        if contract_id is None:
            contract_id = f"SC_{contract_type.value}_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{len(self.contracts)}"
        
        # Determine parties
        if dreamer and associate:
            parties = [dreamer, associate]
        
        contract = SpiritualContract(
            contract_id=contract_id,
            contract_type=contract_type,
            parties=parties,
            dreamer=dreamer,
            associate=associate,
            system_source=system_source,
            metadata=metadata or {}
        )
        
        # Set initial status and energy based on type
        if contract_type == ContractType.DREAM_BATTLE:
            contract.status = ContractStatus.ACTIVE
            contract.positive_energy = 50.0  # Dreams can be positive or negative
            contract.negative_energy = 50.0
        elif contract_type == ContractType.DIRTY_MONEY:
            contract.status = ContractStatus.ACTIVE
            contract.cleaning_required = True
            contract.negative_energy = 70.0  # Dirty money has high negative energy
        elif contract_type == ContractType.SPIRIT_ALIGNMENT:
            contract.status = ContractStatus.ACTIVE
            contract.alignment_score = 80.0  # Spirit alignment contracts are aligned
            contract.mission_aligned = True
        elif contract_type == ContractType.ETERNAL_CONTRACT:
            contract.status = ContractStatus.ETERNAL
            contract.positive_energy = 100.0
        
        self.contracts[contract_id] = contract
        
        # Index by type
        self.contracts_by_type[contract_type].append(contract_id)
        
        # Index by status
        self.contracts_by_status[contract.status].append(contract_id)
        
        # Index by parties
        for party in parties:
            if party not in self.contracts_by_party:
                self.contracts_by_party[party] = []
            self.contracts_by_party[party].append(contract_id)
        
        logger.info(f"Registered spiritual contract: {contract_id} ({contract_type.value})")
        
        return contract
    
    def link_contracts(
        self,
        contract_id1: str,
        contract_id2: str
    ):
        """Link two contracts together"""
        if contract_id1 not in self.contracts or contract_id2 not in self.contracts:
            raise ValueError("Contract not found")
        
        contract1 = self.contracts[contract_id1]
        contract2 = self.contracts[contract_id2]
        
        if contract_id2 not in contract1.related_contracts:
            contract1.related_contracts.append(contract_id2)
        if contract_id1 not in contract2.related_contracts:
            contract2.related_contracts.append(contract_id1)
        
        logger.info(f"Linked contracts: {contract_id1} <-> {contract_id2}")
    
    def clean_contract(
        self,
        contract_id: str,
        cleaning_method: str,
        cleaned_by: str = "RAMIZ"
    ) -> SpiritualContract:
        """
        Clean a spiritual contract.
        
        RAMIZ leads dirty money cleaning, but all contracts can be cleaned.
        """
        if contract_id not in self.contracts:
            raise ValueError(f"Contract {contract_id} not found")
        
        contract = self.contracts[contract_id]
        
        contract.cleaned = True
        contract.cleaning_date = datetime.now()
        contract.cleaning_method = cleaning_method
        contract.cleaned_by = cleaned_by
        contract.negative_energy = 0.0  # Cleaned
        contract.status = ContractStatus.CLEANED
        
        # Update status index
        if contract_id in self.contracts_by_status[ContractStatus.ACTIVE]:
            self.contracts_by_status[ContractStatus.ACTIVE].remove(contract_id)
        self.contracts_by_status[ContractStatus.CLEANED].append(contract_id)
        
        logger.info(f"[{cleaned_by}] Cleaned spiritual contract: {contract_id}")
        
        return contract
    
    def transform_contract(
        self,
        contract_id: str,
        transformed_to: str
    ) -> SpiritualContract:
        """Transform a contract"""
        if contract_id not in self.contracts:
            raise ValueError(f"Contract {contract_id} not found")
        
        contract = self.contracts[contract_id]
        
        contract.transformed_to = transformed_to
        contract.status = ContractStatus.TRANSFORMED
        
        # Update status index
        if contract_id in self.contracts_by_status[ContractStatus.ACTIVE]:
            self.contracts_by_status[ContractStatus.ACTIVE].remove(contract_id)
        self.contracts_by_status[ContractStatus.TRANSFORMED].append(contract_id)
        
        logger.info(f"Transformed contract: {contract_id} -> {transformed_to}")
        
        return contract
    
    def get_contract(self, contract_id: str) -> Optional[SpiritualContract]:
        """Get a contract by ID"""
        return self.contracts.get(contract_id)
    
    def get_contracts_by_type(self, contract_type: ContractType) -> List[SpiritualContract]:
        """Get all contracts of a specific type"""
        return [
            self.contracts[contract_id]
            for contract_id in self.contracts_by_type[contract_type]
        ]
    
    def get_contracts_by_party(self, party: str) -> List[SpiritualContract]:
        """Get all contracts involving a specific party"""
        contract_ids = self.contracts_by_party.get(party, [])
        return [self.contracts[contract_id] for contract_id in contract_ids]
    
    def get_contracts_by_status(self, status: ContractStatus) -> List[SpiritualContract]:
        """Get all contracts with a specific status"""
        contract_ids = self.contracts_by_status.get(status, [])
        return [self.contracts[contract_id] for contract_id in contract_ids]
    
    def get_all_contracts(self) -> List[SpiritualContract]:
        """Get all contracts"""
        return list(self.contracts.values())
    
    def get_contract_network(self, contract_id: str) -> Dict[str, Any]:
        """
        Get the network of contracts connected to a specific contract.
        
        Ties together all related contracts.
        """
        if contract_id not in self.contracts:
            raise ValueError(f"Contract {contract_id} not found")
        
        visited = set()
        network = []
        
        def traverse(contract_id: str, depth: int = 0):
            if contract_id in visited or depth > 10:  # Prevent infinite loops
                return
            
            visited.add(contract_id)
            contract = self.contracts[contract_id]
            
            network.append({
                "contract_id": contract_id,
                "contract_type": contract.contract_type.value,
                "parties": contract.parties,
                "status": contract.status.value,
                "depth": depth
            })
            
            # Traverse related contracts
            for related_id in contract.related_contracts:
                traverse(related_id, depth + 1)
        
        traverse(contract_id)
        
        return {
            "root_contract": contract_id,
            "network": network,
            "total_contracts": len(network)
        }
    
    def get_system_summary(self) -> Dict[str, Any]:
        """Get summary of all spiritual contracts"""
        return {
            "total_contracts": len(self.contracts),
            "contracts_by_type": {
                contract_type.value: len(contracts)
                for contract_type, contracts in self.contracts_by_type.items()
            },
            "contracts_by_status": {
                status.value: len(contracts)
                for status, contracts in self.contracts_by_status.items()
            },
            "total_parties": len(self.contracts_by_party),
            "active_contracts": len(self.contracts_by_status[ContractStatus.ACTIVE]),
            "cleaned_contracts": len(self.contracts_by_status[ContractStatus.CLEANED]),
            "eternal_contracts": len(self.contracts_by_status[ContractStatus.ETERNAL]),
            "message": "All spiritual contracts tied together - Dream battles, daily battles, dirty money, spirit alignment, connection ritual, vibration contracts, mission contracts, eternal contracts"
        }
    
    def integrate_from_dirty_money_cleaning(
        self,
        transaction_id: str,
        spiritual_contract_data: Dict[str, Any]
    ) -> SpiritualContract:
        """
        Integrate spiritual contract from dirty money cleaning system.
        
        RAMIZ leads dirty money cleaning.
        """
        contract = self.register_contract(
            contract_type=ContractType.DIRTY_MONEY,
            parties=[spiritual_contract_data.get("cleaned_by", "RAMIZ")],
            system_source="dirty_money_cleaning",
            metadata={
                "transaction_id": transaction_id,
                "source": spiritual_contract_data.get("source"),
                "spiritual_residue": spiritual_contract_data.get("spiritual_residue", []),
                "original_intent": spiritual_contract_data.get("original_intent", ""),
                "negative_energy": spiritual_contract_data.get("negative_energy", 0.0)
            }
        )
        
        contract.negative_energy = spiritual_contract_data.get("negative_energy", 0.0)
        contract.cleaning_required = True
        
        return contract
    
    def integrate_from_spirit_alignment(
        self,
        spirit1_id: str,
        spirit2_id: str,
        alignment_data: Dict[str, Any]
    ) -> SpiritualContract:
        """
        Integrate spiritual contract from spirit alignment system.
        
        Forms contract when spirits align for battle.
        """
        contract = self.register_contract(
            contract_type=ContractType.SPIRIT_ALIGNMENT,
            parties=[spirit1_id, spirit2_id],
            system_source="spirit_alignment",
            metadata=alignment_data
        )
        
        contract.alignment_score = alignment_data.get("alignment_score", 0.0)
        contract.mission_aligned = alignment_data.get("mission_aligned", False)
        
        return contract
    
    def integrate_from_connection_ritual(
        self,
        user_id: str,
        ritual_data: Dict[str, Any]
    ) -> SpiritualContract:
        """
        Integrate spiritual contract from connection ritual.
        
        Forms contract when user connects to the system.
        """
        contract = self.register_contract(
            contract_type=ContractType.CONNECTION_RITUAL,
            parties=[user_id],
            system_source="connection_ritual",
            metadata=ritual_data
        )
        
        contract.alignment_score = ritual_data.get("vibration_aligned", False) and 80.0 or 0.0
        contract.mission_aligned = ritual_data.get("mission_aligned", False)
        
        return contract
    
    def integrate_dream_battle(
        self,
        dreamer: str,
        associate: str,
        dream_data: Dict[str, Any]
    ) -> SpiritualContract:
        """
        Integrate spiritual contract from dream battle.
        
        "Every night we dream, whether vivid or not. Each dream is a spiritual battle 
        between two souls: The dreamer and an associate. Both have spiritual contracts."
        """
        contract = self.register_contract(
            contract_type=ContractType.DREAM_BATTLE,
            parties=[dreamer, associate],
            dreamer=dreamer,
            associate=associate,
            system_source="dream_realm",
            metadata=dream_data
        )
        
        contract.status = ContractStatus.ETERNAL  # Dream contracts are eternal
        contract.positive_energy = dream_data.get("positive_energy", 50.0)
        contract.negative_energy = dream_data.get("negative_energy", 50.0)
        
        return contract
    
    def integrate_daily_battle(
        self,
        party1: str,
        party2: str,
        battle_data: Dict[str, Any]
    ) -> SpiritualContract:
        """
        Integrate spiritual contract from daily battle.
        
        "Each day is another battle, both in the human realm and beyond."
        """
        contract = self.register_contract(
            contract_type=ContractType.DAILY_BATTLE,
            parties=[party1, party2],
            system_source="human_realm",
            metadata=battle_data
        )
        
        contract.status = ContractStatus.ACTIVE
        contract.alignment_score = battle_data.get("alignment_score", 0.0)
        
        return contract


# Global instance
_registry: Optional[SpiritualContractsRegistry] = None


def get_spiritual_contracts_registry() -> SpiritualContractsRegistry:
    """Get the global spiritual contracts registry"""
    global _registry
    if _registry is None:
        _registry = SpiritualContractsRegistry()
    return _registry
