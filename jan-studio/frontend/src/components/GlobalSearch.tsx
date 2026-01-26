/** * * Global Search Component
 *  * 
 *  * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 *  * Spiritual Alignment Over Mechanical Productivity
 *  * 
 *  * Provides global search functionality across personas, history, and templates
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

import { useState, useEffect, useRef, useCallback } from 'react';
import { getPersonas } from '@/api/personas';
import { getGenerationHistory } from '@/api/generation';
import { getTemplates } from '@/api/templates';
import { useKeyboardShortcut as useKeyboardShortcutHook, CommonShortcuts } from '@/utils/keyboardShortcuts';
import { useFocusTrap, useReturnFocus } from '@/hooks/useFocusManagement';

export interface SearchResult {
  id: string;
  type: 'persona' | 'history' | 'template';
  title: string;
  subtitle?: string;
  metadata?: Record<string, any>;
}

interface GlobalSearchProps {
  onSelect: (result: SearchResult) => void;
  searchIn?: ('personas' | 'history' | 'templates')[];
  placeholder?: string;
}

export default function GlobalSearch({
  onSelect,
  searchIn = ['personas', 'history', 'templates'],
  placeholder = 'Search personas, history, templates...',
}: GlobalSearchProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [loading, setLoading] = useState(false);
  const [selectedIndex, setSelectedIndex] = useState(0);
  const searchInputRef = useRef<HTMLInputElement>(null);
  const resultsRef = useRef<HTMLDivElement>(null);
  const modalRef = useRef<HTMLDivElement>(null);
  
  // Focus management
  useFocusTrap(isOpen, modalRef);
  useReturnFocus(isOpen);

  // Register keyboard shortcut to open search
  useKeyboardShortcutHook(
    CommonShortcuts.search(() => {
      setIsOpen(true);
      setTimeout(() => searchInputRef.current?.focus(), 100);
    }),
    []
  );

  // Close on Escape
  useKeyboardShortcutHook(
    CommonShortcuts.escape(() => {
      if (isOpen) {
        setIsOpen(false);
        setQuery('');
        setResults([]);
      }
    }),
    [isOpen]
  );

  // Search function with debouncing
  const performSearch = useCallback(
    async (searchQuery: string) => {
      if (!searchQuery.trim()) {
        setResults([]);
        return;
      }

      setLoading(true);
      const allResults: SearchResult[] = [];

      try {
        // Search personas
        if (searchIn.includes('personas')) {
          try {
            const personas = await getPersonas();
            const matchingPersonas = personas
              .filter((name) =>
                name.toLowerCase().includes(searchQuery.toLowerCase())
              )
              .slice(0, 5)
              .map((name) => ({
                id: `persona-${name}`,
                type: 'persona' as const,
                title: name,
                subtitle: 'Persona',
                metadata: { name },
              }));

            allResults.push(...matchingPersonas);
          } catch (err) {
            console.error('Failed to search personas:', err);
          }
        }

        // Search history
        if (searchIn.includes('history')) {
          try {
            const history = await getGenerationHistory();
            const matchingHistory = history
              .filter(
                (entry) =>
                  entry.prompt?.toLowerCase().includes(searchQuery.toLowerCase()) ||
                  entry.content?.toLowerCase().includes(searchQuery.toLowerCase()) ||
                  entry.persona?.toLowerCase().includes(searchQuery.toLowerCase())
              )
              .slice(0, 5)
              .map((entry) => ({
                id: entry.id || `history-${entry.timestamp}`,
                type: 'history' as const,
                title: entry.prompt?.substring(0, 60) || 'Untitled',
                subtitle: `${entry.persona} • ${entry.output_type || 'text'}`,
                metadata: { entry },
              }));

            allResults.push(...matchingHistory);
          } catch (err) {
            console.error('Failed to search history:', err);
          }
        }

        // Search templates
        if (searchIn.includes('templates')) {
          try {
            const templates = await getTemplates();
            const matchingTemplates = templates
              .filter(
                (template) =>
                  template.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                  template.description?.toLowerCase().includes(searchQuery.toLowerCase())
              )
              .slice(0, 5)
              .map((template) => ({
                id: `template-${template.name}`,
                type: 'template' as const,
                title: template.name,
                subtitle: template.description || 'Template',
                metadata: { template },
              }));

            allResults.push(...matchingTemplates);
          } catch (err) {
            console.error('Failed to search templates:', err);
          }
        }

        setResults(allResults);
        setSelectedIndex(0);
      } catch (err) {
        console.error('Search failed:', err);
      } finally {
        setLoading(false);
      }
    },
    [searchIn]
  );

  // Debounced search
  useEffect(() => {
    const timer = setTimeout(() => {
      performSearch(query);
    }, 300);

    return () => clearTimeout(timer);
  }, [query, performSearch]);

  // Keyboard navigation
  useEffect(() => {
    if (!isOpen) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        setSelectedIndex((prev) => Math.min(prev + 1, results.length - 1));
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        setSelectedIndex((prev) => Math.max(prev - 1, 0));
      } else if (e.key === 'Enter' && results[selectedIndex]) {
        e.preventDefault();
        handleSelectResult(results[selectedIndex]);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, results, selectedIndex]);

  // Scroll selected result into view
  useEffect(() => {
    if (resultsRef.current && selectedIndex >= 0) {
      const selectedElement = resultsRef.current.children[selectedIndex] as HTMLElement;
      if (selectedElement) {
        selectedElement.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      }
    }
  }, [selectedIndex]);

  const handleSelectResult = (result: SearchResult) => {
    onSelect(result);
    setIsOpen(false);
    setQuery('');
    setResults([]);
  };

  const getResultIcon = (type: SearchResult['type']) => {
    switch (type) {
      case 'persona':
        return '👤';
      case 'history':
        return '🕐';
      case 'template':
        return '📄';
      default:
        return '🔍';
    }
  };

  if (!isOpen) {
    return (
      <button
        onClick={() => setIsOpen(true)}
        style={{
          padding: '0.5rem 1rem',
          border: '1px solid #333',
          borderRadius: '4px',
          backgroundColor: '#1a1a1a',
          color: '#999',
          cursor: 'pointer',
          fontSize: '0.875rem',
          width: '100%',
          textAlign: 'left',
          display: 'flex',
          alignItems: 'center',
          gap: '0.5rem',
        }}
        aria-label="Open search"
      >
        <span>🔍</span>
        <span>{placeholder}</span>
        <span style={{ marginLeft: 'auto', fontSize: '0.75rem', opacity: 0.6 }}>
          Ctrl+K
        </span>
      </button>
    );
  }

  return (
    <div
      ref={modalRef}
      role="dialog"
      aria-modal="true"
      aria-label="Global search"
      style={{
        position: 'fixed',
        top: '20%',
        left: '50%',
        transform: 'translateX(-50%)',
        width: '600px',
        maxWidth: '90vw',
        zIndex: 1000,
        backgroundColor: '#1a1a1a',
        border: '2px solid #0070f3',
        borderRadius: '8px',
        boxShadow: '0 8px 32px rgba(0, 0, 0, 0.5)',
      }}
    >
      {/* Search Input */}
      <div style={{ padding: '1rem', borderBottom: '1px solid #333' }}>
        <input
          ref={searchInputRef}
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder={placeholder}
          autoFocus
          style={{
            width: '100%',
            padding: '0.75rem',
            border: 'none',
            backgroundColor: '#0a0a0a',
            color: '#e0e0e0',
            fontSize: '1rem',
            fontFamily: 'inherit',
            outline: '2px solid transparent',
            outlineOffset: '2px',
          }}
          aria-label="Search input"
          aria-describedby="search-help"
          onFocus={(e) => {
            e.target.style.outline = '2px solid #0070f3';
          }}
          onBlur={(e) => {
            e.target.style.outline = '2px solid transparent';
          }}
        />
      </div>

      {/* Results */}
      {loading ? (
        <div style={{ padding: '2rem', textAlign: 'center', color: '#999' }}>
          Searching...
        </div>
      ) : results.length > 0 ? (
        <div
          ref={resultsRef}
          style={{
            maxHeight: '400px',
            overflowY: 'auto',
          }}
          role="listbox"
          aria-label="Search results"
        >
          {results.map((result, index) => (
            <div
              key={result.id}
              onClick={() => handleSelectResult(result)}
              style={{
                padding: '1rem',
                cursor: 'pointer',
                backgroundColor: index === selectedIndex ? '#0a0a1a' : 'transparent',
                borderBottom: '1px solid #333',
                display: 'flex',
                alignItems: 'center',
                gap: '1rem',
                transition: 'background-color 0.15s',
              }}
              role="option"
              aria-selected={index === selectedIndex}
              onMouseEnter={() => setSelectedIndex(index)}
            >
              <span style={{ fontSize: '1.25rem' }}>{getResultIcon(result.type)}</span>
              <div style={{ flex: 1 }}>
                <div style={{ fontWeight: 600, color: '#e0e0e0', marginBottom: '0.25rem' }}>
                  {result.title}
                </div>
                {result.subtitle && (
                  <div style={{ fontSize: '0.875rem', color: '#999' }}>
                    {result.subtitle}
                  </div>
                )}
              </div>
              <span
                style={{
                  fontSize: '0.75rem',
                  color: '#666',
                  textTransform: 'uppercase',
                  fontFamily: 'monospace',
                }}
              >
                {result.type}
              </span>
            </div>
          ))}
        </div>
      ) : query.trim() ? (
        <div style={{ padding: '2rem', textAlign: 'center', color: '#999' }}>
          No results found
        </div>
      ) : (
        <div style={{ padding: '2rem', textAlign: 'center', color: '#999' }}>
          Start typing to search...
        </div>
      )}

      {/* Footer */}
      <div
        style={{
          padding: '0.75rem 1rem',
          borderTop: '1px solid #333',
          fontSize: '0.75rem',
          color: '#666',
          display: 'flex',
          justifyContent: 'space-between',
        }}
      >
        <span>↑↓ Navigate • Enter Select • Esc Close</span>
        <span>{results.length} result{results.length !== 1 ? 's' : ''}</span>
      </div>
    </div>
  );
}
