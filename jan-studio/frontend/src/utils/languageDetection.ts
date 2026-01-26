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
 * Language Detection Utilities for Global Expansion
 */

import type { SupportedLanguage } from '@/contexts/I18nContext';

// Character ranges for different languages
const LANGUAGE_PATTERNS: Record<SupportedLanguage, RegExp[]> = {
  en: [/^[a-zA-Z\s.,!?'"-]+$/],
  tr: [/[şğüöıçŞĞÜÖİÇ]/, /[a-zA-ZşğüöıçŞĞÜÖİÇ\s.,!?'"-]+$/],
  fr: [/[àâäéèêëïîôùûüÿçÀÂÄÉÈÊËÏÎÔÙÛÜŸÇ]/, /[a-zA-ZàâäéèêëïîôùûüÿçÀÂÄÉÈÊËÏÎÔÙÛÜŸÇ\s.,!?'"-]+$/],
  es: [/[ñáéíóúüÑÁÉÍÓÚÜ]/, /[a-zA-ZñáéíóúüÑÁÉÍÓÚÜ\s.,!?'"-]+$/],
  ar: [/[\u0600-\u06FF]/, /[\u0600-\u06FF\s.,!?'"-]+$/],
  de: [/[äöüßÄÖÜ]/, /[a-zA-ZäöüßÄÖÜ\s.,!?'"-]+$/],
  it: [/[àèéìíîòóùúÀÈÉÌÍÎÒÓÙÚ]/, /[a-zA-ZàèéìíîòóùúÀÈÉÌÍÎÒÓÙÚ\s.,!?'"-]+$/],
  pt: [/[áàâãéêíóôõúüçÁÀÂÃÉÊÍÓÔÕÚÜÇ]/, /[a-zA-ZáàâãéêíóôõúüçÁÀÂÃÉÊÍÓÔÕÚÜÇ\s.,!?'"-]+$/],
  ru: [/[\u0400-\u04FF]/, /[\u0400-\u04FF\s.,!?'"-]+$/],
  zh: [/[\u4e00-\u9fff]/, /[\u4e00-\u9fff\s.,!?'"-]+$/],
  ja: [/[\u3040-\u309F\u30A0-\u30FF\u4e00-\u9fff]/, /[\u3040-\u309F\u30A0-\u30FF\u4e00-\u9fff\s.,!?'"-]+$/],
  ko: [/[\uAC00-\uD7AF]/, /[\uAC00-\uD7AF\s.,!?'"-]+$/],
};

// Common words/phrases for each language
const LANGUAGE_KEYWORDS: Record<SupportedLanguage, string[]> = {
  en: ['the', 'and', 'is', 'are', 'was', 'were', 'this', 'that', 'with', 'from'],
  tr: ['ve', 'ile', 'bir', 'bu', 'şu', 'için', 'gibi', 'kadar', 'daha', 'çok'],
  fr: ['le', 'la', 'les', 'un', 'une', 'des', 'et', 'ou', 'dans', 'pour'],
  es: ['el', 'la', 'los', 'las', 'un', 'una', 'y', 'o', 'en', 'con'],
  ar: ['في', 'من', 'إلى', 'على', 'عن', 'مع', 'هذا', 'هذه', 'الذي', 'التي'],
  de: ['der', 'die', 'das', 'und', 'oder', 'in', 'auf', 'für', 'mit', 'von'],
  it: ['il', 'la', 'lo', 'gli', 'le', 'un', 'una', 'e', 'o', 'in'],
  pt: ['o', 'a', 'os', 'as', 'um', 'uma', 'e', 'ou', 'em', 'com'],
  ru: ['и', 'в', 'на', 'с', 'для', 'от', 'к', 'по', 'это', 'что'],
  zh: ['的', '是', '在', '有', '和', '了', '不', '我', '他', '她'],
  ja: ['の', 'は', 'が', 'を', 'に', 'で', 'と', 'から', 'まで', 'より'],
  ko: ['의', '이', '가', '을', '를', '에', '에서', '와', '과', '로'],
};

export interface LanguageDetectionResult {
  language: SupportedLanguage;
  confidence: number;
  detectedBy: 'pattern' | 'keywords' | 'mixed';
}

/**
 * Detect language from text input
 */
export function detectLanguage(text: string): LanguageDetectionResult | null {
  if (!text || text.trim().length < 3) {
    return null;
  }

  const normalizedText = text.trim().toLowerCase();
  const scores: Map<SupportedLanguage, number> = new Map();

  // Initialize scores
  Object.keys(LANGUAGE_PATTERNS).forEach(lang => {
    scores.set(lang as SupportedLanguage, 0);
  });

  // Pattern matching
  Object.entries(LANGUAGE_PATTERNS).forEach(([lang, patterns]) => {
    patterns.forEach(pattern => {
      if (pattern.test(text)) {
        scores.set(lang as SupportedLanguage, (scores.get(lang as SupportedLanguage) || 0) + 1);
      }
    });
  });

  // Keyword matching
  Object.entries(LANGUAGE_KEYWORDS).forEach(([lang, keywords]) => {
    const keywordCount = keywords.filter(keyword => 
      normalizedText.includes(keyword.toLowerCase())
    ).length;
    scores.set(lang as SupportedLanguage, (scores.get(lang as SupportedLanguage) || 0) + keywordCount * 0.5);
  });

  // Find best match
  let bestLanguage: SupportedLanguage = 'en';
  let bestScore = 0;
  let detectionMethod: 'pattern' | 'keywords' | 'mixed' = 'pattern';

  scores.forEach((score, lang) => {
    if (score > bestScore) {
      bestScore = score;
      bestLanguage = lang;
    }
  });

  // Determine detection method
  const patternScore = LANGUAGE_PATTERNS[bestLanguage].some(p => p.test(text)) ? 1 : 0;
  const keywordScore = LANGUAGE_KEYWORDS[bestLanguage].some(k => normalizedText.includes(k)) ? 1 : 0;
  if (patternScore > 0 && keywordScore > 0) {
    detectionMethod = 'mixed';
  } else if (keywordScore > 0) {
    detectionMethod = 'keywords';
  }

  // Calculate confidence (0-1)
  const totalPossibleScore = LANGUAGE_PATTERNS[bestLanguage].length + (LANGUAGE_KEYWORDS[bestLanguage].length * 0.5);
  const confidence = Math.min(1, bestScore / Math.max(1, totalPossibleScore * 0.3));

  if (confidence < 0.3) {
    return null; // Too low confidence
  }

  return {
    language: bestLanguage,
    confidence,
    detectedBy: detectionMethod,
  };
}

/**
 * Suggest language based on user input
 */
export function suggestLanguage(text: string, currentLanguage: SupportedLanguage): SupportedLanguage | null {
  const detection = detectLanguage(text);
  if (!detection) {
    return null;
  }

  // Only suggest if different from current and confidence is high
  if (detection.language !== currentLanguage && detection.confidence > 0.5) {
    return detection.language;
  }

  return null;
}

/**
 * Check if text contains multiple languages (code-switching)
 */
export function detectCodeSwitching(text: string): {
  languages: SupportedLanguage[];
  segments: Array<{ text: string; language: SupportedLanguage; confidence: number }>;
} {
  // Simple approach: split by sentences and detect each
  const sentences = text.split(/[.!?]\s+/).filter(s => s.trim().length > 0);
  const segments: Array<{ text: string; language: SupportedLanguage; confidence: number }> = [];
  const languages = new Set<SupportedLanguage>();

  sentences.forEach(sentence => {
    const detection = detectLanguage(sentence);
    if (detection && detection.confidence > 0.4) {
      segments.push({
        text: sentence,
        language: detection.language,
        confidence: detection.confidence,
      });
      languages.add(detection.language);
    }
  });

  return {
    languages: Array.from(languages),
    segments,
  };
}
