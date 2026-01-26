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

interface PersonaFormProps {
  onSubmit: (data: PersonaFormData) => void;
  onCancel?: () => void;
  initialData?: Partial<PersonaFormData>;
}

export interface PersonaFormData {
  name: string;
  description: string;
  template: 'storyteller' | 'music' | 'educator' | 'blank';
}

const TEMPLATES = [
  { value: 'storyteller', label: 'Storyteller', description: 'Creative writing and storytelling' },
  { value: 'music', label: 'Music Producer', description: 'Audio and music generation' },
  { value: 'educator', label: 'Educator', description: 'Teaching and explanatory content' },
  { value: 'blank', label: 'Blank', description: 'Start from scratch' },
] as const;

export default function PersonaForm({ onSubmit, onCancel, initialData }: PersonaFormProps) {
  const [formData, setFormData] = useState<PersonaFormData>({
    name: initialData?.name || '',
    description: initialData?.description || '',
    template: initialData?.template || 'blank',
  });
  const [errors, setErrors] = useState<{ [key: string]: string }>({});

  const validate = (): boolean => {
    const newErrors: { [key: string]: string } = {};

    if (!formData.name.trim()) {
      newErrors.name = 'Name is required';
    } else if (!/^[a-z0-9_-]+$/.test(formData.name)) {
      newErrors.name = 'Name must contain only lowercase letters, numbers, hyphens, and underscores';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (validate()) {
      onSubmit(formData);
    }
  };

  return (
    <div className="card">
      <h2>Create New Persona</h2>
      
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '1.5rem' }}>
          <label className="label">
            Persona Name <span style={{ color: '#d32f2f' }}>*</span>
          </label>
          <input
            type="text"
            className="input"
            value={formData.name}
            onChange={(e) => setFormData({ ...formData, name: e.target.value })}
            placeholder="e.g., storyteller, music-producer"
            style={{
              fontFamily: 'monospace',
              backgroundColor: errors.name ? '#ffebee' : undefined,
            }}
          />
          {errors.name && <div className="error">{errors.name}</div>}
          <div style={{ fontSize: '0.75rem', color: '#666', marginTop: '0.25rem' }}>
            Use lowercase letters, numbers, hyphens, and underscores only
          </div>
        </div>

        <div style={{ marginBottom: '1.5rem' }}>
          <label className="label">Description</label>
          <textarea
            className="textarea"
            value={formData.description}
            onChange={(e) => setFormData({ ...formData, description: e.target.value })}
            placeholder="Brief description of this persona's purpose..."
            rows={3}
          />
        </div>

        <div style={{ marginBottom: '1.5rem' }}>
          <label className="label">Template</label>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '1rem' }}>
            {TEMPLATES.map((template) => (
              <div
                key={template.value}
                onClick={() => setFormData({ ...formData, template: template.value as any })}
                style={{
                  padding: '1rem',
                  border: formData.template === template.value ? '2px solid #0070f3' : '1px solid #333',
                  borderRadius: '4px',
                  cursor: 'pointer',
                  backgroundColor: formData.template === template.value ? '#1a1a1a' : '#0a0a0a',
                  transition: 'all 0.2s',
                }}
              >
                <div style={{ fontWeight: 600, marginBottom: '0.5rem' }}>
                  {template.label}
                </div>
                <div style={{ fontSize: '0.875rem', color: '#999' }}>
                  {template.description}
                </div>
              </div>
            ))}
          </div>
        </div>

        <div style={{ display: 'flex', gap: '1rem' }}>
          <button type="submit" className="button">
            Create Persona
          </button>
          {onCancel && (
            <button type="button" className="button" onClick={onCancel} style={{ backgroundColor: '#666' }}>
              Cancel
            </button>
          )}
        </div>
      </form>
    </div>
  );
}

