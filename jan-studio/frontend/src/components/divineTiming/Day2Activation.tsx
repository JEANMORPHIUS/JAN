/** * * DAY 2: JOY ACTIVATION SEQUENCE
 *  * 10-Second Smile Timer, 5 Micro-Joy Moments, Evening Protection Recognition
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
import { SmileTimer, MicroJoyMoment, ProtectionRecognition } from '../../types/divineTiming';
import styles from './Day2Activation.module.css';

interface Day2ActivationProps {
  onComplete: (data: {
    smileTimer: SmileTimer;
    microJoys: MicroJoyMoment[];
    protection: ProtectionRecognition;
  }) => void;
}

export default function Day2Activation({ onComplete }: Day2ActivationProps) {
  const [smileTimer, setSmileTimer] = useState<SmileTimer>({
    started: false,
    duration: 10,
    completed: false
  });
  
  const [smileCountdown, setSmileCountdown] = useState(10);
  const [microJoys, setMicroJoys] = useState<MicroJoyMoment[]>([]);
  const [protection, setProtection] = useState<ProtectionRecognition>({
    disaster1: '',
    disaster2: '',
    disaster3: '',
    timestamp: new Date()
  });
  
  const [newJoyDescription, setNewJoyDescription] = useState('');
  const [newJoyEnergy, setNewJoyEnergy] = useState(5);
  const [bodyMovementReminder, setBodyMovementReminder] = useState(false);
  
  const intervalRef = useRef<NodeJS.Timeout | null>(null);

  useEffect(() => {
    if (smileTimer.started && smileCountdown > 0 && !smileTimer.completed) {
      intervalRef.current = setInterval(() => {
        setSmileCountdown(prev => {
          if (prev <= 1) {
            setSmileTimer(prev => ({ ...prev, completed: true }));
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
  }, [smileTimer.started, smileCountdown, smileTimer.completed]);

  const startSmileTimer = () => {
    setSmileTimer(prev => ({ ...prev, started: true, startTime: new Date() }));
    setSmileCountdown(10);
    setBodyMovementReminder(true);
  };

  const addMicroJoy = () => {
    if (newJoyDescription.trim()) {
      const joy: MicroJoyMoment = {
        id: Date.now().toString(),
        description: newJoyDescription,
        timestamp: new Date(),
        energyLevel: newJoyEnergy
      };
      setMicroJoys(prev => [...prev, joy]);
      setNewJoyDescription('');
      setNewJoyEnergy(5);
    }
  };

  const saveProtection = () => {
    setProtection(prev => ({
      ...prev,
      timestamp: new Date()
    }));
  };

  useEffect(() => {
    if (smileTimer.completed && microJoys.length >= 5 && 
        protection.disaster1 && protection.disaster2 && protection.disaster3) {
      onComplete({
        smileTimer,
        microJoys,
        protection
      });
    }
  }, [smileTimer, microJoys, protection, onComplete]);

  return (
    <div className={styles.day2Container}>
      <div className={styles.dayHeader}>
        <div className={styles.dayNumber}>DAY 2</div>
        <div className={styles.dayTitle}>Joy Activation Sequence</div>
      </div>

      {/* 10-Second Smile Timer */}
      <div className={styles.section}>
        <div className={styles.sectionTitle}>10-Second Smile Timer</div>
        <div className={styles.sectionSubtitle}>Neuroscience-based joy activation</div>
        <div className={styles.neuroscienceNote}>
          Joy is energy in motion - physical movement enhances activation
        </div>

        {bodyMovementReminder && (
          <div className={styles.movementReminder}>
            💃 Move your body during this activation!
          </div>
        )}

        {!smileTimer.started ? (
          <button onClick={startSmileTimer} className={styles.startSmileButton}>
            Start Smile Timer
          </button>
        ) : !smileTimer.completed ? (
          <div className={styles.smileDisplay}>
            <div className={styles.smileEmoji}>😊</div>
            <div className={styles.smileCountdown}>{smileCountdown}</div>
            <div className={styles.smileInstruction}>Keep Smiling!</div>
          </div>
        ) : (
          <div className={styles.smileComplete}>
            <div className={styles.completeCheckmark}>✓</div>
            <div className={styles.completeMessage}>Joy Activated!</div>
            <div className={styles.completeTime}>
              Completed at {smileTimer.startTime 
                ? new Date(smileTimer.startTime).toLocaleTimeString()
                : 'Now'}
            </div>
          </div>
        )}
      </div>

      {/* 5 Micro-Joy Moments */}
      <div className={styles.section}>
        <div className={styles.sectionTitle}>5 Micro-Joy Moments</div>
        <div className={styles.sectionSubtitle}>Log moments of joy throughout the day</div>

        <div className={styles.joyProgress}>
          {microJoys.length} / 5 Moments Logged
        </div>

        <div className={styles.joyInputGroup}>
          <textarea
            value={newJoyDescription}
            onChange={(e) => setNewJoyDescription(e.target.value)}
            placeholder="Describe your micro-joy moment..."
            className={styles.joyInput}
            rows={3}
          />

          <div className={styles.energySlider}>
            <label>Energy Level: {newJoyEnergy}</label>
            <input
              type="range"
              min="1"
              max="10"
              value={newJoyEnergy}
              onChange={(e) => setNewJoyEnergy(Number(e.target.value))}
              className={styles.slider}
            />
            <div className={styles.sliderLabels}>
              <span>Low</span>
              <span>High</span>
            </div>
          </div>

          <button
            onClick={addMicroJoy}
            disabled={!newJoyDescription.trim() || microJoys.length >= 5}
            className={styles.addJoyButton}
          >
            Add Joy Moment
          </button>
        </div>

        <div className={styles.joyList}>
          {microJoys.map((joy) => (
            <div key={joy.id} className={styles.joyItem}>
              <div className={styles.joyDescription}>{joy.description}</div>
              <div className={styles.joyMeta}>
                <span className={styles.joyEnergy}>Energy: {joy.energyLevel}/10</span>
                <span className={styles.joyTime}>
                  {new Date(joy.timestamp).toLocaleTimeString()}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Evening Protection Recognition */}
      <div className={styles.section}>
        <div className={styles.sectionTitle}>Evening Protection Recognition</div>
        <div className={styles.sectionSubtitle}>List three disasters prevented by God</div>

        <div className={styles.protectionInputs}>
          <div className={styles.protectionItem}>
            <label>Disaster 1 Prevented:</label>
            <input
              type="text"
              value={protection.disaster1}
              onChange={(e) => setProtection(prev => ({ ...prev, disaster1: e.target.value }))}
              placeholder="What disaster was prevented?"
              className={styles.protectionInput}
            />
          </div>

          <div className={styles.protectionItem}>
            <label>Disaster 2 Prevented:</label>
            <input
              type="text"
              value={protection.disaster2}
              onChange={(e) => setProtection(prev => ({ ...prev, disaster2: e.target.value }))}
              placeholder="What disaster was prevented?"
              className={styles.protectionInput}
            />
          </div>

          <div className={styles.protectionItem}>
            <label>Disaster 3 Prevented:</label>
            <input
              type="text"
              value={protection.disaster3}
              onChange={(e) => setProtection(prev => ({ ...prev, disaster3: e.target.value }))}
              placeholder="What disaster was prevented?"
              className={styles.protectionInput}
            />
          </div>
        </div>

        <button
          onClick={saveProtection}
          disabled={!protection.disaster1 || !protection.disaster2 || !protection.disaster3}
          className={styles.saveProtectionButton}
        >
          Save Protection Recognition
        </button>
      </div>
    </div>
  );
}
