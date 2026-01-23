/**
 * HUMAN DIGNITY TYPES
 * The Digital Architect of Human Experience
 * 
 * These types ensure that all data displays, messages, and interactions
 * prioritize human dignity over technical efficiency.
 */

import { EarthAlignment } from './earthAlignment';
import { EntityVoice } from './integratedStewardship';

/**
 * Humanized Metric
 * Every biological metric must include human context, not just raw numbers
 */
export interface HumanizedMetric {
  /** Raw metric value */
  value: number;
  rawMetric: number;
  /** Human context for this metric */
  humanContext: {
    /** What this metric means for the human (acknowledgment, not judgment) */
    message: string;
    /** Empathy level: acknowledgment, support, celebration, or alert */
    empathy: 'acknowledgment' | 'support' | 'celebration' | 'alert';
    /** Stewardship prompt: how to honor this truth */
    stewardshipPrompt: string;
  };
  /** Earth alignment context */
  earthAlignment: {
    /** Is this reading aligned with Earth's rhythm? */
    aligned: boolean;
    /** What Earth's rhythm tells us about this reading */
    message: string;
  };
}

/**
 * Humanized Weekly Report
 * Reports are stories of stewardship and resilience, not just statistics
 */
export interface HumanizedWeeklyReport {
  /** Statistical data (mean, variance, etc.) */
  glucoseStats: {
    mean: number;
    variance: number;
    standardDeviation: number;
    min: number;
    max: number;
    count: number;
    varianceLevel: 'Low' | 'Medium' | 'High';
  };
  /** Human story: resilience, learning, celebration */
  humanStory: {
    /** Acknowledgment of resilience (e.g., "This week, your body navigated 17 readings") */
    resilience: string;
    /** Learning from the data (e.g., "The bitter morning loops indicate processing") */
    learning: string;
    /** Celebration of commitment (e.g., "Your morning protocols are honored") */
    celebration: string;
  };
  /** Earth story: alignment and rhythm */
  earthStory: {
    /** How readings aligned with Earth's rhythm */
    alignment: string;
    /** What Earth's rhythm tells us (e.g., "bitter taste suggests circadian response") */
    rhythm: string;
  };
  /** Stewardship prompts: acknowledgment and support */
  stewardshipPrompt: {
    /** Acknowledgment of stewardship commitment */
    acknowledgment: string;
    /** Support message: variance is data, not judgment */
    support: string;
  };
}

/**
 * Humanized Score Response
 * Scores are reflections of stewardship journeys, not judgments
 */
export interface HumanizedScoreResponse {
  seedAccessGranted: boolean;
  stewardshipScore: number;
  /** Human context: acknowledgment, support, learning */
  humanContext: {
    /** Acknowledgment of the journey (e.g., "Your score reflects your journey, not judgment") */
    acknowledgment: string;
    /** Supportive message (progress, not perfection) */
    support: string;
    /** Learning opportunity (what the data tells us) */
    learning: string;
  };
  /** Path forward: guidance and encouragement */
  pathForward: {
    /** Guidance for stewardship */
    guidance: string;
    /** Encouragement (stewardship is commitment, not perfection) */
    encouragement: string;
  };
}

/**
 * Humanized Error Response
 * Errors are system failures or learning opportunities, not user failures
 */
export interface HumanizedErrorResponse {
  /** Technical error details */
  technicalError: {
    type: 'api_downtime' | 'sensor_failure' | 'system_latency' | 'red_tape' | 'other';
    description: string;
    timestamp: string;
    isCritical: boolean;
  };
  /** Human context: acknowledgment, context, support */
  humanContext: {
    /** Acknowledgment (e.g., "This is not your fault") */
    acknowledgment: string;
    /** Context about why errors occur (broken systems, red tape) */
    context: string;
    /** Support message (Law references, biological truth) */
    support: string;
  };
  /** Resilience strategy: action and Earth alignment */
  resilienceStrategy: {
    /** What to do (e.g., "Return to manual readings") */
    action: string;
    /** Earth alignment context (connection to Earth is not broken) */
    earthAlignment: string;
  };
}

/**
 * Humanized Community Node
 * Community nodes are networks of stewarded beings, not data points
 */
export interface HumanizedCommunityNode {
  partnerId: string;
  stewardshipScore: number;
  isActive: boolean;
  /** Human context: acknowledgment, collective, privacy */
  humanContext: {
    /** Acknowledgment (e.g., "This node represents a community of stewards") */
    acknowledgment: string;
    /** Collective framing (e.g., "We steward together, not in competition") */
    collective: string;
    /** Privacy acknowledgment (e.g., "Individual scores are private") */
    privacy: string;
  };
  /** Earth alignment: network and symbiosis */
  earthAlignment: {
    /** Network context (e.g., "London and Cyprus are unified") */
    network: string;
    /** Symbiotic relationship (e.g., "Man and Earth live symbiotically") */
    symbiosis: string;
  };
}

/**
 * Humanized Entity Voice
 * Entity voices are empathetic guides for stewardship, not just alerts
 */
export interface HumanizedEntityVoice {
  entity: EntityVoice;
  message: string;
  /** Human context: acknowledgment, empathy, support */
  humanContext: {
    /** Acknowledgment (e.g., "Your body is experiencing high muscle tension") */
    acknowledgment: string;
    /** Empathy (e.g., "This is not judgment—it is data") */
    empathy: string;
    /** Support (e.g., "Your stewardship is honored, not judged") */
    support: string;
  };
  /** Earth alignment: context and guidance */
  earthAlignment: {
    /** Context (e.g., "Your body is out of sync with Earth's rest phase") */
    context: string;
    /** Guidance (e.g., "Return to silence. Law 11: The quiet teaches") */
    guidance: string;
  };
}

/**
 * Empathy Level
 * Levels of empathy for humanized interactions
 */
export type EmpathyLevel = 'acknowledgment' | 'support' | 'celebration' | 'alert';
