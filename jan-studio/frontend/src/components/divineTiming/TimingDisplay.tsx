/**
 * TIMING & FREQUENCY DISPLAY
 * Kronos, Chyros, Moed visualization
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 */

import { useEffect, useState } from 'react';
import { ActivationWindow, MoedAppointment, TimingType } from '../../types/divineTiming';
import { getTimeRemaining, checkIdentityShift, formatChyrosTime, isMoedTime, getTimingType } from '../../utils/divineTiming';
import styles from './TimingDisplay.module.css';

interface TimingDisplayProps {
  activationWindow: ActivationWindow;
  moedAppointments: MoedAppointment[];
  activationStart: Date;
}

export default function TimingDisplay({
  activationWindow,
  moedAppointments,
  activationStart
}: TimingDisplayProps) {
  const [currentTime, setCurrentTime] = useState(new Date());
  const [timingType, setTimingType] = useState<TimingType>('kronos');
  const [isMoed, setIsMoed] = useState(false);
  const identityShift = checkIdentityShift(activationStart);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentTime(new Date());
      setTimingType(getTimingType(new Date()));
      setIsMoed(isMoedTime(new Date(), moedAppointments));
    }, 1000);

    return () => clearInterval(interval);
  }, [moedAppointments]);

  const timeRemaining = getTimeRemaining(activationWindow);
  const isChyros = timingType === 'chyros';
  const currentTimingType = getTimingType(currentTime);

  return (
    <div className={styles.timingContainer}>
      <div className={styles.header}>
        <div className={styles.title}>Divine Timing & Frequency</div>
        <div className={`${styles.timingType} ${currentTimingType === 'chyros' ? styles.chyros : ''} ${isMoed ? styles.moed : ''}`}>
          {isMoed ? 'MOED' : currentTimingType.toUpperCase()}
        </div>
      </div>

      {/* Current Time */}
      <div className={styles.currentTime}>
        <div className={styles.timeLabel}>Current Time</div>
        <div className={styles.timeValue}>{formatChyrosTime(currentTime)}</div>
        {currentTimingType === 'chyros' && (
          <div className={styles.chyrosIndicator}>
            ⚡ CHYROS WINDOW - Divine Timing Active
          </div>
        )}
        {isMoed && (
          <div className={styles.moedIndicator}>
            📅 MOED - Appointed Time
          </div>
        )}
      </div>

      {/* Activation Window */}
      <div className={styles.windowDisplay}>
        <div className={styles.windowTitle}>
          {activationWindow.type === '72_hour' ? '72-Hour Activation' : '40-Day Transition'}
        </div>
        <div className={styles.windowProgress}>
          <div className={styles.progressBar}>
            <div
              className={styles.progressFill}
              style={{ width: `${activationWindow.progress}%` }}
            />
          </div>
          <div className={styles.progressText}>
            Day {activationWindow.currentDay} / {activationWindow.type === '72_hour' ? '3' : '40'}
            {' '}• {activationWindow.progress.toFixed(1)}%
          </div>
        </div>
        {timeRemaining.isActive && (
          <div className={styles.timeRemaining}>
            <div className={styles.remainingLabel}>Time Remaining</div>
            <div className={styles.remainingTime}>
              {timeRemaining.hours}h {timeRemaining.minutes}m {timeRemaining.seconds}s
            </div>
          </div>
        )}
      </div>

      {/* Identity Shift Tracker */}
      {activationWindow.type === '40_day' && (
        <div className={styles.identityShift}>
          <div className={styles.shiftTitle}>Identity Shift Progress</div>
          <div className={styles.shiftProgress}>
            <div className={styles.progressBar}>
              <div
                className={styles.progressFill}
                style={{ width: `${identityShift.progress}%` }}
              />
            </div>
            <div className={styles.shiftText}>
              {identityShift.reached 
                ? '✓ Identity Shift Complete (Day 21+)'
                : `${identityShift.daysRemaining} days until Day 21 milestone`
              }
            </div>
          </div>
        </div>
      )}

      {/* Moed Appointments */}
      {moedAppointments.length > 0 && (
        <div className={styles.moedList}>
          <div className={styles.moedTitle}>Moed Appointments</div>
          {moedAppointments.map((appt) => (
            <div
              key={appt.id}
              className={`${styles.moedItem} ${appt.completed ? styles.completed : ''}`}
            >
              <div className={styles.moedName}>{appt.name}</div>
              <div className={styles.moedTime}>
                {formatChyrosTime(new Date(appt.scheduledTime))}
              </div>
              <div className={styles.moedSignificance}>{appt.significance}</div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

