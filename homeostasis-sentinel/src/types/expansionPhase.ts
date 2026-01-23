/**
 * EXPANSION PHASE ARCHITECTURE (WEEKS 2-5) TYPES
 * Scale the Stewardship System from Bio-Data to Geo-Cultural Data
 * 
 * Components:
 * - Global Braid API: Lunar/Solar/Seasonal cycles for London (Haringey) and Cyprus (Nicosia/Kyrenia)
 * - Community_Integrity_Ledger: Multi-tenant DB for 8 Communities
 * - Threshold_Defense_v2: Shell_Masking for Seed data translation
 * - Stewardship_Alert_System: Unified Council Alert for low scores
 */

import { HealthMetrics } from './index';
import { EarthAlignment } from './earthAlignment';
import { ProtocolEvent } from './stewardship';

/**
 * Geographic Locations
 */
export type GeographicLocation = 'London_Haringey' | 'Cyprus_Nicosia' | 'Cyprus_Kyrenia';

/**
 * Community Node
 */
export type CommunityNode = 
  | 'Community_1'
  | 'Community_2'
  | 'Community_3'
  | 'Community_4'
  | 'Community_5'
  | 'Community_6'
  | 'Community_7'
  | 'Community_8';

/**
 * Global Braid API Data
 * Integrate Lunar/Solar/Seasonal cycles for London (Haringey) and Cyprus (Nicosia/Kyrenia)
 */
export interface GlobalBraidAPIData {
  /** Geographic location */
  location: GeographicLocation;
  /** Location coordinates */
  coordinates: {
    latitude: number;
    longitude: number;
    timezone: string;
  };
  /** Current Earth alignment for location */
  earthAlignment: EarthAlignment;
  /** Local solar cycle */
  localSolarCycle: LocalSolarCycle;
  /** Local lunar cycle */
  localLunarCycle: LocalLunarCycle;
  /** Local seasonal cycle */
  localSeasonalCycle: LocalSeasonalCycle;
  /** Cultural rhythm cycles */
  culturalRhythmCycles: CulturalRhythmCycles;
  /** Timestamp */
  timestamp: string;
}

/**
 * Local Solar Cycle
 */
export interface LocalSolarCycle {
  /** Sunrise time (local) */
  sunrise: string;
  /** Sunset time (local) */
  sunset: string;
  /** Solar window (local hours) */
  solarWindow: {
    start: number;  // Hour (e.g., 10)
    end: number;    // Hour (e.g., 18)
  };
  /** Solar intensity (0-100) */
  solarIntensity: number;
  /** Current phase */
  phase: 'sunrise' | 'solar_peak' | 'sunset' | 'night';
}

/**
 * Local Lunar Cycle
 */
export interface LocalLunarCycle {
  /** Lunar phase */
  phase: 'new_moon' | 'waxing' | 'full_moon' | 'waning';
  /** Days from new moon */
  daysFromNewMoon: number;
  /** Lunar intensity (0-100) */
  lunarIntensity: number;
}

/**
 * Local Seasonal Cycle
 */
export interface LocalSeasonalCycle {
  /** Current season */
  season: 'winter' | 'spring' | 'summer' | 'autumn';
  /** Day of year */
  dayOfYear: number;
  /** Seasonal intensity (0-100) */
  seasonalIntensity: number;
  /** Local seasonal characteristics */
  localCharacteristics: string;
}

/**
 * Cultural Rhythm Cycles
 * Sync `biological_temple_data` with `cultural_rhythm_cycles`
 */
export interface CulturalRhythmCycles {
  /** Cultural sync score (0-100) */
  culturalSyncScore: number;
  /** Local cultural rhythms */
  localRhythms: {
    /** Daily rhythms (e.g., prayer times, meal times) */
    daily: string[];
    /** Weekly rhythms (e.g., Friday prayers, Sunday gatherings) */
    weekly: string[];
    /** Monthly rhythms (e.g., festivals, celebrations) */
    monthly: string[];
    /** Seasonal rhythms (e.g., harvest, planting) */
    seasonal: string[];
  };
  /** Biological-cultural alignment */
  biologicalCulturalAlignment: number;  // 0-100
}

/**
 * Community Integrity Ledger Entry
 * Multi-tenant DB structure for the 8 Communities
 */
export interface CommunityIntegrityLedgerEntry {
  /** Community node ID */
  communityNode: CommunityNode;
  /** Entry ID */
  id: string;
  /** Entry timestamp */
  timestamp: string;
  /** Racon Compliance (Laws 1-40) */
  raconCompliance: RaconCompliance;
  /** Symbiosis Score (Health) of territory (0-100) */
  symbiosisScore: number;
  /** Community health status */
  healthStatus: 'optimal' | 'stable' | 'attention' | 'crisis';
  /** Geographic location */
  location: GeographicLocation;
  /** Biological temple data */
  biologicalTempleData: BiologicalTempleData;
  /** Cultural rhythm cycles */
  culturalRhythmCycles: CulturalRhythmCycles;
  /** Community stewardship score (0-100) */
  stewardshipScore: number;
}

/**
 * Racon Compliance
 * Track 'Racon Compliance' (Laws 1-40) for each community node
 */
export interface RaconCompliance {
  /** Total laws (40) */
  totalLaws: number;
  /** Laws compliant */
  lawsCompliant: number;
  /** Compliance rate (0-1) */
  complianceRate: number;
  /** Compliance by volume */
  complianceByVolume: {
    /** Loyalty (Laws 1-10) */
    loyalty: number;     // 0-1
    /** Silence (Laws 11-20) */
    silence: number;     // 0-1
    /** Respect (Laws 21-30) */
    respect: number;     // 0-1
    /** War (Laws 31-40) */
    war: number;        // 0-1
  };
  /** Non-compliant laws */
  nonCompliantLaws: number[];
  /** Last compliance check */
  lastComplianceCheck: string;
}

/**
 * Biological Temple Data
 * Sync with cultural rhythm cycles
 */
export interface BiologicalTempleData {
  /** Average glucose (mmol/L) */
  averageGlucose: number;
  /** Average vision clarity (1-10) */
  averageVisionClarity: number;
  /** Average muscle tension (1-10) */
  averageMuscleTension: number;
  /** Average breath quality (1-10) */
  averageBreathQuality: number;
  /** Bio-homeostasis score (0-1) */
  bioHomeostasis: number;
  /** Data point count */
  dataPointCount: number;
}

/**
 * Community Integrity Ledger
 * Multi-tenant DB structure
 */
export interface CommunityIntegrityLedger {
  /** All community entries */
  entries: CommunityIntegrityLedgerEntry[];
  /** Entries by community node */
  entriesByCommunity: Record<CommunityNode, CommunityIntegrityLedgerEntry[]>;
  /** Current symbiosis scores by community */
  symbiosisScoresByCommunity: Record<CommunityNode, number>;
  /** Overall community health map */
  healthMap: Record<CommunityNode, 'optimal' | 'stable' | 'attention' | 'crisis'>;
  /** Total communities */
  totalCommunities: number;
  /** Average symbiosis score */
  averageSymbiosisScore: number;
}

/**
 * Threshold Defense v2 State
 * Shell_Masking: Automatically translate 'Seed' data into 'Standard Compliance' language
 */
export interface ThresholdDefenseV2State {
  /** Is internal sacred mode active? */
  is_internal_sacred: boolean;
  /** Shell masking active? */
  shellMaskingActive: boolean;
  /** Seed data original */
  seedData: any;
  /** Shell data translated */
  shellData: any;
  /** Translation rules applied */
  translationRules: string[];
  /** Threshold integrity */
  thresholdIntegrity: number;
  /** Last masking timestamp */
  lastMaskingTimestamp?: string;
}

/**
 * Shell Masking Translation Rule
 */
export interface ShellMaskingRule {
  /** Seed language pattern */
  seedPattern: string | RegExp;
  /** Shell language replacement */
  shellReplacement: string;
  /** Rule description */
  description: string;
  /** Law reference */
  lawReference?: string;
}

/**
 * Stewardship Alert System State
 * Unified Council Alert for low scores
 */
export interface StewardshipAlertSystem {
  /** Is alert active? */
  isAlertActive: boolean;
  /** Alert type */
  alertType: 'Community_Low' | 'Bio_Homeostasis_Low' | 'Both' | 'None';
  /** Alert severity */
  severity: 'low' | 'medium' | 'high' | 'critical';
  /** Triggered conditions */
  triggeredConditions: {
    /** Community score < 0.5 */
    communityScoreLow: boolean;
    /** Bio homeostasis < 0.7 */
    bioHomeostasisLow: boolean;
  };
  /** Alert values */
  alertValues: {
    /** Current community score */
    communityScore: number;
    /** Current bio homeostasis */
    bioHomeostasis: number;
  };
  /** Unified Council Alert */
  unifiedCouncilAlert?: UnifiedCouncilAlert;
  /** Alert timestamp */
  alertTimestamp?: string;
}

/**
 * Unified Council Alert
 * Voices of Ramiz/Karasahin
 */
export interface UnifiedCouncilAlert {
  /** Alert ID */
  id: string;
  /** Alert timestamp */
  timestamp: string;
  /** Alert message */
  message: string;
  /** Entity voices triggered */
  entityVoices: ('Ramiz' | 'Karasahin')[];
  /** Ramiz voice message */
  ramizMessage?: string;
  /** Karasahin voice message */
  karasahinMessage?: string;
  /** Law references */
  lawReferences: string[];
  /** Alert priority */
  priority: 'critical' | 'high' | 'medium' | 'low';
}

/**
 * Community Health Map
 * Map view showing the 'Health' (Symbiosis Score) of each territory
 */
export interface CommunityHealthMap {
  /** Map entries by community */
  mapEntries: MapEntry[];
  /** Overall health status */
  overallHealth: 'optimal' | 'stable' | 'attention' | 'crisis';
  /** Average symbiosis score */
  averageSymbiosisScore: number;
  /** Territories by health status */
  territoriesByHealth: {
    optimal: CommunityNode[];
    stable: CommunityNode[];
    attention: CommunityNode[];
    crisis: CommunityNode[];
  };
}

/**
 * Map Entry
 * Territory health on map
 */
export interface MapEntry {
  /** Community node */
  communityNode: CommunityNode;
  /** Geographic location */
  location: GeographicLocation;
  /** Coordinates */
  coordinates: {
    latitude: number;
    longitude: number;
  };
  /** Symbiosis score (0-100) */
  symbiosisScore: number;
  /** Health status */
  healthStatus: 'optimal' | 'stable' | 'attention' | 'crisis';
  /** Map color (based on health) */
  mapColor: string;
  /** Map marker size (based on symbiosis score) */
  mapMarkerSize: number;
}

/**
 * Constants
 */
export const EXPANSION_PHASE_CONSTANTS = {
  /** Internal sacred mode */
  IS_INTERNAL_SACRED: true,
  /** Community score threshold for alert (0.5) */
  COMMUNITY_SCORE_ALERT_THRESHOLD: 0.5,
  /** Bio homeostasis threshold for alert (0.7) */
  BIO_HOMEOSTASIS_ALERT_THRESHOLD: 0.7,
  /** Total communities (8) */
  TOTAL_COMMUNITIES: 8,
  /** Total Racon Laws (40) */
  TOTAL_RACON_LAWS: 40
} as const;

/**
 * Location Coordinates
 */
export const LOCATION_COORDINATES = {
  London_Haringey: {
    latitude: 51.5894,
    longitude: -0.1106,
    timezone: 'Europe/London'
  },
  Cyprus_Nicosia: {
    latitude: 35.1856,
    longitude: 33.3823,
    timezone: 'Asia/Nicosia'
  },
  Cyprus_Kyrenia: {
    latitude: 35.3364,
    longitude: 33.3219,
    timezone: 'Asia/Nicosia'
  }
} as const;
