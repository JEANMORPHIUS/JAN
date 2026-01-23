/**
 * EARTH ALIGNMENT TYPES
 * The Truth Engine: Man and Earth live symbiotically
 * 
 * Data Architecture aligned with Earth's movements:
 * - Solar cycles (daily rotation)
 * - Seasonal cycles (yearly orbit)
 * - Lunar cycles (monthly orbit)
 * - Circadian rhythms (SCN synchronization)
 */

export interface EarthAlignment {
  /** Solar cycle alignment (daily rotation) */
  solar: SolarAlignment;
  /** Seasonal cycle alignment (yearly orbit) */
  seasonal: SeasonalAlignment;
  /** Lunar cycle alignment (monthly orbit) */
  lunar: LunarAlignment;
  /** Circadian rhythm alignment (SCN synchronization) */
  circadian: CircadianAlignment;
  /** Overall symbiotic alignment score (0-100) */
  symbioticScore: number;
  /** Date/time of alignment calculation */
  timestamp: string;
}

export interface SolarAlignment {
  /** Current hour (0-23) */
  hour: number;
  /** Phase: 'sunrise' | 'solar_peak' | 'sunset' | 'night' */
  phase: SolarPhase;
  /** Solar window (10am-6pm) alignment */
  inSolarWindow: boolean;
  /** Hours until/from sunrise */
  hoursFromSunrise: number;
  /** Hours until/from sunset */
  hoursFromSunset: number;
  /** Solar energy intensity (0-100) */
  solarIntensity: number;
}

export type SolarPhase = 'sunrise' | 'solar_peak' | 'sunset' | 'night';

export interface SeasonalAlignment {
  /** Current season: 'winter' | 'spring' | 'summer' | 'autumn' */
  season: Season;
  /** Day of year (1-365/366) */
  dayOfYear: number;
  /** Days until/from solstice/equinox */
  daysFromSolsticeEquinox: number;
  /** Seasonal energy intensity (0-100) */
  seasonalIntensity: number;
}

export type Season = 'winter' | 'spring' | 'summer' | 'autumn';

export interface LunarAlignment {
  /** Lunar phase: 'new_moon' | 'waxing' | 'full_moon' | 'waning' */
  phase: LunarPhase;
  /** Days from new moon (0-29.5) */
  daysFromNewMoon: number;
  /** Lunar energy intensity (0-100) */
  lunarIntensity: number;
}

export type LunarPhase = 'new_moon' | 'waxing' | 'full_moon' | 'waning';

export interface CircadianAlignment {
  /** SCN (Suprachiasmatic Nucleus) sync score (0-100) */
  scnSyncScore: number;
  /** Current circadian phase */
  phase: CircadianPhase;
  /** Hours from circadian peak */
  hoursFromCircadianPeak: number;
  /** Alignment with Earth rotation (0-100) */
  earthRotationAlignment: number;
}

export type CircadianPhase = 'awakening' | 'active' | 'maintenance' | 'repair';

/**
 * Loop-Earth Symbiotic Relationship
 */
export interface LoopEarthAlignment {
  /** Loop event aligned with Earth rhythm */
  loopEvent: LoopEvent;
  /** Earth alignment at loop time */
  earthAlignment: EarthAlignment;
  /** Symbiotic compliance: Is loop honoring Earth's rhythm? */
  symbioticCompliance: boolean;
  /** Original Error flag: Loop against Earth's rhythm (red tape interference) */
  originalErrorFlag: boolean;
}

export interface LoopEvent {
  /** Time of loop event */
  timestamp: string;
  /** Loop volume (ml) */
  volume: number;
  /** Loop frequency count for day */
  frequency: number;
  /** Urine characteristics */
  urineCharacteristics: UrineCharacteristics;
}

export interface UrineCharacteristics {
  /** Color (1-10: 1=dark/concentrated, 10=clear/dilute) */
  color: number;
  /** Taste/texture description */
  characteristics?: string;
  /** Time relative to Earth cycle */
  earthCycleTime?: string;
}

/**
 * Original Error Detection
 * Flags when man-made systems conflict with biological/Earth reality
 */
export interface OriginalErrorFlag {
  /** Is this an Original Error interference? */
  isError: boolean;
  /** Type of error: 'red_tape' | 'bureaucracy' | 'sensor_error' | 'insurance_delay' | 'belief_override' */
  errorType?: OriginalErrorType;
  /** Description of error */
  description: string;
  /** Biological truth being overridden */
  biologicalTruth: string;
  /** Belief-based override (Law 1: The Table Never Lies) */
  beliefOverride?: boolean;
  /** Timestamp of error detection */
  timestamp: string;
}

export type OriginalErrorType = 
  | 'red_tape' 
  | 'bureaucracy' 
  | 'sensor_error' 
  | 'insurance_delay' 
  | 'belief_override'
  | 'man_made_separation';
