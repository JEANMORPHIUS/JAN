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
 * Prompt Templates Component
 */

import { useState, useMemo, useEffect } from 'react';

interface PromptTemplate {
  name: string;
  description: string;
  content: string;
  variables?: string[];
  category: 'story' | 'lyric' | 'educational' | 'reflection' | 'question';
}

const DEFAULT_TEMPLATES: PromptTemplate[] = [
  {
    name: 'Story - Personal Journey',
    description: 'A personal story about transformation',
    content: 'Write a story about {{topic}} that shows the journey from {{start}} to {{end}}. Include moments of {{challenge}} and {{breakthrough}}.',
    variables: ['topic', 'start', 'end', 'challenge', 'breakthrough'],
    category: 'story',
  },
  {
    name: 'Lyric - Purpose Over Performance',
    description: 'A song lyric about purpose',
    content: 'Write lyrics about {{theme}} that emphasize purpose over performance. The message should be {{tone}} and {{mood}}.',
    variables: ['theme', 'tone', 'mood'],
    category: 'lyric',
  },
  {
    name: 'Educational - Ancient Blueprint',
    description: 'Educational content about the Ancient Blueprint',
    content: 'Explain the Ancient Blueprint in the context of {{context}}. Focus on how it relates to {{connection}} and why {{importance}}.',
    variables: ['context', 'connection', 'importance'],
    category: 'educational',
  },
  {
    name: 'Reflection - Signal Interference',
    description: 'A reflection on clearing signal interference',
    content: 'Reflect on how {{interference_type}} has blocked the signal in your life. Share how {{method}} helped clear it.',
    variables: ['interference_type', 'method'],
    category: 'reflection',
  },
  {
    name: 'Question - Third Call',
    description: 'A thought-provoking question about the Third Call',
    content: 'What does it mean when you hear the call {{number}} times? How do you recognize {{recognition}} and respond with {{response}}?',
    variables: ['number', 'recognition', 'response'],
    category: 'question',
  },
];

interface PromptTemplatesProps {
  persona?: string;
  onSelect: (template: PromptTemplate) => void;
  onClose?: () => void;
}

export default function PromptTemplates({ persona, onSelect, onClose }: PromptTemplatesProps) {
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [savedTemplates, setSavedTemplates] = useState<PromptTemplate[]>([]);
  const [showSaveForm, setShowSaveForm] = useState(false);
  const [newTemplate, setNewTemplate] = useState<Partial<PromptTemplate>>({});
  
  // Load saved templates from localStorage
  useEffect(() => {
    try {
      const stored = localStorage.getItem('jan-prompt-templates');
      if (stored) {
        setSavedTemplates(JSON.parse(stored));
      }
    } catch (err) {
      console.error('Failed to load saved templates:', err);
    }
  }, []);

  const categories = useMemo(() => {
    const cats = Array.from(new Set(DEFAULT_TEMPLATES.map(t => t.category)));
    return ['all', ...cats];
  }, []);

  const allTemplates = useMemo(() => {
    return [...DEFAULT_TEMPLATES, ...savedTemplates];
  }, [savedTemplates]);

  const filteredTemplates = useMemo(() => {
    let filtered = allTemplates;

    if (selectedCategory !== 'all') {
      filtered = filtered.filter(t => t.category === selectedCategory);
    }

    if (searchQuery.trim()) {
      const query = searchQuery.toLowerCase();
      filtered = filtered.filter(t =>
        t.name.toLowerCase().includes(query) ||
        t.description.toLowerCase().includes(query)
      );
    }

    return filtered;
  }, [allTemplates, selectedCategory, searchQuery]);
  
  const saveTemplate = () => {
    if (!newTemplate.name || !newTemplate.content) return;
    
    const template: PromptTemplate = {
      name: newTemplate.name,
      description: newTemplate.description || '',
      content: newTemplate.content,
      variables: newTemplate.variables,
      category: newTemplate.category || 'story',
    };
    
    const updated = [...savedTemplates, template];
    setSavedTemplates(updated);
    localStorage.setItem('jan-prompt-templates', JSON.stringify(updated));
    setShowSaveForm(false);
    setNewTemplate({});
  };
  
  const deleteTemplate = (name: string) => {
    const updated = savedTemplates.filter(t => t.name !== name);
    setSavedTemplates(updated);
    localStorage.setItem('jan-prompt-templates', JSON.stringify(updated));
  };

  const processTemplate = (template: PromptTemplate): string => {
    let content = template.content;
    const date = new Date().toLocaleDateString();
    
    // Replace common variables
    content = content.replace(/\{\{persona_name\}\}/g, persona || 'the persona');
    content = content.replace(/\{\{date\}\}/g, date);
    
    return content;
  };

  return (
    <div className="card" style={{ maxHeight: '600px', overflowY: 'auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <h2>Prompt Templates</h2>
        <div style={{ display: 'flex', gap: '0.5rem' }}>
          <button
            className="button"
            onClick={() => setShowSaveForm(!showSaveForm)}
            style={{ padding: '0.5rem 1rem', fontSize: '0.875rem' }}
            aria-label="Save new template"
          >
            + Save Template
          </button>
          {onClose && (
            <button
              className="button"
              onClick={onClose}
              aria-label="Close templates"
            >
              Close
            </button>
          )}
        </div>
      </div>
      
      {showSaveForm && (
        <div className="card" style={{ marginBottom: '1rem', padding: '1rem' }}>
          <h3 style={{ marginTop: 0, marginBottom: '1rem' }}>Save New Template</h3>
          <input
            type="text"
            className="input"
            placeholder="Template name"
            value={newTemplate.name || ''}
            onChange={(e) => setNewTemplate({ ...newTemplate, name: e.target.value })}
            style={{ marginBottom: '0.5rem' }}
            aria-label="Template name"
          />
          <input
            type="text"
            className="input"
            placeholder="Description"
            value={newTemplate.description || ''}
            onChange={(e) => setNewTemplate({ ...newTemplate, description: e.target.value })}
            style={{ marginBottom: '0.5rem' }}
            aria-label="Template description"
          />
          <textarea
            className="textarea"
            placeholder="Template content (use {{variable}} for variables)"
            value={newTemplate.content || ''}
            onChange={(e) => setNewTemplate({ ...newTemplate, content: e.target.value })}
            style={{ minHeight: '150px', marginBottom: '0.5rem' }}
            aria-label="Template content"
          />
          <select
            className="input"
            value={newTemplate.category || 'story'}
            onChange={(e) => setNewTemplate({ ...newTemplate, category: e.target.value as any })}
            style={{ marginBottom: '0.5rem' }}
            aria-label="Template category"
          >
            <option value="story">Story</option>
            <option value="lyric">Lyric</option>
            <option value="educational">Educational</option>
            <option value="reflection">Reflection</option>
            <option value="question">Question</option>
          </select>
          <div style={{ display: 'flex', gap: '0.5rem' }}>
            <button
              className="button"
              onClick={saveTemplate}
              disabled={!newTemplate.name || !newTemplate.content}
              aria-label="Save template"
            >
              Save
            </button>
            <button
              className="button"
              onClick={() => {
                setShowSaveForm(false);
                setNewTemplate({});
              }}
              style={{ backgroundColor: '#666' }}
              aria-label="Cancel"
            >
              Cancel
            </button>
          </div>
        </div>
      )}

      {/* Search */}
      <input
        type="text"
        className="input"
        placeholder="Search templates..."
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
        style={{ marginBottom: '1rem' }}
        aria-label="Search prompt templates"
      />

      {/* Category Filter */}
      <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1rem', flexWrap: 'wrap' }}>
        {categories.map(category => (
          <button
            key={category}
            className="button"
            onClick={() => setSelectedCategory(category)}
            style={{
              padding: '0.5rem 1rem',
              fontSize: '0.875rem',
              backgroundColor: selectedCategory === category ? '#0070f3' : '#1a1a1a',
              border: `1px solid ${selectedCategory === category ? '#0070f3' : '#333'}`,
            }}
            aria-pressed={selectedCategory === category}
          >
            {category.charAt(0).toUpperCase() + category.slice(1)}
          </button>
        ))}
      </div>

      {/* Templates List */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
        {filteredTemplates.map((template, idx) => (
          <div
            key={idx}
            className="card"
            style={{
              padding: '1rem',
              border: '1px solid #333',
              cursor: 'pointer',
              transition: 'all 0.2s',
            }}
            onClick={() => onSelect({
              ...template,
              content: processTemplate(template),
            })}
            onKeyDown={(e) => {
              if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                onSelect({
                  ...template,
                  content: processTemplate(template),
                });
              }
            }}
            tabIndex={0}
            role="button"
            aria-label={`Select template: ${template.name}`}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start', marginBottom: '0.5rem' }}>
              <div style={{ flex: 1 }}>
                <h3 style={{ margin: 0, marginBottom: '0.25rem', fontSize: '1rem' }}>
                  {template.name}
                </h3>
                <p style={{ margin: 0, color: '#999', fontSize: '0.875rem' }}>
                  {template.description}
                </p>
              </div>
              <div style={{ display: 'flex', gap: '0.5rem', alignItems: 'center' }}>
                <span
                  style={{
                    padding: '0.25rem 0.5rem',
                    backgroundColor: '#1a1a2a',
                    border: '1px solid #444',
                    borderRadius: '4px',
                    fontSize: '0.75rem',
                    textTransform: 'capitalize',
                  }}
                >
                  {template.category}
                </span>
                {savedTemplates.some(t => t.name === template.name) && (
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      deleteTemplate(template.name);
                    }}
                    style={{
                      padding: '0.25rem 0.5rem',
                      backgroundColor: '#d32f2f',
                      border: 'none',
                      borderRadius: '4px',
                      color: 'white',
                      fontSize: '0.75rem',
                      cursor: 'pointer',
                    }}
                    aria-label={`Delete template ${template.name}`}
                  >
                    Delete
                  </button>
                )}
              </div>
            </div>
            <div
              style={{
                fontSize: '0.875rem',
                color: '#666',
                fontFamily: 'monospace',
                backgroundColor: '#0a0a0a',
                padding: '0.75rem',
                borderRadius: '4px',
                marginTop: '0.5rem',
              }}
            >
              {processTemplate(template)}
            </div>
            {template.variables && template.variables.length > 0 && (
              <div style={{ fontSize: '0.75rem', color: '#666', marginTop: '0.5rem' }}>
                Variables: {template.variables.join(', ')}
              </div>
            )}
          </div>
        ))}
      </div>

      {filteredTemplates.length === 0 && (
        <p style={{ color: '#999', textAlign: 'center', padding: '2rem' }}>
          No templates found matching your search.
        </p>
      )}
    </div>
  );
}
