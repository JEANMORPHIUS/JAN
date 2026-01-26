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

import { useState, useEffect, useMemo } from 'react';
import { GenerationResult } from './GenerationForm';
import { getGenerationHistory, saveToHistory } from '@/api/generation';
import { shouldVirtualize } from '@/utils/performance';
import { retryWithBackoff, getUserFriendlyError } from '@/utils/errorHandling';

export interface HistoryEntry extends GenerationResult {
  id: string;
  persona: string;
  prompt: string;
  output_type: string;
}

interface HistoryPanelProps {
  onSelectHistory: (entry: HistoryEntry) => void;
  onCompare?: (entries: HistoryEntry[]) => void;
  currentResult?: GenerationResult;
}

export default function HistoryPanel({ onSelectHistory, onCompare, currentResult }: HistoryPanelProps) {
  const [history, setHistory] = useState<HistoryEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set());
  const [filterPersona, setFilterPersona] = useState<string>('');
  const [filterType, setFilterType] = useState<string>('');

  useEffect(() => {
    loadHistory();
  }, []);

  useEffect(() => {
    if (currentResult) {
      // Auto-save current result to history
      saveToHistory(currentResult);
      loadHistory();
    }
  }, [currentResult]);

  const loadHistory = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await retryWithBackoff(
        () => getGenerationHistory(),
        3,
        1000
      );
      setHistory(data);
    } catch (err) {
      console.error('Failed to load history:', err);
      setError(getUserFriendlyError(err));
    } finally {
      setLoading(false);
    }
  };
  
  // Filter history
  const filteredHistory = useMemo(() => {
    let filtered = history;
    
    if (filterPersona) {
      filtered = filtered.filter(entry => 
        entry.persona.toLowerCase().includes(filterPersona.toLowerCase())
      );
    }
    
    if (filterType) {
      filtered = filtered.filter(entry => 
        entry.output_type === filterType
      );
    }
    
    return filtered;
  }, [history, filterPersona, filterType]);
  
  // Get unique personas and types for filters
  const uniquePersonas = useMemo(() => {
    return Array.from(new Set(history.map(e => e.persona))).sort();
  }, [history]);
  
  const uniqueTypes = useMemo(() => {
    return Array.from(new Set(history.map(e => e.output_type))).sort();
  }, [history]);
  
  // Check if virtualization is needed
  const needsVirtualization = shouldVirtualize(filteredHistory.length, 100);

  const handleSelect = (entry: HistoryEntry) => {
    onSelectHistory(entry);
  };

  const handleToggleSelect = (id: string) => {
    const newSelected = new Set(selectedIds);
    if (newSelected.has(id)) {
      newSelected.delete(id);
    } else {
      newSelected.add(id);
    }
    setSelectedIds(newSelected);
  };

  const handleCompare = () => {
    if (selectedIds.size < 2) {
      alert('Select at least 2 entries to compare');
      return;
    }

    const selectedEntries = history.filter(entry => selectedIds.has(entry.id));
    if (onCompare) {
      onCompare(selectedEntries);
    }
  };

  const formatDate = (timestamp: string) => {
    try {
      const date = new Date(timestamp);
      return date.toLocaleDateString() + ' ' + date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    } catch {
      return timestamp;
    }
  };

  const truncate = (text: string, maxLength: number = 100) => {
    if (text.length <= maxLength) return text;
    return text.slice(0, maxLength) + '...';
  };

  return (
    <div className="card">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <h2>Generation History</h2>
        {selectedIds.size >= 2 && (
          <button
            className="button"
            onClick={handleCompare}
            style={{ padding: '0.5rem 1rem', fontSize: '0.875rem' }}
            aria-label={`Compare ${selectedIds.size} entries`}
          >
            Compare ({selectedIds.size})
          </button>
        )}
      </div>
      
      {/* Filters */}
      <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1rem', flexWrap: 'wrap' }}>
        <select
          className="input"
          value={filterPersona}
          onChange={(e) => setFilterPersona(e.target.value)}
          style={{ flex: 1, minWidth: '120px', padding: '0.5rem', fontSize: '0.875rem' }}
          aria-label="Filter by persona"
        >
          <option value="">All Personas</option>
          {uniquePersonas.map(persona => (
            <option key={persona} value={persona}>{persona}</option>
          ))}
        </select>
        <select
          className="input"
          value={filterType}
          onChange={(e) => setFilterType(e.target.value)}
          style={{ flex: 1, minWidth: '120px', padding: '0.5rem', fontSize: '0.875rem' }}
          aria-label="Filter by output type"
        >
          <option value="">All Types</option>
          {uniqueTypes.map(type => (
            <option key={type} value={type}>{type}</option>
          ))}
        </select>
      </div>
      
      {error && (
        <div className="error" style={{ marginBottom: '1rem', padding: '0.75rem' }} role="alert">
          {error}
          <button
            onClick={loadHistory}
            style={{ marginLeft: '0.5rem', padding: '0.25rem 0.5rem', fontSize: '0.75rem' }}
          >
            Retry
          </button>
        </div>
      )}

      {loading ? (
        <div className="loading" role="status" aria-live="polite" aria-busy="true">
          Loading history...
        </div>
      ) : filteredHistory.length === 0 ? (
        <p style={{ color: '#999', fontSize: '0.875rem', textAlign: 'center' }}>
          {history.length === 0 
            ? 'No generation history yet'
            : `No entries match filters (${history.length} total)`}
        </p>
      ) : (
        <div 
          style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem', maxHeight: '600px', overflowY: 'auto' }}
          role="list"
          aria-label="Generation history list"
        >
          {needsVirtualization && (
            <div style={{ fontSize: '0.75rem', color: '#666', padding: '0.5rem', textAlign: 'center' }}>
              Large list ({filteredHistory.length} entries) - Scroll to load more
            </div>
          )}
          {filteredHistory.map((entry) => (
            <div
              key={entry.id}
              role="listitem"
              style={{
                padding: '1rem',
                border: selectedIds.has(entry.id) ? '2px solid #0070f3' : '1px solid #333',
                borderRadius: '4px',
                backgroundColor: selectedIds.has(entry.id) ? '#1a1a2a' : '#0a0a0a',
                cursor: 'pointer',
                transition: 'all 0.2s',
              }}
              onClick={() => handleSelect(entry)}
              onKeyDown={(e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                  e.preventDefault();
                  handleSelect(entry);
                }
              }}
              tabIndex={0}
              aria-label={`History entry: ${entry.persona} - ${entry.output_type}`}
              aria-pressed={selectedIds.has(entry.id)}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start', marginBottom: '0.5rem' }}>
                <div style={{ flex: 1 }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.25rem' }}>
                    <input
                      type="checkbox"
                      checked={selectedIds.has(entry.id)}
                      onChange={(e) => {
                        e.stopPropagation();
                        handleToggleSelect(entry.id);
                      }}
                      onClick={(e) => e.stopPropagation()}
                      aria-label={`Select entry ${entry.id} for comparison`}
                    />
                    <span style={{ fontWeight: 600, fontFamily: 'monospace', fontSize: '0.875rem' }}>
                      {entry.persona}
                    </span>
                    <span style={{
                      padding: '0.125rem 0.5rem',
                      backgroundColor: '#1a1a2a',
                      border: '1px solid #444',
                      borderRadius: '4px',
                      fontSize: '0.75rem',
                      fontFamily: 'monospace',
                    }}>
                      {entry.output_type}
                    </span>
                    {entry.validation && (
                      <span style={{
                        fontSize: '0.75rem',
                        color: entry.validation.valid ? '#2e7d32' : '#d32f2f',
                      }}>
                        {entry.validation.valid ? '✓' : '✗'}
                      </span>
                    )}
                  </div>
                  <div style={{ fontSize: '0.875rem', color: '#999', marginBottom: '0.5rem' }}>
                    {truncate(entry.prompt)}
                  </div>
                  {entry.content && (
                    <div style={{
                      fontSize: '0.75rem',
                      color: '#666',
                      fontFamily: 'monospace',
                      backgroundColor: '#0a0a0a',
                      padding: '0.5rem',
                      borderRadius: '4px',
                      marginBottom: '0.5rem',
                    }}>
                      {truncate(entry.content, 150)}
                    </div>
                  )}
                </div>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem', color: '#666' }}>
                <span>{formatDate(entry.timestamp)}</span>
                <button
                  className="button"
                  onClick={(e) => {
                    e.stopPropagation();
                    handleSelect(entry);
                  }}
                  style={{ padding: '0.25rem 0.75rem', fontSize: '0.75rem' }}
                >
                  Re-run
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

