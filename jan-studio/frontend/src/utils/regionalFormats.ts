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
 * Regional Formatting Utilities for Global Expansion
 */

import type { SupportedLanguage } from '@/contexts/I18nContext';

export interface RegionalFormat {
  dateFormat: (date: Date) => string;
  timeFormat: (date: Date) => string;
  numberFormat: (num: number) => string;
  currencyFormat: (amount: number, currency?: string) => string;
}

const regionalFormats: Record<SupportedLanguage, RegionalFormat> = {
  en: {
    dateFormat: (date: Date) => date.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' }),
    timeFormat: (date: Date) => date.toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' }),
    numberFormat: (num: number) => num.toLocaleString('en-GB'),
    currencyFormat: (amount: number, currency = 'GBP') => 
      new Intl.NumberFormat('en-GB', { style: 'currency', currency }).format(amount),
  },
  tr: {
    dateFormat: (date: Date) => date.toLocaleDateString('tr-TR', { day: 'numeric', month: 'long', year: 'numeric' }),
    timeFormat: (date: Date) => date.toLocaleTimeString('tr-TR', { hour: '2-digit', minute: '2-digit' }),
    numberFormat: (num: number) => num.toLocaleString('tr-TR'),
    currencyFormat: (amount: number, currency = 'TRY') => 
      new Intl.NumberFormat('tr-TR', { style: 'currency', currency }).format(amount),
  },
  fr: {
    dateFormat: (date: Date) => date.toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric' }),
    timeFormat: (date: Date) => date.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' }),
    numberFormat: (num: number) => num.toLocaleString('fr-FR'),
    currencyFormat: (amount: number, currency = 'EUR') => 
      new Intl.NumberFormat('fr-FR', { style: 'currency', currency }).format(amount),
  },
  es: {
    dateFormat: (date: Date) => date.toLocaleDateString('es-ES', { day: 'numeric', month: 'long', year: 'numeric' }),
    timeFormat: (date: Date) => date.toLocaleTimeString('es-ES', { hour: '2-digit', minute: '2-digit' }),
    numberFormat: (num: number) => num.toLocaleString('es-ES'),
    currencyFormat: (amount: number, currency = 'EUR') => 
      new Intl.NumberFormat('es-ES', { style: 'currency', currency }).format(amount),
  },
  ar: {
    dateFormat: (date: Date) => date.toLocaleDateString('ar-SA', { day: 'numeric', month: 'long', year: 'numeric' }),
    timeFormat: (date: Date) => date.toLocaleTimeString('ar-SA', { hour: '2-digit', minute: '2-digit' }),
    numberFormat: (num: number) => num.toLocaleString('ar-SA'),
    currencyFormat: (amount: number, currency = 'SAR') => 
      new Intl.NumberFormat('ar-SA', { style: 'currency', currency }).format(amount),
  },
  de: {
    dateFormat: (date: Date) => date.toLocaleDateString('de-DE', { day: 'numeric', month: 'long', year: 'numeric' }),
    timeFormat: (date: Date) => date.toLocaleTimeString('de-DE', { hour: '2-digit', minute: '2-digit' }),
    numberFormat: (num: number) => num.toLocaleString('de-DE'),
    currencyFormat: (amount: number, currency = 'EUR') => 
      new Intl.NumberFormat('de-DE', { style: 'currency', currency }).format(amount),
  },
  it: {
    dateFormat: (date: Date) => date.toLocaleDateString('it-IT', { day: 'numeric', month: 'long', year: 'numeric' }),
    timeFormat: (date: Date) => date.toLocaleTimeString('it-IT', { hour: '2-digit', minute: '2-digit' }),
    numberFormat: (num: number) => num.toLocaleString('it-IT'),
    currencyFormat: (amount: number, currency = 'EUR') => 
      new Intl.NumberFormat('it-IT', { style: 'currency', currency }).format(amount),
  },
  pt: {
    dateFormat: (date: Date) => date.toLocaleDateString('pt-PT', { day: 'numeric', month: 'long', year: 'numeric' }),
    timeFormat: (date: Date) => date.toLocaleTimeString('pt-PT', { hour: '2-digit', minute: '2-digit' }),
    numberFormat: (num: number) => num.toLocaleString('pt-PT'),
    currencyFormat: (amount: number, currency = 'EUR') => 
      new Intl.NumberFormat('pt-PT', { style: 'currency', currency }).format(amount),
  },
  ru: {
    dateFormat: (date: Date) => date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' }),
    timeFormat: (date: Date) => date.toLocaleTimeString('ru-RU', { hour: '2-digit', minute: '2-digit' }),
    numberFormat: (num: number) => num.toLocaleString('ru-RU'),
    currencyFormat: (amount: number, currency = 'RUB') => 
      new Intl.NumberFormat('ru-RU', { style: 'currency', currency }).format(amount),
  },
  zh: {
    dateFormat: (date: Date) => date.toLocaleDateString('zh-CN', { day: 'numeric', month: 'long', year: 'numeric' }),
    timeFormat: (date: Date) => date.toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' }),
    numberFormat: (num: number) => num.toLocaleString('zh-CN'),
    currencyFormat: (amount: number, currency = 'CNY') => 
      new Intl.NumberFormat('zh-CN', { style: 'currency', currency }).format(amount),
  },
  ja: {
    dateFormat: (date: Date) => date.toLocaleDateString('ja-JP', { day: 'numeric', month: 'long', year: 'numeric' }),
    timeFormat: (date: Date) => date.toLocaleTimeString('ja-JP', { hour: '2-digit', minute: '2-digit' }),
    numberFormat: (num: number) => num.toLocaleString('ja-JP'),
    currencyFormat: (amount: number, currency = 'JPY') => 
      new Intl.NumberFormat('ja-JP', { style: 'currency', currency }).format(amount),
  },
  ko: {
    dateFormat: (date: Date) => date.toLocaleDateString('ko-KR', { day: 'numeric', month: 'long', year: 'numeric' }),
    timeFormat: (date: Date) => date.toLocaleTimeString('ko-KR', { hour: '2-digit', minute: '2-digit' }),
    numberFormat: (num: number) => num.toLocaleString('ko-KR'),
    currencyFormat: (amount: number, currency = 'KRW') => 
      new Intl.NumberFormat('ko-KR', { style: 'currency', currency }).format(amount),
  },
};

export function getRegionalFormat(language: SupportedLanguage): RegionalFormat {
  return regionalFormats[language] || regionalFormats.en;
}

export function formatDateRegional(date: Date | string, language: SupportedLanguage): string {
  const dateObj = typeof date === 'string' ? new Date(date) : date;
  return getRegionalFormat(language).dateFormat(dateObj);
}

export function formatTimeRegional(date: Date | string, language: SupportedLanguage): string {
  const dateObj = typeof date === 'string' ? new Date(date) : date;
  return getRegionalFormat(language).timeFormat(dateObj);
}

export function formatNumberRegional(num: number, language: SupportedLanguage): string {
  return getRegionalFormat(language).numberFormat(num);
}

export function formatCurrencyRegional(amount: number, language: SupportedLanguage, currency?: string): string {
  return getRegionalFormat(language).currencyFormat(amount, currency);
}
