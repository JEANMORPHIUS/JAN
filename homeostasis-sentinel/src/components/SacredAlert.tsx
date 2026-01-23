/**
 * SACRED ALERT COMPONENT
 * One alert at a time, with substance and stillness
 * 
 * Principles:
 * - Stillness over noise
 * - Substance over stimulation
 * - Revelation over reaction
 */

import React from 'react';
import { HealthMetrics } from '../types';
import { createSacredAlert } from '../utils/sacredSpace';
import { analyzeWaterMemoryFromMetrics } from '../utils/waterMemory';
import { humanizeMetric } from '../utils/humanDignity';

interface SacredAlertProps {
  metrics: HealthMetrics[];
}

export const SacredAlert: React.FC<SacredAlertProps> = ({ metrics }) => {
  if (metrics.length === 0) {
    return null;
  }

  const latestMetric = metrics[metrics.length - 1];
  const humanized = humanizeMetric(latestMetric, new Date().toISOString());
  
  // Determine if there's an alert-worthy situation
  let hasAlert = false;
  let message = '';
  let revelation = '';
  let action = '';

  // Check for critical glucose
  if (latestMetric.blood_glucose !== undefined) {
    const glucoseMmolL = latestMetric.blood_glucose > 30 
      ? latestMetric.blood_glucose / 18.0182 
      : latestMetric.blood_glucose;
    
    if (glucoseMmolL < 4) {
      hasAlert = true;
      message = `Glucose reading: ${glucoseMmolL.toFixed(1)} mmol/L. This is a low reading, signaling your body needs immediate nourishment.`;
      revelation = "Your body is speaking truth. The mirror never lies. This is data, not judgment. Law 1: The table never lies.";
      action = "Please consume a fast-acting carbohydrate now to restore balance. Return to Law 13. Listen. Trust the loop.";
    } else if (glucoseMmolL > 15) {
      hasAlert = true;
      message = humanized.humanContext;
      revelation = "Your body is processing glucose. The bitter taste tells the truth. This is biological communication, not error. Law 1: The table never lies.";
      action = humanized.recommendation || "Return to Law 13. Listen. Trust the loop.";
    }
  }

  // Check for water memory / spiritual battle
  if (hasAlert) {
    const { spiritualBattle } = analyzeWaterMemoryFromMetrics(latestMetric);
    if (spiritualBattle.outcome === 'dark') {
      revelation += ` The water remembers the spiritual battle. Frequency: ${spiritualBattle.battleSides.dark}. Return to purpose. Return to stillness.`;
    }
  }

  if (!hasAlert) {
    return (
      <div className="sacred-alert sacred-alert-stillness">
        <div className="sacred-alert-content">
          <div className="sacred-alert-message">
            All systems within acceptable parameters. Your body is speaking truth. The mirror never lies.
          </div>
          <div className="sacred-alert-revelation">
            Law 1: The table never lies. Your stewardship is honored, not judged.
          </div>
        </div>
      </div>
    );
  }

  const alert = createSacredAlert(message, revelation, action);

  return (
    <div className={`sacred-alert sacred-alert-${alert.urgency}`}>
      <div className="sacred-alert-content">
        <div className="sacred-alert-message">
          {alert.message}
        </div>
        <div className="sacred-alert-revelation">
          {alert.revelation}
        </div>
        {alert.action && (
          <div className="sacred-alert-action">
            {alert.action}
          </div>
        )}
      </div>
    </div>
  );
};
