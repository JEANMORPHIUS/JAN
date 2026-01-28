# Disk Alignment Checker for C: Drive
# Run this script as Administrator to get full alignment information

Write-Host "=== C: DRIVE ALIGNMENT ANALYSIS ===" -ForegroundColor Cyan
Write-Host ""

# Check if running as administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "WARNING: Not running as Administrator. Some information may be unavailable." -ForegroundColor Yellow
    Write-Host "For complete alignment information, run this script as Administrator." -ForegroundColor Yellow
    Write-Host ""
}

try {
    # Get disk information
    Write-Host "--- DISK INFORMATION ---" -ForegroundColor Green
    $disks = Get-Disk -ErrorAction SilentlyContinue
    if ($disks) {
        foreach ($disk in $disks) {
            $partitions = Get-Partition -DiskNumber $disk.Number -ErrorAction SilentlyContinue | Where-Object {$_.DriveLetter -eq 'C'}
            if ($partitions) {
                Write-Host "Disk Number: $($disk.Number)" -ForegroundColor White
                Write-Host "  Friendly Name: $($disk.FriendlyName)" -ForegroundColor Gray
                Write-Host "  Partition Style: $($disk.PartitionStyle)" -ForegroundColor Gray
                Write-Host "  Logical Sector Size: $($disk.LogicalSectorSize) bytes" -ForegroundColor Gray
                Write-Host "  Physical Sector Size: $($disk.PhysicalSectorSize) bytes" -ForegroundColor Gray
                Write-Host "  Total Size: $([math]::Round($disk.Size / 1GB, 2)) GB" -ForegroundColor Gray
                Write-Host ""
            }
        }
    } else {
        Write-Host "Could not retrieve disk information (requires admin privileges)" -ForegroundColor Red
    }
} catch {
    Write-Host "Error accessing disk information: $_" -ForegroundColor Red
}

try {
    # Get partition information for C: drive
    Write-Host "--- C: DRIVE PARTITION ALIGNMENT ---" -ForegroundColor Green
    $cPartition = Get-Partition -ErrorAction SilentlyContinue | Where-Object {$_.DriveLetter -eq 'C'}
    
    if ($cPartition) {
        foreach ($part in $cPartition) {
            Write-Host "Partition Number: $($part.PartitionNumber)" -ForegroundColor White
            Write-Host "  Disk Number: $($part.DiskNumber)" -ForegroundColor Gray
            Write-Host "  Offset: $($part.Offset) bytes ($([math]::Round($part.Offset / 1MB, 2)) MB)" -ForegroundColor Gray
            Write-Host "  Size: $($part.Size) bytes ($([math]::Round($part.Size / 1GB, 2)) GB)" -ForegroundColor Gray
            Write-Host ""
            
            # Calculate alignment
            $offset = $part.Offset
            $disk = Get-Disk -Number $part.DiskNumber -ErrorAction SilentlyContinue
            
            if ($disk) {
                $logicalSectorSize = $disk.LogicalSectorSize
                $physicalSectorSize = $disk.PhysicalSectorSize
                
                Write-Host "  --- ALIGNMENT ANALYSIS ---" -ForegroundColor Yellow
                
                # Check alignment to logical sectors (typically 512 bytes)
                $logicalAlignment = $offset % $logicalSectorSize
                if ($logicalAlignment -eq 0) {
                    Write-Host "  [OK] Aligned to logical sectors ($logicalSectorSize bytes)" -ForegroundColor Green
                } else {
                    Write-Host "  [X] NOT aligned to logical sectors (offset: $logicalAlignment bytes)" -ForegroundColor Red
                }
                
                # Check alignment to 1MB (recommended for modern drives)
                $oneMB = 1048576
                $mbAlignment = $offset % $oneMB
                if ($mbAlignment -eq 0) {
                    Write-Host "  [OK] Aligned to 1MB boundary (optimal for SSDs)" -ForegroundColor Green
                } else {
                    Write-Host "  [X] NOT aligned to 1MB boundary (offset: $mbAlignment bytes)" -ForegroundColor Red
                }
                
                # Check alignment to physical sectors (typically 4096 bytes for Advanced Format drives)
                if ($physicalSectorSize -gt $logicalSectorSize) {
                    $physicalAlignment = $offset % $physicalSectorSize
                    if ($physicalAlignment -eq 0) {
                        Write-Host "  [OK] Aligned to physical sectors ($physicalSectorSize bytes)" -ForegroundColor Green
                    } else {
                        Write-Host "  [X] NOT aligned to physical sectors (offset: $physicalAlignment bytes)" -ForegroundColor Red
                    }
                }
                
                Write-Host ""
                
                # Visual representation
                Write-Host "  --- VISUAL ALIGNMENT REPRESENTATION ---" -ForegroundColor Yellow
                $sectorsPerMB = $oneMB / $logicalSectorSize
                $offsetInMB = [math]::Floor($offset / $oneMB)
                $offsetInSectors = [math]::Floor($offset / $logicalSectorSize)
                
                Write-Host "  Partition starts at:" -ForegroundColor Gray
                Write-Host "    - Sector: $offsetInSectors" -ForegroundColor Gray
                Write-Host "    - MB boundary: $offsetInMB MB + $mbAlignment bytes" -ForegroundColor Gray
                Write-Host ""
                
                # Show sector grid visualization
                Write-Host "  Sector Alignment Grid (each '|' = 1MB):" -ForegroundColor Gray
                $gridSize = 10
                $startMB = [math]::Max(0, $offsetInMB - 2)
                
                for ($i = 0; $i -lt $gridSize; $i++) {
                    $mbPos = $startMB + $i
                    $mbOffset = $mbPos * $oneMB
                    $isPartitionStart = ($mbOffset -eq $offset)
                    $marker = if ($isPartitionStart) { ">>>C:" } else { "|" }
                    $color = if ($isPartitionStart) { "Green" } else { "DarkGray" }
                    Write-Host "  MB $mbPos : $marker" -ForegroundColor $color
                }
            }
        }
    } else {
        Write-Host "Could not retrieve partition information for C: drive (requires admin privileges)" -ForegroundColor Red
    }
} catch {
    Write-Host "Error accessing partition information: $_" -ForegroundColor Red
}

# Additional alignment recommendations
Write-Host ""
Write-Host "--- ALIGNMENT RECOMMENDATIONS ---" -ForegroundColor Green
Write-Host "• Optimal alignment: Partition offset should be divisible by 1MB (1048576 bytes)" -ForegroundColor White
Write-Host "• For SSDs: 1MB alignment is recommended for best performance" -ForegroundColor White
Write-Host "• For Advanced Format drives (4KB sectors): Alignment to 4096 bytes minimum" -ForegroundColor White
Write-Host "• Modern Windows (Vista+) typically creates 1MB-aligned partitions automatically" -ForegroundColor White
Write-Host ""

if (-not $isAdmin) {
    Write-Host "To get complete information, please run this script as Administrator:" -ForegroundColor Yellow
    Write-Host "  Right-click PowerShell > Run as Administrator" -ForegroundColor Yellow
    Write-Host "  Then run: .\Check-DiskAlignment.ps1" -ForegroundColor Yellow
}
