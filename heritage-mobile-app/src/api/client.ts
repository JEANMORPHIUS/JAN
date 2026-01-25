/**
 * API Client for Heritage Meridian Mobile App
 * Connects to FastAPI backend
 */

import axios from 'axios';

// API Base URL - Change for production
const API_BASE_URL = __DEV__ 
  ? 'http://localhost:8000'  // Development - use your machine's IP for physical device
  : 'https://api.yourdomain.com';  // Production

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for logging
apiClient.interceptors.request.use(
  (config) => {
    console.log(`[API] ${config.method?.toUpperCase()} ${config.url}`);
    return config;
  },
  (error) => {
    console.error('[API] Request error:', error);
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
apiClient.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    console.error('[API] Response error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

export default apiClient;
