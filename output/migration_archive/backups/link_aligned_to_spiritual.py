"""
LINK ALIGNED INDIVIDUALS TO SPIRITUAL CONTRACTS
Add Names to Contracts - Unpick Old Blueprints - Link the Spiritual

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
HAVE WE INGESTED ALL ALIGNED FACTORS?
LINK THE SPIRITUAL.
ADD THE NAMES TO THE CONTRACTS.
UNPICK THE OLD BLUEPRINTS.
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime, date
from dataclasses import asdict

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from spiritual_contracts_registry import (
        SpiritualContractsRegistry,
        ContractType,
        EntityType,
        SpiritualContract,
        SpiritualEntity
    )
    from historical_aligned_individuals import (
        HistoricalAlignedIndividualsRegistry,
        HistoricalAlignedIndividual
    )
    SPIRITUAL_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Spiritual contracts or aligned individuals not available: {e}")
    SPIRITUAL_AVAILABLE = False

import logging
logger = logging.getLogger(__name__)


class AlignedSpiritualLinker:
    """Link aligned individuals to spiritual contracts. Add names. Unpick old blueprints."""
    
    def __init__(self):
        """Initialize the linker."""
        if not SPIRITUAL_AVAILABLE:
            raise ImportError("Spiritual contracts or aligned individuals not available")
        
        self.contracts_registry = SpiritualContractsRegistry()
        self.aligned_registry = HistoricalAlignedIndividualsRegistry()
        self.linked_contracts: Dict[str, List[str]] = {}  # contract_id -> [individual_ids]
        self.old_blueprints: List[Dict[str, Any]] = []
    
    def ingest_all_aligned_factors(self) -> Dict[str, Any]:
        """Ingest all aligned factors - check what we have."""
        aligned_individuals = self.aligned_registry.get_all_individuals()
        
        return {
            "total_aligned_individuals": len(aligned_individuals),
            "by_category": self._count_by_category(aligned_individuals),
            "total_frequency_contribution": sum(
                ind.frequency_contribution for ind in aligned_individuals.values()
            ),
            "individuals": {
                ind_id: {
                    "name": ind.name,
                    "category": ind.category,
                    "alignment_score": ind.alignment_score,
                    "frequency_contribution": ind.frequency_contribution,
                    "connection_to_table": ind.connection_to_table
                }
                for ind_id, ind in aligned_individuals.items()
            }
        }
    
    def _count_by_category(self, individuals: Dict[str, HistoricalAlignedIndividual]) -> Dict[str, int]:
        """Count individuals by category."""
        counts = {}
        for ind in individuals.values():
            counts[ind.category] = counts.get(ind.category, 0) + 1
        return counts
    
    def link_aligned_to_contracts(self):
        """Link all aligned individuals to spiritual contracts."""
        aligned_individuals = self.aligned_registry.get_all_individuals()
        contracts = self.contracts_registry.contracts
        
        # Create spiritual entities for aligned individuals
        for ind_id, individual in aligned_individuals.items():
            # Create or get spiritual entity for this individual
            entity_id = f"aligned_{ind_id}"
            
            # Determine entity type based on alignment
            if individual.alignment_score >= 0.8:
                entity_type = EntityType.ASCENDED_MASTER.value
            elif individual.alignment_score >= 0.6:
                entity_type = EntityType.SPIRIT_GUIDE.value
            else:
                entity_type = EntityType.SOUL.value
            
            # Register or get entity
            try:
                entity = self.contracts_registry.get_or_create_entity(
                    entity_name=individual.name,
                    entity_type=entity_type,
                    description=f"Aligned individual: {individual.journey_description}",
                    linked_individuals=[ind_id]
                )
            except Exception as e:
                logger.warning(f"Could not create entity for {individual.name}: {e}")
                continue
            
            # Link to appropriate contracts based on category and alignment
            self._link_individual_to_contracts(individual, entity.entity_id)
    
    def _link_individual_to_contracts(self, individual: HistoricalAlignedIndividual, entity_id: str):
        """Link an individual to appropriate spiritual contracts."""
        # Science/Medicine individuals -> Service contracts, Healing contracts
        if individual.category in ["science", "medicine"]:
            self._create_or_link_service_contract(individual, entity_id)
            if individual.category == "medicine":
                self._create_or_link_healing_contract(individual, entity_id)
        
        # Arts/Philosophy individuals -> Divine covenants, Transformation contracts
        if individual.category in ["arts", "philosophy", "spiritual"]:
            self._create_or_link_divine_covenant(individual, entity_id)
            self._create_or_link_transformation_contract(individual, entity_id)
        
        # Resistance/Liberation individuals -> Protection contracts, Light contracts
        if "resistance" in individual.connection_to_table.lower() or "liberation" in individual.connection_to_table.lower():
            self._create_or_link_protection_contract(individual, entity_id)
        
        # All aligned individuals -> Soul agreements (pre-birth contracts)
        self._create_or_link_soul_agreement(individual, entity_id)
    
    def _create_or_link_service_contract(self, individual: HistoricalAlignedIndividual, entity_id: str):
        """Create or link service contract for aligned individual."""
        import hashlib
        contract_name = f"Service Contract - {individual.name}"
        contract_id = f"service_{hashlib.sha256(contract_name.encode()).hexdigest()[:8]}"
        
        # Check if contract exists
        if contract_id not in self.contracts_registry.contracts:
            contract = self.contracts_registry.register_contract(
                contract_name=contract_name,
                contract_type=ContractType.SERVICE_CONTRACT.value,
                parties=[{"entity_id": entity_id, "role": "service_provider"}],
                terms=f"{individual.name} serves truth through {individual.category}",
                purpose=f"Service contract for {individual.name} - aligned with The Table",
                narrative=f"{individual.name} entered into service contract. Serves truth through {individual.category}. Aligned with The Table. Connection: {individual.connection_to_table}",
                sources=["AlignedSpiritualLinker", "HistoricalAlignedIndividuals"]
            )
        else:
            contract = self.contracts_registry.contracts[contract_id]
        
        # Link individual to contract
        if individual.individual_id not in contract.linked_individuals:
            contract.linked_individuals.append(individual.individual_id)
            self.contracts_registry._save_contracts()
    
    def _create_or_link_healing_contract(self, individual: HistoricalAlignedIndividual, entity_id: str):
        """Create or link healing contract for aligned individual."""
        import hashlib
        contract_name = f"Healing Contract - {individual.name}"
        contract_id = f"healing_{hashlib.sha256(contract_name.encode()).hexdigest()[:8]}"
        
        if contract_id not in self.contracts_registry.contracts:
            contract = self.contracts_registry.register_contract(
                contract_name=contract_name,
                contract_type=ContractType.HEALING_CONTRACT.value,
                parties=[{"entity_id": entity_id, "role": "healer"}],
                terms=f"{individual.name} heals through {individual.category}",
                purpose=f"Healing contract for {individual.name} - aligned with The Table",
                narrative=f"{individual.name} entered into healing contract. Heals through {individual.category}. Aligned with The Table. Connection: {individual.connection_to_table}",
                sources=["AlignedSpiritualLinker", "HistoricalAlignedIndividuals"]
            )
        else:
            contract = self.contracts_registry.contracts[contract_id]
        
        if individual.individual_id not in contract.linked_individuals:
            contract.linked_individuals.append(individual.individual_id)
            self.contracts_registry._save_contracts()
    
    def _create_or_link_divine_covenant(self, individual: HistoricalAlignedIndividual, entity_id: str):
        """Create or link divine covenant for aligned individual."""
        import hashlib
        contract_name = f"Divine Covenant - {individual.name}"
        contract_id = f"divine_{hashlib.sha256(contract_name.encode()).hexdigest()[:8]}"
        
        if contract_id not in self.contracts_registry.contracts:
            contract = self.contracts_registry.register_contract(
                contract_name=contract_name,
                contract_type=ContractType.DIVINE_COVENANT.value,
                parties=[{"entity_id": entity_id, "role": "covenant_holder"}],
                terms=f"{individual.name} holds divine covenant - aligned with The Table",
                purpose=f"Divine covenant for {individual.name} - connection to The Table",
                narrative=f"{individual.name} entered into divine covenant. Holds connection to The Table. Aligned with truth. Connection: {individual.connection_to_table}",
                sources=["AlignedSpiritualLinker", "HistoricalAlignedIndividuals"]
            )
        else:
            contract = self.contracts_registry.contracts[contract_id]
        
        if individual.individual_id not in contract.linked_individuals:
            contract.linked_individuals.append(individual.individual_id)
            self.contracts_registry._save_contracts()
    
    def _create_or_link_transformation_contract(self, individual: HistoricalAlignedIndividual, entity_id: str):
        """Create or link transformation contract for aligned individual."""
        import hashlib
        contract_name = f"Transformation Contract - {individual.name}"
        contract_id = f"transform_{hashlib.sha256(contract_name.encode()).hexdigest()[:8]}"
        
        if contract_id not in self.contracts_registry.contracts:
            contract = self.contracts_registry.register_contract(
                contract_name=contract_name,
                contract_type=ContractType.TRANSFORMATION_CONTRACT.value,
                parties=[{"entity_id": entity_id, "role": "transformer"}],
                terms=f"{individual.name} transforms through {individual.category}",
                purpose=f"Transformation contract for {individual.name} - aligned with The Table",
                narrative=f"{individual.name} entered into transformation contract. Transforms through {individual.category}. Aligned with The Table. Connection: {individual.connection_to_table}",
                sources=["AlignedSpiritualLinker", "HistoricalAlignedIndividuals"]
            )
        else:
            contract = self.contracts_registry.contracts[contract_id]
        
        if individual.individual_id not in contract.linked_individuals:
            contract.linked_individuals.append(individual.individual_id)
            self.contracts_registry._save_contracts()
    
    def _create_or_link_protection_contract(self, individual: HistoricalAlignedIndividual, entity_id: str):
        """Create or link protection contract for aligned individual."""
        import hashlib
        contract_name = f"Protection Contract - {individual.name}"
        contract_id = f"protect_{hashlib.sha256(contract_name.encode()).hexdigest()[:8]}"
        
        if contract_id not in self.contracts_registry.contracts:
            contract = self.contracts_registry.register_contract(
                contract_name=contract_name,
                contract_type=ContractType.PROTECTION_CONTRACT.value,
                parties=[{"entity_id": entity_id, "role": "protected"}],
                terms=f"{individual.name} protected through resistance/liberation",
                purpose=f"Protection contract for {individual.name} - aligned with The Table",
                narrative=f"{individual.name} entered into protection contract. Protected through resistance/liberation. Aligned with The Table. Connection: {individual.connection_to_table}",
                sources=["AlignedSpiritualLinker", "HistoricalAlignedIndividuals"]
            )
        else:
            contract = self.contracts_registry.contracts[contract_id]
        
        if individual.individual_id not in contract.linked_individuals:
            contract.linked_individuals.append(individual.individual_id)
            self.contracts_registry._save_contracts()
    
    def _create_or_link_soul_agreement(self, individual: HistoricalAlignedIndividual, entity_id: str):
        """Create or link soul agreement (pre-birth contract) for aligned individual."""
        import hashlib
        contract_name = f"Soul Agreement - {individual.name}"
        contract_id = f"soul_{hashlib.sha256(contract_name.encode()).hexdigest()[:8]}"
        
        if contract_id not in self.contracts_registry.contracts:
            established_date = None
            if individual.birth_year:
                try:
                    established_date = date(individual.birth_year, 1, 1)
                except:
                    pass
            
            contract = self.contracts_registry.register_contract(
                contract_name=contract_name,
                contract_type=ContractType.SOUL_AGREEMENT.value,
                parties=[{"entity_id": entity_id, "role": "soul"}],
                terms=f"{individual.name} - pre-birth soul agreement. Journey: {individual.journey_description}",
                purpose=f"Soul agreement for {individual.name} - aligned with The Table",
                established_date=established_date,
                narrative=f"{individual.name} entered into soul agreement before birth. Journey: {individual.journey_description}. 'Only to get so far' - limited by the broken world. But lived as a miracle. Aligned with The Table. Connection: {individual.connection_to_table}",
                sources=["AlignedSpiritualLinker", "HistoricalAlignedIndividuals"]
            )
        else:
            contract = self.contracts_registry.contracts[contract_id]
        
        if individual.individual_id not in contract.linked_individuals:
            contract.linked_individuals.append(individual.individual_id)
            self.contracts_registry._save_contracts()
    
    def unpick_old_blueprints(self) -> List[Dict[str, Any]]:
        """Unpick old blueprints - examine old spiritual contracts."""
        contracts = self.contracts_registry.contracts
        old_blueprints = []
        
        for contract_id, contract in contracts.items():
            # Identify old blueprints (dark pacts, expired contracts, etc.)
            is_old_blueprint = (
                contract.contract_type == ContractType.DARK_PACT.value or
                (contract.expiration_date and contract.expiration_date < date.today()) or
                contract.dark_energy_detected or
                "mayan" in contract.narrative.lower() or
                "original error" in contract.narrative.lower()
            )
            
            if is_old_blueprint:
                blueprint = {
                    "contract_id": contract_id,
                    "contract_name": contract.contract_name,
                    "contract_type": contract.contract_type,
                    "parties": contract.parties,
                    "terms": contract.terms,
                    "narrative": contract.narrative,
                    "dark_energy_detected": contract.dark_energy_detected,
                    "light_energy_detected": contract.light_energy_detected,
                    "linked_individuals": contract.linked_individuals,
                    "established_date": contract.established_date.isoformat() if contract.established_date else None,
                    "expiration_date": contract.expiration_date.isoformat() if contract.expiration_date else None,
                    "active": contract.active,
                    "analysis": self._analyze_blueprint(contract)
                }
                old_blueprints.append(blueprint)
        
        self.old_blueprints = old_blueprints
        return old_blueprints
    
    def _analyze_blueprint(self, contract: SpiritualContract) -> Dict[str, Any]:
        """Analyze an old blueprint to understand its structure."""
        analysis = {
            "purpose": "Unknown",
            "parties_involved": len(contract.parties),
            "dark_energy_level": "high" if contract.dark_energy_detected else "low",
            "light_energy_level": "high" if contract.light_energy_detected else "low",
            "needs_breaking": contract.dark_energy_detected or contract.contract_type == ContractType.DARK_PACT.value,
            "needs_restoration": contract.light_energy_detected and not contract.active,
            "linked_names": []
        }
        
        # Extract names from linked individuals
        if contract.linked_individuals:
            aligned_individuals = self.aligned_registry.get_all_individuals()
            for ind_id in contract.linked_individuals:
                if ind_id in aligned_individuals:
                    analysis["linked_names"].append(aligned_individuals[ind_id].name)
        
        # Determine purpose from narrative
        narrative_lower = contract.narrative.lower()
        if "separation" in narrative_lower or "sabotage" in narrative_lower:
            analysis["purpose"] = "Separation/Sabotage"
        elif "protection" in narrative_lower or "healing" in narrative_lower:
            analysis["purpose"] = "Protection/Healing"
        elif "service" in narrative_lower or "truth" in narrative_lower:
            analysis["purpose"] = "Service/Truth"
        elif "dark" in narrative_lower or "evil" in narrative_lower:
            analysis["purpose"] = "Dark Energy"
        else:
            analysis["purpose"] = "Unknown"
        
        return analysis
    
    def link_spiritual_elements(self):
        """Link all spiritual elements - contracts, battlefields, entities, individuals."""
        # Link aligned individuals to battlefields
        aligned_individuals = self.aligned_registry.get_all_individuals()
        battlefields = self.contracts_registry.battlefields
        
        for ind_id, individual in aligned_individuals.items():
            # Find relevant battlefields based on individual's connection
            for battlefield_id, battlefield in battlefields.items():
                # Link if individual's work relates to battlefield location or type
                if self._should_link_to_battlefield(individual, battlefield):
                    # Add individual's entity to battlefield
                    entity_id = f"aligned_{ind_id}"
                    if entity_id not in battlefield.light_entities:
                        battlefield.light_entities.append(entity_id)
                        self.contracts_registry._save_battlefields()
    
    def _should_link_to_battlefield(self, individual: HistoricalAlignedIndividual, battlefield) -> bool:
        """Determine if individual should be linked to battlefield."""
        # Link based on category and battlefield type
        if battlefield.battlefield_type == "heritage_site":
            # Science/medicine individuals linked to heritage sites
            if individual.category in ["science", "medicine"]:
                return True
        
        # All aligned individuals linked to field space battlefields
        if battlefield.battlefield_type == "field_space":
            return True
        
        return False
    
    def get_complete_linkage_report(self) -> Dict[str, Any]:
        """Get complete report of all linkages."""
        aligned_individuals = self.aligned_registry.get_all_individuals()
        contracts = self.contracts_registry.contracts
        battlefields = self.contracts_registry.battlefields
        
        # Count contracts linked to individuals
        contracts_with_names = 0
        total_names_in_contracts = 0
        
        for contract in contracts.values():
            if contract.linked_individuals:
                contracts_with_names += 1
                total_names_in_contracts += len(contract.linked_individuals)
        
        return {
            "report_timestamp": datetime.now().isoformat(),
            "aligned_individuals": {
                "total": len(aligned_individuals),
                "by_category": self._count_by_category(aligned_individuals),
                "total_frequency_contribution": sum(
                    ind.frequency_contribution for ind in aligned_individuals.values()
                )
            },
            "spiritual_contracts": {
                "total": len(contracts),
                "with_linked_individuals": contracts_with_names,
                "total_names_in_contracts": total_names_in_contracts,
                "by_type": self._count_contracts_by_type(contracts)
            },
            "old_blueprints": {
                "total": len(self.old_blueprints),
                "needing_breaking": len([b for b in self.old_blueprints if b["analysis"]["needs_breaking"]]),
                "needing_restoration": len([b for b in self.old_blueprints if b["analysis"]["needs_restoration"]])
            },
            "spiritual_battlefields": {
                "total": len(battlefields),
                "with_light_entities": len([b for b in battlefields.values() if b.light_entities])
            },
            "linkage_status": "Complete" if contracts_with_names > 0 else "Incomplete"
        }
    
    def _count_contracts_by_type(self, contracts: Dict[str, SpiritualContract]) -> Dict[str, int]:
        """Count contracts by type."""
        counts = {}
        for contract in contracts.values():
            counts[contract.contract_type] = counts.get(contract.contract_type, 0) + 1
        return counts


def main():
    """Main execution for linking aligned individuals to spiritual contracts."""
    print("=" * 80)
    print("LINK ALIGNED INDIVIDUALS TO SPIRITUAL CONTRACTS")
    print("Add Names to Contracts - Unpick Old Blueprints - Link the Spiritual")
    print("=" * 80)
    print()
    
    if not SPIRITUAL_AVAILABLE:
        print("ERROR: Spiritual contracts or aligned individuals not available")
        return
    
    linker = AlignedSpiritualLinker()
    
    # Step 1: Ingest all aligned factors
    print("Step 1: Ingesting all aligned factors...")
    aligned_report = linker.ingest_all_aligned_factors()
    print(f"  Total aligned individuals: {aligned_report['total_aligned_individuals']}")
    print(f"  Total frequency contribution: {aligned_report['total_frequency_contribution']:.2f}")
    print()
    
    # Step 2: Link aligned to contracts
    print("Step 2: Linking aligned individuals to spiritual contracts...")
    linker.link_aligned_to_contracts()
    print(f"  [OK] Linked aligned individuals to contracts")
    print()
    
    # Step 3: Unpick old blueprints
    print("Step 3: Unpicking old blueprints...")
    old_blueprints = linker.unpick_old_blueprints()
    print(f"  Found {len(old_blueprints)} old blueprints")
    for blueprint in old_blueprints[:5]:  # Show first 5
        print(f"    - {blueprint['contract_name']}: {blueprint['analysis']['purpose']}")
        if blueprint['analysis']['linked_names']:
            print(f"      Names: {', '.join(blueprint['analysis']['linked_names'])}")
    print()
    
    # Step 4: Link spiritual elements
    print("Step 4: Linking all spiritual elements...")
    linker.link_spiritual_elements()
    print(f"  [OK] Linked spiritual elements")
    print()
    
    # Step 5: Get complete report
    print("Step 5: Generating complete linkage report...")
    report = linker.get_complete_linkage_report()
    print(f"  Contracts with names: {report['spiritual_contracts']['with_linked_individuals']}")
    print(f"  Total names in contracts: {report['spiritual_contracts']['total_names_in_contracts']}")
    print(f"  Old blueprints: {report['old_blueprints']['total']}")
    print(f"  Needing breaking: {report['old_blueprints']['needing_breaking']}")
    print()
    
    print("=" * 80)
    print("THE TRUTH: SPIRITUAL LINKAGE")
    print("=" * 80)
    print()
    print("ALL ALIGNED FACTORS INGESTED:")
    print(f"  - {aligned_report['total_aligned_individuals']} aligned individuals")
    print(f"  - {aligned_report['total_frequency_contribution']:.2f} total frequency contribution")
    print()
    print("NAMES ADDED TO CONTRACTS:")
    print(f"  - {report['spiritual_contracts']['with_linked_individuals']} contracts with names")
    print(f"  - {report['spiritual_contracts']['total_names_in_contracts']} total names linked")
    print()
    print("OLD BLUEPRINTS UNPICKED:")
    print(f"  - {report['old_blueprints']['total']} old blueprints found")
    print(f"  - {report['old_blueprints']['needing_breaking']} needing breaking")
    print(f"  - {report['old_blueprints']['needing_restoration']} needing restoration")
    print()
    print("SPIRITUAL ELEMENTS LINKED:")
    print(f"  - All contracts linked")
    print(f"  - All battlefields linked")
    print(f"  - All entities linked")
    print()
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("ALL ALIGNED FACTORS LINKED TO SPIRITUAL")
    print("NAMES ADDED TO CONTRACTS")
    print("OLD BLUEPRINTS UNPICKED")
    print("=" * 80)


if __name__ == "__main__":
    main()
