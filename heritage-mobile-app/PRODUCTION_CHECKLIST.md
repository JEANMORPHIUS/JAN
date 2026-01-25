# Production Deployment Checklist

**Complete checklist for deploying JAN Ecosystem Mobile App to production**

---

## Pre-Deployment (Week 1)

### Configuration
- [ ] Update `src/config/constants.ts` with production API URL
- [ ] Create `.env` file from `.env.example`
- [ ] Set `API_BASE_URL` in `.env`
- [ ] Set `APP_ENV=production` in `.env`
- [ ] Set `DEBUG=false` in `.env`
- [ ] Update `app.json` with correct bundle identifiers
- [ ] Update `eas.json` with project ID
- [ ] Verify all environment variables

### Testing
- [ ] Test on iOS device
- [ ] Test on Android device
- [ ] Test all navigation flows
- [ ] Test API connectivity
- [ ] Test offline mode
- [ ] Test GPS features
- [ ] Test map rendering
- [ ] Test share functionality
- [ ] Test error states
- [ ] Test loading states

### Code Quality
- [ ] Run TypeScript compiler (`tsc --noEmit`)
- [ ] Check for console.log statements (remove in production)
- [ ] Verify error handling
- [ ] Check for memory leaks
- [ ] Review code for security issues

---

## Asset Preparation (Week 1-2)

### App Icons
- [ ] Create iOS app icon (1024x1024)
- [ ] Create Android app icon (512x512)
- [ ] Create adaptive icon foreground
- [ ] Create adaptive icon background
- [ ] Test icons at various sizes
- [ ] Verify icons meet guidelines

### Screenshots
- [ ] Take iOS screenshots (all required sizes)
- [ ] Take Android screenshots (phone and tablet)
- [ ] Optimize screenshot file sizes
- [ ] Verify screenshot quality
- [ ] Organize screenshots in folders

### Other Assets
- [ ] Update splash screen if needed
- [ ] Create feature graphic (Android)
- [ ] Create app preview video (optional)
- [ ] Verify all assets are in correct format

---

## EAS Setup (Week 2)

### Account Setup
- [ ] Create Expo account
- [ ] Install EAS CLI (`npm install -g eas-cli`)
- [ ] Login to EAS (`eas login`)
- [ ] Create EAS project (`eas init`)
- [ ] Update `eas.json` with project ID

### Build Configuration
- [ ] Review `eas.json` configuration
- [ ] Set up iOS provisioning (if needed)
- [ ] Set up Android keystore (if needed)
- [ ] Configure build profiles
- [ ] Test development build

---

## Build Process (Week 2-3)

### iOS Build
- [ ] Run `eas build --platform ios --profile production`
- [ ] Monitor build progress
- [ ] Download iOS build
- [ ] Test iOS build on device
- [ ] Verify iOS build works correctly

### Android Build
- [ ] Run `eas build --platform android --profile production`
- [ ] Monitor build progress
- [ ] Download Android build
- [ ] Test Android build on device
- [ ] Verify Android build works correctly

### Build Verification
- [ ] Test all features on production builds
- [ ] Verify API connectivity
- [ ] Test offline functionality
- [ ] Check performance
- [ ] Verify no crashes

---

## App Store Submission (Week 3)

### iOS App Store
- [ ] Create App Store Connect account (if needed)
- [ ] Create app record in App Store Connect
- [ ] Fill in app information
- [ ] Upload screenshots
- [ ] Write app description
- [ ] Set keywords
- [ ] Set pricing and availability
- [ ] Upload build via EAS (`eas submit --platform ios`)
- [ ] Submit for review
- [ ] Monitor review status

### Google Play Store
- [ ] Create Google Play Console account (if needed)
- [ ] Create app in Play Console
- [ ] Fill in app details
- [ ] Upload screenshots
- [ ] Write app description
- [ ] Complete content rating questionnaire
- [ ] Upload build via EAS (`eas submit --platform android`)
- [ ] Submit for review
- [ ] Monitor review status

---

## Post-Launch (Week 4+)

### Monitoring
- [ ] Set up crash reporting
- [ ] Set up analytics
- [ ] Monitor app store reviews
- [ ] Track user engagement
- [ ] Monitor API performance

### Maintenance
- [ ] Plan version 1.1 features
- [ ] Address user feedback
- [ ] Fix reported bugs
- [ ] Improve performance
- [ ] Update documentation

---

## Quick Reference

### Build Commands
```bash
# Development build
eas build --profile development

# Preview build
eas build --profile preview

# Production build
eas build --platform ios --profile production
eas build --platform android --profile production
```

### Submit Commands
```bash
# Submit to iOS
eas submit --platform ios

# Submit to Android
eas submit --platform android
```

### Testing Commands
```bash
# Start development server
npm start

# Run on iOS simulator
npm run ios

# Run on Android emulator
npm run android
```

---

## Mission Alignment

**"THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS"**

Every step should honor:
- ✅ Community access
- ✅ Heritage preservation
- ✅ Truth and integrity
- ✅ Sacred weight
- ✅ Global connection

---

**Status:** Ready for production deployment  
**Next Action:** Complete pre-deployment checklist

**ENERGY + LOVE = WE ALL WIN**
