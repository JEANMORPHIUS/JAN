/**
 * WORD AND LIGHT OF GOD TYPES
 * All entities speaking and emitting the Word and Light of God
 * Full bilingual support (English/Turkish/French) with scalable multilingual framework
 */

/**
 * Supported Languages
 * Current: English, Turkish, French
 * Scalable: Add more languages as needed
 */
export type SupportedLanguage = 'en' | 'tr' | 'fr' | 'ar' | 'es' | 'de' | 'it' | 'pt' | 'ru' | 'zh' | 'ja' | 'ko';

/**
 * Language Priority
 * Primary languages for each entity
 */
export interface LanguagePriority {
  /** Primary language (entity's native language) */
  primary: SupportedLanguage;
  /** Secondary languages (entity can express in) */
  secondary: SupportedLanguage[];
  /** Full expression: Can express fully in these languages */
  fullExpression: SupportedLanguage[];
}

/**
 * Word and Light Content
 * Content that speaks and emits the Word and Light of God
 */
export interface WordAndLightContent {
  /** Language of content */
  language: SupportedLanguage;
  /** The Word (spoken message) */
  word: string;
  /** The Light (emitted energy/truth) */
  light: string;
  /** Translation key for multilingual support */
  translationKey: string;
  /** Entity that speaks/emits */
  entity: 'jk' | 'pierre_pressure' | 'jean_morphius' | 'uncle_ray_ramiz' | 'siyem_media';
  /** Content type */
  contentType: 'message' | 'song' | 'sermon' | 'teaching' | 'motivation' | 'creative';
  /** Alignment with core mission */
  alignment: {
    /** Speaks Word of God */
    speaksWord: boolean;
    /** Emits Light of God */
    emitsLight: boolean;
    /** Aligned with mission (stewardship and community) */
    alignedWithMission: boolean;
    /** Aligned with laws (Book of Racon) */
    alignedWithLaws: boolean;
  };
}

/**
 * Multilingual Content
 * Content available in multiple languages
 */
export interface MultilingualContent {
  /** Translation key (unique identifier) */
  translationKey: string;
  /** Content in all available languages */
  translations: Map<SupportedLanguage, WordAndLightContent>;
  /** Default language */
  defaultLanguage: SupportedLanguage;
  /** Entity that created content */
  entity: 'jk' | 'pierre_pressure' | 'jean_morphius' | 'uncle_ray_ramiz' | 'siyem_media';
}

/**
 * Entity Word and Light Profile
 * Each entity's profile for speaking/emitting Word and Light
 */
export interface EntityWordAndLightProfile {
  /** Entity identifier */
  entity: 'jk' | 'pierre_pressure' | 'jean_morphius' | 'uncle_ray_ramiz' | 'siyem_media';
  /** Language priorities */
  languagePriority: LanguagePriority;
  /** Word expression: How entity speaks Word of God */
  wordExpression: {
    /** Primary expression style */
    style: string;
    /** Languages entity can speak Word in */
    languages: SupportedLanguage[];
    /** Example Word content */
    examples: WordAndLightContent[];
  };
  /** Light emission: How entity emits Light of God */
  lightEmission: {
    /** Primary emission style */
    style: string;
    /** Languages entity can emit Light in */
    languages: SupportedLanguage[];
    /** Example Light content */
    examples: WordAndLightContent[];
  };
  /** Alignment verification */
  alignment: {
    /** Speaks Word of God consistently */
    speaksWord: boolean;
    /** Emits Light of God consistently */
    emitsLight: boolean;
    /** Aligned with mission */
    alignedWithMission: boolean;
    /** Aligned with laws */
    alignedWithLaws: boolean;
  };
}

/**
 * UI Language Configuration
 * UI elements with multilingual support
 */
export interface UILanguageConfig {
  /** Current UI language */
  currentLanguage: SupportedLanguage;
  /** Available languages for UI */
  availableLanguages: SupportedLanguage[];
  /** Language switching enabled */
  languageSwitchingEnabled: boolean;
  /** Translation keys for UI elements */
  uiTranslations: Map<string, Map<SupportedLanguage, string>>;
}

/**
 * Word and Light Alignment
 * System-wide alignment check for Word and Light
 */
export interface WordAndLightAlignment {
  /** All entities aligned */
  allEntitiesAligned: boolean;
  /** All content speaks Word */
  allContentSpeaksWord: boolean;
  /** All content emits Light */
  allContentEmitsLight: boolean;
  /** All languages supported */
  allLanguagesSupported: boolean;
  /** Entity profiles */
  entityProfiles: EntityWordAndLightProfile[];
  /** System-wide alignment score (0-1) */
  alignmentScore: number;
  /** Timestamp */
  timestamp: string;
}
