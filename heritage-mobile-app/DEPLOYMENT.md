# Deployment Guide

**JAN Ecosystem Mobile App - Production Deployment**

---

## Pre-Deployment Checklist

### ✅ Code Quality
- [x] TypeScript strict mode enabled
- [x] Error boundaries implemented
- [x] Loading states for all async operations
- [x] Empty states for all lists
- [x] Error handling throughout
- [x] Consistent UI components

### ✅ Performance
- [x] Optimized renders with React.memo where needed
- [x] Efficient list rendering
- [x] Image optimization (if applicable)
- [x] Code splitting (Expo handles this)

### ✅ Testing
- [ ] Test on iOS device/simulator
- [ ] Test on Android device/emulator
- [ ] Test offline functionality
- [ ] Test GPS/location features
- [ ] Test map rendering
- [ ] Test share functionality
- [ ] Test navigation flows

### ✅ Configuration
- [ ] Update API base URL for production
- [ ] Configure app.json for production
- [ ] Set up environment variables
- [ ] Configure app icons and splash screens
- [ ] Set up app signing (iOS/Android)

---

## Build for Production

### iOS

```bash
# Install EAS CLI
npm install -g eas-cli

# Login to Expo
eas login

# Configure build
eas build:configure

# Build for iOS
eas build --platform ios

# Or build locally
expo build:ios
```

### Android

```bash
# Build for Android
eas build --platform android

# Or build locally
expo build:android
```

---

## App Store Submission

### iOS App Store

1. **Prepare App Store Connect:**
   - Create app record
   - Set app name, description, keywords
   - Upload screenshots
   - Set pricing and availability

2. **Build and Submit:**
   ```bash
   eas build --platform ios --profile production
   eas submit --platform ios
   ```

3. **Required Information:**
   - App name: "JAN Ecosystem"
   - Subtitle: "Heritage & Community"
   - Description: [See App Store Description below]
   - Keywords: heritage, wonders, community, stewardship
   - Category: Travel, Education
   - Privacy Policy URL
   - Support URL

### Google Play Store

1. **Prepare Google Play Console:**
   - Create app
   - Set app details
   - Upload graphics
   - Set content rating

2. **Build and Submit:**
   ```bash
   eas build --platform android --profile production
   eas submit --platform android
   ```

3. **Required Information:**
   - App name: "JAN Ecosystem"
   - Short description: "Explore heritage sites and connect with community"
   - Full description: [See Play Store Description below]
   - Category: Travel & Local, Education
   - Privacy Policy URL
   - Content rating questionnaire

---

## App Store Descriptions

### App Store (iOS)

**Name:** JAN Ecosystem

**Subtitle:** Heritage & Community

**Description:**

Explore the world's heritage sites and connect with the global community through the JAN Ecosystem mobile app.

**Features:**
- Discover the 7 Wonders of the World with detailed information
- Explore the Seven Pillars and Heritage Meridian System
- View interactive maps with all heritage sites
- Find nearby heritage sites using GPS
- Understand the Shell vs Seed analysis of each site
- Share heritage sites with friends and family
- Get directions to heritage sites
- Works offline with automatic sync

**Mission:**
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS

Download now and join the global heritage community.

### Play Store (Android)

**Name:** JAN Ecosystem

**Short Description:**
Explore heritage sites, find nearby wonders, and connect with the global community.

**Full Description:**

JAN Ecosystem is your gateway to exploring the world's most significant heritage sites. Discover the 7 Wonders of the World, explore the Seven Pillars, and understand the Heritage Meridian System that connects us all.

**Key Features:**

🗺️ **Interactive Maps**
- View all heritage sites on one map
- See meridian connections between sites
- Filter by wonders or pillars
- Toggle between standard and satellite views

📍 **GPS Integration**
- Find nearby heritage sites
- Calculate distance and direction
- Configurable search radius
- Sort by proximity

📱 **Offline Support**
- Works without internet connection
- Automatic data sync when online
- Manual refresh option

🔍 **Detailed Information**
- Full wonder details with Shell vs Seed analysis
- Field resonance indicators
- Meridian connections
- Cultural heritage context

📤 **Share & Navigate**
- Share heritage sites with others
- Get directions via Google Maps
- Native share functionality

**Mission:**
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS

Download now and become part of the global heritage community.

---

## Environment Configuration

### Development

```typescript
// src/api/client.ts
const API_BASE_URL = __DEV__ 
  ? 'http://localhost:8000'
  : 'https://api.yourdomain.com';
```

### Production

Update `src/api/client.ts` with production API URL:

```typescript
const API_BASE_URL = 'https://api.yourdomain.com';
```

---

## Testing Checklist

### Functional Testing
- [ ] App launches successfully
- [ ] All tabs navigate correctly
- [ ] Wonders list loads and displays
- [ ] Wonder detail screen shows all information
- [ ] Map displays all markers
- [ ] GPS nearby sites works
- [ ] Share functionality works
- [ ] Directions open correctly
- [ ] Offline mode works
- [ ] Pull-to-refresh works
- [ ] Error states display correctly

### Performance Testing
- [ ] App loads quickly (< 3 seconds)
- [ ] Lists scroll smoothly
- [ ] Map renders without lag
- [ ] No memory leaks
- [ ] Battery usage is reasonable

### Device Testing
- [ ] iPhone (latest iOS)
- [ ] Android (latest version)
- [ ] Tablet (iPad/Android tablet)
- [ ] Different screen sizes
- [ ] Dark mode (if applicable)

---

## Troubleshooting

### Common Issues

**App won't connect to backend:**
- Check API_BASE_URL in `src/api/client.ts`
- Verify backend is running
- Check network connectivity
- For physical device, use computer's IP address

**GPS not working:**
- Check location permissions
- Verify location services are enabled
- Test on physical device (simulators may have issues)

**Map not displaying:**
- Check Google Maps API key (if required)
- Verify map provider configuration
- Check network connectivity

**Offline mode not working:**
- Verify AsyncStorage permissions
- Check device storage space
- Clear app data and retry

---

## Support

For issues or questions:
- Check documentation in `/docs`
- Review error logs
- Contact development team

---

**Mission:** THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
