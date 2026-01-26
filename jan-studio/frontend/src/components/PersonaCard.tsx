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

import { useState } from 'react';

interface PersonaCardProps {
  persona: PersonaInfo;
  onEdit: (name: string) => void;
  onDelete: (name: string) => void;
}

export interface PersonaInfo {
  name: string;
  description?: string;
  ruleCount?: number;
  lastModified?: string;
  fileCount?: number;
}

export default function PersonaCard({ persona, onEdit, onDelete }: PersonaCardProps) {
  const [showDeleteConfirm, setShowDeleteConfirm] = useState(false);

  const handleDelete = () => {
    if (showDeleteConfirm) {
      onDelete(persona.name);
      setShowDeleteConfirm(false);
    } else {
      setShowDeleteConfirm(true);
    }
  };

  const formatDate = (dateString?: string) => {
    if (!dateString) return 'Unknown';
    try {
      const date = new Date(dateString);
      return date.toLocaleDateString() + ' ' + date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    } catch {
      return 'Unknown';
    }
  };

  return (
    <div className="persona-card">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start', marginBottom: '1rem' }}>
        <div>
          <h3 style={{ margin: 0, marginBottom: '0.5rem', fontFamily: 'monospace' }}>
            {persona.name}
          </h3>
          {persona.description && (
            <p style={{ margin: 0, color: '#999', fontSize: '0.875rem' }}>
              {persona.description}
            </p>
          )}
        </div>
        <div style={{ display: 'flex', gap: '0.5rem' }}>
          <button
            className="button"
            onClick={() => onEdit(persona.name)}
            style={{ padding: '0.25rem 0.75rem', fontSize: '0.75rem' }}
          >
            Edit
          </button>
          <button
            className="button"
            onClick={handleDelete}
            style={{
              padding: '0.25rem 0.75rem',
              fontSize: '0.75rem',
              backgroundColor: showDeleteConfirm ? '#d32f2f' : '#666',
            }}
          >
            {showDeleteConfirm ? 'Confirm' : 'Delete'}
          </button>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '1rem', fontSize: '0.875rem' }}>
        <div>
          <div style={{ color: '#999', marginBottom: '0.25rem' }}>Files</div>
          <div style={{ fontFamily: 'monospace' }}>{persona.fileCount || 0}</div>
        </div>
        <div>
          <div style={{ color: '#999', marginBottom: '0.25rem' }}>Rules</div>
          <div style={{ fontFamily: 'monospace' }}>{persona.ruleCount || 0}</div>
        </div>
        <div>
          <div style={{ color: '#999', marginBottom: '0.25rem' }}>Modified</div>
          <div style={{ fontFamily: 'monospace', fontSize: '0.75rem' }}>
            {formatDate(persona.lastModified)}
          </div>
        </div>
      </div>

      {showDeleteConfirm && (
        <div style={{
          marginTop: '1rem',
          padding: '0.75rem',
          backgroundColor: '#2a1a1a',
          border: '1px solid #d32f2f',
          borderRadius: '4px',
          fontSize: '0.875rem',
        }}>
          Are you sure? This will delete all files for this persona.
        </div>
      )}
    </div>
  );
}

