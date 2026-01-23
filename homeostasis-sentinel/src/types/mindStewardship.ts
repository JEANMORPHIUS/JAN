/**
 * MIND STEWARDSHIP TYPES
 * Everything Begins in the Mind: Protecting the Source from Hijacking
 * 
 * Principles:
 * - Mind as source, not receiver
 * - Stillness over noise
 * - Substance over stimulation
 * - Action over consumption
 * - Revelation over reaction
 */

/**
 * Mind as Source
 * The mind is the source of action, creation, and revelation
 */
export interface MindAsSource {
  /** Is mind source? (not receiver) */
  isSource: boolean;
  /** Source type: What the mind creates */
  sourceType: 'action' | 'creation' | 'revelation' | 'wisdom';
  /** Protection level: How the mind is protected */
  protectionLevel: 'stillness' | 'substance' | 'action' | 'revelation';
}

/**
 * Hijacking Protection
 * Protection from dark energy hijacking
 */
export interface HijackingProtection {
  /** Frequency protection: Protects from frequency switching (purpose → impulsiveness) */
  frequencyProtection: boolean;
  /** Receiver protection: Protects from receiver rewiring (vessel → receiver) */
  receiverProtection: boolean;
  /** Motion protection: Protects from motion without direction (action → consumption) */
  motionProtection: boolean;
  /** Stimulation protection: Protects from stimulation over substance (revelation → achievement) */
  stimulationProtection: boolean;
}

/**
 * Sacred Space for Mind
 * Sacred space that protects the mind
 */
export interface SacredSpaceForMind {
  /** Stillness mode: Stillness over noise */
  stillnessMode: boolean;
  /** Substance mode: Substance over stimulation */
  substanceMode: boolean;
  /** Action mode: Action over consumption */
  actionMode: boolean;
  /** Revelation mode: Revelation over reaction */
  revelationMode: boolean;
}

/**
 * Mind Stewardship
 * Complete mind stewardship system
 */
export interface MindStewardship {
  /** The mind as source */
  mindAsSource: MindAsSource;
  
  /** Hijacking protection */
  hijackingProtection: HijackingProtection;
  
  /** Sacred space for mind */
  sacredSpace: SacredSpaceForMind;
  
  /** Timestamp */
  timestamp: string;
}
