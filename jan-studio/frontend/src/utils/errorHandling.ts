/**
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
 * THE REST IS UP TO BABA X.
 * 
 * Error handling utilities for Creation Centre
 */

export interface ApiError {
  message: string;
  code?: string;
  status?: number;
  retryable?: boolean;
}

/**
 * Check if error is retryable
 */
export function isRetryableError(error: any): boolean {
  if (!error) return false;
  
  // Network errors are retryable
  if (error.code === 'NETWORK_ERROR' || error.message?.includes('network')) {
    return true;
  }
  
  // 5xx server errors are retryable
  if (error.response?.status >= 500 && error.response?.status < 600) {
    return true;
  }
  
  // 429 rate limit errors are retryable
  if (error.response?.status === 429) {
    return true;
  }
  
  return false;
}

/**
 * Get user-friendly error message
 */
export function getUserFriendlyError(error: any): string {
  if (!error) return 'An unknown error occurred';
  
  // Network errors
  if (error.code === 'NETWORK_ERROR' || error.message?.includes('network')) {
    return 'Network error. Please check your connection and try again.';
  }
  
  // API errors with messages
  if (error.response?.data?.detail) {
    return error.response.data.detail;
  }
  
  if (error.response?.data?.message) {
    return error.response.data.message;
  }
  
  // Status code based messages
  if (error.response?.status === 404) {
    return 'Resource not found.';
  }
  
  if (error.response?.status === 403) {
    return 'You do not have permission to perform this action.';
  }
  
  if (error.response?.status === 401) {
    return 'Please log in to continue.';
  }
  
  if (error.response?.status >= 500) {
    return 'Server error. Please try again later.';
  }
  
  // Generic fallback
  return error.message || 'An error occurred. Please try again.';
}

/**
 * Retry function with exponential backoff
 */
export async function retryWithBackoff<T>(
  fn: () => Promise<T>,
  maxRetries: number = 3,
  initialDelay: number = 1000
): Promise<T> {
  let lastError: any;
  
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error;
      
      if (attempt === maxRetries || !isRetryableError(error)) {
        throw error;
      }
      
      // Exponential backoff: 1s, 2s, 4s
      const delay = initialDelay * Math.pow(2, attempt);
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
  
  throw lastError;
}

/**
 * Check if device is online
 */
export function isOnline(): boolean {
  if (typeof navigator === 'undefined') return true;
  return navigator.onLine;
}

/**
 * Queue for offline operations
 */
class OfflineQueue {
  private queue: Array<() => Promise<void>> = [];
  
  add(operation: () => Promise<void>) {
    this.queue.push(operation);
  }
  
  async process() {
    if (!isOnline()) return;
    
    while (this.queue.length > 0) {
      const operation = this.queue.shift();
      if (operation) {
        try {
          await operation();
        } catch (error) {
          console.error('Failed to process queued operation:', error);
          // Re-queue if retryable
          if (isRetryableError(error)) {
            this.queue.push(operation);
          }
        }
      }
    }
  }
}

export const offlineQueue = new OfflineQueue();
