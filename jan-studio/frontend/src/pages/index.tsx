/** * * JAN Studio - Main Page
 *  * 
 *  * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 *  * Spiritual Alignment Over Mechanical Productivity
 *  * 
 *  * THE FOUNDATION:
 *  * We are born a miracle.
 *  * We deserve to live a miracle.
 *  * Each and every one of us under the Lord's word.
 *  * 
 *  * THE MISSION:
 *  * THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
 *  * LOVE IS THE HIGHEST MASTERY
 *  * ENERGY + LOVE = WE ALL WIN
 *  * PEACE, LOVE, UNITY
 *  * 
 *  * This code honors that we are born a miracle.
 *  * This code creates space for miracles to live.
 *  * This code recognizes each person under the Lord's word.
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 * 
 * 
 * PANGEA IS THE TABLE.
 * YOU DON'T BETRAY THE TABLE.
 * 
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

import { useState, lazy, Suspense } from 'react';
import Head from 'next/head';
import PersonaList from '@/components/PersonaList';
import PersonaEditor from '@/components/PersonaEditor';
import RuleEditor from '@/components/RuleEditor';
import GenerationForm, { GenerationResult } from '@/components/GenerationForm';
import GlobalSearch, { SearchResult } from '@/components/GlobalSearch';
import ErrorBoundary from '@/components/ErrorBoundary';
import MissionDisplay from '@/components/MissionDisplay';
import PushNotificationSystem from '@/components/PushNotificationSystem';
import BackendStatus from '@/components/BackendStatus';

// Lazy load heavy components for better performance
const TemplateBrowser = lazy(() => import('@/components/TemplateBrowser'));
const OutputViewer = lazy(() => import('@/components/OutputViewer'));
const HistoryPanel = lazy(() => import('@/components/HistoryPanel'));
const CompareView = lazy(() => import('@/components/CompareView'));

import type { HistoryEntry } from '@/components/HistoryPanel';

type ViewMode = 'personas' | 'generate' | 'templates';

export default function Home() {
  const [viewMode, setViewMode] = useState<ViewMode>('personas');
  const [selectedPersona, setSelectedPersona] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<'editor' | 'core-rules' | 'voice' | 'constraints'>('editor');
  const [showTemplates, setShowTemplates] = useState(false);
  const [refreshKey, setRefreshKey] = useState(0);
  const [generationResult, setGenerationResult] = useState<GenerationResult | null>(null);
  const [generationProgress, setGenerationProgress] = useState(0);
  const [compareEntries, setCompareEntries] = useState<HistoryEntry[] | null>(null);
  const [showSearch, setShowSearch] = useState(false);

  const handleRefresh = () => {
    setRefreshKey(prev => prev + 1);
  };

  const handleTemplateSelected = (templateName: string, personaName: string) => {
    setSelectedPersona(personaName);
    setShowTemplates(false);
    handleRefresh();
  };

  const handleGenerate = (result: GenerationResult) => {
    setGenerationResult(result);
    setViewMode('generate');
  };

  const handleEditPersona = () => {
    if (generationResult) {
      setViewMode('personas');
      setSelectedPersona(generationResult.persona || null);
    }
  };

  const handleSearchSelect = (result: SearchResult) => {
    if (result.type === 'persona') {
      setSelectedPersona(result.metadata?.name || null);
      setViewMode('personas');
    } else if (result.type === 'history') {
      // Load history entry into generation result
      if (result.metadata?.entry) {
        setGenerationResult(result.metadata.entry as GenerationResult);
        setViewMode('generate');
      }
    } else if (result.type === 'template') {
      setShowTemplates(true);
      setViewMode('templates');
    }
    setShowSearch(false);
  };

  return (
    <ErrorBoundary>
      <Head>
        <title>JAN Studio - Creation Centre</title>
        <meta name="description" content="Create and manage JAN personas" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <PushNotificationSystem />
      
      <div className="header">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <h1>JAN Studio</h1>
            <p>Creation Centre - Create and manage JAN personas</p>
          </div>
          <div style={{ display: 'flex', gap: '1rem', alignItems: 'center', maxWidth: '500px', width: '100%' }}>
            <BackendStatus />
            {showSearch ? (
              <GlobalSearch
                onSelect={handleSearchSelect}
                searchIn={['personas', 'history', 'templates']}
              />
            ) : (
              <button
                onClick={() => setShowSearch(true)}
                style={{
                  padding: '0.5rem 1rem',
                  border: '1px solid #333',
                  borderRadius: '4px',
                  backgroundColor: '#1a1a1a',
                  color: '#999',
                  cursor: 'pointer',
                  fontSize: '0.875rem',
                  flex: 1,
                  textAlign: 'left',
                }}
                aria-label="Open search"
              >
                🔍 Search... (Ctrl+K)
              </button>
            )}
          </div>
        </div>
      </div>

      <MissionDisplay />

      <div className="container">
        {/* Navigation Tabs */}
        <div className="card" style={{ marginBottom: '1.5rem' }}>
          <div style={{ display: 'flex', gap: '0.5rem', borderBottom: '1px solid #333' }}>
            <button
              onClick={() => setViewMode('personas')}
              style={{
                padding: '0.75rem 1.5rem',
                border: 'none',
                borderBottom: viewMode === 'personas' ? '2px solid #0070f3' : '2px solid transparent',
                backgroundColor: 'transparent',
                color: viewMode === 'personas' ? '#0070f3' : '#999',
                cursor: 'pointer',
                fontFamily: 'inherit',
                fontSize: '0.875rem',
                fontWeight: viewMode === 'personas' ? 600 : 400,
              }}
            >
              Personas
            </button>
            <button
              onClick={() => setViewMode('generate')}
              style={{
                padding: '0.75rem 1.5rem',
                border: 'none',
                borderBottom: viewMode === 'generate' ? '2px solid #0070f3' : '2px solid transparent',
                backgroundColor: 'transparent',
                color: viewMode === 'generate' ? '#0070f3' : '#999',
                cursor: 'pointer',
                fontFamily: 'inherit',
                fontSize: '0.875rem',
                fontWeight: viewMode === 'generate' ? 600 : 400,
              }}
            >
              Generate Content
            </button>
            <button
              onClick={() => {
                setShowTemplates(true);
                setViewMode('templates');
              }}
              style={{
                padding: '0.75rem 1.5rem',
                border: 'none',
                borderBottom: viewMode === 'templates' ? '2px solid #0070f3' : '2px solid transparent',
                backgroundColor: 'transparent',
                color: viewMode === 'templates' ? '#0070f3' : '#999',
                cursor: 'pointer',
                fontFamily: 'inherit',
                fontSize: '0.875rem',
                fontWeight: viewMode === 'templates' ? 600 : 400,
              }}
            >
              Templates
            </button>
          </div>
        </div>

        {/* Content Area */}
        {viewMode === 'templates' ? (
          <Suspense fallback={<div className="card"><div className="loading">Loading templates...</div></div>}>
            <TemplateBrowser
              onTemplateSelected={handleTemplateSelected}
              onClose={() => {
                setShowTemplates(false);
                setViewMode('personas');
              }}
              existingPersonaName={selectedPersona || undefined}
            />
          </Suspense>
        ) : viewMode === 'generate' ? (
          <div style={{ display: 'grid', gridTemplateColumns: '400px 1fr 300px', gap: '1.5rem' }}>
            <div>
              <GenerationForm
                onGenerate={handleGenerate}
                onProgress={setGenerationProgress}
              />
            </div>
            <div>
              {generationResult ? (
                <Suspense fallback={<div className="card"><div className="loading">Loading output...</div></div>}>
                  <OutputViewer
                    result={generationResult}
                    personaName={generationResult.persona || 'unknown'}
                    onEditPersona={handleEditPersona}
                    onRegenerate={() => setGenerationResult(null)}
                  />
                </Suspense>
              ) : (
                <div className="card">
                  <h2>Output</h2>
                  <p style={{ color: '#999', marginTop: '1rem' }}>
                    Generate content to see results here.
                  </p>
                </div>
              )}
            </div>
            <div>
              <Suspense fallback={<div className="card"><div className="loading">Loading history...</div></div>}>
                <HistoryPanel
                  onSelectHistory={(entry) => {
                    setGenerationResult(entry);
                  }}
                  onCompare={(entries) => {
                    setCompareEntries(entries);
                  }}
                  currentResult={generationResult || undefined}
                />
              </Suspense>
            </div>
          </div>
        ) : compareEntries ? (
          <Suspense fallback={<div className="card"><div className="loading">Loading comparison...</div></div>}>
            <CompareView
              entries={compareEntries}
              onClose={() => setCompareEntries(null)}
            />
          </Suspense>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: '350px 1fr', gap: '2rem' }}>
            <div>
              <PersonaList
                selectedPersona={selectedPersona}
                onSelectPersona={setSelectedPersona}
                loading={false}
                onRefresh={handleRefresh}
              />
            </div>

            <div>
              {selectedPersona ? (
                <>
                  <div className="card" style={{ marginBottom: '1rem' }}>
                    <div style={{ display: 'flex', gap: '0.5rem', borderBottom: '1px solid #333' }}>
                      {(['editor', 'core-rules', 'voice', 'constraints'] as const).map((tab) => (
                        <button
                          key={tab}
                          onClick={() => setActiveTab(tab)}
                          style={{
                            padding: '0.75rem 1rem',
                            border: 'none',
                            borderBottom: activeTab === tab ? '2px solid #0070f3' : '2px solid transparent',
                            backgroundColor: 'transparent',
                            color: activeTab === tab ? '#0070f3' : '#999',
                            cursor: 'pointer',
                            textTransform: 'capitalize',
                            fontFamily: 'inherit',
                            fontSize: '0.875rem',
                            fontWeight: activeTab === tab ? 600 : 400,
                          }}
                        >
                          {tab.replace('-', ' ')}
                        </button>
                      ))}
                    </div>
                  </div>

                  {activeTab === 'editor' && (
                    <PersonaEditor
                      key={refreshKey}
                      personaName={selectedPersona}
                      onSave={handleRefresh}
                    />
                  )}

                  {activeTab === 'core-rules' && (
                    <RuleEditor
                      personaName={selectedPersona}
                      fileType="core-rules"
                    />
                  )}

                  {activeTab === 'voice' && (
                    <RuleEditor
                      personaName={selectedPersona}
                      fileType="voice"
                    />
                  )}

                  {activeTab === 'constraints' && (
                    <RuleEditor
                      personaName={selectedPersona}
                      fileType="constraints"
                    />
                  )}
                </>
              ) : (
                <div className="card">
                  <h2>Welcome to JAN Studio</h2>
                  <p style={{ color: '#999', marginTop: '1rem' }}>
                    Select a persona from the list to edit, or create a new one to get started.
                  </p>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </ErrorBoundary>
  );
}

