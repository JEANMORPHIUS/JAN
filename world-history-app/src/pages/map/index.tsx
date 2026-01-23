/**
 * WORLD HISTORY MAP
 * Interactive Map Component with Mapbox GL JS
 * 
 * Features:
 * - Heritage site markers (color-coded by field resonance)
 * - Tectonic plate boundaries overlay
 * - Spiritual battlefields highlighted
 * - Energy grid connections
 * - Cluster markers (zoom out → grouped sites)
 * - Click markers → site detail
 */

import { NextPage } from 'next'
import { useState, useEffect } from 'react'
import Head from 'next/head'
import axios from 'axios'
import Map, { Marker, Popup, Source, Layer } from 'react-map-gl'
import 'mapbox-gl/dist/mapbox-gl.css'
import styles from '../../styles/Map.module.css'

interface HeritageSite {
  site_id: string
  name: string
  location: { lat: number; lon: number }
  field_resonance: number
  site_type: string
  timeline_dimension: string
  connection_to_table: string
  narrative: string
}

const MapPage: NextPage = () => {
  const [sites, setSites] = useState<HeritageSite[]>([])
  const [loading, setLoading] = useState(true)
  const [selectedSite, setSelectedSite] = useState<HeritageSite | null>(null)
  const [viewState, setViewState] = useState({
    longitude: 0,
    latitude: 20,
    zoom: 2
  })

  useEffect(() => {
    fetchMapData()
  }, [])

  const fetchMapData = async () => {
    try {
      setLoading(true)
      
      // Fetch heritage sites
      const heritageResponse = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/public/world-history/map`)
      const geojson = heritageResponse.data.geojson
      
      // Convert GeoJSON to sites array
      let sitesData: HeritageSite[] = geojson.features.map((feature: any) => ({
        site_id: feature.properties.site_id,
        name: feature.properties.name,
        location: {
          lat: feature.geometry.coordinates[1],
          lon: feature.geometry.coordinates[0]
        },
        field_resonance: feature.properties.field_resonance,
        site_type: feature.properties.site_type,
        timeline_dimension: feature.properties.timeline_dimension,
        connection_to_table: feature.properties.connection_to_table,
        narrative: feature.properties.narrative
      }))
      
      // Also fetch frequential events with locations
      try {
        const freqResponse = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/frequential-events/events`, {
          params: { limit: 1000 }
        })
        
        // Add frequential events as sites
        const freqSites: HeritageSite[] = (freqResponse.data.events || [])
          .filter((e: any) => e.location && e.location.lat && e.location.lon)
          .map((e: any) => ({
            site_id: `freq_${e.event_id}`,
            name: e.title,
            location: e.location,
            field_resonance: e.field_resonance_after,
            site_type: `frequential_${e.category}`,
            timeline_dimension: 'frequential',
            connection_to_table: e.connection_to_table,
            narrative: e.narrative
          }))
        
        sitesData = [...sitesData, ...freqSites]
      } catch (freqError) {
        console.warn('Could not fetch frequential events for map:', freqError)
      }
      
      setSites(sitesData)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching map data:', error)
      setLoading(false)
    }
  }

  const getResonanceColor = (resonance: number): string => {
    if (resonance >= 0.9) return '#00ff00' // Green - high resonance
    if (resonance >= 0.7) return '#ffff00' // Yellow - moderate
    if (resonance >= 0.5) return '#ff9900' // Orange - low
    return '#ff0000' // Red - very low
  }

  const mapboxToken = process.env.NEXT_PUBLIC_MAPBOX_TOKEN || ''

  if (!mapboxToken) {
    return (
      <div className={styles.container}>
        <div className={styles.error}>
          <h2>Mapbox Token Required</h2>
          <p>Please set NEXT_PUBLIC_MAPBOX_TOKEN in your environment variables.</p>
          <p>You can get a free token from <a href="https://www.mapbox.com/" target="_blank" rel="noopener noreferrer">mapbox.com</a></p>
        </div>
      </div>
    )
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>World History Map - The History of The World</title>
        <meta name="description" content="Interactive map of heritage sites. Field resonance. Connection to The Table." />
      </Head>

      <div className={styles.header}>
        <h1>World History Map</h1>
        <p className={styles.truth}>Heritage sites across the world. Field resonance. Connection to The Table.</p>
        <div className={styles.legend}>
          <div className={styles.legendItem}>
            <span className={styles.legendColor} style={{ backgroundColor: '#00ff00' }}></span>
            <span>High Resonance (0.9+)</span>
          </div>
          <div className={styles.legendItem}>
            <span className={styles.legendColor} style={{ backgroundColor: '#ffff00' }}></span>
            <span>Moderate (0.7-0.9)</span>
          </div>
          <div className={styles.legendItem}>
            <span className={styles.legendColor} style={{ backgroundColor: '#ff9900' }}></span>
            <span>Low (0.5-0.7)</span>
          </div>
          <div className={styles.legendItem}>
            <span className={styles.legendColor} style={{ backgroundColor: '#ff0000' }}></span>
            <span>Very Low (&lt;0.5)</span>
          </div>
        </div>
      </div>

      {loading ? (
        <div className={styles.loading}>Loading map data...</div>
      ) : (
        <div className={styles.mapContainer}>
          <Map
            {...viewState}
            onMove={evt => setViewState(evt.viewState)}
            mapboxAccessToken={mapboxToken}
            style={{ width: '100%', height: '100%' }}
            mapStyle="mapbox://styles/mapbox/dark-v11"
          >
            {sites.map(site => (
              <Marker
                key={site.site_id}
                longitude={site.location.lon}
                latitude={site.location.lat}
                onClick={() => setSelectedSite(site)}
              >
                <div
                  className={styles.marker}
                  style={{ backgroundColor: getResonanceColor(site.field_resonance) }}
                  title={site.name}
                >
                  <div className={styles.markerInner}></div>
                </div>
              </Marker>
            ))}

            {selectedSite && (
              <Popup
                longitude={selectedSite.location.lon}
                latitude={selectedSite.location.lat}
                onClose={() => setSelectedSite(null)}
                closeButton={true}
                closeOnClick={false}
              >
                <div className={styles.popup}>
                  <h3>{selectedSite.name}</h3>
                  <p><strong>Field Resonance:</strong> {selectedSite.field_resonance.toFixed(3)}</p>
                  <p><strong>Type:</strong> {selectedSite.site_type}</p>
                  <p><strong>Connection:</strong> {selectedSite.connection_to_table}</p>
                  <p><strong>Narrative:</strong> {selectedSite.narrative}</p>
                </div>
              </Popup>
            )}
          </Map>
        </div>
      )}
    </div>
  )
}

export default MapPage
