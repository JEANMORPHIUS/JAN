# JAN Studio Pi - Raspberry Pi 5 Edition

**Optimized version for Raspberry Pi 5 with AI Kit**

---

## Requirements

- **Hardware:** Raspberry Pi 5 (8GB RAM recommended)
- **OS:** Raspberry Pi OS (64-bit)
- **Storage:** 8GB+ free space
- **Network:** Optional (works offline)

---

## Performance Targets

- ✅ Boot to UI: <30 seconds
- ✅ Persona creation: <5 seconds
- ✅ Generation: <1 minute (local model)
- ✅ Fully offline capable
- ✅ Memory: <2GB usage
- ✅ CPU: <80% during generation
- ✅ Storage: <8GB total

---

## Installation

### Quick Install

```bash
cd ~
git clone <jan-studio-repo>
cd jan-studio/pi
chmod +x install-pi.sh
./install-pi.sh
```

### Manual Install

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv git build-essential

# Create virtual environment
python3 -m venv ~/jan-venv
source ~/jan-venv/bin/activate

# Install Python packages
pip install -r requirements-pi.txt

# Create directories
mkdir -p ~/.jan-models
mkdir -p ~/JAN/Siyem.org
```

---

## Models

### Local AI Models

1. **TinyLlama (1B)** - Text generation
   - Size: ~2GB
   - First run downloads automatically
   - Location: `~/.jan-models/tinyllama`

2. **Whisper Tiny** - Speech-to-text
   - Size: ~75MB
   - Location: `~/.jan-models/whisper-tiny`

3. **MusicGen Small** - Audio generation
   - Size: ~1.5GB
   - Location: `~/.jan-models/musicgen-small`

### Model Download

Models download automatically on first use. To pre-download:

```python
from local_ai_service import get_tinyllama, get_whisper, get_musicgen

# Download models
get_tinyllama().load()
get_whisper().load()
get_musicgen().load()
```

---

## Running

### Manual Start

```bash
source ~/jan-venv/bin/activate
cd ~/jan-studio/pi
python3 pi_api.py
```

### Systemd Service (Auto-start)

```bash
# Start service
sudo systemctl start jan-studio-pi

# Enable on boot
sudo systemctl enable jan-studio-pi

# View logs
sudo journalctl -u jan-studio-pi -f

# Stop service
sudo systemctl stop jan-studio-pi
```

### Access UI

Open browser to: `http://localhost:8000`

Or from another device: `http://<pi-ip-address>:8000`

---

## Optimizations

### 1. Lightweight Frontend

- Vanilla JavaScript (no React/Vue)
- Minimal dependencies
- Single HTML file
- <100KB total

### 2. Local AI Models

- TinyLlama (1B) instead of larger models
- 8-bit quantization
- CPU-optimized inference
- Lazy loading

### 3. SQLite Storage

- No external database
- File-based storage
- Minimal overhead

### 4. Resource Limits

Systemd service includes:
- Memory limit: 2GB
- CPU quota: 80%

---

## Performance Monitoring

### Check Stats

```bash
curl http://localhost:8000/api/stats
```

Returns:
```json
{
  "memory": {
    "used_mb": 1200,
    "available_mb": 800,
    "percent": 60.0
  },
  "cpu": {
    "percent": 45.0,
    "count": 4
  },
  "disk": {
    "used_gb": 5.2,
    "free_gb": 2.8
  }
}
```

### Health Check

```bash
curl http://localhost:8000/api/health
```

---

## Troubleshooting

### Out of Memory

```bash
# Check memory usage
free -h

# Reduce model size or use swap
sudo dmesg | grep -i swap
```

### Slow Generation

- Ensure models are loaded (check `/api/health`)
- Reduce `max_length` parameter
- Close other applications
- Check CPU temperature: `vcgencmd measure_temp`

### Model Download Fails

```bash
# Manual download
cd ~/.jan-models
# Download models manually or use git-lfs
```

---

## Offline Mode

JAN Studio Pi works fully offline:

1. Models are stored locally
2. No external API calls
3. SQLite for storage
4. Static frontend

To ensure offline mode:
```bash
# Disable network (optional)
sudo ifconfig wlan0 down
```

---

## Storage Usage

Expected storage:
- OS + dependencies: ~4GB
- Models: ~4GB
- JAN Studio: ~500MB
- **Total: ~8.5GB**

---

## API Endpoints

### Generate Content

```bash
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Write a short story",
    "max_length": 512,
    "temperature": 0.7
  }'
```

### Health Check

```bash
curl http://localhost:8000/api/health
```

### System Stats

```bash
curl http://localhost:8000/api/stats
```

---

## Development

### Run in Development Mode

```bash
source ~/jan-venv/bin/activate
cd ~/jan-studio/pi
uvicorn pi_api:app --reload --host 0.0.0.0 --port 8000
```

### Test Performance

```bash
# Time generation
time curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Test", "max_length": 256}'
```

---

## Status

✅ **Optimized for Pi 5**  
✅ **Lightweight frontend**  
✅ **Local AI models**  
✅ **Systemd service**  
✅ **Performance monitoring**  
✅ **Offline capable**

**Ready for:** Raspberry Pi 5 deployment

---

**Last Updated:** 2025-01-27  
**Version:** 1.0.0-pi

