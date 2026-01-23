/**
 * NOURISHMENT HIVE
 * Working Forward - Best Case Scenarios for All Mankind and Earth
 * 
 * THE TRUTH:
 * IN A BROKEN WORLD HUMANS ARE BROKEN
 * WHAT THEY CONSUME CREATES ALL THE CHAOS INTERNALLY
 * SINCE WE'VE WORKED BACKWARDS...LETS WORK FORWARD
 * CONSIDER ALL POTENTIAL AND BEST CASE SCENARIOS
 * FOR ALL MANKIND AND THE EARTH
 * HOW DO WE BEST NOURISH EACH OTHER AS A HIVE
 */

import { NextPage } from 'next'
import { useState, useEffect } from 'react'
import Head from 'next/head'
import Link from 'next/link'
import axios from 'axios'
import styles from '../../styles/NourishmentHive.module.css'

interface NourishmentSource {
  name: string
  type: string
  impact: number
  accessibility: number
  sustainability: number
  hive_benefit: string
  consumption_healing: string
  best_case_scenario: string
}

interface BestCaseScenario {
  domain: string
  vision: string
  current_state: string
  transformation_path: string[]
  nourishment_required: string[]
  hive_benefit: string
  earth_benefit: string
  timeline: string
  indicators: string[]
}

const NourishmentHivePage: NextPage = () => {
  const [plan, setPlan] = useState<any>(null)
  const [path, setPath] = useState<any>(null)
  const [loading, setLoading] = useState(true)
  const [selectedScenario, setSelectedScenario] = useState<string | null>(null)
  const [selectedSource, setSelectedSource] = useState<string | null>(null)

  useEffect(() => {
    fetchNourishmentData()
  }, [])

  const fetchNourishmentData = async () => {
    try {
      setLoading(true)
      const [planResponse, pathResponse] = await Promise.all([
        axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/nourishment-hive/nourishment-plan`),
        axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/nourishment-hive/hive-path`)
      ])
      setPlan(planResponse.data.plan)
      setPath(pathResponse.data.path)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching nourishment data:', error)
      setLoading(false)
    }
  }

  const getTypeColor = (type: string): string => {
    const colors: { [key: string]: string } = {
      physical: '#ff6600',
      emotional: '#ff00ff',
      mental: '#0066cc',
      spiritual: '#00cc66',
      creative: '#cc00cc',
      community: '#00ffff',
      environmental: '#00ff00',
      economic: '#ff9900'
    }
    return colors[type] || '#666'
  }

  const getAccessibilityColor = (access: number): string => {
    if (access >= 0.8) return '#00ff00'
    if (access >= 0.6) return '#ffff00'
    if (access >= 0.4) return '#ff9900'
    return '#ff0000'
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>Nourishment Hive - Working Forward - Best Case Scenarios</title>
        <meta name="description" content="How do we best nourish each other as a hive? Best case scenarios for all mankind and Earth." />
      </Head>

      <div className={styles.header}>
        <h1>Nourishment Hive</h1>
        <p className={styles.truth}>
          IN A BROKEN WORLD HUMANS ARE BROKEN<br />
          WHAT THEY CONSUME CREATES ALL THE CHAOS INTERNALLY<br />
          SINCE WE'VE WORKED BACKWARDS...LETS WORK FORWARD<br />
          CONSIDER ALL POTENTIAL AND BEST CASE SCENARIOS<br />
          FOR ALL MANKIND AND THE EARTH<br />
          HOW DO WE BEST NOURISH EACH OTHER AS A HIVE
        </p>
        <Link href="/" className={styles.backLink}>← Back to Home</Link>
      </div>

      {loading ? (
        <div className={styles.loading}>Loading nourishment hive data...</div>
      ) : plan && path && (
        <>
          <div className={styles.visionSection}>
            <h2>Vision</h2>
            <p className={styles.visionText}>{plan.vision}</p>
            <p className={styles.principle}>{plan.principle}</p>
          </div>

          <div className={styles.pathSection}>
            <h2>Hive Nourishment Path</h2>
            <p className={styles.currentState}>{path.current_state}</p>
            <p className={styles.transformation}>{path.transformation}</p>
            <div className={styles.pathSteps}>
              {path.path.map((step: any, idx: number) => (
                <div key={idx} className={styles.pathStep}>
                  <div className={styles.stepNumber}>{step.step}</div>
                  <div className={styles.stepContent}>
                    <h3>{step.phase}</h3>
                    <p className={styles.stepAction}>{step.action}</p>
                    <p className={styles.stepNourishment}>Nourishment: {step.nourishment}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className={styles.sourcesSection}>
            <h2>Nourishment Sources</h2>
            <p className={styles.sectionIntro}>
              Sources of nourishment that heal broken consumption patterns
            </p>
            <div className={styles.sourcesGrid}>
              {Object.entries(plan.nourishment_sources || {}).map(([sourceId, source]: [string, any]) => (
                <div
                  key={sourceId}
                  className={styles.sourceCard}
                  style={{ borderLeftColor: getTypeColor(source.type) }}
                  onClick={() => setSelectedSource(selectedSource === sourceId ? null : sourceId)}
                >
                  <div className={styles.sourceHeader}>
                    <h3>{source.name}</h3>
                    <span className={styles.sourceType} style={{ backgroundColor: getTypeColor(source.type) }}>
                      {source.type}
                    </span>
                  </div>
                  <div className={styles.sourceMetrics}>
                    <div className={styles.metric}>
                      <span>Impact:</span>
                      <span style={{ color: '#00ff00' }}>{source.impact.toFixed(1)}</span>
                    </div>
                    <div className={styles.metric}>
                      <span>Accessibility:</span>
                      <span style={{ color: getAccessibilityColor(source.accessibility) }}>
                        {(source.accessibility * 100).toFixed(0)}%
                      </span>
                    </div>
                    <div className={styles.metric}>
                      <span>Sustainability:</span>
                      <span style={{ color: source.sustainability > 0.7 ? '#00ff00' : '#ff9900' }}>
                        {(source.sustainability * 100).toFixed(0)}%
                      </span>
                    </div>
                  </div>
                  <p className={styles.hiveBenefit}>{source.hive_benefit}</p>
                  
                  {selectedSource === sourceId && (
                    <div className={styles.sourceDetails}>
                      <div className={styles.detailSection}>
                        <h4>Consumption Healing:</h4>
                        <p>{source.consumption_healing}</p>
                      </div>
                      <div className={styles.detailSection}>
                        <h4>Best Case Scenario:</h4>
                        <p>{source.best_case_scenario}</p>
                      </div>
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>

          <div className={styles.scenariosSection}>
            <h2>Best Case Scenarios</h2>
            <p className={styles.sectionIntro}>
              Best case scenarios for all mankind and Earth
            </p>
            <div className={styles.scenariosGrid}>
              {Object.entries(plan.best_case_scenarios || {}).map(([scenarioId, scenario]: [string, any]) => (
                <div
                  key={scenarioId}
                  className={styles.scenarioCard}
                  style={{ borderLeftColor: getTypeColor(scenario.domain) }}
                  onClick={() => setSelectedScenario(selectedScenario === scenarioId ? null : scenarioId)}
                >
                  <div className={styles.scenarioHeader}>
                    <h3>{scenario.vision}</h3>
                    <span className={styles.scenarioDomain} style={{ backgroundColor: getTypeColor(scenario.domain) }}>
                      {scenario.domain}
                    </span>
                  </div>
                  <div className={styles.scenarioCurrent}>
                    <strong>Current:</strong> {scenario.current_state}
                  </div>
                  <div className={styles.scenarioTimeline}>
                    <strong>Timeline:</strong> {scenario.timeline}
                  </div>
                  
                  {selectedScenario === scenarioId && (
                    <div className={styles.scenarioDetails}>
                      <div className={styles.detailSection}>
                        <h4>Transformation Path:</h4>
                        <ul>
                          {scenario.transformation_path.map((step: string, idx: number) => (
                            <li key={idx}>{step}</li>
                          ))}
                        </ul>
                      </div>
                      <div className={styles.detailSection}>
                        <h4>Hive Benefit:</h4>
                        <p>{scenario.hive_benefit}</p>
                      </div>
                      <div className={styles.detailSection}>
                        <h4>Earth Benefit:</h4>
                        <p>{scenario.earth_benefit}</p>
                      </div>
                      <div className={styles.detailSection}>
                        <h4>Indicators:</h4>
                        <ul>
                          {scenario.indicators.map((indicator: string, idx: number) => (
                            <li key={idx}>{indicator}</li>
                          ))}
                        </ul>
                      </div>
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>

          <div className={styles.consumptionHealingSection}>
            <h2>Consumption Healing</h2>
            <div className={styles.healingGrid}>
              <div className={styles.brokenConsumption}>
                <h3>Broken Consumption (Creates Chaos)</h3>
                <ul>
                  {plan.consumption_healing?.broken_consumption?.map((item: string, idx: number) => (
                    <li key={idx} className={styles.brokenItem}>{item}</li>
                  ))}
                </ul>
              </div>
              <div className={styles.nourishmentReplacement}>
                <h3>Nourishment Replacement (Heals)</h3>
                <ul>
                  {plan.consumption_healing?.nourishment_replacement?.map((item: string, idx: number) => (
                    <li key={idx} className={styles.nourishmentItem}>{item}</li>
                  ))}
                </ul>
              </div>
            </div>
          </div>

          <div className={styles.footer}>
            <p className={styles.truth}>
              <strong>THE TRUTH:</strong><br />
              {plan.the_truth}
            </p>
          </div>
        </>
      )}
    </div>
  )
}

export default NourishmentHivePage
