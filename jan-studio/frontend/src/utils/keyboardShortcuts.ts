/** * * Keyboard Shortcuts Utility
 *  * 
 *  * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 *  * Spiritual Alignment Over Mechanical Productivity
 *  * 
 *  * Provides keyboard shortcut handling for the Creation Centre UI
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

export type ShortcutCallback = (e: KeyboardEvent) => void;

export interface ShortcutConfig {
  key: string;
  ctrl?: boolean;
  meta?: boolean; // Cmd on Mac
  shift?: boolean;
  alt?: boolean;
  callback: ShortcutCallback;
  description: string;
  preventDefault?: boolean;
}

class KeyboardShortcutsManager {
  private shortcuts: Map<string, ShortcutConfig> = new Map();
  private enabled: boolean = true;

  /**
   * Register a keyboard shortcut
   */
  register(config: ShortcutConfig): () => void {
    const id = this.generateShortcutId(config);
    this.shortcuts.set(id, config);

    // Return unregister function
    return () => {
      this.shortcuts.delete(id);
    };
  }

  /**
   * Enable/disable all shortcuts
   */
  setEnabled(enabled: boolean) {
    this.enabled = enabled;
  }

  /**
   * Get all registered shortcuts with descriptions
   */
  getAllShortcuts(): Array<{ id: string; config: ShortcutConfig }> {
    return Array.from(this.shortcuts.entries()).map(([id, config]) => ({
      id,
      config,
    }));
  }

  /**
   * Generate a unique ID for a shortcut configuration
   */
  private generateShortcutId(config: ShortcutConfig): string {
    const parts = [];
    if (config.ctrl) parts.push('ctrl');
    if (config.meta) parts.push('meta');
    if (config.shift) parts.push('shift');
    if (config.alt) parts.push('alt');
    parts.push(config.key.toLowerCase());
    return parts.join('+');
  }

  /**
   * Check if a keyboard event matches a shortcut config
   */
  private matchesShortcut(e: KeyboardEvent, config: ShortcutConfig): boolean {
    const keyMatch = e.key.toLowerCase() === config.key.toLowerCase();
    const ctrlMatch = config.ctrl ? e.ctrlKey : !e.ctrlKey;
    const metaMatch = config.meta !== undefined 
      ? (config.meta ? e.metaKey : !e.metaKey)
      : (!e.metaKey && !e.ctrlKey || (e.metaKey || e.ctrlKey)); // Allow either if not specified
    const shiftMatch = config.shift !== undefined ? (config.shift ? e.shiftKey : !e.shiftKey) : true;
    const altMatch = config.alt !== undefined ? (config.alt ? e.altKey : !e.altKey) : true;

    // Handle Ctrl/Cmd cross-platform
    const platformCtrlMatch = config.ctrl 
      ? (e.ctrlKey || e.metaKey) 
      : (!config.meta ? (!e.ctrlKey && !e.metaKey) : (!e.ctrlKey && e.metaKey));

    return keyMatch && platformCtrlMatch && shiftMatch && altMatch;
  }

  /**
   * Handle keyboard event
   */
  handleKeyDown = (e: KeyboardEvent): void => {
    if (!this.enabled) return;

    for (const config of this.shortcuts.values()) {
      if (this.matchesShortcut(e, config)) {
        if (config.preventDefault !== false) {
          e.preventDefault();
        }
        config.callback(e);
        break; // Only trigger first matching shortcut
      }
    }
  };

  /**
   * Initialize keyboard shortcuts (call this once)
   * Only works in browser environment (client-side)
   */
  initialize(): () => void {
    // Check if we're in a browser environment
    if (typeof window === 'undefined') {
      // Return a no-op cleanup function for SSR
      return () => {};
    }
    
    window.addEventListener('keydown', this.handleKeyDown);
    return () => {
      if (typeof window !== 'undefined') {
        window.removeEventListener('keydown', this.handleKeyDown);
      }
    };
  }
}

// Singleton instance
export const keyboardShortcuts = new KeyboardShortcutsManager();

// Initialize only on client-side (browser)
if (typeof window !== 'undefined') {
  keyboardShortcuts.initialize();
}

/**
 * React hook for using keyboard shortcuts
 */
export function useKeyboardShortcut(
  config: ShortcutConfig,
  deps: any[] = []
): void {
  // Import React dynamically to avoid issues
  if (typeof window !== 'undefined') {
    const React = require('react');
    const { useEffect } = React;

    useEffect(() => {
      const unregister = keyboardShortcuts.register(config);
      return unregister;
      // eslint-disable-next-line react-hooks/exhaustive-deps
    }, deps);
  }
}

/**
 * Common shortcut configurations
 */
export const CommonShortcuts = {
  search: (callback: ShortcutCallback): ShortcutConfig => ({
    key: 'k',
    ctrl: true,
    meta: true, // Cmd on Mac
    callback,
    description: 'Open search',
    preventDefault: true,
  }),
  save: (callback: ShortcutCallback): ShortcutConfig => ({
    key: 's',
    ctrl: true,
    meta: true,
    callback,
    description: 'Save current file',
    preventDefault: true,
  }),
  escape: (callback: ShortcutCallback): ShortcutConfig => ({
    key: 'Escape',
    callback,
    description: 'Close dialog or cancel',
  }),
  generate: (callback: ShortcutCallback): ShortcutConfig => ({
    key: 'Enter',
    ctrl: true,
    meta: true,
    callback,
    description: 'Generate content',
    preventDefault: true,
  }),
};
