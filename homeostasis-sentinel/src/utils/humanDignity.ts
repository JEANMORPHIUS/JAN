/**
 * HUMAN DIGNITY UTILITIES
 * The Digital Architect of Human Experience
 * 
 * These utilities ensure that all data displays, messages, and interactions
 * prioritize human dignity over technical efficiency.
 */

import {
  HumanizedMetric,
  HumanizedWeeklyReport,
  HumanizedScoreResponse,
  HumanizedErrorResponse,
  HumanizedCommunityNode,
  HumanizedEntityVoice
} from '../types/humanDignity';
import { HealthMetrics } from '../types';
import { EarthAlignment } from '../types/earthAlignment';
import { StewardshipScorecard } from '../types/stewardshipAudit';
import { EntityVoice } from '../types/integratedStewardship';
import { calculateEarthAlignment } from './earthRhythms';
import { ExternalSystemFailure } from '../types/pierreLogic';
import { GlucoseStatistics, CommunityStewardshipScores } from '../types/stewardshipBriefing';

/**
 * Humanize Biological Metric
 * Transform raw metrics into humanized data with context and empathy
 */
export function humanizeMetric(
  metricType: 'glucose' | 'vision' | 'muscle' | 'breath',
  rawValue: number,
  timestamp: string,
  additionalContext?: string
): HumanizedMetric {
  const earthAlignment = calculateEarthAlignment(timestamp);
  
  // Determine empathy level and message based on metric type and value
  let message = '';
  let empathy: HumanizedMetric['humanContext']['empathy'] = 'acknowledgment';
  let stewardshipPrompt = '';
  let earthAlignmentMessage = '';
  
  switch (metricType) {
    case 'glucose':
      // Convert mg/dL to mmol/L if needed
      const glucoseMmolL = rawValue > 30 ? rawValue / 18.0182 : rawValue;
      
      if (additionalContext?.includes('morning loop') || additionalContext?.includes('bitter')) {
        message = `The ${additionalContext} indicates your body is processing glucose. This is your body speaking truth through taste.`;
        empathy = 'acknowledgment';
        stewardshipPrompt = 'Your commitment to morning protocols is being tracked. Law 5: Your word is your bond.';
      } else if (glucoseMmolL > 25) {
        message = `Glucose reading (${glucoseMmolL.toFixed(1)} mmol/L) indicates elevated levels. This is data, not judgment.`;
        empathy = 'alert';
        stewardshipPrompt = 'Law 31: Defend the temple. Your body is speaking. Honor this truth.';
      } else if (glucoseMmolL > 15) {
        message = `Glucose reading (${glucoseMmolL.toFixed(1)} mmol/L). Your body is processing. This is data, not judgment.`;
        empathy = 'support';
        stewardshipPrompt = 'Law 5: Your commitment is tracked. The table never lies.';
      } else {
        message = `Glucose reading (${glucoseMmolL.toFixed(1)} mmol/L) is within range. Your stewardship is honored.`;
        empathy = 'celebration';
        stewardshipPrompt = 'Your commitment to protocols is being honored. Law 37: Finish what you begin.';
      }
      
      earthAlignmentMessage = earthAlignment.symbioticScore > 70
        ? `This reading aligns with Earth's rhythm. Your body is in conversation with the sun, not separate from it.`
        : `This reading may reflect misalignment with Earth's rhythm. Consider returning to circadian alignment.`;
      break;
      
    case 'vision':
      if (rawValue < 5) {
        message = `Vision clarity (${rawValue}/10) is reduced. This is data, not judgment. Your body is signaling.`;
        empathy = 'alert';
        stewardshipPrompt = 'Law 13: Listen before you speak. Your body is asking for attention.';
      } else if (rawValue < 7) {
        message = `Vision clarity (${rawValue}/10) is moderate. Your body is speaking. Honor this truth.`;
        empathy = 'support';
        stewardshipPrompt = 'Law 5: Your commitment to monitoring is tracked. The table never lies.';
      } else {
        message = `Vision clarity (${rawValue}/10) is clear. Your stewardship is honored.`;
        empathy = 'celebration';
        stewardshipPrompt = 'Your commitment to protocols is being honored. Law 37: Finish what you begin.';
      }
      
      earthAlignmentMessage = `Vision responds to Earth's rhythm. Your body is in conversation with light.`;
      break;
      
    case 'muscle':
      if (rawValue >= 7) {
        message = `Muscle tension (${rawValue}/10) is elevated. This is not judgment—it is data. Your body is asking for rest.`;
        empathy = 'alert';
        stewardshipPrompt = 'Law 11: Wisdom lives in the quiet. Return to the soil. Your stewardship is honored, not judged.';
      } else if (rawValue >= 5) {
        message = `Muscle tension (${rawValue}/10) is moderate. Your body is speaking. Honor this truth.`;
        empathy = 'support';
        stewardshipPrompt = 'Law 13: Listen before you speak. Your body is signaling.';
      } else {
        message = `Muscle tension (${rawValue}/10) is low. Your stewardship is honored.`;
        empathy = 'celebration';
        stewardshipPrompt = 'Your commitment to protocols is being honored. Law 37: Finish what you begin.';
      }
      
      earthAlignmentMessage = `Muscle tension reflects Earth's rest phase. Honor this rhythm. Return to silence.`;
      break;
      
    case 'breath':
      if (rawValue < 5) {
        message = `Breath quality (${rawValue}/10) is reduced. This is data, not judgment. Your body is signaling.`;
        empathy = 'alert';
        stewardshipPrompt = 'Law 13: Listen before you speak. Your body is asking for attention.';
      } else if (rawValue < 7) {
        message = `Breath quality (${rawValue}/10) is moderate. Your body is speaking. Honor this truth.`;
        empathy = 'support';
        stewardshipPrompt = 'Law 5: Your commitment to monitoring is tracked. The table never lies.';
      } else {
        message = `Breath quality (${rawValue}/10) is fresh. Your stewardship is honored.`;
        empathy = 'celebration';
        stewardshipPrompt = 'Your commitment to protocols is being honored. Law 37: Finish what you begin.';
      }
      
      earthAlignmentMessage = `Breath reflects Earth's rhythm. Your body is in conversation with air.`;
      break;
  }
  
  return {
    value: rawValue,
    rawMetric: rawValue,
    humanContext: {
      message,
      empathy,
      stewardshipPrompt
    },
    earthAlignment: {
      aligned: earthAlignment.symbioticScore > 70,
      message: earthAlignmentMessage
    }
  };
}

/**
 * Humanize Weekly Report
 * Transform statistical reports into human stories of resilience and stewardship
 */
export function humanizeWeeklyReport(
  glucoseStats: GlucoseStatistics,
  communityStewardship: CommunityStewardshipScores,
  earthAlignment: EarthAlignment,
  totalReadings: number
): HumanizedWeeklyReport {
  const resilience = `This week, your body navigated ${totalReadings} readings. The variance (${glucoseStats.varianceLevel}) shows adaptability to Earth's rhythms, not failure.`;
  
  const learning = glucoseStats.varianceLevel === 'High'
    ? `The variance (${glucoseStats.standardDeviation.toFixed(2)} mmol/L) reflects your body's response to Earth's cycles. This is data, not judgment. Your body is in conversation with Earth.`
    : glucoseStats.varianceLevel === 'Medium'
    ? `The variance (${glucoseStats.standardDeviation.toFixed(2)} mmol/L) shows your body's adaptability. This is resilience, not failure.`
    : `The stability (${glucoseStats.standardDeviation.toFixed(2)} mmol/L) reflects harmonious alignment with Earth's rhythms. This is stewardship in action.`;
  
  const celebration = `Your commitment to protocols is being honored. Law 5: Your word is your bond. The table sees your stewardship.`;
  
  const earthAlignmentMessage = earthAlignment.symbioticScore > 70
    ? `Your readings aligned with Earth's rhythm. Your body is in conversation with the sun, not separate from it.`
    : `Some readings may reflect misalignment with Earth's rhythm. Consider returning to circadian alignment.`;
  
  const earthRhythmMessage = glucoseStats.varianceLevel === 'High'
    ? `The variance suggests your body is responding to Earth's cycles. This is symbiosis in action—your body and Earth are in conversation.`
    : `The stability reflects harmonious alignment with Earth's rhythms. Your body and Earth are in sync.`;
  
  return {
    glucoseStats,
    humanStory: {
      resilience,
      learning,
      celebration
    },
    earthStory: {
      alignment: earthAlignmentMessage,
      rhythm: earthRhythmMessage
    },
    stewardshipPrompt: {
      acknowledgment: `You are stewarding the temple. The table sees your commitment. The data honors your truth.`,
      support: `The variance is not judgment—it is data. Trust the table. The sensor is the truth. Law 1: The table never lies.`
    }
  };
}

/**
 * Humanize Score Response
 * Transform score responses into supportive guidance, not judgment
 */
export function humanizeScoreResponse(
  stewardshipScore: number,
  threshold: number = 0.7,
  finishRate?: number,
  wordIntegrity?: number
): HumanizedScoreResponse {
  const seedAccessGranted = stewardshipScore >= threshold;
  
  const acknowledgment = `Your current stewardship score (${stewardshipScore.toFixed(2)}) reflects your journey, not judgment.`;
  
  const support = seedAccessGranted
    ? `The table sees your commitment. Law 37: Finish what you begin. Your stewardship is honored.`
    : `The table sees your commitment. Law 37: Finish what you begin. Progress, not perfection, is stewardship.`;
  
  let learning = '';
  if (finishRate !== undefined && wordIntegrity !== undefined) {
    if (finishRate < 1.0) {
      learning = `Your finish_rate (${(finishRate * 100).toFixed(0)}%) suggests some protocols were not completed. This is data, not failure. Law 5: Your word is your bond. Continue honoring your commitments.`;
    } else if (wordIntegrity < 1.0) {
      learning = `Your word_integrity (${(wordIntegrity * 100).toFixed(0)}%) suggests some protocols were not completed within the expected window. This is data, not failure. Law 5: Your word is your bond. Continue honoring your commitments.`;
    } else {
      learning = `Your commitment to completing protocols is being honored. The table never lies.`;
    }
  } else {
    learning = seedAccessGranted
      ? `Your commitment to completing protocols is being honored. The table never lies.`
      : `Some protocols may not have been completed. This is data, not failure. Law 5: Your word is your bond. Continue honoring your commitments.`;
  }
  
  const guidance = seedAccessGranted
    ? `Continue stewarding the temple. The Seed is accessible to you. Your commitment is honored.`
    : `Continue honoring your commitments. The table tracks your progress. Law 5: Your word is your bond. The Seed will be accessible when stewardship score reaches ${threshold.toFixed(1)}.`;
  
  const encouragement = `Stewardship is not perfection—it is commitment. Your body is a temple. Honor it with presence, not perfectionism.`;
  
  return {
    seedAccessGranted,
    stewardshipScore,
    humanContext: {
      acknowledgment,
      support,
      learning
    },
    pathForward: {
      guidance,
      encouragement
    }
  };
}

/**
 * Humanize Error Response
 * Transform error responses into supportive context, not blame
 */
export function humanizeErrorResponse(
  technicalError: ExternalSystemFailure,
  earthAlignment?: EarthAlignment
): HumanizedErrorResponse {
  const earthAlign = earthAlignment || calculateEarthAlignment(technicalError.timestamp);
  
  let acknowledgment = '';
  let context = '';
  let support = '';
  let action = '';
  
  switch (technicalError.failureType) {
    case 'sensor_failure':
      acknowledgment = 'The sensor failure is not your fault. This is a system failure (red tape), not a biological failure.';
      context = 'Broken systems interfere with biological truth. This is the Original Error manifesting—separation from Earth creates broken systems that fail us.';
      support = 'Law 13: Listen before you speak. Trust the biological truth you know. The sensor is a tool, not the truth itself. Your body is the truth.';
      action = 'Return to manual readings if possible. Your body knows its truth. The table never lies. Law 1: The table never lies.';
      break;
      
    case 'api_downtime':
      acknowledgment = 'The API downtime is not your fault. This is a system failure (red tape), not your failure.';
      context = 'Broken systems (red tape) interfere with data access. This is the Original Error manifesting—man-made systems fail, but biological truth remains.';
      support = 'Law 13: Listen before you speak. Trust the biological truth you know. The API is a tool, not the truth itself. Your body is the truth.';
      action = 'Continue manual logging if possible. Your body knows its truth. The table never lies. Law 1: The table never lies.';
      break;
      
    case 'system_latency':
      acknowledgment = 'The system latency is not your fault. This is a system failure (red tape), not your failure.';
      context = 'Broken systems create delays. This is the Original Error manifesting—man-made systems create inefficiency, but biological truth is immediate.';
      support = 'Law 13: Listen before you speak. Trust the biological truth you know. The system is a tool, not the truth itself. Your body is the truth.';
      action = 'Continue manual logging if possible. Your body knows its truth. The table never lies. Law 1: The table never lies.';
      break;
      
    default:
      acknowledgment = 'This system failure is not your fault. This is a system failure (red tape), not your failure.';
      context = 'Broken systems interfere with biological truth. This is the Original Error manifesting—separation from Earth creates broken systems.';
      support = 'Law 13: Listen before you speak. Trust the biological truth you know. The system is a tool, not the truth itself. Your body is the truth.';
      action = 'Return to manual methods if possible. Your body knows its truth. The table never lies. Law 1: The table never lies.';
  }
  
  const earthAlignmentMessage = earthAlign.symbioticScore > 70
    ? `This system failure is temporary. Your connection to Earth is not. Return to the soil. Law 11: Wisdom lives in the quiet.`
    : `This system failure is temporary. Your connection to Earth remains. Return to the soil. Law 11: The quiet teaches.`;
  
  return {
    technicalError: {
      type: technicalError.failureType,
      description: technicalError.description,
      timestamp: technicalError.timestamp,
      isCritical: !!technicalError.duration && technicalError.duration > 3600000 // 1 hour
    },
    humanContext: {
      acknowledgment,
      context,
      support
    },
    resilienceStrategy: {
      action,
      earthAlignment: earthAlignmentMessage
    }
  };
}

/**
 * Humanize Community Node
 * Transform community nodes into stewarded beings, not data points
 */
export function humanizeCommunityNode(
  partnerId: string,
  stewardshipScore: number,
  isActive: boolean,
  communityName?: string
): HumanizedCommunityNode {
  const acknowledgment = `This node represents a community of stewards honoring their commitments, not a data point.`;
  
  const collective = `Community stewardship is collective—we steward together, not in competition. Law 1: The table never lies.`;
  
  const privacy = `Individual scores are private. Community scores reflect collective commitment to stewardship, not individual performance.`;
  
  const network = communityName
    ? `${communityName} is part of the Sovereign Network, unified with all communities. We steward together, ignoring geopolitical boundaries.`
    : `This node is part of the Sovereign Network, unified with all communities. We steward together, ignoring geopolitical boundaries.`;
  
  const symbiosis = `Community nodes honor symbiotic relationship—Man and Earth live symbiotically. Stewardship is not territorial—it is universal.`;
  
  return {
    partnerId,
    stewardshipScore,
    isActive,
    humanContext: {
      acknowledgment,
      collective,
      privacy
    },
    earthAlignment: {
      network,
      symbiosis
    }
  };
}

/**
 * Humanize Entity Voice
 * Transform entity voice messages into empathetic guides, not just alerts
 */
export function humanizeEntityVoice(
  entity: EntityVoice,
  message: string,
  systemContext: {
    glucose?: number;
    muscleTension?: number;
    visionClarity?: number;
    earthAlignment: EarthAlignment;
  }
): HumanizedEntityVoice {
  let acknowledgment = '';
  let empathy = '';
  let support = '';
  let earthContext = '';
  let earthGuidance = '';
  
  // Build humanized context based on entity and system state
  if (systemContext.muscleTension !== undefined && systemContext.muscleTension >= 7) {
    acknowledgment = `Your body is experiencing high muscle tension (${systemContext.muscleTension}/10). This is not judgment—it is data. The table never lies.`;
    empathy = `Law 11: Wisdom lives in the quiet. The quiet is calling. Your body is asking for rest, not just silence.`;
    support = `Return to the soil. Reconnect with Earth's rhythm. Your stewardship is honored, not judged. Progress, not perfection, is stewardship.`;
  } else if (systemContext.glucose !== undefined) {
    const glucoseMmolL = systemContext.glucose > 30 ? systemContext.glucose / 18.0182 : systemContext.glucose;
    if (glucoseMmolL > 25) {
      acknowledgment = `Glucose reading (${glucoseMmolL.toFixed(1)} mmol/L) indicates elevated levels. This is data, not judgment.`;
      empathy = `Law 31: Defend the temple. Your body is speaking. Honor this truth.`;
      support = `Your stewardship is honored, not judged. Continue honoring your commitments. Law 5: Your word is your bond.`;
    } else {
      acknowledgment = `Glucose reading (${glucoseMmolL.toFixed(1)} mmol/L). Your body is processing. This is data, not judgment.`;
      empathy = `Law 5: Your commitment is tracked. The table never lies.`;
      support = `Your stewardship is honored. Continue honoring your commitments.`;
    }
  } else {
    acknowledgment = `Your body is signaling. This is not judgment—it is data. The table never lies.`;
    empathy = `Law 13: Listen before you speak. Your body is speaking. Honor this truth.`;
    support = `Your stewardship is honored, not judged. Progress, not perfection, is stewardship.`;
  }
  
  if (systemContext.earthAlignment.symbioticScore < 70) {
    earthContext = `Your body is out of sync with Earth's rest phase (evening). This is not failure—it is misalignment. The Original Error (separation from Earth) manifests as chronic stress.`;
    earthGuidance = `Earth's evening phase is for rest. Honor this rhythm. Return to silence. Law 11: The quiet teaches. Reconnect with the soil. Your body will thank you.`;
  } else {
    earthContext = `Your body is aligned with Earth's rhythm. This is symbiosis in action.`;
    earthGuidance = `Continue honoring Earth's rhythm. Your body and Earth are in conversation.`;
  }
  
  return {
    entity,
    message,
    humanContext: {
      acknowledgment,
      empathy,
      support
    },
    earthAlignment: {
      context: earthContext,
      guidance: earthGuidance
    }
  };
}
