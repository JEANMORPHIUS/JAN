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

import { useState, useEffect } from 'react';
import dynamic from 'next/dynamic';
import { getPersonaFile, savePersonaFile } from '@/api/personas';

// Dynamically import markdown editor to avoid SSR issues
let MarkdownIt: any;
let mdParser: any;

if (typeof window !== 'undefined') {
  MarkdownIt = require('markdown-it');
  mdParser = new MarkdownIt(/* markdown-it options */);
}

const MdEditor = dynamic(() => import('react-markdown-editor-lite'), {
  ssr: false,
});

// Import editor styles - we'll override with dark mode
import 'react-markdown-editor-lite/lib/index.css';

interface RuleEditorProps {
  personaName: string;
  fileType: 'core-rules' | 'voice' | 'constraints';
}

const FILE_MAPPING = {
  'core-rules': 'creative_rules.md',
  'voice': 'profile.md',
  'constraints': 'creative_rules.md',
};

export default function RuleEditor({ personaName, fileType }: RuleEditorProps) {
  const [content, setContent] = useState<string>('');
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState<{ type: 'success' | 'error'; text: string } | null>(null);

  useEffect(() => {
    loadContent();
  }, [personaName, fileType]);

  const loadContent = async () => {
    try {
      setLoading(true);
      const fileName = FILE_MAPPING[fileType];
      const data = await getPersonaFile(personaName, fileName);
      setContent(data);
    } catch (err) {
      console.error('Failed to load content:', err);
      setContent('# New File\n\nStart writing...');
    } finally {
      setLoading(false);
    }
  };

  const handleSave = async () => {
    try {
      setSaving(true);
      setMessage(null);
      const fileName = FILE_MAPPING[fileType];
      await savePersonaFile(personaName, fileName, content);
      setMessage({ type: 'success', text: 'Saved successfully!' });
      setTimeout(() => setMessage(null), 3000);
    } catch (err) {
      setMessage({ type: 'error', text: 'Failed to save' });
      console.error('Failed to save:', err);
    } finally {
      setSaving(false);
    }
  };

  const handleEditorChange = ({ text }: { text: string }) => {
    setContent(text);
  };

  if (loading) {
    return (
      <div className="card">
        <div className="loading" aria-live="polite" aria-busy="true">
          Loading editor...
        </div>
      </div>
    );
  }

  return (
    <div className="card">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <h2 style={{ margin: 0, textTransform: 'capitalize' }}>
          {fileType.replace('-', ' ')}
        </h2>
        <button
          className="button"
          onClick={handleSave}
          disabled={saving}
          aria-label={`Save ${fileType}`}
          aria-busy={saving}
        >
          {saving ? 'Saving...' : 'Save'}
        </button>
      </div>

      {message && (
        <div 
          className={message.type === 'success' ? 'success' : 'error'} 
          style={{ marginBottom: '1rem' }}
          role="alert"
          aria-live={message.type === 'error' ? 'assertive' : 'polite'}
        >
          {message.text}
        </div>
      )}

      <div style={{ border: '1px solid #333', borderRadius: '4px', overflow: 'hidden' }}>
        {typeof window !== 'undefined' && mdParser && (
          <MdEditor
            value={content}
            style={{ height: '600px' }}
            renderHTML={(text) => mdParser.render(text)}
            onChange={handleEditorChange}
            config={{
              view: {
                menu: true,
                md: true,
                html: true,
              },
              canView: {
                menu: true,
                md: true,
                html: true,
                fullScreen: true,
                hideMenu: false,
              },
            }}
          />
        )}
      </div>
    </div>
  );
}

