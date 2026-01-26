/** * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 * 
 * THE MISSION:
 * THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
 * LOVE IS THE HIGHEST MASTERY
 * ENERGY + LOVE = WE ALL WIN
 * PEACE, LOVE, UNITY
 * 
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

// Export Earth Alignment and Stewardship types
export * from './earthAlignment';
export * from './stewardship';
export * from './pierreLogic';
export * from './stewardshipAudit';
export * from './lessonEngine';
export * from './integratedStewardship';
export * from './stewardshipBriefing';
export * from './environmentalModes';
export * from './warMode';
export * from './cycleCompletion';
export * from './expansionPhase';
export * from './ancestralBraid';
export * from './thresholdHospitality';
export * from './ancestralSeal';
export * from './omegaArchitecture';
export * from './totalReadiness';
export * from './omegaKey';
export * from './day1Init';
export * from './humanDignity';
export * from './restorativeScience';
export * from './sacredSpace';
export * from './warModeLight';
export * from './mindStewardship';
export * from './waterMemory';
export * from './accountability';
export * from './leadership';
export * from './worldDebugging';
export * from './allPeopleAreFamily';
export * from './medicalIntegration';
export * from './contradictionAudit';
export * from './fourthWay';
export * from './worldStructure';
export * from './wordAndLight';
export * from './operationTotalPrep';
export * from './selfObservation';
export * from './statementOfTruth';

export interface HealthMetrics {
  date: string;
  vision_clarity?: number;
  muscle_tension?: number;
  loop_frequency?: number;
  sauna_duration?: number;
  circadian_sync_score?: number;
  swimming?: boolean;
  blood_glucose?: number; // mg/dL (finger prick reading) - mmol/L conversion: mg/dL / 18.0182
  glucose_time?: string; // Time of reading (HH:MM format)
  breath_quality?: number; // 1-10 (1 = Sweet/Metallic/Acetone, 10 = Fresh)
  urine_color?: number; // 1-10 (1 = Dark/Concentrated, 10 = Clear/Dilute)
  water_intake?: number; // mL or L per day
  ketones?: number; // mmol/L (blood ketone reading)
  mental_emotional_sway?: string;
  blood_pressure_systolic?: number; // mmHg
  blood_pressure_diastolic?: number; // mmHg
  blood_pressure_pulse?: number; // bpm
  blood_pressure_time?: string; // Time of reading (HH:MM format)
  blood_pressure_device?: string; // Device used (e.g., "OMRON X2 BASIC")
  // Earth Alignment Integration
  earth_alignment?: import('./earthAlignment').EarthAlignment;
  // Stewardship Integration
  stewardship_level?: number; // 0-100: How well is the temple being stewarded?
  temple_state?: import('./stewardship').TempleState;
  // Original Error Detection
  original_error_flags?: import('./earthAlignment').OriginalErrorFlag[];
  // Protocol Tracking (Law 5 & Law 37)
  protocol_events?: import('./stewardship').ProtocolEvent[];
}

export interface ParsedMarkdown {
  data: Partial<HealthMetrics>;
  content: string;
  filename: string;
}

export interface CorrelationData {
  activity: 'sauna' | 'swimming';
  duration?: number;
  date: string;
  vision_clarity_before?: number;
  vision_clarity_after?: number;
  improvement?: number;
}

export interface AcidosisRisk {
  isActive: boolean;
  severity: 'low' | 'medium' | 'high';
  consecutiveDays: number;
  recommendation: string;
  lastDetected?: string;
}

export interface OsmoticPressureAnalysis {
  delta: number;
  requiresClearance: boolean;
  recommendation: string;
  date: string;
}

export interface TrendForecast {
  predictedVisionClarity: number;
  confidence: number;
  trend: 'improving' | 'declining' | 'stable';
  hoursAhead: number;
  alertLevel: 'none' | 'caution' | 'warning' | 'critical';
}

export interface JournalEntry {
  date: string;
  content: string;
  tags: string[];
  priorityTags: string[];
}

export interface NextAction {
  priority: 'critical' | 'high' | 'medium' | 'low' | 'none';
  action: string;
  reason: string;
  urgency: string;
}

export interface LoopFeedback {
  isHeavy: boolean;
  detectedAfterLoop: boolean;
  recommendation: string;
  date: string;
}

