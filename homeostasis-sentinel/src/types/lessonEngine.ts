/** * * LESSON ENGINE TYPES
 *  * Transform lessons into dynamic, data-driven experiences
 *  * 
 *  * Architecture:
 *  * - Trigger: On 'First Loop' activation, ping Symbiotic Compass
 *  * - Logic: Conditional display based on biological state and Earth alignment
 *  * - Compliance: Track 'Finish Rate' (Law 37) - Did user complete the lesson?
 *  * - Storage: Store result in 'The Table' (Immutable DB)
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
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

import { EarthAlignment } from './earthAlignment';
import { ProtocolEvent } from './stewardship';

/**
 * Lesson Definition
 */
export interface Lesson {
  /** Lesson identifier (e.g., "lesson_01_first_loop") */
  id: string;
  /** Lesson name/title */
  name: string;
  /** Lesson description */
  description: string;
  /** Trigger conditions */
  trigger: LessonTrigger;
  /** Conditional logic for display */
  conditions: LessonCondition[];
  /** Lesson content (can be dynamic based on conditions) */
  content: LessonContent;
  /** Completion criteria (Law 37: Finish What You Begin) */
  completionCriteria: CompletionCriteria;
  /** Associated Racon Law */
  raconLaw?: string;
}

/**
 * Lesson Trigger
 * When should the lesson activate?
 */
export interface LessonTrigger {
  /** Trigger type: 'first_loop' | 'glucose_threshold' | 'time_based' | 'earth_alignment' */
  type: TriggerType;
  /** Trigger conditions */
  conditions: TriggerCondition[];
  /** Symbiotic Compass ping required? */
  requiresSymbioticCompass: boolean;
}

export type TriggerType = 'first_loop' | 'glucose_threshold' | 'time_based' | 'earth_alignment' | 'combined';

export interface TriggerCondition {
  /** Condition type: 'glucose' | 'time' | 'sunset' | 'sunrise' | 'loop_count' | 'vision' | 'earth_phase' */
  type: string;
  /** Operator: '>' | '<' | '==' | '>=' | '<=' */
  operator: string;
  /** Value to compare against */
  value: number | string;
}

/**
 * Lesson Condition
 * Conditional logic for dynamic content display
 */
export interface LessonCondition {
  /** Condition ID */
  id: string;
  /** Condition logic (IF statement) */
  logic: ConditionLogic;
  /** Content to display when condition is true */
  displayContent: LessonContent;
}

export interface ConditionLogic {
  /** All conditions must be true (AND) */
  all?: ConditionLogic[];
  /** Any condition must be true (OR) */
  any?: ConditionLogic[];
  /** Single condition */
  condition?: TriggerCondition;
}

/**
 * Lesson Content
 * Dynamic content based on conditions
 */
export interface LessonContent {
  /** Main message/instruction */
  message: string;
  /** Supporting text */
  supportingText?: string;
  /** Racon Law reference (e.g., "Law 31: The War begins") */
  raconLawReference?: string;
  /** Earth alignment context */
  earthContext?: string;
  /** Action required */
  action?: string;
}

/**
 * Completion Criteria
 * Law 37: Finish What You Begin
 */
export interface CompletionCriteria {
  /** What constitutes completion? */
  criteria: CompletionRequirement[];
  /** Minimum completion score (0-100) */
  minimumScore: number;
}

export interface CompletionRequirement {
  /** Requirement type: 'loop_alignment' | 'glucose_target' | 'time_window' | 'earth_alignment' */
  type: string;
  /** Target value */
  target: number | string;
  /** Weight for completion calculation */
  weight: number;
}

/**
 * Lesson State
 * Current state of a lesson instance
 */
export interface LessonState {
  /** Lesson ID */
  lessonId: string;
  /** Is lesson active? */
  isActive: boolean;
  /** Was lesson triggered? */
  wasTriggered: boolean;
  /** Trigger timestamp */
  triggerTimestamp?: string;
  /** Current conditions met */
  conditionsMet: string[];
  /** Displayed content */
  displayedContent?: LessonContent;
  /** Completion status */
  completion: LessonCompletion;
  /** Earth alignment at trigger time */
  earthAlignment?: EarthAlignment;
}

/**
 * Lesson Completion
 * Law 37: Finish What You Begin
 */
export interface LessonCompletion {
  /** Is lesson completed? */
  isCompleted: boolean;
  /** Completion timestamp */
  completionTimestamp?: string;
  /** Completion score (0-100) */
  completionScore: number;
  /** Completion rate (Law 37 adherence) */
  finishRate: number;
  /** Completed requirements */
  completedRequirements: string[];
  /** Failed requirements */
  failedRequirements: string[];
  /** Protocol event (Law 37 tracking) */
  protocolEvent?: ProtocolEvent;
}

/**
 * The Table Entry
 * Immutable database entry for lesson completion
 * Law 1: The Table Never Lies
 */
export interface TableEntry {
  /** Unique entry ID */
  id: string;
  /** Timestamp of entry (immutable) */
  timestamp: string;
  /** Lesson ID */
  lessonId: string;
  /** Lesson state at completion */
  lessonState: LessonState;
  /** Biological truth at completion */
  biologicalTruth: {
    glucose?: number;
    visionClarity?: number;
    muscleTension?: number;
    breathQuality?: number;
  };
  /** Earth alignment at completion */
  earthAlignment: EarthAlignment;
  /** Law 37 compliance */
  law37Compliance: boolean;
  /** Finish rate */
  finishRate: number;
  /** Immutable: Cannot be modified after creation */
  immutable: true;
}

/**
 * Lesson Engine State
 * Overall state of the lesson engine
 */
export interface LessonEngineState {
  /** Active lessons */
  activeLessons: LessonState[];
  /** Completed lessons */
  completedLessons: TableEntry[];
  /** Available lessons */
  availableLessons: Lesson[];
  /** Overall completion rate (Law 37 adherence) */
  overallCompletionRate: number;
  /** The Table: All immutable entries */
  theTable: TableEntry[];
}
