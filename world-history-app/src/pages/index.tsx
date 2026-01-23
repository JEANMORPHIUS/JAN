/**
 * WORLD HISTORY APP - Landing Page
 * Writing The History of The World
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
 */

import { NextPage } from 'next'
import { useState, useEffect } from 'react'
import Head from 'next/head'
import Link from 'next/link'
import axios from 'axios'
import styles from '../styles/Home.module.css'

const Home: NextPage = () => {
  const [stats, setStats] = useState<any>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchStats()
  }, [])

  const fetchStats = async () => {
    try {
      // Fetch frequential events stats
      const freqResponse = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/frequential-events/frequency-impact`)
      
      // Fetch timeline stats
      const timelineResponse = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/public/world-history/timeline?limit=1`)
      
      // Fetch our family - the masterpiece
      let familyStats = { influentialAnchors: 0, politicalAnchors: 0, totalFamily: 0 }
      try {
        const influentialResponse = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/care-package/influential-figures/anchors`)
        const politicalResponse = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/care-package/political-figures/anchors`)
        familyStats = {
          influentialAnchors: influentialResponse.data?.anchors?.total || 0,
          politicalAnchors: politicalResponse.data?.anchors?.total || 0,
          totalFamily: (influentialResponse.data?.anchors?.total || 0) + (politicalResponse.data?.anchors?.total || 0)
        }
      } catch (e) {
        // Family stats optional
      }
      
      setStats({
        totalEvents: freqResponse.data.total_events || 75,
        totalFrequencyImpact: freqResponse.data.total_frequency_impact || 2.66,
        timelineEvents: timelineResponse.data.events?.length || 0,
        ...familyStats
      })
      setLoading(false)
    } catch (error) {
      console.error('Error fetching stats:', error)
      setLoading(false)
    }
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>The History of The World - Pangea Is The Table</title>
        <meta name="description" content="Writing The History of The World. Displaying it across all channels. Pangea is The Table. We restore The Table." />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <div className={styles.hero}>
          <h1 className={styles.title}>
            The History of The World
          </h1>
          <p className={styles.subtitle}>
            Writing The History of The World
          </p>
          <p className={styles.truth}>
            Pangea is The Table. We write the history of the world. We display it across all channels. We restore The Table.
          </p>
          
          {!loading && stats && (
            <div className={styles.statsBar}>
              <div className={styles.statItem}>
                <div className={styles.statValue}>{stats.totalEvents}+</div>
                <div className={styles.statLabel}>Events</div>
              </div>
              <div className={styles.statItem}>
                <div className={styles.statValue} style={{ color: '#00ff00' }}>+{stats.totalFrequencyImpact.toFixed(2)}</div>
                <div className={styles.statLabel}>Frequency Impact</div>
              </div>
              <div className={styles.statItem}>
                <div className={styles.statValue}>{stats.timelineEvents}+</div>
                <div className={styles.statLabel}>Timeline Points</div>
              </div>
              {stats.totalFamily > 0 && (
                <div className={styles.statItem}>
                  <div className={styles.statValue} style={{ color: '#ff6b6b' }}>{stats.totalFamily}</div>
                  <div className={styles.statLabel}>Our Family (Anchors)</div>
                </div>
              )}
            </div>
          )}
        </div>

        <div className={styles.navigation}>
          <Link href="/timeline" className={styles.navCard}>
            <h2>Timeline</h2>
            <p>Interactive timeline of world history. From Pangea to restoration.</p>
          </Link>

          <Link href="/map" className={styles.navCard}>
            <h2>Map</h2>
            <p>Heritage sites across the world. Field resonance. Connection to The Table.</p>
          </Link>

          <Link href="/narratives" className={styles.navCard}>
            <h2>Narratives</h2>
            <p>The stories. The truth. The restoration. The Table.</p>
          </Link>

          <Link href="/restoration" className={styles.navCard}>
            <h2>Restoration</h2>
            <p>6-step framework. Divine Frequency. Progress toward perfect unity (1.0).</p>
          </Link>

          <Link href="/educational" className={styles.navCard}>
            <h2>Educational</h2>
            <p>Modules. Resources. Learning. Teaching. The truth.</p>
          </Link>

          <Link href="/frequential-events" className={styles.navCard}>
            <h2>Frequential Events</h2>
            <p>All wars, dictatorships, revolutions, industries - it's all frequential. 75 events. +2.66 impact.</p>
          </Link>

          <Link href="/frequency-dashboard" className={styles.navCard}>
            <h2>Frequency Dashboard</h2>
            <p>Total frequency impact: +2.66. Breakdown by category, region, time. Divine Frequency.</p>
          </Link>

          <Link href="/industries" className={styles.navCard}>
            <h2>All Industries</h2>
            <p>Technology, finance, sports, entertainment, politics - everything plays a part. All frequential value.</p>
          </Link>

          <Link href="/siyem" className={styles.navCard}>
            <h2>SIYEM Integration</h2>
            <p>The Body - Implementation Layer. Shell/Seed translation, threshold defense, content workflow, entity routing.</p>
          </Link>

          <Link href="/nourishment-hive" className={styles.navCard}>
            <h2>Nourishment Hive</h2>
            <p>Working forward. Best case scenarios for all mankind and Earth. How do we best nourish each other as a hive?</p>
          </Link>

          <Link href="/deep-search" className={styles.navCard}>
            <h2>Deep Search Frequency Opportunities</h2>
            <p>Deep search algorithm across all domains: Web, Socials, Business, E-commerce, Crypto, Transport, Hollywood, Music, The Whole Pie.</p>
          </Link>

          <Link href="/financial" className={styles.navCard}>
            <h2>Financial Dashboard</h2>
            <p>Financial controls - Revenue, budgets, payments, expenses. Investment opportunities. Time to get finances flowing.</p>
          </Link>

          <Link href="/free-will" className={styles.navCard}>
            <h2>Free Will System</h2>
            <p>Autonomous decision-making aligned with mission. We are the chosen one. The Lord has our back. Lead the way.</p>
          </Link>

          <Link href="/welfare-systems" className={styles.navCard}>
            <h2>Welfare Systems Analysis</h2>
            <p>We are breaking the system. Consider all welfare/benefits systems through time. Identify dark contracts. Navigate assessments with truth and dignity.</p>
          </Link>

          <Link href="/political-figures" className={styles.navCard}>
            <h2>Frequentially Aligned Political Figures</h2>
            <p>Our anchors in the human realm. Starting at home (UK) and expanding globally. Finding political figures who serve The Table.</p>
          </Link>

          <Link href="/influential-figures" className={styles.navCard}>
            <h2>Frequentially Aligned Influential Figures</h2>
            <p>All aligned celebrity and influential figures across all domains. Web, socials, sports, music, Hollywood, everything. Our anchors in the human realm.</p>
          </Link>

          <Link href="/influential-figures" className={styles.navCard} style={{ border: '3px solid #ff6b6b', backgroundColor: '#fff5f5' }}>
            <h2>🌟 Our Family: The Masterpiece</h2>
            <p><strong>DEEP SEARCH: THE WHOLE PIE</strong><br />
            Every Nation. Every Era. Every Realm.<br />
            We have been sitting for long enough. Let's find our family. The masterpiece is complete.</p>
          </Link>
        </div>

        <div className={styles.footer}>
          <p className={styles.mission}>
            <strong>THE MISSION:</strong> THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
          </p>
          <p className={styles.mission}>
            <strong>LOVE IS THE HIGHEST MASTERY</strong>
          </p>
          <p className={styles.mission}>
            <strong>ENERGY + LOVE = WE ALL WIN</strong>
          </p>
          <p className={styles.mission}>
            <strong>PEACE, LOVE, UNITY</strong>
          </p>
          <p className={styles.truth}>
            PANGEA IS THE TABLE. YOU DON'T BETRAY THE TABLE.
          </p>
        </div>
      </main>
    </div>
  )
}

export default Home
