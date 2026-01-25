import { useState, useEffect } from 'react';
import Head from 'next/head';
import Link from 'next/link';
import { useRouter } from 'next/router';
import { getPersonas, getCategories } from '@/api/marketplace';

interface Persona {
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
}

export default function Marketplace() {
  const router = useRouter();
  const [personas, setPersonas] = useState<Persona[]>([]);
  const [categories, setCategories] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null);
  const [sortBy, setSortBy] = useState<string>('downloads');

  useEffect(() => {
    loadData();
  }, [selectedCategory, sortBy]);

  const loadData = async () => {
    try {
      setLoading(true);
      const [personasData, categoriesData] = await Promise.all([
        getPersonas({ category: selectedCategory || undefined, sort_by: sortBy }),
        getCategories(),
      ]);
      setPersonas(personasData);
      setCategories(categoriesData);
    } catch (err) {
      console.error('Failed to load marketplace:', err);
    } finally {
      setLoading(false);
    }
  };

  const formatRating = (rating: number) => {
    return rating.toFixed(1);
  };

  const formatDate = (dateString: string) => {
    try {
      return new Date(dateString).toLocaleDateString();
    } catch {
      return dateString;
    }
  };

  return (
    <>
      <Head>
        <title>JAN Marketplace - Browse Personas</title>
        <meta name="description" content="Browse and download JAN personas" />
      </Head>

      <div className="header">
        <h1>JAN Marketplace</h1>
        <p>Discover and download personas created by the community</p>
      </div>

      <div className="container">
        <div style={{ marginBottom: '2rem' }}>
          <div style={{ display: 'flex', gap: '1rem', alignItems: 'center', marginBottom: '1rem' }}>
            <div style={{ flex: 1 }}>
              <label className="label" style={{ marginBottom: '0.5rem' }}>Category:</label>
              <select
                className="input"
                value={selectedCategory || ''}
                onChange={(e) => setSelectedCategory(e.target.value || null)}
                style={{ width: '200px' }}
              >
                <option value="">All Categories</option>
                {categories.map((cat) => (
                  <option key={cat} value={cat}>
                    {cat}
                  </option>
                ))}
              </select>
            </div>

            <div style={{ flex: 1 }}>
              <label className="label" style={{ marginBottom: '0.5rem' }}>Sort By:</label>
              <select
                className="input"
                value={sortBy}
                onChange={(e) => setSortBy(e.target.value)}
                style={{ width: '200px' }}
              >
                <option value="downloads">Most Downloaded</option>
                <option value="rating">Highest Rated</option>
                <option value="created_at">Newest</option>
                <option value="updated_at">Recently Updated</option>
              </select>
            </div>

            <div>
              <button
                className="button"
                style={{ backgroundColor: '#2e7d32' }}
                onClick={() => router.push('/marketplace/submit')}
              >
                + Submit Persona
              </button>
            </div>
          </div>
        </div>

        {loading ? (
          <div className="card">
            <div className="loading">Loading marketplace...</div>
          </div>
        ) : personas.length === 0 ? (
          <div className="card">
            <p style={{ color: '#999', textAlign: 'center' }}>
              No personas found. Be the first to submit one!
            </p>
          </div>
        ) : (
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
            gap: '1.5rem',
          }}>
            {personas.map((persona) => (
              <div
                key={persona.id}
                className="persona-card"
                style={{ cursor: 'pointer', height: '100%' }}
                onClick={() => router.push(`/marketplace/${persona.id}`)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    router.push(`/marketplace/${persona.id}`);
                  }
                }}
                role="link"
                tabIndex={0}
                aria-label={`View ${persona.name} persona`}
              >
                <div style={{ marginBottom: '1rem' }}>
                  <h3 style={{ margin: 0, marginBottom: '0.5rem', fontFamily: 'monospace' }}>
                    {persona.name}
                  </h3>
                  {persona.author_name && (
                    <div style={{ fontSize: '0.875rem', color: '#999' }}>
                      by {persona.author_name}
                    </div>
                  )}
                </div>

                {persona.description && (
                  <p style={{
                    fontSize: '0.875rem',
                    color: '#ccc',
                    marginBottom: '1rem',
                    display: '-webkit-box',
                    WebkitLineClamp: 3,
                    WebkitBoxOrient: 'vertical',
                    overflow: 'hidden',
                  }}>
                    {persona.description}
                  </p>
                )}

                <div style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  marginBottom: '1rem',
                  fontSize: '0.875rem',
                }}>
                  <div>
                    <span style={{ color: '#999' }}>⭐ </span>
                    <span style={{ fontWeight: 600 }}>
                      {formatRating(persona.rating)}
                    </span>
                    <span style={{ color: '#666', marginLeft: '0.25rem' }}>
                      ({persona.rating_count})
                    </span>
                  </div>
                  <div style={{ color: '#999' }}>
                    📥 {persona.downloads}
                  </div>
                </div>

                {persona.category && (
                  <div style={{
                    display: 'inline-block',
                    padding: '0.25rem 0.5rem',
                    backgroundColor: '#1a1a2a',
                    border: '1px solid #444',
                    borderRadius: '4px',
                    fontSize: '0.75rem',
                    fontFamily: 'monospace',
                    marginBottom: '0.5rem',
                  }}>
                    {persona.category}
                  </div>
                )}

                <div style={{ fontSize: '0.75rem', color: '#666', marginTop: '0.5rem' }}>
                  v{persona.version} • {formatDate(persona.created_at)}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </>
  );
}

