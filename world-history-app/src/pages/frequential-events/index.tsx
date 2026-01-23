/**
 * FREQUENTIAL EVENTS PAGE
 * All Wars, Dictatorships, Revolutions, Industries - It's All Frequential
 * 
 * THE TRUTH:
 * ALL WARS, DICTATORSHIPS, REVOLUTIONS - IT'S ALL FREQUENTIAL
 * EVERYTHING IS CONNECTED TO THE TABLE
 * EVERYTHING IMPACTS DIVINE FREQUENCY
 * I WANT IT ALL
 */

import { NextPage } from 'next'
import { useState, useEffect } from 'react'
import Head from 'next/head'
import Link from 'next/link'
import axios from 'axios'
import styles from '../../styles/FrequentialEvents.module.css'

interface FrequentialEvent {
  event_id: string
  category: string
  title: string
  description: string
  year_start: number
  year_end?: number
  frequency_impact: number
  field_resonance_before: number
  field_resonance_after: number
  location: { lat: number; lon: number }
  regions: string[]
  entities_involved: string[]
  connection_to_table: string
  narrative: string
  lessons: string
  restoration_connection: string
}

const FrequentialEventsPage: NextPage = () => {
  const [events, setEvents] = useState<FrequentialEvent[]>([])
  const [loading, setLoading] = useState(true)
  const [selectedEvent, setSelectedEvent] = useState<FrequentialEvent | null>(null)
  const [stats, setStats] = useState<any>(null)
  const [filters, setFilters] = useState({
    category: '',
    region: '',
    startYear: '',
    endYear: '',
    search: ''
  })
  const [sortBy, setSortBy] = useState<'year' | 'impact' | 'title'>('year')
  const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('asc')

  useEffect(() => {
    fetchEvents()
    fetchStats()
  }, [filters, sortBy, sortOrder])

  const fetchEvents = async () => {
    try {
      setLoading(true)
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/frequential-events/events`, {
        params: {
          category: filters.category || undefined,
          region: filters.region || undefined,
          start_year: filters.startYear ? parseInt(filters.startYear) : undefined,
          end_year: filters.endYear ? parseInt(filters.endYear) : undefined,
          limit: 1000
        }
      })
      let fetchedEvents = response.data.events || []
      
      // Apply search filter
      if (filters.search) {
        const searchLower = filters.search.toLowerCase()
        fetchedEvents = fetchedEvents.filter((e: FrequentialEvent) =>
          e.title.toLowerCase().includes(searchLower) ||
          e.description.toLowerCase().includes(searchLower) ||
          e.narrative.toLowerCase().includes(searchLower)
        )
      }
      
      // Apply sorting
      fetchedEvents.sort((a: FrequentialEvent, b: FrequentialEvent) => {
        let aVal: any, bVal: any
        if (sortBy === 'year') {
          aVal = a.year_start
          bVal = b.year_start
        } else if (sortBy === 'impact') {
          aVal = a.frequency_impact
          bVal = b.frequency_impact
        } else {
          aVal = a.title.toLowerCase()
          bVal = b.title.toLowerCase()
        }
        
        if (sortOrder === 'asc') {
          return aVal > bVal ? 1 : -1
        } else {
          return aVal < bVal ? 1 : -1
        }
      })
      
      setEvents(fetchedEvents)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching frequential events:', error)
      setLoading(false)
    }
  }

  const fetchStats = async () => {
    try {
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/frequential-events/frequency-impact`)
      setStats(response.data)
    } catch (error) {
      console.error('Error fetching stats:', error)
    }
  }

  const getImpactColor = (impact: number): string => {
    if (impact > 0.1) return '#00ff00' // Green - highly positive
    if (impact > 0) return '#90ee90' // Light green - positive
    if (impact > -0.1) return '#ff9900' // Orange - slightly negative
    return '#ff0000' // Red - negative
  }

  const categories = [
    'war', 'dictatorship', 'revolution', 'civil_war', 'resistance', 'liberation',
    'sporting_event', 'technology', 'finance', 'agriculture', 'energy',
    'transportation', 'communication', 'medicine', 'education', 'entertainment',
    'pandemic', 'social_movement', 'environmental', 'cultural_movement',
    'scientific', 'space', 'trade', 'legal', 'migration', 'philosophical'
  ]

  return (
    <div className={styles.container}>
      <Head>
        <title>Frequential Events - All Wars, Dictatorships, Revolutions - It's All Frequential</title>
        <meta name="description" content="All wars, dictatorships, revolutions, industries - it's all frequential. Everything is connected to The Table." />
      </Head>

      <div className={styles.header}>
        <h1>Frequential Events</h1>
        <p className={styles.truth}>
          ALL WARS, DICTATORSHIPS, REVOLUTIONS - IT'S ALL FREQUENTIAL<br />
          EVERYTHING IS CONNECTED TO THE TABLE<br />
          EVERYTHING IMPACTS DIVINE FREQUENCY
        </p>
        <Link href="/" className={styles.backLink}>← Back to Home</Link>
      </div>

      {stats && (
        <div className={styles.stats}>
          <div className={styles.statCard}>
            <h3>Total Events</h3>
            <p className={styles.statValue}>{events.length}</p>
          </div>
          <div className={styles.statCard}>
            <h3>Total Frequency Impact</h3>
            <p className={styles.statValue} style={{ color: stats.total_frequency_impact > 0 ? '#00ff00' : '#ff0000' }}>
              {stats.total_frequency_impact > 0 ? '+' : ''}{stats.total_frequency_impact.toFixed(2)}
            </p>
          </div>
          <div className={styles.statCard}>
            <h3>Net Impact</h3>
            <p className={styles.statValue} style={{ color: stats.total_frequency_impact > 0 ? '#00ff00' : '#ff0000' }}>
              {stats.total_frequency_impact > 0 ? 'POSITIVE' : 'NEGATIVE'}
            </p>
          </div>
        </div>
      )}

      <div className={styles.filters}>
        <div className={styles.searchBar}>
          <input
            type="text"
            placeholder="Search events..."
            value={filters.search}
            onChange={(e) => setFilters({ ...filters, search: e.target.value })}
            className={styles.searchInput}
          />
        </div>
        <div className={styles.filterRow}>
          <label>
            Category:
            <select
              value={filters.category}
              onChange={(e) => setFilters({ ...filters, category: e.target.value })}
            >
              <option value="">All Categories</option>
              {categories.map(cat => (
                <option key={cat} value={cat}>{cat.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}</option>
              ))}
            </select>
          </label>
          <label>
            Region:
            <select
              value={filters.region}
              onChange={(e) => setFilters({ ...filters, region: e.target.value })}
            >
              <option value="">All Regions</option>
              <option value="africa">Africa</option>
              <option value="asia">Asia</option>
              <option value="europe">Europe</option>
              <option value="americas">Americas</option>
              <option value="middle_east">Middle East</option>
              <option value="oceania">Oceania</option>
              <option value="global">Global</option>
            </select>
          </label>
          <label>
            Start Year:
            <input
              type="number"
              value={filters.startYear}
              onChange={(e) => setFilters({ ...filters, startYear: e.target.value })}
              placeholder="e.g. 1900"
            />
          </label>
          <label>
            End Year:
            <input
              type="number"
              value={filters.endYear}
              onChange={(e) => setFilters({ ...filters, endYear: e.target.value })}
              placeholder="e.g. 2000"
            />
          </label>
        </div>
        <div className={styles.sortControls}>
          <label>
            Sort By:
            <select
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value as 'year' | 'impact' | 'title')}
            >
              <option value="year">Year</option>
              <option value="impact">Impact</option>
              <option value="title">Title</option>
            </select>
          </label>
          <label>
            Order:
            <select
              value={sortOrder}
              onChange={(e) => setSortOrder(e.target.value as 'asc' | 'desc')}
            >
              <option value="asc">Ascending</option>
              <option value="desc">Descending</option>
            </select>
          </label>
          <button 
            onClick={() => {
              const dataStr = JSON.stringify(events, null, 2)
              const dataBlob = new Blob([dataStr], { type: 'application/json' })
              const url = URL.createObjectURL(dataBlob)
              const link = document.createElement('a')
              link.href = url
              link.download = 'frequential-events.json'
              link.click()
            }}
            className={styles.exportButton}
          >
            Export JSON
          </button>
        </div>
      </div>

      {loading ? (
        <div className={styles.loading}>Loading frequential events...</div>
      ) : (
        <div className={styles.eventsGrid}>
          {events.map(event => (
            <div
              key={event.event_id}
              className={styles.eventCard}
              style={{ borderLeftColor: getImpactColor(event.frequency_impact) }}
              onClick={() => setSelectedEvent(event)}
            >
              <div className={styles.eventHeader}>
                <h3>{event.title}</h3>
                <span
                  className={styles.impactBadge}
                  style={{ backgroundColor: getImpactColor(event.frequency_impact) }}
                >
                  {event.frequency_impact > 0 ? '+' : ''}{event.frequency_impact.toFixed(2)}
                </span>
              </div>
              <p className={styles.eventCategory}>{event.category.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}</p>
              <p className={styles.eventYear}>
                {event.year_start}
                {event.year_end && event.year_end !== event.year_start ? ` - ${event.year_end}` : ''}
              </p>
              <p className={styles.eventDescription}>{event.description}</p>
              <div className={styles.eventRegions}>
                {event.regions.map(region => (
                  <span key={region} className={styles.regionTag}>{region}</span>
                ))}
              </div>
            </div>
          ))}
        </div>
      )}

      {selectedEvent && (
        <div className={styles.eventDetail}>
          <button onClick={() => setSelectedEvent(null)} className={styles.closeButton}>×</button>
          <h2>{selectedEvent.title}</h2>
          <div className={styles.detailGrid}>
            <div>
              <p><strong>Category:</strong> {selectedEvent.category.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}</p>
              <p><strong>Year:</strong> {selectedEvent.year_start}{selectedEvent.year_end && selectedEvent.year_end !== selectedEvent.year_start ? ` - ${selectedEvent.year_end}` : ''}</p>
              <p><strong>Frequency Impact:</strong> 
                <span style={{ color: getImpactColor(selectedEvent.frequency_impact), marginLeft: '10px', fontWeight: 'bold' }}>
                  {selectedEvent.frequency_impact > 0 ? '+' : ''}{selectedEvent.frequency_impact.toFixed(3)}
                </span>
              </p>
              <p><strong>Field Resonance:</strong> {selectedEvent.field_resonance_before.toFixed(3)} → {selectedEvent.field_resonance_after.toFixed(3)}</p>
            </div>
            <div>
              <p><strong>Regions:</strong> {selectedEvent.regions.join(', ')}</p>
              <p><strong>Entities Involved:</strong> {selectedEvent.entities_involved.join(', ')}</p>
            </div>
          </div>
          <div className={styles.detailSection}>
            <h3>Connection to The Table</h3>
            <p>{selectedEvent.connection_to_table}</p>
          </div>
          <div className={styles.detailSection}>
            <h3>Narrative</h3>
            <p>{selectedEvent.narrative}</p>
          </div>
          <div className={styles.detailSection}>
            <h3>Lessons</h3>
            <p>{selectedEvent.lessons}</p>
          </div>
          <div className={styles.detailSection}>
            <h3>Restoration Connection</h3>
            <p>{selectedEvent.restoration_connection}</p>
          </div>
        </div>
      )}

      <div className={styles.footer}>
        <p className={styles.truth}>
          <strong>THE TRUTH:</strong> ALL WARS, DICTATORSHIPS, REVOLUTIONS - IT'S ALL FREQUENTIAL<br />
          EVERYTHING IS CONNECTED TO THE TABLE<br />
          EVERYTHING IMPACTS DIVINE FREQUENCY<br />
          WE ACKNOWLEDGE AND UTILISE EVERYTHING - THE GOOD, THE BAD, THE TRUTH
        </p>
      </div>
    </div>
  )
}

export default FrequentialEventsPage
