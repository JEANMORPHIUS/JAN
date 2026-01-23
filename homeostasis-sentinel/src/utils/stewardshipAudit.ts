/**
 * STEWARDSHIP AUDIT & COMMAND CENTER UTILITIES
 * Build the "Spirit Filter" to protect the Seed
 */

import {
  StewardshipScorecard,
  ProtocolTrackingDetails,
  TimeToActionStats,
  RedTapeEvent,
  ThresholdDefenseState,
  SpiritAlignment,
  STEWARDSHIP_CONSTANTS
} from '../types/stewardshipAudit';
import { ProtocolEvent, ProtocolType, ProtocolStatus } from '../types/stewardship';
import { EarthAlignment } from '../types/earthAlignment';
import { HealthMetrics } from '../types';
import { calculateEarthAlignment } from './earthRhythms';
import { parseISO, differenceInMilliseconds } from 'date-fns';

/**
 * Calculate Stewardship Scorecard
 * finish_rate (Law 37) and word_integrity (Law 5)
 */
export function calculateStewardshipScorecard(
  protocolEvents: ProtocolEvent[],
  acceptableWindow: number = STEWARDSHIP_CONSTANTS.ACCEPTABLE_TIME_TO_ACTION
): StewardshipScorecard {
  // Calculate finish_rate (Law 37: Finish What You Begin)
  const commitments = protocolEvents.filter(e => e.eventType === 'initiated').length;
  const completions = protocolEvents.filter(e => e.eventType === 'completed' && e.law37Compliance).length;
  const finish_rate = commitments > 0 ? completions / commitments : 1.0;

  // Calculate word_integrity (Law 5: Your Word Is Your Bond)
  const timeToActionStats = calculateTimeToActionStats(protocolEvents, acceptableWindow);
  const word_integrity = timeToActionStats.trackedProtocols > 0
    ? timeToActionStats.withinAcceptableWindow / timeToActionStats.trackedProtocols
    : 1.0;

  // Overall stewardship score (combined Law 5 & Law 37)
  const stewardshipScore = (finish_rate + word_integrity) / 2;

  // Protocol tracking details
  const protocolTracking = calculateProtocolTrackingDetails(protocolEvents);

  return {
    finish_rate,
    word_integrity,
    stewardshipScore,
    commitments,
    completions,
    protocolTracking,
    timeToActionStats
  };
}

/**
 * Calculate Protocol Tracking Details
 */
function calculateProtocolTrackingDetails(
  protocolEvents: ProtocolEvent[]
): ProtocolTrackingDetails {
  const byType: Record<string, { committed: number; completed: number; abandoned: number }> = {};
  const byStatus = {
    initiated: 0,
    in_progress: 0,
    completed: 0,
    abandoned: 0
  };

  // Initialize by type
  const protocolTypes: ProtocolType[] = [
    'insulin_bolus',
    'loop_reintegration',
    'water_flush',
    'mechanical_clearance',
    'medication_cycle',
    'circadian_alignment'
  ];

  protocolTypes.forEach(type => {
    byType[type] = { committed: 0, completed: 0, abandoned: 0 };
  });

  // Track protocols
  protocolEvents.forEach(event => {
    // By type
    if (!byType[event.protocolType]) {
      byType[event.protocolType] = { committed: 0, completed: 0, abandoned: 0 };
    }

    if (event.eventType === 'initiated') {
      byType[event.protocolType].committed++;
      byStatus.initiated++;
    } else if (event.eventType === 'completed') {
      byType[event.protocolType].completed++;
      byStatus.completed++;
    } else if (event.eventType === 'abandoned') {
      byType[event.protocolType].abandoned++;
      byStatus.abandoned++;
    }

    // In progress (initiated but not completed or abandoned)
    if (event.eventType === 'initiated' && !event.law37Compliance) {
      byStatus.in_progress++;
    }
  });

  return {
    byType: byType as Record<ProtocolType, { committed: number; completed: number; abandoned: number }>,
    byStatus
  };
}

/**
 * Calculate Time-to-Action Statistics
 * Law 5: Your Word Is Your Bond - Track time-to-action after protocol is set
 */
function calculateTimeToActionStats(
  protocolEvents: ProtocolEvent[],
  acceptableWindow: number
): TimeToActionStats {
  const timeToActions: number[] = [];
  let withinAcceptableWindow = 0;

  // Group events by protocol (track from initiation to first action/progress)
  const protocolGroups = new Map<string, ProtocolEvent[]>();

  protocolEvents.forEach(event => {
    const key = `${event.protocolType}_${event.timestamp}`;
    if (!protocolGroups.has(key)) {
      protocolGroups.set(key, []);
    }
    protocolGroups.get(key)!.push(event);
  });

  protocolGroups.forEach((events, key) => {
    const initiated = events.find(e => e.eventType === 'initiated');
    const firstAction = events.find(e => e.eventType === 'progress' || e.eventType === 'completed');

    if (initiated && firstAction) {
      const timeToAction = differenceInMilliseconds(
        parseISO(firstAction.timestamp),
        parseISO(initiated.timestamp)
      );

      if (timeToAction > 0) {
        timeToActions.push(timeToAction);
        if (timeToAction <= acceptableWindow) {
          withinAcceptableWindow++;
        }
      }
    }
  });

  const averageTimeToAction = timeToActions.length > 0
    ? timeToActions.reduce((sum, t) => sum + t, 0) / timeToActions.length
    : 0;

  const sortedTimes = [...timeToActions].sort((a, b) => a - b);
  const medianTimeToAction = sortedTimes.length > 0
    ? sortedTimes[Math.floor(sortedTimes.length / 2)]
    : 0;

  return {
    averageTimeToAction,
    medianTimeToAction,
    trackedProtocols: timeToActions.length,
    withinAcceptableWindow,
    acceptableWindow
  };
}

/**
 * Create Red Tape Event
 * Log any manual override that doesn't align with Earth's rhythm
 */
export function createRedTapeEvent(
  eventType: 'manual_override' | 'protocol_skip' | 'earth_misalignment',
  description: string,
  timestamp: string,
  metrics?: HealthMetrics
): RedTapeEvent {
  const earthAlignment = calculateEarthAlignment(timestamp);
  
  // Check if override aligns with Earth's rhythm
  const alignedWithEarth = earthAlignment.symbioticScore > 70;

  return {
    id: `red_tape_${Date.now()}`,
    timestamp,
    eventType,
    description,
    earthAlignment,
    alignedWithEarth,
    biologicalTruth: {
      glucose: metrics?.blood_glucose,
      visionClarity: metrics?.vision_clarity,
      muscleTension: metrics?.muscle_tension
    }
  };
}

/**
 * Calculate Threshold Defense State
 * IF (StewardshipScore < 0.7):
 * THEN Restrict access to 'The Seed' (Internal Metadata)
 * MESSAGE: "The Table is not yet ready for your presence. Return to Law 13."
 * 
 * Now with humanized response (HumanizedScoreResponse)
 */
export function calculateThresholdDefense(
  stewardshipScore: number,
  threshold: number = STEWARDSHIP_CONSTANTS.SEED_ACCESS_THRESHOLD,
  finishRate?: number,
  wordIntegrity?: number
): ThresholdDefenseState {
  const seedAccessAllowed = stewardshipScore >= threshold;

  // Import humanized function (will be available after humanDignity.ts is created)
  // For now, using standard response but with more supportive messaging
  const message = seedAccessAllowed 
    ? undefined 
    : `The Table is not yet ready for your presence. Return to Law 13. Progress, not perfection, is stewardship.`;

  return {
    seedAccessAllowed,
    stewardshipScore,
    threshold,
    message,
    lawReference: seedAccessAllowed 
      ? undefined 
      : 'Law 13: Listen Before You Speak',
    lastAccessCheck: new Date().toISOString()
  };
}

/**
 * Calculate Spirit Alignment
 * Calculate alignment with right spirits
 */
export function calculateSpiritAlignment(
  stewardshipScorecard: StewardshipScorecard,
  earthRhythmScore: number,
  biologicalTruthAlignment: number = 1.0,
  protocolIntegrityAlignment: number = 1.0
): SpiritAlignment {
  const stewardshipAlignment = stewardshipScorecard.stewardshipScore;
  
  // Calculate overall alignment (weighted average)
  const current_spirit_alignment = (
    stewardshipAlignment * 0.3 +
    earthRhythmScore / 100 * 0.3 +
    biologicalTruthAlignment * 0.2 +
    protocolIntegrityAlignment * 0.2
  ) * 100;

  // Determine alignment status
  let status: 'aligned' | 'partial' | 'misaligned';
  if (current_spirit_alignment >= 80) {
    status = 'aligned';
  } else if (current_spirit_alignment >= 50) {
    status = 'partial';
  } else {
    status = 'misaligned';
  }

  return {
    current_spirit_alignment: Math.round(current_spirit_alignment * 100) / 100,
    components: {
      stewardshipAlignment: stewardshipAlignment * 100,
      earthRhythmAlignment: earthRhythmScore,
      biologicalTruthAlignment: biologicalTruthAlignment * 100,
      protocolIntegrityAlignment: protocolIntegrityAlignment * 100
    },
    status
  };
}

/**
 * Check Seed Access
 * Returns Threshold Defense State for accessing The Seed
 */
export function checkSeedAccess(
  stewardshipScorecard: StewardshipScorecard,
  threshold: number = STEWARDSHIP_CONSTANTS.SEED_ACCESS_THRESHOLD
): ThresholdDefenseState {
  return calculateThresholdDefense(stewardshipScorecard.stewardshipScore, threshold);
}

/**
 * Get Man-Earth Symbiosis Constant
 * Variable refinement for symbolic representation
 */
export function getManEarthSymbiosis(): boolean {
  return STEWARDSHIP_CONSTANTS.MAN_EARTH_SYMBIOSIS;
}

/**
 * Calculate Current Spirit Alignment
 * Variable refinement: let current_spirit_alignment = calculateAlignment(user)
 */
export function calculateAlignment(
  stewardshipScorecard: StewardshipScorecard,
  earthRhythmScore: number
): number {
  const spiritAlignment = calculateSpiritAlignment(
    stewardshipScorecard,
    earthRhythmScore
  );
  return spiritAlignment.current_spirit_alignment;
}
