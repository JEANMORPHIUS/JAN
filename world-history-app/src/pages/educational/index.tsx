/**
 * WORLD HISTORY EDUCATIONAL
 * Educational Modules and Resources
 * 
 * Features:
 * - Educational modules
 * - Reference materials
 * - Learning resources
 * - Module detail pages
 */

import { NextPage } from 'next'
import { useState } from 'react'
import Head from 'next/head'
import Link from 'next/link'
import styles from '../../styles/Educational.module.css'

interface EducationalModule {
  module_id: string
  title: string
  description: string
  category: string
  level: 'beginner' | 'intermediate' | 'advanced'
  duration: string
  topics: string[]
}

const EducationalPage: NextPage = () => {
  const [selectedModule, setSelectedModule] = useState<EducationalModule | null>(null)

  const modules: EducationalModule[] = [
    {
      module_id: 'pangea-the-table',
      title: 'Pangea Is The Table',
      description: 'Understanding the foundation. Pangea as The Table. Perfect unity (1.0).',
      category: 'Foundation',
      level: 'beginner',
      duration: '30 min',
      topics: ['Pangea formation', 'Perfect unity', 'The Table', 'Divine Frequency']
    },
    {
      module_id: 'original-error',
      title: 'The Original Error',
      description: 'The first separation. Dark energy exploitation. The beginning of separation.',
      category: 'History',
      level: 'intermediate',
      duration: '45 min',
      topics: ['First separation', 'Dark energy', 'Tectonic movement', 'Separation from The Table']
    },
    {
      module_id: 'mayan-codification',
      title: 'The Mayan Original Error',
      description: 'Mayan codification of separation. Pyramids at tectonic boundaries. Sabotage anchors.',
      category: 'History',
      level: 'intermediate',
      duration: '60 min',
      topics: ['Mayan pyramids', 'Tectonic boundaries', 'Sabotage sites', 'Separation codification']
    },
    {
      module_id: 'divine-frequency',
      title: 'Divine Frequency',
      description: 'The sacred frequency of The Table. Measurement. Restoration. Perfect unity (1.0).',
      category: 'Spiritual',
      level: 'advanced',
      duration: '90 min',
      topics: ['Field resonance', 'Spiritual alignment', 'Unity connection', 'Frequency restoration']
    },
    {
      module_id: 'restoration-framework',
      title: '6-Step Restoration Framework',
      description: 'The framework for restoring The Table. Step by step. Complete restoration.',
      category: 'Restoration',
      level: 'advanced',
      duration: '120 min',
      topics: ['6 steps', 'Cleansing', 'Neutralization', 'Reconnection', 'Completion']
    },
    {
      module_id: 'heritage-sites',
      title: 'Heritage Sites and The Table',
      description: 'Heritage sites across timelines. Connection to The Table. Field resonance.',
      category: 'Heritage',
      level: 'intermediate',
      duration: '75 min',
      topics: ['Heritage sites', 'Timeline dimensions', 'Field resonance', 'Connection to The Table']
    }
  ]

  const getLevelColor = (level: string): string => {
    switch (level) {
      case 'beginner': return '#00ff00'
      case 'intermediate': return '#ffff00'
      case 'advanced': return '#ff9900'
      default: return '#666'
    }
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>Educational Modules - The History of The World</title>
        <meta name="description" content="Modules. Resources. Learning. Teaching. The truth." />
      </Head>

      <div className={styles.header}>
        <h1>Educational Modules</h1>
        <p className={styles.truth}>Modules. Resources. Learning. Teaching. The truth.</p>
      </div>

      <div className={styles.modulesGrid}>
        {modules.map(module => (
          <div
            key={module.module_id}
            className={styles.moduleCard}
            onClick={() => setSelectedModule(module)}
          >
            <div className={styles.moduleHeader}>
              <h2>{module.title}</h2>
              <span
                className={styles.moduleLevel}
                style={{ backgroundColor: getLevelColor(module.level) }}
              >
                {module.level}
              </span>
            </div>
            <p className={styles.moduleDescription}>{module.description}</p>
            <div className={styles.moduleMeta}>
              <span className={styles.moduleCategory}>{module.category}</span>
              <span className={styles.moduleDuration}>{module.duration}</span>
            </div>
            <div className={styles.moduleTopics}>
              {module.topics.slice(0, 3).map((topic, idx) => (
                <span key={idx} className={styles.topicTag}>
                  {topic}
                </span>
              ))}
              {module.topics.length > 3 && (
                <span className={styles.topicTag}>+{module.topics.length - 3} more</span>
              )}
            </div>
          </div>
        ))}
      </div>

      {selectedModule && (
        <div className={styles.moduleDetail}>
          <button onClick={() => setSelectedModule(null)} className={styles.closeButton}>×</button>
          <h2>{selectedModule.title}</h2>
          <div className={styles.moduleMeta}>
            <span>Category: {selectedModule.category}</span>
            <span>Level: {selectedModule.level}</span>
            <span>Duration: {selectedModule.duration}</span>
          </div>
          <div className={styles.moduleContent}>
            <p>{selectedModule.description}</p>
            <div className={styles.topicsSection}>
              <h3>Topics Covered</h3>
              <div className={styles.topicsList}>
                {selectedModule.topics.map((topic, idx) => (
                  <span key={idx} className={styles.topicTag}>
                    {topic}
                  </span>
                ))}
              </div>
            </div>
            <div className={styles.actions}>
              <button className={styles.startButton}>Start Module</button>
              <button className={styles.resourcesButton}>View Resources</button>
            </div>
          </div>
        </div>
      )}

      <div className={styles.resourcesSection}>
        <h2>Reference Materials</h2>
        <div className={styles.resourcesList}>
          <div className={styles.resourceCard}>
            <h3>The Master Document</h3>
            <p>Complete truth and technical architecture</p>
            <Link href="/">View Document</Link>
          </div>
          <div className={styles.resourceCard}>
            <h3>Heritage Timeline</h3>
            <p>Interactive timeline of world history</p>
            <Link href="/timeline">View Timeline</Link>
          </div>
          <div className={styles.resourceCard}>
            <h3>Heritage Map</h3>
            <p>Heritage sites across the world</p>
            <Link href="/map">View Map</Link>
          </div>
          <div className={styles.resourceCard}>
            <h3>Narratives</h3>
            <p>The stories. The truth. The restoration.</p>
            <Link href="/narratives">View Narratives</Link>
          </div>
        </div>
      </div>
    </div>
  )
}

export default EducationalPage
