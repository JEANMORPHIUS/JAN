/**
 * WORLD HISTORY RESTORATION
 * 6-Step Framework Progress and Divine Frequency Tracker
 * 
 * Features:
 * - 6-step restoration framework progress
 * - Divine Frequency tracker (0.78 → 1.0)
 * - Real-time updates via WebSocket
 * - Progress visualization
 */

import { NextPage } from 'next'
import { useState, useEffect, useRef } from 'react'
import Head from 'next/head'
import axios from 'axios'
import styles from '../../styles/Restoration.module.css'

interface DivineFrequency {
  current_frequency: number
  target_frequency: number
  frequency_state: string
  alignment_percentage: number
  gap: number
  progress: {
    from: number
    to: number
    current: number
    percentage: number
  }
  the_truth: string
}

interface RestorationStep {
  step_number: number
  step_name: string
  description: string
  status: 'pending' | 'in_progress' | 'completed'
  progress_percentage: number
}

const RestorationPage: NextPage = () => {
  const [frequency, setFrequency] = useState<DivineFrequency | null>(null)
  const [loading, setLoading] = useState(true)
  const [wsConnected, setWsConnected] = useState(false)
  const wsRef = useRef<WebSocket | null>(null)

  const restorationSteps: RestorationStep[] = [
    {
      step_number: 1,
      step_name: 'Recognize The Original Error',
      description: 'Acknowledge the first separation and Mayan codification',
      status: 'completed',
      progress_percentage: 100
    },
    {
      step_number: 2,
      step_name: 'Cleanse The Shell',
      description: 'Neutralize sabotage sites, break contracts, restore heritage',
      status: 'in_progress',
      progress_percentage: 45
    },
    {
      step_number: 3,
      step_name: 'Restore Divine Frequency',
      description: 'Activate sources, increase contributions, restore toward 1.0',
      status: 'in_progress',
      progress_percentage: 22
    },
    {
      step_number: 4,
      step_name: 'Reconnect The Table',
      description: 'Restore connections, rebuild unity, reconnect Pangea',
      status: 'pending',
      progress_percentage: 0
    },
    {
      step_number: 5,
      step_name: 'Complete The Restoration',
      description: 'Finalize restoration, achieve perfect unity (1.0)',
      status: 'pending',
      progress_percentage: 0
    },
    {
      step_number: 6,
      step_name: 'Maintain The Table',
      description: 'Protect The Table, maintain unity, prevent future separation',
      status: 'pending',
      progress_percentage: 0
    }
  ]

  useEffect(() => {
    fetchFrequency()
    connectWebSocket()
    
    return () => {
      if (wsRef.current) {
        wsRef.current.close()
      }
    }
  }, [])

  const fetchFrequency = async () => {
    try {
      setLoading(true)
      const response = await axios.get(
        `${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/public/world-history/frequency`
      )
      setFrequency(response.data)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching frequency:', error)
      setLoading(false)
    }
  }

  const connectWebSocket = () => {
    try {
      const wsUrl = process.env.NEXT_PUBLIC_API_URL?.replace('http', 'ws') || 'ws://localhost:8000'
      const ws = new WebSocket(`${wsUrl}/api/public/world-history/ws`)
      
      ws.onopen = () => {
        setWsConnected(true)
        ws.send(JSON.stringify({ action: 'subscribe_frequency' }))
      }
      
      ws.onmessage = (event) => {
        const data = JSON.parse(event.data)
        if (data.type === 'frequency_update') {
          setFrequency(prev => prev ? {
            ...prev,
            current_frequency: data.value,
            progress: {
              ...prev.progress,
              current: data.value,
              percentage: ((data.value - 0.78) / (1.0 - 0.78)) * 100
            }
          } : null)
        }
      }
      
      ws.onerror = (error) => {
        console.error('WebSocket error:', error)
        setWsConnected(false)
      }
      
      ws.onclose = () => {
        setWsConnected(false)
        // Reconnect after 5 seconds
        setTimeout(connectWebSocket, 5000)
      }
      
      wsRef.current = ws
    } catch (error) {
      console.error('Error connecting WebSocket:', error)
    }
  }

  const getFrequencyColor = (freq: number): string => {
    if (freq >= 0.9) return '#00ff00' // Green
    if (freq >= 0.7) return '#ffff00' // Yellow
    if (freq >= 0.5) return '#ff9900' // Orange
    return '#ff0000' // Red
  }

  const getStepStatusColor = (status: string): string => {
    switch (status) {
      case 'completed': return '#00ff00'
      case 'in_progress': return '#ffff00'
      default: return '#666'
    }
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>Restoration Progress - The History of The World</title>
        <meta name="description" content="6-step framework. Divine Frequency. Progress toward perfect unity (1.0)." />
      </Head>

      <div className={styles.header}>
        <h1>Restoration Progress</h1>
        <p className={styles.truth}>6-step framework. Divine Frequency. Progress toward perfect unity (1.0).</p>
        <div className={styles.wsStatus}>
          <span className={wsConnected ? styles.connected : styles.disconnected}>
            {wsConnected ? '●' : '○'} {wsConnected ? 'Connected' : 'Disconnected'}
          </span>
        </div>
      </div>

      {loading ? (
        <div className={styles.loading}>Loading restoration data...</div>
      ) : (
        <>
          {frequency && (
            <div className={styles.frequencySection}>
              <h2>Divine Frequency</h2>
              <div className={styles.frequencyDisplay}>
                <div className={styles.frequencyValue}>
                  <span className={styles.currentValue}>
                    {frequency.current_frequency.toFixed(3)}
                  </span>
                  <span className={styles.targetValue}>
                    → {frequency.target_frequency.toFixed(1)}
                  </span>
                </div>
                <div className={styles.frequencyBar}>
                  <div
                    className={styles.frequencyProgress}
                    style={{
                      width: `${frequency.progress.percentage}%`,
                      backgroundColor: getFrequencyColor(frequency.current_frequency)
                    }}
                  >
                    <span className={styles.progressLabel}>
                      {frequency.progress.percentage.toFixed(1)}%
                    </span>
                  </div>
                </div>
                <div className={styles.frequencyInfo}>
                  <span>State: {frequency.frequency_state}</span>
                  <span>Alignment: {frequency.alignment_percentage.toFixed(1)}%</span>
                  <span>Gap: {frequency.gap.toFixed(3)}</span>
                </div>
                <div className={styles.truthBox}>
                  <p>{frequency.the_truth}</p>
                </div>
              </div>
            </div>
          )}

          <div className={styles.stepsSection}>
            <h2>6-Step Restoration Framework</h2>
            <div className={styles.stepsList}>
              {restorationSteps.map(step => (
                <div key={step.step_number} className={styles.stepCard}>
                  <div className={styles.stepHeader}>
                    <div className={styles.stepNumber}>{step.step_number}</div>
                    <div className={styles.stepInfo}>
                      <h3>{step.step_name}</h3>
                      <p>{step.description}</p>
                    </div>
                    <div
                      className={styles.stepStatus}
                      style={{ color: getStepStatusColor(step.status) }}
                    >
                      {step.status.replace('_', ' ').toUpperCase()}
                    </div>
                  </div>
                  <div className={styles.stepProgress}>
                    <div className={styles.progressBar}>
                      <div
                        className={styles.progressFill}
                        style={{
                          width: `${step.progress_percentage}%`,
                          backgroundColor: getStepStatusColor(step.status)
                        }}
                      />
                    </div>
                    <span className={styles.progressText}>
                      {step.progress_percentage}%
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </>
      )}
    </div>
  )
}

export default RestorationPage
