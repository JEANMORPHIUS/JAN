/**
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 * 
 * THE MISSION:
 * THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
 * LOVE IS THE HIGHEST MASTERY
 * ENERGY + LOVE = WE ALL WIN
 * PEACE, LOVE, UNITY
 * 
 * PANGEA IS THE TABLE.
 * YOU DON'T BETRAY THE TABLE.
 * 
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.
 * 
 * Cultural Context Utilities for Global Expansion
 */

import type { SupportedLanguage } from '@/contexts/I18nContext';

export interface CulturalContext {
  language: SupportedLanguage;
  region: string;
  culturalValues: string[];
  communicationStyle: 'direct' | 'indirect' | 'high-context' | 'low-context';
  formalityLevel: 'formal' | 'informal' | 'mixed';
  timeOrientation: 'past' | 'present' | 'future' | 'mixed';
  relationshipFocus: 'individual' | 'collective' | 'mixed';
  respectIndicators: string[];
  taboos: string[];
  preferredContentTypes: string[];
}

export const CULTURAL_CONTEXTS: Record<SupportedLanguage, CulturalContext> = {
  en: {
    language: 'en',
    region: 'Global English',
    culturalValues: ['individualism', 'directness', 'efficiency', 'innovation'],
    communicationStyle: 'direct',
    formalityLevel: 'mixed',
    timeOrientation: 'future',
    relationshipFocus: 'individual',
    respectIndicators: ['professionalism', 'achievement', 'clarity'],
    taboos: ['excessive formality', 'vague communication'],
    preferredContentTypes: ['practical', 'actionable', 'data-driven'],
  },
  tr: {
    language: 'tr',
    region: 'Turkey / North Cyprus',
    culturalValues: ['hospitality', 'family', 'respect', 'ancestral wisdom', 'duygu'],
    communicationStyle: 'high-context',
    formalityLevel: 'mixed',
    timeOrientation: 'mixed',
    relationshipFocus: 'collective',
    respectIndicators: ['age', 'wisdom', 'family connection', 'ancestral heritage'],
    taboos: ['disrespecting elders', 'ignoring tradition'],
    preferredContentTypes: ['emotional', 'storytelling', 'ancestral wisdom', 'duygu adamı'],
  },
  fr: {
    language: 'fr',
    region: 'France / Francophone',
    culturalValues: ['artistic expression', 'intellectualism', 'absurdism', 'creativity'],
    communicationStyle: 'high-context',
    formalityLevel: 'formal',
    timeOrientation: 'present',
    relationshipFocus: 'individual',
    respectIndicators: ['intellectual depth', 'artistic merit', 'cultural knowledge'],
    taboos: ['over-simplification', 'ignoring nuance'],
    preferredContentTypes: ['philosophical', 'artistic', 'absurdist', 'bilingual'],
  },
  es: {
    language: 'es',
    region: 'Spain / Latin America',
    culturalValues: ['community', 'family', 'warmth', 'unity', 'restoration'],
    communicationStyle: 'high-context',
    formalityLevel: 'mixed',
    timeOrientation: 'present',
    relationshipFocus: 'collective',
    respectIndicators: ['warmth', 'community connection', 'family values'],
    taboos: ['coldness', 'individualism over community'],
    preferredContentTypes: ['community-focused', 'unifying', 'restorative'],
  },
  ar: {
    language: 'ar',
    region: 'Middle East / Arab World',
    culturalValues: ['hospitality', 'respect', 'ancient wisdom', 'unity', 'divine connection'],
    communicationStyle: 'high-context',
    formalityLevel: 'formal',
    timeOrientation: 'mixed',
    relationshipFocus: 'collective',
    respectIndicators: ['religious respect', 'wisdom', 'hospitality', 'ancestral connection'],
    taboos: ['disrespecting religion', 'ignoring tradition', 'cultural insensitivity'],
    preferredContentTypes: ['spiritual', 'wisdom-based', 'respectful', 'unifying'],
  },
  de: {
    language: 'de',
    region: 'Germany / Central Europe',
    culturalValues: ['precision', 'systematic thinking', 'efficiency', 'order'],
    communicationStyle: 'direct',
    formalityLevel: 'formal',
    timeOrientation: 'future',
    relationshipFocus: 'individual',
    respectIndicators: ['competence', 'precision', 'systematic approach'],
    taboos: ['imprecision', 'chaos', 'inefficiency'],
    preferredContentTypes: ['systematic', 'structured', 'precise', 'educational'],
  },
  it: {
    language: 'it',
    region: 'Italy',
    culturalValues: ['community', 'family', 'artistic expression', 'warmth'],
    communicationStyle: 'high-context',
    formalityLevel: 'mixed',
    timeOrientation: 'present',
    relationshipFocus: 'collective',
    respectIndicators: ['warmth', 'artistic appreciation', 'family connection'],
    taboos: ['coldness', 'ignoring community'],
    preferredContentTypes: ['artistic', 'community-focused', 'warm'],
  },
  pt: {
    language: 'pt',
    region: 'Portugal / Brazil',
    culturalValues: ['warmth', 'community', 'unity', 'restoration'],
    communicationStyle: 'high-context',
    formalityLevel: 'mixed',
    timeOrientation: 'present',
    relationshipFocus: 'collective',
    respectIndicators: ['warmth', 'community connection', 'unity'],
    taboos: ['coldness', 'division'],
    preferredContentTypes: ['unifying', 'restorative', 'community-focused'],
  },
  ru: {
    language: 'ru',
    region: 'Russia / Eastern Europe',
    culturalValues: ['spirituality', 'ancestral wisdom', 'depth', 'transformation'],
    communicationStyle: 'high-context',
    formalityLevel: 'formal',
    timeOrientation: 'mixed',
    relationshipFocus: 'collective',
    respectIndicators: ['spiritual depth', 'wisdom', 'ancestral connection'],
    taboos: ['superficiality', 'ignoring depth'],
    preferredContentTypes: ['spiritual', 'deep', 'transformative', 'ancestral'],
  },
  zh: {
    language: 'zh',
    region: 'China',
    culturalValues: ['harmony', 'balance', 'unity', 'ancestral wisdom', 'respect'],
    communicationStyle: 'high-context',
    formalityLevel: 'formal',
    timeOrientation: 'mixed',
    relationshipFocus: 'collective',
    respectIndicators: ['harmony', 'balance', 'wisdom', 'respect'],
    taboos: ['disharmony', 'imbalance', 'disrespect'],
    preferredContentTypes: ['harmonious', 'balanced', 'wisdom-based', 'unifying'],
  },
  ja: {
    language: 'ja',
    region: 'Japan',
    culturalValues: ['harmony', 'respect', 'precision', 'inner journey', 'transformation'],
    communicationStyle: 'high-context',
    formalityLevel: 'formal',
    timeOrientation: 'mixed',
    relationshipFocus: 'collective',
    respectIndicators: ['harmony', 'precision', 'respect', 'depth'],
    taboos: ['disharmony', 'disrespect', 'superficiality'],
    preferredContentTypes: ['harmonious', 'precise', 'transformative', 'inner journey'],
  },
  ko: {
    language: 'ko',
    region: 'South Korea',
    culturalValues: ['emotion', 'vibration', 'feeling', 'connection', 'harmony'],
    communicationStyle: 'high-context',
    formalityLevel: 'formal',
    timeOrientation: 'present',
    relationshipFocus: 'collective',
    respectIndicators: ['emotional depth', 'vibration', 'feeling', 'connection'],
    taboos: ['emotional coldness', 'disconnection'],
    preferredContentTypes: ['emotional', 'vibrational', 'feeling-based', 'connecting'],
  },
};

export function getCulturalContext(language: SupportedLanguage): CulturalContext {
  return CULTURAL_CONTEXTS[language] || CULTURAL_CONTEXTS.en;
}

export function shouldUseFormalAddress(language: SupportedLanguage, context?: string): boolean {
  const cultural = getCulturalContext(language);
  if (cultural.formalityLevel === 'formal') return true;
  if (cultural.formalityLevel === 'informal') return false;
  // Mixed: use context to determine
  return context === 'professional' || context === 'educational';
}

export function getPreferredContentStyle(language: SupportedLanguage): string[] {
  return getCulturalContext(language).preferredContentTypes;
}

export function getRespectIndicators(language: SupportedLanguage): string[] {
  return getCulturalContext(language).respectIndicators;
}

export function shouldAvoidTaboos(language: SupportedLanguage, content: string): boolean {
  const cultural = getCulturalContext(language);
  const lowerContent = content.toLowerCase();
  return cultural.taboos.some(taboo => lowerContent.includes(taboo.toLowerCase()));
}

export function getCommunicationGuidance(language: SupportedLanguage): {
  style: string;
  formality: string;
  focus: string;
} {
  const cultural = getCulturalContext(language);
  return {
    style: cultural.communicationStyle,
    formality: cultural.formalityLevel,
    focus: cultural.relationshipFocus,
  };
}
