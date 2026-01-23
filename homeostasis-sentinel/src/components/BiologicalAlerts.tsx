import React from 'react';
import { HealthMetrics } from '../types';
import { detectAcidosisRisk, calculateOsmoticPressure, calculateEnhancedCircadianScore, detectGritFactor, detectLoopFeedback, getGlucoseAlerts, calculateVisionVelocity, checkRecoveryRate, detectCurrentAcidosis } from '../utils/biologicalLogic';

interface BiologicalAlertsProps {
  metrics: HealthMetrics[];
}

export const BiologicalAlerts: React.FC<BiologicalAlertsProps> = ({ metrics }) => {
  const acidosisRisk = detectAcidosisRisk(metrics);
  const osmoticAnalyses = calculateOsmoticPressure(metrics);
  const recentOsmotic = osmoticAnalyses[osmoticAnalyses.length - 1];
  const circadianScore = calculateEnhancedCircadianScore(metrics);
  const gritFactor = detectGritFactor(metrics);
  const loopFeedback = detectLoopFeedback(metrics);
  const recentLoopFeedback = loopFeedback[loopFeedback.length - 1];
  const glucoseAlerts = getGlucoseAlerts(metrics);
  const visionVelocity = calculateVisionVelocity(metrics);
  const recoveryRate = checkRecoveryRate(metrics);

  const activeAlerts = [];

  // "Break Glass" - Highest Priority Alert
  if (glucoseAlerts.hasBreakGlass && glucoseAlerts.latestGlucose !== undefined && glucoseAlerts.latestVision !== undefined) {
    activeAlerts.push({
      type: 'break-glass',
      severity: 'high',
      title: '🚨 BREAK GLASS: Protocol Failing',
      message: `Glucose ${glucoseAlerts.latestGlucose} mg/dL AND Vision ${glucoseAlerts.latestVision.toFixed(1)}/10. Loop theory failing. Have fast-acting insulin ready.`,
      icon: '🚨'
    });
  }

  // "Double-Down" Rule
  if (glucoseAlerts.hasDoubleDown && glucoseAlerts.latestGlucose !== undefined && glucoseAlerts.latestVision !== undefined) {
    activeAlerts.push({
      type: 'double-down',
      severity: 'high',
      title: 'DOUBLE-DOWN: Critical Osmotic Pressure',
      message: `Glucose ${glucoseAlerts.latestGlucose} mg/dL AND Vision ${glucoseAlerts.latestVision.toFixed(1)}/10. STOP LOOP. Critical osmotic pressure.`,
      icon: '⚡'
    });
  }

  if (glucoseAlerts.hasCriticalLow && glucoseAlerts.latestGlucose !== undefined) {
    activeAlerts.push({
      type: 'glucose',
      severity: 'high',
      title: 'CRITICAL: Very Low Glucose',
      message: `Blood glucose is ${glucoseAlerts.latestGlucose} mg/dL (critical low <54). More dangerous in zero-food state (no glycogen stores).`,
      icon: '🚨'
    });
  } else if (glucoseAlerts.hasLow && glucoseAlerts.latestGlucose !== undefined) {
    activeAlerts.push({
      type: 'glucose',
      severity: 'medium',
      title: 'Low Glucose Alert',
      message: `Blood glucose is ${glucoseAlerts.latestGlucose} mg/dL (low <70). Monitor closely.`,
      icon: '⚠️'
    });
  } else if (glucoseAlerts.hasHigh && glucoseAlerts.latestGlucose !== undefined && !glucoseAlerts.hasDoubleDown) {
    activeAlerts.push({
      type: 'glucose',
      severity: 'high',
      title: 'High Glucose Alert',
      message: `Blood glucose is ${glucoseAlerts.latestGlucose} mg/dL (high >180). Consider intervention.`,
      icon: '📈'
    });
  }

  // Rapid Vision Decline (Velocity)
  if (visionVelocity.isRapidDecline) {
    activeAlerts.push({
      type: 'velocity',
      severity: 'high',
      title: 'Rapid Vision Decline',
      message: `Vision dropping at dangerous velocity (${visionVelocity.velocity.toFixed(2)}/hour). ${Math.abs(visionVelocity.change).toFixed(1)} point change in ${visionVelocity.hours.toFixed(1)} hours.`,
      icon: '⬇️'
    });
  }

  // Recovery Rate Failure
  if (recoveryRate.hasFailedRecovery) {
    activeAlerts.push({
      type: 'recovery',
      severity: 'high',
      title: 'Mechanical Lever Failed',
      message: recoveryRate.recommendation,
      icon: '❌'
    });
  }

  // Velocity & Glycogen Paradox (Low Glucose + Negative Velocity)
  if (glucoseAlerts.hasLow && glucoseAlerts.latestGlucose !== undefined && visionVelocity.velocity < 0) {
    activeAlerts.push({
      type: 'velocity-glycogen',
      severity: 'high',
      title: 'URGENT RECOVERY: Velocity & Glycogen Paradox',
      message: `Low glucose (${glucoseAlerts.latestGlucose} mg/dL) with vision declining (velocity: ${visionVelocity.velocity.toFixed(2)}/hour). In zero-food state, "Low" can become "Crash" in minutes. Have honey/juice ready.`,
      icon: '⚡'
    });
  }

  if (acidosisRisk.isActive) {
    activeAlerts.push({
      type: 'acidosis',
      severity: acidosisRisk.severity,
      title: 'System Acidic - "Sway" Detected',
      message: acidosisRisk.recommendation,
      icon: '🚨'
    });
  }

  if (recentOsmotic && recentOsmotic.requiresClearance) {
    activeAlerts.push({
      type: 'osmotic',
      severity: 'high',
      title: 'Mechanical Clearance Required',
      message: recentOsmotic.recommendation,
      icon: '💧'
    });
  }

  if (gritFactor.requiresClearance) {
    activeAlerts.push({
      type: 'grit',
      severity: gritFactor.severity,
      title: 'Stagnation Detected (Grit Factor)',
      message: gritFactor.recommendation,
      icon: '🔄'
    });
  }

  if (recentLoopFeedback?.isHeavy) {
    activeAlerts.push({
      type: 'loop',
      severity: 'high',
      title: 'Loop Too Heavy',
      message: recentLoopFeedback.recommendation,
      icon: '⚖️'
    });
  }

  if (circadianScore.violations > 0) {
    activeAlerts.push({
      type: 'circadian',
      severity: 'medium',
      title: 'Circadian Compliance Issue',
      message: `${circadianScore.violations} loop frequency violation(s) detected outside 08:00-20:00 window. Adjusted score: ${circadianScore.adjustedScore.toFixed(1)}/100`,
      icon: '🌙'
    });
  }

  if (activeAlerts.length === 0) {
    return (
      <div className="biological-alerts">
        <h3 className="section-title">Biological System Status</h3>
        <div className="system-status-ok">
          <span className="status-icon">✅</span>
          <span>All systems within acceptable parameters</span>
        </div>
      </div>
    );
  }

  return (
    <div className="biological-alerts">
      <h3 className="section-title">Biological System Status</h3>
      <div className="alerts-container">
        {activeAlerts.map((alert, idx) => (
          <div key={idx} className={`biological-alert alert-${alert.severity}`}>
            <div className="alert-header">
              <span className="alert-icon">{alert.icon}</span>
              <strong>{alert.title}</strong>
            </div>
            <div className="alert-message">{alert.message}</div>
          </div>
        ))}
      </div>
    </div>
  );
};

