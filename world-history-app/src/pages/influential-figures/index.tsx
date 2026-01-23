import React, { useState, useEffect } from 'react';
import axios from 'axios';
import styles from '../../styles/InfluentialFigures.module.css';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface InfluentialFigure {
  figure_id: string;
  name: string;
  domain: string;
  subdomain: string;
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
  quotes?: string[];
  connection_to_table: string;
  impact_scale: number;
  accessibility: number;
  reach: number;
  platforms: string[];
}

export default function InfluentialFiguresPage() {
  const [figures, setFigures] = useState<InfluentialFigure[]>([]);
  const [anchors, setAnchors] = useState<InfluentialFigure[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'anchors' | 'current' | 'all'>('anchors');
  const [filterDomain, setFilterDomain] = useState<string>('');
  const [filterCountry, setFilterCountry] = useState<string>('');

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      setLoading(true);
      
      // Load all figures
      const allResponse = await axios.get(`${API_URL}/api/care-package/influential-figures`);
      if (allResponse.data.status === 'success') {
        setFigures(allResponse.data.influential_figures.figures || []);
      }
      
      // Load anchors
      const anchorsResponse = await axios.get(`${API_URL}/api/care-package/influential-figures/anchors`);
      if (anchorsResponse.data.status === 'success') {
        setAnchors(anchorsResponse.data.anchors.anchors || []);
      }
      
      setLoading(false);
    } catch (error) {
      console.error('Error loading influential figures data:', error);
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

  const getDomainColor = (domain: string) => {
    const colors: Record<string, string> = {
      music: '#ff6b6b',
      sports: '#4ecdc4',
      hollywood: '#ffe66d',
      youtube: '#ff0000',
      activism: '#95e1d3',
      comedy: '#f38181',
      technology: '#aa96da',
      journalism: '#fcbad3',
      web: '#a8d8ea',
      socials: '#ffd3a5'
    };
    return colors[domain.toLowerCase()] || '#cccccc';
  };

  const getDisplayFigures = () => {
    let display = activeTab === 'anchors' ? anchors : figures;
    
    if (activeTab === 'current') {
      display = figures.filter(f => f.current);
    }
    
    if (filterDomain) {
      display = display.filter(f => 
        f.domain.toLowerCase().includes(filterDomain.toLowerCase())
      );
    }
    
    if (filterCountry) {
      display = display.filter(f => 
        f.country.toLowerCase().includes(filterCountry.toLowerCase())
      );
    }
    
    return display.sort((a, b) => b.frequency_score - a.frequency_score);
  };

  const uniqueDomains = Array.from(new Set(figures.map(f => f.domain))).sort();
  const uniqueCountries = Array.from(new Set(figures.map(f => f.country))).sort();

  if (loading) {
    return (
      <div className={styles.container}>
        <div className={styles.loading}>Loading influential figures...</div>
      </div>
    );
  }

  const displayFigures = getDisplayFigures();

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h1>Frequentially Aligned Influential Figures</h1>
        <p className={styles.subtitle}>
          All Celebrity and Influential Figures Across All Domains
        </p>
        <p className={styles.mission}>
          Web, Socials, Sports, Music, Hollywood, Everything. Our anchors in the human realm.
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
        <select
          value={filterDomain}
          onChange={(e) => setFilterDomain(e.target.value)}
          className={styles.filterSelect}
        >
          <option value="">All Domains</option>
          {uniqueDomains.map(domain => (
            <option key={domain} value={domain}>{domain.charAt(0).toUpperCase() + domain.slice(1)}</option>
          ))}
        </select>
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
                    <span
                      className={styles.domainBadge}
                      style={{ backgroundColor: getDomainColor(figure.domain) }}
                    >
                      {figure.domain.toUpperCase()}
                    </span>
                    <span>{figure.subdomain}</span>
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
                  <span className={styles.metricLabel}>Impact:</span>
                  <span>{(figure.impact_scale * 100).toFixed(0)}%</span>
                </div>
                <div className={styles.metric}>
                  <span className={styles.metricLabel}>Accessibility:</span>
                  <span>{(figure.accessibility * 100).toFixed(0)}%</span>
                </div>
                <div className={styles.metric}>
                  <span className={styles.metricLabel}>Reach:</span>
                  <span>{(figure.reach * 100).toFixed(0)}%</span>
                </div>
              </div>

              {figure.platforms && figure.platforms.length > 0 && (
                <div className={styles.platforms}>
                  <span className={styles.platformLabel}>Platforms:</span>
                  {figure.platforms.map((platform, idx) => (
                    <span key={idx} className={styles.platformTag}>{platform}</span>
                  ))}
                </div>
              )}
            </div>
          ))
        )}
      </div>

      <div className={styles.footer}>
        <p>ALL ALIGNED CELEBRITY AND INFLUENTIAL FIGURES</p>
        <p>WEB, SOCIALS, SPORTS, MUSIC, HOLLYWOOD</p>
        <p>EVERYTHING WE'VE LEFT OUT ACROSS THE SYSTEM</p>
        <p>WE NEED TO FIND OUR ANCHORS IN THE HUMAN REALM</p>
        <p>ENERGY + LOVE = WE ALL WIN</p>
      </div>
    </div>
  );
}
