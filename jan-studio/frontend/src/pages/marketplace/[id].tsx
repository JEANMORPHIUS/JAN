import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import Head from 'next/head';
import { getPersonaDetails, downloadPersona, ratePersona } from '@/api/marketplace';

interface PersonaDetail {
  persona: {
    id: number;
    name: string;
    author_name?: string;
    description?: string;
    category?: string;
    downloads: number;
    rating: number;
    rating_count: number;
    version: string;
    created_at: string;
  };
  files: Array<{
    id: number;
    file_path: string;
    file_content: string;
    version: string;
  }>;
  ratings: Array<{
    id: number;
    username?: string;
    rating: number;
    comment?: string;
    created_at: string;
  }>;
}

export default function PersonaDetailPage() {
  const router = useRouter();
  const { id } = router.query;
  const [data, setData] = useState<PersonaDetail | null>(null);
  const [loading, setLoading] = useState(true);
  const [downloading, setDownloading] = useState(false);
  const [rating, setRating] = useState(0);
  const [comment, setComment] = useState('');
  const [submittingRating, setSubmittingRating] = useState(false);
  const [message, setMessage] = useState<{ type: 'success' | 'error'; text: string } | null>(null);

  useEffect(() => {
    if (id) {
      loadPersona();
    }
  }, [id]);

  const loadPersona = async () => {
    try {
      setLoading(true);
      const data = await getPersonaDetails(Number(id));
      setData(data);
    } catch (err) {
      console.error('Failed to load persona:', err);
      setMessage({ type: 'error', text: 'Failed to load persona' });
    } finally {
      setLoading(false);
    }
  };

  const handleDownload = async () => {
    try {
      setDownloading(true);
      setMessage(null);
      const result = await downloadPersona(Number(id));
      setMessage({ type: 'success', text: 'Downloaded successfully!' });
      
      // Trigger file download
      const blob = new Blob([JSON.stringify(result.files, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `${result.persona.name}-persona.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      
      // Reload to update download count
      await loadPersona();
    } catch (err: any) {
      setMessage({ type: 'error', text: err.response?.data?.detail || 'Download failed' });
    } finally {
      setDownloading(false);
    }
  };

  const handleRate = async () => {
    if (rating < 1 || rating > 5) {
      setMessage({ type: 'error', text: 'Please select a rating between 1 and 5' });
      return;
    }

    try {
      setSubmittingRating(true);
      setMessage(null);
      await ratePersona(Number(id), rating, comment);
      setMessage({ type: 'success', text: 'Rating submitted!' });
      setRating(0);
      setComment('');
      await loadPersona();
    } catch (err: any) {
      setMessage({ type: 'error', text: err.response?.data?.detail || 'Failed to submit rating' });
    } finally {
      setSubmittingRating(false);
    }
  };

  if (loading) {
    return (
      <>
        <Head>
          <title>Loading... - JAN Marketplace</title>
        </Head>
        <div className="container">
          <div className="card">
            <div className="loading">Loading persona...</div>
          </div>
        </div>
      </>
    );
  }

  if (!data) {
    return (
      <>
        <Head>
          <title>Not Found - JAN Marketplace</title>
        </Head>
        <div className="container">
          <div className="card">
            <h2>Persona Not Found</h2>
            <button
              className="button"
              onClick={() => router.push('/marketplace')}
            >
              Back to Marketplace
            </button>
          </div>
        </div>
      </>
    );
  }

  const { persona, files, ratings } = data;

  return (
    <>
      <Head>
        <title>{persona.name} - JAN Marketplace</title>
        <meta name="description" content={persona.description} />
      </Head>

      <div className="header">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <h1>{persona.name}</h1>
            <p>by {persona.author_name || 'Unknown'}</p>
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
        {message && (
          <div className={message.type === 'success' ? 'success' : 'error'} style={{ marginBottom: '1rem' }}>
            {message.text}
          </div>
        )}

        <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '2rem' }}>
          <div>
            <div className="card" style={{ marginBottom: '1.5rem' }}>
              <h2>Description</h2>
              <p style={{ color: '#ccc', lineHeight: '1.6' }}>
                {persona.description || 'No description provided.'}
              </p>
            </div>

            <div className="card" style={{ marginBottom: '1.5rem' }}>
              <h2>Files ({files.length})</h2>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                {files.map((file) => (
                  <div
                    key={file.id}
                    style={{
                      padding: '0.75rem',
                      backgroundColor: '#0a0a0a',
                      border: '1px solid #333',
                      borderRadius: '4px',
                      fontFamily: 'monospace',
                      fontSize: '0.875rem',
                    }}
                  >
                    {file.file_path} (v{file.version})
                  </div>
                ))}
              </div>
            </div>

            <div className="card">
              <h2>Ratings ({ratings.length})</h2>
              {ratings.length === 0 ? (
                <p style={{ color: '#999' }}>No ratings yet. Be the first to rate!</p>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                  {ratings.map((r) => (
                    <div
                      key={r.id}
                      style={{
                        padding: '1rem',
                        backgroundColor: '#0a0a0a',
                        border: '1px solid #333',
                        borderRadius: '4px',
                      }}
                    >
                      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
                        <div>
                          <strong>{r.username || 'Anonymous'}</strong>
                          <span style={{ marginLeft: '0.5rem', color: '#ff9800' }}>
                            {'⭐'.repeat(r.rating)}
                          </span>
                        </div>
                        <div style={{ fontSize: '0.875rem', color: '#666' }}>
                          {new Date(r.created_at).toLocaleDateString()}
                        </div>
                      </div>
                      {r.comment && (
                        <p style={{ color: '#ccc', fontSize: '0.875rem', margin: 0 }}>
                          {r.comment}
                        </p>
                      )}
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

          <div>
            <div className="card" style={{ marginBottom: '1.5rem' }}>
              <h2>Stats</h2>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                <div>
                  <div style={{ color: '#999', fontSize: '0.875rem', marginBottom: '0.25rem' }}>Rating</div>
                  <div style={{ fontSize: '1.5rem', fontWeight: 600 }}>
                    ⭐ {persona.rating.toFixed(1)}
                    <span style={{ fontSize: '0.875rem', color: '#666', marginLeft: '0.5rem' }}>
                      ({persona.rating_count} reviews)
                    </span>
                  </div>
                </div>
                <div>
                  <div style={{ color: '#999', fontSize: '0.875rem', marginBottom: '0.25rem' }}>Downloads</div>
                  <div style={{ fontSize: '1.5rem', fontWeight: 600 }}>📥 {persona.downloads}</div>
                </div>
                {persona.category && (
                  <div>
                    <div style={{ color: '#999', fontSize: '0.875rem', marginBottom: '0.25rem' }}>Category</div>
                    <div style={{
                      display: 'inline-block',
                      padding: '0.5rem 1rem',
                      backgroundColor: '#1a1a2a',
                      border: '1px solid #444',
                      borderRadius: '4px',
                      fontFamily: 'monospace',
                    }}>
                      {persona.category}
                    </div>
                  </div>
                )}
                <div>
                  <div style={{ color: '#999', fontSize: '0.875rem', marginBottom: '0.25rem' }}>Version</div>
                  <div style={{ fontFamily: 'monospace' }}>v{persona.version}</div>
                </div>
                <div>
                  <div style={{ color: '#999', fontSize: '0.875rem', marginBottom: '0.25rem' }}>Created</div>
                  <div>{new Date(persona.created_at).toLocaleDateString()}</div>
                </div>
              </div>
            </div>

            <div className="card" style={{ marginBottom: '1.5rem' }}>
              <button
                className="button"
                onClick={handleDownload}
                disabled={downloading}
                style={{ width: '100%', marginBottom: '1rem' }}
              >
                {downloading ? 'Downloading...' : '📥 Download Persona'}
              </button>
            </div>

            <div className="card">
              <h2>Rate This Persona</h2>
              <div style={{ marginBottom: '1rem' }}>
                <label className="label">Rating (1-5 stars)</label>
                <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '0.5rem' }}>
                  {[1, 2, 3, 4, 5].map((star) => (
                    <button
                      key={star}
                      onClick={() => setRating(star)}
                      style={{
                        fontSize: '1.5rem',
                        background: 'none',
                        border: 'none',
                        cursor: 'pointer',
                        color: rating >= star ? '#ff9800' : '#666',
                        padding: 0,
                      }}
                    >
                      ⭐
                    </button>
                  ))}
                </div>
                {rating > 0 && (
                  <div style={{ fontSize: '0.875rem', color: '#999' }}>
                    Selected: {rating} star{rating !== 1 ? 's' : ''}
                  </div>
                )}
              </div>
              <div style={{ marginBottom: '1rem' }}>
                <label className="label">Comment (optional)</label>
                <textarea
                  className="textarea"
                  value={comment}
                  onChange={(e) => setComment(e.target.value)}
                  placeholder="Share your thoughts..."
                  rows={3}
                />
              </div>
              <button
                className="button"
                onClick={handleRate}
                disabled={submittingRating || rating < 1}
                style={{ width: '100%' }}
              >
                {submittingRating ? 'Submitting...' : 'Submit Rating'}
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

