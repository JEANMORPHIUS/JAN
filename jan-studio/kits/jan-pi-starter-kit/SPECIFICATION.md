# JAN Pi Starter Kit - Complete Specification

**Shippable education kit for classroom AI and creativity**

---

## Kit Overview

The JAN Pi Starter Kit is a complete, ready-to-use package that enables educators to teach AI and creativity without technical setup. Everything is pre-configured and ready to use out of the box.

**Target Price:** <$100  
**Target Audience:** Educators, schools, homeschoolers  
**Use Case:** Classroom AI education, creative writing, digital literacy

---

## Hardware Components

### 1. Raspberry Pi 5 (4GB RAM)
- **Model:** Raspberry Pi 5 Model B (4GB)
- **Specifications:**
  - 4GB LPDDR4 RAM
  - Broadcom BCM2712 quad-core Cortex-A76 processor
  - VideoCore VII GPU
  - 2x USB 3.0 ports, 2x USB 2.0 ports
  - Gigabit Ethernet
  - WiFi 5, Bluetooth 5.0
  - 2x micro-HDMI ports
  - 40-pin GPIO header
- **Cost:** ~$75
- **Supplier:** Official Raspberry Pi distributor

### 2. AI Kit Attachment
- **Component:** Raspberry Pi AI Kit (Hailo-8L AI accelerator)
- **Specifications:**
  - Hailo-8L NPU (13 TOPS)
  - M.2 HAT+ connector
  - Active cooling solution
  - Pre-assembled
- **Cost:** ~$70 (if included) OR optional upgrade
- **Alternative:** Standard Pi 5 without AI Kit (reduces cost to target)
- **Note:** For <$100 target, may need to make AI Kit optional

### 3. MicroSD Card (32GB)
- **Capacity:** 32GB Class 10, A1 rated
- **Pre-loaded:** Raspberry Pi OS + JAN Studio
- **Speed:** Minimum 100MB/s read, 20MB/s write
- **Brand:** SanDisk Ultra or equivalent
- **Cost:** ~$8
- **Pre-installation:** Yes (see Software section)

### 4. Power Supply
- **Type:** USB-C power supply
- **Output:** 5V, 5A (27W)
- **Specifications:**
  - Official Raspberry Pi 5 power supply
  - 1.5m USB-C cable
  - Overcurrent protection
- **Cost:** ~$12
- **Supplier:** Official Raspberry Pi

### 5. Case
- **Type:** Official Raspberry Pi 5 case
- **Features:**
  - Ventilated design
  - Access to all ports
  - Mounting points
  - Color: Red/white (Raspberry Pi colors)
- **Cost:** ~$8
- **Alternative:** Budget case (~$5)

### 6. Quick Start Card
- **Format:** Laminated card, 4"x6"
- **Content:** 5-minute setup instructions
- **Cost:** ~$0.50 (printing)

### 7. USB Drive (Optional)
- **Capacity:** 8GB USB 2.0
- **Purpose:** Backup and file transfer
- **Cost:** ~$3
- **Status:** Optional add-on

---

## Hardware Cost Breakdown

| Component | Cost | Notes |
|-----------|------|-------|
| Raspberry Pi 5 (4GB) | $75 | Core component |
| MicroSD Card (32GB) | $8 | Pre-loaded |
| Power Supply | $12 | Official Pi supply |
| Case | $8 | Official case |
| Quick Start Card | $0.50 | Printed |
| **Subtotal** | **$103.50** | |
| **With AI Kit** | **+$70** | Optional upgrade |
| **Target Adjustment** | **-$3.50** | Need to reduce |

### Cost Optimization Options

**Option 1: Standard Kit (<$100)**
- Remove AI Kit (make optional)
- Use budget case ($5 instead of $8)
- **Total: ~$100**

**Option 2: Premium Kit (~$170)**
- Include AI Kit
- Official case
- USB drive included
- **Total: ~$170**

**Recommended:** Offer both options

---

## Software Pre-Installation

### Base System
- **OS:** Raspberry Pi OS (64-bit) Lite
- **Version:** Latest stable release
- **Kernel:** 6.x
- **Boot:** Fast boot enabled (<30 seconds)

### JAN Studio Installation
- **Version:** JAN Studio Pi Edition
- **Location:** `/home/pi/jan-studio/`
- **Service:** Auto-start enabled (systemd)
- **Interface:** Kids-friendly interface default
- **Port:** 8000

### Pre-Installed Models
- **TinyLlama (1B):** ~2GB
- **Whisper Tiny:** ~75MB
- **MusicGen Small:** ~1.5GB
- **Total:** ~4GB
- **Location:** `~/.jan-models/`

### Example Personas
Pre-installed personas:
1. **The Storyteller** - Creative writing
2. **The Educator** - Explanations
3. **The Music Producer** - Music and lyrics
4. **The Helper** - Friendly assistant

**Location:** `~/JAN/Siyem.org/`

### Tutorial Videos
- **Format:** MP4, local storage
- **Location:** `/home/pi/jan-studio/tutorials/`
- **Videos:**
  1. Quick Start (2 minutes)
  2. Creating Your First Persona (5 minutes)
  3. Writing Effective Prompts (5 minutes)
  4. Advanced Features (5 minutes)
- **Total Size:** ~200MB

### Documentation
- **Location:** `/home/pi/jan-studio/docs/`
- **Files:**
  - Quick Start Guide (PDF)
  - Full Curriculum (PDF)
  - Troubleshooting Guide (PDF)
  - Teacher Guide (PDF)

---

## SD Card Image Specifications

### Image Structure
```
jan-pi-starter-kit-v1.0.img
├── Boot partition (FAT32, 256MB)
├── Root partition (ext4, ~28GB)
└── Pre-configured with:
    - Raspberry Pi OS
    - JAN Studio
    - Models
    - Personas
    - Tutorials
    - Documentation
```

### Image Creation Process
1. Flash Raspberry Pi OS to SD card
2. First boot configuration (headless)
3. Install JAN Studio
4. Download and install models
5. Configure example personas
6. Add tutorials and documentation
7. Configure auto-start
8. Test all functionality
9. Create image backup
10. Verify image integrity

### Image Size
- **Base OS:** ~2GB
- **JAN Studio:** ~500MB
- **Models:** ~4GB
- **Tutorials:** ~200MB
- **Documentation:** ~50MB
- **Total Used:** ~7GB
- **Free Space:** ~25GB (for user content)

---

## Documentation Package

### 1. Quick Start Card (Included in Box)
- **Format:** Laminated 4"x6" card
- **Content:**
  - Step 1: Plug in power
  - Step 2: Connect to network (optional)
  - Step 3: Open browser to http://localhost:8000
  - Step 4: Start creating!
- **Visual:** Simple diagrams, large text

### 2. Quick Start Guide (Digital + Print)
- **Format:** PDF, 2 pages
- **Content:**
  - 5-minute setup
  - First persona creation
  - First content generation
  - Troubleshooting basics
- **Location:** Pre-loaded on SD card

### 3. Troubleshooting Guide
- **Format:** PDF, 10 pages
- **Content:**
  - Common issues and solutions
  - Network setup
  - Performance tips
  - Support contacts
- **Location:** Pre-loaded on SD card

### 4. Classroom Setup Guide
- **Format:** PDF, 15 pages
- **Content:**
  - Network configuration
  - Multiple device access
  - Student management
  - Best practices
- **Location:** Pre-loaded on SD card

### 5. Project Ideas Booklet
- **Format:** PDF, 20 pages
- **Content:**
  - 20+ project ideas
  - Step-by-step guides
  - Cross-curricular connections
  - Assessment ideas
- **Location:** Pre-loaded on SD card

### 6. Full Curriculum (Digital)
- **Format:** PDF, 100+ pages
- **Content:**
  - Complete 5-lesson curriculum
  - Worksheets
  - Rubrics
  - Teacher guides
- **Location:** Pre-loaded on SD card

---

## Packaging

### Box Contents
1. Raspberry Pi 5 (in case)
2. Power supply with cable
3. MicroSD card (pre-loaded, in protective case)
4. Quick Start Card
5. Welcome letter
6. Warranty information
7. Support card with QR code

### Box Design
- **Size:** 8"x6"x3" (fits all components)
- **Material:** Cardboard, eco-friendly
- **Design:** Colorful, kid-friendly
- **Branding:** JAN Studio logo, "Ready to Create!"
- **Labels:** Clear component list

### Packaging Steps
1. Assemble Pi in case
2. Insert pre-loaded SD card
3. Package power supply
4. Add documentation
5. Include Quick Start Card
6. Seal box
7. Apply shipping label

---

## Quality Assurance

### Pre-Shipment Testing
Each kit must pass:

1. **Hardware Test**
   - [ ] Pi boots successfully
   - [ ] All ports functional
   - [ ] Power supply works
   - [ ] SD card readable

2. **Software Test**
   - [ ] OS boots in <30 seconds
   - [ ] JAN Studio starts automatically
   - [ ] Interface accessible at localhost:8000
   - [ ] Models load successfully
   - [ ] Example personas work
   - [ ] Content generation works

3. **Documentation Test**
   - [ ] All files present
   - [ ] PDFs open correctly
   - [ ] Tutorials play
   - [ ] Links work

4. **Packaging Test**
   - [ ] All components included
   - [ ] Box sealed properly
   - [ ] Documentation complete

---

## Pricing Strategy

### Standard Kit (<$100)
**Target Price: $99**

**Components:**
- Raspberry Pi 5 (4GB): $75
- SD Card (32GB, pre-loaded): $8
- Power Supply: $12
- Case: $5 (budget)
- Quick Start Card: $0.50
- Packaging: $1
- **Subtotal: $101.50**
- **Margin adjustment: -$2.50**
- **Final: $99**

### Premium Kit (~$170)
**Price: $169**

**Additional:**
- AI Kit: +$70
- Official case: +$3
- USB drive: +$3
- **Total: $169**

### Educational Discount
- **Bulk orders (10+):** 10% discount
- **School districts:** 15% discount
- **Non-profits:** 20% discount

---

## Shipping and Distribution

### Shipping Options
1. **Standard Shipping:** 5-7 business days
2. **Expedited:** 2-3 business days
3. **International:** Available (varies by region)

### Distribution Channels
1. **Direct Sales:** Website/store
2. **Educational Distributors:** School supply companies
3. **Retail Partners:** Electronics stores
4. **Grant Programs:** Educational grants

### Bulk Orders
- **10-24 kits:** 10% discount
- **25-49 kits:** 15% discount
- **50+ kits:** 20% discount
- **Custom:** Contact for pricing

---

## Support and Warranty

### Warranty
- **Hardware:** 1 year manufacturer warranty
- **Software:** 90 days support
- **SD Card:** 1 year replacement

### Support Channels
1. **Email:** support@janstudio.edu
2. **Documentation:** Pre-loaded guides
3. **Community:** Forum/community support
4. **Video Tutorials:** Pre-loaded on device

### Replacement Policy
- **Defective hardware:** Free replacement
- **SD card issues:** Free replacement (first year)
- **Software issues:** Support and updates

---

## Marketing Materials

### Website Content
- Product page with specifications
- Video demonstrations
- Testimonials from educators
- Ordering information

### Promotional Materials
- Product flyer (PDF)
- Classroom poster
- Social media graphics
- Press release template

---

## Future Enhancements

### Version 2.0 Ideas
- Larger SD card (64GB)
- WiFi dongle for older Pi models
- HDMI cable included
- Keyboard/mouse bundle option
- Carrying case
- Stickers and branding materials

### Optional Add-ons
- USB keyboard/mouse combo
- HDMI cable
- Carrying case
- Additional SD cards
- Model expansion pack

---

## Compliance and Safety

### Safety Standards
- CE marking (EU)
- FCC certification (US)
- RoHS compliant
- Child-safe components

### Educational Standards
- Aligns with digital literacy standards
- Supports STEM/STEAM education
- Age-appropriate content
- Privacy-compliant (no data collection)

---

## Production Checklist

### Manufacturing
- [ ] Source components
- [ ] Create SD card images
- [ ] Test each kit
- [ ] Package components
- [ ] Quality assurance
- [ ] Shipping preparation

### Documentation
- [ ] Print Quick Start Cards
- [ ] Create PDF guides
- [ ] Record tutorial videos
- [ ] Write welcome letter
- [ ] Create support materials

### Distribution
- [ ] Set up online store
- [ ] Establish distribution channels
- [ ] Create marketing materials
- [ ] Launch support system

---

## Status

✅ **Specification complete**  
✅ **Pricing defined**  
✅ **Components listed**  
✅ **Documentation specified**  
✅ **Packaging designed**  
✅ **Quality assurance defined**

**Ready for:** Manufacturing and distribution

---

**Specification Version:** 1.0  
**Last Updated:** 2025-01-27

