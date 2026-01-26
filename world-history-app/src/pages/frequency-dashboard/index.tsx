/** * * FREQUENCY IMPACT DASHBOARD
 *  * Total Frequency Impact: +2.66
 *  * Breakdown by Category, Region, Time
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

import { NextPage } from 'next'
import { useState, useEffect, useRef } from 'react'
import Head from 'next/head'
import Link from 'next/link'
import axios from 'axios'
import * as d3 from 'd3'
import styles from '../../styles/FrequencyDashboard.module.css'

const FrequencyDashboardPage: NextPage = () => {
  const [stats, setStats] = useState<any>(null)
  const [loading, setLoading] = useState(true)
  const [events, setEvents] = useState<any[]>([])
  const chartRef = useRef<SVGSVGElement>(null)
  const pieChartRef = useRef<SVGSVGElement>(null)

  useEffect(() => {
    fetchStats()
    fetchEvents()
  }, [])

  useEffect(() => {
    if (stats && chartRef.current) {
      renderTrendChart()
    }
  }, [stats, events])

  useEffect(() => {
    if (stats && pieChartRef.current) {
      renderPieChart()
    }
  }, [stats])

  const fetchStats = async () => {
    try {
      setLoading(true)
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/frequential-events/frequency-impact`)
      setStats(response.data)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching frequency impact:', error)
      setLoading(false)
    }
  }

  const fetchEvents = async () => {
    try {
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/frequential-events/events?limit=1000`)
      setEvents(response.data.events || [])
    } catch (error) {
      console.error('Error fetching events:', error)
    }
  }

  const renderTrendChart = () => {
    if (!chartRef.current || !events.length) return

    const svg = d3.select(chartRef.current)
    svg.selectAll('*').remove()

    const width = chartRef.current.clientWidth || 800
    const height = 300
    const margin = { top: 20, right: 20, bottom: 40, left: 60 }

    svg.attr('width', width).attr('height', height)

    // Group events by decade for trend
    const decadeData: { [key: number]: number } = {}
    events.forEach((event: any) => {
      const decade = Math.floor(event.year_start / 10) * 10
      if (!decadeData[decade]) decadeData[decade] = 0
      decadeData[decade] += event.frequency_impact || 0
    })

    const data = Object.entries(decadeData)
      .map(([decade, impact]) => ({ decade: parseInt(decade), impact: impact as number }))
      .sort((a, b) => a.decade - b.decade)

    const xScale = d3.scaleLinear()
      .domain(d3.extent(data, d => d.decade) as [number, number])
      .range([margin.left, width - margin.right])

    const yScale = d3.scaleLinear()
      .domain([d3.min(data, d => d.impact) || 0, d3.max(data, d => d.impact) || 1])
      .nice()
      .range([height - margin.bottom, margin.top])

    // Draw line
    const line = d3.line<{ decade: number; impact: number }>()
      .x(d => xScale(d.decade))
      .y(d => yScale(d.impact))
      .curve(d3.curveMonotoneX)

    svg.append('path')
      .datum(data)
      .attr('fill', 'none')
      .attr('stroke', '#0066cc')
      .attr('stroke-width', 3)
      .attr('d', line)

    // Draw points
    svg.selectAll('circle')
      .data(data)
      .enter()
      .append('circle')
      .attr('cx', d => xScale(d.decade))
      .attr('cy', d => yScale(d.impact))
      .attr('r', 4)
      .attr('fill', d => d.impact > 0 ? '#00ff00' : '#ff0000')
      .attr('stroke', '#fff')
      .attr('stroke-width', 2)

    // X-axis
    const xAxis = d3.axisBottom(xScale).tickFormat(d => `${d}`)
    svg.append('g')
      .attr('transform', `translate(0, ${height - margin.bottom})`)
      .call(xAxis)
      .append('text')
      .attr('x', width / 2)
      .attr('y', 35)
      .attr('fill', '#666')
      .style('text-anchor', 'middle')
      .text('Decade')

    // Y-axis
    const yAxis = d3.axisLeft(yScale)
    svg.append('g')
      .attr('transform', `translate(${margin.left}, 0)`)
      .call(yAxis)
      .append('text')
      .attr('transform', 'rotate(-90)')
      .attr('y', -40)
      .attr('x', -height / 2)
      .attr('fill', '#666')
      .style('text-anchor', 'middle')
      .text('Frequency Impact')
  }

  const renderPieChart = () => {
    if (!pieChartRef.current || !stats?.impact_by_category) return

    const svg = d3.select(pieChartRef.current)
    svg.selectAll('*').remove()

    const width = pieChartRef.current.clientWidth || 400
    const height = 400
    const radius = Math.min(width, height) / 2 - 40

    const data = Object.entries(stats.impact_by_category)
      .map(([category, impact]: [string, any]) => ({
        category: category.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase()),
        impact: Math.abs(impact),
        value: impact,
        color: impact > 0 ? '#00ff00' : impact < 0 ? '#ff0000' : '#999'
      }))
      .sort((a, b) => b.impact - a.impact)
      .slice(0, 10) // Top 10 categories

    const pie = d3.pie<typeof data[0]>()
      .value(d => d.impact)
      .sort(null)

    const arc = d3.arc<d3.PieArcDatum<typeof data[0]>>()
      .innerRadius(radius * 0.5)
      .outerRadius(radius)

    const g = svg.append('g')
      .attr('transform', `translate(${width / 2}, ${height / 2})`)

    const arcs = g.selectAll('arc')
      .data(pie(data))
      .enter()
      .append('g')

    arcs.append('path')
      .attr('d', arc)
      .attr('fill', d => d.data.color)
      .attr('stroke', '#fff')
      .attr('stroke-width', 2)
      .on('mouseover', function(event, d) {
        d3.select(this).attr('opacity', 0.7)
      })
      .on('mouseout', function() {
        d3.select(this).attr('opacity', 1)
      })

    arcs.append('text')
      .attr('transform', d => `translate(${arc.centroid(d)})`)
      .attr('text-anchor', 'middle')
      .attr('font-size', '10px')
      .attr('fill', '#fff')
      .text(d => d.data.category.substring(0, 10))
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>Frequency Impact Dashboard - Divine Frequency</title>
        <meta name="description" content="Frequency impact dashboard. Total impact: +2.66. Breakdown by category, region, time." />
      </Head>

      <div className={styles.header}>
        <h1>Frequency Impact Dashboard</h1>
        <p className={styles.truth}>
          ALL WARS, DICTATORSHIPS, REVOLUTIONS - IT'S ALL FREQUENTIAL<br />
          EVERYTHING IMPACTS DIVINE FREQUENCY
        </p>
        <Link href="/" className={styles.backLink}>← Back to Home</Link>
      </div>

      {loading ? (
        <div className={styles.loading}>Loading frequency impact data...</div>
      ) : stats && (
        <>
          <div className={styles.totalImpact}>
            <h2>Total Frequency Impact</h2>
            <div className={styles.impactValue} style={{ color: stats.total_frequency_impact > 0 ? '#00ff00' : '#ff0000' }}>
              {stats.total_frequency_impact > 0 ? '+' : ''}{stats.total_frequency_impact.toFixed(2)}
            </div>
            <p className={styles.interpretation}>{stats.interpretation.net_impact}</p>
          </div>

          <div className={styles.chartsSection}>
            <div className={styles.trendChart}>
              <h2>Frequency Impact Trend Over Time</h2>
              <svg ref={chartRef} className={styles.chartSvg}></svg>
            </div>
            <div className={styles.pieChart}>
              <h2>Top Categories by Impact</h2>
              <svg ref={pieChartRef} className={styles.chartSvg}></svg>
            </div>
          </div>

          <div className={styles.breakdown}>
            <h2>Impact by Category - Everything Plays a Part</h2>
            <p className={styles.breakdownIntro}>
              All industries, all events, all movements - everything impacts Divine Frequency. 
              Political events, sporting events, technology, finance, entertainment - it's all frequential.
            </p>
            <div className={styles.categoryGrid}>
              {Object.entries(stats.impact_by_category || {})
                .sort((a, b) => (b[1] as number) - (a[1] as number))
                .map(([category, impact]: [string, any]) => {
                  const isIndustry = ['technology', 'finance', 'agriculture', 'energy', 'transportation', 
                    'communication', 'medicine', 'education', 'entertainment'].includes(category)
                  const isPolitical = ['war', 'dictatorship', 'revolution', 'civil_war', 'resistance', 
                    'liberation', 'legal'].includes(category)
                  const isSporting = category === 'sporting_event'
                  
                  return (
                  <div key={category} className={`${styles.categoryCard} ${isIndustry ? styles.industryCard : ''} ${isPolitical ? styles.politicalCard : ''} ${isSporting ? styles.sportingCard : ''}`}>
                    <div className={styles.categoryHeader}>
                      <h3>{category.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}</h3>
                      {isIndustry && <span className={styles.categoryBadge}>Industry</span>}
                      {isPolitical && <span className={styles.categoryBadge}>Political</span>}
                      {isSporting && <span className={styles.categoryBadge}>Sporting</span>}
                    </div>
                    <div className={styles.categoryImpact} style={{ color: impact > 0 ? '#00ff00' : impact < 0 ? '#ff0000' : '#999' }}>
                      {impact > 0 ? '+' : ''}{impact.toFixed(3)}
                    </div>
                    <div className={styles.categoryBar}>
                      <div 
                        className={styles.categoryBarFill}
                        style={{
                          width: `${Math.min(Math.abs(impact) * 100, 100)}%`,
                          backgroundColor: impact > 0 ? '#00ff00' : impact < 0 ? '#ff0000' : '#999'
                        }}
                      />
                    </div>
                  </div>
                )})}
            </div>
          </div>

          <div className={styles.truthSection}>
            <h2>The Truth</h2>
            <p>{stats.the_truth}</p>
          </div>
        </>
      )}
    </div>
  )
}

export default FrequencyDashboardPage
