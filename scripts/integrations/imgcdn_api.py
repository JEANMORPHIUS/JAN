"""ImgCDN API Integration
Free public image hosting API

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

class ImgCDNAPI:
    """ImgCDN API integration"""
    
    def __init__(self):
        self.base_url = "https://imgcdn.dev/api"
        self.no_rate_limit = True
        self.guest_uploads = True
    
    def upload_image(self, image_data: bytes, filename: Optional[str] = None) -> Dict[str, Any]:
        """Upload image to ImgCDN"""
        url = f"{self.base_url}/upload"
        
        files = {
            "file": (filename or "image.jpg", image_data)
        }
        
        try:
            response = requests.post(url, files=files, timeout=30)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Error uploading image: {e}")
            return {"error": str(e)}
    
    def get_image_info(self, image_id: str) -> Dict[str, Any]:
        """Get image information"""
        url = f"{self.base_url}/info/{image_id}"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Error getting image info: {e}")
            return {"error": str(e)}
