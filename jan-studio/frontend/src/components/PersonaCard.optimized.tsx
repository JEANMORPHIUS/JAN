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
 * OPTIMIZED VERSION: Memoized for performance
 */

import { memo } from 'react';

export interface PersonaInfo {
  name: string;
  fileCount: number;
  ruleCount: number;
  lastModified?: string;
}

interface PersonaCardProps {
  persona: PersonaInfo;
  onEdit: (name: string) => void;
  onDelete: (name: string) => void;
  isSelected?: boolean;
}

function PersonaCard({ persona, onEdit, onDelete, isSelected = false }: PersonaCardProps) {
  return (
    <div
      className="card"
      style={{
        border: isSelected ? '2px solid #0070f3' : '1px solid #333',
        backgroundColor: isSelected ? '#1a1a2a' : '#1a1a1a',
        cursor: 'pointer',
        transition: 'all 0.2s',
      }}
      onClick={() => onEdit(persona.name)}
      role="button"
      tabIndex={0}
      aria-label={`Persona: ${persona.name}`}
      aria-pressed={isSelected}
      onKeyDown={(e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          onEdit(persona.name);
        }
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start', marginBottom: '0.75rem' }}>
        <h3 style={{ margin: 0, fontSize: '1rem', fontWeight: 600 }}>{persona.name}</h3>
        <button
          className="button"
          onClick={(e) => {
            e.stopPropagation();
            if (confirm(`Delete persona "${persona.name}"?`)) {
              onDelete(persona.name);
            }
          }}
          style={{
            padding: '0.25rem 0.75rem',
            fontSize: '0.75rem',
            backgroundColor: '#d32f2f',
            border: 'none',
          }}
          aria-label={`Delete persona ${persona.name}`}
        >
          Delete
        </button>
      </div>
      
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '0.5rem', fontSize: '0.75rem', fontFamily: 'monospace' }}>
        <div>
          <div style={{ color: '#999' }}>Files</div>
          <div style={{ color: '#e0e0e0', fontWeight: 600 }}>{persona.fileCount}</div>
        </div>
        <div>
          <div style={{ color: '#999' }}>Rules</div>
          <div style={{ color: '#e0e0e0', fontWeight: 600 }}>{persona.ruleCount}</div>
        </div>
        <div>
          <div style={{ color: '#999' }}>Status</div>
          <div style={{ color: '#2e7d32', fontWeight: 600 }}>Active</div>
        </div>
      </div>
      
      {persona.lastModified && (
        <div style={{ fontSize: '0.75rem', color: '#666', marginTop: '0.5rem' }}>
          Modified: {new Date(persona.lastModified).toLocaleDateString()}
        </div>
      )}
    </div>
  );
}

// Memoize with custom comparison for performance
export default memo(PersonaCard, (prevProps, nextProps) => {
  return (
    prevProps.persona.name === nextProps.persona.name &&
    prevProps.persona.fileCount === nextProps.persona.fileCount &&
    prevProps.persona.ruleCount === nextProps.persona.ruleCount &&
    prevProps.persona.lastModified === nextProps.persona.lastModified &&
    prevProps.isSelected === nextProps.isSelected
  );
});
