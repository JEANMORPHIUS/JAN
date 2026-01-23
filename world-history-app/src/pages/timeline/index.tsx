/**
 * WORLD HISTORY TIMELINE
 * Interactive Timeline Component
 * 
 * Features:
 * - Horizontal scroll timeline (zoomable)
 * - Click events → expand narrative
 * - Hover → quick info popup
 * - Filter by region, time period, field resonance
 * - Bookmark key events
 */

import { NextPage } from 'next'
import { useState, useEffect, useRef } from 'react'
import Head from 'next/head'
import axios from 'axios'
import * as d3 from 'd3'
import styles from '../../styles/Timeline.module.css'

interface TimelineEvent {
  event_id: string
  title: string
  description: string
  year_occurred: number
  year_precision: string
  event_type: string
  field_resonance: number
  location: { lat: number; lon: number }
  timeline_dimension: string
  narrative: string
  category?: string // frequential event category
  frequency_impact?: number // frequential event impact (-1.0 to 1.0)
  connection_to_table?: string
  lessons?: string
}

const TimelinePage: NextPage = () => {
  const [events, setEvents] = useState<TimelineEvent[]>([])
  const [loading, setLoading] = useState(true)
  const [selectedEvent, setSelectedEvent] = useState<TimelineEvent | null>(null)
  const [filters, setFilters] = useState({
    startYear: -335000000,
    endYear: 2026,
    region: '',
    eventType: '',
    category: '',
    search: ''
  })
  const [eventCount, setEventCount] = useState(0)
  const svgRef = useRef<SVGSVGElement>(null)

  useEffect(() => {
    fetchTimelineData()
  }, [filters])

  const fetchTimelineData = async () => {
    try {
      setLoading(true)
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/public/world-history/timeline`, {
        params: {
          start_year: filters.startYear,
          end_year: filters.endYear,
          region: filters.region || undefined,
          event_type: filters.eventType || undefined,
          limit: 1000
        }
      })
      
      // Also fetch frequential events if showing all or frequential
      if (!filters.eventType || filters.eventType === 'frequential') {
        try {
          const freqResponse = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/frequential-events/events`, {
            params: {
              start_year: filters.startYear,
              end_year: filters.endYear,
              region: filters.region || undefined,
              category: filters.category || undefined,
              limit: 1000
            }
          })
          
          // Merge frequential events into timeline events
          const freqEvents = (freqResponse.data.events || []).map((e: any) => ({
            event_id: e.event_id,
            title: e.title,
            description: e.description,
            year_occurred: e.year_start,
            year_precision: e.year_precision,
            event_type: 'frequential',
            field_resonance: e.field_resonance_after,
            location: e.location,
            timeline_dimension: 'frequential',
            narrative: e.narrative,
            category: e.category,
            frequency_impact: e.frequency_impact,
            connection_to_table: e.connection_to_table,
            lessons: e.lessons
          }))
          
          // Combine and sort by year
          let allEvents = [...(response.data.timeline || []), ...freqEvents]
          
          // Apply search filter
          if (filters.search) {
            const searchLower = filters.search.toLowerCase()
            allEvents = allEvents.filter((e: TimelineEvent) =>
              e.title.toLowerCase().includes(searchLower) ||
              e.description.toLowerCase().includes(searchLower) ||
              (e.narrative && e.narrative.toLowerCase().includes(searchLower))
            )
          }
          
          allEvents.sort((a, b) => a.year_occurred - b.year_occurred)
          setEvents(allEvents)
          setEventCount(allEvents.length)
          setLoading(false)
          return
        } catch (freqError) {
          console.warn('Could not fetch frequential events:', freqError)
          // Continue with just timeline events
        }
      }
      let timelineEvents = response.data.timeline || []
      
      // Apply search filter
      if (filters.search) {
        const searchLower = filters.search.toLowerCase()
        timelineEvents = timelineEvents.filter((e: TimelineEvent) =>
          e.title.toLowerCase().includes(searchLower) ||
          e.description.toLowerCase().includes(searchLower) ||
          (e.narrative && e.narrative.toLowerCase().includes(searchLower))
        )
      }
      
      setEvents(timelineEvents)
      setEventCount(timelineEvents.length)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching timeline:', error)
      setLoading(false)
    }
  }

  useEffect(() => {
    if (events.length > 0 && svgRef.current) {
      renderTimeline()
    }
  }, [events])

  const renderTimeline = () => {
    if (!svgRef.current) return

    const svg = d3.select(svgRef.current)
    svg.selectAll('*').remove()

    const width = svgRef.current.clientWidth || 1200
    const height = 400
    const margin = { top: 20, right: 20, bottom: 60, left: 80 }

    svg.attr('width', width).attr('height', height)

    const xScale = d3.scaleLinear()
      .domain([filters.startYear, filters.endYear])
      .range([margin.left, width - margin.right])

    const yScale = d3.scaleBand()
      .domain(events.map(e => e.event_id))
      .range([margin.top, height - margin.bottom])
      .padding(0.2)

    // Draw timeline line
    svg.append('line')
      .attr('x1', margin.left)
      .attr('x2', width - margin.right)
      .attr('y1', height / 2)
      .attr('y2', height / 2)
      .attr('stroke', '#333')
      .attr('stroke-width', 2)

    // Draw events
    events.forEach(event => {
      const x = xScale(event.year_occurred)
      const y = yScale(event.event_id) || height / 2

      // Event circle - larger for frequential events
      const isFrequential = event.event_type === 'frequential' || event.frequency_impact !== undefined
      const circleSize = isFrequential ? 10 : 8
      const circle = svg.append('circle')
        .attr('cx', x)
        .attr('cy', y)
        .attr('r', circleSize)
        .attr('fill', getResonanceColor(event.field_resonance, event.frequency_impact))
        .attr('stroke', '#fff')
        .attr('stroke-width', isFrequential ? 3 : 2)
        .style('cursor', 'pointer')
        .attr('class', isFrequential ? 'frequential-event' : '')
        .on('click', () => setSelectedEvent(event))
        .on('mouseover', function() {
          d3.select(this).attr('r', circleSize + 4)
        })
        .on('mouseout', function() {
          d3.select(this).attr('r', circleSize)
        })

      // Event label
      svg.append('text')
        .attr('x', x)
        .attr('y', y - 15)
        .attr('text-anchor', 'middle')
        .attr('font-size', '12px')
        .attr('fill', '#333')
        .text(event.title)
    })

    // X-axis
    const xAxis = d3.axisBottom(xScale)
      .tickFormat(d => {
        if (typeof d === 'number') {
          if (d < 0) return `${Math.abs(d)} BCE`
          return `${d} CE`
        }
        return String(d)
      })

    svg.append('g')
      .attr('transform', `translate(0, ${height - margin.bottom})`)
      .call(xAxis)
  }

  const getResonanceColor = (resonance: number, frequencyImpact?: number): string => {
    // If frequential event, use frequency impact for color
    if (frequencyImpact !== undefined) {
      if (frequencyImpact > 0.1) return '#00ff00' // Green - positive impact
      if (frequencyImpact > 0) return '#90ee90' // Light green - slightly positive
      if (frequencyImpact > -0.1) return '#ff9900' // Orange - slightly negative
      return '#ff0000' // Red - negative impact
    }
    // Otherwise use field resonance
    if (resonance >= 0.9) return '#00ff00' // Green - high resonance
    if (resonance >= 0.7) return '#ffff00' // Yellow - moderate
    if (resonance >= 0.5) return '#ff9900' // Orange - low
    return '#ff0000' // Red - very low
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>World History Timeline - The History of The World</title>
        <meta name="description" content="Interactive timeline of world history. From Pangea to restoration." />
      </Head>

      <div className={styles.header}>
        <h1>World History Timeline</h1>
        <p className={styles.truth}>Pangea is The Table. We write the history of the world.</p>
      </div>

      <div className={styles.eventCount}>
        <p>Showing {eventCount} events</p>
      </div>

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
        <div className={styles.filterControls}>
        <label>
          Start Year:
          <input
            type="number"
            value={filters.startYear}
            onChange={(e) => setFilters({ ...filters, startYear: parseInt(e.target.value) })}
          />
        </label>
        <label>
          End Year:
          <input
            type="number"
            value={filters.endYear}
            onChange={(e) => setFilters({ ...filters, endYear: parseInt(e.target.value) })}
          />
        </label>
        <label>
          Event Type:
          <select
            value={filters.eventType}
            onChange={(e) => setFilters({ ...filters, eventType: e.target.value })}
          >
            <option value="">All</option>
            <option value="natural">Natural</option>
            <option value="spiritual">Spiritual</option>
            <option value="historical">Historical</option>
            <option value="frequential">Frequential (Wars, Revolutions, Industries, All)</option>
          </select>
        </label>
        <label>
          Category:
          <select
            value={filters.category || ''}
            onChange={(e) => setFilters({ ...filters, category: e.target.value })}
          >
            <option value="">All Categories</option>
            <option value="war">Wars</option>
            <option value="revolution">Revolutions</option>
            <option value="resistance">Resistance</option>
            <option value="sporting_event">Sporting Events</option>
            <option value="technology">Technology</option>
            <option value="social_movement">Social Movements</option>
            <option value="environmental">Environmental</option>
            <option value="pandemic">Pandemics</option>
          </select>
        </label>
        </div>
      </div>

      {loading ? (
        <div className={styles.loading}>Loading timeline...</div>
      ) : (
        <div className={styles.timelineContainer}>
          <svg ref={svgRef} className={styles.timelineSvg}></svg>
        </div>
      )}

      {selectedEvent && (
        <div className={styles.eventDetail}>
          <button onClick={() => setSelectedEvent(null)} className={styles.closeButton}>×</button>
          <h2>{selectedEvent.title}</h2>
          <p><strong>Year:</strong> {selectedEvent.year_occurred < 0 ? `${Math.abs(selectedEvent.year_occurred)} BCE` : `${selectedEvent.year_occurred} CE`}</p>
          <p><strong>Field Resonance:</strong> {selectedEvent.field_resonance.toFixed(3)}</p>
          {selectedEvent.frequency_impact !== undefined && (
            <p><strong>Frequency Impact:</strong> {selectedEvent.frequency_impact > 0 ? '+' : ''}{selectedEvent.frequency_impact.toFixed(3)}</p>
          )}
          {selectedEvent.category && (
            <p><strong>Category:</strong> {selectedEvent.category.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}</p>
          )}
          <p><strong>Type:</strong> {selectedEvent.event_type}</p>
          {selectedEvent.connection_to_table && (
            <div>
              <p><strong>Connection to The Table:</strong></p>
              <p>{selectedEvent.connection_to_table}</p>
            </div>
          )}
          {selectedEvent.lessons && (
            <div>
              <p><strong>Lessons:</strong></p>
              <p>{selectedEvent.lessons}</p>
            </div>
          )}
          <p><strong>Narrative:</strong> {selectedEvent.narrative}</p>
        </div>
      )}
    </div>
  )
}

export default TimelinePage
