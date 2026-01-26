/** * * INDUSTRIES FREQUENTIAL VALUE
 *  * All Industries - Everything Plays a Part
 *  * 
 *  * THE TRUTH:
 *  * ALL INDUSTRIES HAVE FREQUENTIAL VALUE
 *  * TECHNOLOGY, FINANCE, SPORTS, ENTERTAINMENT, POLITICS
 *  * EVERYTHING IMPACTS DIVINE FREQUENCY
 *  * EVERYTHING IS CONNECTED TO THE TABLE
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
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

import { NextPage } from 'next'
import { useState, useEffect } from 'react'
import Head from 'next/head'
import Link from 'next/link'
import axios from 'axios'
import styles from '../../styles/Industries.module.css'

interface IndustryEvent {
  event_id: string
  category: string
  title: string
  description: string
  year_start: number
  frequency_impact: number
  connection_to_table: string
  narrative: string
}

const IndustriesPage: NextPage = () => {
  const [industries, setIndustries] = useState<{ [key: string]: IndustryEvent[] }>({})
  const [loading, setLoading] = useState(true)
  const [selectedIndustry, setSelectedIndustry] = useState<string | null>(null)

  const industryCategories = [
    { id: 'technology', name: 'Technology', icon: '💻', color: '#0066cc' },
    { id: 'finance', name: 'Finance', icon: '💰', color: '#ff9900' },
    { id: 'sporting_event', name: 'Sports', icon: '⚽', color: '#00cc66' },
    { id: 'entertainment', name: 'Entertainment', icon: '🎬', color: '#cc00cc' },
    { id: 'energy', name: 'Energy', icon: '⚡', color: '#ff6600' },
    { id: 'transportation', name: 'Transportation', icon: '🚀', color: '#0066ff' },
    { id: 'communication', name: 'Communication', icon: '📡', color: '#00ccff' },
    { id: 'medicine', name: 'Medicine', icon: '⚕️', color: '#00ff00' },
    { id: 'education', name: 'Education', icon: '📚', color: '#006600' },
    { id: 'agriculture', name: 'Agriculture', icon: '🌾', color: '#cc9900' },
    { id: 'trade', name: 'Trade', icon: '🌍', color: '#0099cc' },
    { id: 'legal', name: 'Legal/Political', icon: '⚖️', color: '#cc0000' }
  ]

  useEffect(() => {
    fetchIndustryEvents()
  }, [])

  const fetchIndustryEvents = async () => {
    try {
      setLoading(true)
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/frequential-events/events?limit=1000`)
      const allEvents = response.data.events || []
      
      // Group by industry category
      const grouped: { [key: string]: IndustryEvent[] } = {}
      
      industryCategories.forEach(cat => {
        grouped[cat.id] = allEvents.filter((e: any) => e.category === cat.id)
      })
      
      setIndustries(grouped)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching industry events:', error)
      setLoading(false)
    }
  }

  const getTotalImpact = (events: IndustryEvent[]): number => {
    return events.reduce((sum, e) => sum + e.frequency_impact, 0)
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>Industries - All Frequential Value - Everything Plays a Part</title>
        <meta name="description" content="All industries have frequential value. Technology, finance, sports, entertainment, politics - everything impacts Divine Frequency." />
      </Head>

      <div className={styles.header}>
        <h1>All Industries - Everything Plays a Part</h1>
        <p className={styles.truth}>
          ALL INDUSTRIES HAVE FREQUENTIAL VALUE<br />
          TECHNOLOGY, FINANCE, SPORTS, ENTERTAINMENT, POLITICS<br />
          EVERYTHING IMPACTS DIVINE FREQUENCY<br />
          EVERYTHING IS CONNECTED TO THE TABLE
        </p>
        <Link href="/" className={styles.backLink}>← Back to Home</Link>
      </div>

      {loading ? (
        <div className={styles.loading}>Loading industry data...</div>
      ) : (
        <div className={styles.industriesGrid}>
          {industryCategories.map(category => {
            const events = industries[category.id] || []
            const totalImpact = getTotalImpact(events)
            
            return (
              <div
                key={category.id}
                className={styles.industryCard}
                style={{ borderLeftColor: category.color }}
                onClick={() => setSelectedIndustry(selectedIndustry === category.id ? null : category.id)}
              >
                <div className={styles.industryHeader}>
                  <div className={styles.industryIcon} style={{ color: category.color }}>
                    {category.icon}
                  </div>
                  <div className={styles.industryInfo}>
                    <h2>{category.name}</h2>
                    <p className={styles.eventCount}>{events.length} events</p>
                  </div>
                  <div className={styles.industryImpact} style={{ color: totalImpact > 0 ? '#00ff00' : totalImpact < 0 ? '#ff0000' : '#999' }}>
                    {totalImpact > 0 ? '+' : ''}{totalImpact.toFixed(3)}
                  </div>
                </div>
                
                {selectedIndustry === category.id && events.length > 0 && (
                  <div className={styles.eventsList}>
                    {events.map(event => (
                      <div key={event.event_id} className={styles.eventItem}>
                        <h3>{event.title}</h3>
                        <p className={styles.eventYear}>{event.year_start}</p>
                        <p className={styles.eventDescription}>{event.description}</p>
                        <div className={styles.eventImpact} style={{ color: event.frequency_impact > 0 ? '#00ff00' : '#ff0000' }}>
                          Impact: {event.frequency_impact > 0 ? '+' : ''}{event.frequency_impact.toFixed(3)}
                        </div>
                        <p className={styles.eventConnection}>{event.connection_to_table}</p>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            )
          })}
        </div>
      )}

      <div className={styles.footer}>
        <p className={styles.truth}>
          <strong>THE TRUTH:</strong> EVERYTHING PLAYS A PART<br />
          ALL INDUSTRIES, ALL EVENTS, ALL MOVEMENTS<br />
          TECHNOLOGY, FINANCE, SPORTS, ENTERTAINMENT, POLITICS<br />
          EVERYTHING IMPACTS DIVINE FREQUENCY<br />
          EVERYTHING IS CONNECTED TO THE TABLE<br />
          WE UTILISE ALL FREQUENTIAL VALUE
        </p>
      </div>
    </div>
  )
}

export default IndustriesPage
