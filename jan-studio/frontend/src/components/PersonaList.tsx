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

import { useState, useEffect, useMemo, useRef } from 'react';
import PersonaCard, { PersonaInfo } from './PersonaCard';
import PersonaForm, { PersonaFormData } from './PersonaForm';
import { getPersonas, createPersona, deletePersona, getPersonaFiles } from '@/api/personas';
import { debounce, shouldVirtualize } from '@/utils/performance';

interface PersonaListProps {
  selectedPersona: string | null;
  onSelectPersona: (name: string) => void;
  loading: boolean;
  onRefresh: () => void;
}

export default function PersonaList({
  selectedPersona,
  onSelectPersona,
  loading,
  onRefresh,
}: PersonaListProps) {
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [personas, setPersonas] = useState<PersonaInfo[]>([]);
  const [loadingPersonas, setLoadingPersonas] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [debouncedSearchQuery, setDebouncedSearchQuery] = useState('');
  const [sortBy, setSortBy] = useState<'name' | 'date' | 'files'>('name');
  
  // Debounce search query
  useEffect(() => {
    const debounced = debounce((value: string) => {
      setDebouncedSearchQuery(value);
    }, 300);
    
    debounced(searchQuery);
  }, [searchQuery]);

  useEffect(() => {
    loadPersonas();
  }, []);

  const loadPersonas = async () => {
    try {
      setLoadingPersonas(true);
      const personaNames = await getPersonas();
      
      // Load details for each persona
      const personaDetails = await Promise.all(
        personaNames.map(async (name) => {
          try {
            const files = await getPersonaFiles(name);
            return {
              name,
              fileCount: files.length,
              ruleCount: files.filter(f => f.includes('rules') || f.includes('profile')).length,
            } as PersonaInfo;
          } catch {
            return { name, fileCount: 0, ruleCount: 0 } as PersonaInfo;
          }
        })
      );
      
      setPersonas(personaDetails);
    } catch (err) {
      console.error('Failed to load personas:', err);
    } finally {
      setLoadingPersonas(false);
    }
  };

  // Filter and sort personas
  const filteredAndSortedPersonas = useMemo(() => {
    let filtered = personas;

    // Filter by debounced search query
    if (debouncedSearchQuery.trim()) {
      const query = debouncedSearchQuery.toLowerCase();
      filtered = filtered.filter(
        (persona) =>
          persona.name.toLowerCase().includes(query)
      );
    }

    // Sort
    const sorted = [...filtered].sort((a, b) => {
      switch (sortBy) {
        case 'name':
          return a.name.localeCompare(b.name);
        case 'files':
          return b.fileCount - a.fileCount;
        case 'date':
          // If we had dates, we'd sort by them. For now, fall back to name.
          return a.name.localeCompare(b.name);
        default:
          return 0;
      }
    });

    return sorted;
  }, [personas, debouncedSearchQuery, sortBy]);
  
  // Check if virtualization is needed
  const needsVirtualization = shouldVirtualize(filteredAndSortedPersonas.length, 50);

  const handleCreatePersona = async (data: PersonaFormData) => {
    try {
      await createPersona(data.name);
      // TODO: Apply template based on data.template
      await loadPersonas();
      setShowCreateForm(false);
      onSelectPersona(data.name);
      onRefresh();
    } catch (err) {
      console.error('Failed to create persona:', err);
    }
  };

  const handleDeletePersona = async (name: string) => {
    try {
      await deletePersona(name);
      await loadPersonas();
      if (selectedPersona === name) {
        onSelectPersona('');
      }
      onRefresh();
    } catch (err) {
      console.error('Failed to delete persona:', err);
    }
  };

  if (showCreateForm) {
    return (
      <div>
        <PersonaForm
          onSubmit={handleCreatePersona}
          onCancel={() => setShowCreateForm(false)}
        />
      </div>
    );
  }

  return (
    <div>
      <div className="card" style={{ marginBottom: '1.5rem' }}>
        <h2>Personas</h2>
        
        {/* Search Input */}
        <input
          type="text"
          className="input"
          placeholder="Search personas..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          style={{ marginBottom: '0.75rem' }}
          aria-label="Search personas"
          aria-describedby="search-help"
        />
        {needsVirtualization && (
          <div id="search-help" style={{ fontSize: '0.75rem', color: '#666', marginTop: '0.25rem' }}>
            Large list detected - virtualization active
          </div>
        )}

        {/* Sort Selector */}
        <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '0.75rem' }}>
          <label
            htmlFor="sort-select"
            style={{ fontSize: '0.75rem', color: '#999', alignSelf: 'center' }}
          >
            Sort by:
          </label>
          <select
            id="sort-select"
            className="input"
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value as 'name' | 'date' | 'files')}
            style={{ flex: 1, padding: '0.5rem', fontSize: '0.875rem' }}
            aria-label="Sort personas"
          >
            <option value="name">Name</option>
            <option value="files">File Count</option>
            <option value="date">Date</option>
          </select>
        </div>

        <button
          className="button"
          onClick={() => setShowCreateForm(true)}
          style={{ width: '100%' }}
          aria-label="Create new persona"
        >
          + Create New Persona
        </button>
      </div>

      {loadingPersonas ? (
        <div className="card" role="status" aria-live="polite">
          <div className="loading">Loading personas...</div>
        </div>
      ) : filteredAndSortedPersonas.length === 0 ? (
        <div className="card">
          <p style={{ color: '#999', fontSize: '0.875rem', textAlign: 'center' }}>
            {searchQuery.trim()
              ? `No personas found matching "${searchQuery}"`
              : 'No personas found. Create one to get started.'}
          </p>
        </div>
      ) : (
        <div
          style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}
          role="list"
          aria-label="Persona list"
        >
          {filteredAndSortedPersonas.length !== personas.length && (
            <div
              style={{
                fontSize: '0.75rem',
                color: '#999',
                padding: '0.5rem',
                textAlign: 'center',
              }}
            >
              Showing {filteredAndSortedPersonas.length} of {personas.length} personas
            </div>
          )}
          {filteredAndSortedPersonas.map((persona) => (
            <PersonaCard
              key={persona.name}
              persona={persona}
              onEdit={onSelectPersona}
              onDelete={handleDeletePersona}
              isSelected={selectedPersona === persona.name}
            />
          ))}
        </div>
      )}
    </div>
  );
}

