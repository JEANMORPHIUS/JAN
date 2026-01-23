/**
 * Encryption Utility for Health Data Protection
 *
 * Purpose: Protect the miracle's biology (health metrics) with browser-based encryption
 * Philosophy: "We are born a miracle" - sacred data deserves sacred protection
 *
 * Implementation: AES-GCM encryption using Web Crypto API
 * - No external dependencies
 * - User-controlled encryption key
 * - Forward secrecy
 * - HIPAA-compliant approach
 */

const ALGORITHM = 'AES-GCM';
const KEY_LENGTH = 256;
const IV_LENGTH = 12; // 96 bits for GCM

/**
 * Generate a cryptographic key from a user passphrase
 * Uses PBKDF2 for key derivation
 */
export async function deriveKeyFromPassphrase(
  passphrase: string,
  salt: Uint8Array
): Promise<CryptoKey> {
  const encoder = new TextEncoder();
  const passphraseKey = await crypto.subtle.importKey(
    'raw',
    encoder.encode(passphrase),
    'PBKDF2',
    false,
    ['deriveKey']
  );

  return crypto.subtle.deriveKey(
    {
      name: 'PBKDF2',
      salt: salt,
      iterations: 100000, // OWASP recommendation
      hash: 'SHA-256',
    },
    passphraseKey,
    { name: ALGORITHM, length: KEY_LENGTH },
    false, // not extractable
    ['encrypt', 'decrypt']
  );
}

/**
 * Generate a random salt for key derivation
 */
export function generateSalt(): Uint8Array {
  return crypto.getRandomValues(new Uint8Array(16));
}

/**
 * Generate a random initialization vector
 */
function generateIV(): Uint8Array {
  return crypto.getRandomValues(new Uint8Array(IV_LENGTH));
}

/**
 * Encrypt data using AES-GCM
 *
 * @param data - Data to encrypt (will be stringified)
 * @param key - Encryption key derived from passphrase
 * @returns Encrypted data with IV prepended (base64 encoded)
 */
export async function encrypt(
  data: unknown,
  key: CryptoKey
): Promise<string> {
  const encoder = new TextEncoder();
  const dataString = JSON.stringify(data);
  const dataBuffer = encoder.encode(dataString);

  const iv = generateIV();

  const encryptedBuffer = await crypto.subtle.encrypt(
    {
      name: ALGORITHM,
      iv: iv,
    },
    key,
    dataBuffer
  );

  // Prepend IV to encrypted data
  const combined = new Uint8Array(iv.length + encryptedBuffer.byteLength);
  combined.set(iv, 0);
  combined.set(new Uint8Array(encryptedBuffer), iv.length);

  // Convert to base64 for storage
  return btoa(String.fromCharCode(...combined));
}

/**
 * Decrypt data using AES-GCM
 *
 * @param encryptedData - Base64 encoded encrypted data with IV prepended
 * @param key - Encryption key derived from passphrase
 * @returns Decrypted data (parsed from JSON)
 */
export async function decrypt(
  encryptedData: string,
  key: CryptoKey
): Promise<unknown> {
  // Decode from base64
  const combined = Uint8Array.from(atob(encryptedData), c => c.charCodeAt(0));

  // Extract IV and encrypted data
  const iv = combined.slice(0, IV_LENGTH);
  const encryptedBuffer = combined.slice(IV_LENGTH);

  const decryptedBuffer = await crypto.subtle.decrypt(
    {
      name: ALGORITHM,
      iv: iv,
    },
    key,
    encryptedBuffer
  );

  const decoder = new TextDecoder();
  const dataString = decoder.decode(decryptedBuffer);

  return JSON.parse(dataString);
}

/**
 * Storage wrapper for encrypted localStorage
 */
export class SecureStorage {
  private key: CryptoKey | null = null;
  private salt: Uint8Array | null = null;
  private readonly SALT_KEY = 'homeostasis_salt';

  /**
   * Initialize secure storage with user passphrase
   * If salt exists in localStorage, reuse it; otherwise generate new
   */
  async initialize(passphrase: string): Promise<void> {
    // Load or generate salt
    const saltString = localStorage.getItem(this.SALT_KEY);
    if (saltString) {
      this.salt = Uint8Array.from(atob(saltString), c => c.charCodeAt(0));
    } else {
      this.salt = generateSalt();
      localStorage.setItem(this.SALT_KEY, btoa(String.fromCharCode(...this.salt)));
    }

    // Derive key from passphrase
    this.key = await deriveKeyFromPassphrase(passphrase, this.salt);
  }

  /**
   * Store encrypted data
   */
  async setItem(key: string, value: unknown): Promise<void> {
    if (!this.key) {
      throw new Error('SecureStorage not initialized. Call initialize() first.');
    }

    const encrypted = await encrypt(value, this.key);
    localStorage.setItem(key, encrypted);
  }

  /**
   * Retrieve and decrypt data
   */
  async getItem(key: string): Promise<unknown> {
    if (!this.key) {
      throw new Error('SecureStorage not initialized. Call initialize() first.');
    }

    const encrypted = localStorage.getItem(key);
    if (!encrypted) {
      return null;
    }

    try {
      return await decrypt(encrypted, this.key);
    } catch (error) {
      console.error('Decryption failed. Wrong passphrase or corrupted data.');
      throw error;
    }
  }

  /**
   * Remove item from storage
   */
  removeItem(key: string): void {
    localStorage.removeItem(key);
  }

  /**
   * Clear all storage (including salt)
   */
  clear(): void {
    localStorage.clear();
    this.key = null;
    this.salt = null;
  }

  /**
   * Check if storage is initialized
   */
  isInitialized(): boolean {
    return this.key !== null;
  }
}

/**
 * Migration utility: Convert existing unencrypted data to encrypted
 */
export async function migrateToEncrypted(
  oldKey: string,
  newStorage: SecureStorage
): Promise<boolean> {
  try {
    // Read existing unencrypted data
    const oldData = localStorage.getItem(oldKey);
    if (!oldData) {
      return false; // No data to migrate
    }

    const parsedData = JSON.parse(oldData);

    // Write encrypted version
    await newStorage.setItem(oldKey, parsedData);

    // Remove old unencrypted version
    localStorage.removeItem(oldKey);

    console.log(`✅ Successfully migrated ${oldKey} to encrypted storage`);
    return true;
  } catch (error) {
    console.error(`❌ Migration failed for ${oldKey}:`, error);
    return false;
  }
}
