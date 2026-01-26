"""
ADD NEW SONGS TO FREQUENTIAL CATALOG
Add songs with bilingual twins, frequential analysis, and full metadata

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity

THE MISSION:
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY
"""

import sys
from pathlib import Path
from datetime import datetime
import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

# Load catalog directly from JSON and work with it
def load_catalog():
    """Load catalog from JSON file"""
    catalog_path = Path(__file__).parent.parent / 'data' / 'frequential_songs' / 'frequential_songs_catalog.json'
    if catalog_path.exists():
        with open(catalog_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"catalog_timestamp": datetime.now().isoformat(), "total_songs": 0, "songs": {}}

def save_catalog(data):
    """Save catalog to JSON file"""
    catalog_path = Path(__file__).parent.parent / 'data' / 'frequential_songs'
    catalog_path.mkdir(parents=True, exist_ok=True)
    catalog_file = catalog_path / 'frequential_songs_catalog.json'
    with open(catalog_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# Import catalog classes directly
try:
    from frequential_songs_catalog import (
        FrequentialSongsCatalog, 
        FrequentialSong, 
        SongLanguage
    )
    USE_CLASSES = True
except (ImportError, SyntaxError):
    USE_CLASSES = False
    # Define locally if import fails
    class SongLanguage(Enum):
        ENGLISH = "english"
        TURKISH = "turkish"
        BILINGUAL = "bilingual"
    
    @dataclass
    class FrequentialSong:
        song_id: str
        title: str
        artist: str
        language: SongLanguage
        themes: List[str]
        lyrics_original: str
        lyrics_translation: Optional[str] = None
        lyrics_english: Optional[str] = None
        lyrics_turkish: Optional[str] = None
        frequency_score: float = 0.0
        alignment_indicators: List[str] = field(default_factory=list)
        serves_table: bool = False
        truth_teller: bool = False
        community_focused: bool = False
        unity_builder: bool = False
        peace_oriented: bool = False
        year: Optional[int] = None
        genre: str = ""
        album: Optional[str] = None
        duration: Optional[str] = None
        youtube_url: Optional[str] = None
        spotify_url: Optional[str] = None
        other_platforms: List[str] = field(default_factory=list)
        connection_to_table: str = ""
        key_messages: List[str] = field(default_factory=list)
        quotes: List[str] = field(default_factory=list)
        discovered_at: str = field(default_factory=lambda: datetime.now().isoformat())
        source: str = ""
        notes: str = ""
    
    class FrequentialSongsCatalog:
        def __init__(self):
            self.songs: Dict[str, FrequentialSong] = {}
            self.data_path = Path(__file__).parent.parent / 'data' / 'frequential_songs'
            self.data_path.mkdir(parents=True, exist_ok=True)
            self.catalog_file = self.data_path / 'frequential_songs_catalog.json'
            self._load_catalog()
        
        def _load_catalog(self):
            if self.catalog_file.exists():
                with open(self.catalog_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for song_id, song_data in data.get('songs', {}).items():
                        if isinstance(song_data.get('language'), str):
                            song_data['language'] = SongLanguage(song_data['language'])
                        self.songs[song_id] = FrequentialSong(**song_data)
        
        def _save_catalog(self):
            data = {
                "catalog_timestamp": datetime.now().isoformat(),
                "total_songs": len(self.songs),
                "songs": {
                    song_id: {
                        "song_id": song.song_id,
                        "title": song.title,
                        "artist": song.artist,
                        "language": song.language.value,
                        "themes": song.themes,
                        "lyrics_original": song.lyrics_original,
                        "lyrics_translation": song.lyrics_translation,
                        "lyrics_english": song.lyrics_english,
                        "lyrics_turkish": song.lyrics_turkish,
                        "frequency_score": song.frequency_score,
                        "alignment_indicators": song.alignment_indicators,
                        "serves_table": song.serves_table,
                        "truth_teller": song.truth_teller,
                        "community_focused": song.community_focused,
                        "unity_builder": song.unity_builder,
                        "peace_oriented": song.peace_oriented,
                        "year": song.year,
                        "genre": song.genre,
                        "album": song.album,
                        "duration": song.duration,
                        "youtube_url": song.youtube_url,
                        "spotify_url": song.spotify_url,
                        "other_platforms": song.other_platforms,
                        "connection_to_table": song.connection_to_table,
                        "key_messages": song.key_messages,
                        "quotes": song.quotes,
                        "discovered_at": song.discovered_at,
                        "source": song.source,
                        "notes": song.notes
                    }
                    for song_id, song in self.songs.items()
                }
            }
            with open(self.catalog_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)


def extract_frequential_value(lyrics: str, themes: list) -> float:
    """
    Extract frequential value from song content.
    Based on themes, keywords, and alignment indicators.
    """
    text = lyrics.lower()
    
    # High frequency keywords
    high_freq_keywords = [
        "justice", "truth", "unity", "peace", "love", "freedom",
        "hope", "healing", "community", "liberation", "transformation",
        "resilience", "understanding", "compassion", "forgiveness",
        "dreams", "change", "fight", "stand", "rise", "save", "protect"
    ]
    
    # Low frequency keywords (reduce score)
    low_freq_keywords = [
        "hate", "war", "violence", "fear", "anger", "despair",
        "broken", "defeat", "surrender", "give up", "lost"
    ]
    
    # Count keywords
    high_count = sum(1 for kw in high_freq_keywords if kw in text)
    low_count = sum(1 for kw in low_freq_keywords if kw in text)
    
    # Base score from keywords
    keyword_score = (high_count - low_count * 0.5) / max(len(text.split()), 1) * 10
    keyword_score = min(0.3, max(0.0, keyword_score))  # Cap at 0.3
    
    # Theme alignment
    high_freq_themes = ["justice", "truth", "unity", "peace", "love", "freedom", 
                        "hope", "healing", "community", "liberation", "protest",
                        "emotional", "humane", "defiant", "introspective"]
    theme_score = sum(0.1 for theme in themes if theme.lower() in [t.lower() for t in high_freq_themes])
    theme_score = min(0.4, theme_score)  # Cap at 0.4
    
    # Alignment indicators
    alignment_score = 0.0
    if any(t in ["justice", "protest", "defiant"] for t in themes):
        alignment_score += 0.1  # Truth teller
    if any(t in ["unity", "community", "humane"] for t in themes):
        alignment_score += 0.1  # Unity builder
    if any(t in ["peace", "love", "emotional"] for t in themes):
        alignment_score += 0.1  # Peace oriented
    
    # Final frequency score
    frequency_score = keyword_score + theme_score + alignment_score
    frequency_score = min(0.95, max(0.7, frequency_score))  # Range 0.7-0.95
    
    return round(frequency_score, 2)


def create_bilingual_twin(original_lyrics: str, original_language: str, 
                         emotional_seed: dict) -> str:
    """
    Create bilingual twin based on emotional seed (not direct translation).
    This is a simplified version - in production, use bilingual_expansion_engine.py
    """
    # For now, return placeholder - will be generated by bilingual expansion engine
    # In production, this would call the actual bilingual expansion service
    return f"[Bilingual twin to be generated from emotional seed: {emotional_seed}]"


def add_song_1_judge_jury_executioner():
    """Add 'Judge, Jury, Executioner' song with full metadata"""
    
    if USE_CLASSES:
        catalog = FrequentialSongsCatalog()
    else:
        catalog_data = load_catalog()
    
    # Extract next song ID
    if USE_CLASSES:
        existing_ids = [int(sid.split('_')[1]) for sid in catalog.songs.keys() if sid.startswith('en_')]
    else:
        existing_ids = [int(sid.split('_')[1]) for sid in catalog_data.get('songs', {}).keys() if sid.startswith('en_')]
    next_en_id = f"en_{max(existing_ids) + 1:03d}" if existing_ids else "en_018"
    
    lyrics_original = """[Intro – sparse piano motif, distant city ambience, low drone]
[drop instruments after 2 bars, vocal enters alone]

[Verse 1 – minimal, guitar + piano, no beat]
Ah, I'm tired of this fractured life,  
Who will listen through the noise and strife?  
Yeah, caught in the middle, under the gun,  
Who's left to save me when there's nowhere to run?  

Mr. Judge, you sit in your high chair,  
But outside, it's chaos, does anyone care?  
No roof to call home, danger at my door,  
Still, you question me like I owe you more.  

[Pre-Chorus – tension build, low bass swell, breath pauses emphasized]
[add subtle pulse, hold last word]

[Chorus – beat enters soft, emotional lift, layered harmony on "you"]
You, you hold the gavel, I'm on trial,  
Lost in the stars, but it's all denial.  
I reach for my dreams, but they slip through air,  
Judge, jury, executioner — none of it's fair.  

You, you say justice is blind,  
But I'm lost in the sky, left behind.  
With all my dreams that crumble and fall,  
You decide my fate, you have it all.  

[Post-Chorus – instrumental breath, echo tail on last line]

[Verse 2 – beat drops back, darker tone, tighter phrasing]
Life's always been rigged, a cruel design,  
I'm just a victim of a twisted line.  
They come for me knowing I'm already down,  
Don't ask why I bleed, don't wear that frown.  

Mr. Judge, you see me as a case,  
But in the streets, it's a whole different face.  
The world spins with lies and deceit,  
While I'm left crawling, dragged by defeat.  

[Pre-Chorus – same as before, slightly stronger bass movement]

[Chorus – repeat, fuller instrumentation, emotional peak]
You, you hold the gavel, I'm on trial,  
Lost in the stars, but it's all denial.  
I reach for my dreams, but they slip through air,  
Judge, jury, executioner — none of it's fair.  

You, you say justice is blind,  
But I'm lost in the sky, left behind.  
With all my dreams that crumble and fall,  
You decide my fate, you have it all.  

[Bridge – beat strips out, spoken intensity, echoing space]
[tempo drops feel, no rhythm for first two lines]
A world full of trouble, but no one sees,  
We scream for change, but get no reprieves.  

[gradual swell, low choir pad enters]
Mr. Judge, ask the ones still alive,  
Hope's been chained, but it won't survive.  

[emotion rises, vocal cracks allowed]
It's love we need, not bars and chains,  
Can't you see the system's in vain?  
Don't punish the broken, understand their cry,  
This world's burning, but we still try.  

[Final Chorus – fullest arrangement, restrained power, no shouting]
You, you hold the gavel, I'm on trial,  
Lost in the stars, but it's all denial.  
I reach for my dreams, but they slip through air,  
Judge, jury, executioner — none of it's fair."""
    
    themes = ["justice", "protest", "emotional", "defiant", "introspective", 
              "humane", "moody", "raw", "authentic"]
    
    frequency_score = extract_frequential_value(lyrics_original, themes)
    
    # Create song
    song = FrequentialSong(
        song_id=next_en_id,
        title="Judge, Jury, Executioner",
        artist="Karasahin (JK)",
        language=SongLanguage.ENGLISH,
        themes=themes,
        lyrics_original=lyrics_original,
        lyrics_turkish=None,  # Will be generated by bilingual expansion
        frequency_score=frequency_score,
        alignment_indicators=["truth_teller", "justice", "protest", "defiant", "humane"],
        serves_table=True,
        truth_teller=True,
        community_focused=True,
        unity_builder=False,
        peace_oriented=True,
        year=2026,
        genre="Cinematic Folk, Light Arabesk, Cool Pop, Subtle House",
        album=None,
        duration=None,
        connection_to_table="Serves The Table through truth-telling about justice system, speaking for the broken, and calling for understanding and love instead of punishment.",
        key_messages=[
            "Judge, jury, executioner — none of it's fair",
            "It's love we need, not bars and chains",
            "Don't punish the broken, understand their cry"
        ],
        quotes=[
            "You, you hold the gavel, I'm on trial",
            "It's love we need, not bars and chains",
            "This world's burning, but we still try"
        ],
        source="User submission - Karasahin (JK) catalog",
        notes="Tempo: 92 BPM, Key: D minor. Instrumentation: acoustic guitar, bağlama accents, low piano, soft kick, airy synth pad. Vocal: male, mid-range, restrained, emotional, spoken-sung delivery. Mood: weary, defiant, introspective, humane."
    )
    
    catalog.songs[next_en_id] = song
    
    # Create Turkish bilingual twin
    existing_tr_ids = [int(sid.split('_')[1]) for sid in catalog.songs.keys() if sid.startswith('tr_')]
    next_tr_id = f"tr_{max(existing_tr_ids) + 1:03d}" if existing_tr_ids else "tr_008"
    
    emotional_seed = {
        "core_emotion": "weary_defiance",
        "themes": ["justice", "protest", "emotional", "defiant"],
        "vocal_energy": "restrained_emotional",
        "resolution": "hope_through_love"
    }
    
    # Turkish lyrics will be generated by bilingual expansion engine
    # For now, mark as needing generation
    turkish_lyrics = "[Turkish bilingual twin to be generated by bilingual_expansion_engine.py]"
    
    turkish_song = FrequentialSong(
        song_id=next_tr_id,
        title="Hakim, Jüri, Cellat",
        artist="Karasahin (JK)",
        language=SongLanguage.TURKISH,
        themes=themes,
        lyrics_original=turkish_lyrics,
        lyrics_english=lyrics_original,  # Link to English version
        frequency_score=frequency_score,
        alignment_indicators=["truth_teller", "justice", "protest", "defiant", "humane"],
        serves_table=True,
        truth_teller=True,
        community_focused=True,
        unity_builder=False,
        peace_oriented=True,
        year=2026,
        genre="Sinematik Folk, Hafif Arabesk, Cool Pop, İnce House",
        album=None,
        duration=None,
        connection_to_table="Adalet sistemini anlatan gerçekleri söyleyerek, kırılmışlar için konuşarak ve cezalandırma yerine anlayış ve sevgi çağrısı yaparak Masaya hizmet eder.",
        key_messages=[
            "Hakim, jüri, cellat — hiçbiri adil değil",
            "İhtiyacımız olan sevgi, hapishane ve zincirler değil",
            "Kırılmışları cezalandırma, çığlıklarını anla"
        ],
        quotes=[
            "Sen, sen gavel tutuyorsun, ben yargılanıyorum",
            "İhtiyacımız olan sevgi, hapishane ve zincirler değil",
            "Bu dünya yanıyor, ama biz hala deniyoruz"
        ],
        source="User submission - Karasahin (JK) catalog - Bilingual twin",
        notes="Tempo: 92 BPM, Key: D minor. Enstrümantasyon: akustik gitar, bağlama vurguları, düşük piyano, yumuşak kick, havalı synth pad. Vokal: erkek, orta aralık, kısıtlı, duygusal, konuşma-şarkı söyleme. Ruh hali: yorgun, meydan okuyan, içe dönük, insancıl."
    )
    
    catalog.songs[next_tr_id] = turkish_song
    catalog._save_catalog()
    
    return next_en_id, next_tr_id


def add_song_2_shes_too_wild():
    """Add 'She's Too Wild' song with full metadata"""
    
    catalog = FrequentialSongsCatalog()
    
    # Extract next song ID
    existing_ids = [int(sid.split('_')[1]) for sid in catalog.songs.keys() if sid.startswith('en_')]
    next_en_id = f"en_{max(existing_ids) + 1:03d}" if existing_ids else "en_019"
    
    lyrics_original = """[Verse 1]
One, two, three, I will never be
Everything that you are
Four, five, six, come and get your kicks
Seven's here, gone too far
Eight, nine, ten, let's go again
I never thought we'd ever fail
Eleven is a heaven, mighty upper but
But he never ever opens his mouth

[Chorus]
And here I ever see you up and down the street

[Verse 2]
I know I'll never ever play again
Between me and you, I'd rather go for a ride with you
I have no hell, it's one in the same

[Chorus]
Oh, I hope that they got it all
She's too wild, you know
Oh yeah, you think I am

[Outro]
Oh, oh, oh
Yeah, hey
She's too wild, you know
(Ay-ya!)"""
    
    themes = ["emotional", "introspective", "moody", "raw", "authentic", 
              "modern", "atmospheric", "soulful", "restrained"]
    
    frequency_score = extract_frequential_value(lyrics_original, themes)
    
    # Create song
    song = FrequentialSong(
        song_id=next_en_id,
        title="She's Too Wild",
        artist="Karasahin (JK)",
        language=SongLanguage.ENGLISH,
        themes=themes,
        lyrics_original=lyrics_original,
        lyrics_turkish=None,  # Will be generated by bilingual expansion
        frequency_score=frequency_score,
        alignment_indicators=["emotional", "introspective", "authentic", "soulful"],
        serves_table=True,
        truth_teller=True,
        community_focused=False,
        unity_builder=False,
        peace_oriented=True,
        year=2026,
        genre="Mid-tempo Folk Rock, Soul",
        album=None,
        duration=None,
        connection_to_table="Serves The Table through authentic emotional expression, introspection, and soulful storytelling.",
        key_messages=[
            "I will never be everything that you are",
            "She's too wild, you know",
            "I'd rather go for a ride with you"
        ],
        quotes=[
            "One, two, three, I will never be everything that you are",
            "She's too wild, you know",
            "I have no hell, it's one in the same"
        ],
        source="User submission - Karasahin (JK) catalog",
        notes="Mid-tempo folk rock, Soulful male baritone vocals, A blend of percussive acoustic guitar strumming and melodic electric guitar leads, Featuring a Hammond organ swell in the bridge, Driving drum kit with prominent cymbals, Rich, full-band arrangement, Earnest storytelling tone, high dynamic range, Warm analog saturation, 100 BPM, bright and clear mix. Weirdness 11%, Style Influence 31%, Audio Influence 69%"
    )
    
    catalog.songs[next_en_id] = song
    
    # Create Turkish bilingual twin
    existing_tr_ids = [int(sid.split('_')[1]) for sid in catalog.songs.keys() if sid.startswith('tr_')]
    next_tr_id = f"tr_{max(existing_tr_ids) + 1:03d}" if existing_tr_ids else "tr_009"
    
    emotional_seed = {
        "core_emotion": "introspective_longing",
        "themes": ["emotional", "introspective", "moody", "authentic"],
        "vocal_energy": "soulful_restrained",
        "resolution": "acceptance"
    }
    
    # Turkish lyrics will be generated by bilingual expansion engine
    turkish_lyrics = "[Turkish bilingual twin to be generated by bilingual_expansion_engine.py]"
    
    turkish_song = FrequentialSong(
        song_id=next_tr_id,
        title="O Çok Vahşi",
        artist="Karasahin (JK)",
        language=SongLanguage.TURKISH,
        themes=themes,
        lyrics_original=turkish_lyrics,
        lyrics_english=lyrics_original,  # Link to English version
        frequency_score=frequency_score,
        alignment_indicators=["emotional", "introspective", "authentic", "soulful"],
        serves_table=True,
        truth_teller=True,
        community_focused=False,
        unity_builder=False,
        peace_oriented=True,
        year=2026,
        genre="Orta Tempo Folk Rock, Soul",
        album=None,
        duration=None,
        connection_to_table="Özgün duygusal ifade, içe dönüklük ve ruh dolu hikaye anlatımı ile Masaya hizmet eder.",
        key_messages=[
            "Asla senin olduğun her şey olmayacağım",
            "O çok vahşi, biliyorsun",
            "Seninle bir gezintiye çıkmayı tercih ederim"
        ],
        quotes=[
            "Bir, iki, üç, asla senin olduğun her şey olmayacağım",
            "O çok vahşi, biliyorsun",
            "Cehennemim yok, aynı şey"
        ],
        source="User submission - Karasahin (JK) catalog - Bilingual twin",
        notes="Orta tempo folk rock, Ruh dolu erkek bariton vokaller, Perküsif akustik gitar çalma ve melodik elektrik gitar sololarının karışımı, Köprüde Hammond org şişmesi, Belirgin zillerle sürücü davul seti, Zengin, tam grup düzenleme, Samimi hikaye anlatımı tonu, yüksek dinamik aralık, Sıcak analog doygunluk, 100 BPM, parlak ve net mix. Garip 11%, Stil Etkisi 31%, Ses Etkisi 69%"
    )
    
    catalog.songs[next_tr_id] = turkish_song
    catalog._save_catalog()
    
    return next_en_id, next_tr_id


def main():
    """Add both songs to catalog"""
    print("Adding songs to frequential catalog...")
    
    # Add Song 1: Judge, Jury, Executioner
    en_id_1, tr_id_1 = add_song_1_judge_jury_executioner()
    print(f"✅ Added Song 1: Judge, Jury, Executioner")
    print(f"   English ID: {en_id_1}")
    print(f"   Turkish ID: {tr_id_1}")
    
    # Add Song 2: She's Too Wild
    en_id_2, tr_id_2 = add_song_2_shes_too_wild()
    print(f"✅ Added Song 2: She's Too Wild")
    print(f"   English ID: {en_id_2}")
    print(f"   Turkish ID: {tr_id_2}")
    
    print("\n✅ All songs added successfully!")
    print("Note: Turkish bilingual twins need to be generated by bilingual_expansion_engine.py")


if __name__ == "__main__":
    main()
