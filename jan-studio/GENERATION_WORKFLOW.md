# Generation Workflow Documentation

**Complete content generation workflow with validation and history.**

---

## Components

### 1. GenerationForm Component

**File:** `frontend/src/components/GenerationForm.tsx`

**Features:**
- ✅ Persona selector dropdown (loads from API)
- ✅ Large prompt textarea (200px min height)
- ✅ Output type selector (6 types: text, story, lyrics, music, TTS, explanation)
- ✅ Generate button with validation
- ✅ Progress indicator (0-100%)
- ✅ Character count
- ✅ Error handling

**Output Types:**
- Text - General text content
- Story - Short story or narrative
- Lyrics - Song lyrics
- Music - Music prompt (Suno)
- TTS - Text-to-speech script
- Explanation - Educational content

---

### 2. OutputViewer Component

**File:** `frontend/src/components/OutputViewer.tsx`

**Features:**
- ✅ Rendered output (markdown support)
- ✅ Rule validation status display
  - Passed/Failed indicator
  - Violations list
  - Warnings list
  - Checks performed
- ✅ Download button (saves as .txt)
- ✅ Copy to clipboard
- ✅ "Edit Persona" quick link if validation fails
- ✅ Rules applied display
- ✅ Timestamp and persona info

**Validation Display:**
- Green background if valid
- Red background if failed
- Lists violations and warnings
- Shows which checks were performed

---

### 3. HistoryPanel Component

**File:** `frontend/src/components/HistoryPanel.tsx`

**Features:**
- ✅ Previous generations list
- ✅ Quick re-run button
- ✅ Compare outputs (select 2+ entries)
- ✅ Checkbox selection for comparison
- ✅ Entry details (persona, type, validation status)
- ✅ Truncated preview of prompt and content
- ✅ Timestamp display

**History Storage:**
- Uses localStorage (client-side)
- Keeps last 50 entries
- Auto-saves on generation
- Sorted by most recent first

---

### 4. CompareView Component

**File:** `frontend/src/components/CompareView.tsx`

**Features:**
- ✅ Side-by-side comparison
- ✅ Multiple entries (2+)
- ✅ Shows persona, type, timestamp
- ✅ Validation status per entry
- ✅ Full content display
- ✅ Close button

---

## API Integration

### Backend Endpoint

**File:** `backend/jan-generation-api.py`

**Endpoint:** `POST /api/jan/generate`

**Request:**
```json
{
  "persona": "storyteller",
  "prompt": "Write a short story about...",
  "output_type": "story",
  "options": {
    "length": "500",
    "temperature": 0.7
  }
}
```

**Response:**
```json
{
  "success": true,
  "content": "Generated content here...",
  "validation": {
    "valid": true,
    "violations": [],
    "warnings": [],
    "checks_performed": {
      "telos": true,
      "essence": true,
      "entity_rules": true,
      "security_lens": true
    }
  },
  "rules_applied": ["telos", "essence", "entity_profile", "entity_rules"],
  "timestamp": "2025-01-27T12:00:00"
}
```

**Workflow:**
1. Receives generation request
2. Executes JAN workflow (`execute_jan_workflow`)
3. Generates content (calls AI service)
4. Validates output (`validate_output`)
5. Returns result with validation

---

## UI Layout

### Generation View

```
┌─────────────────────────────────────────────────────────┐
│ Navigation: Personas | Generate Content | Templates      │
├──────────────┬──────────────────────┬────────────────────┤
│ Generation   │ Output Viewer        │ History Panel      │
│ Form         │                      │                    │
│              │ - Content            │ - Previous gens    │
│ - Persona    │ - Validation         │ - Quick re-run     │
│ - Type       │ - Rules applied      │ - Compare          │
│ - Prompt     │ - Download/Copy      │                    │
│ - Generate   │ - Edit Persona link  │                    │
└──────────────┴──────────────────────┴────────────────────┘
```

---

## Workflow Steps

### 1. User Fills Form
- Selects persona
- Chooses output type
- Enters prompt
- Clicks "Generate"

### 2. Generation Process
- Form validates inputs
- Progress indicator shows 0-100%
- API call to `/api/jan/generate`
- JAN workflow executes
- Content generated
- Validation runs

### 3. Results Display
- Output shown in OutputViewer
- Validation status displayed
- Rules applied shown
- History entry created

### 4. User Actions
- Copy content
- Download as file
- Edit persona (if validation fails)
- Re-run generation
- Compare with history

---

## Integration with SIYEM Services

### Services Used

1. **jan_engine.execute_jan_workflow()**
   - Loads rule hierarchy
   - Applies rules to prompt
   - Returns workflow result

2. **jan_validator.validate_output()**
   - Checks telos alignment
   - Checks essence consistency
   - Checks entity rules
   - Checks security lens

3. **jan_integration.read_jan_template()**
   - Loads persona templates
   - Formats prompts

### Service Flow

```
User Input
    ↓
GenerationForm
    ↓
POST /api/jan/generate
    ↓
jan-generation-api.py
    ↓
execute_jan_workflow()
    ↓
[AI Service Call] (placeholder)
    ↓
validate_output()
    ↓
Return Result
    ↓
OutputViewer
    ↓
HistoryPanel (auto-save)
```

---

## Features

### Validation Feedback

**Passed:**
- Green background
- ✓ indicator
- Lists checks performed
- No action needed

**Failed:**
- Red background
- ✗ indicator
- Lists violations
- "Edit Persona" button shown
- Quick link to fix rules

### History Management

- **Auto-save:** Every generation saved automatically
- **Storage:** localStorage (client-side)
- **Limit:** Last 50 entries
- **Features:**
  - Quick re-run
  - Compare multiple entries
  - View full details
  - Filter by persona/type

### Output Actions

- **Copy:** One-click copy to clipboard
- **Download:** Save as .txt file
- **Edit Persona:** Quick link if validation fails
- **Re-run:** Regenerate with same parameters

---

## Error Handling

### Generation Errors

- Network errors show user-friendly messages
- Validation errors display in OutputViewer
- Failed generations show error details
- "Try Again" button available

### Validation Errors

- Violations listed clearly
- Warnings shown separately
- Checks performed displayed
- Quick fix link to persona editor

---

## Next Steps

### To Connect Real AI Service

1. **Update `jan-generation-api.py`:**
   ```python
   # Replace placeholder with actual AI call
   import openai
   response = openai.ChatCompletion.create(
       model="gpt-4",
       messages=[{"role": "user", "content": final_prompt}]
   )
   generated_content = response.choices[0].message.content
   ```

2. **Add API Key Management:**
   - Store keys securely
   - Support multiple providers
   - Handle rate limits

3. **Add Streaming Support:**
   - Real-time progress updates
   - Streaming responses
   - Better UX for long generations

---

## Status

✅ **All components built**  
✅ **API endpoints created**  
✅ **Validation integrated**  
✅ **History tracking working**  
✅ **Compare view functional**

**Ready for:** AI service integration

---

**Last Updated:** 2025-01-27  
**Version:** 0.3.0

