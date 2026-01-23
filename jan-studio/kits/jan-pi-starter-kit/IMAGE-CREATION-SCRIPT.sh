#!/bin/bash
# JAN Pi Starter Kit - SD Card Image Creation Script
# Creates a ready-to-ship SD card image

set -e

echo "🎨 JAN Pi Starter Kit - Image Creation"
echo "========================================"
echo ""

# Configuration
IMAGE_NAME="jan-pi-starter-kit-v1.0"
SD_CARD_DEVICE="/dev/sdX"  # CHANGE THIS!
WORK_DIR="/tmp/jan-pi-build"
MOUNT_POINT="/mnt/pi"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}Please run as root (sudo)${NC}"
    exit 1
fi

# Safety check
echo -e "${YELLOW}⚠️  WARNING: This will format ${SD_CARD_DEVICE}${NC}"
read -p "Are you sure? Type 'yes' to continue: " confirm
if [ "$confirm" != "yes" ]; then
    echo "Aborted."
    exit 1
fi

# Step 1: Download Raspberry Pi OS
echo ""
echo "📥 Step 1: Downloading Raspberry Pi OS..."
cd $WORK_DIR
if [ ! -f "raspios.img" ]; then
    # Download latest Raspberry Pi OS Lite (64-bit)
    wget -O raspios.img.xz "https://downloads.raspberrypi.com/raspios_lite_arm64/images/raspios_lite_arm64-YYYY-MM-DD/YYYY-MM-DD-raspios-bookworm-arm64-lite.img.xz"
    unxz raspios.img.xz
fi

# Step 2: Flash to SD card
echo ""
echo "💾 Step 2: Flashing to SD card..."
dd if=raspios.img of=${SD_CARD_DEVICE} bs=4M status=progress
sync

# Step 3: Mount partitions
echo ""
echo "📂 Step 3: Mounting partitions..."
mkdir -p ${MOUNT_POINT}
mount ${SD_CARD_DEVICE}2 ${MOUNT_POINT}  # Root partition
mount ${SD_CARD_DEVICE}1 ${MOUNT_POINT}/boot  # Boot partition

# Step 4: Enable SSH and configure
echo ""
echo "⚙️  Step 4: Configuring system..."
touch ${MOUNT_POINT}/boot/ssh
touch ${MOUNT_POINT}/boot/ssh.txt

# Create first-boot script
cat > ${MOUNT_POINT}/boot/first-boot.sh << 'EOF'
#!/bin/bash
# First boot configuration

# Update system
apt-get update
apt-get upgrade -y

# Install dependencies
apt-get install -y python3 python3-pip python3-venv git build-essential

# Create JAN directory
mkdir -p /home/pi/JAN/Siyem.org
mkdir -p /home/pi/.jan-models

# Set permissions
chown -R pi:pi /home/pi/JAN
chown -R pi:pi /home/pi/.jan-models

# Install JAN Studio
cd /home/pi
git clone <jan-studio-repo> jan-studio
cd jan-studio/pi

# Create virtual environment
python3 -m venv ~/jan-venv
source ~/jan-venv/bin/activate

# Install packages
pip install -r requirements-pi.txt

# Install systemd service
cp jan-studio-kids.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable jan-studio-kids

# Download models (background)
nohup python3 -c "from local_ai_service import get_tinyllama; get_tinyllama().load()" &

# Create example personas
# (Add persona creation scripts here)

# Clean up
rm /boot/first-boot.sh
reboot
EOF

chmod +x ${MOUNT_POINT}/boot/first-boot.sh

# Step 5: Copy documentation
echo ""
echo "📚 Step 5: Copying documentation..."
mkdir -p ${MOUNT_POINT}/home/pi/jan-studio/docs
cp -r ../curriculum/* ${MOUNT_POINT}/home/pi/jan-studio/docs/
cp ../README-PI.md ${MOUNT_POINT}/home/pi/jan-studio/docs/

# Step 6: Copy tutorial videos
echo ""
echo "🎥 Step 6: Copying tutorial videos..."
mkdir -p ${MOUNT_POINT}/home/pi/jan-studio/tutorials
# (Add video files here)

# Step 7: Create example personas
echo ""
echo "👤 Step 7: Creating example personas..."
# (Add persona creation scripts here)

# Step 8: Configure auto-start
echo ""
echo "🚀 Step 8: Configuring auto-start..."
# Service already configured in first-boot script

# Step 9: Unmount
echo ""
echo "📤 Step 9: Unmounting..."
sync
umount ${MOUNT_POINT}/boot
umount ${MOUNT_POINT}

# Step 10: Create image backup
echo ""
echo "💾 Step 10: Creating image backup..."
dd if=${SD_CARD_DEVICE} of=${IMAGE_NAME}.img bs=4M status=progress
gzip ${IMAGE_NAME}.img

echo ""
echo -e "${GREEN}✅ Image creation complete!${NC}"
echo "Image saved as: ${IMAGE_NAME}.img.gz"
echo ""
echo "Next steps:"
echo "1. Test the SD card in a Pi"
echo "2. Verify all functionality"
echo "3. Create production images"
echo "4. Package and ship!"

