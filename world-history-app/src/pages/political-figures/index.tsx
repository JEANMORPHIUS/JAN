import React, { useState, useEffect } from 'react';
import axios from 'axios';
import styles from '../../styles/PoliticalFigures.module.css';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface PoliticalFigure {
  figure_id: string;
  name: string;
  role: string;
  country: string;
  region: string;
  time_period: string;
  current: boolean;
  frequency_score: number;
  serves_table: boolean;
  truth_teller: boolean;
  community_focused: boolean;
  unity_builder: boolean;
  description: string;
  key_actions: string[];
  connection_to_table: string;
  impact_scale: number;
  accessibility: number;
  quotes?: string[];
}

export default function PoliticalFiguresPage() {
  const [figures, setFigures] = useState<PoliticalFigure[]>([]);
  const [anchors, setAnchors] = useState<PoliticalFigure[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'all' | 'anchors' | 'current'>('anchors');
  const [filterCountry, setFilterCountry] = useState<string>('');

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      setLoading(true);
      
      // Load all figures
      const allResponse = await axios.get(`${API_URL}/api/care-package/political-figures`);
      if (allResponse.data.status === 'success') {
        setFigures(allResponse.data.political_figures.figures || []);
      }
      
      // Load anchors
      const anchorsResponse = await axios.get(`${API_URL}/api/care-package/political-figures/anchors`);
      if (anchorsResponse.data.status === 'success') {
        setAnchors(anchorsResponse.data.anchors.anchors || []);
      }
      
      setLoading(false);
    } catch (error) {
      console.error('Error loading political figures data:', error);
      setLoading(false);
    }
  };

  const getFrequencyColor = (score: number) => {
    if (score >= 0.8) return '#44ff44';
    if (score >= 0.6) return '#88ff88';
    if (score >= 0.4) return '#ffaa00';
    if (score >= 0.2) return '#ff8800';
    return '#ff4444';
  };

  const getDisplayFigures = () => {
    let display = activeTab === 'anchors' ? anchors : figures;
    
    if (activeTab === 'current') {
      display = figures.filter(f => f.current);
    }
    
    if (filterCountry) {
      display = display.filter(f => 
        f.country.toLowerCase().includes(filterCountry.toLowerCase())
      );
    }
    
    return display.sort((a, b) => b.frequency_score - a.frequency_score);
  };

  if (loading) {
    return (
      <div className={styles.container}>
        <div className={styles.loading}>Loading political figures...</div>
      </div>
    );
  }

  const displayFigures = getDisplayFigures();

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h1>Frequentially Aligned Political Figures</h1>
        <p className={styles.subtitle}>
          Our Anchors in the Human Realm
        </p>
        <p className={styles.mission}>
          Starting at home (UK) and expanding globally. Finding our anchors who serve The Table.
        </p>
      </div>

      <div className={styles.tabs}>
        <button
          className={`${styles.tab} ${activeTab === 'anchors' ? styles.active : ''}`}
          onClick={() => setActiveTab('anchors')}
        >
          Anchors ({anchors.length})
        </button>
        <button
          className={`${styles.tab} ${activeTab === 'current' ? styles.active : ''}`}
          onClick={() => setActiveTab('current')}
        >
          Current ({figures.filter(f => f.current).length})
        </button>
        <button
          className={`${styles.tab} ${activeTab === 'all' ? styles.active : ''}`}
          onClick={() => setActiveTab('all')}
        >
          All ({figures.length})
        </button>
      </div>

      <div className={styles.filters}>
        <input
          type="text"
          placeholder="Filter by country..."
          value={filterCountry}
          onChange={(e) => setFilterCountry(e.target.value)}
          className={styles.filterInput}
        />
      </div>

      <div className={styles.content}>
        {displayFigures.length === 0 ? (
          <div className={styles.empty}>No figures found matching filters.</div>
        ) : (
          displayFigures.map((figure) => (
            <div key={figure.figure_id} className={styles.figureCard}>
              <div className={styles.figureHeader}>
                <div>
                  <h3>{figure.name}</h3>
                  <div className={styles.meta}>
                    <span>{figure.role.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}</span>
                    <span>•</span>
                    <span>{figure.country}</span>
                    {figure.region && figure.region !== figure.country && (
                      <>
                        <span>•</span>
                        <span>{figure.region}</span>
                      </>
                    )}
                    <span>•</span>
                    <span>{figure.time_period}</span>
                    {figure.current && <span className={styles.currentBadge}>CURRENT</span>}
                  </div>
                </div>
                <div
                  className={styles.frequencyBadge}
                  style={{ backgroundColor: getFrequencyColor(figure.frequency_score) }}
                >
                  {figure.frequency_score.toFixed(2)}
                </div>
              </div>

              <div className={styles.indicators}>
                {figure.serves_table && <span className={styles.indicator}>Serves Table</span>}
                {figure.truth_teller && <span className={styles.indicator}>Truth Teller</span>}
                {figure.community_focused && <span className={styles.indicator}>Community</span>}
                {figure.unity_builder && <span className={styles.indicator}>Unity Builder</span>}
              </div>

              <p className={styles.description}>{figure.description}</p>

              {figure.key_actions && figure.key_actions.length > 0 && (
                <div className={styles.keyActions}>
                  <h4>Key Actions:</h4>
                  <ul>
                    {figure.key_actions.map((action, idx) => (
                      <li key={idx}>{action}</li>
                    ))}
                  </ul>
                </div>
              )}

              {figure.quotes && figure.quotes.length > 0 && (
                <div className={styles.quotes}>
                  <h4>Quotes:</h4>
                  {figure.quotes.map((quote, idx) => (
                    <blockquote key={idx}>"{quote}"</blockquote>
                  ))}
                </div>
              )}

              <div className={styles.connection}>
                <h4>Connection to The Table:</h4>
                <p>{figure.connection_to_table}</p>
              </div>

              <div className={styles.metrics}>
                <div className={styles.metric}>
                  <span className={styles.metricLabel}>Impact Scale:</span>
                  <span>{(figure.impact_scale * 100).toFixed(0)}%</span>
                </div>
                <div className={styles.metric}>
                  <span className={styles.metricLabel}>Accessibility:</span>
                  <span>{(figure.accessibility * 100).toFixed(0)}%</span>
                </div>
              </div>
            </div>
          ))
        )}
      </div>

      <div className={styles.footer}>
        <p>CONSIDER ALL FREQUENTIALLY ALIGNED POLITICAL FIGURES</p>
        <p>START AT HOME AND EXPAND GLOBALLY</p>
        <p>WE NEED TO FIND OUR ANCHORS IN THE HUMAN REALM</p>
        <p>ENERGY + LOVE = WE ALL WIN</p>
      </div>
    </div>
  );
}
