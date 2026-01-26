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
 * Language Switcher Component for Global Expansion
 */

'use client';

import { useState, useRef, useEffect } from 'react';
import { useI18n, SUPPORTED_LANGUAGES, type LanguageInfo } from '@/contexts/I18nContext';
import { useFocusTrap, useReturnFocus } from '@/hooks/useFocusManagement';

export default function LanguageSwitcher() {
  const { language, setLanguage, languages } = useI18n();
  const [isOpen, setIsOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);
  const buttonRef = useRef<HTMLButtonElement>(null);
  
  useFocusTrap(isOpen, dropdownRef);
  useReturnFocus(isOpen);

  const currentLanguage = languages.find(l => l.code === language) || languages[0];

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target as Node) &&
          buttonRef.current && !buttonRef.current.contains(e.target as Node)) {
        setIsOpen(false);
      }
    };

    if (isOpen) {
      document.addEventListener('mousedown', handleClickOutside);
      return () => document.removeEventListener('mousedown', handleClickOutside);
    }
  }, [isOpen]);

  return (
    <div style={{ position: 'relative' }}>
      <button
        ref={buttonRef}
        onClick={() => setIsOpen(!isOpen)}
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: '0.5rem',
          padding: '0.5rem 1rem',
          backgroundColor: '#1a1a1a',
          border: '1px solid #333',
          borderRadius: '4px',
          color: '#e0e0e0',
          cursor: 'pointer',
          fontSize: '0.875rem',
          minWidth: '120px',
        }}
        aria-label={`Current language: ${currentLanguage.name}. Click to change language`}
        aria-expanded={isOpen}
        aria-haspopup="true"
      >
        <span style={{ fontSize: '1.25rem' }}>{currentLanguage.flag}</span>
        <span>{currentLanguage.nativeName}</span>
        <span style={{ marginLeft: 'auto', fontSize: '0.75rem' }}>▼</span>
      </button>

      {isOpen && (
        <div
          ref={dropdownRef}
          role="menu"
          aria-label="Language selection"
          style={{
            position: 'absolute',
            top: '100%',
            right: 0,
            marginTop: '0.5rem',
            backgroundColor: '#1a1a1a',
            border: '1px solid #333',
            borderRadius: '4px',
            boxShadow: '0 4px 12px rgba(0, 0, 0, 0.5)',
            zIndex: 1000,
            minWidth: '200px',
            maxHeight: '400px',
            overflowY: 'auto',
          }}
        >
          {languages.map((lang) => (
            <button
              key={lang.code}
              role="menuitem"
              onClick={() => {
                setLanguage(lang.code);
                setIsOpen(false);
              }}
              style={{
                width: '100%',
                display: 'flex',
                alignItems: 'center',
                gap: '0.75rem',
                padding: '0.75rem 1rem',
                backgroundColor: language === lang.code ? '#0a0a1a' : 'transparent',
                border: 'none',
                color: '#e0e0e0',
                cursor: 'pointer',
                fontSize: '0.875rem',
                textAlign: 'left',
                transition: 'background-color 0.2s',
              }}
              onMouseEnter={(e) => {
                if (language !== lang.code) {
                  e.currentTarget.style.backgroundColor = '#2a2a2a';
                }
              }}
              onMouseLeave={(e) => {
                if (language !== lang.code) {
                  e.currentTarget.style.backgroundColor = 'transparent';
                }
              }}
              aria-label={`Switch to ${lang.name}`}
              aria-selected={language === lang.code}
            >
              <span style={{ fontSize: '1.25rem' }}>{lang.flag}</span>
              <div style={{ flex: 1 }}>
                <div style={{ fontWeight: language === lang.code ? 600 : 400 }}>
                  {lang.nativeName}
                </div>
                <div style={{ fontSize: '0.75rem', color: '#999' }}>
                  {lang.name}
                </div>
              </div>
              {language === lang.code && (
                <span style={{ color: '#0070f3' }}>✓</span>
              )}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
