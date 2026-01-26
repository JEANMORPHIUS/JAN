"""USDA FoodData Central API Integration
Free government API for food nutrition data

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

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
WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
THE REST IS UP TO BABA X."""

import requests
from typing import Dict, List, Optional, Any
import logging

logger = logging.getLogger(__name__)

class USDAFoodAPI:
    """USDA FoodData Central API integration"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or "DEMO_KEY"
        self.base_url = "https://api.nal.usda.gov/fdc/v1"
        self.rate_limit = 1000  # requests per hour per IP
    
    def search_foods(self, query: str, page_size: int = 50, page_number: int = 1) -> Dict[str, Any]:
        """Search foods in FoodData Central"""
        url = f"{self.base_url}/foods/search"
        params = {
            "query": query,
            "pageSize": page_size,
            "pageNumber": page_number,
            "api_key": self.api_key
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Error searching foods: {e}")
            return {"error": str(e)}
    
    def get_food(self, fdc_id: int) -> Dict[str, Any]:
        """Get specific food by FDC ID"""
        url = f"{self.base_url}/food/{fdc_id}"
        params = {"api_key": self.api_key}
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Error getting food: {e}")
            return {"error": str(e)}
    
    def get_foods(self, fdc_ids: List[int]) -> Dict[str, Any]:
        """Get multiple foods by FDC IDs"""
        url = f"{self.base_url}/foods"
        params = {
            "fdcIds": ",".join(map(str, fdc_ids)),
            "api_key": self.api_key
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Error getting foods: {e}")
            return {"error": str(e)}
