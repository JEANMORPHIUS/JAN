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

import { useState, useEffect, memo, useRef } from 'react';
import { getTemplates, getTemplate, instantiateTemplate, savePersonaAsTemplate } from '@/api/templates';
import PersonaForm, { PersonaFormData } from './PersonaForm';
import { useFocusTrap, useReturnFocus } from '@/hooks/useFocusManagement';

interface Template {
  name: string;
  description?: string;
  category?: string;
  created_at: string;
  file_count: number;
  persona_name?: string;
}

interface TemplateBrowserProps {
  onTemplateSelected: (templateName: string, personaName: string) => void;
  onClose: () => void;
  existingPersonaName?: string;
}

function TemplateBrowser({
  onTemplateSelected,
  onClose,
  existingPersonaName,
}: TemplateBrowserProps) {
  const [templates, setTemplates] = useState<Template[]>([]);
  const [selectedTemplate, setSelectedTemplate] = useState<string | null>(null);
  const [templateDetails, setTemplateDetails] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [instantiating, setInstantiating] = useState(false);
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [message, setMessage] = useState<{ type: 'success' | 'error'; text: string } | null>(null);
  const modalRef = useRef<HTMLDivElement>(null);
  
  // Focus management - TemplateBrowser is always shown as modal
  useFocusTrap(true, modalRef);
  useReturnFocus(true);

  useEffect(() => {
    loadTemplates();
  }, []);

  useEffect(() => {
    if (selectedTemplate) {
      loadTemplateDetails();
    }
  }, [selectedTemplate]);

  const loadTemplates = async () => {
    try {
      setLoading(true);
      const data = await getTemplates();
      setTemplates(data);
    } catch (err) {
      console.error('Failed to load templates:', err);
      setMessage({ type: 'error', text: 'Failed to load templates' });
    } finally {
      setLoading(false);
    }
  };

  const loadTemplateDetails = async () => {
    if (!selectedTemplate) return;

    try {
      const data = await getTemplate(selectedTemplate);
      setTemplateDetails(data);
    } catch (err) {
      console.error('Failed to load template details:', err);
    }
  };

  const handleInstantiate = async (personaName: string) => {
    if (!selectedTemplate) return;

    try {
      setInstantiating(true);
      setMessage(null);
      await instantiateTemplate(selectedTemplate, personaName);
      setMessage({ type: 'success', text: 'Persona created successfully!' });
      setTimeout(() => {
        onTemplateSelected(selectedTemplate, personaName);
        onClose();
      }, 1000);
    } catch (err: any) {
      setMessage({ type: 'error', text: err.response?.data?.detail || 'Failed to create persona' });
    } finally {
      setInstantiating(false);
    }
  };

  const handleSaveAsTemplate = async (templateName: string, description?: string) => {
    if (!existingPersonaName) return;

    try {
      await savePersonaAsTemplate(existingPersonaName, templateName, description);
      setMessage({ type: 'success', text: 'Template saved successfully!' });
      await loadTemplates();
    } catch (err: any) {
      setMessage({ type: 'error', text: err.response?.data?.detail || 'Failed to save template' });
    }
  };

  if (showCreateForm) {
    return (
      <div className="card">
        <h2>Create Persona from Template</h2>
        <PersonaForm
          onSubmit={(data) => handleInstantiate(data.name)}
          onCancel={() => setShowCreateForm(false)}
        />
      </div>
    );
  }

  return (
    <div 
      ref={modalRef}
      className="card"
      role="dialog"
      aria-modal="true"
      aria-label="Template browser"
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <h2>Templates</h2>
        <button 
          className="button" 
          onClick={onClose} 
          style={{ backgroundColor: '#666' }}
          aria-label="Close template browser"
        >
          Close
        </button>
      </div>

      {message && (
        <div className={message.type === 'success' ? 'success' : 'error'} style={{ marginBottom: '1rem' }}>
          {message.text}
        </div>
      )}

      {existingPersonaName && (
        <div style={{ marginBottom: '1rem', padding: '1rem', backgroundColor: '#2a2a2a', borderRadius: '4px' }}>
          <p style={{ marginBottom: '0.5rem', fontSize: '0.875rem' }}>
            Save "{existingPersonaName}" as template:
          </p>
          <input
            type="text"
            className="input"
            placeholder="Template name (e.g., my-custom-template)"
            id="template-name-input"
            style={{ marginBottom: '0.5rem' }}
          />
          <button
            className="button"
            onClick={() => {
              const input = document.getElementById('template-name-input') as HTMLInputElement;
              if (input?.value) {
                handleSaveAsTemplate(input.value);
              }
            }}
          >
            Save as Template
          </button>
        </div>
      )}

      {loading ? (
        <div className="loading">Loading templates...</div>
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: '300px 1fr', gap: '1.5rem' }}>
          <div>
            <h3 style={{ fontSize: '1rem', marginBottom: '1rem' }}>Available Templates</h3>
            {templates.length === 0 ? (
              <p style={{ color: '#999', fontSize: '0.875rem' }}>No templates available</p>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                {templates.map((template) => (
                  <div
                    key={template.name}
                    onClick={() => setSelectedTemplate(template.name)}
                    style={{
                      padding: '1rem',
                      border: selectedTemplate === template.name ? '2px solid #0070f3' : '1px solid #333',
                      borderRadius: '4px',
                      cursor: 'pointer',
                      backgroundColor: selectedTemplate === template.name ? '#1a1a1a' : '#0a0a0a',
                      transition: 'all 0.2s',
                    }}
                  >
                    <div style={{ fontWeight: 600, marginBottom: '0.25rem', fontFamily: 'monospace' }}>
                      {template.name}
                    </div>
                    {template.description && (
                      <div style={{ fontSize: '0.875rem', color: '#999', marginBottom: '0.25rem' }}>
                        {template.description}
                      </div>
                    )}
                    <div style={{ fontSize: '0.75rem', color: '#666' }}>
                      {template.file_count} files
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>

          <div>
            {selectedTemplate && templateDetails ? (
              <div>
                <h3 style={{ fontSize: '1rem', marginBottom: '1rem' }}>Template Details</h3>
                <div style={{ marginBottom: '1rem' }}>
                  <div style={{ marginBottom: '0.5rem' }}>
                    <strong>Name:</strong> <span style={{ fontFamily: 'monospace' }}>{templateDetails.name}</span>
                  </div>
                  {templateDetails.description && (
                    <div style={{ marginBottom: '0.5rem' }}>
                      <strong>Description:</strong> {templateDetails.description}
                    </div>
                  )}
                  {templateDetails.category && (
                    <div style={{ marginBottom: '0.5rem' }}>
                      <strong>Category:</strong> {templateDetails.category}
                    </div>
                  )}
                  <div style={{ marginBottom: '0.5rem' }}>
                    <strong>Files:</strong> {Object.keys(templateDetails.persona_data?.files || {}).length}
                  </div>
                </div>

                <div style={{ marginBottom: '1rem' }}>
                  <h4 style={{ fontSize: '0.875rem', marginBottom: '0.5rem' }}>Files included:</h4>
                  <ul style={{ fontSize: '0.875rem', color: '#999', fontFamily: 'monospace', paddingLeft: '1.5rem' }}>
                    {Object.keys(templateDetails.persona_data?.files || {}).map((file) => (
                      <li key={file}>{file}</li>
                    ))}
                  </ul>
                </div>

                <button
                  className="button"
                  onClick={() => setShowCreateForm(true)}
                  disabled={instantiating}
                  style={{ width: '100%' }}
                >
                  {instantiating ? 'Creating...' : 'Use This Template'}
                </button>
              </div>
            ) : (
              <div style={{ color: '#999', fontSize: '0.875rem' }}>
                Select a template to view details
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

// Memoize TemplateBrowser to prevent unnecessary re-renders
export default memo(TemplateBrowser, (prevProps, nextProps) => {
  return (
    prevProps.existingPersonaName === nextProps.existingPersonaName
  );
});

