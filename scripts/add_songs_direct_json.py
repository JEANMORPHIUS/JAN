"""
ADD NEW SONGS TO FREQUENTIAL CATALOG - Direct JSON Version
Add songs with bilingual twins, frequential analysis, and full metadata

DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
Spiritual Alignment Over Mechanical Productivity
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List


def extract_frequential_value(lyrics: str, themes: list) -> float:
    """Extract frequential value from song content"""
    text = lyrics.lower()
    
    high_freq_keywords = [
        "justice", "truth", "unity", "peace", "love", "freedom",
        "hope", "healing", "community", "liberation", "transformation",
        "resilience", "understanding", "compassion", "forgiveness",
        "dreams", "change", "fight", "stand", "rise", "save", "protect"
    ]
    
    low_freq_keywords = [
        "hate", "war", "violence", "fear", "anger", "despair",
        "broken", "defeat", "surrender", "give up", "lost"
    ]
    
    high_count = sum(1 for kw in high_freq_keywords if kw in text)
    low_count = sum(1 for kw in low_freq_keywords if kw in text)
    
    keyword_score = (high_count - low_count * 0.5) / max(len(text.split()), 1) * 10
    keyword_score = min(0.3, max(0.0, keyword_score))
    
    high_freq_themes = ["justice", "truth", "unity", "peace", "love", "freedom", 
                        "hope", "healing", "community", "liberation", "protest",
                        "emotional", "humane", "defiant", "introspective"]
    theme_score = sum(0.1 for theme in themes if theme.lower() in [t.lower() for t in high_freq_themes])
    theme_score = min(0.4, theme_score)
    
    alignment_score = 0.0
    if any(t in ["justice", "protest", "defiant"] for t in themes):
        alignment_score += 0.1
    if any(t in ["unity", "community", "humane"] for t in themes):
        alignment_score += 0.1
    if any(t in ["peace", "love", "emotional"] for t in themes):
        alignment_score += 0.1
    
    frequency_score = keyword_score + theme_score + alignment_score
    frequency_score = min(0.95, max(0.7, frequency_score))
    
    return round(frequency_score, 2)


def load_catalog() -> Dict:
    """Load catalog from JSON"""
    catalog_path = Path(__file__).parent.parent / 'data' / 'frequential_songs' / 'frequential_songs_catalog.json'
    if catalog_path.exists():
        with open(catalog_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"catalog_timestamp": datetime.now().isoformat(), "total_songs": 0, "songs": {}}


def save_catalog(data: Dict):
    """Save catalog to JSON"""
    catalog_path = Path(__file__).parent.parent / 'data' / 'frequential_songs'
    catalog_path.mkdir(parents=True, exist_ok=True)
    catalog_file = catalog_path / 'frequential_songs_catalog.json'
    with open(catalog_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def add_song_1():
    """Add 'Judge, Jury, Executioner' song"""
    catalog = load_catalog()
    
    existing_ids = [int(sid.split('_')[1]) for sid in catalog.get('songs', {}).keys() if sid.startswith('en_')]
    next_en_id = f"en_{max(existing_ids) + 1:03d}" if existing_ids else "en_018"
    
    lyrics = """[Intro – sparse piano motif, distant city ambience, low drone]
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
    
    freq_score = extract_frequential_value(lyrics, themes)
    
    song_data = {
        "song_id": next_en_id,
        "title": "Judge, Jury, Executioner",
        "artist": "Karasahin (JK)",
        "language": "english",
        "themes": themes,
        "lyrics_original": lyrics,
        "lyrics_translation": None,
        "lyrics_english": None,
        "lyrics_turkish": None,
        "frequency_score": freq_score,
        "alignment_indicators": ["truth_teller", "justice", "protest", "defiant", "humane"],
        "serves_table": True,
        "truth_teller": True,
        "community_focused": True,
        "unity_builder": False,
        "peace_oriented": True,
        "year": 2026,
        "genre": "Cinematic Folk, Light Arabesk, Cool Pop, Subtle House",
        "album": None,
        "duration": None,
        "youtube_url": None,
        "spotify_url": None,
        "other_platforms": [],
        "connection_to_table": "Serves The Table through truth-telling about justice system, speaking for the broken, and calling for understanding and love instead of punishment.",
        "key_messages": [
            "Judge, jury, executioner — none of it's fair",
            "It's love we need, not bars and chains",
            "Don't punish the broken, understand their cry"
        ],
        "quotes": [
            "You, you hold the gavel, I'm on trial",
            "It's love we need, not bars and chains",
            "This world's burning, but we still try"
        ],
        "discovered_at": datetime.now().isoformat(),
        "source": "User submission - Karasahin (JK) catalog",
        "notes": "Tempo: 92 BPM, Key: D minor. Instrumentation: acoustic guitar, bağlama accents, low piano, soft kick, airy synth pad. Vocal: male, mid-range, restrained, emotional, spoken-sung delivery. Mood: weary, defiant, introspective, humane. Genres: cinematic, folk, pop, arabesk, house, protest, emotional, justice, acoustic, piano, bağlama, mid-tempo, minor, moody, introspective, defiant, humane, spoken-sung, raw, authentic, modern, atmospheric, urban, soulful, restrained."
    }
    
    catalog['songs'][next_en_id] = song_data
    
    # Turkish twin
    existing_tr_ids = [int(sid.split('_')[1]) for sid in catalog.get('songs', {}).keys() if sid.startswith('tr_')]
    next_tr_id = f"tr_{max(existing_tr_ids) + 1:03d}" if existing_tr_ids else "tr_008"
    
    turkish_song = {
        "song_id": next_tr_id,
        "title": "Hakim, Jüri, Cellat",
        "artist": "Karasahin (JK)",
        "language": "turkish",
        "themes": themes,
        "lyrics_original": "[Turkish bilingual twin to be generated by bilingual_expansion_engine.py]",
        "lyrics_translation": None,
        "lyrics_english": lyrics,
        "lyrics_turkish": None,
        "frequency_score": freq_score,
        "alignment_indicators": ["truth_teller", "justice", "protest", "defiant", "humane"],
        "serves_table": True,
        "truth_teller": True,
        "community_focused": True,
        "unity_builder": False,
        "peace_oriented": True,
        "year": 2026,
        "genre": "Sinematik Folk, Hafif Arabesk, Cool Pop, İnce House",
        "album": None,
        "duration": None,
        "youtube_url": None,
        "spotify_url": None,
        "other_platforms": [],
        "connection_to_table": "Adalet sistemini anlatan gerçekleri söyleyerek, kırılmışlar için konuşarak ve cezalandırma yerine anlayış ve sevgi çağrısı yaparak Masaya hizmet eder.",
        "key_messages": [
            "Hakim, jüri, cellat — hiçbiri adil değil",
            "İhtiyacımız olan sevgi, hapishane ve zincirler değil",
            "Kırılmışları cezalandırma, çığlıklarını anla"
        ],
        "quotes": [
            "Sen, sen gavel tutuyorsun, ben yargılanıyorum",
            "İhtiyacımız olan sevgi, hapishane ve zincirler değil",
            "Bu dünya yanıyor, ama biz hala deniyoruz"
        ],
        "discovered_at": datetime.now().isoformat(),
        "source": "User submission - Karasahin (JK) catalog - Bilingual twin",
        "notes": "Tempo: 92 BPM, Key: D minor. Enstrümantasyon: akustik gitar, bağlama vurguları, düşük piyano, yumuşak kick, havalı synth pad. Vokal: erkek, orta aralık, kısıtlı, duygusal, konuşma-şarkı söyleme. Ruh hali: yorgun, meydan okuyan, içe dönük, insancıl."
    }
    
    catalog['songs'][next_tr_id] = turkish_song
    catalog['total_songs'] = len(catalog['songs'])
    catalog['catalog_timestamp'] = datetime.now().isoformat()
    
    save_catalog(catalog)
    return next_en_id, next_tr_id


def add_song_2():
    """Add 'She's Too Wild' song"""
    catalog = load_catalog()
    
    existing_ids = [int(sid.split('_')[1]) for sid in catalog.get('songs', {}).keys() if sid.startswith('en_')]
    next_en_id = f"en_{max(existing_ids) + 1:03d}" if existing_ids else "en_019"
    
    lyrics = """[Verse 1]
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
    
    freq_score = extract_frequential_value(lyrics, themes)
    
    song_data = {
        "song_id": next_en_id,
        "title": "She's Too Wild",
        "artist": "Karasahin (JK)",
        "language": "english",
        "themes": themes,
        "lyrics_original": lyrics,
        "lyrics_translation": None,
        "lyrics_english": None,
        "lyrics_turkish": None,
        "frequency_score": freq_score,
        "alignment_indicators": ["emotional", "introspective", "authentic", "soulful"],
        "serves_table": True,
        "truth_teller": True,
        "community_focused": False,
        "unity_builder": False,
        "peace_oriented": True,
        "year": 2026,
        "genre": "Mid-tempo Folk Rock, Soul",
        "album": None,
        "duration": None,
        "youtube_url": None,
        "spotify_url": None,
        "other_platforms": [],
        "connection_to_table": "Serves The Table through authentic emotional expression, introspection, and soulful storytelling.",
        "key_messages": [
            "I will never be everything that you are",
            "She's too wild, you know",
            "I'd rather go for a ride with you"
        ],
        "quotes": [
            "One, two, three, I will never be everything that you are",
            "She's too wild, you know",
            "I have no hell, it's one in the same"
        ],
        "discovered_at": datetime.now().isoformat(),
        "source": "User submission - Karasahin (JK) catalog",
        "notes": "Mid-tempo folk rock, Soulful male baritone vocals, A blend of percussive acoustic guitar strumming and melodic electric guitar leads, Featuring a Hammond organ swell in the bridge, Driving drum kit with prominent cymbals, Rich, full-band arrangement, Earnest storytelling tone, high dynamic range, Warm analog saturation, 100 BPM, bright and clear mix. Weirdness 11%, Style Influence 31%, Audio Influence 69%. Genres: folk, pop, emotional, acoustic, piano, mid-tempo, minor, moody, introspective, raw, authentic, modern, atmospheric, urban, soulful, restrained."
    }
    
    catalog['songs'][next_en_id] = song_data
    
    # Turkish twin
    existing_tr_ids = [int(sid.split('_')[1]) for sid in catalog.get('songs', {}).keys() if sid.startswith('tr_')]
    next_tr_id = f"tr_{max(existing_tr_ids) + 1:03d}" if existing_tr_ids else "tr_009"
    
    turkish_song = {
        "song_id": next_tr_id,
        "title": "O Çok Vahşi",
        "artist": "Karasahin (JK)",
        "language": "turkish",
        "themes": themes,
        "lyrics_original": "[Turkish bilingual twin to be generated by bilingual_expansion_engine.py]",
        "lyrics_translation": None,
        "lyrics_english": lyrics,
        "lyrics_turkish": None,
        "frequency_score": freq_score,
        "alignment_indicators": ["emotional", "introspective", "authentic", "soulful"],
        "serves_table": True,
        "truth_teller": True,
        "community_focused": False,
        "unity_builder": False,
        "peace_oriented": True,
        "year": 2026,
        "genre": "Orta Tempo Folk Rock, Soul",
        "album": None,
        "duration": None,
        "youtube_url": None,
        "spotify_url": None,
        "other_platforms": [],
        "connection_to_table": "Özgün duygusal ifade, içe dönüklük ve ruh dolu hikaye anlatımı ile Masaya hizmet eder.",
        "key_messages": [
            "Asla senin olduğun her şey olmayacağım",
            "O çok vahşi, biliyorsun",
            "Seninle bir gezintiye çıkmayı tercih ederim"
        ],
        "quotes": [
            "Bir, iki, üç, asla senin olduğun her şey olmayacağım",
            "O çok vahşi, biliyorsun",
            "Cehennemim yok, aynı şey"
        ],
        "discovered_at": datetime.now().isoformat(),
        "source": "User submission - Karasahin (JK) catalog - Bilingual twin",
        "notes": "Orta tempo folk rock, Ruh dolu erkek bariton vokaller, Perküsif akustik gitar çalma ve melodik elektrik gitar sololarının karışımı, Köprüde Hammond org şişmesi, Belirgin zillerle sürücü davul seti, Zengin, tam grup düzenleme, Samimi hikaye anlatımı tonu, yüksek dinamik aralık, Sıcak analog doygunluk, 100 BPM, parlak ve net mix. Garip 11%, Stil Etkisi 31%, Ses Etkisi 69%"
    }
    
    catalog['songs'][next_tr_id] = turkish_song
    catalog['total_songs'] = len(catalog['songs'])
    catalog['catalog_timestamp'] = datetime.now().isoformat()
    
    save_catalog(catalog)
    return next_en_id, next_tr_id


def main():
    print("Adding songs to frequential catalog...")
    
    en_id_1, tr_id_1 = add_song_1()
    print(f"[OK] Added Song 1: Judge, Jury, Executioner")
    print(f"   English ID: {en_id_1}")
    print(f"   Turkish ID: {tr_id_1}")
    
    en_id_2, tr_id_2 = add_song_2()
    print(f"[OK] Added Song 2: She's Too Wild")
    print(f"   English ID: {en_id_2}")
    print(f"   Turkish ID: {tr_id_2}")
    
    print("\n[OK] All songs added successfully!")
    print("Note: Turkish bilingual twins need to be generated by bilingual_expansion_engine.py")


if __name__ == "__main__":
    main()
