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


def add_song_3():
    """Add 'Someone on TV' song"""
    catalog = load_catalog()
    
    existing_ids = [int(sid.split('_')[1]) for sid in catalog.get('songs', {}).keys() if sid.startswith('en_')]
    next_en_id = f"en_{max(existing_ids) + 1:03d}" if existing_ids else "en_014"
    
    lyrics = """[Verse 1]
All I ever really wanted to be was someone on TV
Someone people could see, cause then you can get away with almost anything
You put your mind to
I've forgotten everything you've ever seen for
Everything you've ever believed in
Oh, that's a funny way to live your life, but it's
I said, can you hear me?

[Verse 2]
And ever since you left me, I've been running around
I've been chasing every piece of ass
Sooner or later, one of them might just crash

[Instrumental]
Crash
Crash"""
    
    themes = ["emotional", "introspective", "moody", "raw", "authentic", 
              "modern", "atmospheric", "melancholic", "reflective", "evocative"]
    
    freq_score = extract_frequential_value(lyrics, themes)
    
    song_data = {
        "song_id": next_en_id,
        "title": "Someone on TV",
        "artist": "Karasahin (JK)",
        "language": "english",
        "themes": themes,
        "lyrics_original": lyrics,
        "lyrics_translation": None,
        "lyrics_english": None,
        "lyrics_turkish": None,
        "frequency_score": freq_score,
        "alignment_indicators": ["emotional", "introspective", "authentic", "reflective"],
        "serves_table": True,
        "truth_teller": True,
        "community_focused": False,
        "unity_builder": False,
        "peace_oriented": True,
        "year": 2026,
        "genre": "Mid-tempo Indie Folk Rock",
        "album": None,
        "duration": None,
        "youtube_url": None,
        "spotify_url": None,
        "other_platforms": [],
        "connection_to_table": "Serves The Table through authentic emotional expression, introspection, and evocative storytelling about identity and longing.",
        "key_messages": [
            "All I ever really wanted to be was someone on TV",
            "I've forgotten everything you've ever seen for",
            "Sooner or later, one of them might just crash"
        ],
        "quotes": [
            "All I ever really wanted to be was someone on TV",
            "Someone people could see, cause then you can get away with almost anything",
            "I've been chasing every piece of ass"
        ],
        "discovered_at": datetime.now().isoformat(),
        "source": "User submission - Karasahin (JK) catalog",
        "notes": "Mid-tempo indie folk rock, melancholic yet driving, Mellow male vocals, harmonizing with himself in the chorus, Clean acoustic guitar strumming, syncopated rhythm, melodic bass guitar, Subtle Rhodes piano accents, The vibe is lonely but rhythmic, like a long drive at dusk, Crisp production, clear vocals, 105 BPM, Bittersweet, reflective, evocative storytelling. Weirdness 11%, Style Influence 31%, Audio Influence 69%. Genres: folk, pop, emotional, acoustic, piano, mid-tempo, minor, moody, introspective, raw, authentic, modern, atmospheric, urban, soulful, restrained, melancholic, reflective, evocative."
    }
    
    catalog['songs'][next_en_id] = song_data
    
    # Turkish twin
    existing_tr_ids = [int(sid.split('_')[1]) for sid in catalog.get('songs', {}).keys() if sid.startswith('tr_')]
    next_tr_id = f"tr_{max(existing_tr_ids) + 1:03d}" if existing_tr_ids else "tr_011"
    
    turkish_song = {
        "song_id": next_tr_id,
        "title": "Televizyonda Biri",
        "artist": "Karasahin (JK)",
        "language": "turkish",
        "themes": themes,
        "lyrics_original": "[Turkish bilingual twin to be generated by bilingual_expansion_engine.py]",
        "lyrics_translation": None,
        "lyrics_english": lyrics,
        "lyrics_turkish": None,
        "frequency_score": freq_score,
        "alignment_indicators": ["emotional", "introspective", "authentic", "reflective"],
        "serves_table": True,
        "truth_teller": True,
        "community_focused": False,
        "unity_builder": False,
        "peace_oriented": True,
        "year": 2026,
        "genre": "Orta Tempo Indie Folk Rock",
        "album": None,
        "duration": None,
        "youtube_url": None,
        "spotify_url": None,
        "other_platforms": [],
        "connection_to_table": "Kimlik ve özlem hakkında özgün duygusal ifade, içe dönüklük ve etkileyici hikaye anlatımı ile Masaya hizmet eder.",
        "key_messages": [
            "Tek istediğim televizyonda biri olmaktı",
            "Gördüğün her şeyi unuttum",
            "Er ya da geç, biri çökebilir"
        ],
        "quotes": [
            "Tek istediğim televizyonda biri olmaktı",
            "İnsanların görebileceği biri, çünkü o zaman neredeyse her şeyi yapabilirsin",
            "Her parçayı kovalıyorum"
        ],
        "discovered_at": datetime.now().isoformat(),
        "source": "User submission - Karasahin (JK) catalog - Bilingual twin",
        "notes": "Orta tempo indie folk rock, melankolik ama sürücü, Yumuşak erkek vokaller, nakaratta kendisiyle uyumlu, Temiz akustik gitar çalma, senkoplu ritim, melodik bas gitar, İnce Rhodes piyano vurguları, Ruh hali yalnız ama ritmik, alacakaranlıkta uzun bir sürüş gibi, Net üretim, net vokaller, 105 BPM, Acı-tatlı, düşündürücü, etkileyici hikaye anlatımı."
    }
    
    catalog['songs'][next_tr_id] = turkish_song
    catalog['total_songs'] = len(catalog['songs'])
    catalog['catalog_timestamp'] = datetime.now().isoformat()
    
    save_catalog(catalog)
    return next_en_id, next_tr_id


def add_song_4():
    """Add 'Kıbrıs Bizim Canımız' song"""
    catalog = load_catalog()
    
    existing_ids = [int(sid.split('_')[1]) for sid in catalog.get('songs', {}).keys() if sid.startswith('tr_')]
    next_tr_id = f"tr_{max(existing_ids) + 1:03d}" if existing_ids else "tr_012"
    
    lyrics = """[Intro – slow ceremonial opening]
[Low davul heartbeat in 4/4; distant male choir hums on a single note; deep cello drones establish gravity]
(Voice enters solemn, restrained, almost spoken, with controlled vibrato)

Kıta 1
Dünya yanar dert içinde
Toprak kavga, kan izinde
Masum canlar göç içinde
Ağlar yürek, sönmez közüm

[Strings begin to rise slowly; bağlama tremolo underneath last line; breath audible at phrase ends]

⸻

[Nakarat – first lift, dignified not explosive yet]
[Mehter-style snare rolls softly; choir opens into harmony thirds; tempo steady]
(Vocal grows fuller, proud but mournful)

Nakarat
Kıbrıs bizim canımız
Toprağında kanımız
Gerçek Kıbrıslı direnir
Yaşatır vatanımız

[Last line held with sustained vibrato; short echo tail]

⸻

[Kıta 2 – movement and memory]
[Rhythm tightens; subtle rhythmic oud pattern joins; violins pulse gently]
(Vocal slightly warmer, reflective rather than angry)

Kıta 2
Anılarla dolu dağlar
Göçmen geçti, kaldı yarlar
Cennetime açtı yollar
Yine biziz köklerimiz

[Choir hums quietly under "köklerimiz"]

⸻

[Nakarat – stronger, collective voice]
[Davul hits heavier; brass (trumpet + horn blend) answers melody; crowd texture fades in]
(Vocal firm, resolute, chest-led)

Nakarat
Kıbrıs bizim canımız
Toprağında kanımız
Gerçek Kıbrıslı direnir
Yaşatır vatanımız

⸻

[Kıta 3 – hope and resolve]
[Music briefly drops back; single cello + piano; light breath before first word]
(Vocal tender, hopeful, lifted at phrase ends)

Kıta 3
Güneş doğar umut ile
Barış gelsin sevda dile
Özgür yaşa kendiyle
Kıbrıs'ın kalbinde biz

[String swell begins midway through verse, foreshadowing finale]

⸻

[Nakarat (2x) – final anthem]
[Full orchestra unleashed: davul, mehter snare, soaring strings, brass fanfares, massive choir]
(First pass strong; second pass louder, communal, almost shouted)

Nakarat
Kıbrıs bizim canımız
Toprağında kanımız
Gerçek Kıbrıslı direnir
Yaşatır vatanımız

Nakarat (repeat)
Kıbrıs bizim canımız
Toprağında kanımız
Gerçek Kıbrıslı direnir
Yaşatır vatanımız

[Outro – reverent fade]
[Choir sustains final chord; lone cello descends; distant davul heartbeat fades into silence]"""
    
    themes = ["patriotic", "identity", "resilience", "hope", "unity", "emotional", 
              "ceremonial", "historical", "proud", "mournful", "defiant", "communal"]
    
    freq_score = extract_frequential_value(lyrics, themes)
    
    song_data = {
        "song_id": next_tr_id,
        "title": "Kıbrıs Bizim Canımız",
        "artist": "Karasahin (JK)",
        "language": "turkish",
        "themes": themes,
        "lyrics_original": lyrics,
        "lyrics_translation": None,
        "lyrics_english": None,
        "lyrics_turkish": None,
        "frequency_score": freq_score,
        "alignment_indicators": ["unity_builder", "community_focused", "peace_oriented", "identity", "resilience"],
        "serves_table": True,
        "truth_teller": True,
        "community_focused": True,
        "unity_builder": True,
        "peace_oriented": True,
        "year": 2026,
        "genre": "Epic Anatolian Patriotic Ballad, Arabesk, Folk",
        "album": None,
        "duration": None,
        "youtube_url": None,
        "spotify_url": None,
        "other_platforms": [],
        "connection_to_table": "Serves The Table through honoring Cyprus identity, resilience, and unity. A song of land, roots, and endurance that moves from grief to remembrance to unity to defiant hope.",
        "key_messages": [
            "Kıbrıs bizim canımız",
            "Gerçek Kıbrıslı direnir",
            "Yaşatır vatanımız",
            "Güneş doğar umut ile"
        ],
        "quotes": [
            "Kıbrıs bizim canımız",
            "Toprağında kanımız",
            "Gerçek Kıbrıslı direnir",
            "Yaşatır vatanımız"
        ],
        "discovered_at": datetime.now().isoformat(),
        "source": "User submission - Karasahin (JK) catalog",
        "notes": "Epic Anatolian patriotic ballad with strong arabesque and folk foundations, performed by a deep male vocal with emotional vibrato and dignified restraint, Tempo mid-slow, ceremonial and steady, Arrangement builds from sparse davul, cello, and drone into a full Ottoman-inspired orchestral anthem, Instrumentation includes davul, mehter snare, bağlama, oud, deep cellos, soaring violins, cinematic brass, and a powerful male choir, Mood is mournful yet proud, rooted in history, resilience, and identity, Vocals should feel sincere, grounded, and communal — never pop, never glossy, Production cinematic and spacious, with wide stereo strings, deep low-end percussion, and reverbs that feel like open land and memory, Emotional arc moves from grief → remembrance → unity → defiant hope, Timeless, serious, and respectful — a song of land, roots, and endurance. Weirdness 11%, Style Influence 31%. Genres: cinematic, folk, arabesk, patriotic, emotional, justice, acoustic, piano, bağlama, mid-tempo, minor, moody, introspective, defiant, humane, raw, authentic, modern, atmospheric, urban, soulful, ceremonial, historical, proud, mournful, communal."
    }
    
    catalog['songs'][next_tr_id] = song_data
    
    # English twin
    existing_en_ids = [int(sid.split('_')[1]) for sid in catalog.get('songs', {}).keys() if sid.startswith('en_')]
    next_en_id = f"en_{max(existing_en_ids) + 1:03d}" if existing_en_ids else "en_015"
    
    english_lyrics = "[English bilingual twin to be generated by bilingual_expansion_engine.py]"
    
    english_song = {
        "song_id": next_en_id,
        "title": "Cyprus Is Our Soul",
        "artist": "Karasahin (JK)",
        "language": "english",
        "themes": themes,
        "lyrics_original": english_lyrics,
        "lyrics_translation": None,
        "lyrics_english": None,
        "lyrics_turkish": lyrics,
        "frequency_score": freq_score,
        "alignment_indicators": ["unity_builder", "community_focused", "peace_oriented", "identity", "resilience"],
        "serves_table": True,
        "truth_teller": True,
        "community_focused": True,
        "unity_builder": True,
        "peace_oriented": True,
        "year": 2026,
        "genre": "Epic Anatolian Patriotic Ballad, Arabesk, Folk",
        "album": None,
        "duration": None,
        "youtube_url": None,
        "spotify_url": None,
        "other_platforms": [],
        "connection_to_table": "Serves The Table through honoring Cyprus identity, resilience, and unity. A song of land, roots, and endurance that moves from grief to remembrance to unity to defiant hope.",
        "key_messages": [
            "Cyprus is our soul",
            "True Cypriot resists",
            "We keep our homeland alive",
            "Sun rises with hope"
        ],
        "quotes": [
            "Cyprus is our soul",
            "Our blood in its soil",
            "True Cypriot resists",
            "We keep our homeland alive"
        ],
        "discovered_at": datetime.now().isoformat(),
        "source": "User submission - Karasahin (JK) catalog - Bilingual twin",
        "notes": "Epic Anatolian patriotic ballad with strong arabesque and folk foundations, performed by a deep male vocal with emotional vibrato and dignified restraint, Tempo mid-slow, ceremonial and steady, Arrangement builds from sparse davul, cello, and drone into a full Ottoman-inspired orchestral anthem, Instrumentation includes davul, mehter snare, bağlama, oud, deep cellos, soaring violins, cinematic brass, and a powerful male choir, Mood is mournful yet proud, rooted in history, resilience, and identity, Vocals should feel sincere, grounded, and communal — never pop, never glossy, Production cinematic and spacious, with wide stereo strings, deep low-end percussion, and reverbs that feel like open land and memory, Emotional arc moves from grief → remembrance → unity → defiant hope, Timeless, serious, and respectful — a song of land, roots, and endurance."
    }
    
    catalog['songs'][next_en_id] = english_song
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
    
    en_id_3, tr_id_3 = add_song_3()
    print(f"[OK] Added Song 3: Someone on TV")
    print(f"   English ID: {en_id_3}")
    print(f"   Turkish ID: {tr_id_3}")
    
    en_id_4, tr_id_4 = add_song_4()
    print(f"[OK] Added Song 4: Kibris Bizim Canimiz")
    print(f"   English ID: {en_id_4}")
    print(f"   Turkish ID: {tr_id_4}")
    
    print("\n[OK] All songs added successfully!")
    print("Note: Bilingual twins need to be generated by bilingual_expansion_engine.py")


if __name__ == "__main__":
    main()
