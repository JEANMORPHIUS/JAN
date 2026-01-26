/** * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
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

import { memo, useMemo, useRef, useEffect } from 'react';
import { HistoryEntry } from './HistoryPanel';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { useFocusTrap, useReturnFocus } from '@/hooks/useFocusManagement';

interface CompareViewProps {
  entries: HistoryEntry[];
  onClose: () => void;
}

function CompareView({ entries, onClose }: CompareViewProps) {
  // Memoize grid columns calculation
  const gridColumns = useMemo(() => entries.length, [entries.length]);
  const modalRef = useRef<HTMLDivElement>(null);
  
  // Focus management
  useFocusTrap(true, modalRef);
  useReturnFocus(true);
  
  // Focus close button on mount
  useEffect(() => {
    const closeButton = modalRef.current?.querySelector('button') as HTMLElement;
    closeButton?.focus();
  }, []);
  return (
    <div 
      ref={modalRef}
      className="card"
      role="dialog"
      aria-modal="true"
      aria-label={`Compare ${entries.length} outputs`}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <h2>Compare Outputs ({entries.length})</h2>
        <button 
          className="button" 
          onClick={onClose} 
          style={{ backgroundColor: '#666' }}
          aria-label="Close compare view"
        >
          Close
        </button>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: `repeat(${gridColumns}, 1fr)`, gap: '1rem' }}>
        {entries.map((entry, idx) => (
          <div
            key={entry.id}
            style={{
              border: '1px solid #333',
              borderRadius: '4px',
              padding: '1rem',
              backgroundColor: '#0a0a0a',
            }}
          >
            <div style={{ marginBottom: '0.75rem' }}>
              <div style={{ fontWeight: 600, fontFamily: 'monospace', marginBottom: '0.25rem' }}>
                {entry.persona}
              </div>
              <div style={{ fontSize: '0.75rem', color: '#999', marginBottom: '0.25rem' }}>
                {entry.output_type} • {new Date(entry.timestamp).toLocaleString()}
              </div>
              {entry.validation && (
                <div style={{
                  fontSize: '0.75rem',
                  color: entry.validation.valid ? '#2e7d32' : '#d32f2f',
                  marginBottom: '0.25rem',
                }}>
                  {entry.validation.valid ? '✓ Valid' : '✗ Invalid'}
                </div>
              )}
            </div>

            <div style={{
              fontSize: '0.875rem',
              color: '#999',
              marginBottom: '0.5rem',
              fontStyle: 'italic',
            }}>
              Prompt: {entry.prompt?.slice(0, 100)}...
            </div>

            <div style={{
              border: '1px solid #333',
              borderRadius: '4px',
              padding: '0.75rem',
              backgroundColor: '#0a0a0a',
              maxHeight: '400px',
              overflowY: 'auto',
              fontSize: '0.875rem',
              fontFamily: 'monospace',
            }}>
              {entry.content ? (
                <ReactMarkdown remarkPlugins={[remarkGfm]}>
                  {entry.content}
                </ReactMarkdown>
              ) : (
                <div style={{ color: '#666', fontStyle: 'italic' }}>No content</div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

// Memoize CompareView to prevent unnecessary re-renders
export default memo(CompareView, (prevProps, nextProps) => {
  if (prevProps.entries.length !== nextProps.entries.length) return false;
  return prevProps.entries.every((entry, idx) => 
    entry.id === nextProps.entries[idx]?.id &&
    entry.content === nextProps.entries[idx]?.content
  );
});

