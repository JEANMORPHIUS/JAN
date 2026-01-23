/**
 * LOCATION SETTINGS COMPONENT
 *
 * Purpose: Allow users to set their geographic location for accurate Earth alignment
 * Foundation: "Man and Earth live symbiotically" - requires user's actual location
 *
 * Provides:
 * - Preset locations (London, North Cyprus, Cyprus, Istanbul)
 * - Current sunrise/sunset times
 * - Today's solar window recommendation
 * - Seasonal context
 */

import { useState, useEffect } from 'react';
import {
  LocationConfig,
  PRESET_LOCATIONS,
  loadLocation,
  saveLocation
} from '../config/location';
import {
  formatSunriseTime,
  formatSunsetTime,
  formatSolarWindow,
  getSeasonalContext
} from '../utils/astronomicalCalculations';
import './LocationSettings.css';

export function LocationSettings() {
  const [location, setLocation] = useState<LocationConfig>(loadLocation());
  const [showSettings, setShowSettings] = useState(false);
  const [sunriseTime, setSunriseTime] = useState<string>('');
  const [sunsetTime, setSunsetTime] = useState<string>('');
  const [solarWindow, setSolarWindow] = useState<string>('');
  const [seasonalContext, setSeasonalContext] = useState<string>('');

  useEffect(() => {
    // Calculate and display today's solar data
    const today = new Date();
    setSunriseTime(formatSunriseTime(today, location));
    setSunsetTime(formatSunsetTime(today, location));
    setSolarWindow(formatSolarWindow(today, location));
    setSeasonalContext(getSeasonalContext(today, location));
  }, [location]);

  const handleLocationChange = (newLocation: LocationConfig) => {
    setLocation(newLocation);
    saveLocation(newLocation);
  };

  return (
    <div className="location-settings">
      <button
        className="location-toggle"
        onClick={() => setShowSettings(!showSettings)}
        title="Configure location for accurate sunrise/sunset times"
      >
        📍 {location.name}
      </button>

      {showSettings && (
        <div className="location-modal">
          <div className="location-modal-content">
            <div className="location-header">
              <h2>Location Settings</h2>
              <button
                className="location-close"
                onClick={() => setShowSettings(false)}
              >
                ✕
              </button>
            </div>

            <div className="location-body">
              <p className="location-description">
                <strong>Why location matters:</strong> "Man and Earth live symbiotically."
                For accurate Loop timing aligned with Earth's movements, we need your actual
                location to calculate real sunrise/sunset times (not hardcoded guesses).
              </p>

              <div className="location-select-group">
                <label htmlFor="location-select">Choose your location:</label>
                <select
                  id="location-select"
                  value={location.name}
                  onChange={(e) => {
                    const newLocation = Object.values(PRESET_LOCATIONS)
                      .find(loc => loc.name === e.target.value);
                    if (newLocation) {
                      handleLocationChange(newLocation);
                    }
                  }}
                >
                  {Object.values(PRESET_LOCATIONS).map(loc => (
                    <option key={loc.name} value={loc.name}>
                      {loc.name}
                    </option>
                  ))}
                </select>
              </div>

              {location.description && (
                <div className="location-community">
                  <p><strong>Community:</strong> {location.description}</p>
                </div>
              )}

              <div className="location-details">
                <h3>Geographic Coordinates</h3>
                <div className="location-coords">
                  <div className="coord-item">
                    <span className="coord-label">Latitude:</span>
                    <span className="coord-value">{location.latitude}°</span>
                  </div>
                  <div className="coord-item">
                    <span className="coord-label">Longitude:</span>
                    <span className="coord-value">{location.longitude}°</span>
                  </div>
                  <div className="coord-item">
                    <span className="coord-label">Timezone:</span>
                    <span className="coord-value">{location.timezone}</span>
                  </div>
                </div>
              </div>

              <div className="location-solar-data">
                <h3>Today's Solar Data ({new Date().toLocaleDateString()})</h3>
                <div className="solar-data-grid">
                  <div className="solar-data-item">
                    <span className="solar-label">Sunrise:</span>
                    <span className="solar-value">{sunriseTime}</span>
                  </div>
                  <div className="solar-data-item">
                    <span className="solar-label">Sunset:</span>
                    <span className="solar-value">{sunsetTime}</span>
                  </div>
                  <div className="solar-data-item solar-window-highlight">
                    <span className="solar-label">Optimal Loop Window:</span>
                    <span className="solar-value">{solarWindow}</span>
                  </div>
                </div>

                <div className="seasonal-context">
                  <p><strong>Seasonal Context:</strong> {seasonalContext}</p>
                </div>
              </div>

              <div className="location-narrative">
                <h3>Symbiotic Alignment</h3>
                <p>
                  By setting your location, the system can calculate actual sunrise/sunset
                  times that change with seasons. Winter days in London are short (sunrise ~08:00,
                  sunset ~16:00), while summer days are long (sunrise ~05:00, sunset ~21:00).
                </p>
                <p>
                  This honors the symbiotic relationship: your Loop timing aligns with Earth's
                  actual movements at your specific location, not generic hardcoded times.
                </p>
              </div>
            </div>

            <div className="location-footer">
              <button
                className="location-save"
                onClick={() => setShowSettings(false)}
              >
                Save & Close
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
