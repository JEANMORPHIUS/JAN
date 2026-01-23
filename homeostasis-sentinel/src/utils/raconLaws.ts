/**
 * RACON LAW INTEGRATION
 * The Book of Racon: 40 Laws Operating System
 * 
 * Key Laws Applied:
 * - Law 1: The Table Never Lies (Truth Engine - biological data is truth)
 * - Law 5: Your Word Is Your Bond (Protocol Tracking - track to completion)
 * - Law 37: Finish What You Begin (Protocol Completion - complete all initiated protocols)
 * 
 * The database is 'The Table.' It cannot lie.
 * Any belief-based overrides must be flagged as 'Original Error' interference.
 */

import { HealthMetrics } from '../types';
import { 
  OriginalErrorFlag, 
  OriginalErrorType 
} from '../types/earthAlignment';
import {
  ProtocolStewardship,
  ProtocolEvent,
  ProtocolType,
  ProtocolEventType,
  ProtocolCompletionStatus,
  ProtocolStatus
} from '../types/stewardship';
import { parseISO } from 'date-fns';

/**
 * Law 1: The Table Never Lies
 * Truth Engine: Biological data is truth, not belief
 * 
 * Detect belief-based overrides that conflict with biological truth
 */
export function detectBeliefOverride(
  biologicalTruth: number,
  beliefOverride?: number,
  sensorReading?: number
): OriginalErrorFlag {
  if (beliefOverride === undefined) {
    return {
      isError: false,
      description: 'No belief override detected. Biological truth honored.',
      biologicalTruth: `Biological truth: ${biologicalTruth}`,
      timestamp: new Date().toISOString()
    };
  }
  
  // If belief override conflicts with biological truth, flag as error
  const conflict = Math.abs(beliefOverride - biologicalTruth) > 10; // Threshold: 10% difference
  
  if (conflict) {
    return {
      isError: true,
      errorType: 'belief_override',
      description: `Belief override (${beliefOverride}) conflicts with biological truth (${biologicalTruth}). Law 1: The Table Never Lies.`,
      biologicalTruth: `Biological truth: ${biologicalTruth}`,
      beliefOverride: true,
      timestamp: new Date().toISOString()
    };
  }
  
  return {
    isError: false,
    description: 'Belief override aligned with biological truth.',
    biologicalTruth: `Biological truth: ${biologicalTruth}`,
    timestamp: new Date().toISOString()
  };
}

/**
 * Detect "Original Error" interference
 * Red tape, bureaucracy, sensor errors, insurance delays
 */
export function detectOriginalError(
  metrics: HealthMetrics[],
  expectedReading?: number
): OriginalErrorFlag[] {
  const errors: OriginalErrorFlag[] = [];
  
  for (const metric of metrics) {
    // Check for sensor error (glucose reading too extreme without biological markers)
    if (metric.blood_glucose !== undefined) {
      const glucose = metric.blood_glucose;
      
      // Sensor error: Extremely high glucose (>300) without vision/muscle symptoms
      if (glucose > 300 && 
          (metric.vision_clarity === undefined || metric.vision_clarity >= 6) &&
          (metric.muscle_tension === undefined || metric.muscle_tension <= 5)) {
        errors.push({
          isError: true,
          errorType: 'sensor_error',
          description: `Sensor error detected: Glucose ${glucose} without corresponding biological markers. Possibly sensor malfunction or red tape interference.`,
          biologicalTruth: `Expected biological truth based on vision (${metric.vision_clarity}) and muscle tension (${metric.muscle_tension})`,
          timestamp: metric.date
        });
      }
    }
    
    // Check for insurance delay (missing medication/insulin data when expected)
    // This would be detected by missing protocol completion (Law 37)
    
    // Check for red tape interference (delayed access to biological truth)
    if (metric.date) {
      const metricDate = parseISO(metric.date);
      const daysSinceMetric = (Date.now() - metricDate.getTime()) / (1000 * 60 * 60 * 24);
      
      // If metric is more than 7 days old without update, possible red tape delay
      if (daysSinceMetric > 7) {
        errors.push({
          isError: true,
          errorType: 'red_tape',
          description: `Red tape interference: Data gap detected (${daysSinceMetric.toFixed(1)} days). Possible bureaucracy delay in accessing biological truth.`,
          biologicalTruth: `Last recorded biological truth: ${metric.date}`,
          timestamp: new Date().toISOString()
        });
      }
    }
  }
  
  return errors;
}

/**
 * Law 5: Your Word Is Your Bond
 * Protocol Tracking: Track all initiated protocols to completion
 */
export function trackProtocolCommitment(
  protocolType: ProtocolType,
  timestamp: string,
  commitmentLevel: number
): ProtocolEvent {
  return {
    timestamp,
    protocolType,
    eventType: 'initiated',
    details: `Protocol ${protocolType} initiated with commitment level ${commitmentLevel}. Law 5: Your Word Is Your Bond.`,
    law5Compliance: commitmentLevel >= 70, // Minimum 70% commitment for Law 5 compliance
    law37Compliance: false // Will be updated on completion
  };
}

/**
 * Law 37: Finish What You Begin
 * Protocol Completion: Complete all initiated protocols
 */
export function completeProtocol(
  protocolEvent: ProtocolEvent,
  timestamp: string
): ProtocolEvent {
  return {
    ...protocolEvent,
    timestamp,
    eventType: 'completed',
    details: `Protocol ${protocolEvent.protocolType} completed. Law 37: Finish What You Begin.`,
    law5Compliance: protocolEvent.law5Compliance, // Maintain original commitment
    law37Compliance: true // Protocol completed
  };
}

/**
 * Calculate Protocol Stewardship
 * Combines Law 5 (commitment) and Law 37 (completion)
 */
export function calculateProtocolStewardship(
  protocolEvents: ProtocolEvent[]
): ProtocolStewardship {
  // Calculate completion status
  const totalInitiated = protocolEvents.filter(e => e.eventType === 'initiated').length;
  const protocolsCompleted = protocolEvents.filter(e => e.law37Compliance).length;
  const protocolsAbandoned = protocolEvents.filter(e => 
    e.eventType === 'abandoned' || 
    (e.eventType === 'initiated' && !e.law37Compliance)
  ).length;
  
  const completionRate = totalInitiated > 0 
    ? (protocolsCompleted / totalInitiated) * 100 
    : 100;
  
  // Calculate Law 37 adherence (completion rate)
  const law37Adherence = completionRate;
  
  // Calculate protocol commitment (Law 5 compliance rate)
  const law5Compliant = protocolEvents.filter(e => e.law5Compliance).length;
  const protocolCommitment = protocolEvents.length > 0
    ? (law5Compliant / protocolEvents.length) * 100
    : 100;
  
  // Get active protocols (initiated but not completed)
  const activeProtocols = protocolEvents
    .filter(e => e.eventType === 'initiated' && !e.law37Compliance)
    .map(e => ({
      protocolType: e.protocolType,
      startTime: e.timestamp,
      expectedCompletion: '', // Would be calculated based on protocol type
      status: 'in_progress' as ProtocolStatus,
      commitmentLevel: e.law5Compliance ? 90 : 50
    }));
  
  const completionStatus: ProtocolCompletionStatus = {
    totalInitiated,
    protocolsCompleted,
    protocolsAbandoned,
    completionRate,
    law37Adherence
  };
  
  return {
    protocolCommitment,
    activeProtocols,
    completionStatus,
    protocolTracking: protocolEvents
  };
}

/**
 * Check if protocol should be initiated (Law 5: Your Word Is Your Bond)
 * Only initiate if commitment level is sufficient
 */
export function shouldInitiateProtocol(commitmentLevel: number): boolean {
  // Minimum 70% commitment for Law 5 compliance
  return commitmentLevel >= 70;
}

/**
 * Check if protocol should be completed (Law 37: Finish What You Begin)
 * All initiated protocols must be completed
 */
export function shouldCompleteProtocol(protocolEvent: ProtocolEvent): boolean {
  // If protocol is initiated, it must be completed (Law 37)
  return protocolEvent.eventType === 'initiated' && !protocolEvent.law37Compliance;
}
