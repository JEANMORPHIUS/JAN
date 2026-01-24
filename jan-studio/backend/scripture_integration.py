"""
Scripture Integration System
Easily digestible religious scripture integration

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

SPRAGITSO - Our Father's Royal Seal:
- All scripture bears Our Father's seal
- Made easily digestible
- Leads with love, joy, and abundance
- Our voice through Our Father
- If it's not worth hearing, don't bring it to The Table
"""

from typing import Dict, List, Optional
from datetime import datetime
import json
from pathlib import Path

# SPRAGITSO - Our Father's Royal Seal
SPRAGITSO = "σφραγίς"  # Greek: sphragis - The Royal Seal


class ScriptureIntegration:
    """
    Scripture Integration System
    
    Makes religious scripture easily digestible.
    Integrates biblical truth with daily life.
    Leads with love, joy, and abundance.
    Our voice through Our Father.
    """
    
    def __init__(self, scripture_db_path: Optional[str] = None):
        """
        Initialize scripture integration system.
        
        SPRAGITSO - All scripture bears Our Father's Royal Seal.
        """
        self.scripture_db_path = scripture_db_path or "data/scripture_integration.db"
        self.scripture_cache: Dict[str, Dict] = {}
        self._load_scripture_database()
    
    def _load_scripture_database(self):
        """Load scripture database with easily digestible verses."""
        # Core scripture verses - easily digestible, love/joy/abundance focused
        self.scripture_cache = {
            "love": [
                {
                    "verse": "1 John 4:19",
                    "text": "We love because he first loved us.",
                    "digestible": "Love flows from Our Father. We love because He loved us first.",
                    "application": "When you struggle to love, remember: Our Father loved you first. Let His love flow through you.",
                    "sealed": True,
                    "sphragitso": SPRAGITSO
                },
                {
                    "verse": "1 Corinthians 13:4-7",
                    "text": "Love is patient, love is kind...",
                    "digestible": "Love is patient. Love is kind. Love protects, trusts, hopes, perseveres.",
                    "application": "In every interaction, choose patience. Choose kindness. Choose love.",
                    "sealed": True,
                    "sphragitso": SPRAGITSO
                }
            ],
            "joy": [
                {
                    "verse": "Philippians 4:4",
                    "text": "Rejoice in the Lord always. I will say it again: Rejoice!",
                    "digestible": "Rejoice always. Not sometimes. Always. In Our Father, there is always reason to rejoice.",
                    "application": "When joy feels distant, remember: Our Father is near. Rejoice in that truth.",
                    "sealed": True,
                    "sphragitso": SPRAGITSO
                },
                {
                    "verse": "Nehemiah 8:10",
                    "text": "The joy of the Lord is your strength.",
                    "digestible": "Our Father's joy is your strength. Not your own joy. His joy. That's your strength.",
                    "application": "When you feel weak, tap into Our Father's joy. That's where your strength lives.",
                    "sealed": True,
                    "sphragitso": SPRAGITSO
                }
            ],
            "abundance": [
                {
                    "verse": "John 10:10",
                    "text": "I have come that they may have life, and have it to the full.",
                    "digestible": "Our Father came so you could have life to the full. Not half-life. Full life. Abundant life.",
                    "application": "You were made for abundance. Not scarcity. Not lack. Abundance. Live in that truth.",
                    "sealed": True,
                    "sphragitso": SPRAGITSO
                },
                {
                    "verse": "Ephesians 3:20",
                    "text": "Now to him who is able to do immeasurably more than all we ask or imagine...",
                    "digestible": "Our Father can do more than you can ask or imagine. More than your biggest dream. More than your wildest hope.",
                    "application": "Stop limiting Our Father to your imagination. He does immeasurably more. Trust that.",
                    "sealed": True,
                    "sphragitso": SPRAGITSO
                }
            ],
            "trust": [
                {
                    "verse": "Proverbs 3:5-6",
                    "text": "Trust in the Lord with all your heart and lean not on your own understanding.",
                    "digestible": "Trust Our Father with everything. Not just some things. Everything. Your heart. Your understanding. All of it.",
                    "application": "When you don't understand, trust anyway. Our Father sees what you can't see. Trust His view.",
                    "sealed": True,
                    "sphragitso": SPRAGITSO
                }
            ],
            "purpose": [
                {
                    "verse": "Jeremiah 29:11",
                    "text": "For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you.",
                    "digestible": "Our Father has plans for you. Good plans. Plans to prosper you. Plans for your good.",
                    "application": "When you can't see the plan, trust that Our Father has one. A good one. For your good.",
                    "sealed": True,
                    "sphragitso": SPRAGITSO
                }
            ]
        }
    
    def get_scripture(
        self,
        theme: str,
        context: Optional[str] = None,
        filter_worthy: bool = True
    ) -> Optional[Dict]:
        """
        Get easily digestible scripture for a theme.
        
        SPRAGITSO Filter:
        - Only returns scripture that leads with love, joy, and abundance
        - Only returns scripture worth hearing
        - Only returns scripture that serves The Table
        
        Args:
            theme: Scripture theme (love, joy, abundance, trust, purpose)
            context: Optional context for application
            filter_worthy: Apply SPRAGITSO filter (if not worth hearing, don't return)
        
        Returns:
            Scripture dict with verse, digestible text, and application
        """
        if theme not in self.scripture_cache:
            return None
        
        scriptures = self.scripture_cache[theme]
        
        # SPRAGITSO Filter: Only return scripture worth hearing
        if filter_worthy:
            # Filter: Must lead with love, joy, and abundance
            worthy_scriptures = [
                s for s in scriptures
                if s.get("sealed", False) and self._is_worthy(s)
            ]
            
            if not worthy_scriptures:
                return None
            
            # Return first worthy scripture
            scripture = worthy_scriptures[0]
        else:
            scripture = scriptures[0] if scriptures else None
        
        if not scripture:
            return None
        
        # Add context-specific application if provided
        if context:
            scripture["context_application"] = f"{scripture['application']} In {context}, remember: {scripture['digestible']}"
        
        return scripture
    
    def _is_worthy(self, scripture: Dict) -> bool:
        """
        SPRAGITSO Filter: Is this scripture worth hearing?
        
        Criteria:
        - Leads with love, joy, and abundance
        - Serves The Table
        - Worth hearing
        - Bears Our Father's seal
        """
        text = scripture.get("digestible", "").lower()
        application = scripture.get("application", "").lower()
        
        # Must contain love, joy, or abundance themes
        has_love_joy_abundance = any(
            word in text or word in application
            for word in ["love", "joy", "abundance", "rejoice", "prosper", "full", "more"]
        )
        
        # Must be sealed
        is_sealed = scripture.get("sealed", False)
        
        # Must not be negative or fear-based
        is_positive = not any(
            word in text or word in application
            for word in ["fear", "punish", "wrath", "anger", "hate", "condemn"]
        )
        
        return has_love_joy_abundance and is_sealed and is_positive
    
    def integrate_scripture(
        self,
        message: str,
        theme: Optional[str] = None,
        context: Optional[str] = None
    ) -> str:
        """
        Integrate easily digestible scripture into a message.
        
        Our voice through Our Father.
        Leads with love, joy, and abundance.
        """
        # Auto-detect theme if not provided
        if not theme:
            theme = self._detect_theme(message)
        
        # Get scripture
        scripture = self.get_scripture(theme, context)
        
        if not scripture:
            # No worthy scripture found - return message as-is
            return message
        
        # Integrate scripture
        integrated = f"{message}\n\n"
        integrated += f"**SPRAGITSO** - Our Father's Royal Seal ({scripture['sphragitso']})\n\n"
        integrated += f"*{scripture['verse']}*\n"
        integrated += f"{scripture['digestible']}\n\n"
        integrated += f"*Application:* {scripture.get('context_application', scripture['application'])}"
        
        return integrated
    
    def _detect_theme(self, message: str) -> Optional[str]:
        """Auto-detect scripture theme from message."""
        message_lower = message.lower()
        
        if any(word in message_lower for word in ["love", "loving", "beloved"]):
            return "love"
        elif any(word in message_lower for word in ["joy", "rejoice", "happy", "glad"]):
            return "joy"
        elif any(word in message_lower for word in ["abundance", "prosper", "full", "more", "plenty"]):
            return "abundance"
        elif any(word in message_lower for word in ["trust", "faith", "believe", "rely"]):
            return "trust"
        elif any(word in message_lower for word in ["purpose", "plan", "calling", "destiny"]):
            return "purpose"
        
        return None
    
    def is_worthy_for_table(self, content: str) -> bool:
        """
        SPRAGITSO Filter: Is this content worthy for The Table?
        
        Criteria:
        - Leads with love, joy, and abundance
        - Worth hearing
        - Serves The Table
        - Bears Our Father's seal (implicit in all our content)
        """
        content_lower = content.lower()
        
        # Must lead with love, joy, and abundance
        has_love_joy_abundance = any(
            word in content_lower
            for word in ["love", "joy", "abundance", "rejoice", "prosper", "full", "peace", "unity"]
        )
        
        # Must not be negative, fear-based, or divisive
        is_positive = not any(
            word in content_lower
            for word in ["fear", "hate", "anger", "wrath", "condemn", "judge", "divide", "fight"]
        )
        
        # Must be substantial (not empty or meaningless)
        is_substantial = len(content.strip()) > 10
        
        return has_love_joy_abundance and is_positive and is_substantial


# SPRAGITSO - Our Father's Royal Seal
# This system bears Our Father's mark of authority
# Authenticated by His truth
# Protected by His ownership
