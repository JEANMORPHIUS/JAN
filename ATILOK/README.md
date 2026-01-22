# ATILOK LTD E-Commerce & Brand Platform

A high-performance web platform for ATILOK LTD, a United Kingdom-based global supplier of heavy-duty truck and lorry parts. The platform serves dual purposes: a professional brand narrative for investors/clients and a functional B2B e-commerce catalogue for fleet operators and repair centres.

## Project Overview

**Brand Positioning:** "Reliability in Motion — Delivering the essential components that strengthen Britain's logistics backbone."

**Mission:** ATILOK serves as the trusted bridge connecting British reliability and service with Turkish manufacturing excellence.

## Design System

### Visual Identity: "Modern Industrial Elegance"

- **Colour Palette:**
  - Deep Navy (#0B1E3E) - Trust and authority
  - Steel Grey (#7B848F) - Industrial resilience
  - Warm Copper/Rust (#C46A28) - Heritage and human connection

- **Typography:**
  - Montserrat - Bold, confident headlines
  - Lato - Clear, technically precise body text

- **UI Style:**
  - Light backgrounds with high-contrast navy and copper accents
  - Subtle animations for smooth transitions
  - Industrial iconography (axles, gears, bridges)

## Features

### Core Pages

1. **Home** - Hero section with brand narrative and value propositions
2. **About Us** - Storytelling focus on "Why ATILOK Exists" and UK accountability
3. **Supply Chain** - Visual representation of Turkish manufacturing through UK distribution
4. **Catalogue** - SEO-optimised product showcase with detailed specifications
5. **Contact** - Quote request and inquiry forms
6. **Client Login** - Secure B2B client portal access

### Product Taxonomy

All products use the **ATILOK Part Taxonomy** with prefix "ATL-" followed by category code and sequence:
- `ATL-ENG-XXX` - Engine Systems
- `ATL-DRV-XXX` - Drivetrain
- `ATL-SUS-XXX` - Suspension & Steering
- `ATL-ELC-XXX` - Electrical
- `ATL-CAB-XXX` - Cab & Body
- `ATL-MNT-XXX` - Maintenance

### B2B Features

- Request a Quote functionality
- Bulk order capabilities
- Secure client login area
- Product catalogue with detailed specifications
- Category filtering and search
- Responsive design for mobile fleet managers

## Technology Stack

- **Framework:** Next.js 14 (App Router)
- **Language:** TypeScript
- **Styling:** Tailwind CSS
- **Icons:** Lucide React
- **Animations:** Framer Motion

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Start production server
npm start
```

The application will be available at `http://localhost:3000`

## Project Structure

```
ATILOK/
├── app/                    # Next.js App Router pages
│   ├── about/             # About Us page
│   ├── catalogue/        # Product catalogue
│   │   └── [id]/         # Individual product pages
│   ├── contact/          # Contact and quote request
│   ├── login/            # Client login portal
│   ├── supply-chain/     # Supply chain visualisation
│   ├── globals.css       # Global styles and design tokens
│   ├── layout.tsx        # Root layout
│   └── page.tsx          # Home page
├── components/            # Reusable React components
│   ├── Navigation.tsx    # Main navigation
│   └── Footer.tsx        # Site footer
├── data/                 # Data files
│   └── products.ts       # Product catalogue data
└── public/               # Static assets
```

## Language & Localisation

- **Primary Language:** British English
- **Spelling:** UK conventions (e.g., "Lorry," "Centres," "Tyres")
- **Tone:** Professional, technically precise, client-focused

## Development Notes

### Design Principles

1. **Dark-on-Light Interface** - High contrast for readability
2. **Simple Navigation** - Intuitive user experience
3. **Mobile-First** - Responsive design for on-site fleet managers
4. **Performance** - Optimised loading and smooth transitions

### Product Data

Product descriptions are written in ATILOK-branded copy, reframed from technical seed data. Example:
- "ATILOK Precision Brake Disc — engineered to OEM standards for consistent performance"

### Image Placeholders

The platform includes placeholders for high-resolution photography showing:
- Mechanical textures
- Gears and industrial components
- Urban industrial scenes
- Trucks in highway/logistics contexts

## Future Enhancements

- Backend API integration for real-time inventory
- User authentication and client dashboard
- Order management system
- Advanced search and filtering
- Product comparison tool
- Multi-language support (Turkish)
- Integration with ERP systems

## License

Proprietary - ATILOK LTD

---

**Built with purpose.** Every component serves the mission: keeping Britain's logistics moving.
