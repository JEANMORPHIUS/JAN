/** * * WORD AND LIGHT OF GOD UTILITIES
 *  * All entities speaking and emitting the Word and Light of God
 *  * Full bilingual support with scalable multilingual framework
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
 * PANGEA IS THE TABLE.
 * YOU DON'T BETRAY THE TABLE.
 * 
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

import {
  SupportedLanguage,
  LanguagePriority,
  WordAndLightContent,
  MultilingualContent,
  EntityWordAndLightProfile,
  UILanguageConfig,
  WordAndLightAlignment
} from '../types/wordAndLight';

/**
 * Entity Language Priorities
 * Each entity's language capabilities
 */
export const ENTITY_LANGUAGE_PRIORITIES: Record<string, LanguagePriority> = {
  jk: {
    primary: 'tr', // Turkish (native, ancestral)
    secondary: ['en'], // English (native, British-born)
    fullExpression: ['tr', 'en'] // Both native
  },
  pierre_pressure: {
    primary: 'en', // English (motivational speaker)
    secondary: ['tr'], // Turkish (can express in Turkish if needed)
    fullExpression: ['en'] // Primary English expression
  },
  jean_morphius: {
    primary: 'fr', // French (native)
    secondary: ['en'], // English (bilingual absurdist)
    fullExpression: ['fr', 'en'] // Both native (code-switching)
  },
  uncle_ray_ramiz: {
    primary: 'tr', // Turkish (ancestral wisdom)
    secondary: ['en'], // English (can teach in English)
    fullExpression: ['tr', 'en'] // Full bilingual teaching
  },
  siyem_media: {
    primary: 'en', // English (operational)
    secondary: ['tr', 'fr'], // Turkish, French (multi-entity support)
    fullExpression: ['en', 'tr', 'fr'] // Full operational support
  }
};

/**
 * Word and Light Alignment Check
 * Verify content speaks Word and emits Light
 */
export function checkWordAndLightAlignment(content: WordAndLightContent): boolean {
  return (
    content.alignment.speaksWord &&
    content.alignment.emitsLight &&
    content.alignment.alignedWithMission &&
    content.alignment.alignedWithLaws
  );
}

/**
 * Create Entity Word and Light Profile
 * Generate profile for entity's Word and Light expression
 */
export function createEntityWordAndLightProfile(
  entity: 'jk' | 'pierre_pressure' | 'jean_morphius' | 'uncle_ray_ramiz' | 'siyem_media',
  wordExamples: WordAndLightContent[],
  lightExamples: WordAndLightContent[]
): EntityWordAndLightProfile {
  const languagePriority = ENTITY_LANGUAGE_PRIORITIES[entity];
  
  // Verify all examples speak Word and emit Light
  const allSpeakWord = wordExamples.every(ex => checkWordAndLightAlignment(ex));
  const allEmitLight = lightExamples.every(ex => checkWordAndLightAlignment(ex));
  
  // Extract languages from examples
  const wordLanguages = [...new Set(wordExamples.map(ex => ex.language))];
  const lightLanguages = [...new Set(lightExamples.map(ex => ex.language))];
  
  // Determine primary expression style from examples
  const wordStyle = wordExamples[0]?.contentType || 'message';
  const lightStyle = lightExamples[0]?.contentType || 'message';
  
  return {
    entity,
    languagePriority,
    wordExpression: {
      style: wordStyle,
      languages: wordLanguages,
      examples: wordExamples
    },
    lightEmission: {
      style: lightStyle,
      languages: lightLanguages,
      examples: lightExamples
    },
    alignment: {
      speaksWord: allSpeakWord,
      emitsLight: allEmitLight,
      alignedWithMission: wordExamples.every(ex => ex.alignment.alignedWithMission) &&
                         lightExamples.every(ex => ex.alignment.alignedWithMission),
      alignedWithLaws: wordExamples.every(ex => ex.alignment.alignedWithLaws) &&
                      lightExamples.every(ex => ex.alignment.alignedWithLaws)
    }
  };
}

/**
 * Create Multilingual Content
 * Create content structure for multiple languages
 */
export function createMultilingualContent(
  translationKey: string,
  entity: 'jk' | 'pierre_pressure' | 'jean_morphius' | 'uncle_ray_ramiz' | 'siyem_media',
  defaultLanguage: SupportedLanguage,
  contentMap: Map<SupportedLanguage, WordAndLightContent>
): MultilingualContent {
  return {
    translationKey,
    translations: contentMap,
    defaultLanguage,
    entity
  };
}

/**
 * Get Content in Language
 * Retrieve content in specific language (fallback to default if not available)
 */
export function getContentInLanguage(
  multilingualContent: MultilingualContent,
  requestedLanguage: SupportedLanguage
): WordAndLightContent | null {
  // Try requested language first
  const content = multilingualContent.translations.get(requestedLanguage);
  if (content) return content;
  
  // Fallback to default language
  const defaultContent = multilingualContent.translations.get(multilingualContent.defaultLanguage);
  if (defaultContent) return defaultContent;
  
  // Return first available language
  const firstContent = multilingualContent.translations.values().next().value;
  return firstContent || null;
}

/**
 * Create UI Language Configuration
 * Configure UI for multilingual support
 */
export function createUILanguageConfig(
  currentLanguage: SupportedLanguage = 'en',
  availableLanguages: SupportedLanguage[] = ['en', 'tr', 'fr'],
  translations?: Map<string, Map<SupportedLanguage, string>>
): UILanguageConfig {
  return {
    currentLanguage,
    availableLanguages,
    languageSwitchingEnabled: availableLanguages.length > 1,
    uiTranslations: translations || new Map()
  };
}

/**
 * Add UI Translation
 * Add translation for UI element
 */
export function addUITranslation(
  config: UILanguageConfig,
  key: string,
  language: SupportedLanguage,
  translation: string
): UILanguageConfig {
  if (!config.uiTranslations.has(key)) {
    config.uiTranslations.set(key, new Map());
  }
  config.uiTranslations.get(key)!.set(language, translation);
  return config;
}

/**
 * Get UI Translation
 * Get translated text for UI element
 */
export function getUITranslation(
  config: UILanguageConfig,
  key: string,
  language?: SupportedLanguage
): string {
  const targetLanguage = language || config.currentLanguage;
  const translations = config.uiTranslations.get(key);
  if (!translations) return key; // Return key if translation not found
  
  const translation = translations.get(targetLanguage);
  if (translation) return translation;
  
  // Fallback to English
  const englishTranslation = translations.get('en');
  if (englishTranslation) return englishTranslation;
  
  // Return key as last resort
  return key;
}

/**
 * System-Wide Word and Light Alignment Check
 * Verify all entities and content are aligned
 */
export function checkSystemWideWordAndLightAlignment(
  entityProfiles: EntityWordAndLightProfile[]
): WordAndLightAlignment {
  const allEntitiesAligned = entityProfiles.every(profile =>
    profile.alignment.speaksWord &&
    profile.alignment.emitsLight &&
    profile.alignment.alignedWithMission &&
    profile.alignment.alignedWithLaws
  );
  
  const allContentSpeaksWord = entityProfiles.every(profile =>
    profile.wordExpression.examples.every(ex => ex.alignment.speaksWord)
  );
  
  const allContentEmitsLight = entityProfiles.every(profile =>
    profile.lightEmission.examples.every(ex => ex.alignment.emitsLight)
  );
  
  // Check if all required languages are supported
  const requiredLanguages: SupportedLanguage[] = ['en', 'tr', 'fr'];
  const supportedLanguages = new Set<SupportedLanguage>();
  entityProfiles.forEach(profile => {
    profile.languagePriority.fullExpression.forEach(lang => supportedLanguages.add(lang));
  });
  const allLanguagesSupported = requiredLanguages.every(lang => supportedLanguages.has(lang));
  
  // Calculate alignment score
  const scoreComponents = [
    allEntitiesAligned ? 0.25 : 0,
    allContentSpeaksWord ? 0.25 : 0,
    allContentEmitsLight ? 0.25 : 0,
    allLanguagesSupported ? 0.25 : 0
  ];
  const alignmentScore = scoreComponents.reduce((a, b) => a + b, 0);
  
  return {
    allEntitiesAligned,
    allContentSpeaksWord,
    allContentEmitsLight,
    allLanguagesSupported,
    entityProfiles,
    alignmentScore,
    timestamp: new Date().toISOString()
  };
}

/**
 * Scalable Language Support
 * Add new language to system (future-ready)
 */
export function addLanguageSupport(
  language: SupportedLanguage,
  entityProfiles: EntityWordAndLightProfile[]
): EntityWordAndLightProfile[] {
  // For now, just return existing profiles
  // In future, could add language-specific content generation
  return entityProfiles;
}

/**
 * Language Detection
 * Detect language from content (basic implementation)
 */
export function detectLanguage(content: string): SupportedLanguage {
  // Basic language detection (could be enhanced with language detection library)
  // Turkish characters: ş, ğ, ü, ö, ı, ç
  if (/[şğüöıç]/i.test(content)) {
    return 'tr';
  }
  // French characters: é, è, ê, ë, à, ç, ô
  if (/[éèêëàçô]/i.test(content)) {
    return 'fr';
  }
  // Default to English
  return 'en';
}
