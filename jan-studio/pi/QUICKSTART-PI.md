# Quick Start - Raspberry Pi 5

**Get JAN Studio Pi running in 5 minutes**

---

## Prerequisites

- Raspberry Pi 5 (8GB RAM recommended)
- Raspberry Pi OS (64-bit)
- Internet connection (for initial setup)

---

## Installation

### 1. Clone Repository

```bash
cd ~
git clone <jan-studio-repo>
cd jan-studio/pi
```

### 2. Run Install Script

```bash
chmod +x install-pi.sh
./install-pi.sh
```

This will:
- Install system dependencies
- Create Python virtual environment
- Install Python packages
- Set up systemd service

### 3. Start Service

```bash
sudo systemctl start jan-studio-pi
```

### 4. Access UI

Open browser: `http://localhost:8000`

---

## First Run

### 1. Check Health

```bash
curl http://localhost:8000/api/health
```

### 2. Test Generation

```bash
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello, world!", "max_length": 100}'
```

### 3. Models Download

Models download automatically on first use. This may take 10-30 minutes depending on internet speed.

---

## Performance Test

Run performance tests:

```bash
source ~/jan-venv/bin/activate
python3 test_performance.py
```

Expected results:
- ✅ Boot time: <30s
- ✅ Persona creation: <5s
- ✅ Generation: <60s
- ✅ Memory: <2GB
- ✅ CPU: <80%

---

## Troubleshooting

### Service Won't Start

```bash
# Check logs
sudo journalctl -u jan-studio-pi -n 50

# Check status
sudo systemctl status jan-studio-pi
```

### Out of Memory

```bash
# Check memory
free -h

# Enable swap (if needed)
sudo dmesg | grep -i swap
```

### Models Not Loading

```bash
# Check model directory
ls -lh ~/.jan-models/

# Manual download (if needed)
source ~/jan-venv/bin/activate
python3 -c "from local_ai_service import get_tinyllama; get_tinyllama().load()"
```

---

## Auto-Start on Boot

Service is enabled by default. To disable:

```bash
sudo systemctl disable jan-studio-pi
```

---

## Access from Other Devices

Find Pi IP address:

```bash
hostname -I
```

Access from browser: `http://<pi-ip>:8000`

---

## Next Steps

- Create your first persona
- Generate content
- Check system stats
- Customize configuration

---

**Ready to use!** 🚀

