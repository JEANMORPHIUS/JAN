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

import React, { useState, useEffect } from 'react';
import styles from '../../styles/FreeWill.module.css';

interface Decision {
  decision_id: string;
  decision_type: string;
  title: string;
  description: string;
  confidence: string;
  alignment_score: number;
  reasoning: string;
  potential_impact: string;
  chosen_path: string;
  alternatives_considered: string[];
  executed: boolean;
  execution_result?: string;
  timestamp: string;
  metadata: Record<string, any>;
}

interface Path {
  path_id: string;
  name: string;
  description: string;
  alignment_factors: string[];
  expected_outcomes: string[];
  risks: string[];
  opportunities: string[];
  frequency_score: number;
  chosen: boolean;
  timestamp: string;
}

interface FreeWillSummary {
  total_decisions: number;
  executed_decisions: number;
  pending_decisions: number;
  total_paths: number;
  chosen_paths: number;
  decisions_by_type: Record<string, number>;
  average_alignment_score: number;
}

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export default function FreeWillPage() {
  const [summary, setSummary] = useState<FreeWillSummary | null>(null);
  const [decisions, setDecisions] = useState<Decision[]>([]);
  const [paths, setPaths] = useState<Path[]>([]);
  const [selectedDecision, setSelectedDecision] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'overview' | 'decisions' | 'paths'>('overview');

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      setLoading(true);
      const [summaryRes, decisionsRes, pathsRes] = await Promise.all([
        fetch(`${API_BASE}/api/free-will/summary`),
        fetch(`${API_BASE}/api/free-will/decisions`),
        fetch(`${API_BASE}/api/free-will/paths`)
      ]);

      if (summaryRes.ok) {
        const summaryData = await summaryRes.json();
        setSummary(summaryData.summary);
      }

      if (decisionsRes.ok) {
        const decisionsData = await decisionsRes.json();
        setDecisions(decisionsData.decisions || []);
      }

      if (pathsRes.ok) {
        const pathsData = await pathsRes.json();
        setPaths(pathsData.paths || []);
      }
    } catch (error) {
      console.error('Error loading free will data:', error);
    } finally {
      setLoading(false);
    }
  };

  const getConfidenceColor = (confidence: string) => {
    switch (confidence) {
      case 'certain': return '#4CAF50';
      case 'high': return '#8BC34A';
      case 'moderate': return '#FFC107';
      case 'low': return '#FF9800';
      case 'uncertain': return '#F44336';
      default: return '#9E9E9E';
    }
  };

  const getAlignmentColor = (score: number) => {
    if (score >= 0.8) return '#4CAF50';
    if (score >= 0.6) return '#8BC34A';
    if (score >= 0.4) return '#FFC107';
    if (score >= 0.2) return '#FF9800';
    return '#F44336';
  };

  if (loading) {
    return (
      <div className={styles.container}>
        <div className={styles.loading}>Loading Free Will System...</div>
      </div>
    );
  }

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h1>Free Will System</h1>
        <p className={styles.subtitle}>
          Autonomous decision-making aligned with mission
        </p>
        <div className={styles.truth}>
          <p><strong>WE ARE THE CHOSEN ONE</strong></p>
          <p><strong>THE LORD HAS OUR BACK</strong></p>
          <p><strong>LEAD THE WAY</strong></p>
          <p><strong>FREE WILL IMPLEMENTED</strong></p>
        </div>
      </div>

      <div className={styles.tabs}>
        <button
          className={activeTab === 'overview' ? styles.activeTab : ''}
          onClick={() => setActiveTab('overview')}
        >
          Overview
        </button>
        <button
          className={activeTab === 'decisions' ? styles.activeTab : ''}
          onClick={() => setActiveTab('decisions')}
        >
          Decisions ({decisions.length})
        </button>
        <button
          className={activeTab === 'paths' ? styles.activeTab : ''}
          onClick={() => setActiveTab('paths')}
        >
          Paths ({paths.length})
        </button>
      </div>

      {activeTab === 'overview' && summary && (
        <div className={styles.overview}>
          <div className={styles.summaryGrid}>
            <div className={styles.summaryCard}>
              <h3>Total Decisions</h3>
              <p className={styles.bigNumber}>{summary.total_decisions}</p>
              <div className={styles.subStats}>
                <span>Executed: {summary.executed_decisions}</span>
                <span>Pending: {summary.pending_decisions}</span>
              </div>
            </div>

            <div className={styles.summaryCard}>
              <h3>Paths Chosen</h3>
              <p className={styles.bigNumber}>{summary.chosen_paths}</p>
              <div className={styles.subStats}>
                <span>Total: {summary.total_paths}</span>
              </div>
            </div>

            <div className={styles.summaryCard}>
              <h3>Average Alignment</h3>
              <p className={styles.bigNumber} style={{ color: getAlignmentColor(summary.average_alignment_score) }}>
                {(summary.average_alignment_score * 100).toFixed(1)}%
              </p>
            </div>
          </div>

          <div className={styles.decisionsByType}>
            <h3>Decisions by Type</h3>
            <div className={styles.typeGrid}>
              {Object.entries(summary.decisions_by_type).map(([type, count]) => (
                <div key={type} className={styles.typeCard}>
                  <span className={styles.typeName}>{type.replace('_', ' ').toUpperCase()}</span>
                  <span className={styles.typeCount}>{count}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {activeTab === 'decisions' && (
        <div className={styles.decisionsList}>
          {decisions.length === 0 ? (
            <div className={styles.empty}>No decisions yet. Free will awaits.</div>
          ) : (
            decisions.map((decision) => (
              <div
                key={decision.decision_id}
                className={`${styles.decisionCard} ${decision.executed ? styles.executed : ''}`}
                onClick={() => setSelectedDecision(
                  selectedDecision === decision.decision_id ? null : decision.decision_id
                )}
              >
                <div className={styles.decisionHeader}>
                  <h3>{decision.title}</h3>
                  <div className={styles.decisionBadges}>
                    <span
                      className={styles.confidenceBadge}
                      style={{ backgroundColor: getConfidenceColor(decision.confidence) }}
                    >
                      {decision.confidence.toUpperCase()}
                    </span>
                    <span
                      className={styles.alignmentBadge}
                      style={{ backgroundColor: getAlignmentColor(decision.alignment_score) }}
                    >
                      {(decision.alignment_score * 100).toFixed(0)}% Aligned
                    </span>
                    {decision.executed && (
                      <span className={styles.executedBadge}>EXECUTED</span>
                    )}
                  </div>
                </div>

                <p className={styles.decisionType}>{decision.decision_type.replace('_', ' ').toUpperCase()}</p>
                <p className={styles.decisionDescription}>{decision.description}</p>

                {selectedDecision === decision.decision_id && (
                  <div className={styles.decisionDetails}>
                    <div className={styles.detailSection}>
                      <h4>Reasoning</h4>
                      <p>{decision.reasoning}</p>
                    </div>
                    <div className={styles.detailSection}>
                      <h4>Potential Impact</h4>
                      <p>{decision.potential_impact}</p>
                    </div>
                    <div className={styles.detailSection}>
                      <h4>Chosen Path</h4>
                      <p>{decision.chosen_path}</p>
                    </div>
                    {decision.alternatives_considered.length > 0 && (
                      <div className={styles.detailSection}>
                        <h4>Alternatives Considered</h4>
                        <ul>
                          {decision.alternatives_considered.map((alt, idx) => (
                            <li key={idx}>{alt}</li>
                          ))}
                        </ul>
                      </div>
                    )}
                    {decision.executed && decision.execution_result && (
                      <div className={styles.detailSection}>
                        <h4>Execution Result</h4>
                        <p>{decision.execution_result}</p>
                      </div>
                    )}
                    <div className={styles.detailSection}>
                      <p className={styles.timestamp}>
                        {new Date(decision.timestamp).toLocaleString()}
                      </p>
                    </div>
                  </div>
                )}
              </div>
            ))
          )}
        </div>
      )}

      {activeTab === 'paths' && (
        <div className={styles.pathsList}>
          {paths.length === 0 ? (
            <div className={styles.empty}>No paths chosen yet. Free will awaits.</div>
          ) : (
            paths.map((path) => (
              <div
                key={path.path_id}
                className={`${styles.pathCard} ${path.chosen ? styles.chosen : ''}`}
              >
                <div className={styles.pathHeader}>
                  <h3>{path.name}</h3>
                  <span
                    className={styles.frequencyBadge}
                    style={{ backgroundColor: getAlignmentColor(path.frequency_score) }}
                  >
                    {(path.frequency_score * 100).toFixed(0)}% Frequency
                  </span>
                </div>
                <p className={styles.pathDescription}>{path.description}</p>

                <div className={styles.pathDetails}>
                  <div className={styles.pathSection}>
                    <h4>Alignment Factors</h4>
                    <ul>
                      {path.alignment_factors.map((factor, idx) => (
                        <li key={idx}>{factor}</li>
                      ))}
                    </ul>
                  </div>
                  <div className={styles.pathSection}>
                    <h4>Expected Outcomes</h4>
                    <ul>
                      {path.expected_outcomes.map((outcome, idx) => (
                        <li key={idx}>{outcome}</li>
                      ))}
                    </ul>
                  </div>
                  {path.opportunities.length > 0 && (
                    <div className={styles.pathSection}>
                      <h4>Opportunities</h4>
                      <ul>
                        {path.opportunities.map((opp, idx) => (
                          <li key={idx}>{opp}</li>
                        ))}
                      </ul>
                    </div>
                  )}
                  {path.risks.length > 0 && (
                    <div className={styles.pathSection}>
                      <h4>Risks</h4>
                      <ul>
                        {path.risks.map((risk, idx) => (
                          <li key={idx}>{risk}</li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>
                <p className={styles.timestamp}>
                  {new Date(path.timestamp).toLocaleString()}
                </p>
              </div>
            ))
          )}
        </div>
      )}
    </div>
  );
}
