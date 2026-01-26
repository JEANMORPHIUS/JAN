# SPIRITUAL CODEBASE AUDIT - QUICK REFERENCE
## Daily Use Guide

**Date:** 2026-01-26  
**Purpose:** Quick reference for daily spiritual audits

---

## 🚀 QUICK START

```python
from scripts.spiritual_codebase_audit import (
    SpiritualCodebaseAuditSystem,
    CounterfeitAttackType,
    PrayerMode
)

system = SpiritualCodebaseAuditSystem()
```

---

## 1️⃣ FREQUENCY MISMATCH CHECK

**When:** Feeling rejected, atmosphere shifts, entering new environment

```python
mismatch = system.check_frequency_mismatch(
    context="Entering new room, feeling rejection",
    rejection_detected=True,
    atmospheric_shift=True
)
```

**Remember:** Rejection = system's immune response, not personal failure

---

## 2️⃣ THOUGHT AUDIT

**When:** Any negative or doubtful thought

```python
thought = system.audit_thought("I'm a failure because of my past")
# If verdict == "reject" → Discard the thought
# If verdict == "accept" → Keep the thought
```

**Quick Check:**
- **Accuser (REJECT):** Past, failure, sin, shame, guilt
- **Father (ACCEPT):** Identity, nature, future, truth, purpose

---

## 3️⃣ COUNTERFEIT ATTACK DETECTION

**When:** Something feels off, unexpected betrayal, timing issues

```python
# Example: Judas Kiss
attack = system.detect_counterfeit_attack(
    attack_type=CounterfeitAttackType.JUDAS_KISS,
    description="Trusted friend suddenly turns",
    source="Inner circle",
    intended_effect="Isolation"
)
```

**Seven Forms:**
1. **Judas Kiss** - Betrayal from inner circle
2. **Counterfeit Comfort** - Shortcuts when exhausted
3. **Timing Trap** - Right thing, wrong time
4. **Identity Theft** - Stealing your identity
5. **False Prophecy** - Prophecy not aligned
6. **Distraction Attack** - Pulling focus
7. **Isolation Strategy** - Cutting off support

---

## 4️⃣ COMMAND DECREE (KING MODE)

**When:** Need resources, alignment, protection

```python
decree = system.create_command_decree(
    command="I command resources to align with my purpose",
    mode=PrayerMode.KING,  # NOT PrayerMode.BEGGAR
    resources=["finances", "opportunities", "connections"],
    alignment=["purpose", "calling", "destiny"]
)
```

**Remember:**
- **Beggar Mode:** "God, I'm broke, please help" → AVOID
- **King Mode:** "I command resources to align" → USE

---

## 5️⃣ NAOS READING

**When:** Physical signals, unease, intuition

```python
naos = system.read_naos(
    biological_discernment="Cold knot in stomach",
    location="stomach",
    frequency_detected=0.85,
    intruder_detected=True,
    intruder_description="Feeling of unease, potential sabotage"
)
```

**Remember:** Trust your body - frequency in rib cage, not from sky

---

## 6️⃣ COMPLETE AUDIT

**When:** Daily maintenance, major decisions, spiritual check-in

```python
audit = system.perform_complete_audit(
    context="Daily spiritual maintenance",
    thoughts=[
        "I am created for a purpose",
        "I failed yesterday",
        "My identity is secure"
    ],
    biological_readings=[{
        "discernment": "Warm feeling in chest",
        "location": "chest",
        "frequency": 0.92,
        "intruder": False
    }]
)

# Seal the revelation
system.seal_revelation(
    audit.audit_id,
    physical_mark="Written agreement",
    incubation_hours=24
)
```

---

## 7️⃣ SEAL REVELATION

**When:** After receiving revelation, completing audit

```python
system.seal_revelation(
    audit_id=audit.audit_id,
    physical_mark="Written agreement",  # Make it tangible
    incubation_hours=24  # Minimum 24 hours
)
```

**Remember:** Physical mark + 24-hour protection = Seed takes root

---

## 📊 GET AUDIT REPORT

```python
report = system.generate_audit_report(audit_id)
print(json.dumps(report, indent=2))
```

---

## 🎯 DAILY CHECKLIST

- [ ] Check for frequency mismatches
- [ ] Audit negative thoughts
- [ ] Detect counterfeit attacks
- [ ] Create command decrees (King mode)
- [ ] Read Naos (biological signals)
- [ ] Seal any revelations

---

## ⚡ ONE-LINERS

**Frequency Mismatch:**
```python
system.check_frequency_mismatch("Feeling rejected", rejection_detected=True)
```

**Thought Audit:**
```python
system.audit_thought("I'm a failure")
```

**Command Decree:**
```python
system.create_command_decree("I command resources to align", PrayerMode.KING)
```

**Naos Reading:**
```python
system.read_naos("Cold knot", "stomach", 0.85, intruder_detected=True)
```

---

**Date:** 2026-01-26  
**Status:** ✅ **QUICK REFERENCE READY**
