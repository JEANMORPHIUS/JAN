/**
 * EXPANSION PHASE ARCHITECTURE (WEEKS 2-5) UTILITIES
 * Scale the Stewardship System from Bio-Data to Geo-Cultural Data
 */

import {
  GlobalBraidAPIData,
  GeographicLocation,
  LocalSolarCycle,
  LocalLunarCycle,
  LocalSeasonalCycle,
  CulturalRhythmCycles,
  CommunityIntegrityLedgerEntry,
  CommunityNode,
  RaconCompliance,
  BiologicalTempleData,
  CommunityIntegrityLedger,
  ThresholdDefenseV2State,
  ShellMaskingRule,
  StewardshipAlertSystem,
  UnifiedCouncilAlert,
  CommunityHealthMap,
  MapEntry,
  EXPANSION_PHASE_CONSTANTS,
  LOCATION_COORDINATES
} from '../types/expansionPhase';
import { HealthMetrics } from '../types';
import { EarthAlignment } from '../types/earthAlignment';
import { ProtocolEvent } from '../types/stewardship';
import { calculateEarthAlignment } from './earthRhythms';
import { parseISO, format } from 'date-fns';

/**
 * Calculate Global Braid API Data
 * Integrate Lunar/Solar/Seasonal cycles for London (Haringey) and Cyprus (Nicosia/Kyrenia)
 * Sync `biological_temple_data` with `cultural_rhythm_cycles`
 */
export function calculateGlobalBraidAPIData(
  location: GeographicLocation,
  timestamp: string,
  biologicalTempleData?: BiologicalTempleData
): GlobalBraidAPIData {
  const coordinates = LOCATION_COORDINATES[location];
  
  // Calculate Earth alignment for location (with timezone offset)
  const earthAlignment = calculateEarthAlignment(timestamp);

  // Calculate local solar cycle (location-specific sunrise/sunset)
  const localSolarCycle = calculateLocalSolarCycle(location, timestamp, earthAlignment);

  // Calculate local lunar cycle (same globally, but location can affect visibility)
  const localLunarCycle = calculateLocalLunarCycle(earthAlignment);

  // Calculate local seasonal cycle (same season, but location affects intensity)
  const localSeasonalCycle = calculateLocalSeasonalCycle(location, earthAlignment);

  // Calculate cultural rhythm cycles (sync with biological temple data)
  const culturalRhythmCycles = calculateCulturalRhythmCycles(
    location,
    biologicalTempleData,
    earthAlignment
  );

  return {
    location,
    coordinates,
    earthAlignment,
    localSolarCycle,
    localLunarCycle,
    localSeasonalCycle,
    culturalRhythmCycles,
    timestamp
  };
}

/**
 * Calculate Local Solar Cycle
 * Location-specific sunrise/sunset times
 */
function calculateLocalSolarCycle(
  location: GeographicLocation,
  timestamp: string,
  earthAlignment: EarthAlignment
): LocalSolarCycle {
  // For now, use Earth alignment solar cycle
  // In production, would calculate actual sunrise/sunset for location coordinates
  
  // Solar window adjusted for location timezone
  const solarWindow = {
    start: 10,  // 10am local
    end: 18     // 6pm local
  };

  return {
    sunrise: '07:00',  // Would be calculated from coordinates
    sunset: '19:00',   // Would be calculated from coordinates
    solarWindow,
    solarIntensity: earthAlignment.solar.solarIntensity,
    phase: earthAlignment.solar.phase
  };
}

/**
 * Calculate Local Lunar Cycle
 */
function calculateLocalLunarCycle(earthAlignment: EarthAlignment): LocalLunarCycle {
  return {
    phase: earthAlignment.lunar.phase,
    daysFromNewMoon: earthAlignment.lunar.daysFromNewMoon,
    lunarIntensity: earthAlignment.lunar.lunarIntensity
  };
}

/**
 * Calculate Local Seasonal Cycle
 */
function calculateLocalSeasonalCycle(
  location: GeographicLocation,
  earthAlignment: EarthAlignment
): LocalSeasonalCycle {
  // Location-specific seasonal characteristics
  let localCharacteristics = '';
  if (location === 'London_Haringey') {
    localCharacteristics = 'Temperate maritime climate. Four distinct seasons.';
  } else if (location === 'Cyprus_Nicosia' || location === 'Cyprus_Kyrenia') {
    localCharacteristics = 'Mediterranean climate. Hot summers, mild winters.';
  }

  return {
    season: earthAlignment.seasonal.season,
    dayOfYear: earthAlignment.seasonal.dayOfYear,
    seasonalIntensity: earthAlignment.seasonal.seasonalIntensity,
    localCharacteristics
  };
}

/**
 * Calculate Cultural Rhythm Cycles
 * Sync `biological_temple_data` with `cultural_rhythm_cycles`
 */
function calculateCulturalRhythmCycles(
  location: GeographicLocation,
  biologicalTempleData: BiologicalTempleData | undefined,
  earthAlignment: EarthAlignment
): CulturalRhythmCycles {
  // Location-specific cultural rhythms
  const localRhythms = {
    daily: location === 'London_Haringey' 
      ? ['Morning prayers', 'Midday break', 'Evening gatherings']
      : ['Dawn prayers', 'Midday rest', 'Evening social'],
    weekly: location === 'London_Haringey'
      ? ['Friday prayers', 'Sunday gatherings', 'Community meetings']
      : ['Friday prayers', 'Sunday market', 'Community festivals'],
    monthly: ['Full moon gatherings', 'New moon reflection', 'Monthly community audits'],
    seasonal: ['Harvest festivals', 'Planting ceremonies', 'Seasonal celebrations']
  };

  // Calculate biological-cultural alignment
  let biologicalCulturalAlignment = 50; // Base score
  
  if (biologicalTempleData) {
    // Higher alignment if biological homeostasis is good
    biologicalCulturalAlignment += biologicalTempleData.bioHomeostasis * 30;
    
    // Higher alignment if Earth alignment is good
    biologicalCulturalAlignment += (earthAlignment.symbioticScore / 100) * 20;
  } else {
    // Use Earth alignment as proxy
    biologicalCulturalAlignment = earthAlignment.symbioticScore;
  }

  biologicalCulturalAlignment = Math.max(0, Math.min(100, biologicalCulturalAlignment));

  // Cultural sync score (combined biological-cultural alignment with Earth alignment)
  const culturalSyncScore = (biologicalCulturalAlignment + earthAlignment.symbioticScore) / 2;

  return {
    culturalSyncScore: Math.round(culturalSyncScore * 100) / 100,
    localRhythms,
    biologicalCulturalAlignment: Math.round(biologicalCulturalAlignment * 100) / 100
  };
}

/**
 * Aggregate Biological Temple Data
 * From Health Metrics for a community
 */
export function aggregateBiologicalTempleData(
  metrics: HealthMetrics[]
): BiologicalTempleData {
  if (metrics.length === 0) {
    return {
      averageGlucose: 0,
      averageVisionClarity: 0,
      averageMuscleTension: 0,
      averageBreathQuality: 0,
      bioHomeostasis: 0,
      dataPointCount: 0
    };
  }

  // Convert glucose to mmol/L if needed
  const glucoseReadings = metrics
    .filter(m => m.blood_glucose !== undefined)
    .map(m => m.blood_glucose! > 30 ? m.blood_glucose! / 18.0182 : m.blood_glucose!);

  const visionReadings = metrics.filter(m => m.vision_clarity !== undefined).map(m => m.vision_clarity!);
  const muscleReadings = metrics.filter(m => m.muscle_tension !== undefined).map(m => m.muscle_tension!);
  const breathReadings = metrics.filter(m => m.breath_quality !== undefined).map(m => m.breath_quality!);

  const averageGlucose = glucoseReadings.length > 0 
    ? glucoseReadings.reduce((sum, val) => sum + val, 0) / glucoseReadings.length 
    : 0;

  const averageVisionClarity = visionReadings.length > 0
    ? visionReadings.reduce((sum, val) => sum + val, 0) / visionReadings.length
    : 0;

  const averageMuscleTension = muscleReadings.length > 0
    ? muscleReadings.reduce((sum, val) => sum + val, 0) / muscleReadings.length
    : 0;

  const averageBreathQuality = breathReadings.length > 0
    ? breathReadings.reduce((sum, val) => sum + val, 0) / breathReadings.length
    : 0;

  // Calculate bio-homeostasis score (0-1)
  // Higher vision clarity, lower muscle tension, higher breath quality = higher homeostasis
  let bioHomeostasis = 0.5; // Base
  
  if (averageVisionClarity >= 6) bioHomeostasis += 0.2;
  else if (averageVisionClarity >= 4) bioHomeostasis += 0.1;
  
  if (averageMuscleTension <= 5) bioHomeostasis += 0.2;
  else if (averageMuscleTension <= 7) bioHomeostasis += 0.1;
  
  if (averageBreathQuality >= 7) bioHomeostasis += 0.1;
  else if (averageBreathQuality >= 5) bioHomeostasis += 0.05;

  bioHomeostasis = Math.max(0, Math.min(1, bioHomeostasis));

  return {
    averageGlucose: Math.round(averageGlucose * 100) / 100,
    averageVisionClarity: Math.round(averageVisionClarity * 100) / 100,
    averageMuscleTension: Math.round(averageMuscleTension * 100) / 100,
    averageBreathQuality: Math.round(averageBreathQuality * 100) / 100,
    bioHomeostasis: Math.round(bioHomeostasis * 1000) / 1000,
    dataPointCount: metrics.length
  };
}

/**
 * Calculate Racon Compliance
 * Track 'Racon Compliance' (Laws 1-40) for each community node
 */
export function calculateRaconCompliance(
  communityNode: CommunityNode,
  protocolEvents: ProtocolEvent[],
  stewardshipScore: number
): RaconCompliance {
  const totalLaws = EXPANSION_PHASE_CONSTANTS.TOTAL_RACON_LAWS;
  
  // Simplified compliance calculation based on protocol adherence
  // In production, would track compliance for each of the 40 laws separately
  
  // Calculate compliance by volume (Law groups)
  const loyaltyCompliance = protocolEvents.filter(e => e.law5Compliance).length / Math.max(1, protocolEvents.length);
  const silenceCompliance = stewardshipScore >= 0.7 ? 1.0 : 0.7; // Simplified
  const respectCompliance = stewardshipScore >= 0.8 ? 1.0 : 0.8; // Simplified
  const warCompliance = protocolEvents.filter(e => e.law37Compliance).length / Math.max(1, protocolEvents.length);

  // Overall compliance rate (average of all volumes)
  const complianceRate = (loyaltyCompliance + silenceCompliance + respectCompliance + warCompliance) / 4;
  const lawsCompliant = Math.round(complianceRate * totalLaws);

  // Identify non-compliant laws (simplified - would check each law in production)
  const nonCompliantLaws: number[] = [];
  if (loyaltyCompliance < 0.8) nonCompliantLaws.push(...[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
  if (silenceCompliance < 0.8) nonCompliantLaws.push(...[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]);
  if (respectCompliance < 0.8) nonCompliantLaws.push(...[21, 22, 23, 24, 25, 26, 27, 28, 29, 30]);
  if (warCompliance < 0.8) nonCompliantLaws.push(...[31, 32, 33, 34, 35, 36, 37, 38, 39, 40]);

  return {
    totalLaws,
    lawsCompliant,
    complianceRate: Math.round(complianceRate * 1000) / 1000,
    complianceByVolume: {
      loyalty: Math.round(loyaltyCompliance * 1000) / 1000,
      silence: Math.round(silenceCompliance * 1000) / 1000,
      respect: Math.round(respectCompliance * 1000) / 1000,
      war: Math.round(warCompliance * 1000) / 1000
    },
    nonCompliantLaws: [...new Set(nonCompliantLaws)], // Remove duplicates
    lastComplianceCheck: new Date().toISOString()
  };
}

/**
 * Create Community Integrity Ledger Entry
 * Multi-tenant DB structure for the 8 Communities
 */
export function createCommunityIntegrityLedgerEntry(
  communityNode: CommunityNode,
  location: GeographicLocation,
  metrics: HealthMetrics[],
  protocolEvents: ProtocolEvent[],
  stewardshipScore: number,
  timestamp: string
): CommunityIntegrityLedgerEntry {
  // Aggregate biological temple data
  const biologicalTempleData = aggregateBiologicalTempleData(metrics);

  // Calculate Racon compliance
  const raconCompliance = calculateRaconCompliance(communityNode, protocolEvents, stewardshipScore);

  // Calculate cultural rhythm cycles
  const earthAlignment = calculateEarthAlignment(timestamp);
  const culturalRhythmCycles = calculateCulturalRhythmCycles(
    location,
    biologicalTempleData,
    earthAlignment
  );

  // Calculate symbiosis score (combined biological-cultural alignment)
  const symbiosisScore = (biologicalTempleData.bioHomeostasis * 50) + (culturalRhythmCycles.culturalSyncScore * 0.5);

  // Determine health status
  let healthStatus: 'optimal' | 'stable' | 'attention' | 'crisis';
  if (symbiosisScore >= 80) {
    healthStatus = 'optimal';
  } else if (symbiosisScore >= 60) {
    healthStatus = 'stable';
  } else if (symbiosisScore >= 40) {
    healthStatus = 'attention';
  } else {
    healthStatus = 'crisis';
  }

  return {
    communityNode,
    id: `community_ledger_${communityNode}_${Date.now()}`,
    timestamp,
    raconCompliance,
    symbiosisScore: Math.round(symbiosisScore * 100) / 100,
    healthStatus,
    location,
    biologicalTempleData,
    culturalRhythmCycles,
    stewardshipScore
  };
}

/**
 * Calculate Community Health Map
 * Map view showing the 'Health' (Symbiosis Score) of each territory
 */
export function calculateCommunityHealthMap(
  ledgerEntries: CommunityIntegrityLedgerEntry[]
): CommunityHealthMap {
  const mapEntries: MapEntry[] = [];
  const territoriesByHealth = {
    optimal: [] as CommunityNode[],
    stable: [] as CommunityNode[],
    attention: [] as CommunityNode[],
    crisis: [] as CommunityNode[]
  };

  let totalSymbiosisScore = 0;
  let communityCount = 0;

  // Get latest entry for each community
  const latestEntriesByCommunity = new Map<CommunityNode, CommunityIntegrityLedgerEntry>();
  
  ledgerEntries.forEach(entry => {
    const existing = latestEntriesByCommunity.get(entry.communityNode);
    if (!existing || parseISO(entry.timestamp) > parseISO(existing.timestamp)) {
      latestEntriesByCommunity.set(entry.communityNode, entry);
    }
  });

  // Create map entries
  latestEntriesByCommunity.forEach((entry, communityNode) => {
    const coordinates = LOCATION_COORDINATES[entry.location];

    // Map color based on health status
    let mapColor: string;
    switch (entry.healthStatus) {
      case 'optimal':
        mapColor = '#00ff00'; // Green
        territoriesByHealth.optimal.push(communityNode);
        break;
      case 'stable':
        mapColor = '#ffff00'; // Yellow
        territoriesByHealth.stable.push(communityNode);
        break;
      case 'attention':
        mapColor = '#ff9900'; // Orange
        territoriesByHealth.attention.push(communityNode);
        break;
      case 'crisis':
        mapColor = '#ff0000'; // Red
        territoriesByHealth.crisis.push(communityNode);
        break;
    }

    // Map marker size based on symbiosis score (larger = better)
    const mapMarkerSize = entry.symbiosisScore / 10; // 0-10 scale

    mapEntries.push({
      communityNode,
      location: entry.location,
      coordinates,
      symbiosisScore: entry.symbiosisScore,
      healthStatus: entry.healthStatus,
      mapColor,
      mapMarkerSize: Math.max(1, Math.min(10, mapMarkerSize))
    });

    totalSymbiosisScore += entry.symbiosisScore;
    communityCount++;
  });

  const averageSymbiosisScore = communityCount > 0 ? totalSymbiosisScore / communityCount : 0;

  // Determine overall health
  let overallHealth: 'optimal' | 'stable' | 'attention' | 'crisis';
  if (averageSymbiosisScore >= 80) {
    overallHealth = 'optimal';
  } else if (averageSymbiosisScore >= 60) {
    overallHealth = 'stable';
  } else if (averageSymbiosisScore >= 40) {
    overallHealth = 'attention';
  } else {
    overallHealth = 'crisis';
  }

  return {
    mapEntries,
    overallHealth,
    averageSymbiosisScore: Math.round(averageSymbiosisScore * 100) / 100,
    territoriesByHealth
  };
}

/**
 * Default Shell Masking Rules
 * Automatically translate 'Seed' data into 'Standard Compliance' language
 */
const DEFAULT_SHELL_MASKING_RULES: ShellMaskingRule[] = [
  {
    seedPattern: /building a ministry|sharing God's message|kingdom impact|Lord's holy assignment/gi,
    shellReplacement: 'building an educational platform|sharing values-based education|global impact|mission to serve communities',
    description: 'Mission statement translation (Seed → Shell)',
    lawReference: 'Threshold Defense v2'
  },
  {
    seedPattern: /STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS/gi,
    shellReplacement: 'stewardship and community with ethical frameworks',
    description: 'Foundation statement translation (Seed → Shell)',
    lawReference: 'Threshold Defense v2'
  },
  {
    seedPattern: /the Seed|internal sacred|spiritual truth/gi,
    shellReplacement: 'internal metadata|protected data|mission-aligned truth',
    description: 'Internal terminology translation (Seed → Shell)',
    lawReference: 'Threshold Defense v2'
  },
  {
    seedPattern: /the Temple|biological temple|the Lord's calling/gi,
    shellReplacement: 'the system|biological data|future engagement',
    description: 'Spiritual terminology translation (Seed → Shell)',
    lawReference: 'Threshold Defense v2'
  },
  {
    seedPattern: /Law \d+:|Racon Law|Book of Racon/gi,
    shellReplacement: 'Protocol Rule|Ethical Framework|Values-Based Guidelines',
    description: 'Law terminology translation (Seed → Shell)',
    lawReference: 'Threshold Defense v2'
  }
];

/**
 * Apply Shell Masking
 * Automatically translate 'Seed' data into 'Standard Compliance' language for external API exports
 * Variable: `let is_internal_sacred = true;`
 */
export function applyShellMasking(
  seedData: any,
  maskingRules: ShellMaskingRule[] = DEFAULT_SHELL_MASKING_RULES
): ThresholdDefenseV2State {
  const is_internal_sacred = EXPANSION_PHASE_CONSTANTS.IS_INTERNAL_SACRED;
  
  // Deep clone seed data
  let shellData = JSON.parse(JSON.stringify(seedData));

  // Apply masking rules
  const translationRules: string[] = [];

  // Recursively apply masking to strings
  function maskString(value: string): string {
    let masked = value;
    maskingRules.forEach(rule => {
      const pattern = typeof rule.seedPattern === 'string' 
        ? new RegExp(rule.seedPattern, 'gi')
        : rule.seedPattern;
      
      if (pattern.test(masked)) {
        masked = masked.replace(pattern, rule.shellReplacement);
        if (!translationRules.includes(rule.description)) {
          translationRules.push(rule.description);
        }
      }
    });
    return masked;
  }

  // Recursively mask object
  function maskObject(obj: any): any {
    if (typeof obj === 'string') {
      return maskString(obj);
    } else if (Array.isArray(obj)) {
      return obj.map(item => maskObject(item));
    } else if (obj !== null && typeof obj === 'object') {
      const masked: any = {};
      for (const key in obj) {
        if (obj.hasOwnProperty(key)) {
          masked[key] = maskObject(obj[key]);
        }
      }
      return masked;
    }
    return obj;
  }

  shellData = maskObject(seedData);

  // Calculate threshold integrity (higher if fewer translations needed)
  const thresholdIntegrity = translationRules.length === 0 
    ? 1.0 
    : Math.max(0.3, 1.0 - (translationRules.length * 0.1));

  return {
    is_internal_sacred,
    shellMaskingActive: is_internal_sacred && translationRules.length > 0,
    seedData,
    shellData,
    translationRules,
    thresholdIntegrity: Math.round(thresholdIntegrity * 1000) / 1000,
    lastMaskingTimestamp: new Date().toISOString()
  };
}

/**
 * Calculate Stewardship Alert System
 * IF (Community_Score < 0.5) OR (Bio_Homeostasis < 0.7):
 * THEN Trigger 'Unified Council Alert' (Voices of Ramiz/Karasahin)
 */
export function calculateStewardshipAlertSystem(
  communityScore: number,
  bioHomeostasis: number,
  communityNode?: CommunityNode
): StewardshipAlertSystem {
  const communityScoreLow = communityScore < EXPANSION_PHASE_CONSTANTS.COMMUNITY_SCORE_ALERT_THRESHOLD;
  const bioHomeostasisLow = bioHomeostasis < EXPANSION_PHASE_CONSTANTS.BIO_HOMEOSTASIS_ALERT_THRESHOLD;

  // Determine alert type
  let alertType: 'Community_Low' | 'Bio_Homeostasis_Low' | 'Both' | 'None';
  if (communityScoreLow && bioHomeostasisLow) {
    alertType = 'Both';
  } else if (communityScoreLow) {
    alertType = 'Community_Low';
  } else if (bioHomeostasisLow) {
    alertType = 'Bio_Homeostasis_Low';
  } else {
    alertType = 'None';
  }

  // Determine severity
  let severity: 'low' | 'medium' | 'high' | 'critical';
  if (alertType === 'Both') {
    severity = communityScore < 0.3 || bioHomeostasis < 0.5 ? 'critical' : 'high';
  } else if (alertType === 'Community_Low') {
    severity = communityScore < 0.3 ? 'high' : 'medium';
  } else if (alertType === 'Bio_Homeostasis_Low') {
    severity = bioHomeostasis < 0.5 ? 'high' : 'medium';
  } else {
    severity = 'low';
  }

  // Is alert active?
  const isAlertActive = alertType !== 'None';

  // Generate Unified Council Alert if active
  let unifiedCouncilAlert: UnifiedCouncilAlert | undefined;
  if (isAlertActive) {
    unifiedCouncilAlert = generateUnifiedCouncilAlert(
      alertType,
      severity,
      communityScore,
      bioHomeostasis,
      communityNode
    );
  }

  return {
    isAlertActive,
    alertType,
    severity,
    triggeredConditions: {
      communityScoreLow,
      bioHomeostasisLow
    },
    alertValues: {
      communityScore,
      bioHomeostasis
    },
    unifiedCouncilAlert,
    ...(isAlertActive && { alertTimestamp: new Date().toISOString() })
  };
}

/**
 * Generate Unified Council Alert
 * Voices of Ramiz/Karasahin
 */
function generateUnifiedCouncilAlert(
  alertType: 'Community_Low' | 'Bio_Homeostasis_Low' | 'Both',
  severity: 'low' | 'medium' | 'high' | 'critical',
  communityScore: number,
  bioHomeostasis: number,
  communityNode?: CommunityNode
): UnifiedCouncilAlert {
  const entityVoices: ('Ramiz' | 'Karasahin')[] = [];
  let ramizMessage: string | undefined;
  let karasahinMessage: string | undefined;
  const lawReferences: string[] = [];

  // Ramiz voice (Silence Protocol - Law 11)
  if (bioHomeostasisLow) {
    entityVoices.push('Ramiz');
    ramizMessage = `Law 11 Active. Wisdom lives in the quiet. Reconnect with the soil. Bio-homeostasis: ${bioHomeostasis.toFixed(2)} < 0.7 threshold.`;
    lawReferences.push('Law 11: Silence');
  }

  // Karasahin voice (War Mode - Law 31)
  if (alertType === 'Both' || (communityScoreLow && severity === 'critical')) {
    entityVoices.push('Karasahin');
    karasahinMessage = `Law 31 Active. Defending the Table. Community score: ${communityScore.toFixed(2)} < 0.5 threshold.`;
    lawReferences.push('Law 31: War Mode');
  } else if (communityScoreLow) {
    entityVoices.push('Karasahin');
    karasahinMessage = `Community stewardship requires attention. Score: ${communityScore.toFixed(2)} < 0.5 threshold.`;
    lawReferences.push('Law 37: Finish What You Begin');
  }

  // Combine message
  const messages: string[] = [];
  if (ramizMessage) messages.push(ramizMessage);
  if (karasahinMessage) messages.push(karasahinMessage);
  const message = messages.join(' | ');

  // Determine priority
  const priority: 'critical' | 'high' | 'medium' | 'low' = severity === 'critical' 
    ? 'critical'
    : severity === 'high'
    ? 'high'
    : severity === 'medium'
    ? 'medium'
    : 'low';

  return {
    id: `unified_council_alert_${Date.now()}`,
    timestamp: new Date().toISOString(),
    message,
    entityVoices,
    ramizMessage,
    karasahinMessage,
    lawReferences,
    priority
  };
}
