/** * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
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

import React from 'react';
import { HealthMetrics } from '../types';
import { generateNextAction } from '../utils/nextActionEngine';

interface NextActionProps {
  metrics: HealthMetrics[];
}

export const NextAction: React.FC<NextActionProps> = ({ metrics }) => {
  const action = generateNextAction(metrics);

  const priorityClassMap = {
    critical: 'action-critical',
    high: 'action-high',
    medium: 'action-medium',
    low: 'action-low',
    none: 'action-none'
  };

  const priorityIconMap = {
    critical: '🚨',
    high: '⚠️',
    medium: '⚡',
    low: 'ℹ️',
    none: '✅'
  };

  const priorityLabelMap = {
    critical: 'CRITICAL',
    high: 'HIGH PRIORITY',
    medium: 'MEDIUM PRIORITY',
    low: 'LOW PRIORITY',
    none: 'SYSTEM STABLE'
  };

  return (
    <div className="next-action">
      <h3 className="section-title">Next Action Recommendation</h3>
      <div className={`action-card ${priorityClassMap[action.priority]}`}>
        <div className="action-header">
          <div className="action-priority">
            <span className="priority-icon">{priorityIconMap[action.priority]}</span>
            <span className="priority-label">{priorityLabelMap[action.priority]}</span>
          </div>
        </div>

        <div className="action-content">
          <div className="action-main">
            <div className="action-title">Recommended Action:</div>
            <div className="action-text">{action.action}</div>
          </div>

          <div className="action-details">
            <div className="action-reason">
              <strong>Reason:</strong> {action.reason}
            </div>
            <div className="action-urgency">
              <strong>Urgency:</strong> {action.urgency}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

