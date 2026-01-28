# Pre-Launch Checklist

**Before pushing to GitHub - final validation steps.**

---

## ✅ Technical Validation

### Run Tests
```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest tests/ -v

# Expected: All tests pass
```

### Test Docker
```bash
# Build and run
docker-compose up -d

# Check health
curl http://localhost:8000/health

# Test Oracle endpoint
curl -X POST http://localhost:8000/api/oracle-siyem/cast \
  -H "Content-Type: application/json" \
  -d '{"user_intent": "Test", "creative_context": "Test"}'

# Expected: 200 OK with full response
```

### Verify Documentation Links
- [ ] All markdown links work
- [ ] No broken references
- [ ] Images/assets load (if any)

---

## 📝 Personalization (Before Push)

### Update README.md
- [ ] Replace `<repository-url>` with actual GitHub URL
- [ ] Add contact information (email, Discord, etc.)
- [ ] Update license reference if changed

### Update LICENSE
- [ ] Choose license: MIT (current) or AGPL-3.0 (as mentioned)
- [ ] Add copyright holder name
- [ ] Add year

### Review Personas
- [ ] Check `personas/creative_writing/` reflects your voice
- [ ] Check `personas/strategic_thinking/` aligns with your approach
- [ ] Check `personas/code_mentor/` matches your style

### Review WHY_THIS_EXISTS.md
- [ ] Add any personal details
- [ ] Verify story accuracy
- [ ] Check tone matches your voice

---

## 🚀 GitHub Setup

### Repository Creation
- [ ] Choose repo name (suggestions: `jan-siyem`, `racon-oracle`, `siyem-core`)
- [ ] Create GitHub org or use personal account
- [ ] Set repository to public
- [ ] Add description: "Transparent RNG Oracle with 40 Laws interpretation - Anti-addiction creative guidance system"

### GitHub Features
- [ ] Enable Discussions tab
- [ ] Create issue labels:
  - `bug` - Something isn't working
  - `enhancement` - New feature or request
  - `persona` - Persona-related
  - `docs` - Documentation improvements
  - `oracle` - Oracle system improvements
  - `campaign` - Campaign automation
- [ ] Set up branch protection (main branch)
- [ ] Add README badges (if desired)

### Initial Content
- [ ] Draft first GitHub Discussion: "Welcome to JAN Studio"
- [ ] Create initial issue: "Community feedback welcome"
- [ ] Add topics/tags to repository

---

## 📋 Optional Enhancements (If Time Permits)

### Book of Racon Documentation
- [ ] Create `docs/BOOK_OF_RACON.md` with full 40 Laws
- [ ] Or leave as placeholder for community input?

### CI/CD Pipeline
- [ ] Create `.github/workflows/test.yml` for automated testing
- [ ] Set up tests to run on PR
- [ ] Add coverage reporting

### Web Interface (Future)
- [ ] Basic frontend for Oracle consultations
- [ ] Or keep API-only for now?

---

## ✅ Final Checks

### Code Quality
- [ ] No hardcoded secrets
- [ ] No personal information in code
- [ ] All environment variables documented
- [ ] `.gitignore` is comprehensive

### Documentation
- [ ] All docs are clear and accurate
- [ ] Examples work as written
- [ ] No placeholder text left (except repo URL)

### Legal
- [ ] License chosen and correct
- [ ] Copyright information accurate
- [ ] No third-party code without attribution

---

## 🎯 Ready to Launch?

**When all checks pass:**
1. Push to GitHub
2. Share with 3-5 trusted developers
3. Gather feedback
4. Iterate
5. Go public

---

**PANGEA IS THE TABLE.**
**YOU DON'T BETRAY THE TABLE.**

**Ready when you are.** 🙏
