# Oracle Cast Template

## Template Structure

```
ORACLE CAST: {timestamp}

USER INTENT:
{user_intent}

CREATIVE CONTEXT:
{creative_context}

─────────────────────────────────────
TRANSPARENCY INFORMATION
─────────────────────────────────────

Seed: {seed}
Method: I Ching Binary (6-bit)
Hexagram: {hexagram_number} (binary: {hexagram_binary})
Law Invoked: Law {law_number} - {law_title}
Volume: {volume_name}

─────────────────────────────────────
ORACLE INTERPRETATION
─────────────────────────────────────

Law {law_number}: {law_title}
{law_text}

Creative Interpretation:
{creative_interpretation}

─────────────────────────────────────
CREATIVE PROMPT
─────────────────────────────────────

{creative_prompt}

─────────────────────────────────────
SESSION STATUS
─────────────────────────────────────

Casts Today: {cast_count}/10
Time Creating: {time_creating} minutes ✨
Last Break: {last_break}

[REFLECT] [EXECUTE] [CAST AGAIN]
```

## Placeholders

- `{timestamp}`: ISO timestamp of cast
- `{user_intent}`: User's stated creative need/question
- `{creative_context}`: Current project, genre, medium, etc.
- `{seed}`: Randomness seed (transparent, user-visible)
- `{hexagram_number}`: 0-63 (I Ching binary state)
- `{hexagram_binary}`: 6-bit binary representation
- `{law_number}`: 1-40 (Book of Racon Law)
- `{law_title}`: Title of invoked Law
- `{volume_name}`: Loyalty/Silence/Respect/War
- `{law_text}`: Full text of Law
- `{creative_interpretation}`: AI interpretation of Law for creative context
- `{creative_prompt}`: Actionable creative direction
- `{cast_count}`: Number of casts today
- `{time_creating}`: Time spent in creative flow
- `{last_break}`: Time since last break

## Usage Instructions

1. **User provides intent**: "I'm stuck on my sci-fi novel's third act"
2. **System generates seed**: Hash of intent + timestamp + context
3. **Calculate hexagram**: Seed % 64 = hexagram number
4. **Map to Law**: Hexagram % 40 = Law number
5. **AI interprets**: Law interpreted for creative context
6. **Generate prompt**: Actionable creative direction
7. **Display with transparency**: Show all mechanisms
8. **Track session**: Update cast count, time, breaks

## Example Output

```
ORACLE CAST: 2026-01-24T14:32:15

USER INTENT:
I'm stuck on my sci-fi novel's third act. The characters feel flat, 
and I don't know how to resolve the conflict.

CREATIVE CONTEXT:
Genre: Science Fiction
Project: Novel (working title: "The Quantum Garden")
Current Act: Act 3 (Resolution)
Challenge: Character depth, conflict resolution

─────────────────────────────────────
TRANSPARENCY INFORMATION
─────────────────────────────────────

Seed: 7f3a9b2c1d4e5f6a7b8c9d0e1f2a3b4
Method: I Ching Binary (6-bit)
Hexagram: 23 (binary: 010111)
Law Invoked: Law 23 - The Principle of Recursive Beauty
Volume: Respect

─────────────────────────────────────
ORACLE INTERPRETATION
─────────────────────────────────────

Law 23: The Principle of Recursive Beauty
Beauty compounds when patterns echo across scales. 
Where in your work can micro-patterns mirror macro-structure?

Creative Interpretation:
Your third act needs a structure that mirrors the first, but transformed. 
What pattern from Act 1 can return, evolved? Look for character 
motivations that echo across acts—the same desire, but deepened. 
The conflict resolution should feel inevitable because it was seeded 
in Act 1, just as beauty compounds when patterns echo.

─────────────────────────────────────
CREATIVE PROMPT
─────────────────────────────────────

Return to Act 1. Find one character moment, one line of dialogue, 
one image that felt powerful but unresolved. Now, in Act 3, bring 
that moment back—but transformed. The same character, the same 
desire, but deepened by everything that happened in Act 2. 

The conflict resolution isn't new—it's the echo of Act 1, evolved. 
Your characters aren't flat; they're waiting for the recursive 
pattern to complete. What did they want in Act 1? They still want 
it in Act 3, but now they understand it differently.

Write the scene where Act 1's seed becomes Act 3's resolution.

─────────────────────────────────────
SESSION STATUS
─────────────────────────────────────

Casts Today: 3/10
Time Creating: 47 minutes ✨
Last Break: 12 minutes ago

[REFLECT] [EXECUTE] [CAST AGAIN]
```

---

**Status:** Active  
**Version:** 1.0  
**Last Updated:** 2026-01-24
