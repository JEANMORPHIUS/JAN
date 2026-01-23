# JAN Studio Frontend

Next.js frontend for JAN Studio.

## Setup

### Install Dependencies

```bash
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Build

```bash
npm run build
npm start
```

## Project Structure

```
src/
├── components/        # React components
│   ├── PersonaList.tsx
│   └── PersonaEditor.tsx
├── pages/            # Next.js pages
│   ├── index.tsx     # Main page
│   └── _app.tsx      # App wrapper
├── api/              # API client
│   └── personas.ts
└── styles/           # Global styles
    └── globals.css
```

## Features

- List all personas
- Create new personas
- Edit persona files
- Save file changes
- View file content

## API Integration

The frontend connects to the FastAPI backend via Next.js rewrites (see `next.config.js`).

All API calls go through `/api/*` which proxies to `http://localhost:8000/*`.

