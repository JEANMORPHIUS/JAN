/** * * ADMIN DASHBOARD - Landing Page
 *  * Heritage Curation, Timeline Management, Analytics
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
import { useSession } from 'next-auth/react'
import Head from 'next/head'
import Link from 'next/link'
import { useRouter } from 'next/router'
import styles from '../styles/Admin.module.css'

const AdminDashboard: NextPage = () => {
  const { data: session, status } = useSession()
  const router = useRouter()

  if (status === 'loading') {
    return <div className={styles.loading}>Loading...</div>
  }

  if (status === 'unauthenticated') {
    router.push('/login')
    return null
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>Admin Dashboard - World History Curation</title>
        <meta name="description" content="Admin dashboard for heritage curation, timeline management, and analytics" />
      </Head>

      <div className={styles.header}>
        <h1>Admin Dashboard</h1>
        <p className={styles.subtitle}>Heritage Curation • Timeline Management • Analytics</p>
        <div className={styles.userInfo}>
          <span>Logged in as: {session?.user?.email}</span>
        </div>
      </div>

      <div className={styles.navigation}>
        <Link href="/admin/heritage/sites" className={styles.navCard}>
          <h2>Heritage Sites</h2>
          <p>CRUD heritage sites. Manage site data. Edit narratives.</p>
        </Link>

        <Link href="/admin/heritage/narratives" className={styles.navCard}>
          <h2>Narratives</h2>
          <p>Edit narratives. Review content. Manage narrative connections.</p>
        </Link>

        <Link href="/admin/heritage/patterns" className={styles.navCard}>
          <h2>Dark Energy Patterns</h2>
          <p>Detect dark energy patterns. Analyze temporal patterns.</p>
        </Link>

        <Link href="/admin/timeline/events" className={styles.navCard}>
          <h2>Timeline Events</h2>
          <p>Add/edit timeline events. Manage chronology.</p>
        </Link>

        <Link href="/admin/timeline/dimensions" className={styles.navCard}>
          <h2>Timeline Dimensions</h2>
          <p>Manage timeline dimensions. Configure temporal layers.</p>
        </Link>

        <Link href="/admin/curation/queue" className={styles.navCard}>
          <h2>Content Queue</h2>
          <p>Content approval queue. Review pending submissions.</p>
        </Link>

        <Link href="/admin/curation/review" className={styles.navCard}>
          <h2>Narrative Review</h2>
          <p>Review narratives. Approve/reject content.</p>
        </Link>

        <Link href="/admin/curation/moderation" className={styles.navCard}>
          <h2>Content Moderation</h2>
          <p>Moderate content. Flag issues. Manage reports.</p>
        </Link>

        <Link href="/admin/analytics/frequency" className={styles.navCard}>
          <h2>Divine Frequency</h2>
          <p>Monitor Divine Frequency. Track restoration progress.</p>
        </Link>

        <Link href="/admin/analytics/resonance" className={styles.navCard}>
          <h2>Field Resonance</h2>
          <p>Field resonance analytics. Site resonance tracking.</p>
        </Link>

        <Link href="/admin/analytics/engagement" className={styles.navCard}>
          <h2>User Engagement</h2>
          <p>User engagement metrics. Content performance.</p>
        </Link>

        <Link href="/admin/distribution/channels" className={styles.navCard}>
          <h2>Channel Management</h2>
          <p>Manage distribution channels. Configure sync settings.</p>
        </Link>

        <Link href="/admin/distribution/exports" className={styles.navCard}>
          <h2>Export Management</h2>
          <p>Manage exports. Schedule exports. Download data.</p>
        </Link>

        <Link href="/admin/distribution/sync" className={styles.navCard}>
          <h2>Multi-Channel Sync</h2>
          <p>Sync status. Multi-channel synchronization.</p>
        </Link>
      </div>
    </div>
  )
}

export default AdminDashboard
