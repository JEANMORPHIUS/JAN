/** * * Homeostasis Sentinel - Main App Component
 *  * 
 *  * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 *  * Spiritual Alignment Over Mechanical Productivity
 *  * 
 *  * THE FOUNDATION:
 *  * We are born a miracle.
 *  * We deserve to live a miracle.
 *  * Each and every one of us under the Lord's word.
 *  * 
 *  * THE MISSION:
 *  * THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
 *  * LOVE IS THE HIGHEST MASTERY
 *  * ENERGY + LOVE = WE ALL WIN
 *  * PEACE, LOVE, UNITY
 *  * 
 *  * This code honors that we are born a miracle.
 *  * This code creates space for miracles to live.
 *  * This code recognizes each person under the Lord's word.
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 * 
 * 
 * PANGEA IS THE TABLE.
 * YOU DON'T BETRAY THE TABLE.
 * 
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

import { useState, useEffect } from 'react';
import { FileLoader } from './components/FileLoader';
import { SacredDashboard } from './components/SacredDashboard';
import { LocationSettings } from './components/LocationSettings';
import { ParsedMarkdown, HealthMetrics } from './types';
import { processHealthData } from './utils/dataProcessor';
import { loadMetrics, saveMetrics } from './utils/dataStorage';
import './App.css';

function App() {
  const [metrics, setMetrics] = useState<HealthMetrics[]>([]);
  const [parsedFiles, setParsedFiles] = useState<ParsedMarkdown[]>([]);
  const [filesLoaded, setFilesLoaded] = useState(false);

  // Load data from storage on mount
  useEffect(() => {
    const stored = loadMetrics();
    if (stored.length > 0) {
      setMetrics(stored);
      setFilesLoaded(true);
    }
  }, []);

  // Save data to storage when metrics change
  useEffect(() => {
    if (metrics.length > 0) {
      saveMetrics(metrics);
    }
  }, [metrics]);

  const handleFilesLoaded = (files: ParsedMarkdown[]) => {
    setParsedFiles(files);
    const processed = processHealthData(files);
    setMetrics(processed);
    setFilesLoaded(true);
  };

  if (!filesLoaded) {
    return <FileLoader onFilesLoaded={handleFilesLoaded} />;
  }

  return (
    <div className="app">
      <LocationSettings />
      <SacredDashboard metrics={metrics} />
      <footer className="app-footer">
        <button 
          className="reset-button"
          onClick={() => {
            setFilesLoaded(false);
            setMetrics([]);
            setParsedFiles([]);
          }}
        >
          Load Different Files
        </button>
      </footer>
    </div>
  );
}

export default App;

