import { HealthMetrics, AcidosisRisk, OsmoticPressureAnalysis, LoopFeedback } from '../types';
import { parseISO, addHours, getHours } from 'date-fns';

/** * * Acidosis Risk Predictor ("Sway" Logic)
 *  * T1D: Absence of insulin leads to ketone production (acid)
 *  * When blood becomes acidic, nervous system "sways"
 *  * 
 *  * Trigger: muscle_tension > 7 AND vision_clarity < 5 for more than two consecutive data points
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
export function detectAcidosisRisk(metrics: HealthMetrics[]): AcidosisRisk {
  const sorted = [...metrics].sort((a, b) => a.date!.localeCompare(b.date!));
  
  let consecutiveCount = 0;
  let lastDetected: string | undefined;
  let maxConsecutive = 0;
  
  for (const metric of sorted) {
    const isAcidic = 
      (metric.muscle_tension !== undefined && metric.muscle_tension > 7) &&
      (metric.vision_clarity !== undefined && metric.vision_clarity < 5);
    
    if (isAcidic) {
      consecutiveCount++;
      lastDetected = metric.date;
      if (consecutiveCount > maxConsecutive) {
        maxConsecutive = consecutiveCount;
      }
    } else {
      consecutiveCount = 0;
    }
  }
  
  const isActive = maxConsecutive >= 2;
  
  let severity: 'low' | 'medium' | 'high' = 'low';
  if (maxConsecutive >= 4) severity = 'high';
  else if (maxConsecutive >= 2) severity = 'medium';
  
  const recommendation = isActive
    ? `SYSTEM ACIDIC: Flush recommended (increased pure water/alkaline hydration). Avoid Loop re-integration until muscle tension drops below 5.`
    : `System stable. Continue monitoring.`;
  
  return {
    isActive,
    severity,
    consecutiveDays: maxConsecutive,
    recommendation,
    lastDetected
  };
}

/**
 * Osmotic Pressure Coefficient
 * Vision blur in T1D is usually caused by glucose-induced swelling of the eye lens
 * 
 * Logic: Calculate delta between loop_frequency and vision_clarity
 * If loop_frequency is high but vision_clarity is decreasing → "Mechanical Clearance Required"
 */
export function calculateOsmoticPressure(metrics: HealthMetrics[]): OsmoticPressureAnalysis[] {
  const sorted = [...metrics]
    .filter(m => m.loop_frequency !== undefined && m.vision_clarity !== undefined)
    .sort((a, b) => a.date!.localeCompare(b.date!));
  
  const analyses: OsmoticPressureAnalysis[] = [];
  
  for (let i = 0; i < sorted.length; i++) {
    const current = sorted[i];
    const delta = (current.loop_frequency ?? 0) - (current.vision_clarity ?? 0);
    
    // Check if vision is decreasing while loop frequency is high
    const previous = i > 0 ? sorted[i - 1] : null;
    const visionDecreasing = previous && 
      (current.vision_clarity ?? 0) < (previous.vision_clarity ?? 0);
    const loopHigh = (current.loop_frequency ?? 0) > 6;
    
    const requiresClearance = loopHigh && visionDecreasing && delta > 2;
    
    const recommendation = requiresClearance
      ? `MECHANICAL CLEARANCE REQUIRED: High loop frequency with declining vision. Consider Swim/Sauna/Movement to clear glucose-induced osmotic pressure.`
      : delta > 3
        ? `Monitor: Loop frequency significantly higher than vision clarity.`
        : `Osmotic balance stable.`;
    
    analyses.push({
      delta,
      requiresClearance,
      recommendation,
      date: current.date!
    });
  }
  
  return analyses;
}

/**
 * Enhanced Circadian Compliance Scoring
 * Penalize circadian_sync_score if loop_frequency increments occur outside 08:00 - 20:00 range
 * 
 * Re-ingesting melatonin-heavy "night urine" during solar peak or glucose-heavy "day urine" 
 * during repair phase (night) disrupts the Suprachiasmatic Nucleus (SCN)
 */
export function calculateEnhancedCircadianScore(metrics: HealthMetrics[]): {
  score: number;
  violations: number;
  adjustedScore: number;
} {
  const sorted = [...metrics]
    .filter(m => m.circadian_sync_score !== undefined && m.loop_frequency !== undefined)
    .sort((a, b) => a.date!.localeCompare(b.date!));
  
  let violations = 0;
  let totalScore = 0;
  let scoreCount = 0;
  
  for (const metric of sorted) {
    const baseScore = metric.circadian_sync_score ?? 0;
    totalScore += baseScore;
    scoreCount++;
    
    // Extract hour from date (default to noon if no time specified)
    const date = parseISO(metric.date!);
    const hour = getHours(date);
    
    // Check if loop frequency activity occurred outside 08:00-20:00 window
    const loopActive = (metric.loop_frequency ?? 0) > 0;
    const outsideWindow = hour < 8 || hour >= 20;
    
    if (loopActive && outsideWindow) {
      violations++;
    }
  }
  
  const avgScore = scoreCount > 0 ? totalScore / scoreCount : 0;
  
  // Penalize: -5 points per violation, minimum score of 0
  const penalty = violations * 5;
  const adjustedScore = Math.max(0, avgScore - penalty);
  
  return {
    score: avgScore,
    violations,
    adjustedScore
  };
}

/**
 * "Grit" Factor: Detect stagnation (tension increasing without mechanical clearance)
 * If muscle_tension increases while swim_duration or sauna_duration remains zero,
 * escalate the "Mechanical Clearance" alert.
 */
export function detectGritFactor(metrics: HealthMetrics[]): {
  requiresClearance: boolean;
  severity: 'low' | 'medium' | 'high';
  recommendation: string;
  date?: string;
} {
  const sorted = [...metrics]
    .filter(m => m.muscle_tension !== undefined)
    .sort((a, b) => a.date!.localeCompare(b.date!));

  if (sorted.length < 2) {
    return {
      requiresClearance: false,
      severity: 'low',
      recommendation: 'Insufficient data to detect stagnation pattern.'
    };
  }

  // Check last 2-3 data points for tension increase without activity
  const recent = sorted.slice(-3);
  let tensionIncrease = false;
  let noActivity = true;

  for (let i = 1; i < recent.length; i++) {
    const prev = recent[i - 1];
    const curr = recent[i];
    
    const tensionRising = (prev.muscle_tension ?? 0) < (curr.muscle_tension ?? 0);
    const hasActivity = (curr.sauna_duration ?? 0) > 0 || curr.swimming === true;

    if (tensionRising) {
      tensionIncrease = true;
      if (!hasActivity && (prev.sauna_duration ?? 0) === 0 && prev.swimming !== true) {
        noActivity = true;
        return {
          requiresClearance: true,
          severity: (curr.muscle_tension ?? 0) > 7 ? 'high' : (curr.muscle_tension ?? 0) > 5 ? 'medium' : 'low',
          recommendation: `MECHANICAL CLEARANCE REQUIRED: Muscle tension increasing (${prev.muscle_tension?.toFixed(1)} → ${curr.muscle_tension?.toFixed(1)}) without swim/sauna activity. Stagnation = acidity. Recommend immediate Swim or Sauna session.`,
          date: curr.date
        };
      }
    }
  }

  return {
    requiresClearance: false,
    severity: 'low',
    recommendation: 'Tension patterns within acceptable range with adequate clearance activity.'
  };
}

/**
 * "Loop" Feedback: Detect if loop is too "heavy" (hyper-osmotic with glucose)
 * If vision_clarity drops below 4 shortly after a loop_frequency increment,
 * OR if blood_glucose is high (>180) after loop increment,
 * flag that the "Loop" is currently too "heavy" and advise a 2-hour "Water-Only" window.
 */
export function detectLoopFeedback(metrics: HealthMetrics[]): LoopFeedback[] {
  const sorted = [...metrics]
    .filter(m => m.loop_frequency !== undefined && m.vision_clarity !== undefined)
    .sort((a, b) => a.date!.localeCompare(b.date!));

  const feedback: LoopFeedback[] = [];

  for (let i = 1; i < sorted.length; i++) {
    const prev = sorted[i - 1];
    const curr = sorted[i];
    
    const loopIncreased = (prev.loop_frequency ?? 0) < (curr.loop_frequency ?? 0);
    const visionDropped = (curr.vision_clarity ?? 0) < 4;
    const visionDeclined = (curr.vision_clarity ?? 0) < (prev.vision_clarity ?? 0);
    const glucoseHigh = (curr.blood_glucose ?? 0) > 180;

    // Check if vision dropped below 4 after loop increment OR glucose is high
    if (loopIncreased && (visionDropped || visionDeclined || glucoseHigh)) {
      const isHeavy = (curr.vision_clarity ?? 0) < 4 || glucoseHigh;
      
      let recommendation = '';
      if (glucoseHigh && curr.blood_glucose) {
        recommendation = `LOOP TOO HEAVY: Glucose ${curr.blood_glucose} mg/dL after loop increment. Loop is hyper-osmotic with glucose. ADVISORY: 2-hour Water-Only window before next loop.`;
      } else if ((curr.vision_clarity ?? 0) < 4) {
        recommendation = `LOOP TOO HEAVY: Vision dropped to ${curr.vision_clarity?.toFixed(1)} after loop increment. Loop is hyper-osmotic with glucose. ADVISORY: 2-hour Water-Only window before next loop.`;
      } else {
        recommendation = `Loop impact detected: Vision/glucose changes after loop increment. Monitor closely.`;
      }
      
      feedback.push({
        isHeavy,
        detectedAfterLoop: true,
        recommendation,
        date: curr.date!
      });
    }
  }

  return feedback;
}

/**
 * Get glucose alerts (high/low thresholds)
 * Enhanced for zero-food T1D protocol
 */
export function getGlucoseAlerts(metrics: HealthMetrics[]): {
  hasHigh: boolean;
  hasLow: boolean;
  hasCriticalLow: boolean;
  hasBreakGlass: boolean; // Glucose >250 AND Vision <3
  hasDoubleDown: boolean; // Glucose >180 AND Vision <4 (critical osmotic pressure)
  latestGlucose?: number;
  latestVision?: number;
  highCount: number;
  lowCount: number;
  criticalLowCount: number;
} {
  const glucoseReadings = metrics
    .filter(m => m.blood_glucose !== undefined)
    .sort((a, b) => a.date!.localeCompare(b.date!));

  if (glucoseReadings.length === 0) {
    return {
      hasHigh: false,
      hasLow: false,
      hasCriticalLow: false,
      hasBreakGlass: false,
      hasDoubleDown: false,
      highCount: 0,
      lowCount: 0,
      criticalLowCount: 0
    };
  }

  const latest = metrics[metrics.length - 1];
  const latestGlucose = latest.blood_glucose ?? 0;
  const latestVision = latest.vision_clarity;

  const highCount = glucoseReadings.filter(m => (m.blood_glucose ?? 0) > 180).length;
  const lowCount = glucoseReadings.filter(m => (m.blood_glucose ?? 0) < 70 && (m.blood_glucose ?? 0) >= 54).length;
  const criticalLowCount = glucoseReadings.filter(m => (m.blood_glucose ?? 0) < 54).length;

  // "Break Glass" condition: Protocol failing - glucose >250 AND vision <3
  const hasBreakGlass = latestGlucose > 250 && latestVision !== undefined && latestVision < 3;

  // "Double-Down" Rule: High glucose AND low vision = critical osmotic pressure
  const hasDoubleDown = latestGlucose > 180 && latestVision !== undefined && latestVision < 4;

  return {
    hasHigh: latestGlucose > 180,
    hasLow: latestGlucose < 70 && latestGlucose >= 54,
    hasCriticalLow: latestGlucose < 54,
    hasBreakGlass,
    hasDoubleDown,
    latestGlucose,
    latestVision,
    highCount,
    lowCount,
    criticalLowCount
  };
}

/**
 * Calculate "Velocity" of vision decline
 * Detects rapid drops (e.g., 8 to 5 in 2 hours)
 */
export function calculateVisionVelocity(metrics: HealthMetrics[]): {
  velocity: number; // Change per hour
  isRapidDecline: boolean;
  hours: number;
  change: number;
} {
  const visionData = metrics
    .filter(m => m.vision_clarity !== undefined)
    .sort((a, b) => a.date!.localeCompare(b.date!));

  if (visionData.length < 2) {
    return {
      velocity: 0,
      isRapidDecline: false,
      hours: 0,
      change: 0
    };
  }

  // Get last 2 data points
  const recent = visionData.slice(-2);
  const prev = recent[0];
  const curr = recent[1];

  const prevVision = prev.vision_clarity ?? 0;
  const currVision = curr.vision_clarity ?? 0;
  const change = currVision - prevVision;

  // Estimate hours between readings (default to 1 if same day)
  const prevDate = parseISO(prev.date!);
  const currDate = parseISO(curr.date!);
  const hoursDiff = Math.max(1, (currDate.getTime() - prevDate.getTime()) / (1000 * 60 * 60));
  
  const velocity = change / hoursDiff;

  // Rapid decline: Dropping >1.5 points per hour
  const isRapidDecline = velocity < -1.5;

  return {
    velocity,
    isRapidDecline,
    hours: hoursDiff,
    change
  };
}

/**
 * Recovery Rate: Check if swim/sauna improved vision within 60 minutes
 * Enhanced: 20 MIN SWIM must improve vision by at least 1 point within 60 min
 * If mechanical clearance doesn't meet threshold, lever has failed
 */
export function checkRecoveryRate(metrics: HealthMetrics[]): {
  hasFailedRecovery: boolean;
  lastActivity?: string;
  visionBefore?: number;
  visionAfter?: number;
  improvement?: number;
  recommendation: string;
} {
  const sorted = [...metrics]
    .filter(m => m.vision_clarity !== undefined)
    .sort((a, b) => a.date!.localeCompare(b.date!));

  if (sorted.length < 2) {
    return {
      hasFailedRecovery: false,
      recommendation: 'Insufficient data to assess recovery rate.'
    };
  }

  // Look for recent activity (swim or sauna) - check within 60 minutes
  for (let i = sorted.length - 1; i > 0; i--) {
    const current = sorted[i];
    const previous = sorted[i - 1];

    const currentDate = parseISO(current.date!);
    const previousDate = parseISO(previous.date!);
    const minutesDiff = (currentDate.getTime() - previousDate.getTime()) / (1000 * 60);

    // Check if activity occurred and we're within 60 minutes
    const hadSwim = current.swimming === true;
    const hadSauna = (current.sauna_duration && current.sauna_duration > 0);
    
    if ((hadSwim || hadSauna) && minutesDiff <= 60) {
      const visionBefore = previous.vision_clarity ?? 0;
      const visionAfter = current.vision_clarity ?? 0;
      const improvement = visionAfter - visionBefore;

      const activityType = hadSwim ? 'Swim' : 'Sauna';
      const activityDuration = hadSwim ? '20 MIN' : `${current.sauna_duration} MIN`;

      // Enhanced threshold: Must improve by at least 1 point for 20 MIN SWIM
      // For sauna, threshold is 0.5 points
      const requiredImprovement = hadSwim ? 1.0 : 0.5;

      if (improvement < requiredImprovement) {
        return {
          hasFailedRecovery: true,
          lastActivity: `${activityDuration} ${activityType}`,
          visionBefore,
          visionAfter,
          improvement,
          recommendation: `MECHANICAL LEVER FAILED: ${activityDuration} ${activityType} did not improve vision by required threshold (${visionBefore.toFixed(1)} → ${visionAfter.toFixed(1)}, need +${requiredImprovement}). Sugar/acid load too high for mechanical clearance alone. Protocol needs "Water Flush" or medical intervention.`
        };
      }
    }
  }

  return {
    hasFailedRecovery: false,
    recommendation: 'No recovery failures detected.'
  };
}

/**
 * Detect Current Acidosis State (not prediction)
 * If breath_quality < 3 (Metallic/Acetone) AND muscle_tension > 8
 * This is current acidosis, not predicted risk
 */
export function detectCurrentAcidosis(metrics: HealthMetrics[]): {
  isCurrentAcidosis: boolean;
  severity: 'medium' | 'high';
  recommendation: string;
  date?: string;
} {
  const sorted = [...metrics]
    .filter(m => m.breath_quality !== undefined && m.muscle_tension !== undefined)
    .sort((a, b) => a.date!.localeCompare(b.date!));

  if (sorted.length === 0) {
    return {
      isCurrentAcidosis: false,
      severity: 'medium',
      recommendation: 'Insufficient data to detect current acidosis state.'
    };
  }

  const latest = sorted[sorted.length - 1];
  const breathLow = (latest.breath_quality ?? 10) < 3;
  const tensionHigh = (latest.muscle_tension ?? 0) > 8;

  if (breathLow && tensionHigh) {
    const severity = (latest.muscle_tension ?? 0) > 9 ? 'high' : 'medium';
    return {
      isCurrentAcidosis: true,
      severity,
      recommendation: `CURRENT ACIDOSIS STATE: Breath quality ${latest.breath_quality?.toFixed(1)}/10 (Acetone/Metallic) AND Muscle tension ${latest.muscle_tension?.toFixed(1)}/10. This is not a prediction - you are currently in an acidic state. IMMEDIATE ACTION: Flush protocol + mechanical clearance.`,
      date: latest.date
    };
  }

  return {
    isCurrentAcidosis: false,
    severity: 'medium',
    recommendation: 'No current acidosis state detected.'
  };
}

/**
 * "Hard-Deck" Kill-Switch: Critical system breach detection
 * If TrendForecaster predicts vision_clarity < 2 within next 12 hours,
 * trigger CRITICAL SYSTEM BREACH alert to prevent permanent damage.
 */
export function checkHardDeckKillSwitch(predictedVision: number | null): {
  isBreach: boolean;
  alert: string;
} {
  if (predictedVision === null) {
    return {
      isBreach: false,
      alert: ''
    };
  }

  if (predictedVision < 2) {
    return {
      isBreach: true,
      alert: '🚨 CRITICAL SYSTEM BREACH 🚨\n\nPredicted vision clarity < 2 within 12 hours. This represents risk of permanent vascular or neurological damage.\n\nSTOP PROTOCOL IMMEDIATELY.\n\nThis is a RED LIGHT condition. Do not continue fasting protocol. Seek medical attention if symptoms persist.'
    };
  }

  if (predictedVision < 3) {
    return {
      isBreach: false,
      alert: '⚠️ APPROACHING HARD-DECK\n\nPredicted vision clarity < 3. Monitor extremely closely. Prepare to halt protocol if vision continues to decline.'
    };
  }

  return {
    isBreach: false,
    alert: ''
  };
}

