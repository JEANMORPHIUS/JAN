/**
 * THRESHOLD DEFENSE & SACRED HOSPITALITY LOGIC TYPES
 * Implement 'Spirit Filtering' for Community Nodes
 * 
 * Components:
 * - Threshold_Gatekeeper: Law 13 Audit for new partners/users
 * - Border_Fluidity_Protocol: 8 London Communities as Sovereign Network
 * - The Sovereign Map: Thresholds glow based on hospitality_integrity
 */

import { ProtocolEvent } from './stewardship';
import { CommunityNode, GeographicLocation } from './expansionPhase';

/**
 * Threshold Gatekeeper State
 * Law 13 Audit: Monitor communication patterns for 7 days before granting 'Seed' access
 */
export interface ThresholdGatekeeperState {
  /** Is gatekeeper active? */
  isActive: boolean;
  /** Partner/User ID */
  partnerUserId: string;
  /** Request timestamp */
  requestTimestamp: string;
  /** Audit start timestamp */
  auditStartTimestamp: string;
  /** Audit duration (7 days) */
  auditDurationDays: number;
  /** Days remaining in audit */
  daysRemaining: number;
  /** Is audit complete? */
  auditComplete: boolean;
  /** Spirit authenticity score (0-1) - Derived from Law 5 and Law 37 consistency */
  spiritAuthenticityScore: number;
  /** Law 13 audit status */
  law13AuditStatus: Law13AuditStatus;
  /** Communication patterns monitored */
  communicationPatterns: CommunicationPattern[];
  /** Seed access granted? */
  seedAccessGranted: boolean;
  /** Access grant timestamp */
  accessGrantTimestamp?: string;
  /** Access denial reason (if denied) */
  accessDenialReason?: string;
}

/**
 * Law 13 Audit Status
 * Law 13: Listen Before You Speak
 */
export interface Law13AuditStatus {
  /** Total communications monitored */
  totalCommunications: number;
  /** Communications showing Law 13 compliance (listening before speaking) */
  law13CompliantCommunications: number;
  /** Law 13 compliance rate (0-1) */
  law13ComplianceRate: number;
  /** Communication pattern analysis */
  patternAnalysis: {
    /** Listens before responding */
    listensFirst: boolean;
    /** Asks questions before making statements */
    asksBeforeStates: boolean;
    /** Shows respect in communication */
    showsRespect: boolean;
    /** Avoids defensive communication */
    avoidsDefensive: boolean;
  };
  /** Law 13 audit passed? */
  auditPassed: boolean;
}

/**
 * Communication Pattern
 * Monitored communication event during 7-day audit
 */
export interface CommunicationPattern {
  /** Pattern ID */
  id: string;
  /** Pattern timestamp */
  timestamp: string;
  /** Communication type */
  type: 'message' | 'response' | 'question' | 'statement' | 'action';
  /** Pattern content */
  content: string;
  /** Law 13 compliance detected? */
  law13Compliance: boolean;
  /** Law 5 compliance detected? (Word is Bond) */
  law5Compliance: boolean;
  /** Law 37 compliance detected? (Finish What You Begin) */
  law37Compliance: boolean;
  /** Pattern score (0-1) */
  patternScore: number;
}

/**
 * Spirit Authenticity Score
 * Derived from Law 5 and Law 37 consistency
 */
export interface SpiritAuthenticityScore {
  /** Overall score (0-1) */
  score: number;
  /** Law 5 consistency (0-1) - Word is Bond */
  law5Consistency: number;
  /** Law 37 consistency (0-1) - Finish What You Begin */
  law37Consistency: number;
  /** Combined consistency (0-1) */
  combinedConsistency: number;
  /** Communication pattern consistency */
  communicationConsistency: number;
  /** Calculated from communication patterns */
  calculatedFrom: {
    totalPatterns: number;
    law5CompliantPatterns: number;
    law37CompliantPatterns: number;
  };
}

/**
 * Border Fluidity Protocol State
 * Map all 8 London Communities as a single 'Sovereign Network'
 */
export interface BorderFluidityProtocolState {
  /** Is protocol active? */
  isActive: boolean;
  /** Sovereign network status */
  sovereignNetworkStatus: 'active' | 'inactive' | 'pending';
  /** Unified Racon OS permissions */
  unifiedRaconOSPermissions: UnifiedRaconOSPermissions;
  /** London communities (8) */
  londonCommunities: CommunityNode[];
  /** Cyprus communities */
  cyprusCommunities: CommunityNode[];
  /** Stewardship proximity map */
  stewardshipProximityMap: StewardshipProximityMap;
  /** Red tape boundaries ignored? */
  redTapeBoundariesIgnored: boolean;
  /** Last updated timestamp */
  lastUpdated?: string;
}

/**
 * Unified Racon OS Permissions
 * IF (location == 'London' OR location == 'Cyprus'): Apply Unified Racon OS permissions
 */
export interface UnifiedRaconOSPermissions {
  /** Is unified permissions active? */
  isActive: boolean;
  /** Applicable locations */
  applicableLocations: GeographicLocation[];
  /** Permission level */
  permissionLevel: 'full' | 'partial' | 'restricted' | 'none';
  /** Permissions granted */
  permissionsGranted: RaconOSPermission[];
  /** Permissions denied */
  permissionsDenied: RaconOSPermission[];
  /** Stewardship proximity score (0-1) */
  stewardshipProximityScore: number;
}

/**
 * Racon OS Permission
 */
export type RaconOSPermission = 
  | 'access_seed_language'
  | 'access_heritage_modules'
  | 'access_community_ledger'
  | 'access_stewardship_dashboard'
  | 'access_immutable_table'
  | 'access_advanced_stewardship'
  | 'participate_in_council'
  | 'modify_threshold_defense';

/**
 * Stewardship Proximity Map
 * The system ignores 'Red Tape' geopolitical boundaries in favor of 'Stewardship Proximity'
 */
export interface StewardshipProximityMap {
  /** Network nodes */
  nodes: ProximityNode[];
  /** Network edges (connections) */
  edges: ProximityEdge[];
  /** Overall network integrity (0-1) */
  networkIntegrity: number;
  /** Red tape boundaries ignored */
  redTapeBoundariesIgnored: boolean;
  /** Stewardship boundaries active */
  stewardshipBoundariesActive: boolean;
}

/**
 * Proximity Node
 * Community node with stewardship proximity
 */
export interface ProximityNode {
  /** Community node */
  communityNode: CommunityNode;
  /** Geographic location */
  location: GeographicLocation;
  /** Coordinates */
  coordinates: {
    latitude: number;
    longitude: number;
  };
  /** Stewardship proximity score (0-1) */
  proximityScore: number;
  /** Hospitality integrity (0-1) */
  hospitalityIntegrity: number;
}

/**
 * Proximity Edge
 * Connection between community nodes
 */
export interface ProximityEdge {
  /** Source node */
  from: CommunityNode;
  /** Target node */
  to: CommunityNode;
  /** Connection strength (0-1) */
  strength: number;
  /** Stewardship proximity (0-1) */
  stewardshipProximity: number;
  /** Red tape ignored? */
  redTapeIgnored: boolean;
}

/**
 * The Sovereign Map UI State
 * Visualization where 'Thresholds' (Homes/Centers) glow based on their `hospitality_integrity`
 */
export interface SovereignMapUIState {
  /** Is map active? */
  isActive: boolean;
  /** Map nodes (thresholds) */
  mapNodes: MapThresholdNode[];
  /** Map connections */
  mapConnections: MapConnection[];
  /** Overall network glow intensity (0-1) */
  networkGlowIntensity: number;
  /** Map center */
  mapCenter: {
    latitude: number;
    longitude: number;
  };
  /** Map zoom level */
  mapZoom: number;
  /** Sovereignty status */
  sovereigntyStatus: 'sovereign' | 'partial' | 'restricted' | 'none';
  /** Stewardship territory status */
  isStewardshipTerritory: boolean;
}

/**
 * Map Threshold Node
 * Threshold (Home/Center) on the Sovereign Map
 */
export interface MapThresholdNode {
  /** Node ID */
  id: string;
  /** Community node */
  communityNode: CommunityNode;
  /** Location */
  location: GeographicLocation;
  /** Coordinates */
  coordinates: {
    latitude: number;
    longitude: number;
  };
  /** Hospitality integrity (0-1) */
  hospitalityIntegrity: number;
  /** Glow intensity (0-1) - based on hospitality_integrity */
  glowIntensity: number;
  /** Glow color (CSS color) */
  glowColor: string;
  /** Node size (CSS size) */
  nodeSize: number;
  /** Node CSS properties */
  nodeCSSProperties: MapThresholdNodeCSS;
}

/**
 * Map Threshold Node CSS
 * Dynamic CSS for threshold node visualization
 */
export interface MapThresholdNodeCSS {
  /** Node width (CSS width) */
  width: string;  // e.g., '20px'
  /** Node height (CSS height) */
  height: string;  // e.g., '20px'
  /** Node background color (CSS background-color) */
  backgroundColor: string;  // e.g., '#00ff00'
  /** Node border color (CSS border-color) */
  borderColor: string;  // e.g., '#00ff00'
  /** Node box shadow (CSS box-shadow) - glow effect */
  boxShadow: string;  // e.g., '0 0 20px rgba(0, 255, 0, 0.8)'
  /** Node opacity (CSS opacity) */
  opacity: number;  // 0-1
  /** Node transform scale (CSS transform scale) */
  transformScale: number;  // e.g., 1.0
  /** Node border radius (CSS border-radius) */
  borderRadius: string;  // e.g., '50%'
  /** Node animation duration (CSS animation-duration) */
  animationDuration: string;  // e.g., '2s'
}

/**
 * Map Connection
 * Connection between thresholds on the Sovereign Map
 */
export interface MapConnection {
  /** Connection ID */
  id: string;
  /** Source node */
  from: CommunityNode;
  /** Target node */
  to: CommunityNode;
  /** Connection strength (0-1) */
  strength: number;
  /** Connection color (CSS color) */
  connectionColor: string;
  /** Connection width (CSS width) */
  connectionWidth: string;  // e.g., '2px'
  /** Connection opacity (CSS opacity) */
  connectionOpacity: number;  // 0-1
}

/**
 * Constants
 */
export const THRESHOLD_HOSPITALITY_CONSTANTS = {
  /** Audit duration (7 days) */
  AUDIT_DURATION_DAYS: 7,
  /** Minimum spirit authenticity score for Seed access (0.7) */
  MIN_SPIRIT_AUTHENTICITY_SCORE: 0.7,
  /** Minimum Law 13 compliance rate (0.7) */
  MIN_LAW_13_COMPLIANCE_RATE: 0.7,
  /** Stewardship territory flag */
  IS_STEWARDSHIP_TERRITORY: true,
  /** Stewardship proximity threshold (0.7) */
  STEWARDSHIP_PROXIMITY_THRESHOLD: 0.7,
  /** Red tape boundaries ignored flag */
  RED_TAPE_BOUNDARIES_IGNORED: true
} as const;

/**
 * London Communities (8)
 */
export const LONDON_COMMUNITIES: CommunityNode[] = [
  'Community_1',
  'Community_2',
  'Community_3',
  'Community_4',
  'Community_5',
  'Community_6',
  'Community_7',
  'Community_8'
] as const;
