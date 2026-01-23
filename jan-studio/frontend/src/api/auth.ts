/**
 * Authentication API Client
 * Handles all auth-related API calls with Duygu Adami error messages
 *
 * Philosophy: "Identity Over Data" - Treat every user as a sacred key
 */

import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

// ============================================================================
// Types
// ============================================================================

export interface RegisterRequest {
  username: string;
  email: string;
  password: string;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface TokenResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
  expires_in: number;
}

export interface User {
  id: number;
  username: string;
  email: string;
  is_admin: boolean;
  created_at: string;
}

export interface AuthError {
  message: string;      // Duygu Adami message for user
  technical: string;    // Technical detail for debugging
  code?: number;        // HTTP status code
}

// ============================================================================
// Error Translation (Technical → Duygu Adami)
// ============================================================================

function translateError(error: any): AuthError {
  // Network errors
  if (!error.response) {
    return {
      message: "Can't reach the lighthouse. Check your connection.",
      technical: error.message || 'Network error',
    };
  }

  const status = error.response.status;
  const detail = error.response.data?.detail || '';

  // Status-based translation
  switch (status) {
    case 401:
      if (detail.includes('email') || detail.includes('password')) {
        return {
          message: "The key didn't quite turn, mate. Give it another go.",
          technical: detail,
          code: status,
        };
      }
      if (detail.includes('expired')) {
        return {
          message: "Your session has ended. Let's get you back in.",
          technical: detail,
          code: status,
        };
      }
      return {
        message: "The key didn't quite turn, mate. Give it another go.",
        technical: detail,
        code: status,
      };

    case 403:
      if (detail.includes('inactive')) {
        return {
          message: "The door is closed for now. Reach out if you need help.",
          technical: detail,
          code: status,
        };
      }
      return {
        message: "That door isn't open to you yet. Reach out if you need access.",
        technical: detail,
        code: status,
      };

    case 409:
      if (detail.includes('email')) {
        return {
          message: "That identity is already part of the community.",
          technical: detail,
          code: status,
        };
      }
      if (detail.includes('username')) {
        return {
          message: "That name's already taken. Try another?",
          technical: detail,
          code: status,
        };
      }
      return {
        message: "That's already taken. Try something else?",
        technical: detail,
        code: status,
      };

    case 422:
      // Validation errors - try to be specific
      if (detail.includes('password')) {
        return {
          message: "Strengthen your key: needs uppercase, lowercase, and a number.",
          technical: detail,
          code: status,
        };
      }
      if (detail.includes('username')) {
        return {
          message: "A bit more, mate. At least 3 characters.",
          technical: detail,
          code: status,
        };
      }
      return {
        message: "Not quite right. Check your details and try again.",
        technical: detail,
        code: status,
      };

    case 500:
      return {
        message: "The lighthouse is flickering. Try again in a moment.",
        technical: detail || 'Internal server error',
        code: status,
      };

    default:
      return {
        message: "Something's not quite right. Give it another try?",
        technical: detail || 'Unknown error',
        code: status,
      };
  }
}

// ============================================================================
// API Functions
// ============================================================================

/**
 * Register a new user account
 */
export async function register(data: RegisterRequest): Promise<User> {
  try {
    const response = await axios.post<User>(
      `${API_URL}/api/auth/register`,
      data,
      {
        headers: { 'Content-Type': 'application/json' },
      }
    );
    return response.data;
  } catch (error) {
    throw translateError(error);
  }
}

/**
 * Login with email and password
 */
export async function login(data: LoginRequest): Promise<TokenResponse> {
  try {
    const response = await axios.post<TokenResponse>(
      `${API_URL}/api/auth/login`,
      data,
      {
        headers: { 'Content-Type': 'application/json' },
      }
    );
    return response.data;
  } catch (error) {
    throw translateError(error);
  }
}

/**
 * Get current user information
 */
export async function getCurrentUser(accessToken: string): Promise<User> {
  try {
    const response = await axios.get<User>(
      `${API_URL}/api/auth/me`,
      {
        headers: {
          'Authorization': `Bearer ${accessToken}`,
        },
      }
    );
    return response.data;
  } catch (error) {
    throw translateError(error);
  }
}

/**
 * Refresh access token using refresh token
 */
export async function refreshToken(refreshToken: string): Promise<TokenResponse> {
  try {
    const response = await axios.post<TokenResponse>(
      `${API_URL}/api/auth/refresh`,
      { refresh_token: refreshToken },
      {
        headers: { 'Content-Type': 'application/json' },
      }
    );
    return response.data;
  } catch (error) {
    throw translateError(error);
  }
}

/**
 * Logout (invalidate refresh token)
 */
export async function logout(
  accessToken: string,
  refreshToken: string
): Promise<void> {
  try {
    await axios.post(
      `${API_URL}/api/auth/logout`,
      { refresh_token: refreshToken },
      {
        headers: {
          'Authorization': `Bearer ${accessToken}`,
          'Content-Type': 'application/json',
        },
      }
    );
  } catch (error) {
    // Don't throw on logout errors - always clear local state
    console.error('Logout API error:', error);
  }
}

/**
 * Check if token is expired or about to expire
 */
export function isTokenExpiringSoon(expiresIn: number): boolean {
  // Refresh if less than 5 minutes remaining
  return expiresIn < 300;
}

/**
 * Check if error is authentication-related (401/403)
 */
export function isAuthError(error: AuthError): boolean {
  return error.code === 401 || error.code === 403;
}
