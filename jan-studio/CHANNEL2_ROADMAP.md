# Channel 2: Creator Platform - Implementation Roadmap

**Target Users:** Social media creators, content creators, non-technical users
**Focus:** Creator experience, marketplace, payments
**Status:** Architecture Complete, Implementation in Progress

---

## Current State Analysis

### ✅ What's Already Built (Architecture Complete)

**Backend (marketplace_db.py, marketplace_api.py):**
- ✅ Complete database schema (users, personas, files, downloads, ratings)
- ✅ User management (create user, get by username)
- ✅ Persona CRUD operations
- ✅ File storage and versioning
- ✅ Download tracking
- ✅ Rating system with averages
- ✅ Category filtering
- ✅ Sorting (downloads, rating, date)
- ✅ RESTful API endpoints

**Frontend (marketplace pages):**
- ✅ Browse marketplace UI (`/marketplace/index.tsx`)
- ✅ Persona detail page (`/marketplace/[id].tsx`)
- ✅ Submit persona form (`/marketplace/submit.tsx`)
- ✅ API client (marketplace.ts)
- ✅ Category filtering
- ✅ Sorting options
- ✅ Rating display and submission
- ✅ Download functionality
- ✅ Responsive grid layout

**Key Strengths:**
- Solid database architecture
- Clean API design
- Complete persona lifecycle (submit → review → download)
- Rating and review system
- File versioning support

---

## ⚠️ What's Missing (Implementation Needed)

### Priority 1: User Authentication ⭐⭐⭐
**Status:** Not implemented
**Blocking:** Everything else

**Current State:**
- Users are created ad-hoc when submitting personas
- No login/logout
- No session management
- No user profiles
- Username/email entered manually each time

**Needed:**
1. Authentication system (OAuth or email/password)
2. Session management
3. Login/logout pages
4. Protected routes
5. User context/state management

---

### Priority 2: Creator Dashboard ⭐⭐⭐
**Status:** Not implemented
**Blocking:** Creator experience

**Current State:**
- No way to see "my personas"
- No way to see "my purchases"
- No sales analytics
- No persona management

**Needed:**
1. Dashboard page (`/dashboard`)
2. My personas list
3. My purchases list
4. Basic analytics (views, downloads, ratings)
5. Edit/update persona functionality
6. Delete persona functionality

---

### Priority 3: Payment System ⭐⭐
**Status:** Not implemented
**Blocking:** Monetization

**Current State:**
- All personas are free
- No pricing field in database
- No payment processing
- No revenue split

**Needed:**
1. Pricing field in persona schema
2. Stripe integration
3. Purchase flow
4. Transaction management
5. Revenue split logic (70/30)
6. Payout system

---

### Priority 4: Content Generation UI ⭐
**Status:** Basic placeholder exists
**Blocking:** End-user experience

**Current State:**
- Generation API exists (jan_generation_api.py)
- No dedicated UI for creators
- Complex for non-technical users

**Needed:**
1. Simple generation interface
2. Template selection
3. Parameter inputs
4. Generation history
5. Save/export results

---

## Implementation Phases

### Phase 1: Foundation (Weeks 1-2) 🔴 CURRENT PRIORITY

**Goal:** Enable user accounts and basic creator workflows

#### Week 1: Authentication System

**Tasks:**
1. **Choose Auth Strategy**
   - Option A: NextAuth.js (OAuth + email)
   - Option B: Custom JWT (simpler, faster)
   - Recommendation: **Option B for MVP, upgrade later**

2. **Backend Auth API** (`auth_api.py`)
   ```python
   POST /api/auth/register
   POST /api/auth/login
   POST /api/auth/logout
   GET  /api/auth/me
   POST /api/auth/refresh
   ```

3. **Frontend Auth Pages**
   - `/login` - Login form
   - `/register` - Registration form
   - `/auth/callback` - OAuth callback (if using OAuth)

4. **Auth Context**
   - React context for user state
   - Protected route wrapper
   - Token management

5. **Database Updates**
   - Add password_hash to users table
   - Add refresh_tokens table
   - Add email_verified field

#### Week 2: Basic Creator Dashboard

**Tasks:**
1. **Dashboard Page** (`/dashboard`)
   - Layout with sidebar navigation
   - Overview stats (personas, downloads, ratings)
   - Quick actions

2. **My Personas Section** (`/dashboard/personas`)
   - List of created personas
   - Status indicators (pending, approved, rejected)
   - Edit/delete buttons

3. **My Purchases Section** (`/dashboard/purchases`)
   - List of downloaded personas
   - Re-download functionality
   - Purchase history

4. **User Profile** (`/dashboard/profile`)
   - Edit username, email
   - Avatar upload (optional)
   - Bio/description

5. **Backend APIs**
   ```python
   GET  /api/users/me/personas
   GET  /api/users/me/purchases
   PUT  /api/users/me/profile
   ```

---

### Phase 2: Marketplace Core (Weeks 3-4)

**Goal:** Complete the marketplace experience

#### Week 3: Enhanced Discovery

**Tasks:**
1. **Search Functionality**
   - Full-text search on name, description
   - Search bar in marketplace
   - Search API endpoint

2. **Advanced Filtering**
   - Multiple categories
   - Rating threshold
   - Download count ranges
   - Date ranges

3. **Persona Preview**
   - Sample output/screenshots
   - Preview without download
   - Demo mode

4. **Collections/Tags**
   - Tag system for personas
   - Curated collections
   - Trending section

#### Week 4: Persona Management

**Tasks:**
1. **Update Persona**
   - Version bumping
   - Changelog
   - Update notification to users

2. **Persona Analytics**
   - View count tracking
   - Download analytics
   - Rating trends
   - User engagement metrics

3. **Moderation Tools**
   - Admin dashboard (`/admin`)
   - Approve/reject personas
   - Flag content
   - User reports

---

### Phase 3: Payments (Weeks 5-6)

**Goal:** Enable monetization

#### Week 5: Stripe Integration

**Tasks:**
1. **Stripe Setup**
   - Stripe account configuration
   - API keys in .env
   - Webhook endpoints

2. **Database Schema**
   ```sql
   ALTER TABLE personas ADD COLUMN price DECIMAL(10,2) DEFAULT 0.00;

   CREATE TABLE transactions (
     id INTEGER PRIMARY KEY,
     user_id INTEGER,
     persona_id INTEGER,
     amount DECIMAL(10,2),
     stripe_payment_id TEXT,
     status TEXT,
     created_at TIMESTAMP
   );

   CREATE TABLE payouts (
     id INTEGER PRIMARY KEY,
     creator_id INTEGER,
     amount DECIMAL(10,2),
     stripe_payout_id TEXT,
     status TEXT,
     created_at TIMESTAMP
   );
   ```

3. **Payment API**
   ```python
   POST /api/payments/create-checkout
   POST /api/payments/webhook
   GET  /api/payments/history
   ```

4. **Checkout Flow**
   - Stripe Checkout integration
   - Success/cancel pages
   - Receipt email

#### Week 6: Revenue Management

**Tasks:**
1. **Revenue Split Logic**
   - 70% to creator
   - 30% platform fee
   - Calculation and tracking

2. **Payout System**
   - Creator balance tracking
   - Minimum payout threshold
   - Stripe Connect for payouts

3. **Financial Dashboard**
   - Earnings overview
   - Transaction history
   - Payout requests
   - Tax documents (1099, etc.)

---

### Phase 4: Polish (Weeks 7-8)

**Goal:** Enhanced user experience

#### Week 7: Reviews and Social

**Tasks:**
1. **Enhanced Reviews**
   - Verified purchase badge
   - Helpful votes on reviews
   - Report inappropriate reviews
   - Creator responses

2. **Social Features**
   - Follow creators
   - Notifications
   - Activity feed
   - Creator profiles

3. **Recommendations**
   - Similar personas
   - "Users also downloaded"
   - Personalized recommendations

#### Week 8: Content Generation UI

**Tasks:**
1. **Generation Interface** (`/generate`)
   - Select persona
   - Choose template
   - Fill parameters
   - Generate content

2. **History Management**
   - Save generations
   - Re-run with different params
   - Export history

3. **Batch Operations**
   - Generate multiple
   - Schedule generations
   - Templates for common tasks

---

## Technical Architecture

### Authentication Flow

```
┌─────────────┐
│   Browser   │
└─────┬───────┘
      │ 1. POST /auth/login
      │    {email, password}
      ▼
┌─────────────┐
│   Backend   │
│  auth_api   │
└─────┬───────┘
      │ 2. Verify credentials
      │ 3. Generate JWT
      │
      │ 4. Return tokens
      ▼    {access_token, refresh_token}
┌─────────────┐
│   Browser   │
│ Store token │
└─────┬───────┘
      │ 5. Include in headers
      │    Authorization: Bearer <token>
      ▼
┌─────────────┐
│   Backend   │
│ Protected   │
│ Endpoints   │
└─────────────┘
```

### Payment Flow

```
┌─────────────┐
│   User      │
│ Select paid │
│  persona    │
└─────┬───────┘
      │ 1. Click "Purchase"
      ▼
┌─────────────┐
│  Frontend   │
│ Create      │
│ checkout    │
└─────┬───────┘
      │ 2. POST /payments/create-checkout
      ▼
┌─────────────┐
│  Backend    │
│ Create      │
│ Stripe      │
│ session     │
└─────┬───────┘
      │ 3. Return session_url
      ▼
┌─────────────┐
│  Stripe     │
│  Checkout   │
└─────┬───────┘
      │ 4. Payment success
      │ 5. Webhook to backend
      ▼
┌─────────────┐
│  Backend    │
│ Record      │
│ transaction │
│ Grant access│
└─────┬───────┘
      │ 6. Redirect to success
      ▼
┌─────────────┐
│  User       │
│ Download    │
│ persona     │
└─────────────┘
```

### Database Schema Extensions

```sql
-- Current tables (already implemented)
users
personas
persona_files
downloads
ratings

-- New tables needed

CREATE TABLE auth_tokens (
  id INTEGER PRIMARY KEY,
  user_id INTEGER NOT NULL,
  token_hash TEXT NOT NULL,
  refresh_token_hash TEXT,
  expires_at TIMESTAMP NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE transactions (
  id INTEGER PRIMARY KEY,
  buyer_id INTEGER NOT NULL,
  seller_id INTEGER NOT NULL,
  persona_id INTEGER NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  platform_fee DECIMAL(10,2) NOT NULL,
  creator_revenue DECIMAL(10,2) NOT NULL,
  stripe_payment_id TEXT UNIQUE,
  status TEXT NOT NULL, -- pending, completed, refunded
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (buyer_id) REFERENCES users(id),
  FOREIGN KEY (seller_id) REFERENCES users(id),
  FOREIGN KEY (persona_id) REFERENCES personas(id)
);

CREATE TABLE user_purchases (
  id INTEGER PRIMARY KEY,
  user_id INTEGER NOT NULL,
  persona_id INTEGER NOT NULL,
  transaction_id INTEGER,
  purchased_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (persona_id) REFERENCES personas(id),
  FOREIGN KEY (transaction_id) REFERENCES transactions(id),
  UNIQUE(user_id, persona_id)
);

CREATE TABLE payouts (
  id INTEGER PRIMARY KEY,
  creator_id INTEGER NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  stripe_payout_id TEXT UNIQUE,
  status TEXT NOT NULL, -- pending, processing, paid, failed
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  paid_at TIMESTAMP,
  FOREIGN KEY (creator_id) REFERENCES users(id)
);

CREATE TABLE user_profiles (
  user_id INTEGER PRIMARY KEY,
  bio TEXT,
  avatar_url TEXT,
  website TEXT,
  social_links TEXT, -- JSON
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE persona_tags (
  id INTEGER PRIMARY KEY,
  persona_id INTEGER NOT NULL,
  tag TEXT NOT NULL,
  FOREIGN KEY (persona_id) REFERENCES personas(id),
  UNIQUE(persona_id, tag)
);

CREATE TABLE user_follows (
  id INTEGER PRIMARY KEY,
  follower_id INTEGER NOT NULL,
  following_id INTEGER NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (follower_id) REFERENCES users(id),
  FOREIGN KEY (following_id) REFERENCES users(id),
  UNIQUE(follower_id, following_id)
);
```

---

## File Structure

### New Backend Files

```
jan-studio/backend/
├── auth_api.py              # NEW: Authentication endpoints
├── auth_utils.py            # NEW: JWT, password hashing
├── dashboard_api.py         # NEW: Dashboard endpoints
├── payment_api.py           # NEW: Stripe integration
├── user_api.py              # NEW: User profile endpoints
├── admin_api.py             # NEW: Admin/moderation
├── middleware.py            # NEW: Auth middleware
└── config.py                # NEW: App configuration
```

### New Frontend Files

```
jan-studio/frontend/src/
├── pages/
│   ├── login.tsx            # NEW: Login page
│   ├── register.tsx         # NEW: Registration page
│   ├── dashboard/
│   │   ├── index.tsx        # NEW: Dashboard home
│   │   ├── personas.tsx     # NEW: My personas
│   │   ├── purchases.tsx    # NEW: My purchases
│   │   ├── earnings.tsx     # NEW: Financial dashboard
│   │   └── profile.tsx      # NEW: Edit profile
│   ├── admin/
│   │   └── index.tsx        # NEW: Admin dashboard
│   └── generate/
│       └── index.tsx        # NEW: Generation UI
├── components/
│   ├── AuthProvider.tsx     # NEW: Auth context
│   ├── ProtectedRoute.tsx   # NEW: Route guard
│   ├── UserMenu.tsx         # NEW: User dropdown menu
│   └── PaymentButton.tsx    # NEW: Stripe checkout
└── api/
    ├── auth.ts              # NEW: Auth API client
    ├── dashboard.ts         # NEW: Dashboard API
    ├── payments.ts          # NEW: Payment API
    └── users.ts             # NEW: User API
```

---

## Quick Wins (Can Do Now)

### 1. Add Price Field (30 min)
**Impact:** High (enables paid personas)

```python
# In marketplace_db.py
cursor.execute("""
    ALTER TABLE personas ADD COLUMN price DECIMAL(10,2) DEFAULT 0.00
""")
```

### 2. Add User Dashboard Link (15 min)
**Impact:** Medium (improves navigation)

```tsx
// In _app.tsx or header component
<Link href="/dashboard">My Dashboard</Link>
```

### 3. Add Persona Edit Button (45 min)
**Impact:** Medium (creator convenience)

```tsx
// In dashboard/personas.tsx
<Link href={`/dashboard/personas/${persona.id}/edit`}>
  <button>Edit</button>
</Link>
```

### 4. Add Search Placeholder (30 min)
**Impact:** Low (UX improvement)

```tsx
// In marketplace/index.tsx
<input
  type="search"
  placeholder="Search personas..."
  onChange={handleSearch}
/>
```

---

## Success Metrics

### Phase 1 (Weeks 1-2)
- ✅ User registration works
- ✅ Login/logout works
- ✅ Dashboard shows user data
- ✅ Protected routes working

### Phase 2 (Weeks 3-4)
- ✅ Search returns relevant results
- ✅ Users can edit their personas
- ✅ Analytics display correctly
- ✅ Admins can moderate

### Phase 3 (Weeks 5-6)
- ✅ Stripe checkout completes
- ✅ Transactions recorded correctly
- ✅ Revenue split calculated correctly
- ✅ Payouts can be requested

### Phase 4 (Weeks 7-8)
- ✅ Reviews are helpful
- ✅ Social features engage users
- ✅ Generation UI is intuitive
- ✅ History saves correctly

---

## Risk Mitigation

### Authentication Risk
**Risk:** Security vulnerabilities
**Mitigation:**
- Use bcrypt for passwords (already in Python)
- JWT with short expiry
- HTTPS only in production
- Rate limiting on auth endpoints

### Payment Risk
**Risk:** Financial errors, fraud
**Mitigation:**
- Use Stripe (handles compliance)
- Test mode first
- Webhook signature verification
- Idempotency keys
- Comprehensive logging

### Data Risk
**Risk:** Data loss, corruption
**Mitigation:**
- Database backups
- Transaction rollback on errors
- Foreign key constraints
- Validation at API level

---

## Next Steps (Immediate)

**This Week:**
1. Review and approve this roadmap
2. Choose authentication strategy
3. Set up development environment
4. Create auth_api.py stub

**Next Week:**
1. Implement auth endpoints
2. Create login/register pages
3. Add auth middleware
4. Test authentication flow

---

**Version:** 1.0
**Created:** 2026-01-13
**Status:** Ready for Review
**Owner:** Channel 2 - Creator Platform Team
