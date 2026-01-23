import React, { useMemo } from 'react';
import { HealthMetrics } from '../types';
import { getCircadianData, isInSolarWindow } from '../utils/dataProcessor';

interface CircadianHeatmapProps {
  metrics: HealthMetrics[];
}

export const CircadianHeatmap: React.FC<CircadianHeatmapProps> = ({ metrics }) => {
  const circadianData = useMemo(() => getCircadianData(metrics), [metrics]);

  // Create 24-hour grid
  const hours = Array.from({ length: 24 }, (_, i) => i);
  const days = Array.from(new Set(circadianData.map(d => d.date))).slice(-7); // Last 7 days

  const getHeatmapValue = (day: string, hour: number): number | null => {
    const dataPoint = circadianData.find(d => d.date === day && d.hour === hour);
    return dataPoint?.loopFrequency ?? null;
  };

  const getCellColor = (value: number | null, hour: number): string => {
    if (value === null) return 'bg-gray-900';
    
    const inSolarWindow = isInSolarWindow(hour);
    const intensity = Math.min(value / 10, 1); // Normalize to 0-1
    
    if (inSolarWindow) {
      // Green gradient for solar window
      const greenIntensity = Math.floor(intensity * 255);
      return `rgb(34, ${greenIntensity}, 0)`;
    } else {
      // Blue gradient for non-solar window
      const blueIntensity = Math.floor(intensity * 255);
      return `rgb(0, 34, ${blueIntensity})`;
    }
  };

  return (
    <div className="circadian-heatmap">
      <h3 className="section-title">Circadian Heatmap: Loop Integration vs Solar Window (10am-6pm)</h3>
      <div className="heatmap-container">
        <div className="heatmap-grid">
          <div className="heatmap-header">
            <div className="hour-label"></div>
            {hours.map(hour => (
              <div key={hour} className="hour-label">
                {hour.toString().padStart(2, '0')}:00
              </div>
            ))}
          </div>
          {days.map(day => (
            <div key={day} className="heatmap-row">
              <div className="day-label">
                {new Date(day).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}
              </div>
              {hours.map(hour => {
                const value = getHeatmapValue(day, hour);
                const color = getCellColor(value, hour);
                const inSolarWindow = isInSolarWindow(hour);
                
                return (
                  <div
                    key={`${day}-${hour}`}
                    className="heatmap-cell"
                    style={{ backgroundColor: color }}
                    title={`${day} ${hour}:00 - Loop Frequency: ${value ?? 'N/A'} - ${inSolarWindow ? 'Solar Window' : 'Outside Solar Window'}`}
                  >
                    {value !== null && (
                      <span className="cell-value">{value.toFixed(1)}</span>
                    )}
                  </div>
                );
              })}
            </div>
          ))}
        </div>
      </div>
      <div className="heatmap-legend">
        <div className="legend-item">
          <div className="legend-color" style={{ backgroundColor: 'rgb(34, 200, 0)' }}></div>
          <span>Solar Window (10am-6pm) - Integrated</span>
        </div>
        <div className="legend-item">
          <div className="legend-color" style={{ backgroundColor: 'rgb(0, 34, 200)' }}></div>
          <span>Outside Solar Window</span>
        </div>
        <div className="legend-note">
          Intensity indicates Loop Frequency (0-10)
        </div>
      </div>
    </div>
  );
};

