/**
 * CURSOR FIX - Simple, Clean Solution
 * 
 * Ensures cursor and clicks work properly.
 * Runs once on mount, fixes any issues.
 */

import { useEffect } from 'react';

export default function CursorFix() {
  useEffect(() => {
    if (typeof window === 'undefined') return;

    // Detect if running in CursorBrowser
    const isCursorBrowser = navigator.userAgent.includes('Cursor') || 
                           (window as any).cursorBrowser !== undefined;

    // Fix cursor on all buttons and links
    const fixCursors = () => {
      // Buttons - force pointer cursor
      document.querySelectorAll('button').forEach(btn => {
        if (btn instanceof HTMLElement) {
          btn.style.cursor = 'pointer';
          btn.style.setProperty('cursor', 'pointer', 'important');
        }
      });

      // Links - force pointer cursor
      document.querySelectorAll('a').forEach(link => {
        if (link instanceof HTMLElement) {
          link.style.cursor = 'pointer';
          link.style.setProperty('cursor', 'pointer', 'important');
        }
      });

      // Clickable divs (persona cards, etc)
      document.querySelectorAll('[onClick], [onclick]').forEach(el => {
        if (el instanceof HTMLElement) {
          el.style.cursor = 'pointer';
          el.style.setProperty('cursor', 'pointer', 'important');
        }
      });

      // If CursorBrowser, also force on body/html to override any browser-level overrides
      if (isCursorBrowser) {
        document.body.style.cursor = 'default';
        document.documentElement.style.cursor = 'default';
      }
    };

    // Run immediately
    fixCursors();

    // Run after a short delay (in case elements load later)
    setTimeout(fixCursors, 100);
    setTimeout(fixCursors, 500);

    // Watch for new elements
    const observer = new MutationObserver(fixCursors);
    observer.observe(document.body, { childList: true, subtree: true });

    return () => observer.disconnect();
  }, []);

  return null;
}
