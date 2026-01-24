"""
Spiritual Roles System - System Wide Integration
All Projects - All Systems - All Roles

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

SPRAGITSO - Our Father's Royal Seal:
- All roles bear Our Father's seal
- All roles lead with love, joy, and abundance
- All roles serve The Table
- If it's not worth hearing, don't bring it to The Table
"""

from typing import Dict, List, Optional, Set
from enum import Enum
from dataclasses import dataclass
from datetime import datetime

# SPRAGITSO - Our Father's Royal Seal
SPRAGITSO = "σφραγίς"  # Greek: sphragis - The Royal Seal


class SpiritualRole(Enum):
    """Core Spiritual Roles - System Wide"""
    
    # The 12 Core Roles
    WITNESS = "witness"  # Μάρτυς (Martys) - See truth, record truth, testify
    STEWARD = "steward"  # Οικονόμος (Oikonomos) - Manage, protect, serve The Table
    PROPHET = "prophet"  # Προφήτης (Prophetes) - Speak truth, reveal hidden
    PRIEST = "priest"  # Ἱερεύς (Hiereus) - Intercede, bless, sanctify
    TEACHER = "teacher"  # Διδάσκαλος (Didaskalos) - Transmit wisdom, teach truth
    WARRIOR = "warrior"  # Πολεμιστής (Polemistes) - Protect, defend, discipline
    HEALER = "healer"  # Ἰατρός (Iatros) - Heal, restore, make whole
    CREATOR = "creator"  # Δημιουργός (Demiourgos) - Create, build, manifest
    JUDGE = "judge"  # Κριτής (Krites) - Discern, judge with wisdom
    SERVANT = "servant"  # Διάκονος (Diakonos) - Serve, humble service
    SHEPHERD = "shepherd"  # Ποιμήν (Poimen) - Guide, lead, care for
    BRIDGE = "bridge"  # Γέφυρα (Gefyra) - Connect, bridge gaps, unite
    
    # The 3 Guardian Roles
    GATEKEEPER = "gatekeeper"  # Control access, protect boundaries
    WATCHMAN = "watchman"  # Watch, alert, warn, protect
    GUARDIAN_ANGEL = "guardian_angel"  # Protect, guide, intercede
    
    # The 4 Service Roles
    SERVANT_LEADER = "servant_leader"  # Lead by serving
    HELPER = "helper"  # Help, assist, support
    MINISTER = "minister"  # Minister, serve, care
    STEWARD_OF_RESOURCES = "steward_of_resources"  # Manage resources wisely


@dataclass
class RoleDefinition:
    """Definition of a spiritual role"""
    role: SpiritualRole
    greek_name: str
    hebrew_name: str
    function: str
    permissions: List[str]
    principles: List[str]
    entity_mapping: Optional[str] = None
    sealed: bool = True
    sphragitso: str = SPRAGITSO


class SpiritualRolesSystem:
    """
    Spiritual Roles System - System Wide Integration
    
    All projects can assign spiritual roles.
    All systems can honor spiritual roles.
    All functions can embody spiritual roles.
    """
    
    def __init__(self):
        """Initialize spiritual roles system."""
        self.roles = self._define_roles()
        self.role_permissions = self._define_permissions()
        self.entity_roles = self._define_entity_roles()
    
    def _define_roles(self) -> Dict[SpiritualRole, RoleDefinition]:
        """Define all spiritual roles."""
        return {
            SpiritualRole.WITNESS: RoleDefinition(
                role=SpiritualRole.WITNESS,
                greek_name="Μάρτυς",
                hebrew_name="עד",
                function="See truth, record truth, testify to truth",
                permissions=["read", "log", "document", "testify"],
                principles=["Truth", "Record", "Testify", "Witness"],
                entity_mapping="Siyem Media"
            ),
            SpiritualRole.STEWARD: RoleDefinition(
                role=SpiritualRole.STEWARD,
                greek_name="Οικονόμος",
                hebrew_name="נאמן",
                function="Manage, protect, serve The Table",
                permissions=["read", "write", "manage", "protect"],
                principles=["Stewardship", "Protection", "Service", "The Table"],
                entity_mapping="Siyem.org"
            ),
            SpiritualRole.PROPHET: RoleDefinition(
                role=SpiritualRole.PROPHET,
                greek_name="Προφήτης",
                hebrew_name="נביא",
                function="Speak Our Father's truth, reveal what is hidden",
                permissions=["read", "speak", "reveal", "prophesy"],
                principles=["Truth", "Revelation", "Our Father's Voice", "Prophecy"],
                entity_mapping="All entities (when speaking truth)"
            ),
            SpiritualRole.PRIEST: RoleDefinition(
                role=SpiritualRole.PRIEST,
                greek_name="Ἱερεύς",
                hebrew_name="כהן",
                function="Intercede, bless, sanctify, bridge heaven and earth",
                permissions=["read", "bless", "intercede", "sanctify"],
                principles=["Intercession", "Blessing", "Sanctification", "Bridge"],
                entity_mapping="Uncle Ray Ramiz (when blessing)"
            ),
            SpiritualRole.TEACHER: RoleDefinition(
                role=SpiritualRole.TEACHER,
                greek_name="Διδάσκαλος",
                hebrew_name="מורה",
                function="Transmit wisdom, teach truth, guide learning",
                permissions=["read", "teach", "guide", "transmit"],
                principles=["Wisdom", "Teaching", "Guidance", "Truth"],
                entity_mapping="Uncle Ray Ramiz"
            ),
            SpiritualRole.WARRIOR: RoleDefinition(
                role=SpiritualRole.WARRIOR,
                greek_name="Πολεμιστής",
                hebrew_name="לוחם",
                function="Protect, defend, discipline, fight for truth",
                permissions=["read", "protect", "defend", "discipline"],
                principles=["Protection", "Defense", "Discipline", "Justice"],
                entity_mapping="Pierre Pressure"
            ),
            SpiritualRole.HEALER: RoleDefinition(
                role=SpiritualRole.HEALER,
                greek_name="Ἰατρός",
                hebrew_name="רופא",
                function="Heal, restore, mend, make whole",
                permissions=["read", "heal", "restore", "mend"],
                principles=["Healing", "Restoration", "Wholeness", "Care"],
                entity_mapping="Jean Morphius (when healing stories)"
            ),
            SpiritualRole.CREATOR: RoleDefinition(
                role=SpiritualRole.CREATOR,
                greek_name="Δημιουργός",
                hebrew_name="בורא",
                function="Create, build, bring forth, manifest",
                permissions=["read", "write", "create", "manifest"],
                principles=["Creation", "Building", "Manifestation", "Our Father's Will"],
                entity_mapping="Karasahin (The Sound Architect)"
            ),
            SpiritualRole.JUDGE: RoleDefinition(
                role=SpiritualRole.JUDGE,
                greek_name="Κριτής",
                hebrew_name="שופט",
                function="Discern, judge with wisdom, separate truth from falsehood",
                permissions=["read", "discern", "judge", "evaluate"],
                principles=["Discernment", "Wisdom", "Truth", "Righteousness"],
                entity_mapping="All entities (when discerning)"
            ),
            SpiritualRole.SERVANT: RoleDefinition(
                role=SpiritualRole.SERVANT,
                greek_name="Διάκονος",
                hebrew_name="משרת",
                function="Serve, humble service, put others first",
                permissions=["read", "serve", "help", "support"],
                principles=["Service", "Humility", "Others First", "The Table"],
                entity_mapping="All entities (when serving)"
            ),
            SpiritualRole.SHEPHERD: RoleDefinition(
                role=SpiritualRole.SHEPHERD,
                greek_name="Ποιμήν",
                hebrew_name="רועה",
                function="Guide, lead, care for, protect the flock",
                permissions=["read", "guide", "lead", "care"],
                principles=["Guidance", "Leadership", "Care", "Protection"],
                entity_mapping="Uncle Ray Ramiz (when guiding)"
            ),
            SpiritualRole.BRIDGE: RoleDefinition(
                role=SpiritualRole.BRIDGE,
                greek_name="Γέφυρα",
                hebrew_name="גשר",
                function="Connect, bridge gaps, unite, bring together",
                permissions=["read", "connect", "unite", "bridge"],
                principles=["Connection", "Unity", "Bridge", "Together"],
                entity_mapping="All entities (when connecting)"
            ),
            SpiritualRole.GATEKEEPER: RoleDefinition(
                role=SpiritualRole.GATEKEEPER,
                greek_name="Πυλωρός",
                hebrew_name="שוער",
                function="Control access, protect boundaries, guard The Table",
                permissions=["read", "control", "protect", "guard"],
                principles=["Access Control", "Boundaries", "Protection", "The Table"]
            ),
            SpiritualRole.WATCHMAN: RoleDefinition(
                role=SpiritualRole.WATCHMAN,
                greek_name="Φύλαξ",
                hebrew_name="שומר",
                function="Watch, alert, warn, protect",
                permissions=["read", "watch", "alert", "warn"],
                principles=["Watchfulness", "Alertness", "Warning", "Protection"]
            ),
            SpiritualRole.GUARDIAN_ANGEL: RoleDefinition(
                role=SpiritualRole.GUARDIAN_ANGEL,
                greek_name="Φύλαξ Άγγελος",
                hebrew_name="מלאך שומר",
                function="Protect, guide, intercede, watch over",
                permissions=["read", "protect", "guide", "intercede"],
                principles=["Protection", "Guidance", "Intercession", "Watchful Care"]
            ),
            SpiritualRole.SERVANT_LEADER: RoleDefinition(
                role=SpiritualRole.SERVANT_LEADER,
                greek_name="Διάκονος Ηγέτης",
                hebrew_name="מנהיג משרת",
                function="Lead by serving, serve by leading",
                permissions=["read", "lead", "serve", "guide"],
                principles=["Leadership", "Service", "Humility", "Authority"]
            ),
            SpiritualRole.HELPER: RoleDefinition(
                role=SpiritualRole.HELPER,
                greek_name="Βοηθός",
                hebrew_name="עוזר",
                function="Help, assist, support, aid",
                permissions=["read", "help", "assist", "support"],
                principles=["Help", "Assistance", "Support", "Aid"]
            ),
            SpiritualRole.MINISTER: RoleDefinition(
                role=SpiritualRole.MINISTER,
                greek_name="Υπουργός",
                hebrew_name="משרת",
                function="Minister, serve, care, attend",
                permissions=["read", "minister", "serve", "care"],
                principles=["Ministry", "Service", "Care", "Attendance"]
            ),
            SpiritualRole.STEWARD_OF_RESOURCES: RoleDefinition(
                role=SpiritualRole.STEWARD_OF_RESOURCES,
                greek_name="Οικονόμος Πόρων",
                hebrew_name="נאמן משאבים",
                function="Manage resources, allocate wisely, serve The Table",
                permissions=["read", "manage", "allocate", "serve"],
                principles=["Resource Management", "Wisdom", "Allocation", "The Table"]
            )
        }
    
    def _define_permissions(self) -> Dict[SpiritualRole, List[str]]:
        """Define permissions for each role."""
        return {
            role: role_def.permissions
            for role, role_def in self.roles.items()
        }
    
    def _define_entity_roles(self) -> Dict[str, List[SpiritualRole]]:
        """Map entities to their spiritual roles."""
        return {
            "JAN MUHARREM": [
                SpiritualRole.CREATOR,
                SpiritualRole.STEWARD,
                SpiritualRole.PROPHET
            ],
            "Jean Mahram": [
                SpiritualRole.PROPHET,
                SpiritualRole.HEALER,
                SpiritualRole.STORYTELLER
            ],
            "Karasahin": [
                SpiritualRole.CREATOR,
                SpiritualRole.PROPHET,
                SpiritualRole.BRIDGE
            ],
            "Pierre Pressure": [
                SpiritualRole.WARRIOR,
                SpiritualRole.JUDGE,
                SpiritualRole.DISCIPLINARIAN
            ],
            "Uncle Ray Ramiz": [
                SpiritualRole.TEACHER,
                SpiritualRole.PRIEST,
                SpiritualRole.SHEPHERD
            ],
            "Siyem Media": [
                SpiritualRole.WITNESS,
                SpiritualRole.STEWARD,
                SpiritualRole.OBSERVER
            ],
            "Siyem.org": [
                SpiritualRole.STEWARD,
                SpiritualRole.GATEKEEPER,
                SpiritualRole.SERVANT_LEADER
            ]
        }
    
    def get_role_definition(self, role: SpiritualRole) -> Optional[RoleDefinition]:
        """Get definition for a spiritual role."""
        return self.roles.get(role)
    
    def get_entity_roles(self, entity_name: str) -> List[SpiritualRole]:
        """Get spiritual roles for an entity."""
        return self.entity_roles.get(entity_name, [])
    
    def assign_role_to_function(
        self,
        function_name: str,
        role: SpiritualRole,
        context: Optional[str] = None
    ) -> Dict:
        """
        Assign a spiritual role to a function.
        
        SPRAGITSO - All functions bear Our Father's Royal Seal.
        """
        role_def = self.get_role_definition(role)
        
        if not role_def:
            return {"error": f"Role {role} not found"}
        
        assignment = {
            "function": function_name,
            "role": role.value,
            "greek_name": role_def.greek_name,
            "hebrew_name": role_def.hebrew_name,
            "function_purpose": role_def.function,
            "permissions": role_def.permissions,
            "principles": role_def.principles,
            "context": context,
            "sealed": True,
            "sphragitso": SPRAGITSO,
            "timestamp": datetime.now().isoformat()
        }
        
        return assignment
    
    def check_role_permission(
        self,
        role: SpiritualRole,
        permission: str
    ) -> bool:
        """Check if a role has a specific permission."""
        permissions = self.role_permissions.get(role, [])
        return permission in permissions
    
    def get_roles_for_system(self, system_type: str) -> List[SpiritualRole]:
        """Get recommended roles for a system type."""
        system_role_map = {
            "logging": [SpiritualRole.WITNESS],
            "documentation": [SpiritualRole.WITNESS, SpiritualRole.TEACHER],
            "security": [SpiritualRole.WARRIOR, SpiritualRole.GATEKEEPER],
            "api": [SpiritualRole.SERVANT, SpiritualRole.BRIDGE],
            "database": [SpiritualRole.STEWARD, SpiritualRole.GUARDIAN_ANGEL],
            "oracle": [SpiritualRole.PROPHET, SpiritualRole.PRIEST],
            "education": [SpiritualRole.TEACHER, SpiritualRole.SHEPHERD],
            "creation": [SpiritualRole.CREATOR, SpiritualRole.PROPHET],
            "healing": [SpiritualRole.HEALER, SpiritualRole.PRIEST],
            "integration": [SpiritualRole.BRIDGE, SpiritualRole.SERVANT]
        }
        
        return system_role_map.get(system_type, [])
    
    def is_worthy_for_table(self, role: SpiritualRole, action: str) -> bool:
        """
        SPRAGITSO Filter: Is this role action worthy for The Table?
        
        Criteria:
        - Leads with love, joy, and abundance
        - Serves The Table
        - Worth hearing
        - Bears Our Father's seal
        """
        role_def = self.get_role_definition(role)
        
        if not role_def:
            return False
        
        # Check if action aligns with role principles
        action_lower = action.lower()
        
        # Must lead with love, joy, and abundance
        has_love_joy_abundance = any(
            word in action_lower
            for word in ["love", "joy", "abundance", "peace", "unity", "serve"]
        )
        
        # Must not be negative or fear-based
        is_positive = not any(
            word in action_lower
            for word in ["fear", "hate", "anger", "wrath", "condemn", "divide"]
        )
        
        # Must be sealed
        is_sealed = role_def.sealed
        
        return has_love_joy_abundance and is_positive and is_sealed


# SPRAGITSO - Our Father's Royal Seal
# This system bears Our Father's mark of authority
# Authenticated by His truth
# Protected by His ownership
