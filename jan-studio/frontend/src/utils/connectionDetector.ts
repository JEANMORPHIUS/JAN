/** * * Connection Detection Utility
 *  * Auto-enables Lite Mode on slow connections
 *  *
 *  * Philosophy: "No closed doors. No bandwidth barriers."
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

interface ConnectionInfo {
  effectiveType: '4g' | '3g' | '2g' | 'slow-2g';
  downlink: number; // Mbps
  rtt: number; // Round-trip time in ms
}

/**
 * Check if connection is slow
 */
export function isSlowConnection(): boolean {
  if (typeof window === 'undefined') return false;

  const connection = (navigator as any).connection
    || (navigator as any).mozConnection
    || (navigator as any).webkitConnection;

  if (connection) {
    const effectiveType = connection.effectiveType;
    return effectiveType === '2g' || effectiveType === 'slow-2g';
  }

  // Fallback: No API support
  return false;
}

/**
 * Get connection info
 */
export function getConnectionInfo(): ConnectionInfo | null {
  if (typeof window === 'undefined') return null;

  const connection = (navigator as any).connection
    || (navigator as any).mozConnection
    || (navigator as any).webkitConnection;

  if (!connection) return null;

  return {
    effectiveType: connection.effectiveType,
    downlink: connection.downlink,
    rtt: connection.rtt,
  };
}

/**
 * Enable Lite Mode
 */
export function enableLiteMode(): void {
  if (typeof window === 'undefined') return;

  document.body.classList.add('lite-mode');
  localStorage.setItem('ui-mode', 'lite');
  console.log('🔦 Lite Mode enabled (slow connection detected)');
}

/**
 * Disable Lite Mode
 */
export function disableLiteMode(): void {
  if (typeof window === 'undefined') return;

  document.body.classList.remove('lite-mode');
  localStorage.setItem('ui-mode', 'standard');
  console.log('✨ Standard Mode enabled');
}

/**
 * Check if Lite Mode is currently enabled
 */
export function isLiteModeEnabled(): boolean {
  if (typeof window === 'undefined') return false;
  return document.body.classList.contains('lite-mode');
}

/**
 * Auto-detect and set appropriate mode
 */
export function autoDetectUIMode(): void {
  if (typeof window === 'undefined') return;

  // Check user preference first
  const savedMode = localStorage.getItem('ui-mode');
  if (savedMode === 'lite') {
    enableLiteMode();
    return;
  }

  // Auto-detect connection
  if (isSlowConnection()) {
    enableLiteMode();
    showLiteModeNotification();
  }
}

/**
 * Show notification about Lite Mode
 */
function showLiteModeNotification(): void {
  if (typeof window === 'undefined') return;

  // Don't show if already dismissed this session
  if (sessionStorage.getItem('lite-mode-notified') === 'true') {
    return;
  }

  const notification = document.createElement('div');
  notification.className = 'lite-mode-notification';
  notification.innerHTML = `
    <p><strong>🔦 Lite Mode Enabled</strong></p>
    <p>Optimized for your connection speed</p>
    <button class="dismiss-notification">Got it</button>
  `;

  const dismissButton = notification.querySelector('.dismiss-notification');
  dismissButton?.addEventListener('click', () => {
    notification.remove();
    sessionStorage.setItem('lite-mode-notified', 'true');
  });

  document.body.appendChild(notification);

  // Auto-dismiss after 5 seconds
  setTimeout(() => {
    if (notification.parentElement) {
      notification.remove();
      sessionStorage.setItem('lite-mode-notified', 'true');
    }
  }, 5000);
}

/**
 * Listen for connection changes
 */
export function watchConnectionChanges(): void {
  if (typeof window === 'undefined') return;

  const connection = (navigator as any).connection
    || (navigator as any).mozConnection
    || (navigator as any).webkitConnection;

  if (!connection) return;

  connection.addEventListener('change', () => {
    const info = getConnectionInfo();
    console.log('📡 Connection changed:', info);

    // Re-evaluate UI mode
    autoDetectUIMode();
  });
}

/**
 * Initialize connection detection
 * Call this on app startup
 */
export function initConnectionDetection(): void {
  if (typeof window === 'undefined') return;

  autoDetectUIMode();
  watchConnectionChanges();
}
