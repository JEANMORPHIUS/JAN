"""
LEGAL YIN-YANG INTEGRATION
Connect Legal Framework with Yin-Yang Symbiosis

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
Connect the yin with the yang.
Everything must be symbiotic in-house before we can go to war.
Legal compliance (yang) must balance with creative expression (yin).
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

# Import frameworks
try:
    from legal_contractual_framework import get_legal_framework, ChannelType, AgreementType
    from yin_yang_symbiosis import get_yin_yang_framework, BalanceType, SymbiosisLevel
    FRAMEWORKS_AVAILABLE = True
except ImportError as e:
    logger.warning(f"Frameworks not available: {e}")
    FRAMEWORKS_AVAILABLE = False


class LegalYinYangIntegration:
    """
    Legal Yin-Yang Integration
    Connects legal framework with yin-yang symbiosis
    
    Principle: Legal compliance (yang) must balance with creative expression (yin)
    """
    
    def __init__(self):
        """Initialize integration"""
        if not FRAMEWORKS_AVAILABLE:
            raise ImportError("Required frameworks not available")
        
        self.legal_framework = get_legal_framework()
        self.yin_yang_framework = get_yin_yang_framework()
        
        logger.info("Legal Yin-Yang Integration initialized")
    
    def check_legal_creative_balance(self, channel: ChannelType) -> Dict[str, Any]:
        """
        Check balance between legal compliance (yang) and creative expression (yin)
        
        Args:
            channel: Channel type
        
        Returns:
            Balance report
        """
        # Get legal agreements for channel
        agreements = self.legal_framework.get_channel_agreements(channel)
        prs_records = [r for r in self.legal_framework.prs_records.values() if r.channel == channel]
        
        # Check compliance
        compliance_report = self.legal_framework.verify_compliance()
        
        # Check yin-yang balance
        balance_check = self.yin_yang_framework.check_balance(
            BalanceType.CREATIVE_PRACTICAL,
            {
                "creative": {
                    "songs": len(prs_records),
                    "content": "creative_expression"
                },
                "practical": {
                    "agreements": len(agreements),
                    "compliance": compliance_report.get("compliant", 0)
                }
            }
        )
        
        return {
            "channel": channel.value,
            "legal_status": {
                "agreements": len(agreements),
                "prs_records": len(prs_records),
                "compliant": compliance_report.get("compliant", 0),
                "non_compliant": compliance_report.get("non_compliant", 0),
                "pending": compliance_report.get("pending", 0)
            },
            "yin_yang_balance": {
                "level": balance_check.get("level", "unknown"),
                "score": balance_check.get("score", 0.0),
                "yin": "Creative expression (songs, content)",
                "yang": "Legal compliance (agreements, PRS)"
            },
            "symbiotic": balance_check.get("level") == SymbiosisLevel.SYMBIOTIC.value,
            "timestamp": datetime.now().isoformat()
        }
    
    def get_all_channels_balance(self) -> Dict[str, Any]:
        """Get balance for all channels"""
        channels = [ChannelType.PROFESSIONAL, ChannelType.CREATOR, ChannelType.EDUCATIONAL]
        
        results = {}
        for channel in channels:
            results[channel.value] = self.check_legal_creative_balance(channel)
        
        return {
            "channels": results,
            "overall_symbiotic": all(
                r.get("symbiotic", False) for r in results.values()
            ),
            "timestamp": datetime.now().isoformat()
        }


# Global integration instance
_legal_yin_yang: Optional[LegalYinYangIntegration] = None


def get_legal_yin_yang_integration() -> Optional[LegalYinYangIntegration]:
    """Get or create integration"""
    global _legal_yin_yang
    
    if _legal_yin_yang is None and FRAMEWORKS_AVAILABLE:
        try:
            _legal_yin_yang = LegalYinYangIntegration()
        except Exception as e:
            logger.error(f"Error creating integration: {e}")
            return None
    
    return _legal_yin_yang
