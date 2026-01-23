# JAN Studio Kids - Kid-Friendly Interface

**Interface designed for children ages 10-16**

---

## Design Principles

✅ **Large buttons** - Easy to click  
✅ **Visual feedback** - Clear animations and progress  
✅ **Progress indicators** - Shows what's happening  
✅ **No technical jargon** - Friendly, simple language  
✅ **Accessibility** - Voice input and read-aloud  

---

## Pages

### 1. Welcome Screen
**"Let's Create Something!"**

- Large, colorful buttons
- Emoji icons
- Clear options:
  - Create a Character
  - Write a Story
  - My Saved Creations

### 2. Character Creator
**"Describe Your Character"**

- Simple form fields
- Voice input option (🎤)
- Large text areas
- Friendly prompts

### 3. Story Generator
**"What Should They Do?"**

- Character selection cards
- Story prompt input
- Voice input option
- Clear instructions

### 4. Results Screen
**"Here's Your Story!"**

- Confetti animation
- Large, readable text
- Action buttons:
  - 🔊 Read Aloud
  - 💾 Save to USB
  - 🖨️ Print
  - 🏠 Home

### 5. Saved Creations
**"My Saved Creations"**

- List of saved stories
- Easy navigation
- Read full story option

---

## Features

### Voice Input 🎤

- Click "Use Voice" button
- Speak your input
- Automatically transcribed
- Works with browser speech recognition

### Read Aloud 🔊

- Click "Read Aloud" button
- Story is read using text-to-speech
- Adjustable speed and pitch
- Browser-based TTS

### Save to USB 💾

- Downloads story as text file
- Can be copied to USB drive
- Saved with timestamp
- Also saved locally in browser

### Print Option 🖨️

- Opens print dialog
- Formatted for printing
- Perfect for classrooms
- Can print multiple copies

---

## Age Targeting

**Ages 10-16**

- Simple language
- Large, clear buttons
- Visual feedback
- No technical terms
- Fun, engaging design

---

## Accessibility

### Visual

- Large fonts (1.3rem - 3rem)
- High contrast colors
- Clear visual hierarchy
- Emoji icons for clarity

### Audio

- Voice input for typing
- Text-to-speech for reading
- Audio feedback for actions

### Motor

- Large click targets
- Spacious layout
- No precision required
- Touch-friendly

---

## Usage

### Start Service

```bash
sudo systemctl start jan-studio-kids
```

### Access Interface

Open browser: `http://localhost:8000`

Or from another device: `http://<pi-ip>:8000`

### For Kids

1. Click "Create a Character"
2. Enter character name and description
3. Click "Create Character!"
4. Go back and click "Write a Story"
5. Select your character
6. Describe what should happen
7. Click "Create Story!"
8. Enjoy your story!

---

## Technical Details

### Frontend

- **Framework:** Vanilla JavaScript
- **Styling:** CSS with gradients and animations
- **Storage:** LocalStorage for characters and stories
- **Voice:** Web Speech API
- **TTS:** Web Speech Synthesis API

### Backend

- **API:** FastAPI (lightweight)
- **AI:** TinyLlama (local)
- **CORS:** Enabled for network access

### Files

```
pi/
├── frontend-kids/
│   └── index.html          # Kids interface
├── kids_api.py             # Kids API
├── jan-studio-kids.service # Systemd service
└── KIDS_INTERFACE.md       # This file
```

---

## Safety Features

### Content Filtering

- Prompts are modified to be kid-friendly
- AI is instructed to keep content appropriate
- Positive and engaging tone

### Privacy

- All data stored locally
- No external API calls
- No data collection
- Works offline

---

## Classroom Use

### Setup

1. Install on Pi
2. Connect to classroom network
3. Access from student devices
4. Students can create stories independently

### Printing

- Stories can be printed
- Perfect for sharing
- Can create classroom book
- No internet required

### USB Export

- Stories saved to USB
- Can be taken home
- Shared with parents
- Backup for students

---

## Customization

### Colors

Edit CSS in `index.html`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Text

All text is in HTML - easy to modify for different languages or age groups.

### Features

Add or remove features by editing the HTML and JavaScript.

---

## Troubleshooting

### Voice Input Not Working

- Check browser permissions
- Use Chrome or Edge (best support)
- Try typing instead

### Read Aloud Not Working

- Check browser support
- Use Chrome or Edge
- May need internet for some voices

### Save Not Working

- Check browser download settings
- Try different browser
- Check disk space

---

## Status

✅ **Kid-friendly interface**  
✅ **Voice input**  
✅ **Read aloud**  
✅ **Save to USB**  
✅ **Print option**  
✅ **Accessibility features**  
✅ **Safe and private**

**Ready for:** Classroom and home use

---

**Last Updated:** 2025-01-27  
**Version:** 1.0.0-kids

