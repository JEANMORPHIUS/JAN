import { HealthMetrics, NextAction, AcidosisRisk } from '../types';
import { detectAcidosisRisk, detectGritFactor, detectLoopFeedback, calculateOsmoticPressure, getGlucoseAlerts, calculateVisionVelocity, checkRecoveryRate, detectCurrentAcidosis } from './biologicalLogic';
import { forecastVisionClarityMovingAverage } from './trendForecaster';
import { checkHardDeckKillSwitch } from './biologicalLogic';

/** * * Next Action Recommendation Engine
 *  * Generates actionable recommendations based on current biological state
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
export function generateNextAction(metrics: HealthMetrics[]): NextAction {
  if (metrics.length === 0) {
    return {
      priority: 'none',
      action: 'No data available. Begin tracking your daily metrics.',
      reason: 'System requires baseline data to provide recommendations.',
      urgency: 'Establish baseline before starting protocol.'
    };
  }

  const latest = metrics[metrics.length - 1];
  const forecast = forecastVisionClarityMovingAverage(metrics);
  const killSwitch = checkHardDeckKillSwitch(forecast?.predictedVisionClarity ?? null);
  const acidosisRisk = detectAcidosisRisk(metrics);
  const gritFactor = detectGritFactor(metrics);
  const loopFeedback = detectLoopFeedback(metrics);
  const osmoticAnalyses = calculateOsmoticPressure(metrics);
  const recentOsmotic = osmoticAnalyses[osmoticAnalyses.length - 1];
  const glucoseAlerts = getGlucoseAlerts(metrics);
  const visionVelocity = calculateVisionVelocity(metrics);
  const recoveryRate = checkRecoveryRate(metrics);
  const currentAcidosis = detectCurrentAcidosis(metrics);

  // PRIORITY 1: CRITICAL SYSTEM BREACH (Hard-Deck Kill-Switch)
  if (killSwitch.isBreach) {
    return {
      priority: 'critical',
      action: 'STOP PROTOCOL IMMEDIATELY',
      reason: killSwitch.alert,
      urgency: 'RED LIGHT: Predicted vision < 2. Risk of permanent damage.'
    };
  }

  // PRIORITY 2: "Break Glass" - Protocol Failing (Glucose >250 AND Vision <3)
  if (glucoseAlerts.hasBreakGlass && glucoseAlerts.latestGlucose !== undefined && glucoseAlerts.latestVision !== undefined) {
    return {
      priority: 'critical',
      action: '🚨 BREAK GLASS: PROTOCOL FAILING - Glucose >250 mg/dL AND Vision <3. Have fast-acting insulin ready. Loop theory failing physical reality. Consider medical intervention.',
      reason: `Blood glucose ${glucoseAlerts.latestGlucose} mg/dL with vision ${glucoseAlerts.latestVision.toFixed(1)}/10. The "Loop" contains glucose but lacks insulin signaling - fueling the fire.`,
      urgency: 'CRITICAL: Protocol failure detected. Break glass insulin dose may be required.'
    };
  }

  // PRIORITY 3: Current Acidosis State (not prediction)
  if (currentAcidosis.isCurrentAcidosis) {
    return {
      priority: 'critical',
      action: 'CURRENT ACIDOSIS STATE: Breath quality (Acetone) + High tension detected. This is CURRENT state, not prediction. IMMEDIATE: Flush protocol + mechanical clearance (Swim/Sauna).',
      reason: currentAcidosis.recommendation,
      urgency: `CRITICAL: Currently in acidic state (${currentAcidosis.severity} severity). Immediate intervention required.`
    };
  }

  // PRIORITY 4: Critical Glucose (Low) - Velocity & Glycogen Paradox
  if (glucoseAlerts.hasCriticalLow && glucoseAlerts.latestGlucose !== undefined) {
    return {
      priority: 'critical',
      action: 'CRITICAL: Very Low Glucose - Immediate intervention required. In zero-food state, this is MORE dangerous (no glycogen stores). Have high-glucose recovery source (honey/juice) ready.',
      reason: `Blood glucose is ${glucoseAlerts.latestGlucose} mg/dL (critical low <54 mg/dL). Zero glycogen stores in zero-food state increases risk.`,
      urgency: 'CRITICAL: Risk of severe hypoglycemia with no glycogen buffer.'
    };
  }

  // PRIORITY 5: Velocity & Glycogen Paradox (Low Glucose + Negative Velocity)
  if (glucoseAlerts.hasLow && glucoseAlerts.latestGlucose !== undefined && visionVelocity.velocity < 0) {
    return {
      priority: 'high',
      action: 'URGENT RECOVERY: Low glucose (<70) with vision declining. In zero-food state, "Low" can become "Crash" in minutes. Have honey/juice backup ready immediately. Monitor every 15 minutes.',
      reason: `Blood glucose ${glucoseAlerts.latestGlucose} mg/dL (low) with vision velocity ${visionVelocity.velocity.toFixed(2)}/hour (declining). No glycogen buffer in zero-food state.`,
      urgency: 'HIGH: Low glucose + declining vision = risk of rapid crash.'
    };
  }

  // PRIORITY 6: Acidosis Risk (Sway Detected) - Predicted
  if (acidosisRisk.isActive) {
    if (acidosisRisk.severity === 'high') {
      return {
        priority: 'critical',
        action: 'Flush Protocol: Increased pure water/alkaline hydration. Avoid Loop re-integration until tension drops below 5.',
        reason: `${acidosisRisk.consecutiveDays} consecutive days with high tension (>7) and low vision (<5). System acidic.`,
        urgency: 'HIGH: Nervous system "sway" detected. Immediate hydration required.'
      };
    }
    return {
      priority: 'high',
      action: 'Flush Protocol: Increase water/alkaline intake. Monitor tension closely.',
      reason: `Acidosis risk detected: ${acidosisRisk.consecutiveDays} consecutive days.`,
      urgency: 'Moderate: System trending acidic.'
    };
  }

  // PRIORITY 3: Vision Critical
  if (latest.vision_clarity !== undefined && latest.vision_clarity < 3) {
    return {
      priority: 'critical',
      action: 'Immediate intervention: Water flush + consider Swim/Sauna for mechanical clearance. Monitor vision every 30 minutes.',
      reason: `Current vision clarity is ${latest.vision_clarity.toFixed(1)}/10. Approaching Hard-Deck threshold.`,
      urgency: 'CRITICAL: Vision below safety threshold.'
    };
  }

  // PRIORITY 4: Grit Factor (Stagnation = Acidity)
  if (gritFactor.requiresClearance) {
    return {
      priority: gritFactor.severity === 'high' ? 'high' : 'medium',
      action: `MECHANICAL CLEARANCE REQUIRED: ${gritFactor.severity === 'high' ? 'Immediate' : 'Recommended'} Swim or Sauna session. Stagnation = acidity.`,
      reason: gritFactor.recommendation,
      urgency: gritFactor.severity === 'high' ? 'HIGH: Tension rising without clearance activity.' : 'Moderate: Activity required to prevent stagnation.'
    };
  }

  // PRIORITY 5: Loop Too Heavy
  const recentLoopFeedback = loopFeedback[loopFeedback.length - 1];
  if (recentLoopFeedback?.isHeavy) {
    return {
      priority: 'high',
      action: '2-hour Water-Only window before next loop. Loop is currently too "heavy" (hyper-osmotic with glucose).',
      reason: recentLoopFeedback.recommendation,
      urgency: 'HIGH: Loop feedback indicates glucose overload.'
    };
  }

  // PRIORITY 6: Osmotic Pressure (Mechanical Clearance)
  if (recentOsmotic?.requiresClearance) {
    return {
      priority: 'high',
      action: 'MECHANICAL CLEARANCE: Recommend Swim/Sauna/Movement to clear glucose-induced osmotic pressure.',
      reason: recentOsmotic.recommendation,
      urgency: 'HIGH: Vision declining with high loop frequency.'
    };
  }

  // PRIORITY 7: Vision Trending Down
  if (forecast && forecast.trend === 'declining' && forecast.predictedVisionClarity < 5) {
    const swimRecommendation = forecast.predictedVisionClarity < 4 
      ? 'Immediate 20-30 minute Swim session' 
      : 'Consider 20-minute Swim session';
    
    return {
      priority: forecast.alertLevel === 'warning' ? 'high' : 'medium',
      action: `Vision Trending Down: ${swimRecommendation}. Monitor vision closely.`,
      reason: `Forecast predicts vision ${forecast.predictedVisionClarity.toFixed(1)}/10 in next 12 hours (${forecast.confidence}% confidence).`,
      urgency: forecast.alertLevel === 'warning' ? 'HIGH: Vision decline predicted.' : 'Moderate: Monitor closely.'
    };
  }

  // PRIORITY 8: High Tension
  if (latest.muscle_tension !== undefined && latest.muscle_tension > 7) {
    return {
      priority: 'medium',
      action: 'Tension High: Suggest Magnesium/Water Flush. Consider light movement or sauna if tension persists.',
      reason: `Muscle tension is ${latest.muscle_tension.toFixed(1)}/10. Elevated tension indicates metabolic stress.`,
      urgency: 'Moderate: Monitor tension and consider intervention if it continues to rise.'
    };
  }

  // PRIORITY 9: Tension Elevated
  if (latest.muscle_tension !== undefined && latest.muscle_tension > 5 && latest.muscle_tension <= 7) {
    return {
      priority: 'low',
      action: 'Tension Moderately Elevated: Monitor hydration. Consider light activity or sauna if available.',
      reason: `Muscle tension is ${latest.muscle_tension.toFixed(1)}/10. Within acceptable range but trending upward.`,
      urgency: 'Low: Continue monitoring.'
    };
  }

  // PRIORITY 12: System Stable
  return {
    priority: 'none',
    action: 'System Stable: Continue protocol as planned. Maintain hydration and monitor metrics.',
    reason: 'All biological parameters within acceptable ranges.',
    urgency: 'No immediate action required. Continue tracking.'
  };
}

