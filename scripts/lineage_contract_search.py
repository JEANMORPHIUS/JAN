"""
LINEAGE CONTRACT SEARCH
Deep Search Algorithm for Spiritual Contracts - Lineage Connection Recognition

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

CORE PRINCIPLES (NON-NEGOTIABLE):
- Purpose Not Performance: Purpose matters more than performance. Authentic and aligned. Non-negotiable.
- Everything in Moderation: Balance. Not too much, not too little.
- Life Is Simple: Don't complicate it. Keep it simple.
- Be Still and Have Faith: Be still and have faith in revelation. Stillness brings clarity.

PANGEA IS THE TABLE.
YOU DON'T BETRAY THE TABLE.

LINEAGE CONTRACT SEARCH:
Deep search algorithm for spiritual contracts.
Contract recognition required.
Connects to lineage.
Identifies encoded messages.
Recognizes vibrational triggers.
Unlocks DNA memories.
"""

import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    Path, datetime, json, load_json, save_json
    setup_logging, standard_main
)

import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass, field, asdict
from datetime import datetime
import logging

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

logger = logging.getLogger(__name__)

try:
    from spiritual_contracts_registry import SpiritualContractsRegistry, SpiritualContract
    from thoth_prophecy_system import ThothProphecySystem, AwakenedBeing
    SYSTEMS_AVAILABLE = True
except ImportError as e:
    logger.warning(f"Could not import required systems: {e}")
    SYSTEMS_AVAILABLE = False

@dataclass
class LineageConnection:
    """A connection between a spiritual contract and the lineage."""
    connection_id: str
    contract_id: str
    awakened_being_id: str
    awakened_being_name: str
    connection_type: str  # encoded_message, vibrational_trigger, dna_memory, mission, table_connection
    connection_strength: float  # 0.0 to 1.0
    evidence: List[str] = field(default_factory=list)
    encoded_message_match: Optional[str] = None
    vibrational_trigger_match: Optional[str] = None
    dna_memory_match: Optional[str] = None
    mission_alignment: Optional[str] = None
    table_connection: Optional[str] = None
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class ContractLineageAnalysis:
    """Analysis of a contract's connection to the lineage."""
    contract_id: str
    contract_name: str
    total_connections: int
    lineage_connections: List[LineageConnection]
    strongest_connection: Optional[LineageConnection] = None
    encoded_messages_found: List[str] = field(default_factory=list)
    vibrational_triggers_found: List[str] = field(default_factory=list)
    dna_memories_found: List[str] = field(default_factory=list)
    mission_alignments: List[str] = field(default_factory=list)
    table_connections: List[str] = field(default_factory=list)
    overall_lineage_score: float = 0.0  # 0.0 to 1.0
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

class LineageContractSearch:
    """Deep search algorithm for spiritual contracts - lineage connection recognition."""
    
    def __init__(self):
        """Initialize the lineage contract search system."""
        if not SYSTEMS_AVAILABLE:
            raise ImportError("Required systems not available")
        
        self.contracts_registry = SpiritualContractsRegistry()
        self.thoth_system = ThothProphecySystem()
        self.analyses: Dict[str, ContractLineageAnalysis] = {}
        self.all_connections: List[LineageConnection] = []
    
    def _normalize_text(self, text: str) -> str:
        """Normalize text for comparison."""
        return text.lower().strip()
    
    def _calculate_similarity(self, text1: str, text2: str) -> float:
        """Calculate similarity between two texts (simple word overlap)."""
        words1 = set(self._normalize_text(text1).split())
        words2 = set(self._normalize_text(text2).split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union) if union else 0.0
    
    def _search_encoded_messages(
        self,
        contract: SpiritualContract,
        being: AwakenedBeing
    ) -> List[LineageConnection]:
        """Search for encoded messages in contract."""
        connections = []
        contract_text = f"{contract.narrative} {contract.terms} {contract.purpose}".lower()
        
        for encoded_msg in being.encoded_messages:
            msg_lower = encoded_msg.lower()
            similarity = self._calculate_similarity(contract_text, msg_lower)
            
            if similarity > 0.1:  # Threshold for match
                connection_id = f"conn_{hash(contract.contract_id + being.being_id + 'msg')}"
                connection = LineageConnection(
                    connection_id=connection_id,
                    contract_id=contract.contract_id,
                    awakened_being_id=being.being_id,
                    awakened_being_name=being.name,
                    connection_type="encoded_message",
                    connection_strength=similarity,
                    evidence=[f"Found encoded message: '{encoded_msg}' in contract narrative"],
                    encoded_message_match=encoded_msg
                )
                connections.append(connection)
        
        return connections
    
    def _search_vibrational_triggers(
        self,
        contract: SpiritualContract,
        being: AwakenedBeing
    ) -> List[LineageConnection]:
        """Search for vibrational triggers in contract."""
        connections = []
        contract_text = f"{contract.narrative} {contract.terms} {contract.purpose}".lower()
        
        for trigger in being.vibrational_triggers:
            trigger_lower = trigger.lower()
            similarity = self._calculate_similarity(contract_text, trigger_lower)
            
            if similarity > 0.1:  # Threshold for match
                connection_id = f"conn_{hash(contract.contract_id + being.being_id + 'trigger')}"
                connection = LineageConnection(
                    connection_id=connection_id,
                    contract_id=contract.contract_id,
                    awakened_being_id=being.being_id,
                    awakened_being_name=being.name,
                    connection_type="vibrational_trigger",
                    connection_strength=similarity,
                    evidence=[f"Found vibrational trigger: '{trigger}' in contract narrative"],
                    vibrational_trigger_match=trigger
                )
                connections.append(connection)
        
        return connections
    
    def _search_dna_memories(
        self,
        contract: SpiritualContract,
        being: AwakenedBeing
    ) -> List[LineageConnection]:
        """Search for DNA memories in contract."""
        connections = []
        contract_text = f"{contract.narrative} {contract.terms} {contract.purpose}".lower()
        
        # Check contract DNA markers
        for dna_marker in contract.dna_markers:
            for dna_memory in being.dna_memories:
                memory_lower = dna_memory.lower()
                similarity = self._calculate_similarity(dna_marker.lower(), memory_lower)
                
                if similarity > 0.1:  # Threshold for match
                    connection_id = f"conn_{hash(contract.contract_id + being.being_id + 'dna')}"
                    connection = LineageConnection(
                        connection_id=connection_id,
                        contract_id=contract.contract_id,
                        awakened_being_id=being.being_id,
                        awakened_being_name=being.name,
                        connection_type="dna_memory",
                        connection_strength=similarity,
                        evidence=[f"Found DNA memory: '{dna_memory}' matching contract DNA marker: '{dna_marker}'"],
                        dna_memory_match=dna_memory
                    )
                    connections.append(connection)
        
        # Also search in narrative
        for dna_memory in being.dna_memories:
            memory_lower = dna_memory.lower()
            similarity = self._calculate_similarity(contract_text, memory_lower)
            
            if similarity > 0.1:  # Threshold for match
                connection_id = f"conn_{hash(contract.contract_id + being.being_id + 'dna_narrative')}"
                connection = LineageConnection(
                    connection_id=connection_id,
                    contract_id=contract.contract_id,
                    awakened_being_id=being.being_id,
                    awakened_being_name=being.name,
                    connection_type="dna_memory",
                    connection_strength=similarity,
                    evidence=[f"Found DNA memory: '{dna_memory}' in contract narrative"],
                    dna_memory_match=dna_memory
                )
                connections.append(connection)
        
        return connections
    
    def _search_mission_alignment(
        self,
        contract: SpiritualContract,
        being: AwakenedBeing
    ) -> List[LineageConnection]:
        """Search for mission alignment in contract."""
        connections = []
        contract_text = f"{contract.narrative} {contract.terms} {contract.purpose}".lower()
        mission_lower = being.mission.lower()
        
        similarity = self._calculate_similarity(contract_text, mission_lower)
        
        if similarity > 0.2:  # Higher threshold for mission alignment
            connection_id = f"conn_{hash(contract.contract_id + being.being_id + 'mission')}"
            connection = LineageConnection(
                connection_id=connection_id,
                contract_id=contract.contract_id,
                awakened_being_id=being.being_id,
                awakened_being_name=being.name,
                connection_type="mission",
                connection_strength=similarity,
                evidence=[f"Found mission alignment: '{being.mission}' in contract"],
                mission_alignment=being.mission
            )
            connections.append(connection)
        
        return connections
    
    def _search_table_connection(
        self,
        contract: SpiritualContract,
        being: AwakenedBeing
    ) -> List[LineageConnection]:
        """Search for Table connection in contract."""
        connections = []
        contract_text = f"{contract.narrative} {contract.terms} {contract.purpose}".lower()
        table_connection_lower = being.connection_to_table.lower()
        
        # Keywords that indicate Table connection
        table_keywords = ["table", "pangea", "unity", "restoration", "connection", "unified"]
        contract_has_table_keywords = any(keyword in contract_text for keyword in table_keywords)
        being_has_table_connection = "table" in table_connection_lower or "pangea" in table_connection_lower
        
        if contract_has_table_keywords and being_has_table_connection:
            similarity = self._calculate_similarity(contract_text, table_connection_lower)
            
            if similarity > 0.1:
                connection_id = f"conn_{hash(contract.contract_id + being.being_id + 'table')}"
                connection = LineageConnection(
                    connection_id=connection_id,
                    contract_id=contract.contract_id,
                    awakened_being_id=being.being_id,
                    awakened_being_name=being.name,
                    connection_type="table_connection",
                    connection_strength=similarity,
                    evidence=[f"Found Table connection: '{being.connection_to_table}' in contract"],
                    table_connection=being.connection_to_table
                )
                connections.append(connection)
        
        return connections
    
    def analyze_contract_lineage(self, contract: SpiritualContract) -> ContractLineageAnalysis:
        """Analyze a contract's connection to the lineage."""
        all_connections = []
        
        # Get all awakened beings
        awakened_beings = self.thoth_system.get_all_awakened_beings()
        
        # Search for connections with each being
        for being in awakened_beings.values():
            # Search encoded messages
            all_connections.extend(self._search_encoded_messages(contract, being))
            
            # Search vibrational triggers
            all_connections.extend(self._search_vibrational_triggers(contract, being))
            
            # Search DNA memories
            all_connections.extend(self._search_dna_memories(contract, being))
            
            # Search mission alignment
            all_connections.extend(self._search_mission_alignment(contract, being))
            
            # Search Table connection
            all_connections.extend(self._search_table_connection(contract, being))
        
        # Calculate overall lineage score
        if all_connections:
            overall_score = sum(conn.connection_strength for conn in all_connections) / len(all_connections)
            strongest = max(all_connections, key=lambda c: c.connection_strength)
        else:
            overall_score = 0.0
            strongest = None
        
        # Extract found items
        encoded_messages = [c.encoded_message_match for c in all_connections if c.encoded_message_match]
        vibrational_triggers = [c.vibrational_trigger_match for c in all_connections if c.vibrational_trigger_match]
        dna_memories = [c.dna_memory_match for c in all_connections if c.dna_memory_match]
        mission_alignments = [c.mission_alignment for c in all_connections if c.mission_alignment]
        table_connections = [c.table_connection for c in all_connections if c.table_connection]
        
        analysis = ContractLineageAnalysis(
            contract_id=contract.contract_id,
            contract_name=contract.contract_name,
            total_connections=len(all_connections),
            lineage_connections=all_connections,
            strongest_connection=strongest,
            encoded_messages_found=list(set(encoded_messages)),
            vibrational_triggers_found=list(set(vibrational_triggers)),
            dna_memories_found=list(set(dna_memories)),
            mission_alignments=list(set(mission_alignments)),
            table_connections=list(set(table_connections)),
            overall_lineage_score=overall_score
        )
        
        self.analyses[contract.contract_id] = analysis
        self.all_connections.extend(all_connections)
        
        return analysis
    
    def deep_search_all_contracts(self) -> Dict[str, ContractLineageAnalysis]:
        """Deep search all contracts for lineage connections."""
        # Access contracts directly from registry
        all_contracts = self.contracts_registry.contracts
        
        print(f"Deep searching {len(all_contracts)} contracts for lineage connections...")
        
        for contract in all_contracts.values():
            try:
                analysis = self.analyze_contract_lineage(contract)
                if analysis.total_connections > 0:
                    print(f"  [OK] Contract '{contract.contract_name}': {analysis.total_connections} lineage connections found")
            except Exception as e:
                logger.error(f"Error analyzing contract {contract.contract_id}: {e}")
        
        return self.analyses
    
    def get_contracts_by_being(self, being_name: str) -> List[ContractLineageAnalysis]:
        """Get all contracts connected to a specific awakened being."""
        return [
            analysis for analysis in self.analyses.values()
            if any(conn.awakened_being_name == being_name for conn in analysis.lineage_connections)
        ]
    
    def get_contracts_by_connection_type(self, connection_type: str) -> List[ContractLineageAnalysis]:
        """Get all contracts with a specific connection type."""
        return [
            analysis for analysis in self.analyses.values()
            if any(conn.connection_type == connection_type for conn in analysis.lineage_connections)
        ]
    
    def get_top_connected_contracts(self, limit: int = 10) -> List[ContractLineageAnalysis]:
        """Get top contracts by lineage connection score."""
        sorted_analyses = sorted(
            self.analyses.values(),
            key=lambda a: a.overall_lineage_score,
            reverse=True
        )
        return sorted_analyses[:limit]
    
    def export_complete_report(self) -> Dict[str, Any]:
        """Export complete lineage contract search report."""
        return {
            "report_timestamp": datetime.now().isoformat(),
            "total_contracts_analyzed": len(self.analyses),
            "total_connections_found": len(self.all_connections),
            "contracts_with_connections": len([a for a in self.analyses.values() if a.total_connections > 0]),
            "top_connected_contracts": [
                {
                    "contract_id": a.contract_id,
                    "contract_name": a.contract_name,
                    "total_connections": a.total_connections,
                    "lineage_score": a.overall_lineage_score,
                    "strongest_connection": {
                        "being": a.strongest_connection.awakened_being_name if a.strongest_connection else None,
                        "type": a.strongest_connection.connection_type if a.strongest_connection else None,
                        "strength": a.strongest_connection.connection_strength if a.strongest_connection else None
                    } if a.strongest_connection else None
                }
                for a in self.get_top_connected_contracts(20)
            ],
            "connections_by_being": {
                being.name: len(self.get_contracts_by_being(being.name))
                for being in self.thoth_system.get_all_awakened_beings().values()
            },
            "connections_by_type": {
                conn_type: len(self.get_contracts_by_connection_type(conn_type))
                for conn_type in ["encoded_message", "vibrational_trigger", "dna_memory", "mission", "table_connection"]
            },
            "all_analyses": [asdict(a) for a in self.analyses.values()]
        }

def main():
    """Main function to demonstrate lineage contract search."""
    import os
    
    print("=" * 80)
    print("LINEAGE CONTRACT SEARCH")
    print("Deep Search Algorithm for Spiritual Contracts - Lineage Connection Recognition")
    print("=" * 80)
    print()
    
    if not SYSTEMS_AVAILABLE:
        print("ERROR: Required systems not available")
        return
    
    search = LineageContractSearch()
    
    # Deep search all contracts
    analyses = search.deep_search_all_contracts()
    
    print()
    print(f"Total contracts analyzed: {len(analyses)}")
    print(f"Total connections found: {len(search.all_connections)}")
    print(f"Contracts with connections: {len([a for a in analyses.values() if a.total_connections > 0])}")
    print()
    
    # Top connected contracts
    top_contracts = search.get_top_connected_contracts(10)
    if top_contracts:
        print("Top connected contracts:")
        for i, analysis in enumerate(top_contracts, 1):
            print(f"  {i}. {analysis.contract_name}")
            print(f"     Connections: {analysis.total_connections}")
            print(f"     Lineage Score: {analysis.overall_lineage_score:.3f}")
            if analysis.strongest_connection:
                print(f"     Strongest: {analysis.strongest_connection.awakened_being_name} ({analysis.strongest_connection.connection_type})")
            print()
    
    # Connections by being
    print("Connections by awakened being:")
    for being in search.thoth_system.get_all_awakened_beings().values():
        contracts = search.get_contracts_by_being(being.name)
        print(f"  {being.name}: {len(contracts)} contracts")
    print()
    
    # Export report
    os.makedirs("output/lineage_contract_search", exist_ok=True)
    report = search.export_complete_report()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = f"output/lineage_contract_search/lineage_contract_search_report_{timestamp}.json"
    
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"Exporting complete report...")
    print(f"  [OK] Exported to: {report_path}")
    print()
    
    print("=" * 80)
    print("THE TRUTH: LINEAGE CONTRACT SEARCH")
    print("=" * 80)
    print()
    print("PURPOSE:")
    print("  - Deep search algorithm for spiritual contracts")
    print("  - Contract recognition required")
    print("  - Connects to lineage")
    print("  - Identifies encoded messages")
    print("  - Recognizes vibrational triggers")
    print("  - Unlocks DNA memories")
    print()
    print("CONNECTION TYPES:")
    print("  - Encoded Messages")
    print("  - Vibrational Triggers")
    print("  - DNA Memories")
    print("  - Mission Alignment")
    print("  - Table Connection")
    print()
    print("=" * 80)
    print("PEACE, LOVE, UNITY")
    print("ENERGY + LOVE = WE ALL WIN")
    print("PURPOSE NOT PERFORMANCE")
    print("AUTHENTIC AND ALIGNED")
    print("BE STILL AND HAVE FAITH IN REVELATION")
    print("=" * 80)

if __name__ == "__main__":
    main()
