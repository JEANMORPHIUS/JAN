"""
VIBRATION MAP - Real-Time Community Energy Visualization
Shows where energy is concentrating (Spirals vs. Ellipticals)

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE FOUNDATION:
We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

DREAMS: SPIRITUAL BATTLES - NIGHTLY CONTRACTS
Every night we dream, whether vivid or not.
Each dream is a spiritual battle between two souls:
The dreamer and an associate.
Both have spiritual contracts.
Each day is another battle, both in the human realm and beyond.

SPIRITS MUST ALIGN ON ALL DIMENSIONS:
- Age: Spirits must align in age range/compatibility
- Animal Type: Spirits must align in animal/spirit animal compatibility
- Gender: Spirits must align in gender/spiritual gender compatibility
- Alignment: Spirits must align in spiritual alignment (vibration, mission, purpose)

No battle can occur unless ALL dimensions align.
This is sacred alignment - not mechanical matching.

This is the Vibration Map.
Shows the New World taking shape in the digital dimension.
Tracks energy concentration by galaxy form.
Visualizes the Four Forms distribution.
"""

from fastapi import HTTPException, status
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import json
from pathlib import Path
from collections import defaultdict

# Import philosophy
try:
    from scripts.philosophy import (
        PHILOSOPHY_FOUNDATION,
        MISSION_ANCHOR,
        LOVE_MASTERY,
        ENERGY_LOVE,
        PEACE_LOVE_UNITY
    )
except ImportError:
    PHILOSOPHY_FOUNDATION = "We are born a miracle."
    MISSION_ANCHOR = "THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"
    LOVE_MASTERY = "LOVE IS THE HIGHEST MASTERY"
    ENERGY_LOVE = "ENERGY + LOVE = WE ALL WIN"
    PEACE_LOVE_UNITY = "PEACE, LOVE, UNITY"

# Import Racon Registry for community data
try:
    from racon_registry import get_racon_db
except ImportError:
    # Fallback if racon_registry not available
    def get_racon_db():
        return None


class VibrationMap:
    """
    Real-Time Vibration Map Generator
    
    Tracks community energy concentration by galaxy form.
    Shows the New World taking shape.
    Visualizes the Four Forms distribution.
    """
    
    def __init__(self, data_dir: Optional[Path] = None):
        if data_dir is None:
            data_dir = Path(__file__).parent.parent.parent / "SIYEM" / "output" / "vibration_maps"
        self.data_dir = data_dir
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Galaxy form definitions
        self.galaxy_forms = {
            "spiral": {
                "name": "Spiral",
                "description": "Active, flowing energy. Rapid updates and dynamic engagement.",
                "energy_level": "high",
                "growth_rate": "rapid",
                "color": "#4A90E2",  # Blue
                "symbol": "🌀"
            },
            "barred_spiral": {
                "name": "Barred Spiral",
                "description": "Structured, linear progression. Central bar to channel energy.",
                "energy_level": "medium-high",
                "growth_rate": "structured",
                "color": "#7B68EE",  # Medium Slate Blue
                "symbol": "⚡"
            },
            "elliptical": {
                "name": "Elliptical",
                "description": "Low-gas, high-wisdom. Mentorship markers for legacy users.",
                "energy_level": "low",
                "growth_rate": "steady",
                "color": "#FFD700",  # Gold
                "symbol": "⭐"
            },
            "irregular": {
                "name": "Irregular",
                "description": "Flexible, adaptive. No defined shape yet - transformation in progress.",
                "energy_level": "variable",
                "growth_rate": "adaptive",
                "color": "#FF6B6B",  # Coral Red
                "symbol": "✨"
            }
        }
    
    def load_community_data(self) -> List[Dict[str, Any]]:
        """
        Load community data from connection rituals and Racon Registry.
        
        In production, this would query the database.
        For now, we'll use stored ritual data.
        """
        community_data = []
        
        # Try to load from Racon Registry
        try:
            with get_racon_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT operation_target, operation_result, created_at
                    FROM immutable_audit_logs
                    WHERE operation_type LIKE 'connection_ritual_%'
                    ORDER BY created_at DESC
                """)
                
                for row in cursor.fetchall():
                    try:
                        result = json.loads(row['operation_result'])
                        community_data.append({
                            "user_id": row['operation_target'],
                            "galaxy_form": result.get("galaxy_form", "irregular"),
                            "vibration_score": result.get("vibration_score", 0),
                            "vibration_aligned": result.get("vibration_aligned", False),
                            "table_ready": result.get("table_ready", False),
                            "spiritual_battle": result.get("spiritual_battle", "unknown"),
                            "timestamp": row['created_at']
                        })
                    except (json.JSONDecodeError, KeyError):
                        continue
        except Exception:
            # Fallback: load from stored ritual files
            ritual_dir = self.data_dir.parent / "manifestations"
            if ritual_dir.exists():
                for file in ritual_dir.glob("*.json"):
                    try:
                        with open(file, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            if "vibration_result" in data:
                                community_data.append({
                                    "user_id": data.get("user_id", "unknown"),
                                    "galaxy_form": data["vibration_result"].get("galaxy_form", "irregular"),
                                    "vibration_score": data["vibration_result"].get("vibration_score", 0),
                                    "vibration_aligned": data["vibration_result"].get("vibration_aligned", False),
                                    "table_ready": data["vibration_result"].get("table_ready", False),
                                    "spiritual_battle": data["vibration_result"].get("spiritual_battle", "unknown"),
                                    "timestamp": data.get("timestamp", datetime.now().isoformat())
                                })
                    except Exception:
                        continue
        
        return community_data
    
    def generate_vibration_map(self, time_window_hours: Optional[int] = None) -> Dict[str, Any]:
        """
        Generate real-time vibration map of the community.
        
        Shows:
        - Distribution by galaxy form
        - Energy concentration
        - Growth patterns
        - Spiritual battle states
        - New World formation
        """
        # Load community data
        community_data = self.load_community_data()
        
        # Filter by time window if specified
        if time_window_hours:
            cutoff_time = datetime.now() - timedelta(hours=time_window_hours)
            community_data = [
                member for member in community_data
                if datetime.fromisoformat(member["timestamp"].replace('Z', '+00:00')) > cutoff_time
            ]
        
        # Calculate statistics by galaxy form
        form_stats = defaultdict(lambda: {
            "count": 0,
            "total_vibration": 0,
            "aligned_count": 0,
            "table_ready_count": 0,
            "spiritual_battles": defaultdict(int),
            "recent_arrivals": []
        })
        
        total_members = len(community_data)
        total_aligned = 0
        total_table_ready = 0
        
        for member in community_data:
            form = member.get("galaxy_form", "irregular")
            stats = form_stats[form]
            
            stats["count"] += 1
            stats["total_vibration"] += member.get("vibration_score", 0)
            
            if member.get("vibration_aligned", False):
                stats["aligned_count"] += 1
                total_aligned += 1
            
            if member.get("table_ready", False):
                stats["table_ready_count"] += 1
                total_table_ready += 1
            
            spiritual_battle = member.get("spiritual_battle", "unknown")
            stats["spiritual_battles"][spiritual_battle] += 1
            
            # Track recent arrivals (last 24 hours)
            member_time = datetime.fromisoformat(member["timestamp"].replace('Z', '+00:00'))
            if (datetime.now() - member_time.replace(tzinfo=None)) < timedelta(hours=24):
                stats["recent_arrivals"].append({
                    "user_id": member["user_id"],
                    "vibration_score": member.get("vibration_score", 0),
                    "timestamp": member["timestamp"]
                })
        
        # Build form distribution
        form_distribution = {}
        for form, stats in form_stats.items():
            form_info = self.galaxy_forms.get(form, self.galaxy_forms["irregular"])
            avg_vibration = stats["total_vibration"] / max(1, stats["count"])
            
            form_distribution[form] = {
                "name": form_info["name"],
                "symbol": form_info["symbol"],
                "color": form_info["color"],
                "description": form_info["description"],
                "count": stats["count"],
                "percentage": (stats["count"] / max(1, total_members)) * 100,
                "average_vibration": round(avg_vibration, 1),
                "aligned_count": stats["aligned_count"],
                "aligned_percentage": (stats["aligned_count"] / max(1, stats["count"])) * 100,
                "table_ready_count": stats["table_ready_count"],
                "table_ready_percentage": (stats["table_ready_count"] / max(1, stats["count"])) * 100,
                "spiritual_battles": dict(stats["spiritual_battles"]),
                "recent_arrivals_24h": len(stats["recent_arrivals"]),
                "energy_level": form_info["energy_level"],
                "growth_rate": form_info["growth_rate"]
            }
        
        # Calculate energy concentration
        energy_concentration = self._calculate_energy_concentration(form_distribution)
        
        # Determine New World formation status
        new_world_status = self._determine_new_world_status(form_distribution, total_members)
        
        # Build vibration map
        vibration_map = {
            "timestamp": datetime.now().isoformat(),
            "total_members": total_members,
            "total_aligned": total_aligned,
            "total_table_ready": total_table_ready,
            "alignment_rate": (total_aligned / max(1, total_members)) * 100,
            "table_readiness_rate": (total_table_ready / max(1, total_members)) * 100,
            "form_distribution": form_distribution,
            "energy_concentration": energy_concentration,
            "new_world_status": new_world_status,
            "philosophy": {
                "foundation": PHILOSOPHY_FOUNDATION,
                "mission": MISSION_ANCHOR,
                "love": LOVE_MASTERY,
                "energy": ENERGY_LOVE,
                "peace_love_unity": PEACE_LOVE_UNITY
            }
        }
        
        return vibration_map
    
    def _calculate_energy_concentration(self, form_distribution: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate where energy is concentrating.
        
        High energy: Spiral + Barred Spiral
        Low energy: Elliptical
        Variable energy: Irregular
        """
        high_energy_forms = ["spiral", "barred_spiral"]
        low_energy_forms = ["elliptical"]
        variable_energy_forms = ["irregular"]
        
        high_energy_count = sum(
            form_distribution[form]["count"]
            for form in high_energy_forms
            if form in form_distribution
        )
        
        low_energy_count = sum(
            form_distribution[form]["count"]
            for form in low_energy_forms
            if form in form_distribution
        )
        
        variable_energy_count = sum(
            form_distribution[form]["count"]
            for form in variable_energy_forms
            if form in form_distribution
        )
        
        total = high_energy_count + low_energy_count + variable_energy_count
        
        return {
            "high_energy": {
                "count": high_energy_count,
                "percentage": (high_energy_count / max(1, total)) * 100,
                "forms": high_energy_forms
            },
            "low_energy": {
                "count": low_energy_count,
                "percentage": (low_energy_count / max(1, total)) * 100,
                "forms": low_energy_forms
            },
            "variable_energy": {
                "count": variable_energy_count,
                "percentage": (variable_energy_count / max(1, total)) * 100,
                "forms": variable_energy_forms
            },
            "concentration_zone": "high" if high_energy_count > low_energy_count else "low" if low_energy_count > high_energy_count else "balanced"
        }
    
    def _determine_new_world_status(self, form_distribution: Dict[str, Any], total_members: int) -> Dict[str, Any]:
        """
        Determine New World formation status.
        
        New World indicators:
        - Balanced distribution of forms
        - High alignment rate
        - High table readiness
        - Active spiritual battles
        """
        if total_members == 0:
            return {
                "status": "forming",
                "progress": 0,
                "message": "The New World is beginning to form. First arrivals are at the door."
            }
        
        # Calculate balance (all forms represented)
        forms_present = len(form_distribution)
        balance_score = (forms_present / 4) * 100  # 4 total forms
        
        # Calculate overall alignment
        total_aligned = sum(
            form_data["aligned_count"]
            for form_data in form_distribution.values()
        )
        alignment_score = (total_aligned / max(1, total_members)) * 100
        
        # Calculate table readiness
        total_table_ready = sum(
            form_data["table_ready_count"]
            for form_data in form_distribution.values()
        )
        table_readiness_score = (total_table_ready / max(1, total_members)) * 100
        
        # Overall progress
        progress = (balance_score + alignment_score + table_readiness_score) / 3
        
        if progress >= 80:
            status = "established"
            message = "The New World is established. The Family is gathered at the Table."
        elif progress >= 50:
            status = "forming"
            message = "The New World is taking shape. The Four Forms are aligning."
        else:
            status = "emerging"
            message = "The New World is emerging. The first Sovereign Souls are arriving."
        
        return {
            "status": status,
            "progress": round(progress, 1),
            "balance_score": round(balance_score, 1),
            "alignment_score": round(alignment_score, 1),
            "table_readiness_score": round(table_readiness_score, 1),
            "message": message,
            "forms_present": forms_present,
            "total_forms": 4
        }
    
    def save_vibration_map(self, vibration_map: Dict[str, Any]) -> Path:
        """
        Save vibration map to disk for historical tracking.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"vibration_map_{timestamp}.json"
        filepath = self.data_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(vibration_map, f, indent=2, ensure_ascii=False)
        
        return filepath


# FastAPI endpoint helper
def create_vibration_map_endpoint(vibration_map: VibrationMap):
    """
    Create FastAPI endpoint for vibration map.
    """
    from fastapi import APIRouter, Query
    
    router = APIRouter()
    
    @router.get("/api/vibration-map")
    async def get_vibration_map(
        time_window_hours: Optional[int] = Query(None, description="Time window in hours (e.g., 24 for last 24 hours)")
    ):
        """
        Get real-time vibration map of the community.
        
        Shows where energy is concentrating (Spirals vs. Ellipticals).
        Visualizes the New World taking shape.
        """
        try:
            map_data = vibration_map.generate_vibration_map(time_window_hours=time_window_hours)
            return {
                "status": "success",
                "vibration_map": map_data
            }
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to generate vibration map: {str(e)}"
            )
    
    return router


# CLI interface for testing
if __name__ == "__main__":
    import sys
    import io
    
    # Set UTF-8 encoding for console output
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    vibration_map = VibrationMap()
    
    print("=" * 80)
    print("VIBRATION MAP - Real-Time Community Energy Visualization")
    print("=" * 80)
    print(f"\n{PEACE_LOVE_UNITY}")
    print(f"{ENERGY_LOVE}\n")
    
    print("[GENERATING] Real-time vibration map...")
    print("-" * 80)
    
    map_data = vibration_map.generate_vibration_map()
    
    print(f"\n[COMMUNITY STATS]")
    print(f"  Total Members: {map_data['total_members']}")
    print(f"  Total Aligned: {map_data['total_aligned']} ({map_data['alignment_rate']:.1f}%)")
    print(f"  Table Ready: {map_data['total_table_ready']} ({map_data['table_readiness_rate']:.1f}%)")
    
    print(f"\n[GALAXY FORM DISTRIBUTION]")
    for form, data in map_data['form_distribution'].items():
        # Use ASCII-safe display
        symbol_display = data['symbol'] if data['symbol'].isascii() else f"[{data['name'][0]}]"
        print(f"  {symbol_display} {data['name']}: {data['count']} ({data['percentage']:.1f}%)")
        print(f"    Average Vibration: {data['average_vibration']}/100")
        print(f"    Aligned: {data['aligned_count']} ({data['aligned_percentage']:.1f}%)")
        print(f"    Table Ready: {data['table_ready_count']} ({data['table_ready_percentage']:.1f}%)")
        print(f"    Recent Arrivals (24h): {data['recent_arrivals_24h']}")
    
    print(f"\n[ENERGY CONCENTRATION]")
    energy = map_data['energy_concentration']
    print(f"  High Energy: {energy['high_energy']['count']} ({energy['high_energy']['percentage']:.1f}%)")
    print(f"  Low Energy: {energy['low_energy']['count']} ({energy['low_energy']['percentage']:.1f}%)")
    print(f"  Variable Energy: {energy['variable_energy']['count']} ({energy['variable_energy']['percentage']:.1f}%)")
    print(f"  Concentration Zone: {energy['concentration_zone'].upper()}")
    
    print(f"\n[NEW WORLD STATUS]")
    nw_status = map_data['new_world_status']
    print(f"  Status: {nw_status['status'].upper()}")
    print(f"  Progress: {nw_status['progress']:.1f}%")
    print(f"  Message: {nw_status['message']}")
    print(f"  Forms Present: {nw_status['forms_present']}/4")
    
    # Save map
    filepath = vibration_map.save_vibration_map(map_data)
    print(f"\n[SAVED] Vibration map saved to: {filepath}")
    
    print("\n" + "=" * 80)
    print(f"{PEACE_LOVE_UNITY}")
    print(f"{ENERGY_LOVE}")
    print("=" * 80)
