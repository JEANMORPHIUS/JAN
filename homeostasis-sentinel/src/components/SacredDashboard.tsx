/** * * SACRED DASHBOARD COMPONENT
 *  * Single view at a time, with substance and stillness
 *  * 
 *  * Principles:
 *  * - Quality over volume
 *  * - Substance over stimulation
 *  * - Action over consumption
 *  * - Revelation over reaction
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

import React, { useState } from 'react';
import { HealthMetrics } from '../types';
import { createSacredDashboard } from '../utils/sacredSpace';
import { createSacredStewardship } from '../utils/sacredSpace';
import { SacredAlert } from './SacredAlert';
import { analyzeWaterMemoryFromMetrics } from '../utils/waterMemory';
import { humanizeMetric } from '../utils/humanDignity';

interface SacredDashboardProps {
  metrics: HealthMetrics[];
}

type ViewMode = 'stillness' | 'guidance' | 'reflection' | 'action';

export const SacredDashboard: React.FC<SacredDashboardProps> = ({ metrics }) => {
  const [currentView, setCurrentView] = useState<ViewMode>('stillness');

  if (metrics.length === 0) {
    return (
      <div className="sacred-dashboard">
        <div className="sacred-dashboard-content">
          <div className="sacred-dashboard-message">
            Welcome to Homeostasis Sentinel. Load your data to begin your stewardship journey.
          </div>
        </div>
      </div>
    );
  }

  const latestMetric = metrics[metrics.length - 1];
  const humanized = humanizeMetric(latestMetric, new Date().toISOString());
  
  // Analyze water memory
  const analysis = analyzeWaterMemoryFromMetrics(latestMetric, []);
  const waterMemory = analysis.waterMemory;
  const spiritualBattle = analysis.spiritualBattle;
  
  const dashboard = createSacredDashboard(metrics, currentView);
  const stewardship = createSacredStewardship(0.75, true); // Hidden score, show wisdom

  const renderView = () => {
    switch (currentView) {
      case 'stillness':
        return (
          <div className="sacred-view-stillness">
            <div className="sacred-view-title">Your Body Speaking Truth</div>
            <div className="sacred-view-content">
              {humanized.humanContext}
            </div>
            <div className="sacred-view-earth">
              ☀️ Morning Active Phase - Aligned
              <br />
              Your body is in conversation with the sun, not separate from it.
            </div>
            <div className="sacred-view-law">
              Law 5: Your commitment to morning protocols is tracked, not judged.
            </div>
          </div>
        );

      case 'guidance':
        return (
          <div className="sacred-view-guidance">
            <div className="sacred-view-title">Your Stewardship Journey</div>
            <div className="sacred-view-content">
              {stewardship.wisdom}
            </div>
            <div className="sacred-view-reflection">
              {stewardship.reflection}
            </div>
            <div className="sacred-view-guidance">
              {stewardship.guidance}
            </div>
          </div>
        );

      case 'reflection':
        return (
          <div className="sacred-view-reflection">
            <div className="sacred-view-title">Water Memory & Spiritual Battles</div>
            <div className="sacred-view-content">
              The water remembers your vibration: {waterMemory.vibrationalMemory.frequency}
            </div>
            <div className="sacred-view-battle">
              Spiritual Battle: {spiritualBattle.battleSides.light} vs {spiritualBattle.battleSides.dark}
              <br />
              Outcome: {spiritualBattle.outcome === 'light' ? 'Light won. Purpose. Stillness. Revelation.' : 
                        spiritualBattle.outcome === 'dark' ? 'Dark won. Return to purpose. Return to stillness.' :
                        'Ongoing. The battle continues.'}
            </div>
            <div className="sacred-view-water">
              Water Memory: {waterMemory.geneticMemory.geneticTruth}
            </div>
          </div>
        );

      case 'action':
        return (
          <div className="sacred-view-action">
            <div className="sacred-view-title">Next Action</div>
            <div className="sacred-view-content">
              {humanized.recommendation}
            </div>
            <div className="sacred-view-action">
              {dashboard.action}
            </div>
            <div className="sacred-view-law">
              Law 13: Listen. Trust the loop. The table never lies.
            </div>
          </div>
        );

      default:
        return null;
    }
  };

  return (
    <div className="sacred-dashboard">
      <div className="sacred-dashboard-header">
        <h1 className="sacred-dashboard-title">Homeostasis Sentinel</h1>
        <p className="sacred-dashboard-subtitle">Day 5 of 376: The Table is Set</p>
      </div>

      <div className="sacred-dashboard-navigation">
        <button 
          className={`sacred-nav-button ${currentView === 'stillness' ? 'active' : ''}`}
          onClick={() => setCurrentView('stillness')}
        >
          Stillness
        </button>
        <button 
          className={`sacred-nav-button ${currentView === 'guidance' ? 'active' : ''}`}
          onClick={() => setCurrentView('guidance')}
        >
          Guidance
        </button>
        <button 
          className={`sacred-nav-button ${currentView === 'reflection' ? 'active' : ''}`}
          onClick={() => setCurrentView('reflection')}
        >
          Reflection
        </button>
        <button 
          className={`sacred-nav-button ${currentView === 'action' ? 'active' : ''}`}
          onClick={() => setCurrentView('action')}
        >
          Action
        </button>
      </div>

      <div className="sacred-dashboard-main">
        <div className="sacred-alert-container">
          <SacredAlert metrics={metrics} />
        </div>
        
        <div className="sacred-view-container">
          {renderView()}
        </div>
      </div>
    </div>
  );
};
