/**
 * ACCOUNTABILITY UTILITIES
 * Accountability for Self is Key: Wear Your Vulnerabilities, The Mirror Never Lies
 * 
 * Philosophy:
 * - Accountability for self is key
 * - We must wear our vulnerabilities
 * - You can't fool yourself when you look in the mirror
 * - EVERYTHING is chaotic black energy to distract us from ourselves
 */

import {
  Accountability,
  SelfResponsibility,
  Vulnerabilities,
  MirrorOfTruth,
  ProtectionFromDistraction
} from '../types/accountability';

/**
 * Create Self Responsibility
 * Taking responsibility for self, not blaming others
 */
export function createSelfResponsibility(
  isAccountable: boolean = true,
  notBlaming: boolean = true,
  truthTelling: boolean = true
): SelfResponsibility {
  return {
    isAccountable,
    notBlaming,
    truthTelling
  };
}

/**
 * Create Vulnerabilities
 * We must wear our vulnerabilities (not hide, not cover, not deny)
 */
export function createVulnerabilities(
  wearing: boolean = true,
  visible: boolean = true,
  truth: string = "Vulnerabilities are truth, not shame. We must wear them, not hide them."
): Vulnerabilities {
  return {
    wearing,
    visible,
    truth
  };
}

/**
 * Create Mirror of Truth
 * You can't fool yourself when you look in the mirror
 */
export function createMirrorOfTruth(
  neverLies: boolean = true,
  reflectsSelf: boolean = true,
  cannotFool: boolean = true
): MirrorOfTruth {
  return {
    neverLies,
    reflectsSelf,
    cannotFool
  };
}

/**
 * Create Protection from Distraction
 * Protection from chaotic black energy
 */
export function createProtectionFromDistraction(
  sacredSpace: boolean = true,
  mindStewardship: boolean = true,
  mirrorTruth: boolean = true
): ProtectionFromDistraction {
  return {
    sacredSpace,
    mindStewardship,
    mirrorTruth
  };
}

/**
 * Create Accountability
 * Complete accountability system
 */
export function createAccountability(
  isAccountable: boolean = true,
  wearing: boolean = true,
  neverLies: boolean = true,
  protected: boolean = true
): Accountability {
  const selfResponsibility = createSelfResponsibility(isAccountable, true, true);
  const vulnerabilities = createVulnerabilities(wearing, true);
  const mirror = createMirrorOfTruth(neverLies, true, true);
  const protection = createProtectionFromDistraction(protected, protected, protected);
  
  return {
    selfResponsibility,
    vulnerabilities,
    mirror,
    protection,
    timestamp: new Date().toISOString()
  };
}

/**
 * Check Accountability Status
 * Verify accountability is active
 */
export function checkAccountabilityStatus(accountability: Accountability): {
  isAccountable: boolean;
  wearingVulnerabilities: boolean;
  mirrorTruth: boolean;
  protected: boolean;
  status: 'full' | 'partial' | 'none';
} {
  const isAccountable = accountability.selfResponsibility.isAccountable &&
    accountability.selfResponsibility.notBlaming &&
    accountability.selfResponsibility.truthTelling;
  
  const wearingVulnerabilities = accountability.vulnerabilities.wearing &&
    accountability.vulnerabilities.visible;
  
  const mirrorTruth = accountability.mirror.neverLies &&
    accountability.mirror.reflectsSelf &&
    accountability.mirror.cannotFool;
  
  const protected = accountability.protection.sacredSpace &&
    accountability.protection.mindStewardship &&
    accountability.protection.mirrorTruth;
  
  const status = isAccountable && wearingVulnerabilities && mirrorTruth && protected
    ? 'full'
    : (isAccountable || wearingVulnerabilities || mirrorTruth || protected)
    ? 'partial'
    : 'none';
  
  return {
    isAccountable,
    wearingVulnerabilities,
    mirrorTruth,
    protected,
    status
  };
}

/**
 * Get Accountability Message
 * Get message about accountability status
 */
export function getAccountabilityMessage(accountability: Accountability): string {
  const status = checkAccountabilityStatus(accountability);
  
  if (status.status === 'full') {
    return "Accountability for self is key. You are wearing your vulnerabilities. The mirror never lies. You are protected from distraction. This is stewardship, not separation.";
  } else if (status.status === 'partial') {
    return "Accountability for self is key. Some areas need attention. Wear your vulnerabilities. Look in the mirror. Protect yourself from distraction. This is stewardship, not separation.";
  } else {
    return "Accountability for self is key. Take responsibility for self. Wear your vulnerabilities. Look in the mirror. Protect yourself from distraction. This is stewardship, not separation.";
  }
}
