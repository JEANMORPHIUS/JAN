---
type: governance_rule
category: access_control_rules
last_updated: 2026-01-18
format: programmatic
---

# Programmatic Access Control Rules

**Purpose:** Define programmatic access control rules for API governance
**Foundation:** Law 37 - "Protect the System" requires access control
**Companion to:** `access_control.md` (human-readable security protocols)

**Format:** `allow|deny user action entity`

---

## Rules

### System Rules (Highest Priority)
allow system * *

### Admin Rules
allow admin admin *
allow admin backroom *
allow admin publish *
allow admin entity *
allow admin database *
allow admin content *

### Backroom Rules (Infrastructure - CRITICAL)
deny * backroom *
allow admin backroom *

### Seed Rules (Shell/Seed Separation - CRITICAL)
deny * seed *
allow admin seed *
allow seed_editor seed *

### Entity-Specific Publishing Rules
allow jean publish jean_mahram
allow karasahin publish jk
allow ramiz publish uncle_ray_ramiz
allow pierre publish pierre_pressure
allow siyem publish siyem_media

### Entity-Specific Entity Rules
allow jean entity jean_mahram
allow karasahin entity jk
allow ramiz entity uncle_ray_ramiz
allow pierre entity pierre_pressure
allow siyem entity siyem_media

### Content Operations Rules
allow content_creator content *
allow admin content *
allow publisher publish *
allow editor content *

### Database Operations Rules
deny * database *
allow admin database *
allow system database *

---

## Action Definitions

| Action | Description | Examples |
|--------|-------------|----------|
| `admin` | Administrative operations | Sync database, configure system |
| `backroom` | Infrastructure operations | Restart services, modify infrastructure |
| `seed` | Seed content access | Read/edit/publish Seed content |
| `publish` | Publish content | Publish to social media, websites |
| `entity` | Entity operations | Edit entity profiles, manage entity content |
| `database` | Database operations | Sync entity database, query data |
| `content` | Content operations | Create, edit, delete content |
| `*` | Wildcard (all actions) | Matches any action |

---

## Entity Definitions

| Entity | SIYEM Format | Description |
|--------|--------------|-------------|
| Jean | `jean_mahram` | The Storyteller |
| Karasahin | `jk` | The Sound Architect / Voice of God |
| Ramiz | `uncle_ray_ramiz` | The Elder / Teacher |
| Pierre | `pierre_pressure` | The Disciplinarian |
| Siyem | `siyem_media` | The Observer / System Coordinator |
| Backroom | `backroom` | Infrastructure / System Foundation |
| `*` | Wildcard | Matches any entity |

---

## Rule Hierarchy

**Priority Order:**
1. **Explicit DENY** - If any rule denies access, access is denied
2. **Explicit ALLOW** - If a rule allows access and no rule denies, access is allowed
3. **Default DENY** - If no rule matches, access is denied (fail secure)

---

**Status:** ACTIVE
**Last Updated:** 2026-01-18
**Law Applied:** Law 37 - Protect the System
