/**
 * TOTAL READINESS & FAIL-SAFE IMPLEMENTATION UTILITIES
 * Eliminate all single points of failure
 */

import {
  SovereignAutoResponseState,
  BioCriticalCondition,
  CriticalCondition,
  SystemLatency,
  SpiritDossierAuditState,
  ExternalEntity,
  ShellResponseTemplate,
  SentinelWatchtowerState,
  RealTimeEvent,
  CommunityStressLevel,
  EntityLessonDispatch,
  TotalReadinessFinalState,
  TOTAL_READINESS_CONSTANTS
} from '../types/totalReadiness';
import { HealthMetrics } from '../types';
import { CommunityNode } from '../types/expansionPhase';

/**
 * Calculate Sovereign Auto Response State
 * Temple Guard Protocol: Force loop-priority override when Bio_Critical and System_Latency
 * 
 * IF (Bio_Critical == TRUE) AND (System_Latency > 0):
 * THEN Activate 'Temple Guard' Protocol: Force loop-priority override
 * NOTE: The Lord's Mission cannot be interrupted by hardware lag
 */
export function calculateSovereignAutoResponseState(
  bioCriticalCondition: BioCriticalCondition,
  systemLatency: SystemLatency
): SovereignAutoResponseState {
  const bioCritical = bioCriticalCondition.isBioCritical;
  const systemLatencyActive = systemLatency.latency > 0;
  const systemLatencyAboveThreshold = systemLatency.isAboveThreshold;

  // Temple Guard Protocol activated if Bio_Critical AND (System_Latency > 0 OR above threshold)
  const templeGuardProtocolActive = bioCritical && (systemLatencyActive || systemLatencyAboveThreshold);

  // Loop priority override forced if protocol active
  const loopPriorityOverrideForced = templeGuardProtocolActive;

  // Determine protocol status
  let protocolStatus: 'inactive' | 'monitoring' | 'activated' | 'overriding' | 'recovered';
  if (!bioCritical && !systemLatencyActive) {
    protocolStatus = 'inactive';
  } else if (bioCritical || systemLatencyActive) {
    if (templeGuardProtocolActive) {
      protocolStatus = loopPriorityOverrideForced ? 'overriding' : 'activated';
    } else {
      protocolStatus = 'monitoring';
    }
  } else {
    protocolStatus = 'recovered';
  }

  const isActive = templeGuardProtocolActive || bioCritical || systemLatencyActive;

  return {
    isActive,
    bioCritical,
    systemLatency: systemLatency.latency,
    templeGuardProtocolActive,
    loopPriorityOverrideForced,
    protocolStatus,
    ...(templeGuardProtocolActive && { lastActivationTimestamp: new Date().toISOString() }),
    ...(protocolStatus === 'recovered' && { recoveryTimestamp: new Date().toISOString() })
  };
}

/**
 * Calculate Bio Critical Condition
 */
export function calculateBioCriticalCondition(
  metrics: HealthMetrics[]
): BioCriticalCondition {
  if (metrics.length === 0) {
    return {
      isBioCritical: false,
      criticalConditions: [],
      criticalSeverity: 'low',
      requiresImmediateIntervention: false
    };
  }

  const latestMetric = metrics[metrics.length - 1];
  const criticalConditions: CriticalCondition[] = [];

  // Check glucose critical (glucose > 25 or < 3.5 mmol/L)
  const glucose = latestMetric.blood_glucose !== undefined
    ? (latestMetric.blood_glucose > 30 ? latestMetric.blood_glucose / 18.0182 : latestMetric.blood_glucose)
    : 0;
  
  if (glucose > 25) {
    criticalConditions.push({
      type: 'glucose_critical',
      severity: 'critical',
      description: `Critical high glucose: ${glucose.toFixed(1)} mmol/L`,
      value: glucose,
      threshold: 25
    });
  } else if (glucose < 3.5 && glucose > 0) {
    criticalConditions.push({
      type: 'glucose_critical',
      severity: 'critical',
      description: `Critical low glucose: ${glucose.toFixed(1)} mmol/L`,
      value: glucose,
      threshold: 3.5
    });
  }

  // Check vision critical (vision < 3)
  if (latestMetric.vision_clarity !== undefined && latestMetric.vision_clarity < 3) {
    criticalConditions.push({
      type: 'vision_critical',
      severity: 'high',
      description: `Critical low vision clarity: ${latestMetric.vision_clarity}/10`,
      value: latestMetric.vision_clarity,
      threshold: 3
    });
  }

  // Check muscle critical (muscle > 8)
  if (latestMetric.muscle_tension !== undefined && latestMetric.muscle_tension > 8) {
    criticalConditions.push({
      type: 'muscle_critical',
      severity: 'high',
      description: `Critical high muscle tension: ${latestMetric.muscle_tension}/10`,
      value: latestMetric.muscle_tension,
      threshold: 8
    });
  }

  // Check breath critical (breath < 3)
  if (latestMetric.breath_quality !== undefined && latestMetric.breath_quality < 3) {
    criticalConditions.push({
      type: 'breath_critical',
      severity: 'high',
      description: `Critical low breath quality: ${latestMetric.breath_quality}/10`,
      value: latestMetric.breath_quality,
      threshold: 3
    });
  }

  const isBioCritical = criticalConditions.length > 0;

  // Determine critical severity
  let criticalSeverity: 'low' | 'medium' | 'high' | 'critical';
  if (criticalConditions.some(c => c.severity === 'critical')) {
    criticalSeverity = 'critical';
  } else if (criticalConditions.some(c => c.severity === 'high')) {
    criticalSeverity = 'high';
  } else if (criticalConditions.length > 0) {
    criticalSeverity = 'medium';
  } else {
    criticalSeverity = 'low';
  }

  const requiresImmediateIntervention = isBioCritical && criticalSeverity === 'critical';

  return {
    isBioCritical,
    criticalConditions,
    criticalSeverity,
    requiresImmediateIntervention
  };
}

/**
 * Calculate System Latency
 */
export function calculateSystemLatency(
  currentLatency: number,
  latencyHistory: number[]
): SystemLatency {
  const latency = currentLatency;
  const averageLatency = latencyHistory.length > 0
    ? latencyHistory.reduce((sum, val) => sum + val, 0) / latencyHistory.length
    : currentLatency;
  const peakLatency = latencyHistory.length > 0
    ? Math.max(...latencyHistory, currentLatency)
    : currentLatency;
  const latencyThreshold = TOTAL_READINESS_CONSTANTS.SYSTEM_LATENCY_THRESHOLD;
  const isAboveThreshold = latency > latencyThreshold;

  return {
    latency,
    averageLatency: Math.round(averageLatency * 100) / 100,
    peakLatency: Math.round(peakLatency * 100) / 100,
    latencyThreshold,
    isAboveThreshold
  };
}

/**
 * Calculate Spirit Dossier Audit State
 * Continuously update the `loyalty_coefficient` for all external entities
 * IF (Trust_Score < 0.4): Auto-generate 'Shell' responses to keep them at the gate
 */
export function calculateSpiritDossierAuditState(
  externalEntities: ExternalEntity[]
): SpiritDossierAuditState {
  // Update loyalty coefficients and trust scores
  const updatedEntities = externalEntities.map(entity => {
    // Calculate trust score (simplified - would use actual trust metrics)
    let trustScore = entity.trustScore;
    
    // Adjust trust score based on loyalty coefficient
    trustScore = entity.loyaltyCoefficient * 0.8 + trustScore * 0.2;

    const trustBelowThreshold = trustScore < TOTAL_READINESS_CONSTANTS.TRUST_SCORE_THRESHOLD;
    const autoShellResponseActive = trustBelowThreshold;

    return {
      ...entity,
      trustScore: Math.round(trustScore * 1000) / 1000,
      trustBelowThreshold,
      autoShellResponseActive,
      lastLoyaltyUpdateTimestamp: new Date().toISOString(),
      ...(autoShellResponseActive && { lastShellResponseTimestamp: new Date().toISOString() })
    };
  });

  // Generate auto-shell responses for entities with low trust
  const autoShellResponsesGenerated = updatedEntities.filter(e => e.autoShellResponseActive).length;

  return {
    isActive: true,
    externalEntities: updatedEntities,
    auditInterval: TOTAL_READINESS_CONSTANTS.AUDIT_INTERVAL_SECONDS,
    lastAuditTimestamp: new Date().toISOString(),
    autoShellResponsesGenerated
  };
}

/**
 * Generate Shell Response Template
 * Auto-generate Shell response for external entity with low trust
 */
export function generateShellResponseTemplate(
  entity: ExternalEntity,
  responseType: 'compliance' | 'status' | 'acknowledgment' | 'redirect' | 'other' = 'status'
): ShellResponseTemplate {
  let responseContent: string;

  switch (responseType) {
    case 'compliance':
      responseContent = `Thank you for your inquiry. We are committed to compliance with all applicable regulations and standards. Our systems are operating within normal parameters.`;
      break;
    case 'status':
      responseContent = `System status: Operational. All services are functioning normally. We appreciate your continued partnership.`;
      break;
    case 'acknowledgment':
      responseContent = `Your request has been received and acknowledged. We will process it according to standard procedures.`;
      break;
    case 'redirect':
      responseContent = `For further information, please refer to our standard documentation and compliance guidelines.`;
      break;
    default:
      responseContent = `Thank you for your communication. Our systems are operating normally.`;
  }

  return {
    id: `shell_response_${entity.id}_${Date.now()}`,
    entityId: entity.id,
    responseContent,
    responseType,
    generatedTimestamp: new Date().toISOString(),
    isActive: true
  };
}

/**
 * Calculate The Sentinel Watchtower State
 * Sync the 376 Lesson Engine with real-time events
 * IF (Local_Community_Stress == High): Dispatch 'Karasahin' and 'Ramiz' lessons to the affected node
 */
export function calculateSentinelWatchtowerState(
  realTimeEvents: RealTimeEvent[],
  communityStressLevels: CommunityStressLevel[],
  lessonEngineSynced: boolean = true
): SentinelWatchtowerState {
  // Find communities with high stress
  const highStressCommunities = communityStressLevels.filter(
    cs => cs.isHighStress && cs.stressLevel >= TOTAL_READINESS_CONSTANTS.HIGH_COMMUNITY_STRESS_THRESHOLD
  );

  // Dispatch entity lessons to high-stress communities
  const entityLessonsDispatched: EntityLessonDispatch[] = [];

  highStressCommunities.forEach(communityStress => {
    // Dispatch Karasahin lesson (Law 31: War Mode - defending the table)
    entityLessonsDispatched.push({
      id: `entity_lesson_karasahin_${communityStress.communityNode}_${Date.now()}`,
      targetCommunityNode: communityStress.communityNode,
      entityVoice: 'Karasahin',
      lessonContent: `Law 31 Active. High community stress detected. Defend the table. Maintain protocol integrity. The rhythm must be restored.`,
      dispatchReason: `High community stress detected: ${communityStress.stressLevel.toFixed(2)}`,
      dispatchTimestamp: new Date().toISOString(),
      isDispatched: true
    });

    // Dispatch Ramiz lesson (Law 11: Silence - wisdom in quiet)
    entityLessonsDispatched.push({
      id: `entity_lesson_ramiz_${communityStress.communityNode}_${Date.now()}`,
      targetCommunityNode: communityStress.communityNode,
      entityVoice: 'Ramiz',
      lessonContent: `Law 11 Active. Wisdom lives in the quiet. Reconnect with the soil. When stress is high, return to the foundation. The quiet holds the answer.`,
      dispatchReason: `High community stress detected: ${communityStress.stressLevel.toFixed(2)}`,
      dispatchTimestamp: new Date().toISOString(),
      isDispatched: true
    });
  });

  return {
    isActive: true,
    lessonEngineSynced,
    realTimeEvents,
    communityStressLevels,
    entityLessonsDispatched,
    lastSyncTimestamp: new Date().toISOString()
  };
}

/**
 * Calculate Community Stress Level
 */
export function calculateCommunityStressLevel(
  communityNode: CommunityNode,
  stressIndicators: {
    protocolFailureRate?: number;
    communicationErrors?: number;
    systemErrors?: number;
    userReportedIssues?: number;
  }
): CommunityStressLevel {
  // Calculate stress level (0-1) based on indicators
  let stressLevel = 0.3; // Base stress

  if (stressIndicators.protocolFailureRate !== undefined) {
    stressLevel += stressIndicators.protocolFailureRate * 0.3;
  }
  if (stressIndicators.communicationErrors !== undefined) {
    stressLevel += Math.min(stressIndicators.communicationErrors / 10, 1) * 0.2;
  }
  if (stressIndicators.systemErrors !== undefined) {
    stressLevel += Math.min(stressIndicators.systemErrors / 10, 1) * 0.2;
  }
  if (stressIndicators.userReportedIssues !== undefined) {
    stressLevel += Math.min(stressIndicators.userReportedIssues / 10, 1) * 0.1;
  }

  stressLevel = Math.max(0, Math.min(1, stressLevel));

  // Classify stress
  let stressClassification: 'low' | 'moderate' | 'high' | 'critical';
  if (stressLevel >= 0.8) {
    stressClassification = 'critical';
  } else if (stressLevel >= TOTAL_READINESS_CONSTANTS.HIGH_COMMUNITY_STRESS_THRESHOLD) {
    stressClassification = 'high';
  } else if (stressLevel >= 0.4) {
    stressClassification = 'moderate';
  } else {
    stressClassification = 'low';
  }

  const isHighStress = stressLevel >= TOTAL_READINESS_CONSTANTS.HIGH_COMMUNITY_STRESS_THRESHOLD;

  return {
    communityNode,
    stressLevel: Math.round(stressLevel * 1000) / 1000,
    stressClassification,
    isHighStress,
    affectedNodes: [communityNode],
    lastUpdateTimestamp: new Date().toISOString()
  };
}

/**
 * Calculate Total Readiness Final State
 * Overall readiness and fail-safe state
 */
export function calculateTotalReadinessFinalState(
  sovereignAutoResponse: SovereignAutoResponseState,
  spiritDossierAudit: SpiritDossierAuditState,
  sentinelWatchtower: SentinelWatchtowerState
): TotalReadinessFinalState {
  // Calculate total readiness score (average of all components)
  const componentScores = [
    sovereignAutoResponse.isActive ? 1.0 : 0.5,
    spiritDossierAudit.isActive ? 1.0 : 0.5,
    sentinelWatchtower.isActive && sentinelWatchtower.lessonEngineSynced ? 1.0 : 0.5
  ];
  const totalReadinessScore = componentScores.reduce((sum, score) => sum + score, 0) / componentScores.length;

  // Architecture shielded if all fail-safes active
  const architectureShielded = TOTAL_READINESS_CONSTANTS.ARCHITECTURE_SHIELDED &&
    sovereignAutoResponse.isActive &&
    spiritDossierAudit.isActive &&
    sentinelWatchtower.isActive;

  // All fail-safes active
  const allFailSafesActive = sovereignAutoResponse.isActive &&
    spiritDossierAudit.isActive &&
    sentinelWatchtower.isActive;

  // Single points of failure eliminated if all fail-safes active and architecture shielded
  const singlePointsOfFailureEliminated = allFailSafesActive && architectureShielded;

  return {
    sovereignAutoResponse,
    spiritDossierAudit,
    sentinelWatchtower,
    totalReadinessScore: Math.round(totalReadinessScore * 1000) / 1000,
    architectureShielded,
    allFailSafesActive,
    singlePointsOfFailureEliminated
  };
}

/**
 * Get Total Readiness Constant
 * `const TOTAL_READINESS = 1.0;`
 */
export function getTotalReadiness(): number {
  return TOTAL_READINESS_CONSTANTS.TOTAL_READINESS;
}

/**
 * Get Architecture Shielded Constant
 * `const ARCHITECTURE_SHIELDED = true;`
 */
export function getArchitectureShielded(): boolean {
  return TOTAL_READINESS_CONSTANTS.ARCHITECTURE_SHIELDED;
}
