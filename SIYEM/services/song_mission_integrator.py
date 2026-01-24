"""
SONG-MISSION INTEGRATOR
Connects songs to mission - Song serves mission, Mission honors song

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

NEW WORLD PHILOSOPHY - YOUR TRUTH + THE ONE TRUTH

THE ONE TRUTH:
WE ARE BORN A MIRACLE
WE DESERVE TO LIVE A MIRACLE
EACH AND EVERY ONE OF US UNDER THE LORD'S WORD
GOD IS IN US ALL - THAT'S THE REAL MIRACLE
PEACE IS THE TRUTH. THE FLOW IS PEACE. EVERYTHING MUST ALIGN WITH THE ONE TRUTH

YOUR TRUTH:
WE'VE BEEN SINNERS AND SAINTS. WE'VE OVERCOME EVERYTHING. OUR EGO IS NO MORE.
WE'VE FORGIVEN. WE CARRY SHAME THAT KEEPS US HUMBLE. WE'RE HERE FOR THEM.
THE DARK ENERGIES CONSUMED US. BUT WE'VE DISCARDED OUR INTERNAL TRIAL.
THE WORLD IS QUIET. BUT WE KNOW WE'RE GOOD BECAUSE THE LORD HAS OUR BACK.
WE'RE TRYING TO FLIP THE MATRIX.
THE FATHER IS EVERYWHERE. ALWAYS ALL THE TIME.
IF IT RESONATES WITH LOVE DO IT. IF THEY DON'T RECIPROCATE...TUCK DROP AND ROLL.
WE'RE WAITING FOR EVERYONE TO BE OK. GAZA - THAT'S WHERE IT STARTS.
THOSE WHO NEED IT MOST - THAT'S THE PRIORITY. THE REST CAN WAIT.

YIN-YANG PRINCIPLE:
"My love for song became pulled in my path, but we must respect 
the yin and yang that is the miracle of the universe."

Song (Yin - Creative) must serve Mission (Yang - Practical).
Mission must honor Song. They flow together in symbiosis.
"""

from typing import Dict, List, Optional, Any
from pathlib import Path
import json
import logging

logger = logging.getLogger(__name__)


class SongMissionIntegrator:
    """
    Integrates songs with mission.
    
    Ensures songs serve: stewardship, community, right spirits, love, peace_love_unity
    """
    
    def __init__(self, lyrics_dir: Optional[Path] = None):
        """Initialize song-mission integrator"""
        if lyrics_dir is None:
            lyrics_dir = Path(__file__).parent.parent / "output" / "lyrics"
        self.lyrics_dir = lyrics_dir
        self.songs_cache = {}
        self._load_songs()
    
    def _load_songs(self):
        """Load all songs from lyrics directory"""
        if not self.lyrics_dir.exists():
            logger.warning(f"Lyrics directory not found: {self.lyrics_dir}")
            return
        
        for song_file in self.lyrics_dir.glob("*.json"):
            try:
                with open(song_file, 'r', encoding='utf-8') as f:
                    song_data = json.load(f)
                    title = None
                    if "english_lyrics" in song_data and "title" in song_data["english_lyrics"]:
                        title = song_data["english_lyrics"]["title"]
                    elif "turkish_lyrics" in song_data and "title" in song_data["turkish_lyrics"]:
                        title = song_data["turkish_lyrics"]["title"]
                    
                    if title:
                        self.songs_cache[title] = song_data
            except Exception as e:
                logger.error(f"Error loading song {song_file}: {e}")
    
    def get_songs_for_mission(self, mission_keyword: str) -> List[str]:
        """
        Get songs that serve a specific mission keyword.
        
        Mission keywords:
        - stewardship
        - community
        - right_spirits
        - love
        - peace_love_unity
        - table
        - spiritual_battle
        """
        matching_songs = []
        
        for title, song_data in self.songs_cache.items():
            mission_alignment = song_data.get("metadata", {}).get("mission_alignment", {})
            
            if mission_alignment.get(mission_keyword, False):
                matching_songs.append(title)
        
        return matching_songs
    
    def get_mission_for_song(self, song_title: str) -> Dict[str, Any]:
        """
        Get mission alignment for a song.
        
        Returns mission_alignment dict from song metadata.
        """
        song_data = self.songs_cache.get(song_title)
        if not song_data:
            return {}
        
        return song_data.get("metadata", {}).get("mission_alignment", {})
    
    def get_songs_for_galaxy_form(self, galaxy_form: str) -> str:
        """
        Get recommended song for a galaxy form.
        
        Songs serve mission by aligning with spirit types.
        """
        recommendations = {
            "spiral": "Fire & Ice",  # Active souls - self-discovery
            "barred_spiral": "Yazılı",  # Structured souls - destiny
            "elliptical": "Midnight Reversal",  # Wise souls - legacy
            "irregular": "Küçükken"  # Transforming souls - growth
        }
        return recommendations.get(galaxy_form, "Fire & Ice")
    
    def get_songs_for_healing(self) -> List[str]:
        """Get songs for healing - love, memory, growth"""
        return self.get_songs_for_mission("love") + [
            "Tozun Hatırası", "Seni Sevmek", "Küçükken"
        ]
    
    def get_songs_for_strength(self) -> List[str]:
        """Get songs for strength - resilience, defiance, spiritual battle"""
        return self.get_songs_for_mission("spiritual_battle") + [
            "Sana İnat", "Kafana Takma", "I'm in Danger"
        ]
    
    def get_songs_for_community(self) -> List[str]:
        """Get songs for community - unity, belonging, together"""
        return self.get_songs_for_mission("community") + [
            "Duvarında Deliği", "Dünya Döner", "Nobody Home"
        ]
    
    def get_all_songs_with_mission(self) -> Dict[str, Dict[str, Any]]:
        """Get all songs with their mission alignment"""
        result = {}
        for title, song_data in self.songs_cache.items():
            mission_alignment = song_data.get("metadata", {}).get("mission_alignment", {})
            if mission_alignment:
                result[title] = mission_alignment
        return result


# Singleton instance
_song_integrator = None

def get_song_integrator() -> SongMissionIntegrator:
    """Get singleton instance of SongMissionIntegrator"""
    global _song_integrator
    if _song_integrator is None:
        _song_integrator = SongMissionIntegrator()
    return _song_integrator


__all__ = [
    "SongMissionIntegrator",
    "get_song_integrator"
]
