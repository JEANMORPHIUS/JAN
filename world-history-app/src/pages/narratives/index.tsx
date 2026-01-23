/**
 * WORLD HISTORY NARRATIVES
 * Narrative Library and Narrative Tree Visualization
 * 
 * Features:
 * - Narrative library (list of all narratives)
 * - Narrative detail pages
 * - Narrative tree visualization (react-d3-tree)
 * - Connections between narratives
 * - Timeline slider (show tree at different time periods)
 */

import { NextPage } from 'next'
import { useState, useEffect } from 'react'
import Head from 'next/head'
import Link from 'next/link'
import axios from 'axios'
import Tree from 'react-d3-tree'
import styles from '../../styles/Narratives.module.css'

interface Narrative {
  narrative_id: string
  title: string
  narrative: string
  narrative_type: string
  field_resonance: number
  timeline_dimension: string
  connections: string[]
  related_sites: string[]
  the_truth: string
}

interface NarrativeConnection {
  narrative_id: string
  connection_type: string
  strength: number
  direction: string
}

const NarrativesPage: NextPage = () => {
  const [narratives, setNarratives] = useState<Narrative[]>([])
  const [selectedNarrative, setSelectedNarrative] = useState<Narrative | null>(null)
  const [connections, setConnections] = useState<NarrativeConnection[]>([])
  const [treeData, setTreeData] = useState<any>(null)
  const [loading, setLoading] = useState(true)
  const [viewMode, setViewMode] = useState<'list' | 'tree'>('list')

  useEffect(() => {
    fetchNarratives()
  }, [])

  useEffect(() => {
    if (selectedNarrative) {
      fetchConnections(selectedNarrative.narrative_id)
      buildTreeData(selectedNarrative.narrative_id)
    }
  }, [selectedNarrative])

  const fetchNarratives = async () => {
    try {
      setLoading(true)
      // Fetch key narratives
      const narrativeIds = ['pangea_formation', 'first_separation', 'mayan_codification']
      const fetchedNarratives: Narrative[] = []
      
      for (const id of narrativeIds) {
        try {
          const response = await axios.get(
            `${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/public/world-history/narrative/${id}`
          )
          fetchedNarratives.push(response.data)
        } catch (error) {
          console.error(`Error fetching narrative ${id}:`, error)
        }
      }
      
      setNarratives(fetchedNarratives)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching narratives:', error)
      setLoading(false)
    }
  }

  const fetchConnections = async (narrativeId: string) => {
    try {
      const response = await axios.get(
        `${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/public/world-history/connections/${narrativeId}`
      )
      setConnections(response.data.connections || [])
    } catch (error) {
      console.error('Error fetching connections:', error)
    }
  }

  const buildTreeData = (rootNarrativeId: string) => {
    // Build tree structure from connections
    const rootNarrative = narratives.find(n => n.narrative_id === rootNarrativeId)
    if (!rootNarrative) return

    const tree = {
      name: rootNarrative.title,
      attributes: {
        id: rootNarrative.narrative_id,
        type: rootNarrative.narrative_type,
        resonance: rootNarrative.field_resonance.toFixed(3)
      },
      children: connections.map(conn => {
        const connectedNarrative = narratives.find(n => n.narrative_id === conn.narrative_id)
        if (!connectedNarrative) return null
        
        return {
          name: connectedNarrative.title,
          attributes: {
            id: connectedNarrative.narrative_id,
            type: connectedNarrative.narrative_type,
            resonance: connectedNarrative.field_resonance.toFixed(3),
            connection_type: conn.connection_type,
            strength: conn.strength.toFixed(2)
          }
        }
      }).filter(Boolean)
    }

    setTreeData(tree)
  }

  const getNarrativeTypeColor = (type: string): string => {
    switch (type) {
      case 'original': return '#00ff00' // Green - original truth
      case 'error': return '#ff0000' // Red - error
      case 'restoration': return '#0066cc' // Blue - restoration
      default: return '#666'
    }
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>World History Narratives - The History of The World</title>
        <meta name="description" content="The stories. The truth. The restoration. The Table." />
      </Head>

      <div className={styles.header}>
        <h1>World History Narratives</h1>
        <p className={styles.truth}>The stories. The truth. The restoration. The Table.</p>
        
        <div className={styles.viewToggle}>
          <button
            className={viewMode === 'list' ? styles.active : ''}
            onClick={() => setViewMode('list')}
          >
            List View
          </button>
          <button
            className={viewMode === 'tree' ? styles.active : ''}
            onClick={() => setViewMode('tree')}
          >
            Tree View
          </button>
        </div>
      </div>

      {loading ? (
        <div className={styles.loading}>Loading narratives...</div>
      ) : viewMode === 'list' ? (
        <div className={styles.narrativeList}>
          {narratives.map(narrative => (
            <div
              key={narrative.narrative_id}
              className={styles.narrativeCard}
              onClick={() => setSelectedNarrative(narrative)}
            >
              <div className={styles.narrativeHeader}>
                <h2>{narrative.title}</h2>
                <span
                  className={styles.narrativeType}
                  style={{ backgroundColor: getNarrativeTypeColor(narrative.narrative_type) }}
                >
                  {narrative.narrative_type}
                </span>
              </div>
              <p className={styles.narrativePreview}>
                {narrative.narrative.substring(0, 200)}...
              </p>
              <div className={styles.narrativeMeta}>
                <span>Field Resonance: {narrative.field_resonance.toFixed(3)}</span>
                <span>Connections: {narrative.connections.length}</span>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className={styles.treeContainer}>
          {selectedNarrative && treeData ? (
            <div className={styles.treeWrapper}>
              <div className={styles.treeHeader}>
                <h2>Narrative Tree: {selectedNarrative.title}</h2>
                <button onClick={() => setSelectedNarrative(null)}>Back to List</button>
              </div>
              <div className={styles.treeVisualization}>
                <Tree
                  data={treeData}
                  orientation="vertical"
                  pathClassFunc={() => styles.treePath}
                  nodeSize={{ x: 200, y: 100 }}
                  translate={{ x: 400, y: 50 }}
                />
              </div>
            </div>
          ) : (
            <div className={styles.treePlaceholder}>
              <p>Select a narrative from the list to view its connection tree</p>
              <button onClick={() => setViewMode('list')}>Go to List View</button>
            </div>
          )}
        </div>
      )}

      {selectedNarrative && viewMode === 'list' && (
        <div className={styles.narrativeDetail}>
          <button onClick={() => setSelectedNarrative(null)} className={styles.closeButton}>×</button>
          <h2>{selectedNarrative.title}</h2>
          <div className={styles.narrativeMeta}>
            <span>Type: {selectedNarrative.narrative_type}</span>
            <span>Field Resonance: {selectedNarrative.field_resonance.toFixed(3)}</span>
            <span>Timeline: {selectedNarrative.timeline_dimension}</span>
          </div>
          <div className={styles.narrativeContent}>
            <p>{selectedNarrative.narrative}</p>
          </div>
          {connections.length > 0 && (
            <div className={styles.connections}>
              <h3>Connections</h3>
              {connections.map((conn, idx) => (
                <div key={idx} className={styles.connection}>
                  <span>{conn.narrative_id}</span>
                  <span>{conn.connection_type}</span>
                  <span>Strength: {conn.strength.toFixed(2)}</span>
                </div>
              ))}
            </div>
          )}
          <div className={styles.truthBox}>
            <p>{selectedNarrative.the_truth}</p>
          </div>
        </div>
      )}
    </div>
  )
}

export default NarrativesPage
