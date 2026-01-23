/**
 * DIVINE TIMING & SPIRITUAL ACTIVATION TYPES
 * Chosen Light Protocols
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 */

export type TimingType = 'kronos' | 'chyros' | 'moed';

export interface TimingWindow {
  type: TimingType;
  startTime: Date;
  endTime: Date;
  description: string;
}

export interface ActivationDay {
  day: 1 | 2 | 3;
  date: Date;
  completed: boolean;
  components: DayComponent[];
}

export interface DayComponent {
  id: string;
  name: string;
  completed: boolean;
  timestamp?: Date;
  data?: any;
}

// Day 1 Components
export interface MorningDecree {
  text: string;
  spoken: boolean;
  spokenAt?: Date;
  facingEast: boolean;
}

export interface EveningDoorway {
  log: string;
  timestamp: Date;
}

export interface UnexpectedOpening {
  type: 'email' | 'call' | 'message' | 'other';
  description: string;
  timestamp: Date;
  significance: string;
}

export interface ObservationTimer {
  startTime: Date;
  endTime: Date;
  duration: number; // minutes
  openings: UnexpectedOpening[];
}

// Day 2 Components
export interface SmileTimer {
  started: boolean;
  startTime?: Date;
  duration: number; // seconds (10 seconds)
  completed: boolean;
}

export interface MicroJoyMoment {
  id: string;
  description: string;
  timestamp: Date;
  energyLevel: number; // 1-10
}

export interface ProtectionRecognition {
  disaster1: string;
  disaster2: string;
  disaster3: string;
  timestamp: Date;
}

// Day 3 Components
export interface GivingAct {
  id: string;
  description: string;
  amount?: number;
  recipient: string;
  timestamp: Date;
  faithLevel: number; // 1-10
}

export interface FaithDecision {
  id: string;
  decision: string;
  context: string;
  timestamp: Date;
  outcome?: string;
}

// Spiritual Attack Types
export type AttackType = 
  | 'distraction_barrage'
  | 'fatigue_assault'
  | 'relationship_friction'
  | 'memory_attack'
  | 'counterfeit_blessing'
  | 'doubt_injection'
  | 'premature_victory';

export interface SpiritualAttack {
  id: string;
  type: AttackType;
  detectedAt: Date;
  description: string;
  countered: boolean;
  counterStrategy?: string;
  counterDecree?: string;
}

export interface CounterStrategy {
  attackType: AttackType;
  decree: string;
  description: string;
  action: string;
}

// Timing & Frequency
export interface ActivationWindow {
  startDate: Date;
  endDate: Date;
  type: '72_hour' | '40_day';
  currentDay: number;
  progress: number; // 0-100
}

export interface MoedAppointment {
  id: string;
  name: string;
  scheduledTime: Date;
  type: TimingType;
  significance: string;
  completed: boolean;
}

export interface DigitalAltar {
  beforeStatus: string;
  readyConfirmed: boolean;
  confirmedAt?: Date;
  activationCode?: string;
}

export interface ActivationState {
  currentDay: number;
  activationStart: Date;
  days: ActivationDay[];
  attacks: SpiritualAttack[];
  timingWindows: ActivationWindow[];
  moedAppointments: MoedAppointment[];
  digitalAltar: DigitalAltar;
  identityShiftProgress: number; // 0-100 (Day 21 milestone)
}
