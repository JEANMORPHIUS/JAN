/** * * Authentication Context - The Sacred Key
 *  * "Identity Over Data" - Secure authentication state management
 *  *
 *  * Philosophy: Every user is a miracle. Protect their keys with dignity.
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 * 
 * THE MISSION:
 * THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
 * LOVE IS THE HIGHEST MASTERY
 * ENERGY + LOVE = WE ALL WIN
 * PEACE, LOVE, UNITY
 * 
 * PANGEA IS THE TABLE.
 * YOU DON'T BETRAY THE TABLE.
 * 
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { User, TokenResponse, register as registerUser, login as loginUser, getCurrentUser, logout as logoutUser, refreshToken } from '../api/auth';
import { saveTokens, getAccessToken, getRefreshToken, clearTokens, saveUser, getUser, isTokenExpired } from '../utils/tokenStorage';

interface AuthContextType {
  user: User | null | Partial<User>; // Irregular Form: Support flexible user shapes
  loading: boolean;
  isAuthenticated: boolean;
  login: (email: string, password: string) => Promise<void>;
  register: (username: string, email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  refreshAccessToken: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  // Load user from token on mount
  useEffect(() => {
    loadUser();
  }, []);

  // Auto-refresh token before expiry
  useEffect(() => {
    if (!user) return;

    const interval = setInterval(() => {
      const accessToken = getAccessToken();
      if (accessToken && isTokenExpired(accessToken)) {
        refreshAccessToken().catch(() => {
          // Refresh failed, user will be logged out
        });
      }
    }, 60000); // Check every minute

    return () => clearInterval(interval);
  }, [user]);

  /**
   * Load user from stored token
   */
  async function loadUser() {
    try {
      // Try to load cached user first
      const cachedUser = getUser();
      const accessToken = getAccessToken();

      if (!accessToken) {
        setLoading(false);
        return;
      }

      // If token is expired, try to refresh
      if (isTokenExpired(accessToken)) {
        await refreshAccessToken();
        // After refresh, get new token
        const newToken = getAccessToken();
        if (newToken) {
          const userData = await getCurrentUser(newToken);
          setUser(userData);
          saveUser(userData);
        }
      } else {
        // Token valid, use cached user or fetch fresh
        if (cachedUser) {
          setUser(cachedUser);
        } else {
          const userData = await getCurrentUser(accessToken);
          setUser(userData);
          saveUser(userData);
        }
      }
    } catch (error) {
      // Token invalid, clear storage
      clearTokens();
    } finally {
      setLoading(false);
    }
  }

  /**
   * Register a new user
   * After success, auto-login to create seamless onboarding
   */
  async function register(username: string, email: string, password: string) {
    try {
      await registerUser({ username, email, password });
      // After registration, automatically log in
      await login(email, password);
    } catch (error: any) {
      // Error already translated to Duygu Adami in auth.ts
      throw error;
    }
  }

  /**
   * Login with email and password
   * Stores tokens and fetches user data
   */
  async function login(email: string, password: string) {
    try {
      const tokens: TokenResponse = await loginUser({ email, password });

      // Store tokens securely
      saveTokens(tokens.access_token, tokens.refresh_token);

      // Get user data
      const userData = await getCurrentUser(tokens.access_token);
      setUser(userData);
      saveUser(userData);
    } catch (error: any) {
      // Error already translated to Duygu Adami in auth.ts
      throw error;
    }
  }

  /**
   * Logout user
   * Clears tokens and notifies backend
   */
  async function logout() {
    try {
      const accessToken = getAccessToken();
      const refreshTokenValue = getRefreshToken();

      if (accessToken && refreshTokenValue) {
        await logoutUser(accessToken, refreshTokenValue);
      }
    } catch (error) {
      // Continue with logout even if API call fails
      console.error('Logout error:', error);
    } finally {
      // Clear tokens and user
      clearTokens();
      setUser(null);
    }
  }

  /**
   * Refresh access token
   * Auto-called when token is about to expire
   */
  async function refreshAccessToken() {
    try {
      const refreshTokenValue = getRefreshToken();
      if (!refreshTokenValue) {
        throw new Error('No refresh token');
      }

      const tokens = await refreshToken(refreshTokenValue);
      saveTokens(tokens.access_token, tokens.refresh_token);
    } catch (error) {
      // Refresh failed, logout
      await logout();
      throw error;
    }
  }

  const value: AuthContextType = {
    user,
    loading,
    isAuthenticated: !!user,
    login,
    register,
    logout,
    refreshAccessToken,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

/**
 * Hook to use auth context
 */
export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}

