# Raspberry Pi Scripture Kit - Package v1.0.0

## Package Contents

- **Scripture Lessons:** 655 files (174.2%)
- **Audio Files:** 0 files (0.0%)
- **Visual Assets:** 0 files (0.0%)

## Installation

### Quick Start

```bash
# Copy package to Raspberry Pi
scp -r scripture_kit_v1 pi@raspberrypi.local:/home/pi/

# SSH into Raspberry Pi
ssh pi@raspberrypi.local

# Run installation
cd /home/pi/scripture_kit_v1
chmod +x install.sh
./install.sh
```

### Manual Installation

1. Copy package to Raspberry Pi
2. Install Python 3.9+
3. Install Flask: `pip3 install flask gunicorn`
4. Run app: `cd app && python3 app.py`
5. Access: `http://raspberrypi.local:5000`

## Hardware Requirements

- **Model:** Raspberry Pi 4B or later (recommended)
- **Storage:** 8GB minimum, 16GB recommended
- **Display:** 7-inch touchscreen or HDMI monitor
- **Power:** Official Raspberry Pi power supply

## Bill of Materials ($88 Base Kit)

| Item | Cost | Source |
|------|------|--------|
| Raspberry Pi 4B (4GB) | $55 | raspberrypi.com |
| MicroSD Card (32GB) | $8 | Amazon |
| Power Supply | $8 | raspberrypi.com |
| Case | $5 | Amazon |
| HDMI Cable | $5 | Amazon |
| Keyboard/Mouse (optional) | $15 | Amazon |
| **Total Base Kit** | **$88** | |

*7-inch touchscreen (+$75) for standalone use*

## Usage

### Access the Application

**Local:** `http://raspberrypi.local:5000`
**IP Address:** `http://[pi-ip-address]:5000`

### Features

- Browse all 655 scripture lessons
- Play audio for each lesson (Uncle Ray Ramiz voice)
- View age-appropriate visuals
- Filter by age group, language, law number
- Completely offline - no internet required
- Bilingual (English/Turkish)

## Philosophy

**Purpose:** Offline scripture education for all
**Principle:** Purpose Not Performance
**Mission:** No child left behind by digital divide

**Foundation:** We are born a miracle. We deserve to live a miracle.

## Support

For issues or questions:
1. Check `/var/log/scripture-kit.log`
2. Restart service: `sudo systemctl restart scripture-kit`
3. Check status: `sudo systemctl status scripture-kit`

## Updates

To update content:
1. Copy new lesson/audio/image files to respective directories
2. Restart service: `sudo systemctl restart scripture-kit`

No internet connection required - fully offline system.

---

**Package Created:** 2026-01-25T11:33:10.120692
**Version:** 1.0.0
**For:** The Table. For Humanity. Under Father's guidance.
