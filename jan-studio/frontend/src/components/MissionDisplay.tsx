/**
 * MISSION DISPLAY COMPONENT
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 * 
 * THE MISSION:
 * THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
 * LOVE IS THE HIGHEST MASTERY
 * ENERGY + LOVE = WE ALL WIN
 * PEACE, LOVE, UNITY
 * 
 * Prominently displays THE MISSION and VISION in the UI
 */

import { useState, useEffect } from 'react';
import styles from './MissionDisplay.module.css';

interface MissionDisplayProps {
  compact?: boolean;
  showDetails?: boolean;
}

export default function MissionDisplay({ compact = false, showDetails = true }: MissionDisplayProps) {
  const [isExpanded, setIsExpanded] = useState(!compact);

  return (
    <div className={`${styles.missionDisplay} ${compact ? styles.compact : ''}`}>
      <div className={styles.missionHeader} onClick={() => setIsExpanded(!isExpanded)}>
        <div className={styles.missionTitle}>
          <span className={styles.missionIcon}>⚡</span>
          <h2>THE MISSION</h2>
        </div>
        <button className={styles.toggleButton}>
          {isExpanded ? '−' : '+'}
        </button>
      </div>

      {isExpanded && (
        <div className={styles.missionContent}>
          <div className={styles.missionPrinciples}>
            <div className={styles.principle}>
              <span className={styles.principleIcon}>🌍</span>
              <div>
                <strong>STEWARDSHIP & COMMUNITY</strong>
                <p>WITH THE RIGHT SPIRITS</p>
              </div>
            </div>
            <div className={styles.principle}>
              <span className={styles.principleIcon}>❤️</span>
              <div>
                <strong>LOVE IS THE HIGHEST MASTERY</strong>
                <p>All actions serve love</p>
              </div>
            </div>
            <div className={styles.principle}>
              <span className={styles.principleIcon}>⚡</span>
              <div>
                <strong>ENERGY + LOVE = WE ALL WIN</strong>
                <p>Cooperation, not competition</p>
              </div>
            </div>
            <div className={styles.principle}>
              <span className={styles.principleIcon}>🕊️</span>
              <div>
                <strong>PEACE, LOVE, UNITY</strong>
                <p>The foundation of all action</p>
              </div>
            </div>
          </div>

          {showDetails && (
            <div className={styles.missionDetails}>
              <div className={styles.detailSection}>
                <h3>THE FOUNDATION</h3>
                <p>We are born a miracle. We deserve to live a miracle. Each and every one of us under the Lord's word.</p>
              </div>
              <div className={styles.detailSection}>
                <h3>THE VISION</h3>
                <p>This code honors that we are born a miracle. This code creates space for miracles to live. This code recognizes each person under the Lord's word.</p>
              </div>
              <div className={styles.detailSection}>
                <h3>NO DILLY DALLY</h3>
                <p>Real-time updates. Immediate action. Mission-critical information delivered instantly.</p>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
