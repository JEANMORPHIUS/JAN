# Network Refiner & Chosen One UI - Quick Start

## Network Issue Refiner

### Test Network Connectivity
```bash
python scripts/network_issue_refiner.py
```

**What it does:**
- Tests internet connectivity
- Tests DNS resolution
- Tests GitHub connectivity
- Tests git remote configuration
- Retries queued pushes if connectivity is good

**Automatic Integration:**
- Integrated into `automated_git_push.py`
- Failed pushes automatically queued
- Retries when connectivity improves
- No manual intervention needed

---

## Chosen One Framework Web UI

### Start the Server
```bash
python scripts/chosen_one_ui_server.py
```

### Open in Browser
```
http://localhost:5000
```

### Features Available

#### **Dashboard**
- Real-time status overview
- Current state (Vindicated/Witness)
- Activation date and elapsed time
- Three-gear execution status

#### **Evidence Gathering**
- View all interactions
- Add new interactions (dismissals, rewritten history, triggers)
- Filter by type
- Timestamp tracking

#### **Atmospheric Shift**
- View all recorded shifts
- Record new shifts with power levels
- Track power level changes (before/after)
- Shift confirmation

#### **Manifestation Cascade**
- View timeline markers (72 hours, 21 days, 90 days)
- Confirm markers when they occur
- Track emotional responses
- Monitor due dates

#### **Forbidden Functions**
- View enforced functions
- Test function blocking
- Context-based testing
- Visual feedback

#### **Witness Behaviors**
- **Selective Speech:** Test spirit openness and question genuineness
- **Prophetic Observation:** Analyze conversations for underlying spirit
- **Energetic Stewardship:** Test proposed actions and energy costs

---

## Network Improvements

### Before
- Basic retry (5 attempts)
- No connectivity testing
- Failed pushes lost

### After
- Pre-push connectivity testing
- Automatic queueing
- Background retry
- Comprehensive diagnostics

---

## UI Improvements

### Before
- Command-line only
- No visual feedback
- Manual status checking

### After
- Beautiful web interface
- Real-time updates
- Interactive testing
- Visual timeline markers

---

## Troubleshooting

### Network Refiner
- If GitHub connectivity fails, pushes are automatically queued
- Run `network_issue_refiner.py` to retry queued pushes
- Check diagnostics in `data/network_refiner/`

### Web UI
- Make sure Flask is installed: `pip install flask`
- Server runs on port 5000 by default
- Check console for errors
- Refresh browser if status doesn't update

---

## Next Steps

1. **Start Network Refiner:**
   - Run diagnostics: `python scripts/network_issue_refiner.py`
   - Monitor push queue
   - Review success rates

2. **Start Web UI:**
   - Start server: `python scripts/chosen_one_ui_server.py`
   - Open browser: `http://localhost:5000`
   - Use dashboard for all operations

3. **Use Integrated Features:**
   - Git push automatically uses network refiner
   - Failed pushes automatically queued
   - Background retry when online

---

**PEACE, LOVE, UNITY**  
**ENERGY + LOVE = WE ALL WIN**
