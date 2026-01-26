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

import { useState, useEffect, useMemo, memo } from 'react';
import { GenerationResult } from './GenerationForm';
import { getGenerationHistory, saveToHistory } from '@/api/generation';
import { shouldVirtualize } from '@/utils/performance';
import { retryWithBackoff, getUserFriendlyError } from '@/utils/errorHandling';
import { VirtualizedList } from './VirtualizedList';
import { useGenerationHistory, useSaveToHistory } from '@/hooks/useGenerationHistory';
import LoadingState from './LoadingState';
import { useI18n } from '@/contexts/I18nContext';

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
  const { t, language } = useI18n();
  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set());
  const [filterPersona, setFilterPersona] = useState<string>('');
  const [filterType, setFilterType] = useState<string>('');
  const [dateRange, setDateRange] = useState<{ start: string; end: string }>({ start: '', end: '' });
  
  // Use React Query for data fetching
  const { data: history = [], isLoading: loading, error: queryError, refetch } = useGenerationHistory();
  const saveToHistoryMutation = useSaveToHistory();
  
  // Import regional formatting utilities
  const { formatDateRegional, formatTimeRegional } = require('@/utils/regionalFormats');

  useEffect(() => {
    if (currentResult) {
      // Auto-save current result to history
      saveToHistoryMutation.mutate(currentResult as any);
    }
  }, [currentResult, saveToHistoryMutation]);
  
  // Filter history
  const filteredHistory = useMemo(() => {
    let filtered = history;
    
    if (filterPersona) {
      filtered = filtered.filter(entry => 
        entry.persona?.toLowerCase().includes(filterPersona.toLowerCase())
      );
    }
    
    if (filterType) {
      filtered = filtered.filter(entry => 
        entry.output_type === filterType
      );
    }
    
    // Date range filter
    if (dateRange.start) {
      const startDate = new Date(dateRange.start);
      filtered = filtered.filter(entry => {
        const entryDate = new Date(entry.timestamp);
        return entryDate >= startDate;
      });
    }
    
    if (dateRange.end) {
      const endDate = new Date(dateRange.end);
      endDate.setHours(23, 59, 59, 999); // End of day
      filtered = filtered.filter(entry => {
        const entryDate = new Date(entry.timestamp);
        return entryDate <= endDate;
      });
    }
    
    return filtered;
  }, [history, filterPersona, filterType, dateRange]);
  
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
      alert(t('select_at_least_two_to_compare'));
      return;
    }

    const selectedEntries = history.filter(entry => selectedIds.has(entry.id));
    if (onCompare) {
      onCompare(selectedEntries);
    }
  };
  
  const handleBulkDelete = () => {
    if (selectedIds.size === 0) {
      alert(t('select_entries_to_delete'));
      return;
    }
    
    if (confirm(t('confirm_delete_entries', { count: selectedIds.size }))) {
      // Remove from localStorage
      try {
        const stored = localStorage.getItem('jan-generation-history');
        if (stored) {
          const history = JSON.parse(stored);
          const filtered = history.filter((entry: HistoryEntry) => !selectedIds.has(entry.id));
          localStorage.setItem('jan-generation-history', JSON.stringify(filtered));
          setSelectedIds(new Set());
          refetch();
        }
      } catch (err) {
        console.error('Failed to delete entries:', err);
        alert(t('failed_to_delete_entries'));
      }
    }
  };
  
  const handleBulkExport = () => {
    if (selectedIds.size === 0) {
      alert(t('select_entries_to_export'));
      return;
    }
    
    const selectedEntries = history.filter(entry => selectedIds.has(entry.id));
    const exportData = selectedEntries.map(entry => ({
      persona: entry.persona,
      prompt: entry.prompt,
      output_type: entry.output_type,
      content: entry.content,
      timestamp: entry.timestamp,
    }));
    
    const blob = new Blob([JSON.stringify(exportData, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `jan-history-export-${new Date().toISOString().slice(0, 10)}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const formatDate = (timestamp: string) => {
    try {
      const date = new Date(timestamp);
      // Use regional formatting based on current language
      return formatDateRegional(date, language) + ' ' + formatTimeRegional(date, language);
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
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem', flexWrap: 'wrap', gap: '0.5rem' }}>
        <h2 style={{ margin: 0 }}>{t('generation_history')}</h2>
        {selectedIds.size > 0 && (
          <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
            {selectedIds.size >= 2 && (
              <button
                className="button"
                onClick={handleCompare}
                style={{ padding: '0.5rem 1rem', fontSize: '0.875rem' }}
                aria-label={t('compare_entries', { count: selectedIds.size })}
              >
                {t('compare')} ({selectedIds.size})
              </button>
            )}
            <button
              className="button"
              onClick={handleBulkExport}
              style={{ padding: '0.5rem 1rem', fontSize: '0.875rem', backgroundColor: '#0070f3' }}
              aria-label={t('export_entries', { count: selectedIds.size })}
            >
              {t('export')} ({selectedIds.size})
            </button>
            <button
              className="button"
              onClick={handleBulkDelete}
              style={{ padding: '0.5rem 1rem', fontSize: '0.875rem', backgroundColor: '#d32f2f' }}
              aria-label={t('delete_entries', { count: selectedIds.size })}
            >
              {t('delete')} ({selectedIds.size})
            </button>
            <button
              className="button"
              onClick={() => setSelectedIds(new Set())}
              style={{ padding: '0.5rem 1rem', fontSize: '0.875rem', backgroundColor: '#666' }}
              aria-label={t('clear_selection')}
            >
              {t('clear')}
            </button>
          </div>
        )}
      </div>
      
      {/* Filters */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem', marginBottom: '1rem' }}>
        <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
          <select
            className="input"
            value={filterPersona}
            onChange={(e) => setFilterPersona(e.target.value)}
            style={{ flex: 1, minWidth: '120px', padding: '0.5rem', fontSize: '0.875rem' }}
            aria-label="Filter by persona"
          >
            <option value="">{t('all_personas')}</option>
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
            <option value="">{t('all_types')}</option>
            {uniqueTypes.map(type => (
              <option key={type} value={type}>{type}</option>
            ))}
          </select>
        </div>
        
        {/* Date Range Filter */}
        <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
          <input
            type="date"
            className="input"
            value={dateRange.start}
            onChange={(e) => setDateRange({ ...dateRange, start: e.target.value })}
            style={{ flex: 1, minWidth: '120px', padding: '0.5rem', fontSize: '0.875rem' }}
            aria-label="Filter start date"
            placeholder="Start date"
          />
          <input
            type="date"
            className="input"
            value={dateRange.end}
            onChange={(e) => setDateRange({ ...dateRange, end: e.target.value })}
            style={{ flex: 1, minWidth: '120px', padding: '0.5rem', fontSize: '0.875rem' }}
            aria-label="Filter end date"
            placeholder="End date"
          />
          {(dateRange.start || dateRange.end) && (
            <button
              className="button"
              onClick={() => setDateRange({ start: '', end: '' })}
              style={{ padding: '0.5rem 1rem', fontSize: '0.875rem' }}
              aria-label="Clear date filter"
            >
              Clear Dates
            </button>
          )}
        </div>
      </div>
      
      {queryError && (
        <div className="error" style={{ marginBottom: '1rem', padding: '0.75rem' }} role="alert">
          {getUserFriendlyError(queryError)}
          <button
            onClick={() => refetch()}
            style={{ marginLeft: '0.5rem', padding: '0.25rem 0.5rem', fontSize: '0.75rem' }}
          >
            Retry
          </button>
        </div>
      )}

      {loading ? (
        <LoadingState message={t('loading_history')} size="small" />
      ) : filteredHistory.length === 0 ? (
        <p style={{ color: '#999', fontSize: '0.875rem', textAlign: 'center' }}>
          {history.length === 0 
            ? t('no_generation_history')
            : t('no_entries_match_filters', { total: history.length })}
        </p>
      ) : needsVirtualization ? (
        <div style={{ height: '600px' }}>
          <VirtualizedList
            items={filteredHistory}
            estimateSize={180}
            renderItem={(entry, index) => (
              <div style={{ padding: '0.5rem' }}>
                <HistoryEntryCard
                  entry={entry}
                  isSelected={selectedIds.has(entry.id)}
                  onSelect={() => handleSelect(entry)}
                  onToggleSelect={() => handleToggleSelect(entry.id)}
                  formatDate={formatDate}
                  truncate={truncate}
                />
              </div>
            )}
          />
        </div>
      ) : (
        <div 
          style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem', maxHeight: '600px', overflowY: 'auto' }}
          role="list"
          aria-label="Generation history list"
        >
          {filteredHistory.map((entry) => (
            <HistoryEntryCard
              key={entry.id}
              entry={entry}
              isSelected={selectedIds.has(entry.id)}
              onSelect={() => handleSelect(entry)}
              onToggleSelect={() => handleToggleSelect(entry.id)}
              formatDate={formatDate}
              truncate={truncate}
            />
          ))}
        </div>
      )}
    </div>
  );
}

// Separate component for history entry card - memoized for performance
const HistoryEntryCard = memo(function HistoryEntryCard({
  entry,
  isSelected,
  onSelect,
  onToggleSelect,
  formatDate,
  truncate,
}: {
  entry: HistoryEntry;
  isSelected: boolean;
  onSelect: () => void;
  onToggleSelect: () => void;
  formatDate: (timestamp: string) => string;
  truncate: (text: string, maxLength?: number) => string;
}) {
  return (
    <div
      role="listitem"
      style={{
        padding: '1rem',
        border: isSelected ? '2px solid #0070f3' : '1px solid #333',
        borderRadius: '4px',
        backgroundColor: isSelected ? '#1a1a2a' : '#0a0a0a',
        cursor: 'pointer',
        transition: 'all 0.2s',
      }}
      onClick={onSelect}
      onKeyDown={(e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          onSelect();
        }
      }}
      tabIndex={0}
      aria-label={`History entry: ${entry.persona} - ${entry.output_type}`}
      aria-pressed={isSelected}
    >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start', marginBottom: '0.5rem' }}>
                <div style={{ flex: 1 }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.25rem' }}>
                    <input
                      type="checkbox"
                      checked={isSelected}
                      onChange={(e) => {
                        e.stopPropagation();
                        onToggleSelect();
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
                <span>{formatDate(entry.timestamp || new Date().toISOString())}</span>
                <button
                  className="button"
                  onClick={(e) => {
                    e.stopPropagation();
                    onSelect();
                  }}
                  style={{ padding: '0.25rem 0.75rem', fontSize: '0.75rem' }}
                  aria-label="Re-run this generation"
                >
                  Re-run
                </button>
              </div>
            </div>
    );
  }
}, (prevProps, nextProps) => {
  // Memoization comparison - only re-render if these change
  return (
    prevProps.entry.id === nextProps.entry.id &&
    prevProps.isSelected === nextProps.isSelected &&
    prevProps.entry.persona === nextProps.entry.persona &&
    prevProps.entry.output_type === nextProps.entry.output_type &&
    prevProps.entry.timestamp === nextProps.entry.timestamp
  );
});

