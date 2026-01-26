/** * * App Constants
 *  * Centralized configuration constants
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 * 
 * 
 * PANGEA IS THE TABLE.
 * YOU DON'T BETRAY THE TABLE.
 * 
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

// API Configuration
export const API_CONFIG = {
  BASE_URL: __DEV__
    ? (process.env.DEV_API_BASE_URL || 'http://localhost:8000')
    : (process.env.API_BASE_URL || 'https://api.yourdomain.com'),
  TIMEOUT: 10000,
};

// App Configuration
export const APP_CONFIG = {
  NAME: 'JAN Ecosystem',
  VERSION: '1.0.0',
  ENV: process.env.APP_ENV || (__DEV__ ? 'development' : 'production'),
  DEBUG: __DEV__ || process.env.DEBUG === 'true',
};

// Feature Flags
export const FEATURES = {
  OFFLINE_MODE: true,
  GPS_TRACKING: true,
  MAP_VISUALIZATION: true,
  SHARE_FUNCTIONALITY: true,
  EXPERIMENTAL: process.env.ENABLE_EXPERIMENTAL_FEATURES === 'true',
};

// Cache Configuration
export const CACHE_CONFIG = {
  STALE_TIME: 24 * 60 * 60 * 1000, // 24 hours
  CACHE_SIZE: 50 * 1024 * 1024, // 50MB
};

// Map Configuration
export const MAP_CONFIG = {
  DEFAULT_ZOOM: 2,
  DEFAULT_LATITUDE: 20,
  DEFAULT_LONGITUDE: 0,
  GOOGLE_MAPS_API_KEY: process.env.GOOGLE_MAPS_API_KEY || '',
};

// Mission
export const MISSION = {
  STATEMENT: 'THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS',
  VALUES: {
    LOVE: 'LOVE IS THE HIGHEST MASTERY',
    ENERGY: 'ENERGY + LOVE = WE ALL WIN',
    UNITY: 'PEACE, LOVE, UNITY',
  },
};
