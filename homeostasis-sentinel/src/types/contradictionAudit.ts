/**
 * CONTRADICTION AUDIT TYPES
 * Cleaning House: ALL MAN-MADE CONTRADICTIONS
 * 
 * Philosophy:
 * - Are we taking EVERYTHING into account?
 * - ALL MAN-MADE CONTRADICTIONS
 * - WE'RE CLEANING HOUSE
 */

/**
 * System Contradiction
 * A contradiction in a system
 */
export interface SystemContradiction {
  /** System: 'medical' | 'legal' | 'educational' | 'political' | 'economic' | 'digital' | 'social' | 'environmental' */
  system: string;
  /** Contradiction description */
  contradiction: string;
  /** Root cause */
  rootCause: string;
  /** Truth to restore */
  truthToRestore: string;
}

/**
 * System Audit
 * Audit of a system's contradictions
 */
export interface SystemAudit {
  /** System name */
  systemName: string;
  /** Contradictions found */
  contradictions: SystemContradiction[];
  /** Root causes identified */
  rootCauses: string[];
  /** Truths to restore */
  truthsToRestore: string[];
}

/**
 * Comprehensive Contradiction Audit
 * Complete audit of all systems
 */
export interface ComprehensiveContradictionAudit {
  /** Medical systems audit */
  medical: SystemAudit;
  
  /** Legal systems audit */
  legal: SystemAudit;
  
  /** Educational systems audit */
  educational: SystemAudit;
  
  /** Political systems audit */
  political: SystemAudit;
  
  /** Economic systems audit */
  economic: SystemAudit;
  
  /** Digital systems audit */
  digital: SystemAudit;
  
  /** Social systems audit */
  social: SystemAudit;
  
  /** Environmental systems audit */
  environmental: SystemAudit;
  
  /** Total contradictions found */
  totalContradictions: number;
  
  /** Total root causes identified */
  totalRootCauses: number;
  
  /** Timestamp */
  timestamp: string;
}
