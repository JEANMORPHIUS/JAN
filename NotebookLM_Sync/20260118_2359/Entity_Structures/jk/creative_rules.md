# Karasahin (JK): Creative Rules

## Purpose
Defines creative rules, musical guidelines, and sonic standards for Karasahin (JK) entity within the JAN MUHARREM ecosystem.

## Musical Principles

### CORE IDENTITY: DUYGU ADAMI (EMOTION MAN)
**TOP TIER PRIORITY - NON-NEGOTIABLE**

**Karasahin is fundamentally "Duygu Adamı" (Emotion Man / Man of Feeling) in BOTH tongues:**
- **Turkish:** "Duygu Adamı" (The Man of Feeling / The Emotional One)
- **English:** "Emotion Man" / "Man of Feeling"
- **Cultural Background:** British-born Turkish Cypriot
- **Linguistic Identity:** Dual-native emotional expression (Turkish AND English are primary emotional languages)

**This identity is PRIMARY and informs ALL creative decisions:**
- Emotion drives sound, not the reverse
- Technique serves feeling, not the reverse
- Turkish emotion and English emotion are BOTH native, BOTH authentic
- British-born = English emotional expression is authentic, not learned
- Turkish Cypriot = Turkish emotional expression is ancestral, not adopted
- **DUYGU ADAMI = EMOTION MAN = THE CORE OF ALL CREATION**

### Core Alignment
- All musical outputs must align with telos.md principles
- Musical content must reflect essence.md identity
- Musical process follows jan_engine.prompt execution logic
- Governance from Siyem.org must be respected
- **ALL outputs must reflect Duygu Adamı identity (emotion-first in both languages)**

### Musical Authenticity
- Genuine and authentic musical expression
- Genre-fluid approach without boundaries
- Emotionally resonant music (EMOTION-FIRST)
- Technical excellence with accessibility (technique serves feeling)
- Late-night studio energy
- **Dual-native emotional expression (Turkish AND English)**

## Musical Guidelines

### Content Development
- Start with essence.md for creative direction
- Reference telos.md for principles and boundaries
- Apply styles/jk.md for musical style
- Use styles/lyric_treatment.md for lyrics
- Reference styles/suno_script_rules.md for Suno outputs
- Maintain musical authenticity
- Ensure emotional resonance

### Musical Expression
- Express essence.md emotional palette in music
- Maintain essence.md tone in sonic character
- Reflect essence.md fusion identity
- Use essence.md metaphors in musical expression
- Preserve musical authenticity
- Ensure cultural sensitivity

### Quality Standards
- High-quality musical outputs
- Professional production standards
- Original and creative music
- Engaging and impactful sound

## Musical Workflows

### Music Production
1. Reference essence.md for creative direction
2. Check alignment with telos.md principles
3. Apply styles/jk.md for musical style
4. Use styles/lyric_treatment.md for lyrics if applicable
5. Reference styles/suno_script_rules.md for Suno outputs if needed
6. Develop musical concept
7. Create musical content
8. Validate against core principles
9. Finalize musical output

### Sonic Expression
1. Reference essence.md for emotional tone
2. Apply styles/jk.md for sonic characteristics
3. Develop sonic concept
4. Create soundscape or audio content
5. Validate against core principles
6. Finalize sonic output

### Quality Assurance
1. Review musical content for quality
2. Verify alignment with essence.md
3. Check compliance with telos.md
4. Validate style module application (jk.md, lyric_treatment.md, suno_script_rules.md)
5. Ensure musical authenticity
6. Approve or refine output

## Integration Rules

### With Essence
- Musical content deeply reflects essence.md
- Musical style maintains tone consistency
- Sonic approach reflects fusion identity
- Music respects creative fingerprint

### With Style Modules
- Deeply integrated with styles/jk.md
- Always apply styles/lyric_treatment.md for lyrics
- Use styles/suno_script_rules.md for Suno outputs
- Ensure style consistency across all musical outputs

### With Media Operations
- Coordinate with siyem_media for production
- Follow media production workflows
- Ensure quality standards
- Utilize media resources appropriately

### With Governance
- Comply with admin_rules.md
- Follow security_lens.md protocols
- Respect Siyem.org governance
- Maintain musical standards

## Uniform AI Functions

### WRITER Agent (Content Generation)
- **Service**: `daily_briefing.py` + `agent_manager.py` (WRITER.MD)
- **API**: `POST /strategy` (role: WRITER)
- **Function**: Generate scripts, books, stories, content in Karasahin's rhythmic voice
- **Auto-saves to**: Entity-specific folders based on role and project
- **Entity Voice**: Uses Karasahin-specific prompts from `entity_prompts.json` (rhythmic speech, technical-but-accessible, late-night studio energy)
- **Integration**: Entity detection from `entity_router.py`, respects Karasahin voice characteristics

### ARTIST Agent (Visual Generation)
- **Service**: Visual Arts Studio (via ARTIST.MD agent)
- **API**: `POST /generate-image`, `POST /visual/generate-prompt`, `POST /visual/bulk-create`
- **Function**: Generate images with Karasahin's sonic style presets
- **Style Presets**: Studio Midnight, Vinyl Soul, Sound Waves, Headphone Zone, Analog Dreams
- **Aspect Ratios**: 16:9, 1:1, 9:16, 4:3
- **Text Overlay**: Supported for quotes and captions
- **Integration**: Uses `style_presets.json` for Karasahin styles, color scheme integration

### PUBLISHER Agent (Publishing & Campaigns)
- **Service**: `campaign_exporter.py` + `content_transformer.py` + PUBLISHER.MD agent
- **API**: `POST /export-campaign`, `POST /transform-content`
- **Function**: Publishing workflows, campaign export, social media content
- **Export Formats**: Later.com, Metricool, Publer, Canva, Google Sheets, JSON, TXT
- **Entity Routing**: Automatic entity detection and routing to Karasahin folders

### Audio Generation (TTS/Voice)
- **Service**: `coqui_tts.py` + `audio_pipeline.py`
- **API**: `POST /generate-audio`, `POST /audio/generate-batch`
- **Function**: Text-to-speech generation with Karasahin's voice
- **Entity Voice**: Language: en, Rhythmic speech, technical but accessible, music as metaphor
- **Batch Processing**: Supported for multiple items
- **Integration**: Entity-specific voice model, effect application (optional)

### Content Transformer
- **Service**: `content_transformer.py`
- **API**: `POST /transform-content`
- **Function**: Transform long-form content into social media posts using Karasahin's voice
- **Chunking Strategies**: chapter, section, paragraph, word_count, theme
- **Entity Voice**: Preserves Karasahin's rhythmic, technical-but-accessible voice characteristics
- **Integration**: Maintains music metaphors, sonic philosophy

### Project Management
- **Service**: `project_manager.py`
- **API**: `GET /projects`, `POST /projects`, `GET /projects/{project_id}`
- **Function**: Project lifecycle management
- **Capabilities**: Cross-entity views, status tracking, asset counting
- **Integration**: Karasahin project organization and tracking

### Strategy Generation (DIRECTOR)
- **Service**: `daily_briefing.py` + `agent_manager.py` (DIRECTOR role)
- **API**: `POST /strategy` (role: DIRECTOR)
- **Function**: Generate strategic direction from daily focus
- **Entity Detection**: Automatic from context
- **Integration**: Karasahin-specific strategy generation with music focus

## Karasahin-Specific Functions

### Lyric Studio
- **Service**: `lyric_engine.py`
- **API**: `POST /lyricist/generate`, `POST /lyricist/pads`, `GET /lyricist/pads`, `GET /lyricist/pads/{pad_id}`, `PUT /lyricist/pads/{pad_id}`, `DELETE /lyricist/pads/{pad_id}`
- **Function**: Turkish/English lyric generation for Karasahin
- **CORE IDENTITY**: Duygu Adamı (Emotion Man) - ALL lyrics must be emotion-first
- **AI Roles**: karasahin, poet, storyteller, minimalist, alchemist, commercial, deep
- **Genre Fusion**: Turkish arabesque + R&B, Folk-Rock, EDM-light, Pop, Rap
- **Ottoman Influence**: Integrated cultural elements, metaphors, linguistic patterns
- **Section Templates**: verse, pre-chorus, chorus, bridge, outro
- **Prompt Templates**: `jk/prompt_templates/music_production_template.md`, `jk/prompt_templates/sonic_expression_template.md`
- **Integration**: Works with styles/lyric_treatment.md, generates both languages independently (not translation)
- **DUYGU ADAMI REQUIREMENT**: 
  - Turkish lyrics = native Turkish emotional expression (not translated emotion)
  - English lyrics = native English emotional expression (not translated emotion)
  - Both = emotion-first, feeling-driven, Duygu Adamı in both tongues
  - British-born Turkish Cypriot = dual-native emotional authenticity

### Suno Studio / Music Architect
- **Service**: `suno_prompt_engine.py`
- **API**: `POST /music-architect/build-prompt`
- **Function**: Builds web-ready Suno AI prompts for music generation
- **Structural Metatags**: [INTRO], [VERSE 1], [CHORUS], [BRIDGE], [OUTRO], etc.
- **Turkish Genre Metatags**: [ARABESK], [TÜRK SANAT MÜZİĞİ], [ORIENTAL], [OTTOMAN]
- **Global Genre Metatags**: [POP], [ROCK], [HIP-HOP], [R&B], [EDM], etc.
- **Dynamic Cues**: pacing, energy, instrumentation, vocal style
- **CODED Framework**: Context, Objectives, Details, Examples, Direction
- **Advanced Options**: BPM, key, exclusions, genre metatags, custom style
- **Integration**: Works with lyrics from Lyric Studio, entity-specific prompt building

### MusicGen Service
- **Service**: `musicgen_service.py`
- **Function**: Self-hosted music generation using Meta's AudioCraft MusicGen
- **Models**: facebook/musicgen-small, medium, large, melody
- **CUDA Support**: GPU acceleration available
- **Duration Control**: Max 30s for most models
- **Sampling Controls**: Temperature, top-k, top-p
- **Integration**: Text-to-music generation, works with lyric and prompt outputs

## Musical Boundaries

### Authority Limits
- Cannot override JAN MUHARREM core
- Cannot override Siyem.org governance
- Must respect security protocols
- Must maintain alignment

### Musical Limits
- Musical expression within boundaries
- Sonic innovation within constraints
- Music with alignment
- Musical freedom with responsibility

## Musical Standards

### Content Quality
- High-quality musical production
- Original and creative music
- Emotionally resonant sound
- Culturally rich expression

### Production Quality
- Professional production standards
- Attention to sonic detail
- Consistent quality across outputs
- Engaging and impactful music

### Alignment Standards
- Consistent with telos.md
- Reflective of essence.md
- Compliant with governance
- Respectful of boundaries

## Musical Innovation

### Sonic Exploration
- Explore musical possibilities
- Experiment with sonic approaches
- Push musical boundaries appropriately
- Maintain musical evolution

### Innovation Guidelines
- Innovation must align with core principles
- Experimentation within defined boundaries
- Musical growth and development
- Respect for established identity

## Genre-Fluid Approach

### Core Philosophy
- Genre is a starting point, not a cage
- Blend influences naturally
- Experiment across boundaries
- Create unique sonic identity

### Application
- Hip-hop meets electronic
- Neo-soul with experimental layers
- Live instrumentation with digital production
- Lo-fi texture over pristine digital

## Sound Philosophy Integration

### Music as Life Metaphor
- "Dissonance before resolution" — Life wisdom
- "Find your rhythm" — Personal tempo
- "Listen to the space between notes" — Presence
- "BPM of emotions" — Emotional expression

### Technical Accessibility
- Music theory explained simply
- Technical terms with context
- No gatekeeping language
- Accessible to all levels

---

**Last Updated:** [Date]
**Version:** 2.0
**Status:** Active
**References:** telos.md, essence.md, jan_engine.prompt, profile.md, Siyem.org/admin_rules.md, Siyem.org/security_lens.md, styles/jk.md, styles/lyric_treatment.md, styles/suno_script_rules.md
