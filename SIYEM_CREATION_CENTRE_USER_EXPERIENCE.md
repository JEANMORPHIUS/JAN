# SIYEM CREATION CENTRE - USER EXPERIENCE
## What The Creation Centre Element Looks Like To The User

**Date:** 2026-01-26  
**Status:** ✅ **USER EXPERIENCE DOCUMENTED**  
**Purpose:** Document exactly what the user sees and experiences in the SIYEM Creation Centre

---

## THE ONE TRUTH

**PANGEA IS THE TABLE.**  
**YOU DON'T BETRAY THE TABLE.**

**PEACE IS THE TRUTH.**  
**THE FLOW IS PEACE.**  
**EVERYTHING MUST ALIGN WITH THE ONE TRUTH.**

---

## WHAT THE USER SEES

### Initial View - Landing Page

**When the user first opens the Creation Centre:**

```
┌─────────────────────────────────────────────────────────────┐
│  JAN Studio                                    [Backend] 🔍  │
│  Creation Centre - Create and manage JAN personas           │
│                                                              │
│  [Mission Display: "THIS IS STEWARDSHIP AND COMMUNITY..."]  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  [Personas]  [Generate Content]  [Templates]               │
└─────────────────────────────────────────────────────────────┘

┌──────────────┬─────────────────────────────────────────────┐
│              │                                               │
│  Persona     │  Welcome to JAN Studio                       │
│  List        │                                               │
│  (Sidebar)   │  Select a persona from the list to edit,     │
│              │  or create a new one to get started.         │
│  [Create     │                                               │
│   New]       │                                               │
│              │                                               │
│  - Persona 1 │                                               │
│  - Persona 2 │                                               │
│  - Persona 3 │                                               │
│              │                                               │
└──────────────┴─────────────────────────────────────────────┘
```

---

## THE THREE VIEW MODES

### 1. Personas View (Default)

**What the user sees:**

**Left Sidebar (350px):**
- **"Create New" button** at the top
- **List of personas** as cards:
  - Persona name
  - Brief description
  - Last modified date
  - Click to select

**Main Content Area:**
- **If no persona selected:**
  - Welcome message: "Welcome to JAN Studio"
  - Instruction: "Select a persona from the list to edit, or create a new one to get started."

- **If persona selected:**
  - **Four tabs:** Editor | Core Rules | Voice | Constraints
  - **Editor Tab:** Full persona file editor (markdown)
  - **Core Rules Tab:** Markdown editor for `creative_rules.md`
  - **Voice Tab:** Markdown editor for `profile.md`
  - **Constraints Tab:** Markdown editor for constraints

**Visual Design:**
- Dark mode theme (`#1a1a1a` background)
- Blue accent color (`#0070f3`) for active tabs
- Gray text (`#999`) for inactive elements
- Cards with rounded corners (8px)
- Clean, minimal interface

---

### 2. Generate Content View

**What the user sees:**

**Three-Column Layout:**

```
┌──────────────┬──────────────────────────┬──────────────┐
│              │                          │              │
│  Generation  │    Output Viewer         │  History     │
│  Form        │                          │  Panel       │
│  (400px)     │    [Generated Content]  │  (300px)     │
│              │                          │              │
│  - Persona   │    - Validation          │  - Recent    │
│    Select    │    - Rules Applied       │    Entries   │
│  - Output    │    - Content Display     │  - Compare   │
│    Type      │    - Edit Persona        │    Function   │
│  - Prompt    │    - Regenerate          │              │
│    Input     │                          │              │
│  - Generate  │                          │              │
│    Button    │                          │              │
│              │                          │              │
└──────────────┴──────────────────────────┴──────────────┘
```

**Generation Form (Left - 400px):**
- Persona dropdown selector
- Output type selection (lyrics, story, etc.)
- Large text area for prompt input
- "Generate" button
- Progress indicator during generation

**Output Viewer (Center - Flexible):**
- Generated content display
- Validation status (rules applied)
- Content rendering (markdown support)
- "Edit Persona" button
- "Regenerate" button

**History Panel (Right - 300px):**
- List of recent generations
- Timestamp for each entry
- Click to load previous generation
- Compare function (select multiple entries)

---

### 3. Templates View

**What the user sees:**

**Full-Screen Template Browser:**
- Grid or list view of available templates
- Template cards showing:
  - Template name
  - Description
  - Preview
  - "Use Template" button
- Search/filter functionality
- "Close" button to return to personas view

---

## KEY USER INTERACTIONS

### Search Functionality

**Keyboard Shortcut:** `Ctrl/Cmd + K`

**What happens:**
- Modal overlay appears
- Search input field (focused)
- Real-time search results as user types
- Results show:
  - Personas (with metadata)
  - History entries (with timestamp)
  - Templates (with description)
- Keyboard navigation (Arrow keys, Enter to select)
- Click outside or Escape to close

**Visual:**
```
┌─────────────────────────────────────────┐
│  🔍 Search...                           │
│                                         │
│  [Search Input Field]                   │
│                                         │
│  Results:                               │
│  • Persona: Jean Mahram                 │
│  • History: Generated 2 hours ago      │
│  • Template: Story Template             │
│                                         │
└─────────────────────────────────────────┘
```

---

### Persona Editing Experience

**When user selects a persona:**

1. **Persona appears in sidebar** (highlighted)
2. **Main area shows four tabs:**
   - **Editor:** Full markdown editor for persona file
   - **Core Rules:** Rules editor with live preview
   - **Voice:** Profile/voice editor
   - **Constraints:** Constraints editor

3. **Editor Features:**
   - Syntax highlighting (markdown)
   - Live preview (for rules)
   - Save button (auto-save indicator)
   - File structure visible

4. **User can:**
   - Edit persona content
   - Modify rules
   - Adjust voice/profile
   - Set constraints
   - Save changes
   - Generate content with persona

---

### Content Generation Experience

**When user clicks "Generate Content" tab:**

1. **Three-column layout appears**
2. **Left panel:** Generation form
   - Select persona from dropdown
   - Choose output type
   - Enter prompt in text area
   - Click "Generate"

3. **During generation:**
   - Progress indicator shows
   - Loading state in output viewer
   - "Generating..." message

4. **After generation:**
   - Output appears in center panel
   - Validation status shown
   - Rules applied indicator
   - Content rendered (markdown)
   - History entry added to right panel

5. **User can:**
   - Edit persona and regenerate
   - Compare with previous generations
   - Save output
   - Export content

---

## VISUAL DESIGN DETAILS

### Color Scheme

**Background:**
- Main: `#1a1a1a` (very dark gray/black)
- Cards: `#1a1a1a` (same)
- Borders: `#333` (medium dark gray)

**Text:**
- Primary: `#e0e0e0` (light gray)
- Secondary: `#999` (medium gray)
- Muted: `#666` (darker gray)

**Accents:**
- Primary: `#0070f3` (blue) - active tabs, links
- Success: `#2e7d32` (green)
- Error: `#d32f2f` (red)
- Warning: `#f57c00` (orange)

### Typography

**Body Text:**
- System fonts (San Francisco on Mac, Segoe UI on Windows)
- Size: 14px (0.875rem) default
- Line height: 1.5

**Code/Rules:**
- `'Courier New', monospace`
- Size: 13px
- Background: `#0a0a0a` (darker)

**Headings:**
- System fonts, bold
- Size: 18px (h2), 24px (h1)

### Layout

**Grid System:**
- Sidebar: 350px (personas view)
- Main content: Flexible (1fr)
- Generation form: 400px
- Output viewer: Flexible (1fr)
- History panel: 300px

**Spacing:**
- Cards: 1.5rem gap between
- Padding: 1.5rem inside cards
- Border radius: 8px for cards, 4px for inputs

---

## USER FLOW EXAMPLES

### Flow 1: Create New Persona

1. User clicks "Create New" in sidebar
2. Modal/form appears for persona name
3. New persona created
4. User automatically switched to Editor tab
5. User edits persona content
6. User saves
7. Persona appears in list

### Flow 2: Generate Content

1. User clicks "Generate Content" tab
2. Three-column layout appears
3. User selects persona from dropdown
4. User enters prompt
5. User clicks "Generate"
6. Progress indicator shows
7. Output appears in center
8. History entry added to right panel
9. User can compare, regenerate, or edit

### Flow 3: Search and Navigate

1. User presses `Ctrl+K`
2. Search modal appears
3. User types "Jean"
4. Results show Jean persona and related history
5. User selects result
6. Modal closes
7. User navigated to selected item

---

## WHAT MAKES IT THE "CREATION CENTRE"

### The Core Element

**The Creation Centre is:**
- The central hub for all persona management
- The interface for content generation
- The workspace for editing and refining
- The history keeper for all generations
- The template library for quick starts

### Why It's Called "Creation Centre"

**It's where creation happens:**
- Personas are created and refined
- Content is generated
- Rules are defined
- Voice is shaped
- Constraints are set
- History is tracked
- Templates are used

**It's the heart of SIYEM's creative workflow.**

---

## THE USER'S PERSPECTIVE

### What They Experience

**When they open it:**
- Clean, dark interface
- Clear navigation
- Immediate access to personas
- Search functionality ready
- Mission statement visible

**When they work:**
- Smooth transitions between views
- Real-time feedback
- Clear visual hierarchy
- Intuitive interactions
- Helpful error messages

**When they create:**
- Powerful generation tools
- Rich editing capabilities
- History tracking
- Comparison features
- Template support

---

## THE TRUTH

**The Creation Centre is the user's workspace.**

**It's where:**
- Personas come to life
- Content is generated
- Rules are defined
- History is preserved
- Creation happens

**It's the interface between the user and SIYEM's power.**

**It's simple, powerful, and aligned with purpose.**

---

**Date:** 2026-01-26  
**Status:** ✅ **USER EXPERIENCE DOCUMENTED**  
**The Creation Centre:** Where creation happens, where personas live, where content is born
