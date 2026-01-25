/**
 * Unified API Client
 * Centralized API configuration and client setup
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 * 
 * THE MISSION:
 * Connect frontend to backend seamlessly
 * Serve The Table through unified API access
 * 
 * PEACE. LOVE. UNITY.
 */

import axios, { AxiosInstance, AxiosError } from 'axios';

// Get API URL from environment or use default
const getApiUrl = (): string => {
  // In browser, use relative path (Next.js proxy handles it)
  if (typeof window !== 'undefined') {
    return process.env.NEXT_PUBLIC_API_URL || '/api';
  }
  // On server-side, use full URL
  return process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
};

// Create axios instance with default config
export const apiClient: AxiosInstance = axios.create({
  baseURL: getApiUrl(),
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 30000, // 30 second timeout
  withCredentials: true, // Include cookies for auth
});

// Request interceptor - add auth token if available
apiClient.interceptors.request.use(
  (config) => {
    // Add auth token from localStorage if available
    if (typeof window !== 'undefined') {
      const token = localStorage.getItem('auth_token');
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor - handle errors globally
apiClient.interceptors.response.use(
  (response) => {
    return response;
  },
  (error: AxiosError) => {
    // Handle 401 Unauthorized - redirect to login
    if (error.response?.status === 401) {
      if (typeof window !== 'undefined') {
        localStorage.removeItem('auth_token');
        window.location.href = '/login';
      }
    }
    
    // Handle 403 Forbidden - Protocol of Loyalty blocking
    if (error.response?.status === 403) {
      const data = error.response.data as any;
      if (data?.error === "Code that doesn't serve the Table gets purged") {
        console.warn('Protocol of Loyalty: Request blocked -', data.operation);
      }
    }
    
    return Promise.reject(error);
  }
);

// Health check function
export async function checkBackendHealth(): Promise<boolean> {
  try {
    const response = await apiClient.get('/health');
    return response.status === 200;
  } catch (error) {
    console.error('Backend health check failed:', error);
    return false;
  }
}

// Export default instance
export default apiClient;
