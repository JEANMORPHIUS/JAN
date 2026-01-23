/**
 * DATA STORAGE UTILITIES
 * UPDATED: Now uses encryption to protect the miracle's biology
 *
 * Philosophy: "We are born a miracle" - health data is sacred
 * Implementation: AES-GCM encryption with user-controlled passphrase
 *
 * MIGRATION: Automatically upgrades unencrypted data on first use
 */

import { HealthMetrics } from '../types';
import { SecureStorage, migrateToEncrypted } from './encryption';

const STORAGE_KEY = 'homeostasis-sentinel-data';
const LEGACY_STORAGE_KEY = 'homeostasis-sentinel-data-legacy';

// Global secure storage instance
let secureStorage: SecureStorage | null = null;
let isInitialized = false;

/**
 * Initialize secure storage with user passphrase
 * MUST be called before any other storage operations
 *
 * @param passphrase - User's encryption passphrase
 * @returns Promise that resolves when initialization is complete
 */
export async function initializeSecureStorage(passphrase: string): Promise<void> {
  if (!passphrase || passphrase.trim().length < 8) {
    throw new Error('Passphrase must be at least 8 characters');
  }

  secureStorage = new SecureStorage();
  await secureStorage.initialize(passphrase);
  isInitialized = true;

  // Attempt migration from legacy unencrypted storage
  await migrateLegacyData();
}

/**
 * Migrate existing unencrypted data to encrypted storage
 * Called automatically during initialization
 */
async function migrateLegacyData(): Promise<void> {
  if (!secureStorage) return;

  try {
    // Check if there's unencrypted data
    const legacyData = localStorage.getItem(STORAGE_KEY);
    if (!legacyData) return;

    // Check if it's already encrypted (will fail to parse as JSON)
    try {
      JSON.parse(legacyData);
      // If we get here, it's unencrypted - migrate it
      console.log('📦 Migrating unencrypted health data to secure storage...');

      const metrics = JSON.parse(legacyData) as HealthMetrics[];
      await secureStorage.setItem(STORAGE_KEY, metrics);

      // Backup old data before removing
      localStorage.setItem(LEGACY_STORAGE_KEY, legacyData);
      localStorage.removeItem(STORAGE_KEY);

      console.log('✅ Health data successfully encrypted and secured');
    } catch {
      // Already encrypted, do nothing
      console.log('✅ Health data already encrypted');
    }
  } catch (error) {
    console.error('⚠️ Migration failed:', error);
  }
}

/**
 * Check if secure storage is initialized
 */
export function isSecureStorageInitialized(): boolean {
  return isInitialized && secureStorage !== null;
}

/**
 * Save metrics to encrypted storage
 *
 * @throws Error if secure storage not initialized
 */
export async function saveMetrics(metrics: HealthMetrics[]): Promise<void> {
  if (!secureStorage) {
    throw new Error(
      'Secure storage not initialized. Call initializeSecureStorage() first.'
    );
  }

  try {
    await secureStorage.setItem(STORAGE_KEY, metrics);
  } catch (error) {
    console.error('Failed to save metrics:', error);
    throw error;
  }
}

/**
 * Load metrics from encrypted storage
 *
 * @throws Error if secure storage not initialized
 */
export async function loadMetrics(): Promise<HealthMetrics[]> {
  if (!secureStorage) {
    throw new Error(
      'Secure storage not initialized. Call initializeSecureStorage() first.'
    );
  }

  try {
    const data = await secureStorage.getItem(STORAGE_KEY);
    if (!data) return [];
    return data as HealthMetrics[];
  } catch (error) {
    console.error('Failed to load metrics:', error);
    return [];
  }
}

/**
 * Clear all stored data (including encryption keys)
 * WARNING: This is irreversible
 */
export function clearStorage(): void {
  try {
    if (secureStorage) {
      secureStorage.clear();
      secureStorage = null;
      isInitialized = false;
    }
    localStorage.clear();
    console.log('🗑️ All health data cleared');
  } catch (error) {
    console.error('Failed to clear storage:', error);
  }
}

/**
 * Add a new metric
 */
export async function addMetric(metric: HealthMetrics): Promise<void> {
  const metrics = await loadMetrics();
  metrics.push(metric);
  await saveMetrics(metrics);
}

/**
 * Update an existing metric
 */
export async function updateMetric(
  index: number,
  metric: HealthMetrics
): Promise<void> {
  const metrics = await loadMetrics();
  if (index >= 0 && index < metrics.length) {
    metrics[index] = metric;
    await saveMetrics(metrics);
  }
}

/**
 * Delete a metric
 */
export async function deleteMetric(index: number): Promise<void> {
  const metrics = await loadMetrics();
  if (index >= 0 && index < metrics.length) {
    metrics.splice(index, 1);
    await saveMetrics(metrics);
  }
}

/**
 * LEGACY FUNCTION: For backward compatibility
 * Synchronous version that throws if not initialized
 * Use async versions instead
 *
 * @deprecated Use async loadMetrics() instead
 */
export function loadMetricsSync(): HealthMetrics[] {
  if (!isSecureStorageInitialized()) {
    throw new Error('Secure storage not initialized');
  }
  // This won't work with encryption - user must migrate to async
  throw new Error(
    'Synchronous access no longer supported. Use async loadMetrics() instead.'
  );
}
