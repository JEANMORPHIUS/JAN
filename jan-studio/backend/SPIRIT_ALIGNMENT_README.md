# SPIRIT ALIGNMENT - Multi-Dimensional Alignment System

## Overview

The Spirit Alignment system ensures that spiritual battles can only occur when spirits align on **ALL dimensions**. This is sacred alignment - not mechanical matching.

## Core Principle

**"SPIRITS MUST ALIGN ON ALL DIMENSIONS"**

Before any spiritual battle can occur, spirits must align on:
1. **Age Range** - Compatibility in age/soul maturity
2. **Animal Type** - Compatibility in spirit animal/totem
3. **Gender Alignment** - Compatibility in gender/spiritual gender
4. **Spiritual Alignment** - Compatibility in vibration, mission, purpose

## Dimensions

### Age Range
- **ANCIENT**: Very old souls, legacy wisdom
- **MATURE**: Experienced souls, established paths
- **YOUNG**: Growing souls, active development
- **NEWBORN**: New souls, fresh beginnings

### Animal Type
Spirit animals that resonate with each other:
- **Predators**: Wolf, Lion, Tiger, Eagle, Shark
- **Wisdom Keepers**: Owl, Raven, Whale, Elephant
- **Transformers**: Snake, Dragon, Phoenix
- **Gentle Spirits**: Deer, Unicorn, Dolphin
- **Companions**: Dog, Cat, Horse

### Gender Alignment
- **MASCULINE**: Yang energy, action, structure
- **FEMININE**: Yin energy, receptivity, flow
- **BALANCED**: Both energies in harmony
- **FLUID**: Dynamic, adaptable, transformative
- **NEUTRAL**: Beyond binary, pure spirit

### Spiritual Alignment
- **ALIGNED**: Fully aligned with mission, purpose, vibration
- **CALIBRATING**: In process of alignment
- **MISALIGNED**: Not aligned, needs healing
- **TRANSFORMING**: In transformation, becoming aligned

## Usage

### Creating a Spirit

```python
from spirit_alignment import create_spirit_from_user_data, Spirit

# From user data
user_data = {
    "age_range": "mature",
    "animal_type": "wolf",
    "gender_alignment": "balanced",
    "activity_level": "high",
    "wisdom_level": "medium"
}

vibration_result = {
    "vibration_aligned": True,
    "galaxy_form": "spiral",
    "mission_aligned": True,
    "table_ready": True
}

spirit = create_spirit_from_user_data("spirit_001", user_data, vibration_result)
```

### Checking Battle Compatibility

```python
from spirit_alignment import SpiritAlignmentChecker

checker = SpiritAlignmentChecker()

# Check if two spirits can battle
can_battle, reason, details = checker.can_engage_in_battle(spirit1, spirit2)

if can_battle:
    battle_type = checker.determine_battle_type(spirit1, spirit2)
    print(f"Battle permitted: {battle_type}")
else:
    print(f"Battle not permitted: {reason}")
    print(f"Misalignments: {details['misalignment_reasons']}")
```

### Using with Connection Ritual

```python
from connection_ritual import ConnectionRitual

ritual = ConnectionRitual()

# Perform connection ritual (automatically creates Spirit object)
result = ritual.perform_connection_ritual(user_id, user_data)

# Check battle compatibility with another spirit
spirit1 = create_spirit_from_user_data(user_id, user_data, result['vibration_result'])
spirit2 = create_spirit_from_user_data(other_user_id, other_user_data, other_result['vibration_result'])

compatibility = ritual.check_spirit_battle_compatibility(spirit1, spirit2)
```

## API Endpoints

### POST `/api/check-battle-compatibility`

Check if two spirits can engage in a spiritual battle.

**Request:**
```json
{
  "spirit1_id": "user_001",
  "spirit1_data": {
    "age_range": "mature",
    "animal_type": "wolf",
    "gender_alignment": "balanced"
  },
  "spirit2_id": "user_002",
  "spirit2_data": {
    "age_range": "mature",
    "animal_type": "lion",
    "gender_alignment": "balanced"
  }
}
```

**Response:**
```json
{
  "status": "success",
  "compatibility": {
    "can_battle": true,
    "reason": "All dimensions aligned - battle permitted",
    "alignment_details": {
      "age_aligned": true,
      "animal_aligned": true,
      "gender_aligned": true,
      "spiritual_aligned": true,
      "all_dimensions_aligned": true
    },
    "battle_type": "active"
  }
}
```

## Philosophy

This system honors the sacred nature of spiritual battles. Battles are not random encounters - they require complete alignment across all dimensions of spirit. This ensures that battles serve the mission: **"THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"**.

**Energy + Love = We All Win**

Only when spirits align on all dimensions can they engage in battles that serve the greater good, honor the Table (Law 1), and contribute to the New World formation.
