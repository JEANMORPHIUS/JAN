# Teacher Setup Guide: JAN Studio on Raspberry Pi

**Complete setup instructions for classroom deployment**

---

## Prerequisites

- Raspberry Pi 5 (8GB RAM recommended)
- MicroSD card (32GB+ recommended)
- Power supply
- Keyboard, mouse, monitor (or headless setup)
- Internet connection (for initial setup)

---

## Step 1: Install Raspberry Pi OS

1. Download Raspberry Pi OS (64-bit) from raspberrypi.org
2. Flash to microSD card using Raspberry Pi Imager
3. Enable SSH and set WiFi (if using headless)
4. Boot the Pi

---

## Step 2: Install JAN Studio

### Option A: Kids Interface (Recommended for Classroom)

```bash
cd ~
git clone <jan-studio-repo>
cd jan-studio/pi
chmod +x install-pi.sh
./install-pi.sh
```

### Option B: Manual Installation

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv git

# Create virtual environment
python3 -m venv ~/jan-venv
source ~/jan-venv/bin/activate

# Install packages
pip install -r requirements-pi.txt
```

---

## Step 3: Configure for Kids Interface

```bash
# Copy kids service
sudo cp jan-studio-kids.service /etc/systemd/system/

# Enable and start
sudo systemctl daemon-reload
sudo systemctl enable jan-studio-kids
sudo systemctl start jan-studio-kids
```

---

## Step 4: Test Installation

1. **Check service status:**
   ```bash
   sudo systemctl status jan-studio-kids
   ```

2. **Access interface:**
   - Open browser: `http://localhost:8000`
   - Or from another device: `http://<pi-ip>:8000`

3. **Test generation:**
   - Create a test persona
   - Generate content
   - Verify it works

---

## Step 5: Network Setup (For Multiple Devices)

### Find Pi IP Address

```bash
hostname -I
```

### Configure Firewall (Optional)

```bash
sudo ufw allow 8000/tcp
```

### Access from Student Devices

Students can access: `http://<pi-ip>:8000`

---

## Step 6: Pre-Download Models (Optional)

Models download automatically, but you can pre-download:

```bash
source ~/jan-venv/bin/activate
python3 -c "from local_ai_service import get_tinyllama; get_tinyllama().load()"
```

This may take 20-30 minutes depending on internet speed.

---

## Step 7: Create Backup

```bash
# Backup SD card (recommended)
sudo dd if=/dev/sdX of=jan-studio-backup.img bs=4M
```

---

## Troubleshooting

### Service Won't Start

```bash
# Check logs
sudo journalctl -u jan-studio-kids -n 50

# Restart service
sudo systemctl restart jan-studio-kids
```

### Can't Access from Other Devices

- Check Pi IP address: `hostname -I`
- Check firewall: `sudo ufw status`
- Check service is running: `sudo systemctl status jan-studio-kids`

### Out of Memory

- Check memory: `free -h`
- Enable swap if needed
- Close other applications

### Models Not Loading

- Check disk space: `df -h`
- Check model directory: `ls -lh ~/.jan-models/`
- Re-download if needed

---

## Classroom Setup Tips

1. **Dedicated Pi:** Use one Pi per classroom or small group
2. **Network Access:** Ensure Pi is on same network as student devices
3. **Bookmark:** Have students bookmark the Pi IP address
4. **Backup Plan:** Have offline activities ready if Pi has issues
5. **Student Accounts:** Consider creating student accounts (future feature)

---

## Maintenance

### Daily

- Check service is running
- Monitor disk space
- Check for updates (optional)

### Weekly

- Review logs for errors
- Clean up old generated content (if needed)
- Backup student work

### Monthly

- Update system packages (optional)
- Check model updates
- Review performance

---

## Support Resources

- **Documentation:** See `README-PI.md` and `KIDS_INTERFACE.md`
- **Troubleshooting:** See `troubleshooting-faq.md`
- **Community:** (Add your support channels)

---

## Quick Reference

```bash
# Start service
sudo systemctl start jan-studio-kids

# Stop service
sudo systemctl stop jan-studio-kids

# View logs
sudo journalctl -u jan-studio-kids -f

# Restart service
sudo systemctl restart jan-studio-kids

# Check status
sudo systemctl status jan-studio-kids
```

---

**Setup Guide Version:** 1.0  
**Last Updated:** 2025-01-27

