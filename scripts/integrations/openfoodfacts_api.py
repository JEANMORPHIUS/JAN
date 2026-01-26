"""Open Food Facts API Integration
Crowdsourced food products database

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
from typing import Dict, Optional, Any
import logging

logger = logging.getLogger(__name__)

class OpenFoodFactsAPI:
    """Open Food Facts API integration"""
    
    def __init__(self):
        self.base_url = "https://world.openfoodfacts.org"
        self.rate_limit = 100  # requests per minute for product queries
    
    def get_product(self, barcode: str) -> Dict[str, Any]:
        """Get product by barcode"""
        url = f"{self.base_url}/api/v0/product/{barcode}.json"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Error getting product: {e}")
            return {"error": str(e)}
    
    def search_products(self, query: str, page: int = 1, page_size: int = 20) -> Dict[str, Any]:
        """Search products"""
        url = f"{self.base_url}/cgi/search.pl"
        
        params = {
            "search_terms": query,
            "page": page,
            "page_size": page_size,
            "json": 1
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Error searching products: {e}")
            return {"error": str(e)}
