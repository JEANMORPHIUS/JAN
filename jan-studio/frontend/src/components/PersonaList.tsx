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
import { VirtualizedList } from './VirtualizedList';
import { usePersonas, useCreatePersona, useDeletePersona } from '@/hooks/usePersonas';
import LoadingState from './LoadingState';

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
  const [searchQuery, setSearchQuery] = useState('');
  const [debouncedSearchQuery, setDebouncedSearchQuery] = useState('');
  const [sortBy, setSortBy] = useState<'name' | 'date' | 'files'>('name');
  
  // Use React Query for data fetching
  const { data: personas = [], isLoading: loadingPersonas, refetch } = usePersonas();
  const createPersonaMutation = useCreatePersona();
  const deletePersonaMutation = useDeletePersona();
  
  // Debounce search query
  useEffect(() => {
    const debounced = debounce((value: string) => {
      setDebouncedSearchQuery(value);
    }, 300);
    
    debounced(searchQuery);
  }, [searchQuery]);
  
  // Refetch when refresh is called
  useEffect(() => {
    if (onRefresh) {
      refetch();
    }
  }, [onRefresh, refetch]);

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
      await createPersonaMutation.mutateAsync(data.name);
      // TODO: Apply template based on data.template
      setShowCreateForm(false);
      onSelectPersona(data.name);
      onRefresh();
    } catch (err) {
      console.error('Failed to create persona:', err);
    }
  };

  const handleDeletePersona = async (name: string) => {
    try {
      await deletePersonaMutation.mutateAsync(name);
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
        <LoadingState message="Loading personas..." size="small" />
      ) : filteredAndSortedPersonas.length === 0 ? (
        <div className="card">
          <p style={{ color: '#999', fontSize: '0.875rem', textAlign: 'center' }}>
            {searchQuery.trim()
              ? `No personas found matching "${searchQuery}"`
              : 'No personas found. Create one to get started.'}
          </p>
        </div>
      ) : (
        {needsVirtualization ? (
          <div style={{ height: '600px' }}>
            <VirtualizedList
              items={filteredAndSortedPersonas}
              estimateSize={120}
              renderItem={(persona, index) => (
                <div style={{ padding: '0.5rem' }}>
                  <PersonaCard
                    persona={persona}
                    onEdit={onSelectPersona}
                    onDelete={handleDeletePersona}
                    isSelected={selectedPersona === persona.name}
                  />
                </div>
              )}
            />
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
      )}
    </div>
  );
}

