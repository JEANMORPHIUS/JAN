# Oracle Mechanics

**Deep dive into how the Oracle SIYEM system works: RNG, hexagram mapping, and Law interpretation.**

---

## Overview

The Oracle SIYEM system uses **transparent randomness** to guide creative decisions through the 40 Laws of Racon. Unlike gambling algorithms (opaque, exploitative), this system is:

- **Fully Transparent**: User sees every step
- **Deterministic**: Same inputs = same result
- **Verifiable**: User can verify the process
- **User-Serving**: Generates value, not extracts it

---

## The Process: Step by Step

### Step 1: Seed Generation

**Input:**
- `user_intent`: User's creative question/challenge
- `timestamp`: Current timestamp (ISO format)
- `context`: Optional creative context
- `user_id`: Optional user identifier

**Process:**
```python
seed_string = f"{user_intent}:{timestamp}:{context}:{user_id}"
seed_hash = SHA-256(seed_string)
```

**Output:**
```json
{
  "seed": "a1b2c3d4e5f6...",  // 64-character hex hash
  "components": {
    "user_intent": "...",
    "timestamp": "2026-01-28T10:00:00",
    "context": "...",
    "user_id": "user123"
  },
  "method": "SHA-256 hash of concatenated components",
  "verifiable": true
}
```

**Why Transparent?**
- User can recreate the seed from components
- SHA-256 is a standard, verifiable algorithm
- No hidden randomness or manipulation

---

### Step 2: Hexagram Calculation

**Input:** Seed hash (64 hex characters)

**Process:**
```python
# Use first 16 hex characters (64 bits of entropy)
seed_int = int(seed[:16], 16)  # Convert hex to integer
hexagram = seed_int % 64  # Map to 0-63 range
hexagram_binary = format(hexagram, '06b')  # 6-bit binary
```

**Output:**
```json
{
  "hexagram_number": 42,  // 0-63
  "hexagram_binary": "101010",  // 6-bit binary
  "method": "First 16 hex chars → integer → mod 64 → 6-bit binary",
  "transparent": true
}
```

**Why I Ching Format?**
- 64 hexagrams = 2^6 (6-bit binary)
- Each hexagram represents a state/pattern
- Maps naturally to 40 Laws (see next step)

**Verification:**
User can verify by:
1. Taking first 16 hex chars of seed
2. Converting to integer
3. Taking modulo 64
4. Converting to 6-bit binary

---

### Step 3: Law Mapping

**Input:** Hexagram number (0-63)

**Process:**
```python
law_number = (hexagram % 40) + 1  # Maps to 1-40
```

**Output:**
```json
{
  "law_number": 2,  // 1-40
  "law_title": "Your Word Is Your Bond",
  "law_text": "Creative commitments are laws, not suggestions...",
  "volume": "Loyalty",  // Laws 1-10
  "category": "Commitment"
}
```

**The 40 Laws:**
- **Volume 1: Loyalty (Laws 1-10)**: The table, bread and salt, bonds
- **Volume 2: Silence (Laws 11-20)**: Wisdom lives in the quiet
- **Volume 3: Respect (Laws 21-30)**: Honor your elders, know your place
- **Volume 4: War (Laws 31-40)**: Finish what you begin, protect what is yours

**Why This Mapping?**
- 64 hexagrams → 40 Laws (modulo operation)
- Ensures all Laws can be selected
- Deterministic and verifiable

---

### Step 4: Law Interpretation

**Input:**
- Law data (number, title, text, volume)
- User intent
- Creative context

**Process:**
1. **Extract Law Wisdom**: Law text and principles
2. **Apply to Context**: How Law relates to user intent
3. **Generate Guidance**: Actionable creative prompt

**Output:**
```json
{
  "interpretation": "Law 2: Your Word Is Your Bond...",
  "creative_prompt": "Apply Your Word Is Your Bond to your creative work...",
  "law_data": { ... }
}
```

**Interpretation Principles:**
- **Context-Specific**: Tailored to user intent
- **Actionable**: Provides clear next steps
- **Respectful**: Honors Law principles
- **Creative**: Encourages innovation within Law framework

---

## Transparency & Verification

### Full Transparency Data

Every Oracle cast includes complete transparency:

```json
{
  "transparency": {
    "seed": {
      "seed": "a1b2c3d4...",
      "components": { ... },
      "method": "SHA-256 hash...",
      "verifiable": true
    },
    "hexagram": {
      "hexagram_number": 42,
      "hexagram_binary": "101010",
      "method": "First 16 hex chars → integer → mod 64 → 6-bit binary",
      "transparent": true
    },
    "law_mapping": {
      "hexagram": 42,
      "law_number": 2,
      "method": "hexagram % 40 + 1"
    },
    "verifiable": true,
    "user_can_verify": "User can recreate seed from components and verify hexagram calculation"
  }
}
```

### How to Verify

**Verify Seed:**
```python
import hashlib

components = {
    "user_intent": "test",
    "timestamp": "2026-01-28T10:00:00",
    "context": "",
    "user_id": "public"
}
seed_string = f"{components['user_intent']}:{components['timestamp']}:{components['context']}:{components['user_id']}"
seed_hash = hashlib.sha256(seed_string.encode('utf-8')).hexdigest()
# Should match Oracle result
```

**Verify Hexagram:**
```python
seed = "a1b2c3d4e5f6..."  # From Oracle result
seed_int = int(seed[:16], 16)
hexagram = seed_int % 64
hexagram_binary = format(hexagram, '06b')
# Should match Oracle result
```

**Verify Law:**
```python
hexagram = 42  # From Oracle result
law_number = (hexagram % 40) + 1
# Should match Oracle result
```

---

## Anti-Addiction Design

### Success Metrics

**Traditional Platform Metrics:**
- Time on platform (higher = better)
- Clicks, views, engagement (higher = better)
- User retention (higher = better)

**Oracle SIYEM Metrics (Inverted):**
- **Creative Outputs**: Number of things created (higher = better)
- **Time Creating**: Minutes spent creating (not consuming)
- **Success Score**: `(creative_outputs / cast_count) * (1 / (1 + time_on_platform/60))`

**Success = User creates and LEAVES**

### Ethical Guardrails

**After 3 casts:**
- Break prompt suggested
- Encourages reflection

**After 5 casts:**
- Reflection prompt
- Time to contemplate patterns

**After 10 casts:**
- Execution nudge
- "The Oracle has spoken. Now CREATE."

**Healthy Practice:**
- More creative outputs than casts = success
- Taking breaks = healthy
- Creating and leaving = goal

---

## Deterministic Behavior

### Same Inputs = Same Result

If you cast Oracle with the same inputs at different times, you'll get different results (because timestamp changes). But if you recreate the exact same seed components, you'll get the same result.

**Example:**
```python
# Cast 1
seed1 = generate_seed("test", "2026-01-28T10:00:00", "", "user1")

# Cast 2 (same components)
seed2 = generate_seed("test", "2026-01-28T10:00:00", "", "user1")

# seed1 == seed2 (deterministic)
```

**Why This Matters:**
- User can verify the process
- No hidden randomness
- Transparent and trustworthy

---

## Comparison: Gambling RNG vs. Oracle SIYEM

| Aspect | Gambling RNG | Oracle SIYEM |
|--------|-------------|--------------|
| **Transparency** | Opaque, hidden | Fully transparent |
| **Verification** | Cannot verify | User can verify |
| **Purpose** | Extract value | Generate value |
| **Metrics** | Engagement time | Creative outputs |
| **Success** | User stays | User creates and leaves |
| **Addiction** | Encourages | Prevents |

---

## Mathematical Properties

### Entropy

- **Seed**: 256 bits (SHA-256)
- **Hexagram**: 6 bits (64 possibilities)
- **Law**: 6 bits (40 possibilities, modulo mapping)

### Distribution

- **Hexagrams**: Uniform distribution (0-63)
- **Laws**: Uniform distribution (1-40)
- **No Bias**: Each Law equally likely

### Collision Resistance

- **SHA-256**: Cryptographically secure
- **Collision Probability**: Negligible
- **Deterministic**: Same seed = same result

---

## Use Cases

### Creative Guidance

Cast Oracle when you need:
- Story structure guidance
- Character development direction
- Plot decision making
- Creative block resolution

### Decision Making

Use Oracle for:
- Strategic choices
- Project prioritization
- Resource allocation
- Direction setting

### Learning

Study how:
- Laws apply to different contexts
- Patterns emerge across casts
- Wisdom guides creative work
- Transparency builds trust

---

## Best Practices

1. **Cast with Clear Intent**: Specific questions get better guidance
2. **Record Your Outputs**: Track what you create
3. **Take Breaks**: Honor the guardrails
4. **Verify When Curious**: Check the transparency data
5. **Apply the Laws**: Use guidance to create, then execute

---

## Technical Implementation

### Code Location

- **Service**: `SIYEM/services/oracle_siyem_integration.py`
- **API**: `jan-studio/backend/oracle_siyem_api.py`
- **Database**: `SIYEM/data/oracle_siyem.db`

### Key Classes

- `TransparentRNG`: Seed generation and hexagram calculation
- `LawsInterpreter`: Law mapping and interpretation
- `AntiAddictionMetrics`: Success metrics and guardrails
- `OracleSIYEM`: Main orchestrator

---

**PANGEA IS THE TABLE.**
**YOU DON'T BETRAY THE TABLE.**

**The Oracle speaks through transparency.**
**The Laws guide through wisdom.**
**Success is measured by creation, not consumption.**
