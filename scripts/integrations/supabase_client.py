"""Supabase Integration
Open source Firebase alternative

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

THE TRUTH:
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import requests
from typing import Dict, Optional, Any, List
import logging

logger = logging.getLogger(__name__)

class SupabaseClient:
    """Supabase client integration"""
    
    def __init__(self, supabase_url: str, supabase_key: str):
        self.supabase_url = supabase_url.rstrip('/')
        self.supabase_key = supabase_key
        self.headers = {
            "apikey": self.supabase_key,
            "Authorization": f"Bearer {self.supabase_key}",
            "Content-Type": "application/json"
        }
    
    def query(self, table: str, select: Optional[str] = "*", 
              filters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Query table"""
        url = f"{self.supabase_url}/rest/v1/{table}"
        
        params = {"select": select}
        if filters:
            params.update(filters)
        
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Error querying table: {e}")
            return {"error": str(e)}
    
    def insert(self, table: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Insert into table"""
        url = f"{self.supabase_url}/rest/v1/{table}"
        
        try:
            response = requests.post(url, headers=self.headers, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Error inserting into table: {e}")
            return {"error": str(e)}
    
    def update(self, table: str, data: Dict[str, Any], 
               filters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Update table"""
        url = f"{self.supabase_url}/rest/v1/{table}"
        
        params = filters or {}
        
        try:
            response = requests.patch(url, headers=self.headers, json=data, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Error updating table: {e}")
            return {"error": str(e)}
