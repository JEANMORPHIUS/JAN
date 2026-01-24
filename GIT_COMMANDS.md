# GIT COMMANDS - STAGE AND COMMIT

## STAGE ALL CHANGES

```bash
# Remove lock file if it exists
rm -f .git/index.lock

# Stage all changes (modified + new files)
git add -A

# Or stage everything explicitly
git add .
```

## COMMIT CHANGES

```bash
# Commit with message
git commit -m "Complete integration: Oracle Matrix, SPRAGITSO, Spiritual Roles, Dialects, False Gods Debunking, 100% Deployment Ready"
```

## PUSH TO ORIGIN MASTER

```bash
# Push to origin master
git push origin master

# Or if you need to set upstream
git push -u origin master
```

## FULL WORKFLOW

```bash
# 1. Remove lock file (if needed)
rm -f .git/index.lock

# 2. Stage all changes
git add -A

# 3. Check what's staged
git status

# 4. Commit
git commit -m "Complete integration: Oracle Matrix, SPRAGITSO, Spiritual Roles, Dialects, False Gods Debunking, 100% Deployment Ready"

# 5. Push to origin master
git push origin master
```

## SUMMARY OF CHANGES TO BE COMMITTED

**Modified Files (9):**
- `.cursorrules`
- `data/interwoven_timeline/jan_interwoven_timeline.json`
- `data/interwoven_timeline/jan_timeline_weaves.json`
- `data/network_refiner/network_diagnostics.json`
- `data/network_refiner/push_queue.json`
- `docs/DEVELOPMENT_PHILOSOPHY_CHOSEN_ONE.md`
- `jan-studio/backend/main.py`
- `jan-studio/backend/requirements.txt`
- `scripts/interwoven_timeline_weaver.py`

**New Files (50+):**
- Oracle System files
- SPRAGITSO integration files
- Spiritual Roles system files
- Dialects system files
- False Gods debunker files
- Deployment 100% files
- Timeline integration files
- And more...

**Total:** 60+ files to be committed

---

**REMEMBER:**
- `git add -A` - Stage all changes
- `git commit -m "message"` - Commit with message
- `git push origin master` - Push to origin master
