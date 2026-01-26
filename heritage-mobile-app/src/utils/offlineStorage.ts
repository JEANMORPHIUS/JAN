/** * * Offline Storage Utilities
 *  * AsyncStorage caching for wonders, pillars, and other data
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

import AsyncStorage from '@react-native-async-storage/async-storage';
import type { Wonder } from '../api/wonders';
import type { Pillar } from '../api/heritage';

const STORAGE_KEYS = {
  WONDERS: '@heritage:wonders',
  PILLARS: '@heritage:pillars',
  LAST_SYNC: '@heritage:lastSync',
  SYNC_STATUS: '@heritage:syncStatus',
};

export interface SyncStatus {
  lastSync: number | null;
  isSyncing: boolean;
  hasOfflineData: boolean;
}

/**
 * Save wonders to offline storage
 */
export const saveWonders = async (wonders: Wonder[]): Promise<void> => {
  try {
    await AsyncStorage.setItem(STORAGE_KEYS.WONDERS, JSON.stringify(wonders));
    await AsyncStorage.setItem(STORAGE_KEYS.LAST_SYNC, Date.now().toString());
    await updateSyncStatus(true);
  } catch (error) {
    console.error('Error saving wonders:', error);
    throw error;
  }
};

/**
 * Load wonders from offline storage
 */
export const loadWonders = async (): Promise<Wonder[] | null> => {
  try {
    const data = await AsyncStorage.getItem(STORAGE_KEYS.WONDERS);
    if (data) {
      return JSON.parse(data);
    }
    return null;
  } catch (error) {
    console.error('Error loading wonders:', error);
    return null;
  }
};

/**
 * Save pillars to offline storage
 */
export const savePillars = async (pillars: Pillar[]): Promise<void> => {
  try {
    await AsyncStorage.setItem(STORAGE_KEYS.PILLARS, JSON.stringify(pillars));
    await AsyncStorage.setItem(STORAGE_KEYS.LAST_SYNC, Date.now().toString());
    await updateSyncStatus(true);
  } catch (error) {
    console.error('Error saving pillars:', error);
    throw error;
  }
};

/**
 * Load pillars from offline storage
 */
export const loadPillars = async (): Promise<Pillar[] | null> => {
  try {
    const data = await AsyncStorage.getItem(STORAGE_KEYS.PILLARS);
    if (data) {
      return JSON.parse(data);
    }
    return null;
  } catch (error) {
    console.error('Error loading pillars:', error);
    return null;
  }
};

/**
 * Get sync status
 */
export const getSyncStatus = async (): Promise<SyncStatus> => {
  try {
    const lastSyncStr = await AsyncStorage.getItem(STORAGE_KEYS.LAST_SYNC);
    const lastSync = lastSyncStr ? parseInt(lastSyncStr, 10) : null;
    
    const wonders = await loadWonders();
    const pillars = await loadPillars();
    const hasOfflineData = !!(wonders || pillars);

    return {
      lastSync,
      isSyncing: false,
      hasOfflineData,
    };
  } catch (error) {
    console.error('Error getting sync status:', error);
    return {
      lastSync: null,
      isSyncing: false,
      hasOfflineData: false,
    };
  }
};

/**
 * Update sync status
 */
const updateSyncStatus = async (hasData: boolean): Promise<void> => {
  try {
    await AsyncStorage.setItem(STORAGE_KEYS.SYNC_STATUS, JSON.stringify({
      hasOfflineData: hasData,
      lastUpdate: Date.now(),
    }));
  } catch (error) {
    console.error('Error updating sync status:', error);
  }
};

/**
 * Clear all offline data
 */
export const clearOfflineData = async (): Promise<void> => {
  try {
    await AsyncStorage.multiRemove([
      STORAGE_KEYS.WONDERS,
      STORAGE_KEYS.PILLARS,
      STORAGE_KEYS.LAST_SYNC,
      STORAGE_KEYS.SYNC_STATUS,
    ]);
  } catch (error) {
    console.error('Error clearing offline data:', error);
    throw error;
  }
};

/**
 * Check if data is stale (older than 24 hours)
 */
export const isDataStale = async (): Promise<boolean> => {
  try {
    const lastSyncStr = await AsyncStorage.getItem(STORAGE_KEYS.LAST_SYNC);
    if (!lastSyncStr) return true;

    const lastSync = parseInt(lastSyncStr, 10);
    const twentyFourHours = 24 * 60 * 60 * 1000;
    return Date.now() - lastSync > twentyFourHours;
  } catch (error) {
    console.error('Error checking data staleness:', error);
    return true;
  }
};
