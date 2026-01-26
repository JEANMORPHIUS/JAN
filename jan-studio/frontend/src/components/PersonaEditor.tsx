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
import { getPersonaFile, savePersonaFile, getPersonaFiles } from '@/api/personas';

interface PersonaEditorProps {
  personaName: string;
  onSave: () => void;
}

export default function PersonaEditor({ personaName, onSave }: PersonaEditorProps) {
  const [files, setFiles] = useState<string[]>([]);
  const [selectedFile, setSelectedFile] = useState<string | null>(null);
  const [content, setContent] = useState<string>('');
  const [loading, setLoading] = useState(false);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState<{ type: 'success' | 'error'; text: string } | null>(null);

  useEffect(() => {
    loadFiles();
  }, [personaName]);

  useEffect(() => {
    if (selectedFile) {
      loadFileContent();
    }
  }, [selectedFile, personaName]);

  const loadFiles = async () => {
    try {
      setLoading(true);
      const data = await getPersonaFiles(personaName);
      setFiles(data);
      if (data.length > 0 && !selectedFile) {
        setSelectedFile(data[0]);
      }
    } catch (err) {
      console.error('Failed to load files:', err);
    } finally {
      setLoading(false);
    }
  };

  const loadFileContent = async () => {
    if (!selectedFile) return;

    try {
      setLoading(true);
      const data = await getPersonaFile(personaName, selectedFile);
      setContent(data);
    } catch (err) {
      console.error('Failed to load file content:', err);
      setMessage({ type: 'error', text: 'Failed to load file content' });
    } finally {
      setLoading(false);
    }
  };

  const handleSave = async () => {
    if (!selectedFile) return;

    try {
      setSaving(true);
      setMessage(null);
      await savePersonaFile(personaName, selectedFile, content);
      setMessage({ type: 'success', text: 'File saved successfully!' });
      setTimeout(() => setMessage(null), 3000);
      onSave();
    } catch (err) {
      setMessage({ type: 'error', text: 'Failed to save file' });
      console.error('Failed to save file:', err);
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="card">
      <h2>File Editor: {personaName}</h2>

      <div style={{ marginBottom: '1rem' }}>
        <label className="label">Select File:</label>
        <select
          className="input"
          value={selectedFile || ''}
          onChange={(e) => setSelectedFile(e.target.value)}
          style={{ fontFamily: 'monospace' }}
        >
          <option value="">Select a file...</option>
          {files.map((file) => (
            <option key={file} value={file}>
              {file}
            </option>
          ))}
        </select>
      </div>

      {selectedFile && (
        <>
          <div>
            <label className="label">Content:</label>
            <textarea
              className="textarea"
              value={content}
              onChange={(e) => setContent(e.target.value)}
              placeholder="File content..."
              style={{ minHeight: '400px' }}
            />
          </div>

          <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
            <button
              className="button"
              onClick={handleSave}
              disabled={saving}
            >
              {saving ? 'Saving...' : 'Save File'}
            </button>

            {message && (
              <span className={message.type === 'success' ? 'success' : 'error'}>
                {message.text}
              </span>
            )}
          </div>
        </>
      )}

      {loading && <div className="loading">Loading...</div>}
    </div>
  );
}
