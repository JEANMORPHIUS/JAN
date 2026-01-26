/** * * DAY 1: PRIORITY ACCESS CODE
 *  * Morning Decree, Evening Doorway, 12-Hour Observation Timer
 *  * 
 *  * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 *  * Spiritual Alignment Over Mechanical Productivity
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
 * PANGEA IS THE TABLE.
 * YOU DON'T BETRAY THE TABLE.
 * 
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

import { useState, useEffect, useRef } from 'react';
import { 
  MorningDecree, 
  EveningDoorway, 
  UnexpectedOpening, 
  ObservationTimer 
} from '../../types/divineTiming';
import styles from './Day1Activation.module.css';

interface Day1ActivationProps {
  onComplete: (data: {
    morningDecree: MorningDecree;
    eveningDoorway: EveningDoorway;
    observationTimer: ObservationTimer;
  }) => void;
}

export default function Day1Activation({ onComplete }: Day1ActivationProps) {
  const [morningDecree, setMorningDecree] = useState<MorningDecree>({
    text: '',
    spoken: false,
    facingEast: false
  });
  
  const [eveningDoorway, setEveningDoorway] = useState<EveningDoorway>({
    log: '',
    timestamp: new Date()
  });
  
  const [observationTimer, setObservationTimer] = useState<ObservationTimer>({
    startTime: new Date(),
    endTime: new Date(Date.now() + 12 * 60 * 60 * 1000),
    duration: 12 * 60, // 12 hours in minutes
    openings: []
  });
  
  const [timerActive, setTimerActive] = useState(false);
  const [timeRemaining, setTimeRemaining] = useState(12 * 60 * 60); // 12 hours in seconds
  const intervalRef = useRef<NodeJS.Timeout | null>(null);

  useEffect(() => {
    if (timerActive && timeRemaining > 0) {
      intervalRef.current = setInterval(() => {
        setTimeRemaining(prev => {
          if (prev <= 1) {
            setTimerActive(false);
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    } else {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
    }

    return () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
    };
  }, [timerActive, timeRemaining]);

  const startObservation = () => {
    setTimerActive(true);
    setObservationTimer(prev => ({
      ...prev,
      startTime: new Date(),
      endTime: new Date(Date.now() + 12 * 60 * 60 * 1000)
    }));
  };

  const addOpening = (type: UnexpectedOpening['type'], description: string) => {
    const opening: UnexpectedOpening = {
      type,
      description,
      timestamp: new Date(),
      significance: ''
    };
    
    setObservationTimer(prev => ({
      ...prev,
      openings: [...prev.openings, opening]
    }));
  };

  const formatTime = (seconds: number): string => {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const confirmMorningDecree = () => {
    setMorningDecree(prev => ({
      ...prev,
      spoken: true,
      spokenAt: new Date()
    }));
  };

  const saveEveningDoorway = () => {
    setEveningDoorway(prev => ({
      ...prev,
      timestamp: new Date()
    }));
  };

  useEffect(() => {
    if (morningDecree.spoken && eveningDoorway.log && observationTimer.openings.length > 0) {
      onComplete({
        morningDecree,
        eveningDoorway,
        observationTimer
      });
    }
  }, [morningDecree, eveningDoorway, observationTimer, onComplete]);

  return (
    <div className={styles.day1Container}>
      <div className={styles.dayHeader}>
        <div className={styles.dayNumber}>DAY 1</div>
        <div className={styles.dayTitle}>Priority Access Code</div>
      </div>

      {/* Morning Decree Section */}
      <div className={styles.section}>
        <div className={styles.sectionTitle}>Morning Decree</div>
        <div className={styles.sectionSubtitle}>Face East and speak your decree</div>
        
        <div className={styles.compassIndicator}>
          <div className={styles.compassNeedle}>→</div>
          <div className={styles.compassLabel}>EAST</div>
        </div>

        <textarea
          value={morningDecree.text}
          onChange={(e) => setMorningDecree(prev => ({ ...prev, text: e.target.value }))}
          placeholder="Speak your morning decree here..."
          className={styles.decreeInput}
          rows={4}
        />

        <div className={styles.checkboxGroup}>
          <label className={styles.checkboxLabel}>
            <input
              type="checkbox"
              checked={morningDecree.facingEast}
              onChange={(e) => setMorningDecree(prev => ({ ...prev, facingEast: e.target.checked }))}
            />
            <span>Facing East</span>
          </label>
        </div>

        <button
          onClick={confirmMorningDecree}
          disabled={!morningDecree.text || !morningDecree.facingEast}
          className={styles.confirmButton}
        >
          {morningDecree.spoken ? '✓ Decree Spoken' : 'Confirm Decree Spoken'}
        </button>

        {morningDecree.spoken && morningDecree.spokenAt && (
          <div className={styles.confirmation}>
            Spoken at {new Date(morningDecree.spokenAt).toLocaleTimeString()}
          </div>
        )}
      </div>

      {/* 12-Hour Observation Timer */}
      <div className={styles.section}>
        <div className={styles.sectionTitle}>12-Hour Observation Timer</div>
        <div className={styles.sectionSubtitle}>Track unexpected openings</div>

        {!timerActive ? (
          <button onClick={startObservation} className={styles.startTimerButton}>
            Start 12-Hour Observation
          </button>
        ) : (
          <div className={styles.timerDisplay}>
            <div className={styles.timerTime}>{formatTime(timeRemaining)}</div>
            <div className={styles.timerLabel}>Remaining</div>
          </div>
        )}

        <div className={styles.openingsList}>
          <div className={styles.openingsTitle}>Unexpected Openings:</div>
          {observationTimer.openings.map((opening, idx) => (
            <div key={idx} className={styles.openingItem}>
              <div className={styles.openingType}>{opening.type.toUpperCase()}</div>
              <div className={styles.openingDescription}>{opening.description}</div>
              <div className={styles.openingTime}>
                {new Date(opening.timestamp).toLocaleTimeString()}
              </div>
            </div>
          ))}

          <div className={styles.addOpeningButtons}>
            <button onClick={() => addOpening('email', 'Email received')} className={styles.addButton}>
              + Email
            </button>
            <button onClick={() => addOpening('call', 'Call received')} className={styles.addButton}>
              + Call
            </button>
            <button onClick={() => addOpening('message', 'Message received')} className={styles.addButton}>
              + Message
            </button>
            <button onClick={() => addOpening('other', 'Other opening')} className={styles.addButton}>
              + Other
            </button>
          </div>
        </div>
      </div>

      {/* Evening Doorway Threshold */}
      <div className={styles.section}>
        <div className={styles.sectionTitle}>Evening Doorway Threshold</div>
        <div className={styles.sectionSubtitle}>Log your evening threshold</div>

        <textarea
          value={eveningDoorway.log}
          onChange={(e) => setEveningDoorway(prev => ({ ...prev, log: e.target.value }))}
          placeholder="Record what you observed at the evening threshold..."
          className={styles.doorwayInput}
          rows={5}
        />

        <button
          onClick={saveEveningDoorway}
          disabled={!eveningDoorway.log}
          className={styles.saveButton}
        >
          Save Evening Doorway
        </button>
      </div>
    </div>
  );
}
