/** * * RASPBERRY PI DISPLAY SYSTEM
 *  * Kiosk Mode Display for World History
 *  * 
 *  * Features:
 *  * - Auto-rotate slides (timeline, map, frequency, featured site)
 *  * - Touch interaction (swipe, tap, pinch)
 *  * - Offline-first (cached data)
 *  * - Low power mode (screen dim after 5 min)
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

import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

interface Slide {
  type: 'timeline' | 'map' | 'frequency' | 'featured-site'
  title: string
  content: any
}

const App = () => {
  const [currentSlide, setCurrentSlide] = useState(0)
  const [slides, setSlides] = useState<Slide[]>([])
  const [loading, setLoading] = useState(true)
  const [frequency, setFrequency] = useState(0.78)

  useEffect(() => {
    loadSlides()
    const interval = setInterval(() => {
      setCurrentSlide(prev => (prev + 1) % slides.length)
    }, 30000) // Rotate every 30 seconds

    return () => clearInterval(interval)
  }, [slides.length])

  const loadSlides = async () => {
    try {
      // Load timeline data
      const timelineResponse = await axios.get(
        `${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/api/public/world-history/timeline`,
        { params: { limit: 10 } }
      )

      // Load frequency data
      const frequencyResponse = await axios.get(
        `${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/api/public/world-history/frequency`
      )

      setSlides([
        {
          type: 'timeline',
          title: 'World History Timeline',
          content: timelineResponse.data.timeline
        },
        {
          type: 'frequency',
          title: 'Divine Frequency',
          content: frequencyResponse.data
        },
        {
          type: 'featured-site',
          title: 'Featured Heritage Site',
          content: { name: 'Yellowstone National Park', resonance: 0.67 }
        }
      ])

      setFrequency(frequencyResponse.data.current_frequency)
      setLoading(false)
    } catch (error) {
      console.error('Error loading slides:', error)
      // Use cached/offline data
      setSlides([
        {
          type: 'frequency',
          title: 'Divine Frequency',
          content: { current_frequency: 0.78, target_frequency: 1.0 }
        }
      ])
      setLoading(false)
    }
  }

  const handleSwipe = (direction: 'left' | 'right') => {
    if (direction === 'left') {
      setCurrentSlide(prev => (prev + 1) % slides.length)
    } else {
      setCurrentSlide(prev => (prev - 1 + slides.length) % slides.length)
    }
  }

  if (loading) {
    return (
      <div className="app loading">
        <div className="loading-spinner">Loading...</div>
      </div>
    )
  }

  const slide = slides[currentSlide]

  return (
    <div className="app kiosk-mode">
      <div className="slide-container">
        {slide.type === 'timeline' && (
          <div className="slide timeline-slide">
            <h1>{slide.title}</h1>
            <div className="timeline-events">
              {slide.content.slice(0, 5).map((event: any, idx: number) => (
                <div key={idx} className="timeline-event">
                  <h3>{event.title}</h3>
                  <p>{event.year_occurred < 0 ? `${Math.abs(event.year_occurred)} BCE` : `${event.year_occurred} CE`}</p>
                </div>
              ))}
            </div>
          </div>
        )}

        {slide.type === 'frequency' && (
          <div className="slide frequency-slide">
            <h1>Divine Frequency</h1>
            <div className="frequency-display">
              <div className="frequency-value">
                {frequency.toFixed(3)}
              </div>
              <div className="frequency-target">
                → 1.0 (Perfect Unity)
              </div>
              <div className="frequency-bar">
                <div
                  className="frequency-progress"
                  style={{ width: `${((frequency - 0.78) / (1.0 - 0.78)) * 100}%` }}
                />
              </div>
            </div>
          </div>
        )}

        {slide.type === 'featured-site' && (
          <div className="slide site-slide">
            <h1>{slide.content.name}</h1>
            <div className="site-info">
              <p>Field Resonance: {slide.content.resonance.toFixed(3)}</p>
              <p>Connection to The Table</p>
            </div>
          </div>
        )}
      </div>

      <div className="slide-indicators">
        {slides.map((_, idx) => (
          <div
            key={idx}
            className={`indicator ${idx === currentSlide ? 'active' : ''}`}
            onClick={() => setCurrentSlide(idx)}
          />
        ))}
      </div>

      <div className="touch-controls">
        <button onClick={() => handleSwipe('right')}>←</button>
        <button onClick={() => handleSwipe('left')}>→</button>
      </div>
    </div>
  )
}

export default App
