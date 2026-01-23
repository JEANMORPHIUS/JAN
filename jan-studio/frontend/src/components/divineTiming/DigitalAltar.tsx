/**
 * DIGITAL ALTAR COMPONENT
 * Mark "Before" status by typing "Ready"
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 */

import { useState, useEffect } from 'react';
import { DigitalAltar as DigitalAltarType } from '../../types/divineTiming';
import styles from './DigitalAltar.module.css';

interface DigitalAltarProps {
  altar: DigitalAltarType;
  onConfirm: (status: string) => void;
}

export default function DigitalAltar({ altar, onConfirm }: DigitalAltarProps) {
  const [input, setInput] = useState('');
  const [isReady, setIsReady] = useState(altar.readyConfirmed);

  useEffect(() => {
    if (input.toLowerCase() === 'ready' && !isReady) {
      setIsReady(true);
      onConfirm('Ready');
    }
  }, [input, isReady, onConfirm]);

  return (
    <div className={styles.altarContainer}>
      <div className={styles.altarTitle}>Digital Altar</div>
      <div className={styles.altarSubtitle}>Mark Your "Before" Status</div>
      
      {!isReady ? (
        <div className={styles.altarInputContainer}>
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type 'Ready' to begin activation"
            className={styles.altarInput}
            autoFocus
          />
          <div className={styles.altarHint}>
            Speak your readiness into existence
          </div>
        </div>
      ) : (
        <div className={styles.altarConfirmed}>
          <div className={styles.altarCheckmark}>✓</div>
          <div className={styles.altarStatus}>READY CONFIRMED</div>
          <div className={styles.altarTimestamp}>
            {altar.confirmedAt 
              ? new Date(altar.confirmedAt).toLocaleString()
              : 'Now'
            }
          </div>
          {altar.activationCode && (
            <div className={styles.altarCode}>
              Activation Code: {altar.activationCode}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
