"""
SIYEM Biological State Importer
Part of JAN Expansion Protocol
Version: 1.0 Genesis
Date: 2026-01-15

Imports biological state into SIYEM for creative task routing
and biological-creative correlation analysis.
"""

import os
import json
import requests
from datetime import date, datetime
from typing import Dict, List, Optional, Any
from pathlib import Path


class SIYEMImporter:
    """
    Imports biological state into SIYEM backend
    """
    
    def __init__(
        self,
        siyem_api_url: str = "http://localhost:8000",
        biological_state_dir: str = r"S:\JAN\logs\biological_state"
    ):
        """
        Initialize importer
        
        Args:
            siyem_api_url: SIYEM backend API URL
            biological_state_dir: Directory containing exported biological state JSON
        """
        self.api_url = siyem_api_url.rstrip('/')
        self.state_dir = Path(biological_state_dir)
    
    def load_biological_state(self, target_date: Optional[date] = None) -> Optional[Dict[str, Any]]:
        """
        Load biological state from JSON file
        
        Args:
            target_date: Date to load (defaults to today)
            
        Returns:
            Biological state dictionary or None
        """
        if target_date is None:
            target_date = date.today()
        
        date_str = target_date.strftime('%Y-%m-%d')
        state_file = self.state_dir / f"{date_str}.json"
        
        if not state_file.exists():
            print(f"No biological state file for {date_str}")
            return None
        
        with open(state_file) as f:
            return json.load(f)
    
    def import_to_siyem(self, biological_state: Dict[str, Any]) -> bool:
        """
        Import biological state to SIYEM backend
        
        Args:
            biological_state: Biological state dictionary
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Check if endpoint exists
            response = requests.post(
                f"{self.api_url}/api/biological-state",
                json=biological_state,
                timeout=10
            )
            
            if response.status_code == 200:
                print(f"✓ Biological state imported to SIYEM")
                return True
            elif response.status_code == 404:
                print("⚠ SIYEM API endpoint not yet implemented")
                print("  (This is expected in Phase 1 - endpoint will be added in Phase 2)")
                return False
            else:
                print(f"✗ SIYEM import failed: {response.status_code}")
                print(f"  Response: {response.text}")
                return False
        
        except requests.ConnectionError:
            print("✗ Cannot connect to SIYEM backend")
            print(f"  Is SIYEM running at {self.api_url}?")
            return False
        except Exception as e:
            print(f"✗ Error importing to SIYEM: {e}")
            return False
    
    def get_task_recommendations(self) -> Optional[Dict[str, Any]]:
        """
        Get task recommendations from SIYEM based on biological state
        
        Returns:
            Recommendations dictionary or None
        """
        try:
            response = requests.get(
                f"{self.api_url}/api/task-recommendations",
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print("⚠ Task recommendations endpoint not yet implemented")
                return None
            else:
                print(f"✗ Failed to get recommendations: {response.status_code}")
                return None
        
        except requests.ConnectionError:
            print("✗ Cannot connect to SIYEM backend")
            return None
        except Exception as e:
            print(f"✗ Error getting recommendations: {e}")
            return None
    
    def log_creative_session(
        self,
        entity: str,
        session_duration_minutes: int,
        task_type: str,
        quality_rating: Optional[int] = None
    ) -> bool:
        """
        Log creative session to SIYEM
        
        Args:
            entity: Entity name (JEAN, KARASAHIN, etc.)
            session_duration_minutes: Session duration
            task_type: Type of task (storytelling, music, teaching, etc.)
            quality_rating: Self-rated quality (1-10)
            
        Returns:
            True if successful, False otherwise
        """
        try:
            session_data = {
                "entity": entity,
                "timestamp": datetime.now().isoformat(),
                "duration_minutes": session_duration_minutes,
                "task_type": task_type,
                "quality_rating": quality_rating
            }
            
            response = requests.post(
                f"{self.api_url}/api/creative-session-log",
                json=session_data,
                timeout=10
            )
            
            if response.status_code == 200:
                print(f"✓ Creative session logged")
                return True
            elif response.status_code == 404:
                print("⚠ Creative session logging endpoint not yet implemented")
                return False
            else:
                print(f"✗ Session logging failed: {response.status_code}")
                return False
        
        except requests.ConnectionError:
            print("✗ Cannot connect to SIYEM backend")
            return False
        except Exception as e:
            print(f"✗ Error logging session: {e}")
            return False
    
    def get_correlations(self, days: int = 7) -> Optional[Dict[str, Any]]:
        """
        Get biological-creative correlations from SIYEM
        
        Args:
            days: Number of days to analyze
            
        Returns:
            Correlations dictionary or None
        """
        try:
            response = requests.get(
                f"{self.api_url}/api/correlations/daily",
                params={"days": days},
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print("⚠ Correlations endpoint not yet implemented")
                return None
            else:
                print(f"✗ Failed to get correlations: {response.status_code}")
                return None
        
        except requests.ConnectionError:
            print("✗ Cannot connect to SIYEM backend")
            return None
        except Exception as e:
            print(f"✗ Error getting correlations: {e}")
            return None
    
    def sync_today(self) -> bool:
        """
        Sync today's biological state to SIYEM
        
        Returns:
            True if successful, False otherwise
        """
        print("Syncing today's biological state to SIYEM...")
        
        state = self.load_biological_state()
        if not state:
            print("✗ No biological state available for today")
            return False
        
        print(f"Current biological status: {state.get('status', 'UNKNOWN')}")
        
        if state.get('warnings'):
            print("\nWarnings:")
            for warning in state['warnings']:
                print(f"  ⚠ {warning}")
        
        if state.get('recommendations'):
            print("\nRecommendations:")
            for rec in state['recommendations']:
                print(f"  • {rec}")
        
        print("\nImporting to SIYEM...")
        success = self.import_to_siyem(state)
        
        if success:
            # Try to get task recommendations
            print("\nGetting task recommendations...")
            recommendations = self.get_task_recommendations()
            if recommendations:
                print(json.dumps(recommendations, indent=2))
        
        return success


# ============================================================================
# OFFLINE MODE - Local recommendations without SIYEM connection
# ============================================================================

class OfflineRecommendations:
    """
    Generate task recommendations without SIYEM connection
    """
    
    @staticmethod
    def get_recommendations(biological_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate recommendations based on biological state
        
        Args:
            biological_state: Biological state dictionary
            
        Returns:
            Recommendations dictionary
        """
        status = biological_state.get('status', 'NO_DATA')
        glucose = biological_state.get('glucose')
        vision = biological_state.get('vision_clarity')
        
        if status == "CRITICAL":
            return {
                "recommendation": "PROTOCOL_FOCUS",
                "priority": "CRITICAL",
                "tasks": [],
                "message": "Biological state critical. Execute flush protocol. Pause creative work.",
                "entities_recommended": [],
                "entities_avoid": ["ALL"]
            }
        
        elif status == "ELEVATED":
            return {
                "recommendation": "LIGHT_WORK",
                "priority": "MODERATE",
                "tasks": [
                    "Administrative tasks",
                    "Email responses",
                    "Planning and organization",
                    "Light content review"
                ],
                "message": "Biological state elevated. Light creative work only.",
                "entities_recommended": ["PIERRE", "SIYEM_MEDIA"],
                "entities_avoid": ["JEAN", "KARASAHIN"]  # Avoid deep creative work
            }
        
        elif status == "STABLE":
            return {
                "recommendation": "HIGH_CLARITY_WORK",
                "priority": "OPTIMAL",
                "tasks": [
                    "Deep creative work",
                    "Complex problem-solving",
                    "Content creation",
                    "Technical development",
                    "Teaching material development"
                ],
                "message": "Biological state optimal. Perfect for high-clarity creative output.",
                "entities_recommended": ["JEAN", "KARASAHIN", "RAMIZ"],
                "entities_avoid": []
            }
        
        else:
            return {
                "recommendation": "NORMAL_WORK",
                "priority": "NORMAL",
                "tasks": [
                    "Standard creative work",
                    "Project continuation",
                    "Moderate intensity tasks"
                ],
                "message": "Biological state normal. Standard creative activities suitable.",
                "entities_recommended": ["ALL"],
                "entities_avoid": []
            }


# ============================================================================
# CLI INTERFACE
# ============================================================================

def main():
    """Command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Import biological state to SIYEM")
    parser.add_argument('--api-url', default='http://localhost:8000',
                       help='SIYEM API URL')
    parser.add_argument('--sync-today', action='store_true',
                       help='Sync today\'s biological state')
    parser.add_argument('--offline', action='store_true',
                       help='Generate recommendations offline (no SIYEM connection required)')
    parser.add_argument('--log-session', nargs=4, metavar=('ENTITY', 'DURATION', 'TYPE', 'RATING'),
                       help='Log creative session (e.g., JEAN 120 storytelling 8)')
    
    args = parser.parse_args()
    
    importer = SIYEMImporter(siyem_api_url=args.api_url)
    
    if args.sync_today:
        if args.offline:
            print("=== OFFLINE MODE - Local Recommendations ===\n")
            state = importer.load_biological_state()
            if state:
                print(f"Biological Status: {state.get('status', 'UNKNOWN')}\n")
                recommendations = OfflineRecommendations.get_recommendations(state)
                print(json.dumps(recommendations, indent=2))
        else:
            importer.sync_today()
    
    elif args.log_session:
        entity, duration, task_type, rating = args.log_session
        importer.log_creative_session(
            entity=entity,
            session_duration_minutes=int(duration),
            task_type=task_type,
            quality_rating=int(rating)
        )
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

