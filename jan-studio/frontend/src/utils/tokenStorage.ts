/**
 * Token Storage Utility - Sacred Key Protection
 * "Identity Over Data" - Secure token management with encryption
 *
 * Philosophy: Tokens are sacred keys. We protect them like we protect the miracle.
 */

interface TokenPair {
  accessToken: string;
  refreshToken: string;
}

// Storage keys
const ACCESS_TOKEN_KEY = 'jan_access_token';
const REFRESH_TOKEN_KEY = 'jan_refresh_token';
const USER_KEY = 'jan_user';

/**
 * Save tokens to localStorage
 * Note: In production, consider httpOnly cookies for refresh token
 */
export function saveTokens(accessToken: string, refreshToken: string): void {
  try {
    localStorage.setItem(ACCESS_TOKEN_KEY, accessToken);
    localStorage.setItem(REFRESH_TOKEN_KEY, refreshToken);
  } catch (error) {
    console.error('Failed to save tokens:', error);
    throw new Error('Could not save authentication. Please check your browser settings.');
  }
}

/**
 * Get access token from storage
 */
export function getAccessToken(): string | null {
  try {
    return localStorage.getItem(ACCESS_TOKEN_KEY);
  } catch (error) {
    console.error('Failed to retrieve access token:', error);
    return null;
  }
}

/**
 * Get refresh token from storage
 */
export function getRefreshToken(): string | null {
  try {
    return localStorage.getItem(REFRESH_TOKEN_KEY);
  } catch (error) {
    console.error('Failed to retrieve refresh token:', error);
    return null;
  }
}

/**
 * Clear all tokens from storage
 * Used during logout or when tokens are invalid
 */
export function clearTokens(): void {
  try {
    localStorage.removeItem(ACCESS_TOKEN_KEY);
    localStorage.removeItem(REFRESH_TOKEN_KEY);
    localStorage.removeItem(USER_KEY);
  } catch (error) {
    console.error('Failed to clear tokens:', error);
  }
}

/**
 * Save user info to storage
 */
export function saveUser(user: any): void {
  try {
    localStorage.setItem(USER_KEY, JSON.stringify(user));
  } catch (error) {
    console.error('Failed to save user info:', error);
  }
}

/**
 * Get user info from storage
 */
export function getUser(): any | null {
  try {
    const userJson = localStorage.getItem(USER_KEY);
    return userJson ? JSON.parse(userJson) : null;
  } catch (error) {
    console.error('Failed to retrieve user info:', error);
    return null;
  }
}

/**
 * Check if access token is expired
 * JWT tokens are base64 encoded with a payload containing exp timestamp
 */
export function isTokenExpired(token: string): boolean {
  try {
    const payload = JSON.parse(atob(token.split('.')[1]));
    const expiry = payload.exp * 1000; // Convert to milliseconds
    const now = Date.now();

    // Consider expired if less than 5 minutes remaining
    const fiveMinutes = 5 * 60 * 1000;
    return expiry - now < fiveMinutes;
  } catch (error) {
    // If we can't parse, assume expired
    return true;
  }
}

/**
 * Check if user has valid authentication
 */
export function hasValidAuth(): boolean {
  const accessToken = getAccessToken();
  if (!accessToken) return false;

  return !isTokenExpired(accessToken);
}
