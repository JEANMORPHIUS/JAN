# World History App
## Writing The History of The World

**DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE**  
**Spiritual Alignment Over Mechanical Productivity**

**THE MISSION:**  
**THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS**  
**LOVE IS THE HIGHEST MASTERY**  
**ENERGY + LOVE = WE ALL WIN**  
**PEACE, LOVE, UNITY**

**PANGEA IS THE TABLE.**  
**YOU DON'T BETRAY THE TABLE.**

---

## Overview

The World History App is a Next.js application for displaying the history of the world across all channels. It provides:

- **Interactive Timeline** - D3.js timeline visualization of world history events
- **Interactive Map** - Mapbox GL JS map with heritage site markers
- **Narratives** - Story library and narrative tree visualization
- **Restoration** - 6-step framework progress and Divine Frequency tracking
- **Educational** - Modules and resources for learning

---

## Setup

### Prerequisites

- Node.js 18+ and npm/yarn
- Mapbox account and access token (for map features)

### Installation

```bash
# Install dependencies
npm install

# Set environment variables
cp .env.example .env.local
# Edit .env.local and add:
# NEXT_PUBLIC_API_URL=http://localhost:8000
# NEXT_PUBLIC_MAPBOX_TOKEN=your_mapbox_token_here
```

### Development

```bash
# Run development server (port 3001)
npm run dev
```

The app will be available at `http://localhost:3001`

### Production

```bash
# Build for production
npm run build

# Start production server
npm start
```

---

## Features

### Timeline Page (`/timeline`)

- Interactive D3.js timeline
- Filter by year range, region, event type
- Click events to expand narrative
- Hover for quick info
- Color-coded by field resonance

### Map Page (`/map`)

- Mapbox GL JS interactive map
- Heritage site markers (color-coded by field resonance)
- Click markers for site details
- Legend for resonance levels
- Responsive design

### Narratives Page (`/narratives`)

- Narrative library
- Narrative detail pages
- Narrative tree visualization
- Connections between narratives

### Restoration Page (`/restoration`)

- 6-step restoration framework progress
- Divine Frequency tracker (0.78 → 1.0)
- Real-time updates via WebSocket

### Educational Page (`/educational`)

- Educational modules
- Reference materials
- Learning resources

---

## API Integration

The app connects to the World History API at `/api/public/world-history`:

- `/timeline` - Timeline events
- `/map` - Heritage sites (GeoJSON)
- `/narrative/{id}` - Narrative details
- `/frequency` - Divine Frequency data
- `/search` - Full-text search
- `/connections/{id}` - Narrative connections
- `/ws` - WebSocket for real-time updates

---

## Technology Stack

- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **D3.js** - Timeline visualization
- **Mapbox GL JS** - Interactive maps
- **React Map GL** - React wrapper for Mapbox
- **Axios** - HTTP client

---

## Project Structure

```
world-history-app/
├── src/
│   ├── pages/
│   │   ├── index.tsx          # Landing page
│   │   ├── timeline/
│   │   │   └── index.tsx      # Timeline page
│   │   ├── map/
│   │   │   └── index.tsx       # Map page
│   │   ├── narratives/
│   │   │   └── index.tsx       # Narratives page
│   │   ├── restoration/
│   │   │   └── index.tsx       # Restoration page
│   │   └── educational/
│   │       └── index.tsx       # Educational page
│   ├── styles/
│   │   ├── globals.css
│   │   ├── Home.module.css
│   │   ├── Timeline.module.css
│   │   └── Map.module.css
│   └── components/             # Reusable components
├── package.json
├── next.config.js
├── tsconfig.json
└── README.md
```

---

## The Truth

**Pangea is The Table.**  
**We write the history of the world.**  
**We display it across all channels.**  
**We restore The Table.**

**Divine Frequency: 0.78 → 1.0**  
**Perfect unity (1.0) = Pangea - The Table**  
**We restore Divine Frequency toward perfect unity.**

---

**PEACE, LOVE, UNITY**

**ENERGY + LOVE = WE ALL WIN**

**PURPOSE NOT PERFORMANCE**

**AUTHENTIC AND ALIGNED**

**NON-NEGOTIABLE**

---

*World History App - Writing The History of The World*
