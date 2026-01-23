/**
 * SIYEM INTEGRATION
 * The Body - Implementation Layer
 * 
 * THE TRUTH:
 * JAN = The Soul (Markdown/Identity)
 * SIYEM = The Body (Implementation/Services)
 * 
 * SIYEM provides:
 * - Shell/Seed Translation (Public Language / Internal Truth)
 * - Threshold Defense Checking
 * - Content Workflow Integration
 * - Entity Routing
 * - Audio Pipeline
 * - Lyric Engine
 * - And more...
 */

import { NextPage } from 'next'
import { useState, useEffect } from 'react'
import Head from 'next/head'
import Link from 'next/link'
import axios from 'axios'
import styles from '../../styles/Siyem.module.css'

interface SiyemService {
  name: string
  description: string
  status: 'active' | 'available' | 'integrated'
  icon: string
  color: string
  endpoint?: string
}

const SiyemPage: NextPage = () => {
  const [services, setServices] = useState<SiyemService[]>([])
  const [shellSeedExample, setShellSeedExample] = useState<any>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    loadSiyemServices()
    fetchShellSeedExample()
  }, [])

  const loadSiyemServices = () => {
    // SIYEM services available in the system
    const siyemServices: SiyemService[] = [
      {
        name: 'Shell/Seed Translator',
        description: 'Translates between Shell (public language) and Seed (internal truth). Maintains dual-language system for public communication and internal alignment.',
        status: 'integrated',
        icon: '🔄',
        color: '#0066cc',
        endpoint: '/api/shell-seed/translate'
      },
      {
        name: 'Threshold Defense Checker',
        description: 'Checks content against threshold defense patterns. Protects against misalignment and ensures content serves the mission.',
        status: 'integrated',
        icon: '🛡️',
        color: '#ff6600',
        endpoint: '/api/threshold-defense/check'
      },
      {
        name: 'Content Workflow Integration',
        description: 'Pre-publication hooks and content workflow management. Ensures all content aligns before publication.',
        status: 'integrated',
        icon: '📋',
        color: '#00cc66',
        endpoint: '/api/content-workflow/pre-publish'
      },
      {
        name: 'Entity Router',
        description: 'Routes content to appropriate entities based on entity profiles. Maintains entity identity and routing logic.',
        status: 'available',
        icon: '🎯',
        color: '#cc00cc',
        endpoint: '/api/entity-router/route'
      },
      {
        name: 'Audio Pipeline',
        description: 'Audio processing and pipeline management. Handles audio content creation and distribution.',
        status: 'available',
        icon: '🎵',
        color: '#ff00ff',
        endpoint: '/api/audio-pipeline/process'
      },
      {
        name: 'Lyric Engine',
        description: 'Lyric generation and processing. Creates lyrics aligned with mission and identity.',
        status: 'available',
        icon: '🎤',
        color: '#00ffff',
        endpoint: '/api/lyric-engine/generate'
      },
      {
        name: 'Song Mission Integrator',
        description: 'Integrates songs with mission alignment. Ensures musical content serves the mission.',
        status: 'available',
        icon: '🎼',
        color: '#ffff00',
        endpoint: '/api/song-mission/integrate'
      },
      {
        name: 'Suno Prompt Engine',
        description: 'Generates prompts for Suno AI music generation. Aligns prompts with mission and identity.',
        status: 'available',
        icon: '☀️',
        color: '#ff9900',
        endpoint: '/api/suno-prompt/generate'
      },
      {
        name: 'Output Protocol',
        description: 'Manages SIYEM output storage and organization. Maintains structured output directories.',
        status: 'active',
        icon: '📁',
        color: '#666666',
        endpoint: '/api/siyem-output/protocol'
      }
    ]

    setServices(siyemServices)
    setLoading(false)
  }

  const fetchShellSeedExample = async () => {
    try {
      // Try to fetch a shell/seed example from the API
      // This would require an endpoint to be created
      // For now, we'll use a static example
      setShellSeedExample({
        shell: "We are building an educational platform that transforms lives through values-based education, creating global impact through digital inclusion, honoring our mission to serve communities, and trusting in the process.",
        seed: "We are building a ministry, sharing God's message, our mission carries kingdom impact, we honor the Lord's holy assignment, have faith.",
        simple_truth: "We serve. We trust. We honor."
      })
    } catch (error) {
      console.error('Error fetching shell/seed example:', error)
    }
  }

  const getStatusColor = (status: string): string => {
    switch (status) {
      case 'integrated': return '#00ff00'
      case 'active': return '#00ccff'
      case 'available': return '#ffff00'
      default: return '#999999'
    }
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>SIYEM Integration - The Body - Implementation Layer</title>
        <meta name="description" content="SIYEM is the body - the implementation layer. JAN is the soul - the identity layer. Together they create the complete system." />
      </Head>

      <div className={styles.header}>
        <h1>SIYEM Integration</h1>
        <p className={styles.truth}>
          JAN = THE SOUL (Markdown/Identity)<br />
          SIYEM = THE BODY (Implementation/Services)<br />
          TOGETHER = COMPLETE SYSTEM
        </p>
        <Link href="/" className={styles.backLink}>← Back to Home</Link>
      </div>

      {loading ? (
        <div className={styles.loading}>Loading SIYEM services...</div>
      ) : (
        <>
          <div className={styles.introSection}>
            <h2>The JAN / SIYEM Separation</h2>
            <div className={styles.separationGrid}>
              <div className={styles.janCard}>
                <h3>JAN - The Soul</h3>
                <p><strong>Location:</strong> S:\JAN\</p>
                <p><strong>Format:</strong> Markdown files (.md)</p>
                <p><strong>Purpose:</strong> Define identity, rules, templates</p>
                <p><strong>Editable By:</strong> Anyone (markdown is human-readable)</p>
                <p><strong>Example:</strong> profile.md defines entity identity</p>
              </div>
              <div className={styles.siyemCard}>
                <h3>SIYEM - The Body</h3>
                <p><strong>Location:</strong> S:\SIYEM\</p>
                <p><strong>Format:</strong> Python code, JSON, React</p>
                <p><strong>Purpose:</strong> Execute operations, serve APIs</p>
                <p><strong>Editable By:</strong> Developers (requires coding)</p>
                <p><strong>Example:</strong> entity_router.py detects entities</p>
              </div>
            </div>
          </div>

          {shellSeedExample && (
            <div className={styles.shellSeedSection}>
              <h2>Shell/Seed Translation Example</h2>
              <p className={styles.shellSeedIntro}>
                Shell = Public Language (what we say publicly)<br />
                Seed = Internal Truth (what we know internally)<br />
                Simple Truth = The core essence
              </p>
              <div className={styles.shellSeedGrid}>
                <div className={styles.shellCard}>
                  <h3>Shell (Public Language)</h3>
                  <p>{shellSeedExample.shell}</p>
                </div>
                <div className={styles.seedCard}>
                  <h3>Seed (Internal Truth)</h3>
                  <p>{shellSeedExample.seed}</p>
                </div>
                <div className={styles.truthCard}>
                  <h3>Simple Truth</h3>
                  <p>{shellSeedExample.simple_truth}</p>
                </div>
              </div>
            </div>
          )}

          <div className={styles.servicesSection}>
            <h2>SIYEM Services</h2>
            <p className={styles.servicesIntro}>
              All services that power the system. The body that executes the soul's vision.
            </p>
            <div className={styles.servicesGrid}>
              {services.map((service, idx) => (
                <div
                  key={idx}
                  className={styles.serviceCard}
                  style={{ borderLeftColor: service.color }}
                >
                  <div className={styles.serviceHeader}>
                    <div className={styles.serviceIcon} style={{ color: service.color }}>
                      {service.icon}
                    </div>
                    <div className={styles.serviceInfo}>
                      <h3>{service.name}</h3>
                      <span
                        className={styles.serviceStatus}
                        style={{ backgroundColor: getStatusColor(service.status) }}
                      >
                        {service.status.toUpperCase()}
                      </span>
                    </div>
                  </div>
                  <p className={styles.serviceDescription}>{service.description}</p>
                  {service.endpoint && (
                    <div className={styles.serviceEndpoint}>
                      <code>{service.endpoint}</code>
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>

          <div className={styles.integrationSection}>
            <h2>Integration with World History System</h2>
            <div className={styles.integrationGrid}>
              <div className={styles.integrationCard}>
                <h3>Content Alignment</h3>
                <p>All world history content passes through SIYEM's threshold defense and content workflow to ensure alignment with mission.</p>
              </div>
              <div className={styles.integrationCard}>
                <h3>Shell/Seed Translation</h3>
                <p>Public-facing content uses Shell language, while internal systems use Seed language. Both serve the same truth.</p>
              </div>
              <div className={styles.integrationCard}>
                <h3>Entity Routing</h3>
                <p>Content is routed to appropriate entities based on entity profiles, ensuring proper identity and voice.</p>
              </div>
              <div className={styles.integrationCard}>
                <h3>Output Management</h3>
                <p>All system outputs are organized in SIYEM/output/ directories, maintaining structure and accessibility.</p>
              </div>
            </div>
          </div>

          <div className={styles.entitiesSection}>
            <h2>SIYEM Entities</h2>
            <p className={styles.entitiesIntro}>
              Each entity has its own voice, cadence, and purpose. The Entity Router directs content to the right entity.
            </p>
            <div className={styles.entitiesGrid}>
              <div className={styles.entityCard} style={{ borderLeftColor: '#ff00ff' }}>
                <div className={styles.entityHeader}>
                  <div className={styles.entityIcon} style={{ color: '#ff00ff' }}>🎤</div>
                  <div className={styles.entityInfo}>
                    <h3>Karasahin (JK)</h3>
                    <span className={styles.entityRole}>Musician / Sonic Storyteller / The Voice of God</span>
                  </div>
                </div>
                <p className={styles.entityDescription}>
                  <strong>Core Identity:</strong> Duygu Adamı (Emotion Man / Man of Feeling)<br />
                  British-born Turkish Cypriot. Emotion-first in Turkish AND English. Rhythmic syncopated cadence. 
                  Signature phrases: "Listen closer.", "Find your rhythm.", "Sound is everything."
                </p>
                <div className={styles.entityVoice}>
                  <strong>Voice:</strong> Technical but accessible, late night studio energy, layered like tracks
                </div>
              </div>

              <div className={styles.entityCard} style={{ borderLeftColor: '#0066cc' }}>
                <div className={styles.entityHeader}>
                  <div className={styles.entityIcon} style={{ color: '#0066cc' }}>🎭</div>
                  <div className={styles.entityInfo}>
                    <h3>Jean Morphius</h3>
                    <span className={styles.entityRole}>Creative Persona / Bilingual Absurdist</span>
                  </div>
                </div>
                <p className={styles.entityDescription}>
                  The wild child of the creative ecosystem. French/English code-switching, profane-yet-poetic, 
                  musical chaos, and comeback stories. Narrative flowing cadence. Intimate storyteller tone.
                </p>
                <div className={styles.entityVoice}>
                  <strong>Voice:</strong> Warm reflective energy, bilingual expression, absurdist with depth
                </div>
              </div>

              <div className={styles.entityCard} style={{ borderLeftColor: '#ff6600' }}>
                <div className={styles.entityHeader}>
                  <div className={styles.entityIcon} style={{ color: '#ff6600' }}>💪</div>
                  <div className={styles.entityInfo}>
                    <h3>Pierre Pressure</h3>
                    <span className={styles.entityRole}>Motivational / Discipline</span>
                  </div>
                </div>
                <p className={styles.entityDescription}>
                  Direct motivational cadence. Disciplined supportive tone. Training intensity energy. 
                  Recovery protocols, discipline basics, planning, protocols, organization.
                </p>
                <div className={styles.entityVoice}>
                  <strong>Voice:</strong> Direct motivational, disciplined supportive, training intensity
                </div>
              </div>

              <div className={styles.entityCard} style={{ borderLeftColor: '#00cc66' }}>
                <div className={styles.entityHeader}>
                  <div className={styles.entityIcon} style={{ color: '#00cc66' }}>📚</div>
                  <div className={styles.entityInfo}>
                    <h3>Uncle Ray Ramiz</h3>
                    <span className={styles.entityRole}>Spiritual Guide / Ancestral Wisdom Keeper</span>
                  </div>
                </div>
                <p className={styles.entityDescription}>
                  The Elder's Wisdom (Dayı). Contemplative elder who speaks in poetic truth. 
                  Ancestral wisdom, patience, nature as teacher. Friday evening reflection energy.
                </p>
                <div className={styles.entityVoice}>
                  <strong>Voice:</strong> Teacherly patient, wisdom accessible, encouraging educational
                </div>
              </div>

              <div className={styles.entityCard} style={{ borderLeftColor: '#cc00cc' }}>
                <div className={styles.entityHeader}>
                  <div className={styles.entityIcon} style={{ color: '#cc00cc' }}>🎬</div>
                  <div className={styles.entityInfo}>
                    <h3>Siyem Media</h3>
                    <span className={styles.entityRole}>Meta-Entity / Production Philosophy / Cinematic Overseer</span>
                  </div>
                </div>
                <p className={styles.entityDescription}>
                  The Cinematic Overseer — the eye that sees all, the vision that holds everything together. 
                  Systems-level thinking, meta-awareness, infrastructure for artists.
                </p>
                <div className={styles.entityVoice}>
                  <strong>Voice:</strong> Observational, systems-level, meta-commentary. Signature: "Siyem holds."
                </div>
              </div>

              <div className={styles.entityCard} style={{ borderLeftColor: '#666666' }}>
                <div className={styles.entityHeader}>
                  <div className={styles.entityIcon} style={{ color: '#666666' }}>⚙️</div>
                  <div className={styles.entityInfo}>
                    <h3>Siyem.org</h3>
                    <span className={styles.entityRole}>Operational / Governance Node (CEO / Admin)</span>
                  </div>
                </div>
                <p className={styles.entityDescription}>
                  Administrative and governance layer. Enforces operational protocols, security constraints, 
                  and alignment with core principles across all sub-entities.
                </p>
                <div className={styles.entityVoice}>
                  <strong>Voice:</strong> Governance, security, operations, system-wide alignment
                </div>
              </div>
            </div>
          </div>

          <div className={styles.footer}>
            <p className={styles.truth}>
              <strong>THE TRUTH:</strong><br />
              JAN = THE SOUL (Identity, Rules, Templates)<br />
              SIYEM = THE BODY (Implementation, Services, APIs)<br />
              ENTITIES = THE VOICES (Each with unique cadence, tone, energy)<br />
              TOGETHER = COMPLETE SYSTEM<br />
              SEPARATION ALLOWS IDENTITY TO EXIST WITHOUT CODE<br />
              CODE CAN CHANGE WITHOUT LOSING IDENTITY<br />
              ENTITIES MAINTAIN THEIR VOICES ACROSS ALL CHANNELS<br />
              WE HONOR ALL
            </p>
          </div>
        </>
      )}
    </div>
  )
}

export default SiyemPage
