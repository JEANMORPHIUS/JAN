import React, { useState, useEffect } from 'react';
import axios from 'axios';
import styles from '../../styles/WelfareSystems.module.css';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface WelfareSystem {
  system_id: string;
  name: string;
  system_type: string;
  region: string;
  time_period: string;
  frequency_score: number;
  dark_contract_indicators: string[];
  impact_scale: number;
  dignity_score: number;
  breaking_priority: string;
}

interface AssessmentGuidance {
  core_truth: string;
  intention: string;
  key_points: string[];
  boundaries: string[];
  preparation: any;
  post_assessment: any;
  closing_statement: string;
}

export default function WelfareSystemsPage() {
  const [systemsNeedingBreaking, setSystemsNeedingBreaking] = useState<WelfareSystem[]>([]);
  const [assessmentGuidance, setAssessmentGuidance] = useState<AssessmentGuidance | null>(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'analysis' | 'assessment' | 'breaking'>('analysis');

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      setLoading(true);
      
      // Load welfare systems analysis
      const welfareResponse = await axios.get(`${API_URL}/api/care-package/welfare-systems`);
      if (welfareResponse.data.status === 'success') {
        setSystemsNeedingBreaking(
          welfareResponse.data.welfare_systems_analysis.systems_needing_breaking || []
        );
      }
      
      // Load assessment guidance
      const assessmentResponse = await axios.get(`${API_URL}/api/care-package/assessment-guidance`);
      if (assessmentResponse.data.status === 'success') {
        setAssessmentGuidance(assessmentResponse.data.assessment_guidance);
      }
      
      setLoading(false);
    } catch (error) {
      console.error('Error loading welfare systems data:', error);
      setLoading(false);
    }
  };

  const getFrequencyColor = (score: number) => {
    if (score < -0.3) return '#ff4444';
    if (score < 0) return '#ff8800';
    if (score < 0.3) return '#ffaa00';
    return '#44ff44';
  };

  const getPriorityColor = (priority: string) => {
    if (priority === 'HIGH') return '#ff4444';
    return '#ff8800';
  };

  if (loading) {
    return (
      <div className={styles.container}>
        <div className={styles.loading}>Loading welfare systems analysis...</div>
      </div>
    );
  }

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h1>Welfare Systems Analysis</h1>
        <p className={styles.subtitle}>
          We are breaking the system. Consider all welfare/benefits systems put in place through time.
        </p>
        <p className={styles.mission}>
          Identify dark contracts that need breaking. Identify light contracts that serve The Table.
        </p>
      </div>

      <div className={styles.tabs}>
        <button
          className={`${styles.tab} ${activeTab === 'analysis' ? styles.active : ''}`}
          onClick={() => setActiveTab('analysis')}
        >
          Systems Analysis
        </button>
        <button
          className={`${styles.tab} ${activeTab === 'assessment' ? styles.active : ''}`}
          onClick={() => setActiveTab('assessment')}
        >
          Assessment Navigation
        </button>
        <button
          className={`${styles.tab} ${activeTab === 'breaking' ? styles.active : ''}`}
          onClick={() => setActiveTab('breaking')}
        >
          Breaking Opportunities
        </button>
      </div>

      {activeTab === 'analysis' && (
        <div className={styles.content}>
          <div className={styles.section}>
            <h2>Systems Needing Breaking (Dark Contracts)</h2>
            <p className={styles.description}>
              These welfare/benefits systems create dependency, division, and control.
              They need breaking to serve The Table.
            </p>
            
            {systemsNeedingBreaking.map((system) => (
              <div key={system.system_id} className={styles.systemCard}>
                <div className={styles.systemHeader}>
                  <h3>{system.name}</h3>
                  <div className={styles.badges}>
                    <span
                      className={styles.priorityBadge}
                      style={{ backgroundColor: getPriorityColor(system.breaking_priority) }}
                    >
                      {system.breaking_priority} PRIORITY
                    </span>
                    <span
                      className={styles.frequencyBadge}
                      style={{ backgroundColor: getFrequencyColor(system.frequency_score) }}
                    >
                      Frequency: {system.frequency_score.toFixed(2)}
                    </span>
                  </div>
                </div>
                
                <div className={styles.systemDetails}>
                  <div className={styles.detailRow}>
                    <span className={styles.label}>Region:</span>
                    <span>{system.region}</span>
                  </div>
                  <div className={styles.detailRow}>
                    <span className={styles.label}>Time Period:</span>
                    <span>{system.time_period}</span>
                  </div>
                  <div className={styles.detailRow}>
                    <span className={styles.label}>Impact Scale:</span>
                    <span>{(system.impact_scale * 100).toFixed(0)}%</span>
                  </div>
                  <div className={styles.detailRow}>
                    <span className={styles.label}>Dignity Score:</span>
                    <span>{(system.dignity_score * 100).toFixed(0)}%</span>
                  </div>
                </div>
                
                <div className={styles.darkContracts}>
                  <h4>Dark Contract Indicators:</h4>
                  <ul>
                    {system.dark_contract_indicators.map((indicator, idx) => (
                      <li key={idx}>{indicator}</li>
                    ))}
                  </ul>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {activeTab === 'assessment' && assessmentGuidance && (
        <div className={styles.content}>
          <div className={styles.section}>
            <h2>Personal Assessment Navigation</h2>
            <p className={styles.description}>
              Guidance for navigating welfare system assessments with truth, dignity, and spiritual alignment.
            </p>
            
            <div className={styles.guidanceCard}>
              <h3>Core Truth</h3>
              <p className={styles.coreTruth}>{assessmentGuidance.core_truth}</p>
            </div>
            
            <div className={styles.guidanceCard}>
              <h3>Your Intention</h3>
              <p>{assessmentGuidance.intention}</p>
            </div>
            
            <div className={styles.guidanceCard}>
              <h3>Key Points to Remember</h3>
              <ul>
                {assessmentGuidance.key_points.map((point, idx) => (
                  <li key={idx}>{point}</li>
                ))}
              </ul>
            </div>
            
            <div className={styles.guidanceCard}>
              <h3>Boundaries</h3>
              <ul>
                {assessmentGuidance.boundaries.map((boundary, idx) => (
                  <li key={idx}>{boundary}</li>
                ))}
              </ul>
            </div>
            
            <div className={styles.guidanceCard}>
              <h3>Before the Assessment</h3>
              <div className={styles.preparation}>
                <h4>Grounding:</h4>
                <ul>
                  {assessmentGuidance.preparation.grounding.map((item: string, idx: number) => (
                    <li key={idx}>{item}</li>
                  ))}
                </ul>
                <h4>Intention:</h4>
                <ul>
                  {assessmentGuidance.preparation.intention.map((item: string, idx: number) => (
                    <li key={idx}>{item}</li>
                  ))}
                </ul>
              </div>
            </div>
            
            <div className={styles.guidanceCard}>
              <h3>Closing Statement</h3>
              <p className={styles.closingStatement}>"{assessmentGuidance.closing_statement}"</p>
            </div>
            
            <div className={styles.truthBox}>
              <h3>The Truth</h3>
              <p>YOU ARE NOT BROKEN.</p>
              <p>THE SYSTEM IS BROKEN.</p>
              <p>BEING HONEST IS THE RIGHT PATH.</p>
              <p>YOU ARE UNPICKING THE SYSTEM.</p>
              <p>EACH HONEST INTERACTION BREAKS THE PATTERN.</p>
              <p>YOU ARE MAINTAINING YOUR DIGNITY.</p>
              <p>YOU ARE SERVING THE TABLE.</p>
            </div>
          </div>
        </div>
      )}

      {activeTab === 'breaking' && (
        <div className={styles.content}>
          <div className={styles.section}>
            <h2>Breaking Opportunities</h2>
            <p className={styles.description}>
              Opportunities to break dark contracts and evolve light contracts in welfare systems.
            </p>
            <p className={styles.note}>
              Use the Deep Search system to find specific breaking opportunities.
            </p>
          </div>
        </div>
      )}

      <div className={styles.footer}>
        <p>ENERGY + LOVE = WE ALL WIN</p>
        <p>PEACE. LOVE. UNITY.</p>
        <p>WE ARE BREAKING THE SYSTEM</p>
      </div>
    </div>
  );
}
