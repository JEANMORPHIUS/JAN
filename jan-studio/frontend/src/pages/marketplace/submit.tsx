/** * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 * 
 * 
 * PANGEA IS THE TABLE.
 * YOU DON'T BETRAY THE TABLE.
 * 
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import Head from 'next/head';
import { submitPersona } from '@/api/marketplace';
import { getPersonas, getPersonaFiles } from '@/api/personas';

export default function SubmitPersona() {
  const router = useRouter();
  const [formData, setFormData] = useState({
    name: '',
    author_username: '',
    author_email: '',
    description: '',
    category: '',
  });
  const [selectedPersona, setSelectedPersona] = useState<string>('');
  const [personas, setPersonas] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState<{ type: 'success' | 'error'; text: string } | null>(null);

  useEffect(() => {
    loadPersonas();
  }, []);

  const loadPersonas = async () => {
    try {
      const data = await getPersonas();
      setPersonas(data);
    } catch (err) {
      console.error('Failed to load personas:', err);
    }
  };

  const handleLoadPersona = async () => {
    if (!selectedPersona) return;

    try {
      const files = await getPersonaFiles(selectedPersona);
      // Pre-fill form with persona name
      setFormData({ ...formData, name: selectedPersona });
      setMessage({ type: 'success', text: `Loaded ${files.length} files from ${selectedPersona}` });
    } catch (err) {
      setMessage({ type: 'error', text: 'Failed to load persona files' });
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!formData.name || !formData.author_username || !formData.author_email) {
      setMessage({ type: 'error', text: 'Please fill in all required fields' });
      return;
    }

    try {
      setLoading(true);
      setMessage(null);

      // Get files from selected persona or use empty
      let files: Array<{ path: string; content: string }> = [];
      if (selectedPersona) {
        const personaFiles = await getPersonaFiles(selectedPersona);
        for (const fileName of personaFiles) {
          try {
            const content = await fetch(`/api/jan/personas/${selectedPersona}/files/${fileName}`)
              .then(r => r.text());
            files.push({ path: fileName, content });
          } catch {
            // Skip files that can't be loaded
          }
        }
      }

      await submitPersona({
        name: formData.name,
        author_username: formData.author_username,
        author_email: formData.author_email,
        description: formData.description,
        category: formData.category || undefined,
        files,
      });

      setMessage({ type: 'success', text: 'Persona submitted successfully! It will be reviewed before being published.' });
      setTimeout(() => {
        router.push('/marketplace');
      }, 2000);
    } catch (err: any) {
      setMessage({ type: 'error', text: err.response?.data?.detail || 'Failed to submit persona' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <Head>
        <title>Submit Persona - JAN Marketplace</title>
        <meta name="description" content="Submit your JAN persona to the marketplace" />
      </Head>

      <div className="header">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <h1>Submit Persona</h1>
            <p>Share your JAN persona with the community</p>
          </div>
          <button
            className="button"
            style={{ backgroundColor: '#666' }}
            onClick={() => router.push('/marketplace')}
          >
            ← Back to Marketplace
          </button>
        </div>
      </div>

      <div className="container">
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          {message && (
            <div className={message.type === 'success' ? 'success' : 'error'} style={{ marginBottom: '1rem' }}>
              {message.text}
            </div>
          )}

          <div className="card" style={{ marginBottom: '1.5rem' }}>
            <h2>Load from Existing Persona</h2>
            <p style={{ color: '#999', fontSize: '0.875rem', marginBottom: '1rem' }}>
              Select an existing persona to pre-fill the form with its files.
            </p>
            <div style={{ display: 'flex', gap: '1rem' }}>
              <select
                className="input"
                value={selectedPersona}
                onChange={(e) => setSelectedPersona(e.target.value)}
                style={{ flex: 1 }}
              >
                <option value="">Select a persona...</option>
                {personas.map((persona) => (
                  <option key={persona} value={persona}>
                    {persona}
                  </option>
                ))}
              </select>
              <button
                className="button"
                onClick={handleLoadPersona}
                disabled={!selectedPersona}
              >
                Load Files
              </button>
            </div>
          </div>

          <form onSubmit={handleSubmit}>
            <div className="card" style={{ marginBottom: '1.5rem' }}>
              <h2>Persona Information</h2>

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
                  required
                  style={{ fontFamily: 'monospace' }}
                />
                <div style={{ fontSize: '0.75rem', color: '#666', marginTop: '0.25rem' }}>
                  Use lowercase letters, numbers, hyphens, and underscores only
                </div>
              </div>

              <div style={{ marginBottom: '1.5rem' }}>
                <label className="label">
                  Description <span style={{ color: '#d32f2f' }}>*</span>
                </label>
                <textarea
                  className="textarea"
                  value={formData.description}
                  onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                  placeholder="Describe what this persona does, its purpose, and what makes it unique..."
                  required
                  rows={5}
                />
              </div>

              <div style={{ marginBottom: '1.5rem' }}>
                <label className="label">Category</label>
                <select
                  className="input"
                  value={formData.category}
                  onChange={(e) => setFormData({ ...formData, category: e.target.value })}
                >
                  <option value="">Select a category...</option>
                  <option value="creative">Creative</option>
                  <option value="audio">Audio</option>
                  <option value="education">Education</option>
                  <option value="technical">Technical</option>
                  <option value="other">Other</option>
                </select>
              </div>
            </div>

            <div className="card" style={{ marginBottom: '1.5rem' }}>
              <h2>Author Information</h2>

              <div style={{ marginBottom: '1.5rem' }}>
                <label className="label">
                  Username <span style={{ color: '#d32f2f' }}>*</span>
                </label>
                <input
                  type="text"
                  className="input"
                  value={formData.author_username}
                  onChange={(e) => setFormData({ ...formData, author_username: e.target.value })}
                  placeholder="Your username"
                  required
                />
              </div>

              <div style={{ marginBottom: '1.5rem' }}>
                <label className="label">
                  Email <span style={{ color: '#d32f2f' }}>*</span>
                </label>
                <input
                  type="email"
                  className="input"
                  value={formData.author_email}
                  onChange={(e) => setFormData({ ...formData, author_email: e.target.value })}
                  placeholder="your.email@example.com"
                  required
                />
              </div>
            </div>

            <div style={{ display: 'flex', gap: '1rem' }}>
              <button
                type="submit"
                className="button"
                disabled={loading}
                style={{ flex: 1 }}
              >
                {loading ? 'Submitting...' : 'Submit Persona'}
              </button>
              <button
                type="button"
                onClick={() => router.push('/marketplace')}
                  className="button"
                  style={{ backgroundColor: '#666' }}
                >
                  Cancel
                </button>
              </Link>
            </div>
          </form>
        </div>
      </div>
    </>
  );
}

