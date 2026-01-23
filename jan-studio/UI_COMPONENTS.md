# JAN Studio UI Components

**Complete persona creation UI with visual editing capabilities.**

---

## Components Built

### 1. PersonaForm Component

**File:** `frontend/src/components/PersonaForm.tsx`

**Features:**
- ✅ Name input with validation (lowercase, alphanumeric, hyphens, underscores)
- ✅ Description textarea
- ✅ Template selector (Storyteller, Music Producer, Educator, Blank)
- ✅ "Create Persona" button
- ✅ Form validation and error handling

**Visual Design:**
- Clean card layout
- Template cards with hover states
- Validation feedback
- Dark mode styling

---

### 2. RuleEditor Component

**File:** `frontend/src/components/RuleEditor.tsx`

**Features:**
- ✅ Markdown editor using `react-markdown-editor-lite`
- ✅ Live preview pane
- ✅ Tabs for: Core Rules, Voice, Constraints
- ✅ Save button with status feedback
- ✅ File loading and error handling

**Visual Design:**
- Split-pane editor (markdown | preview)
- Dark mode styling
- Monospace fonts for code
- 600px height editor

**File Mapping:**
- `core-rules` → `creative_rules.md`
- `voice` → `profile.md`
- `constraints` → `creative_rules.md`

---

### 3. PersonaCard Component

**File:** `frontend/src/components/PersonaCard.tsx`

**Features:**
- ✅ Card view of personas
- ✅ Quick stats display:
  - File count
  - Rule count
  - Last modified date
- ✅ Edit/Delete actions
- ✅ Delete confirmation

**Visual Design:**
- Card layout with hover effects
- Stats grid (3 columns)
- Action buttons
- Monospace fonts for stats

---

### 4. Updated PersonaList Component

**File:** `frontend/src/components/PersonaList.tsx`

**Features:**
- ✅ Integrates PersonaForm for creation
- ✅ Displays PersonaCard components
- ✅ Loads persona stats
- ✅ Handles create/delete operations

---

## Visual Design

### Dark Mode Default

**Color Scheme:**
- Background: `#0a0a0a` (very dark)
- Cards: `#1a1a1a` (dark)
- Borders: `#333` (medium dark)
- Text: `#e0e0e0` (light)
- Accent: `#0070f3` (blue)
- Error: `#d32f2f` (red)
- Success: `#2e7d32` (green)

### Typography

- **Body:** System fonts (San Francisco, Segoe UI, etc.)
- **Code/Rules:** `'Courier New', monospace`
- **Headings:** System fonts, bold

### Layout

- **Grid Layout:** 350px sidebar | flexible main area
- **Card Spacing:** 1.5rem between cards
- **Padding:** 1.5rem inside cards
- **Border Radius:** 8px for cards, 4px for inputs

---

## Main Page Structure

**File:** `frontend/src/pages/index.tsx`

**Layout:**
```
┌─────────────────────────────────────────┐
│ Header: JAN Studio                       │
├──────────────┬──────────────────────────┤
│ PersonaList  │ Main Content Area        │
│ (Sidebar)    │                          │
│              │ ┌──────────────────────┐ │
│ - Create     │ │ Tabs: Editor | Rules │ │
│ - Persona    │ ├──────────────────────┤ │
│   Cards      │ │ Content (Editor/     │ │
│              │ │  RuleEditor)         │ │
│              │ └──────────────────────┘ │
└──────────────┴──────────────────────────┘
```

**Tabs:**
- **Editor:** File-based editor (PersonaEditor)
- **Core Rules:** Markdown editor for creative_rules.md
- **Voice:** Markdown editor for profile.md
- **Constraints:** Markdown editor for creative_rules.md

---

## API Integration

### Endpoints Used

- `GET /api/jan/personas` - List personas
- `POST /api/jan/personas` - Create persona
- `GET /api/jan/personas/{name}/files` - List files
- `GET /api/jan/personas/{name}/files/{file}` - Get file content
- `PUT /api/jan/personas/{name}/files/{file}` - Save file
- `DELETE /api/jan/personas/{name}` - Delete persona

### Error Handling

- Network errors show user-friendly messages
- Validation errors display inline
- Loading states for async operations
- Success/error feedback

---

## Dependencies Added

```json
{
  "react-markdown-editor-lite": "^1.3.0",
  "react-markdown": "^9.0.0",
  "remark-gfm": "^4.0.0",
  "markdown-it": "^14.0.0"
}
```

---

## Usage Flow

### Creating a Persona

1. Click "+ Create New Persona"
2. Fill in name, description, select template
3. Click "Create Persona"
4. Persona appears in list
5. Select persona to edit

### Editing Rules

1. Select persona from list
2. Click "Core Rules", "Voice", or "Constraints" tab
3. Edit markdown in editor
4. See live preview
5. Click "Save"

### Viewing Stats

1. Persona cards show:
   - File count
   - Rule count
   - Last modified date

---

## Customization

### Changing Colors

Edit `frontend/src/styles/globals.css`:
- Background colors
- Border colors
- Text colors
- Accent colors

### Changing Layout

Edit `frontend/src/pages/index.tsx`:
- Grid column widths
- Tab order
- Component arrangement

### Adding Templates

Edit `frontend/src/components/PersonaForm.tsx`:
- Add to `TEMPLATES` array
- Update template handling in backend

---

## Status

✅ **All components built and ready**  
✅ **Dark mode styling complete**  
✅ **Markdown editor integrated**  
✅ **File management working**  
✅ **Stats display functional**

**Ready for:** Backend integration and testing

---

**Last Updated:** 2025-01-27  
**Version:** 0.2.0

