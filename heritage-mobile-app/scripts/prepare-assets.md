# Asset Preparation Guide

**Prepare all required assets for App Store submission**

---

## Required Assets

### iOS App Store

#### App Icon
- **Size:** 1024x1024 pixels
- **Format:** PNG (no transparency)
- **Location:** `./assets/icon.png`
- **Requirements:**
  - No rounded corners (iOS adds them)
  - No alpha channel
  - High quality, sharp edges
  - Represents app clearly

#### Screenshots (Required)
- **iPhone 6.7" (iPhone 14 Pro Max):**
  - 1290 x 2796 pixels
  - Minimum 1, maximum 10 screenshots
- **iPhone 6.5" (iPhone 11 Pro Max):**
  - 1242 x 2688 pixels
  - Minimum 1, maximum 10 screenshots
- **iPhone 5.5" (iPhone 8 Plus):**
  - 1242 x 2208 pixels
  - Minimum 1, maximum 10 screenshots
- **iPad Pro 12.9":**
  - 2048 x 2732 pixels
  - Minimum 1, maximum 10 screenshots

#### App Preview Video (Optional)
- **Duration:** 15-30 seconds
- **Format:** MOV or MP4
- **Resolution:** Match device screenshot sizes
- **Content:** Show key features in action

---

### Google Play Store

#### App Icon
- **Size:** 512x512 pixels
- **Format:** PNG (32-bit with alpha)
- **Location:** `./assets/adaptive-icon.png` (foreground)
- **Requirements:**
  - Safe zone: 432x432 pixels (center)
  - Can have transparency
  - High quality

#### Feature Graphic
- **Size:** 1024x500 pixels
- **Format:** PNG or JPG
- **Requirements:**
  - No text in outer 48 pixels (safe zone)
  - Represents app clearly
  - Eye-catching design

#### Screenshots
- **Phone:**
  - Minimum 2, maximum 8
  - At least one: 320-3840 pixels wide, 320-3840 pixels tall
  - Aspect ratio: 16:9 or 9:16
- **Tablet (7"):**
  - Minimum 1, maximum 8
  - At least one: 600-3840 pixels wide, 600-3840 pixels tall
- **Tablet (10"):**
  - Minimum 1, maximum 8
  - At least one: 1200-3840 pixels wide, 1200-3840 pixels tall

---

## Design Guidelines

### App Icon Design
- **Theme:** Heritage, community, stewardship
- **Colors:** Dark theme (#0f0f23 background, #e94560 accent)
- **Elements:** Consider heritage symbols, meridian lines, or community imagery
- **Style:** Modern, clean, recognizable at small sizes

### Screenshot Design
- **Show Key Features:**
  1. 7 Wonders list
  2. Wonder detail with Shell/Seed
  3. Interactive map
  4. Nearby sites (GPS)
  5. Network health
- **Add Text Overlays (Optional):**
  - Feature names
  - Brief descriptions
  - Mission statement

### Splash Screen
- **Current:** Dark background (#0f0f23)
- **Logo:** App icon or name
- **Style:** Minimal, fast loading

---

## Tools for Asset Creation

### Design Tools
- **Figma:** Free, web-based design tool
- **Adobe Photoshop:** Professional image editing
- **Canva:** Easy template-based design
- **Sketch:** Mac-only design tool

### Screenshot Tools
- **iOS Simulator:** Built-in screenshot
- **Android Studio:** Built-in screenshot
- **Expo:** `expo start` then take screenshots
- **Physical Device:** Native screenshot

### Icon Generators
- **App Icon Generator:** https://www.appicon.co/
- **IconKitchen:** https://icon.kitchen/
- **MakeAppIcon:** https://makeappicon.com/

---

## Asset Checklist

### iOS
- [ ] App icon (1024x1024)
- [ ] iPhone 6.7" screenshots (1-10)
- [ ] iPhone 6.5" screenshots (1-10)
- [ ] iPhone 5.5" screenshots (1-10)
- [ ] iPad Pro 12.9" screenshots (1-10)
- [ ] App preview video (optional)

### Android
- [ ] App icon (512x512)
- [ ] Feature graphic (1024x500)
- [ ] Phone screenshots (2-8)
- [ ] Tablet 7" screenshots (1-8)
- [ ] Tablet 10" screenshots (1-8)

### Common
- [ ] Splash screen (already configured)
- [ ] Adaptive icon foreground
- [ ] Adaptive icon background

---

## Quick Start

1. **Create App Icon:**
   ```bash
   # Use design tool to create 1024x1024 icon
   # Save as ./assets/icon.png
   ```

2. **Take Screenshots:**
   ```bash
   # Start app
   npm start
   
   # Open in simulator/emulator
   # Navigate to each key screen
   # Take screenshots
   ```

3. **Optimize Images:**
   ```bash
   # Use image optimization tool
   # Compress without losing quality
   # Ensure correct dimensions
   ```

4. **Organize Assets:**
   ```
   assets/
   ├── icon.png (1024x1024)
   ├── adaptive-icon.png (1024x1024)
   ├── splash.png
   ├── screenshots/
   │   ├── ios/
   │   └── android/
   └── favicon.png
   ```

---

## Mission-Aligned Design

**"THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"**

- ✅ **Heritage Connection:** Show heritage sites in assets
- ✅ **Community:** Represent global community
- ✅ **Sacred Weight:** Professional, mission-aligned design
- ✅ **Truth:** Clear, honest representation
- ✅ **Unity:** Cohesive visual identity

---

**Status:** Ready for asset creation  
**Next:** Design app icon and take screenshots
