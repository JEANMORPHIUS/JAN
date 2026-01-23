/**
 * SACRED SPACE UTILITIES
 * Healing a Broken Digital World: Creating Sacred Space for Stillness and Revelation
 * 
 * Principles:
 * - Stillness over noise
 * - Substance over stimulation
 * - Action over consumption
 * - Vessel for revelation (not receiver to be rewired)
 */

import {
  SacredSpace,
  SacredAlert,
  SacredDashboard,
  SacredStewardship,
  SacredUpdates,
  SacredProgress
} from '../types/sacredSpace';
import { HealthMetrics } from '../types';
import { humanizeMetric } from './humanDignity';

/**
 * Create Sacred Space
 * Single, focused view that honors stillness and clarity
 */
export function createSacredSpace(
  metrics: HealthMetrics[],
  stillnessMode: boolean = true
): SacredSpace {
  const latestMetric = metrics[metrics.length - 1];
  const humanized = latestMetric ? humanizeMetric(latestMetric, new Date().toISOString()) : null;
  
  const currentWisdom = humanized
    ? humanized.humanContext
    : "Your body is a temple. Listen to its truth. This is stewardship, not monitoring.";
  
  const currentAction = humanized
    ? humanized.recommendation
    : "Return to Law 13. Listen. Trust the loop.";
  
  const currentRevelation = humanized
    ? `What this means for your stewardship journey: ${humanized.humanContext}`
    : "Your stewardship journey reflects your connection to Earth. This is restoration, not separation.";
  
  return {
    stillnessMode,
    currentWisdom,
    currentAction,
    currentRevelation
  };
}

/**
 * Create Sacred Alert
 * One alert at a time, with substance and stillness
 */
export function createSacredAlert(
  message: string,
  revelation: string,
  action?: string
): SacredAlert {
  // Determine urgency based on message content (stillness, not hijacking)
  let urgency: 'stillness' | 'guidance' | 'support' = 'stillness';
  
  if (message.toLowerCase().includes('critical') || message.toLowerCase().includes('urgent')) {
    urgency = 'guidance'; // Not 'critical' or 'high'
  } else if (message.toLowerCase().includes('support') || message.toLowerCase().includes('help')) {
    urgency = 'support';
  }
  
  return {
    isActive: true,
    message,
    urgency,
    revelation,
    action: action || "Return to Law 13. Listen. Trust the loop."
  };
}

/**
 * Create Sacred Dashboard
 * Single view at a time, with substance and stillness
 */
export function createSacredDashboard(
  metrics: HealthMetrics[],
  currentView: 'stillness' | 'guidance' | 'reflection' | 'action' = 'stillness'
): SacredDashboard {
  const latestMetric = metrics[metrics.length - 1];
  const humanized = latestMetric ? humanizeMetric(latestMetric, new Date().toISOString()) : null;
  
  const content = humanized
    ? humanized.humanContext
    : "Your body is a temple. Listen to its truth. This is stewardship, not monitoring.";
  
  const action = humanized
    ? humanized.recommendation
    : "Return to Law 13. Listen. Trust the loop.";
  
  return {
    currentView,
    content,
    navigation: 'minimal', // Not 'multiple sections'
    action
  };
}

/**
 * Create Sacred Stewardship
 * Wisdom, not numbers
 */
export function createSacredStewardship(
  stewardshipScore: number,
  scoreHidden: boolean = true
): SacredStewardship {
  const wisdom = stewardshipScore >= 0.95
    ? "Your stewardship journey reflects profound alignment and dedication. This is restoration, not achievement."
    : stewardshipScore >= 0.7
    ? "Your stewardship journey reflects strong progress and commitment. Progress, not perfection, is stewardship."
    : "Your stewardship journey reflects areas needing attention. Return to the foundational laws. Every step of conscious effort builds the temple.";
  
  const reflection = "What does your stewardship mean for your connection to Earth? The body is a temple. Stewardship is restoration, not separation.";
  
  const guidance = stewardshipScore >= 0.95
    ? "Continue to walk this path of truth, inspiring others with your unwavering commitment."
    : stewardshipScore >= 0.7
    ? "Identify areas where you can deepen your practice, perhaps revisiting Law 37 to finish what you begin."
    : "Return to the foundational laws and protocols. Remember, every step of conscious effort builds the temple.";
  
  return {
    scoreHidden,
    wisdom,
    reflection,
    guidance
  };
}

/**
 * Create Sacred Updates
 * Stillness, not compulsion
 */
export function createSacredUpdates(
  updateMode: 'on-demand' | 'daily' | 'weekly' = 'on-demand'
): SacredUpdates {
  const updateContent = "Your stewardship journey this week. What does it mean? The body is a temple. Stewardship is restoration, not separation.";
  
  const updateAction = "Return to stillness. Listen. Trust the loop.";
  
  const updateFrequency = updateMode === 'on-demand' ? 'weekly' : updateMode;
  
  return {
    updateMode,
    updateFrequency,
    updateContent,
    updateAction
  };
}

/**
 * Create Sacred Progress
 * Wisdom, not achievement
 */
export function createSacredProgress(
  progressPercentage: number,
  progressHidden: boolean = true
): SacredProgress {
  const wisdom = progressPercentage >= 90
    ? "Your stewardship journey reflects profound progress. This is restoration, not achievement."
    : progressPercentage >= 70
    ? "Your stewardship journey reflects strong progress. Progress, not perfection, is stewardship."
    : "Your stewardship journey reflects areas needing attention. Return to the foundational laws. Every step of conscious effort builds the temple.";
  
  const reflection = "What does your journey mean for your connection to Earth? The body is a temple. Stewardship is restoration, not separation.";
  
  const guidance = progressPercentage >= 90
    ? "Continue to walk this path of truth, inspiring others with your unwavering commitment."
    : progressPercentage >= 70
    ? "Identify areas where you can deepen your practice, perhaps revisiting Law 37 to finish what you begin."
    : "Return to the foundational laws and protocols. Remember, every step of conscious effort builds the temple.";
  
  return {
    progressHidden,
    wisdom,
    reflection,
    guidance
  };
}
