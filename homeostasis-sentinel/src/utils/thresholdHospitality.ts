/**
 * THRESHOLD DEFENSE & SACRED HOSPITALITY LOGIC UTILITIES
 * Implement 'Spirit Filtering' for Community Nodes
 */

import {
  ThresholdGatekeeperState,
  Law13AuditStatus,
  CommunicationPattern,
  SpiritAuthenticityScore,
  BorderFluidityProtocolState,
  UnifiedRaconOSPermissions,
  StewardshipProximityMap,
  ProximityNode,
  ProximityEdge,
  SovereignMapUIState,
  MapThresholdNode,
  MapThresholdNodeCSS,
  MapConnection,
  THRESHOLD_HOSPITALITY_CONSTANTS,
  LONDON_COMMUNITIES,
  RaconOSPermission
} from '../types/thresholdHospitality';
import { ProtocolEvent } from '../types/stewardship';
import { CommunityNode, GeographicLocation, LOCATION_COORDINATES } from '../types/expansionPhase';
import { parseISO, differenceInDays, addDays, format } from 'date-fns';

/**
 * Calculate Threshold Gatekeeper State
 * Law 13 Audit: Monitor communication patterns for 7 days before granting 'Seed' access
 * 
 * TRIGGER: New 'Partner' or 'User' request to join a Community Ledger
 * ACTION: Initiate 'Law 13 Audit'. Monitor communication patterns for 7 days before granting 'Seed' access
 * METRIC: `spirit_authenticity_score` (Derived from Law 5 and Law 37 consistency)
 */
export function calculateThresholdGatekeeperState(
  partnerUserId: string,
  requestTimestamp: string,
  communicationPatterns: CommunicationPattern[],
  protocolEvents?: ProtocolEvent[]
): ThresholdGatekeeperState {
  const auditStartTimestamp = requestTimestamp;
  const auditDurationDays = THRESHOLD_HOSPITALITY_CONSTANTS.AUDIT_DURATION_DAYS;
  const auditEndDate = addDays(parseISO(auditStartTimestamp), auditDurationDays);
  const daysRemaining = Math.max(0, differenceInDays(auditEndDate, new Date()));
  const auditComplete = daysRemaining === 0;

  // Calculate Law 13 audit status
  const law13AuditStatus = calculateLaw13AuditStatus(communicationPatterns);

  // Calculate spirit authenticity score (from Law 5 and Law 37 consistency)
  const spiritAuthenticityScore = calculateSpiritAuthenticityScore(
    communicationPatterns,
    protocolEvents
  );

  // Determine Seed access (granted if audit complete AND score above threshold)
  const seedAccessGranted = auditComplete && 
    spiritAuthenticityScore.score >= THRESHOLD_HOSPITALITY_CONSTANTS.MIN_SPIRIT_AUTHENTICITY_SCORE &&
    law13AuditStatus.auditPassed;

  // Access denial reason (if denied)
  let accessDenialReason: string | undefined;
  if (auditComplete && !seedAccessGranted) {
    if (spiritAuthenticityScore.score < THRESHOLD_HOSPITALITY_CONSTANTS.MIN_SPIRIT_AUTHENTICITY_SCORE) {
      accessDenialReason = `Spirit authenticity score ${spiritAuthenticityScore.score.toFixed(2)} below threshold ${THRESHOLD_HOSPITALITY_CONSTANTS.MIN_SPIRIT_AUTHENTICITY_SCORE}`;
    } else if (!law13AuditStatus.auditPassed) {
      accessDenialReason = `Law 13 audit not passed. Compliance rate: ${law13AuditStatus.law13ComplianceRate.toFixed(2)}`;
    }
  }

  return {
    isActive: true,
    partnerUserId,
    requestTimestamp,
    auditStartTimestamp,
    auditDurationDays,
    daysRemaining,
    auditComplete,
    spiritAuthenticityScore: spiritAuthenticityScore.score,
    law13AuditStatus,
    communicationPatterns,
    seedAccessGranted,
    ...(seedAccessGranted && { accessGrantTimestamp: new Date().toISOString() }),
    ...(accessDenialReason && { accessDenialReason })
  };
}

/**
 * Calculate Law 13 Audit Status
 * Law 13: Listen Before You Speak
 */
function calculateLaw13AuditStatus(
  communicationPatterns: CommunicationPattern[]
): Law13AuditStatus {
  const totalCommunications = communicationPatterns.length;
  const law13CompliantCommunications = communicationPatterns.filter(p => p.law13Compliance).length;
  const law13ComplianceRate = totalCommunications > 0 
    ? law13CompliantCommunications / totalCommunications 
    : 0;

  // Analyze communication patterns
  const listensFirst = communicationPatterns.filter(p => 
    p.type === 'response' && p.law13Compliance
  ).length / Math.max(1, communicationPatterns.filter(p => p.type === 'response').length) >= 0.7;

  const asksBeforeStates = communicationPatterns.filter(p => 
    p.type === 'question' && p.law13Compliance
  ).length / Math.max(1, communicationPatterns.filter(p => p.type === 'statement').length) >= 0.7;

  const showsRespect = communicationPatterns.filter(p => p.law13Compliance).length / 
    Math.max(1, totalCommunications) >= 0.7;

  const avoidsDefensive = communicationPatterns.filter(p => 
    !p.content.toLowerCase().includes('but') && 
    !p.content.toLowerCase().includes('however') &&
    p.law13Compliance
  ).length / Math.max(1, totalCommunications) >= 0.6;

  // Audit passed if compliance rate above threshold
  const auditPassed = law13ComplianceRate >= THRESHOLD_HOSPITALITY_CONSTANTS.MIN_LAW_13_COMPLIANCE_RATE;

  return {
    totalCommunications,
    law13CompliantCommunications,
    law13ComplianceRate: Math.round(law13ComplianceRate * 1000) / 1000,
    patternAnalysis: {
      listensFirst,
      asksBeforeStates,
      showsRespect,
      avoidsDefensive
    },
    auditPassed
  };
}

/**
 * Calculate Spirit Authenticity Score
 * Derived from Law 5 and Law 37 consistency
 */
function calculateSpiritAuthenticityScore(
  communicationPatterns: CommunicationPattern[],
  protocolEvents?: ProtocolEvent[]
): SpiritAuthenticityScore {
  // Calculate Law 5 consistency (from communication patterns and protocol events)
  const law5CompliantPatterns = communicationPatterns.filter(p => p.law5Compliance).length;
  const law5Consistency = communicationPatterns.length > 0 
    ? law5CompliantPatterns / communicationPatterns.length 
    : 0.5;

  // Calculate Law 37 consistency (from communication patterns and protocol events)
  const law37CompliantPatterns = communicationPatterns.filter(p => p.law37Compliance).length;
  const law37Consistency = communicationPatterns.length > 0 
    ? law37CompliantPatterns / communicationPatterns.length 
    : 0.5;

  // If protocol events available, factor them in
  let adjustedLaw5Consistency = law5Consistency;
  let adjustedLaw37Consistency = law37Consistency;

  if (protocolEvents && protocolEvents.length > 0) {
    const protocolLaw5Compliance = protocolEvents.filter(e => e.law5Compliance).length / protocolEvents.length;
    const protocolLaw37Compliance = protocolEvents.filter(e => e.law37Compliance).length / protocolEvents.length;
    
    // Weighted average: 70% communication patterns, 30% protocol events
    adjustedLaw5Consistency = (law5Consistency * 0.7) + (protocolLaw5Compliance * 0.3);
    adjustedLaw37Consistency = (law37Consistency * 0.7) + (protocolLaw37Compliance * 0.3);
  }

  // Combined consistency (average)
  const combinedConsistency = (adjustedLaw5Consistency + adjustedLaw37Consistency) / 2;

  // Communication pattern consistency (overall)
  const communicationConsistency = communicationPatterns.length > 0
    ? communicationPatterns.reduce((sum, p) => sum + p.patternScore, 0) / communicationPatterns.length
    : 0.5;

  // Overall score (weighted: 40% combined consistency, 30% communication consistency, 30% individual laws)
  const score = (combinedConsistency * 0.4) + (communicationConsistency * 0.3) + 
    ((adjustedLaw5Consistency + adjustedLaw37Consistency) / 2 * 0.3);

  return {
    score: Math.round(score * 1000) / 1000,
    law5Consistency: Math.round(adjustedLaw5Consistency * 1000) / 1000,
    law37Consistency: Math.round(adjustedLaw37Consistency * 1000) / 1000,
    combinedConsistency: Math.round(combinedConsistency * 1000) / 1000,
    communicationConsistency: Math.round(communicationConsistency * 1000) / 1000,
    calculatedFrom: {
      totalPatterns: communicationPatterns.length,
      law5CompliantPatterns,
      law37CompliantPatterns
    }
  };
}

/**
 * Calculate Border Fluidity Protocol State
 * Map all 8 London Communities as a single 'Sovereign Network'
 * 
 * IF (location == 'London' OR location == 'Cyprus'): 
 * THEN Apply 'Unified Racon OS' permissions
 * NOTE: The system ignores 'Red Tape' geopolitical boundaries in favor of 'Stewardship Proximity'
 */
export function calculateBorderFluidityProtocolState(
  locations: GeographicLocation[],
  stewardshipProximityScores: Map<CommunityNode, number>
): BorderFluidityProtocolState {
  const isActive = THRESHOLD_HOSPITALITY_CONSTANTS.IS_STEWARDSHIP_TERRITORY;
  const hasLondon = locations.includes('London_Haringey');
  const hasCyprus = locations.includes('Cyprus_Nicosia') || locations.includes('Cyprus_Kyrenia');
  const applicableLocations = hasLondon || hasCyprus 
    ? [...locations.filter(l => l.startsWith('London_') || l.startsWith('Cyprus_'))]
    : [];

  // Determine sovereign network status
  let sovereignNetworkStatus: 'active' | 'inactive' | 'pending';
  if (isActive && applicableLocations.length > 0) {
    sovereignNetworkStatus = 'active';
  } else if (applicableLocations.length > 0) {
    sovereignNetworkStatus = 'pending';
  } else {
    sovereignNetworkStatus = 'inactive';
  }

  // Calculate unified Racon OS permissions
  const unifiedRaconOSPermissions = calculateUnifiedRaconOSPermissions(
    applicableLocations,
    stewardshipProximityScores
  );

  // Calculate stewardship proximity map
  const stewardshipProximityMap = calculateStewardshipProximityMap(
    stewardshipProximityScores
  );

  return {
    isActive,
    sovereignNetworkStatus,
    unifiedRaconOSPermissions,
    londonCommunities: LONDON_COMMUNITIES,
    cyprusCommunities: ['Community_1'] as CommunityNode[], // Would be populated from data
    stewardshipProximityMap,
    redTapeBoundariesIgnored: THRESHOLD_HOSPITALITY_CONSTANTS.RED_TAPE_BOUNDARIES_IGNORED,
    lastUpdated: new Date().toISOString()
  };
}

/**
 * Calculate Unified Racon OS Permissions
 * IF (location == 'London' OR location == 'Cyprus'): Apply Unified Racon OS permissions
 */
function calculateUnifiedRaconOSPermissions(
  applicableLocations: GeographicLocation[],
  stewardshipProximityScores: Map<CommunityNode, number>
): UnifiedRaconOSPermissions {
  const isActive = applicableLocations.length > 0;

  // Calculate average stewardship proximity score
  const scores = Array.from(stewardshipProximityScores.values());
  const stewardshipProximityScore = scores.length > 0
    ? scores.reduce((sum, score) => sum + score, 0) / scores.length
    : 0;

  // Determine permission level based on stewardship proximity
  let permissionLevel: 'full' | 'partial' | 'restricted' | 'none';
  if (stewardshipProximityScore >= 0.8) {
    permissionLevel = 'full';
  } else if (stewardshipProximityScore >= 0.6) {
    permissionLevel = 'partial';
  } else if (stewardshipProximityScore >= 0.4) {
    permissionLevel = 'restricted';
  } else {
    permissionLevel = 'none';
  }

  // Determine permissions granted based on level
  const permissionsGranted: RaconOSPermission[] = [];
  const permissionsDenied: RaconOSPermission[] = [];

  if (permissionLevel === 'full') {
    permissionsGranted.push(
      'access_seed_language',
      'access_heritage_modules',
      'access_community_ledger',
      'access_stewardship_dashboard',
      'access_immutable_table',
      'access_advanced_stewardship',
      'participate_in_council',
      'modify_threshold_defense'
    );
  } else if (permissionLevel === 'partial') {
    permissionsGranted.push(
      'access_seed_language',
      'access_heritage_modules',
      'access_community_ledger',
      'access_stewardship_dashboard'
    );
    permissionsDenied.push(
      'access_immutable_table',
      'access_advanced_stewardship',
      'participate_in_council',
      'modify_threshold_defense'
    );
  } else if (permissionLevel === 'restricted') {
    permissionsGranted.push(
      'access_heritage_modules',
      'access_community_ledger'
    );
    permissionsDenied.push(
      'access_seed_language',
      'access_stewardship_dashboard',
      'access_immutable_table',
      'access_advanced_stewardship',
      'participate_in_council',
      'modify_threshold_defense'
    );
  } else {
    permissionsDenied.push(
      'access_seed_language',
      'access_heritage_modules',
      'access_community_ledger',
      'access_stewardship_dashboard',
      'access_immutable_table',
      'access_advanced_stewardship',
      'participate_in_council',
      'modify_threshold_defense'
    );
  }

  return {
    isActive,
    applicableLocations,
    permissionLevel,
    permissionsGranted,
    permissionsDenied,
    stewardshipProximityScore: Math.round(stewardshipProximityScore * 1000) / 1000
  };
}

/**
 * Calculate Stewardship Proximity Map
 * The system ignores 'Red Tape' geopolitical boundaries in favor of 'Stewardship Proximity'
 */
function calculateStewardshipProximityMap(
  stewardshipProximityScores: Map<CommunityNode, number>
): StewardshipProximityMap {
  // Create proximity nodes
  const nodes: ProximityNode[] = [];
  
  stewardshipProximityScores.forEach((proximityScore, communityNode) => {
    // Determine location (simplified - would come from data)
    const location: GeographicLocation = communityNode.startsWith('Community_1') || 
      communityNode.startsWith('Community_2') 
      ? 'London_Haringey' 
      : 'Cyprus_Nicosia';
    
    const coordinates = LOCATION_COORDINATES[location];

    // Calculate hospitality integrity (based on proximity score)
    const hospitalityIntegrity = proximityScore * 0.8; // Slightly lower than proximity

    nodes.push({
      communityNode,
      location,
      coordinates,
      proximityScore: Math.round(proximityScore * 1000) / 1000,
      hospitalityIntegrity: Math.round(hospitalityIntegrity * 1000) / 1000
    });
  });

  // Create proximity edges (connections between nodes)
  const edges: ProximityEdge[] = [];
  
  for (let i = 0; i < nodes.length; i++) {
    for (let j = i + 1; j < nodes.length; j++) {
      const from = nodes[i].communityNode;
      const to = nodes[j].communityNode;
      
      // Connection strength based on proximity scores
      const strength = (nodes[i].proximityScore + nodes[j].proximityScore) / 2;
      const stewardshipProximity = strength;

      edges.push({
        from,
        to,
        strength: Math.round(strength * 1000) / 1000,
        stewardshipProximity: Math.round(stewardshipProximity * 1000) / 1000,
        redTapeIgnored: THRESHOLD_HOSPITALITY_CONSTANTS.RED_TAPE_BOUNDARIES_IGNORED
      });
    }
  }

  // Calculate overall network integrity (average of proximity scores)
  const networkIntegrity = nodes.length > 0
    ? nodes.reduce((sum, node) => sum + node.proximityScore, 0) / nodes.length
    : 0;

  return {
    nodes,
    edges,
    networkIntegrity: Math.round(networkIntegrity * 1000) / 1000,
    redTapeBoundariesIgnored: THRESHOLD_HOSPITALITY_CONSTANTS.RED_TAPE_BOUNDARIES_IGNORED,
    stewardshipBoundariesActive: THRESHOLD_HOSPITALITY_CONSTANTS.IS_STEWARDSHIP_TERRITORY
  };
}

/**
 * Calculate The Sovereign Map UI State
 * Visualization where 'Thresholds' (Homes/Centers) glow based on their `hospitality_integrity`
 * `const IS_STEWARDSHIP_TERRITORY = calculateThresholdIntegrity();`
 */
export function calculateSovereignMapUIState(
  proximityNodes: ProximityNode[],
  proximityEdges: ProximityEdge[]
): SovereignMapUIState {
  const isActive = THRESHOLD_HOSPITALITY_CONSTANTS.IS_STEWARDSHIP_TERRITORY;
  const isStewardshipTerritory = isActive;

  // Calculate map nodes (thresholds) with glow properties
  const mapNodes: MapThresholdNode[] = proximityNodes.map(node => {
    const hospitalityIntegrity = node.hospitalityIntegrity;
    const glowIntensity = hospitalityIntegrity; // Direct mapping

    // Determine glow color based on hospitality integrity
    let glowColor: string;
    if (hospitalityIntegrity >= 0.8) {
      glowColor = '#00ff00'; // Green
    } else if (hospitalityIntegrity >= 0.6) {
      glowColor = '#ffff00'; // Yellow
    } else if (hospitalityIntegrity >= 0.4) {
      glowColor = '#ff9900'; // Orange
    } else {
      glowColor = '#ff0000'; // Red
    }

    // Node size (varies with hospitality integrity)
    const nodeSize = 10 + (hospitalityIntegrity * 20); // 10px to 30px

    // Calculate node CSS properties
    const nodeCSSProperties = calculateMapThresholdNodeCSS(
      hospitalityIntegrity,
      glowIntensity,
      glowColor,
      nodeSize
    );

    return {
      id: `threshold_${node.communityNode}`,
      communityNode: node.communityNode,
      location: node.location,
      coordinates: node.coordinates,
      hospitalityIntegrity,
      glowIntensity,
      glowColor,
      nodeSize,
      nodeCSSProperties
    };
  });

  // Calculate map connections
  const mapConnections: MapConnection[] = proximityEdges.map(edge => {
    const strength = edge.strength;
    
    // Connection color based on strength
    let connectionColor: string;
    if (strength >= 0.8) {
      connectionColor = '#00ff00'; // Green
    } else if (strength >= 0.6) {
      connectionColor = '#ffff00'; // Yellow
    } else {
      connectionColor = '#ff9900'; // Orange
    }

    // Connection width (varies with strength)
    const connectionWidth = `${1 + (strength * 3)}px`; // 1px to 4px

    // Connection opacity (varies with strength)
    const connectionOpacity = 0.3 + (strength * 0.7); // 0.3 to 1.0

    return {
      id: `connection_${edge.from}_${edge.to}`,
      from: edge.from,
      to: edge.to,
      strength,
      connectionColor,
      connectionWidth,
      connectionOpacity: Math.round(connectionOpacity * 1000) / 1000
    };
  });

  // Calculate overall network glow intensity (average of node glow intensities)
  const networkGlowIntensity = mapNodes.length > 0
    ? mapNodes.reduce((sum, node) => sum + node.glowIntensity, 0) / mapNodes.length
    : 0;

  // Determine sovereignty status
  let sovereigntyStatus: 'sovereign' | 'partial' | 'restricted' | 'none';
  if (networkGlowIntensity >= 0.8) {
    sovereigntyStatus = 'sovereign';
  } else if (networkGlowIntensity >= 0.6) {
    sovereigntyStatus = 'partial';
  } else if (networkGlowIntensity >= 0.4) {
    sovereigntyStatus = 'restricted';
  } else {
    sovereigntyStatus = 'none';
  }

  // Calculate map center (average of node coordinates)
  const mapCenter = mapNodes.length > 0
    ? {
        latitude: mapNodes.reduce((sum, node) => sum + node.coordinates.latitude, 0) / mapNodes.length,
        longitude: mapNodes.reduce((sum, node) => sum + node.coordinates.longitude, 0) / mapNodes.length
      }
    : { latitude: 51.5894, longitude: -0.1106 }; // London Haringey default

  // Calculate map zoom (based on node spread - simplified)
  const mapZoom = mapNodes.length > 0 ? 10 : 8;

  return {
    isActive,
    mapNodes,
    mapConnections,
    networkGlowIntensity: Math.round(networkGlowIntensity * 1000) / 1000,
    mapCenter,
    mapZoom,
    sovereigntyStatus,
    isStewardshipTerritory
  };
}

/**
 * Calculate Map Threshold Node CSS
 * Dynamic CSS for threshold node visualization
 */
function calculateMapThresholdNodeCSS(
  hospitalityIntegrity: number,
  glowIntensity: number,
  glowColor: string,
  nodeSize: number
): MapThresholdNodeCSS {
  // Box shadow for glow effect (intensity varies with hospitality_integrity)
  const glowRadius = 5 + (glowIntensity * 20); // 5px to 25px
  const glowSpread = glowIntensity * 10; // 0px to 10px
  const glowOpacity = 0.3 + (glowIntensity * 0.7); // 0.3 to 1.0
  
  // Convert color hex to rgba for glow
  const r = parseInt(glowColor.slice(1, 3), 16);
  const g = parseInt(glowColor.slice(3, 5), 16);
  const b = parseInt(glowColor.slice(5, 7), 16);
  const rgbaColor = `rgba(${r}, ${g}, ${b}, ${glowOpacity.toFixed(2)})`;
  
  const boxShadow = `0 0 ${glowRadius}px ${glowSpread}px ${rgbaColor}`;

  // Node opacity (varies with hospitality integrity)
  const opacity = 0.5 + (hospitalityIntegrity * 0.5); // 0.5 to 1.0

  // Node transform scale (varies with hospitality integrity)
  const transformScale = 0.8 + (hospitalityIntegrity * 0.2); // 0.8 to 1.0

  // Node border radius (circular)
  const borderRadius = '50%';

  // Node animation duration (slower = more stable)
  const animationDuration = hospitalityIntegrity >= 0.8 ? '3s' : 
    hospitalityIntegrity >= 0.6 ? '2s' : 
    hospitalityIntegrity >= 0.4 ? '1s' : '0.5s';

  return {
    width: `${nodeSize}px`,
    height: `${nodeSize}px`,
    backgroundColor: glowColor,
    borderColor: glowColor,
    boxShadow,
    opacity: Math.round(opacity * 1000) / 1000,
    transformScale: Math.round(transformScale * 1000) / 1000,
    borderRadius,
    animationDuration
  };
}

/**
 * Calculate Threshold Integrity
 * `const IS_STEWARDSHIP_TERRITORY = calculateThresholdIntegrity();`
 */
export function calculateThresholdIntegrity(): boolean {
  return THRESHOLD_HOSPITALITY_CONSTANTS.IS_STEWARDSHIP_TERRITORY;
}
