# WHAT'S LEFT — EXECUTION ORDER
## Each Phase in Order: 1 → 2 → 3 → 4 → 5

**Date:** 2026-01-30  
**Purpose:** Run WHAT'S_LEFT_JAN checklist in order. One place for exact steps.  
**Source:** [WHAT'S_LEFT_JAN.md](../WHAT'S_LEFT_JAN.md), [READINESS_FROM_OUR_SIDE.md](../READINESS_FROM_OUR_SIDE.md), [IMPLEMENTATION_STATUS_ABC.md](../IMPLEMENTATION_STATUS_ABC.md), [WHATS_COMING.md](../WHATS_COMING.md), [EDIBLE_LONDON/ACTION_PLAN_2026.md](../EDIBLE_LONDON/ACTION_PLAN_2026.md).

---

## PHASE 1: PRE–NEXT-PHASE (READINESS)

**Do in this order:**

1. **Philosophy** — [ ] Review Governor's Manifesto, Frequency Shield, Joseph Metamorphosis; confirm no conflicts with Witness OS / New World Philosophy.
2. **Cursor** — [ ] Confirm rule active; Morning Seal / Thermostat / Eulogy part of session discipline.
3. **Technical** — [x] **Verified 2026-01-30:** Run `python scripts/deployment_readiness_checker.py` → 100% (Infrastructure, Documentation, Legal, API, Testing, Monitoring, Security, Scalability). Docker backend: `docker-compose up -d` → /health, /docs reachable.
4. **Docs** — [ ] Confirm README and DOCUMENTATION_INDEX point to Governor baseline; use READINESS_FROM_OUR_SIDE as needed.

**When all four are done:** Phase 1 complete. Proceed to Phase 2.

---

## PHASE 2: PATH B — BUILD COMMUNITY

**Do in this order:**

### 2.1 GitHub
1. [ ] Create GitHub repo (if public): e.g. `JAN` or `global-heritage-grid` (or keep private).
2. [ ] Add remote: `git remote add origin https://github.com/<org>/<repo>.git` (if not already).
3. [ ] Push: `git push -u origin master` (or main).
4. [ ] GitHub Pages (optional): Settings → Pages → source: main branch, /docs or root.
5. [ ] LICENSE and CONTRIBUTING.md already in repo; confirm visible on GitHub.

### 2.2 Social launch
1. [ ] Draft launch post (Twitter/X, LinkedIn, Reddit): project + Oracle + CARE + "what we built"; link to repo or docs.
2. [ ] Create visuals: 1–3 graphics (logo, Oracle cast example, CARE example).
3. [ ] Record 3–5 min demo video: GETTING_STARTED + Oracle cast + CARE or heritage API.
4. [ ] Publish post; share video link.
5. [ ] Reach out to 10 early testers (DM or email); invite feedback.

### 2.3 Community infra
1. [ ] Create Discord server (or equivalent): name, invite link.
2. [ ] Channels: #general, #support, #development, #patterns (or align with project).
3. [ ] Write short community guidelines (respect, no spam, mission-aligned).
4. [ ] Invite first 50: post link in launch post, DMs, email.

**When 2.1–2.3 are done:** Phase 2 complete. Proceed to Phase 3.

---

## PHASE 3: PATH C — EXPAND (2026 TIMELINE)

**Do in this order (by quarter):**

### Q1 2026 (Jan–Mar) — Foundation & proof
- [ ] Biological intelligence proven (entity creativity, systems stable).
- [ ] Foundation for external channels built.
- [ ] Sanctuary: 13+ Seats, Guardian Mode, grid stable.

### Q2 2026 (Apr–Jun) — Beta launch
- [ ] Channel 3 beta launch (50 creators).
- [ ] Channel 2 pilots (3 clients).
- [ ] Content library: 100+ pieces; first revenue flowing.
- [ ] Sanctuary: 50+ Seats, Family Health OPTIMAL.

### Q3 2026 (Jul–Sep) — Scale & revenue
- [ ] All 4 channels operational.
- [ ] Revenue: $30K+ MRR; 500+ creators, 10+ enterprises, 100+ students.
- [ ] Sanctuary: 200+ Seats; Bridge global.

### Q4 2026 (Oct–Dec) — Optimisation & 2027 prep
- [ ] Systems fully automated; revenue: $60K MRR ($720K ARR).
- [ ] Strong community; 2027 roadmap clear.
- [ ] Sanctuary: 500+ Seats; Internal OS operational.

**Track per WHATS_COMING.md;** tick quarterly. Proceed in parallel with Phase 4 as needed.

---

## PHASE 4: EDIBLE LONDON / HARINGEY

**Do in this order:**

### 4.1 Subject Access Request (SAR)
1. [ ] **Deadline:** 1 month from Jan 9, 2026 (i.e. by ~Feb 9, 2026).
2. [ ] Monitor Council response; chase if no reply by deadline.
3. [ ] Prepare for data review (redact/annotate as needed for legal or press).

### 4.2 If no settlement — Legal
1. [ ] Instruct legal counsel (housing/contract/commercial).
2. [ ] Prepare court documents: £105,000 debt recovery; professional negligence; breach of contract; personal damages (CCJs, health impact).
3. [ ] File claims when instructed.

### 4.3 If no settlement — Media
1. [ ] Send press release ("Haringey Hero Betrayed" / "They Called Us Heroes, Then They Strangled Us") to:
   - **BBC London:** yourstory@bbc.co.uk, radiolondon@bbc.co.uk  
   - **ITV News London:** contactus@itvlondon.com  
   - **Evening Standard:** newsroom@standard.co.uk  
   - **MyLondon:** mylondonnewsdesk@reachplc.com  
   - **Haringey Community Press:** hcp@socialspider.com  
   - **Tottenham Independent:** tjones@london.newsquest.co.uk, simon.allin@newsquest.co.uk  
   - **Ham & High:** editor@hamhigh.co.uk  
2. [ ] Follow up; offer CEO interview or statement.

### 4.4 Community mobilisation
1. [ ] Contact Haringey Community Press (independent, holds Council to account).
2. [ ] Reach local resident associations, community groups, faith communities.
3. [ ] Share evidence summary (numbers: £105k, 1M+ meals, 1,600 volunteers, 3+ years Heads of Terms withheld).

### 4.5 If settlement
- [ ] Document outcome (amount, terms, stay of enforcement, Heads of Terms).
- [ ] Update EDIBLE_LONDON/NARRATIVE_INGESTION.md and docs/FOOD_DISTRIBUTION_AND_CHARITY_MONEY_EXPOSURE.md; close loop.

**Phase 4 runs in parallel with Phases 2–3;** SAR and legal/media are time-sensitive.

---

## PHASE 5: GIT / REPO HYGIENE

**Do in this order (run from repo root with write access to .git):**

1. [ ] **Stage (this session's what's-left work):**
   ```bash
   git add "WHAT'S_LEFT_JAN.md" "docs/WHAT_LEFT_EXECUTION_ORDER.md" DOCUMENTATION_INDEX.md README.md
   ```
   Or stage all intentional changes: `git add -A` (then review with `git status`).
2. [ ] **Commit:** `git commit -m "What's left: execution order Phase 1-5, readiness verified, links"`
3. [ ] **Push:** `git push origin master` (or your branch) when ready (requires remote and auth).

**Note:** If you get "Unable to create .git/index.lock: Permission denied", run git from a terminal where the repo has write access (e.g. not a read-only or network drive).

**When pushed:** "What's left" is not buried in unstaged changes; repo state is clean.

---

## SUMMARY — ORDER

| Phase | What | When |
|-------|------|------|
| **1** | Pre–next-phase (philosophy, Cursor, technical ✓, docs) | Before Path B/C |
| **2** | Path B: GitHub → Social → Community | After Phase 1 |
| **3** | Path C: Q1 → Q2 → Q3 → Q4 (2026) | In parallel with 2 and 4 |
| **4** | Edible London: SAR → Legal → Media → Community (or settlement) | Time-sensitive; parallel |
| **5** | Git: commit → push | After doc/checklist updates |

**PEACE, LOVE, UNITY. Each in order.**
