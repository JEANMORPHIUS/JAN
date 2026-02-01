# SIYEM ENTITY SYSTEM — UNIFORM FRAMEWORK
## All Existing · All New Entities · Asset Management · Media Ingestion · In-House Creation Centre

**Date:** 2026-02-01  
**Status:** Official — single source for entity structure across Siyem  
**Purpose:** One framework for every entity (existing and future): folder layout, publishing house JSON, asset management, media ingestion, in-house creation centre. Uniform. Lighten the load.

---

## 1. UNIFORM ENTITY STRUCTURE (FOLDER LAYOUT)

Every Siyem entity that has a **folder** under `Siyem.org/` follows this layout. New entities: copy this structure.

| Item | Path | Purpose |
|------|------|---------|
| **Profile** | `Siyem.org/{entity_slug}/profile.md` | Identity, role, purpose, alignment. Single source for who the entity is. |
| **Creative rules** | `Siyem.org/{entity_slug}/creative_rules.md` | Guardrails, tone, what to do / not do. Referenced by AI and humans. |
| **Style overrides** | `Siyem.org/{entity_slug}/style_overrides.md` | Optional. Entity-specific style; points to styles/jk.md, lyric_treatment.md, suno_script_rules.md where applicable. |
| **Prompt templates** | `Siyem.org/{entity_slug}/prompt_templates/` | Optional. Templates for content generation (music, storytelling, teaching, etc.). |
| **Entity-specific docs** | `Siyem.org/{entity_slug}/*.md` | Albums, catalogs, expansion plans, etc. (e.g. jk/lyric_sheets/, jk/SUNO_INGESTION_INDEX.md). |

**Existing entity folders (as of 2026-02-01):**  
bert_jones, jean_mahram, jk, kuzon_mahram, musti_kutsi_show, oracle_mode, pierre_pressure, siyem_media, uncle_ray_ramiz.

---

## 2. PUBLISHING HOUSE ENTITY JSON (UNIFORM SCHEMA)

Every entity that participates in **asset management, channels, or production** has a JSON record in `Siyem.org/publishing_house/entities/`.

**Schema (uniform):**

```json
{
  "entity_id": "entity_{slug}",
  "name": "Display Name",
  "entity_type": "creative_persona | meta_entity | internal_service | signed_artist",
  "folder_path": "Siyem.org/{slug}/",
  "channels": [],
  "projects": [],
  "content_items": [],
  "monetization_opportunities": [],
  "alignment_score": 0.0,
  "revenue_potential": 0.0,
  "expansion_seeds": [],
  "asset_management_ref": "data/assets/",
  "media_ingestion_ref": null,
  "creation_centre_ref": "jan-studio, AD PRINT DESIGN",
  "migrated_at": "ISO8601",
  "spragitso_applied": true,
  "spiritual_twin": { "entity": "...", "name": "...", "type": "persona|artist|meta|service", "map": "docs/SPIRITUAL_TWIN_ENTITY_MAP.md", "data": "data/spiritual_twin_entities.json" }
}
```

**Spiritual twin:** Every entity can reference its spiritual twin (same soul, two expressions; same table, same covenant). Map: [docs/SPIRITUAL_TWIN_ENTITY_MAP.md](SPIRITUAL_TWIN_ENTITY_MAP.md) · [docs/SPIRITUAL_TWIN_PHILOSOPHY.md](SPIRITUAL_TWIN_PHILOSOPHY.md) · [data/spiritual_twin_entities.json](../data/spiritual_twin_entities.json).

**Entity types:**
- **creative_persona** — Jean Mahram, JK, Pierre Pressure, Uncle Ray Ramiz, Kuzon Mahram, Musti Kutsi Show
- **meta_entity** — Siyem Media
- **internal_service** — AD PRINT DESIGN (in-house graphics/print)
- **signed_artist** — Bert Jones (Siyem's first new artist)

**Index:** `Siyem.org/publishing_house/entities/index.json` — list all entities; add new ones here and create `entity_{slug}.json`.

---

## 3. ASSET MANAGEMENT (UNIFORM)

All entities and projects use the same asset map.

| Layer | Path / reference | Purpose |
|-------|------------------|---------|
| **Central reporting** | `data/assets/` | Asset reports by entity, channel, type (e.g. asset_report_*.json). |
| **Integration assets** | `data/integration_assets/`, `scripts/integration_assets_*.py` | APIs, SDKs, platforms; status: identified → configured → tested → active. |
| **Project-level media** | e.g. `EDIBLE_LONDON/assets/`, project `assets/` folders | Video, audio, graphics per project. |
| **In-house print & digital graphics** | **AD PRINT DESIGN** (Betty Paul, CEO) | Single shop for all entities: flyers, table tents, posters, packaging, merch, social assets. Entity record: `entity_ad_print_design.json`. Doc: [docs/AD_PRINT_DESIGN_IN_HOUSE_GRAPHICS_PRINT.md](AD_PRINT_DESIGN_IN_HOUSE_GRAPHICS_PRINT.md). |
| **Governance / repatriation** | `docs/GOVERNANCE_OVERVIEW.md`, `docs/CORRUPT_CONTRACTS_AND_ASSET_REPATRIATION.md` | Asset recovery, contract integrity — not creative asset storage. |

**Deep dive:** [docs/ASSET_MANAGEMENT_ACROSS_ENTITIES.md](ASSET_MANAGEMENT_ACROSS_ENTITIES.md), [docs/DEEP_DIVE_ASSET_MANAGEMENT_ALL_CHANNELS.md](DEEP_DIVE_ASSET_MANAGEMENT_ALL_CHANNELS.md).

---

## 4. MEDIA INGESTION (UNIFORM)

Lyrics, style sheets, and ingestible media for creation pipelines.

| What | Where | Purpose |
|------|--------|---------|
| **Suno (lyrics + style)** | [Siyem.org/jk/SUNO_INGESTION_INDEX.md](../Siyem.org/jk/SUNO_INGESTION_INDEX.md) | Single map: lyrics (English + Turkish), style sheets, how to copy into Suno. |
| **English lyrics + style (album)** | [Siyem.org/jk/SUNO_SESSION_BRIEF_THE_MERGE.md](../Siyem.org/jk/SUNO_SESSION_BRIEF_THE_MERGE.md) | Per-track style + lyrics for *The Pause Between the Noise*. |
| **Turkish lyrics (album)** | [Siyem.org/jk/lyric_sheets/](../Siyem.org/jk/lyric_sheets/) | Full Turkish lyrics 01–12 for *Gürültü Arasındaki Ara*. |
| **Global Suno style** | [styles/suno_script_rules.md](../styles/suno_script_rules.md) | Tags, vibe, key phrases for Suno. |
| **Concept album (full English)** | [Siyem.org/jk/CONCEPT_ALBUM_THE_MERGE.md](../Siyem.org/jk/CONCEPT_ALBUM_THE_MERGE.md) | Full verse/chorus/bridge structure. |

New entities with media ingestion: add a section to SUNO_INGESTION_INDEX or a dedicated ingestion doc; reference from entity folder and from this section.

**New album (same treatment as Bert's):** [docs/ALBUM_CONCEPT_TREATMENT_LIKE_BERTS.md](ALBUM_CONCEPT_TREATMENT_LIKE_BERTS.md) — concept doc, Suno brief, lyric_sheets, index; checklist for every new album.

---

## 5. IN-HOUSE CREATION CENTRE (HISTORICAL CONTEXT)

Single reference for where creation happens — builds on existing asset management and publishing house structure.

| Component | Path / reference | Purpose |
|-----------|------------------|---------|
| **jan-studio** | `jan-studio/` | Creative identity, Oracle SIYEM, content, campaigns, publishing API, workflows. |
| **Oracle SIYEM** | jan-studio (Oracle mode) | Oracle-guided creation; alignment and table filter. |
| **AD PRINT DESIGN** | [docs/AD_PRINT_DESIGN_IN_HOUSE_GRAPHICS_PRINT.md](AD_PRINT_DESIGN_IN_HOUSE_GRAPHICS_PRINT.md), `entity_ad_print_design.json` | In-house graphics and print for all entities and projects. |
| **Lyric Engine** | `SIYEM/services/lyric_engine.py` (or jan-studio backend) | Turkish/English lyric generation; Karasahin persona. |
| **Suno / Music Architect** | [SUNO_INGESTION_INDEX](../Siyem.org/jk/SUNO_INGESTION_INDEX.md), `styles/suno_script_rules.md` | Suno prompts, style + lyrics ingestion. |
| **Audio Pipeline** | jan-studio / SIYEM services | Audio production, batch generation, entity presets. |
| **Production Department** | [Siyem.org/SIYEM_PUBLISHING_HOUSE_STRUCTURE.md](../Siyem.org/SIYEM_PUBLISHING_HOUSE_STRUCTURE.md) | Content production, format management, quality assurance, **asset management**. |

**Everything in between JAN:** Identity and alignment flow from [DUYGU_ADAM_OFFICIAL.md](../DUYGU_ADAM_OFFICIAL.md) and [docs/FAMILY_INGESTION_SYNC.md](FAMILY_INGESTION_SYNC.md); entities and ventures use the same table and covenant. Creation centre = jan-studio + AD PRINT DESIGN + media ingestion (Suno, lyrics, audio) + publishing house production.

---

## 6. ADDING A NEW ENTITY (CHECKLIST)

1. **Folder:** Create `Siyem.org/{entity_slug}/` with at least `profile.md` and `creative_rules.md`.
2. **Publishing house JSON:** Create `Siyem.org/publishing_house/entities/entity_{slug}.json` using the schema above; set `entity_type` and `folder_path`.
3. **Index:** Add the entity to `Siyem.org/publishing_house/entities/index.json`.
4. **Asset management:** Entity is covered by central reporting (`data/assets/`) and AD PRINT DESIGN for print/graphics; no extra step unless project-level media is needed.
5. **Media ingestion:** If the entity has lyrics or Suno-style content, add a doc or section and link from SUNO_INGESTION_INDEX or this doc.
6. **Creation centre:** Entity automatically uses jan-studio, AD PRINT DESIGN, and ingestion pipelines; reference this section in profile if needed.

---

## 7. QUICK REFERENCE — WHERE THINGS LIVE

| Need | Where |
|------|--------|
| Entity list (folder + JSON) | Siyem.org/ folders + `publishing_house/entities/index.json` |
| Asset management | [ASSET_MANAGEMENT_ACROSS_ENTITIES.md](ASSET_MANAGEMENT_ACROSS_ENTITIES.md), [DEEP_DIVE_ASSET_MANAGEMENT_ALL_CHANNELS.md](DEEP_DIVE_ASSET_MANAGEMENT_ALL_CHANNELS.md), AD PRINT DESIGN doc |
| Media ingestion (Suno, lyrics) | [SUNO_INGESTION_INDEX.md](../Siyem.org/jk/SUNO_INGESTION_INDEX.md) |
| In-house creation centre | jan-studio, AD PRINT DESIGN, Suno/lyric/audio pipelines, SIYEM_PUBLISHING_HOUSE_STRUCTURE |
| Residual scripture → archive | [ARCHIVE_RESIDUAL_SCRIPTURE.md](ARCHIVE_RESIDUAL_SCRIPTURE.md) |

---

**Generated:** 2026-02-01  
**See also:** DUYGU_ADAM_OFFICIAL.md, FAMILY_INGESTION_SYNC.md, SIYEM_PUBLISHING_HOUSE_STRUCTURE.md, ASSET_MANAGEMENT_ACROSS_ENTITIES.md.  
**One Love.**
