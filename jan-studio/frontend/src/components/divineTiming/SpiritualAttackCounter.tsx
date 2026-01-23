/**
 * SPIRITUAL ATTACK COUNTER-STRATEGY ENGINE
 * Monitor and counter the Seven Forms of Attack
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 */

import { useState } from 'react';
import { SpiritualAttack, AttackType, CounterStrategy } from '../../types/divineTiming';
import styles from './SpiritualAttackCounter.module.css';

const COUNTER_STRATEGIES: Record<AttackType, CounterStrategy> = {
  distraction_barrage: {
    attackType: 'distraction_barrage',
    decree: 'This can wait, my activation cannot.',
    description: 'Multiple distractions attempting to pull focus from activation',
    action: 'Return focus to activation protocol immediately'
  },
  fatigue_assault: {
    attackType: 'fatigue_assault',
    decree: 'I receive divine energy restoration. My strength is renewed in the Lord.',
    description: 'Unusual exhaustion or fatigue during activation period',
    action: 'Speak energy restoration decree and rest in faith'
  },
  relationship_friction: {
    attackType: 'relationship_friction',
    decree: 'I recognize this as interference, not personal. I release this to God.',
    description: 'Unexpected conflict or friction in relationships',
    action: 'Recognize as interference, not personal attack'
  },
  memory_attack: {
    attackType: 'memory_attack',
    decree: 'Thank you, God, for this memory as proof of my transformation.',
    description: 'Painful or negative memories surfacing during activation',
    action: 'Thank God for the memory as evidence of growth'
  },
  counterfeit_blessing: {
    attackType: 'counterfeit_blessing',
    decree: 'I wait for 100%, not 80%. I reject the counterfeit and receive the real thing.',
    description: 'Opportunity that seems good but is only 80% of the promise',
    action: 'Run Peace Check diagnostic - is this 100% or deceptive 80%?'
  },
  doubt_injection: {
    attackType: 'doubt_injection',
    decree: 'I rehearse the evidence of past shifts. God has moved before, He will move again.',
    description: 'Doubt or questioning of the activation process',
    action: 'Review Evidence Log of past divine shifts'
  },
  premature_victory: {
    attackType: 'premature_victory',
    decree: 'I intensify rather than relax. The first sign of breakthrough requires more focus, not less.',
    description: 'Temptation to relax after first sign of breakthrough',
    action: 'Intensify focus and commitment, do not relax'
  }
};

interface SpiritualAttackCounterProps {
  attacks: SpiritualAttack[];
  onAttackDetected: (attack: SpiritualAttack) => void;
  onCounterApplied: (attackId: string, decree: string) => void;
}

export default function SpiritualAttackCounter({
  attacks,
  onAttackDetected,
  onCounterApplied
}: SpiritualAttackCounterProps) {
  const [selectedAttack, setSelectedAttack] = useState<AttackType | null>(null);
  const [peaceCheckResult, setPeaceCheckResult] = useState<number | null>(null);
  const [evidenceLog, setEvidenceLog] = useState<string[]>([]);
  const [newEvidence, setNewEvidence] = useState('');

  const detectAttack = (type: AttackType, description: string) => {
    const attack: SpiritualAttack = {
      id: Date.now().toString(),
      type,
      detectedAt: new Date(),
      description,
      countered: false
    };
    onAttackDetected(attack);
    setSelectedAttack(type);
  };

  const applyCounter = (attackId: string, attackType: AttackType) => {
    const strategy = COUNTER_STRATEGIES[attackType];
    onCounterApplied(attackId, strategy.decree);
    
    // Update attack as countered
    const attack = attacks.find(a => a.id === attackId);
    if (attack) {
      attack.countered = true;
      attack.counterStrategy = strategy.action;
      attack.counterDecree = strategy.decree;
    }
  };

  const runPeaceCheck = () => {
    // Peace Check diagnostic for Counterfeit Blessing
    // User should assess if opportunity is 100% or 80%
    const result = prompt('Rate this opportunity (0-100): Is this 100% of the promise or deceptive 80%?');
    if (result) {
      const score = Number(result);
      setPeaceCheckResult(score);
      if (score < 100) {
        alert('WARNING: This may be a counterfeit blessing. Wait for 100%.');
      }
    }
  };

  const addEvidence = () => {
    if (newEvidence.trim()) {
      setEvidenceLog(prev => [...prev, newEvidence]);
      setNewEvidence('');
    }
  };

  return (
    <div className={styles.attackCounterContainer}>
      <div className={styles.header}>
        <div className={styles.title}>Spiritual Attack Counter-Strategy</div>
        <div className={styles.subtitle}>Monitor and counter the Seven Forms of Attack</div>
      </div>

      {/* Attack Detection Buttons */}
      <div className={styles.attackGrid}>
        {Object.entries(COUNTER_STRATEGIES).map(([type, strategy]) => (
          <div key={type} className={styles.attackCard}>
            <div className={styles.attackName}>{strategy.description}</div>
            <button
              onClick={() => detectAttack(type as AttackType, strategy.description)}
              className={styles.detectButton}
            >
              Detect {type.replace('_', ' ').toUpperCase()}
            </button>
          </div>
        ))}
      </div>

      {/* Detected Attacks */}
      {attacks.length > 0 && (
        <div className={styles.attacksList}>
          <div className={styles.listTitle}>Detected Attacks ({attacks.length})</div>
          {attacks.map((attack) => {
            const strategy = COUNTER_STRATEGIES[attack.type];
            return (
              <div key={attack.id} className={styles.attackItem}>
                <div className={styles.attackHeader}>
                  <div className={styles.attackType}>{attack.type.replace('_', ' ').toUpperCase()}</div>
                  <div className={styles.attackTime}>
                    {new Date(attack.detectedAt).toLocaleTimeString()}
                  </div>
                </div>
                <div className={styles.attackDescription}>{attack.description}</div>
                
                {!attack.countered ? (
                  <button
                    onClick={() => applyCounter(attack.id, attack.type)}
                    className={styles.counterButton}
                  >
                    Apply Counter-Strategy
                  </button>
                ) : (
                  <div className={styles.counterApplied}>
                    <div className={styles.counterDecree}>{attack.counterDecree}</div>
                    <div className={styles.counterAction}>{attack.counterStrategy}</div>
                  </div>
                )}

                {/* Specialized Tools */}
                {attack.type === 'counterfeit_blessing' && (
                  <div className={styles.specialTool}>
                    <button onClick={runPeaceCheck} className={styles.peaceCheckButton}>
                      Run Peace Check Diagnostic
                    </button>
                    {peaceCheckResult !== null && (
                      <div className={styles.peaceResult}>
                        Peace Check: {peaceCheckResult}%
                        {peaceCheckResult < 100 && (
                          <div className={styles.warning}>⚠️ This may be counterfeit - wait for 100%</div>
                        )}
                      </div>
                    )}
                  </div>
                )}

                {attack.type === 'doubt_injection' && (
                  <div className={styles.specialTool}>
                    <div className={styles.evidenceLogTitle}>Evidence Log</div>
                    <div className={styles.evidenceList}>
                      {evidenceLog.map((evidence, idx) => (
                        <div key={idx} className={styles.evidenceItem}>{evidence}</div>
                      ))}
                    </div>
                    <div className={styles.evidenceInput}>
                      <input
                        type="text"
                        value={newEvidence}
                        onChange={(e) => setNewEvidence(e.target.value)}
                        placeholder="Add evidence of past shift..."
                        className={styles.evidenceInputField}
                      />
                      <button onClick={addEvidence} className={styles.addEvidenceButton}>
                        Add
                      </button>
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}

      {/* Counter-Strategy Reference */}
      {selectedAttack && (
        <div className={styles.strategyDisplay}>
          <div className={styles.strategyTitle}>Counter-Strategy</div>
          <div className={styles.strategyDecree}>
            "{COUNTER_STRATEGIES[selectedAttack].decree}"
          </div>
          <div className={styles.strategyAction}>
            {COUNTER_STRATEGIES[selectedAttack].action}
          </div>
        </div>
      )}
    </div>
  );
}
