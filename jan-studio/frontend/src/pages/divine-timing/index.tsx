/**
 * DIVINE TIMING & SPIRITUAL ACTIVATION DASHBOARD
 * Chosen Light Protocols
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 */

import { useState, useEffect } from 'react';
import Head from 'next/head';
import { useRouter } from 'next/router';
import { useAuth } from '../../contexts/AuthContext';
import { ActivationState, DigitalAltar, ActivationDay } from '../../types/divineTiming';
import { create72HourWindow, create40DayWindow } from '../../utils/divineTiming';
import DigitalAltarComponent from '../../components/divineTiming/DigitalAltar';
import Day1Activation from '../../components/divineTiming/Day1Activation';
import Day2Activation from '../../components/divineTiming/Day2Activation';
import Day3Activation from '../../components/divineTiming/Day3Activation';
import SpiritualAttackCounter from '../../components/divineTiming/SpiritualAttackCounter';
import TimingDisplay from '../../components/divineTiming/TimingDisplay';
import styles from './divineTiming.module.css';

export default function DivineTimingDashboard() {
  const router = useRouter();
  const { user, isAuthenticated } = useAuth();
  const [activationState, setActivationState] = useState<ActivationState | null>(null);
  const [currentDay, setCurrentDay] = useState<1 | 2 | 3 | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!isAuthenticated) {
      router.push('/login?redirect=/divine-timing');
      return;
    }

    // Load or initialize activation state
    loadActivationState();
  }, [isAuthenticated, router]);

  const loadActivationState = () => {
    // Try to load from localStorage
    const saved = localStorage.getItem('divineTimingActivation');
    if (saved) {
      const parsed = JSON.parse(saved);
      parsed.activationStart = new Date(parsed.activationStart);
      setActivationState(parsed);
      setCurrentDay(parsed.currentDay as 1 | 2 | 3);
    } else {
      // Initialize new activation
      const startDate = new Date();
      const state: ActivationState = {
        currentDay: 1,
        activationStart: startDate,
        days: [],
        attacks: [],
        timingWindows: [
          create72HourWindow(startDate),
          create40DayWindow(startDate)
        ],
        moedAppointments: [],
        digitalAltar: {
          beforeStatus: '',
          readyConfirmed: false
        },
        identityShiftProgress: 0
      };
      setActivationState(state);
      setCurrentDay(1);
    }
    setLoading(false);
  };

  const saveActivationState = (state: ActivationState) => {
    localStorage.setItem('divineTimingActivation', JSON.stringify(state));
    setActivationState(state);
  };

  const confirmDigitalAltar = (status: string) => {
    if (!activationState) return;
    
    const updated: ActivationState = {
      ...activationState,
      digitalAltar: {
        ...activationState.digitalAltar,
        beforeStatus: status,
        readyConfirmed: true,
        confirmedAt: new Date(),
        activationCode: `ACT-${Date.now()}`
      }
    };
    saveActivationState(updated);
  };

  const handleDay1Complete = (data: any) => {
    if (!activationState) return;
    
    const updated: ActivationState = {
      ...activationState,
      days: [
        ...activationState.days,
        {
          day: 1,
          date: new Date(),
          completed: true,
          components: []
        }
      ],
      currentDay: 2
    };
    saveActivationState(updated);
    setCurrentDay(2);
  };

  const handleDay2Complete = (data: any) => {
    if (!activationState) return;
    
    const updated: ActivationState = {
      ...activationState,
      days: [
        ...activationState.days.filter(d => d.day !== 2),
        {
          day: 2,
          date: new Date(),
          completed: true,
          components: []
        }
      ],
      currentDay: 3
    };
    saveActivationState(updated);
    setCurrentDay(3);
  };

  const handleDay3Complete = (data: any) => {
    if (!activationState) return;
    
    const updated: ActivationState = {
      ...activationState,
      days: [
        ...activationState.days.filter(d => d.day !== 3),
        {
          day: 3,
          date: new Date(),
          completed: true,
          components: []
        }
      ]
    };
    saveActivationState(updated);
  };

  const handleAttackDetected = (attack: any) => {
    if (!activationState) return;
    
    const updated: ActivationState = {
      ...activationState,
      attacks: [...activationState.attacks, attack]
    };
    saveActivationState(updated);
  };

  const handleCounterApplied = (attackId: string, decree: string) => {
    if (!activationState) return;
    
    const updated: ActivationState = {
      ...activationState,
      attacks: activationState.attacks.map(a =>
        a.id === attackId
          ? { ...a, countered: true, counterDecree: decree }
          : a
      )
    };
    saveActivationState(updated);
  };

  if (loading || !activationState) {
    return (
      <div className={styles.loading}>
        <div className={styles.loadingText}>Loading Activation Dashboard...</div>
      </div>
    );
  }

  const chyrosWindow = activationState.timingWindows.find(w => w.type === '72_hour');
  const transitionWindow = activationState.timingWindows.find(w => w.type === '40_day');

  return (
    <>
      <Head>
        <title>Divine Timing & Spiritual Activation | Chosen Light</title>
        <meta name="description" content="Divine Timing & Spiritual Activation Dashboard - Chosen Light Protocols" />
      </Head>

      <div className={styles.dashboardContainer}>
        {/* Chyros Atmosphere Header */}
        <div className={styles.chyrosHeader}>
          <div className={styles.headerTitle}>DIVINE TIMING & SPIRITUAL ACTIVATION</div>
          <div className={styles.headerSubtitle}>Chosen Light Protocols</div>
          <div className={styles.headerUrgency}>⚡ URGENT • CELEBRATORY • FOCUSED ⚡</div>
        </div>

        {/* Digital Altar - Must be completed first */}
        {!activationState.digitalAltar.readyConfirmed && (
          <div className={styles.altarSection}>
            <DigitalAltarComponent
              altar={activationState.digitalAltar}
              onConfirm={confirmDigitalAltar}
            />
          </div>
        )}

        {/* Main Content - Only show after altar confirmation */}
        {activationState.digitalAltar.readyConfirmed && (
          <>
            {/* Timing Display */}
            <div className={styles.timingSection}>
              {chyrosWindow && (
                <TimingDisplay
                  activationWindow={chyrosWindow}
                  moedAppointments={activationState.moedAppointments}
                  activationStart={activationState.activationStart}
                />
              )}
            </div>

            {/* Three-Day Activation Protocol */}
            <div className={styles.activationSection}>
              {currentDay === 1 && (
                <Day1Activation onComplete={handleDay1Complete} />
              )}
              {currentDay === 2 && (
                <Day2Activation onComplete={handleDay2Complete} />
              )}
              {currentDay === 3 && (
                <Day3Activation onComplete={handleDay3Complete} />
              )}
            </div>

            {/* Spiritual Attack Counter-Strategy */}
            <div className={styles.attackSection}>
              <SpiritualAttackCounter
                attacks={activationState.attacks}
                onAttackDetected={handleAttackDetected}
                onCounterApplied={handleCounterApplied}
              />
            </div>
          </>
        )}
      </div>
    </>
  );
}
