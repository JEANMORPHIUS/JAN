"""
EDGE DETECTOR - Practical Tool
Detects house edge exposure and generates interventions

STATUS: 🔒 PRIVATE RESEARCH
PURPOSE: Practical tool for harm prevention
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class RiskLevel(Enum):
    """Risk levels for house edge exposure."""
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class GameActivity:
    """Represents a single gambling activity."""
    game_type: str
    bet_amount: float
    timestamp: datetime
    result: Optional[str] = None  # "win", "loss", "near_miss"
    payout: Optional[float] = None


@dataclass
class EdgeDetection:
    """Result of edge detection analysis."""
    house_edge: float
    expected_loss: float
    risk_level: RiskLevel
    intervention_needed: bool
    game_type: str
    total_wagered: float
    recommendations: List[str]


class EdgeDetector:
    """
    Detects house edge exposure and generates interventions.
    """
    
    # House edge by game type (as percentage)
    HOUSE_EDGES = {
        "slots": 0.05,  # 5%
        "blackjack_perfect": 0.005,  # 0.5%
        "blackjack_average": 0.02,  # 2%
        "roulette_european": 0.027,  # 2.7%
        "roulette_american": 0.0526,  # 5.26%
        "craps_pass": 0.0141,  # 1.41%
        "craps_any7": 0.1667,  # 16.67%
        "baccarat_banker": 0.0106,  # 1.06%
        "baccarat_tie": 0.144,  # 14.4%
        "video_poker_perfect": 0.005,  # 0.5%
        "video_poker_average": 0.05,  # 5%
        "keno": 0.25,  # 25%
        "lottery": 0.50,  # 50%
        "sports_betting": 0.045,  # 4.5%
    }
    
    def detect_edge(self, activities: List[GameActivity]) -> EdgeDetection:
        """
        Detect house edge exposure from user activities.
        """
        if not activities:
            return EdgeDetection(
                house_edge=0.0,
                expected_loss=0.0,
                risk_level=RiskLevel.LOW,
                intervention_needed=False,
                game_type="none",
                total_wagered=0.0,
                recommendations=[]
            )
        
        # Group by game type
        game_groups = self._group_by_game(activities)
        
        # Calculate house edge for each game
        edge_results = []
        for game_type, game_activities in game_groups.items():
            house_edge = self._get_house_edge(game_type)
            total_wagered = sum(activity.bet_amount for activity in game_activities)
            expected_loss = total_wagered * house_edge
            
            edge_results.append({
                "game_type": game_type,
                "house_edge": house_edge,
                "total_wagered": total_wagered,
                "expected_loss": expected_loss
            })
        
        # Aggregate results
        total_wagered = sum(r["total_wagered"] for r in edge_results)
        total_expected_loss = sum(r["expected_loss"] for r in edge_results)
        weighted_house_edge = total_expected_loss / total_wagered if total_wagered > 0 else 0.0
        
        # Determine risk level
        risk_level = self._determine_risk_level(weighted_house_edge, total_expected_loss)
        
        # Primary game type (highest wagered)
        primary_game = max(edge_results, key=lambda x: x["total_wagered"])["game_type"] if edge_results else "unknown"
        
        # Generate recommendations
        recommendations = self._generate_recommendations(
            weighted_house_edge,
            total_expected_loss,
            risk_level,
            primary_game
        )
        
        return EdgeDetection(
            house_edge=weighted_house_edge,
            expected_loss=total_expected_loss,
            risk_level=risk_level,
            intervention_needed=risk_level in [RiskLevel.HIGH, RiskLevel.CRITICAL],
            game_type=primary_game,
            total_wagered=total_wagered,
            recommendations=recommendations
        )
    
    def _group_by_game(self, activities: List[GameActivity]) -> Dict[str, List[GameActivity]]:
        """Group activities by game type."""
        groups = {}
        for activity in activities:
            if activity.game_type not in groups:
                groups[activity.game_type] = []
            groups[activity.game_type].append(activity)
        return groups
    
    def _get_house_edge(self, game_type: str) -> float:
        """Get house edge for game type."""
        # Try exact match first
        if game_type in self.HOUSE_EDGES:
            return self.HOUSE_EDGES[game_type]
        
        # Try partial matches
        if "blackjack" in game_type.lower():
            if "perfect" in game_type.lower():
                return self.HOUSE_EDGES["blackjack_perfect"]
            return self.HOUSE_EDGES["blackjack_average"]
        
        if "roulette" in game_type.lower():
            if "american" in game_type.lower():
                return self.HOUSE_EDGES["roulette_american"]
            return self.HOUSE_EDGES["roulette_european"]
        
        if "craps" in game_type.lower():
            if "any7" in game_type.lower() or "any_7" in game_type.lower():
                return self.HOUSE_EDGES["craps_any7"]
            return self.HOUSE_EDGES["craps_pass"]
        
        if "baccarat" in game_type.lower():
            if "tie" in game_type.lower():
                return self.HOUSE_EDGES["baccarat_tie"]
            return self.HOUSE_EDGES["baccarat_banker"]
        
        if "video_poker" in game_type.lower() or "videopoker" in game_type.lower():
            if "perfect" in game_type.lower():
                return self.HOUSE_EDGES["video_poker_perfect"]
            return self.HOUSE_EDGES["video_poker_average"]
        
        # Default to slots (most common, moderate edge)
        return self.HOUSE_EDGES["slots"]
    
    def _determine_risk_level(
        self,
        house_edge: float,
        expected_loss: float
    ) -> RiskLevel:
        """Determine risk level based on house edge and expected loss."""
        if house_edge > 0.10 or expected_loss > 1000:
            return RiskLevel.CRITICAL
        elif house_edge > 0.05 or expected_loss > 500:
            return RiskLevel.HIGH
        elif house_edge > 0.02 or expected_loss > 100:
            return RiskLevel.MODERATE
        else:
            return RiskLevel.LOW
    
    def _generate_recommendations(
        self,
        house_edge: float,
        expected_loss: float,
        risk_level: RiskLevel,
        game_type: str
    ) -> List[str]:
        """Generate recommendations based on edge detection."""
        recommendations = []
        
        # House edge recommendations
        if house_edge > 0.10:
            recommendations.append(
                f"⚠️ CRITICAL: House edge is {house_edge*100:.1f}% - You're being heavily exploited"
            )
        elif house_edge > 0.05:
            recommendations.append(
                f"⚠️ WARNING: House edge is {house_edge*100:.1f}% - Consider Oracle alternative"
            )
        
        # Expected loss recommendations
        if expected_loss > 1000:
            recommendations.append(
                f"⚠️ CRITICAL: Expected loss is ${expected_loss:.2f} - Immediate intervention needed"
            )
        elif expected_loss > 500:
            recommendations.append(
                f"⚠️ WARNING: Expected loss is ${expected_loss:.2f} - Consider stopping"
            )
        elif expected_loss > 100:
            recommendations.append(
                f"💡 MODERATE: Expected loss is ${expected_loss:.2f} - Oracle alternative available"
            )
        
        # Game-specific recommendations
        if game_type in ["keno", "lottery"]:
            recommendations.append(
                f"⚠️ WARNING: {game_type} has extremely high house edge (20-70%) - Consider Oracle"
            )
        elif game_type in ["slots", "roulette_american"]:
            recommendations.append(
                f"💡 MODERATE: {game_type} has moderate house edge - Oracle has 0% edge"
            )
        
        # Oracle alternative
        recommendations.append(
            "🌊 ORACLE ALTERNATIVE: Same randomness, 0% house edge, infinite value (wisdom)"
        )
        
        return recommendations


# USAGE EXAMPLE

if __name__ == "__main__":
    detector = EdgeDetector()
    
    # Example activities
    activities = [
        GameActivity(
            game_type="slots",
            bet_amount=10.0,
            timestamp=datetime.now(),
            result="loss"
        ),
        GameActivity(
            game_type="slots",
            bet_amount=20.0,
            timestamp=datetime.now(),
            result="near_miss"
        ),
        GameActivity(
            game_type="slots",
            bet_amount=50.0,
            timestamp=datetime.now(),
            result="loss"
        ),
        GameActivity(
            game_type="blackjack_average",
            bet_amount=100.0,
            timestamp=datetime.now(),
            result="loss"
        ),
    ]
    
    # Detect edge
    detection = detector.detect_edge(activities)
    
    print("=" * 60)
    print("EDGE DETECTION RESULTS")
    print("=" * 60)
    print()
    print(f"House Edge: {detection.house_edge*100:.2f}%")
    print(f"Expected Loss: ${detection.expected_loss:.2f}")
    print(f"Total Wagered: ${detection.total_wagered:.2f}")
    print(f"Risk Level: {detection.risk_level.value}")
    print(f"Intervention Needed: {detection.intervention_needed}")
    print(f"Primary Game: {detection.game_type}")
    print()
    print("Recommendations:")
    for rec in detection.recommendations:
        print(f"  - {rec}")
    print()
    print("=" * 60)
    print("ORACLE COMPARISON:")
    print("  House Edge: 0%")
    print("  Expected Loss: $0")
    print("  Value: Infinite (wisdom)")
    print("=" * 60)
