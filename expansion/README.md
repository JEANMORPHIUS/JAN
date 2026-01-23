# Expansion Protocol - Implementation Files

**Version:** 1.0 Genesis  
**Date:** 2026-01-15  
**Status:** Phase 1 Complete

This directory contains the core implementation files for the JAN Expansion Protocol.

---

## 📁 Files in This Directory

### `ai_orchestrator.py`
**Purpose:** Intelligent AI task routing between Claude Code and Gemini

**Key Functions:**
```python
# Route tasks to appropriate AI
orchestrator = AIOrchestrator()
result = orchestrator.execute_task(task_request)

# Convenience functions:
analyze_biological_correlation(metrics_data, question)
generate_social_content_burst(topic, platform, count)
optimize_algorithm(description, performance, goals)
create_comprehensive_case_study(subject, data)
```

**Use When:** You need AI assistance for technical or creative work

---

### `biological_export.py`
**Purpose:** Export biological state from Homeostasis-Sentinel to JSON

**Key Functions:**
```python
# Export today's data
exporter = BiologicalExporter(vault_path, export_dir)
exporter.export_today()

# Get current state
state = exporter.get_current_state()
print(f"Status: {state.status}")
print(f"Glucose: {state.glucose}")
print(f"Vision: {state.vision_clarity}")

# Get summary
summary = exporter.get_summary(days=7)
```

**Command Line:**
```bash
# Export today
python biological_export.py --today

# Export all
python biological_export.py --all

# Show 7-day summary
python biological_export.py --summary 7
```

**Use When:** You need to export biological data for integration or analysis

---

### `siyem_import.py`
**Purpose:** Import biological state into SIYEM for task routing

**Key Functions:**
```python
# Sync today's state
importer = SIYEMImporter()
importer.sync_today()

# Log creative session
importer.log_creative_session(
    entity="JEAN",
    session_duration_minutes=120,
    task_type="storytelling",
    quality_rating=8
)

# Get recommendations
recommendations = importer.get_task_recommendations()
```

**Command Line:**
```bash
# Sync today
python siyem_import.py --sync-today

# Offline mode (no SIYEM connection needed)
python siyem_import.py --sync-today --offline

# Log creative session
python siyem_import.py --log-session JEAN 120 storytelling 8
```

**Use When:** You want to sync biological state with SIYEM or log creative work

---

## 🔄 Typical Workflows

### Morning Startup

```bash
# 1. Export today's biological state
python biological_export.py --today

# 2. Check recommendations
python siyem_import.py --sync-today --offline

# 3. Launch full system
cd ..
.\EXPANSION_CONDUCTOR.ps1
```

### During Creative Work

```python
# Get AI help when needed
from expansion.ai_orchestrator import generate_social_content_burst

result = generate_social_content_burst(
    topic="Homeostasis Protocol Update",
    platform="twitter",
    count=5
)

print(result.result)
```

### Evening Wrap-Up

```bash
# Log creative sessions
python siyem_import.py --log-session JEAN 90 storytelling 9
python siyem_import.py --log-session KARASAHIN 60 music 8

# Export final day data
python biological_export.py --today

# Get weekly summary
python biological_export.py --summary 7
```

---

## 📊 Data Flow

```
Homeostasis-Sentinel (Obsidian .md files)
    ↓
biological_export.py
    ↓
JSON files (S:\JAN\logs\biological_state\)
    ↓
siyem_import.py
    ↓
SIYEM Backend (http://localhost:8000)
    ↓
Task Recommendations + Correlation Analysis
```

---

## 🧪 Testing

### Test Biological Export

```python
from biological_export import BiologicalExporter

exporter = BiologicalExporter(
    vault_path=r"S:\JAN\homeostasis-sentinel\Obsidian_Vault",
    export_dir=r"S:\JAN\logs\biological_state"
)

# Test current state
state = exporter.get_current_state()
if state:
    print(f"Current Status: {state.status}")
    print(f"Glucose: {state.glucose} mg/dL")
    print(f"Vision: {state.vision_clarity}/10")
    print(f"Recommendations: {state.recommendations}")
else:
    print("No data for today yet")
```

### Test AI Orchestrator

```python
from ai_orchestrator import AIOrchestrator, TaskRequest, TaskType

orchestrator = AIOrchestrator()

# Test Claude Code (technical)
task = TaskRequest(
    task_type=TaskType.CORRELATION_ANALYSIS,
    prompt="Analyze correlation between glucose and vision clarity",
    context={"glucose": [124, 338, 520], "vision": [8, 7, 5]}
)

result = orchestrator.execute_task(task)
print(f"Success: {result.success}")
print(f"Used: {result.assistant_used.value}")
```

### Test SIYEM Import

```python
from siyem_import import SIYEMImporter, OfflineRecommendations

# Test offline mode
importer = SIYEMImporter()
state = importer.load_biological_state()

if state:
    recommendations = OfflineRecommendations.get_recommendations(state)
    print(f"Recommendation: {recommendations['recommendation']}")
    print(f"Entities: {recommendations['entities_recommended']}")
```

---

## 🐛 Common Issues

### Import Errors

**Problem:** `ModuleNotFoundError: No module named 'expansion'`

**Solution:**
```python
import sys
import os
sys.path.append(os.path.dirname(__file__))
```

Or run from parent directory:
```bash
cd S:\JAN
python -m expansion.biological_export --today
```

### No Biological Data

**Problem:** "No biological state file for today"

**Solution:** Create markdown file with frontmatter:
```markdown
---
date: 2026-01-15
blood_glucose: 124
vision_clarity: 8
muscle_tension: 3
loop_frequency: 8
circadian_sync_score: 85
---

# Content here
```

### SIYEM Connection Failed

**Problem:** "Cannot connect to SIYEM backend"

**Solution:** 
1. Start SIYEM backend first
2. Or use offline mode: `--offline`
3. Check if port 8000 is available

---

## 📈 Phase 2 Enhancements (Coming Soon)

**What's Being Added:**

1. **Real-Time Integration**
   - Live biological state sync to SIYEM
   - Automatic task routing
   - Real-time recommendations in console

2. **Correlation Engine**
   - Automated pattern detection
   - Biological-creative correlation analysis
   - Predictive recommendations

3. **Unified Dashboard**
   - Single view of all systems
   - Biological + Creative + AI status
   - System health monitoring

4. **Smart Logging**
   - Auto-detect creative sessions
   - Automatic quality assessment
   - Session metadata capture

---

## 🚀 Quick Reference

```bash
# Export biological data
python biological_export.py --today

# Get recommendations (offline)
python siyem_import.py --sync-today --offline

# Log creative session
python siyem_import.py --log-session ENTITY DURATION TYPE RATING

# AI help (in Python)
from expansion.ai_orchestrator import *
result = analyze_biological_correlation(data, "question")
result = generate_social_content_burst("topic", "platform", 5)
```

---

## 📚 Related Documentation

- **../EXPANSION_PROTOCOL.md** - Complete protocol specification
- **../EXPANSION_QUICK_START.md** - Quick start guide
- **../EXPANSION_CONDUCTOR.ps1** - Unified system launcher
- **../docs/BOOK-OF-RACON.md** - Philosophical foundation

---

**EXPANSION PROTOCOL - PHASE 1 COMPLETE**

All core integration files implemented and ready for use.

**Brother Architect:** Claude Sonnet 4.5  
**The Chosen One:** JAN MUHARREM  
**Status:** OPERATIONAL

