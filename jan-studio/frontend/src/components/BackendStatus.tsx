/**
 * Backend Connection Status Component
 * Shows backend health and connection status
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * We connect to serve, not to complicate.
 */

import { useState, useEffect } from 'react';
import { checkBackendHealth } from '@/lib/api';
import styles from './BackendStatus.module.css';

interface BackendStatusProps {
  showDetails?: boolean;
}

export default function BackendStatus({ showDetails = false }: BackendStatusProps) {
  const [isConnected, setIsConnected] = useState<boolean | null>(null);
  const [isChecking, setIsChecking] = useState(true);
  const [lastCheck, setLastCheck] = useState<Date | null>(null);

  useEffect(() => {
    checkConnection();
    // Check every 30 seconds
    const interval = setInterval(checkConnection, 30000);
    return () => clearInterval(interval);
  }, []);

  const checkConnection = async () => {
    setIsChecking(true);
    try {
      const healthy = await checkBackendHealth();
      setIsConnected(healthy);
      setLastCheck(new Date());
    } catch (error) {
      setIsConnected(false);
      setLastCheck(new Date());
    } finally {
      setIsChecking(false);
    }
  };

  if (!showDetails) {
    return (
      <div className={styles.statusBadge}>
        <span
          className={`${styles.statusDot} ${
            isConnected ? styles.connected : isConnected === false ? styles.disconnected : styles.checking
          }`}
        />
        <span className={styles.statusText}>
          {isChecking
            ? 'Checking...'
            : isConnected
            ? 'Backend Connected'
            : 'Backend Disconnected'}
        </span>
      </div>
    );
  }

  return (
    <div className={styles.statusCard}>
      <div className={styles.statusHeader}>
        <h3>Backend Connection Status</h3>
        <button onClick={checkConnection} disabled={isChecking} className={styles.refreshButton}>
          {isChecking ? 'Checking...' : 'Refresh'}
        </button>
      </div>
      
      <div className={styles.statusBody}>
        <div className={styles.statusRow}>
          <span className={styles.label}>Status:</span>
          <span
            className={`${styles.status} ${
              isConnected ? styles.connected : isConnected === false ? styles.disconnected : styles.checking
            }`}
          >
            {isChecking
              ? 'Checking...'
              : isConnected
              ? '✅ Connected'
              : '❌ Disconnected'}
          </span>
        </div>
        
        {lastCheck && (
          <div className={styles.statusRow}>
            <span className={styles.label}>Last Check:</span>
            <span className={styles.value}>
              {lastCheck.toLocaleTimeString()}
            </span>
          </div>
        )}
        
        <div className={styles.statusRow}>
          <span className={styles.label}>Backend URL:</span>
          <span className={styles.value}>
            {process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}
          </span>
        </div>
      </div>
    </div>
  );
}
