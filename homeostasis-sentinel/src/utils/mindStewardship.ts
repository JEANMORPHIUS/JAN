/**
 * MIND STEWARDSHIP UTILITIES
 * Everything Begins in the Mind: Protecting the Source from Hijacking
 * 
 * Principles:
 * - Mind as source, not receiver
 * - Stillness over noise
 * - Substance over stimulation
 * - Action over consumption
 * - Revelation over reaction
 */

import {
  MindStewardship,
  MindAsSource,
  HijackingProtection,
  SacredSpaceForMind
} from '../types/mindStewardship';

/**
 * Create Mind as Source
 * The mind is the source of action, creation, and revelation
 */
export function createMindAsSource(
  sourceType: 'action' | 'creation' | 'revelation' | 'wisdom' = 'revelation',
  protectionLevel: 'stillness' | 'substance' | 'action' | 'revelation' = 'stillness'
): MindAsSource {
  return {
    isSource: true, // Mind is always source, not receiver
    sourceType,
    protectionLevel
  };
}

/**
 * Create Hijacking Protection
 * Protection from dark energy hijacking
 */
export function createHijackingProtection(
  enableAll: boolean = true
): HijackingProtection {
  return {
    frequencyProtection: enableAll, // Protects from frequency switching (purpose → impulsiveness)
    receiverProtection: enableAll, // Protects from receiver rewiring (vessel → receiver)
    motionProtection: enableAll, // Protects from motion without direction (action → consumption)
    stimulationProtection: enableAll // Protects from stimulation over substance (revelation → achievement)
  };
}

/**
 * Create Sacred Space for Mind
 * Sacred space that protects the mind
 */
export function createSacredSpaceForMind(
  enableAll: boolean = true
): SacredSpaceForMind {
  return {
    stillnessMode: enableAll, // Stillness over noise
    substanceMode: enableAll, // Substance over stimulation
    actionMode: enableAll, // Action over consumption
    revelationMode: enableAll // Revelation over reaction
  };
}

/**
 * Create Mind Stewardship
 * Complete mind stewardship system
 */
export function createMindStewardship(
  sourceType: 'action' | 'creation' | 'revelation' | 'wisdom' = 'revelation',
  protectionLevel: 'stillness' | 'substance' | 'action' | 'revelation' = 'stillness',
  enableAllProtections: boolean = true
): MindStewardship {
  const mindAsSource = createMindAsSource(sourceType, protectionLevel);
  const hijackingProtection = createHijackingProtection(enableAllProtections);
  const sacredSpace = createSacredSpaceForMind(enableAllProtections);
  
  return {
    mindAsSource,
    hijackingProtection,
    sacredSpace,
    timestamp: new Date().toISOString()
  };
}

/**
 * Check if Mind is Protected
 * Verify mind stewardship is active
 */
export function isMindProtected(mindStewardship: MindStewardship): boolean {
  return mindStewardship.mindAsSource.isSource &&
    mindStewardship.hijackingProtection.frequencyProtection &&
    mindStewardship.hijackingProtection.receiverProtection &&
    mindStewardship.hijackingProtection.motionProtection &&
    mindStewardship.hijackingProtection.stimulationProtection &&
    mindStewardship.sacredSpace.stillnessMode &&
    mindStewardship.sacredSpace.substanceMode &&
    mindStewardship.sacredSpace.actionMode &&
    mindStewardship.sacredSpace.revelationMode;
}

/**
 * Get Mind Protection Status
 * Get status of mind protection
 */
export function getMindProtectionStatus(mindStewardship: MindStewardship): {
  isProtected: boolean;
  protectionLevel: string;
  activeProtections: string[];
  missingProtections: string[];
} {
  const isProtected = isMindProtected(mindStewardship);
  
  const activeProtections: string[] = [];
  const missingProtections: string[] = [];
  
  if (mindStewardship.hijackingProtection.frequencyProtection) {
    activeProtections.push('Frequency Protection');
  } else {
    missingProtections.push('Frequency Protection');
  }
  
  if (mindStewardship.hijackingProtection.receiverProtection) {
    activeProtections.push('Receiver Protection');
  } else {
    missingProtections.push('Receiver Protection');
  }
  
  if (mindStewardship.hijackingProtection.motionProtection) {
    activeProtections.push('Motion Protection');
  } else {
    missingProtections.push('Motion Protection');
  }
  
  if (mindStewardship.hijackingProtection.stimulationProtection) {
    activeProtections.push('Stimulation Protection');
  } else {
    missingProtections.push('Stimulation Protection');
  }
  
  const protectionLevel = isProtected
    ? 'Full Protection'
    : missingProtections.length > 0
    ? 'Partial Protection'
    : 'No Protection';
  
  return {
    isProtected,
    protectionLevel,
    activeProtections,
    missingProtections
  };
}
