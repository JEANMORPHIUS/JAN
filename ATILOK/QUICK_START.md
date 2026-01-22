# ATILOK Platform - Quick Start Guide

## First Time Setup

1. **Install Dependencies**
   ```bash
   cd s:\JAN\ATILOK
   npm install
   ```

2. **Start Development Server**
   ```bash
   npm run dev
   ```

3. **Open in Browser**
   Navigate to `http://localhost:3000`

## Available Pages

- **/** - Home page with brand narrative
- **/about** - About Us and company story
- **/catalogue** - Product catalogue with search and filters
- **/catalogue/[id]** - Individual product detail pages
- **/supply-chain** - Supply chain visualisation
- **/contact** - Quote request and contact form
- **/login** - Client login portal

## Key Features Implemented

✅ Modern Industrial Design System (Navy, Steel, Copper)
✅ Responsive Navigation with Mobile Menu
✅ Product Catalogue with ATILOK Taxonomy (ATL- prefix)
✅ Category Filtering and Search
✅ Quote Request Forms
✅ Client Login Portal
✅ Supply Chain Visualisation
✅ British English Throughout
✅ SEO-Optimised Structure

## Product Data

Product data is stored in `data/products.ts`. To add new products:

1. Follow the ATILOK taxonomy: `ATL-[CATEGORY]-[SEQUENCE]`
2. Categories: ENG, DRV, SUS, ELC, CAB, MNT
3. Include full product description in ATILOK-branded copy
4. Add technical specifications array

## Customisation

### Colours
Edit `tailwind.config.js` to modify the colour palette:
- `navy` - Deep Navy (#0B1E3E)
- `steel` - Steel Grey (#7B848F)
- `copper` - Warm Copper (#C46A28)

### Typography
Fonts are loaded from Google Fonts in `app/globals.css`:
- Montserrat (Headings)
- Lato (Body)

### Brand Messaging
Update brand copy in:
- `app/page.tsx` - Home page hero and value propositions
- `app/about/page.tsx` - Company story
- `components/Footer.tsx` - Footer messaging

## Next Steps

1. **Add Real Images** - Replace placeholders with high-resolution product photography
2. **Backend Integration** - Connect forms to your API/email service
3. **Authentication** - Implement real user authentication for client portal
4. **Inventory Management** - Connect to inventory system for real-time stock
5. **Payment Processing** - Add payment gateway for B2B transactions
6. **Analytics** - Integrate Google Analytics or similar

## Production Build

```bash
npm run build
npm start
```

For deployment to Vercel, Netlify, or other platforms, follow their Next.js deployment guides.

---

**Questions?** Contact the development team or refer to the main README.md
