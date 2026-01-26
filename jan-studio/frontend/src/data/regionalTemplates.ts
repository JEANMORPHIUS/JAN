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
 * Regional Templates for Global Expansion
 */

import type { SupportedLanguage } from '@/contexts/I18nContext';

export interface RegionalTemplate {
  id: string;
  name: string;
  description: string;
  language: SupportedLanguage;
  category: 'story' | 'lyric' | 'educational' | 'reflection' | 'question';
  content: string;
  variables?: string[];
  culturalContext?: string;
}

export const REGIONAL_TEMPLATES: RegionalTemplate[] = [
  // Turkish Templates
  {
    id: 'tr-story-ancestral',
    name: 'Hikaye - Atasal Yolculuk',
    description: 'Atasal bilgelik ve modern dünya arasındaki yolculuk',
    language: 'tr',
    category: 'story',
    content: '{{karakter}} adlı bir karakterin {{başlangıç}} durumundan {{son}} durumuna yolculuğunu anlatan bir hikaye yaz. {{meydan_okuma}} anları ve {{dönüşüm}} anlarını dahil et. Duygu Adamı felsefesini yansıt.',
    variables: ['karakter', 'başlangıç', 'son', 'meydan_okuma', 'dönüşüm'],
    culturalContext: 'Ottoman heritage, Turkish Cypriot culture, ancestral wisdom',
  },
  {
    id: 'tr-lyric-duygu',
    name: 'Şarkı Sözü - Duygu Adamı',
    description: 'Duygu ve frekans üzerine şarkı sözü',
    language: 'tr',
    category: 'lyric',
    content: '{{tema}} teması üzerine, performanstan ziyade amaca vurgu yapan şarkı sözleri yaz. Mesaj {{ton}} ve {{duygu}} olmalı. Gönül, öz, hakikat gibi kavramları kullan.',
    variables: ['tema', 'ton', 'duygu'],
    culturalContext: 'Turkish Arabesque, Ottoman poetry, Duygu Adamı philosophy',
  },
  
  // French Templates
  {
    id: 'fr-story-absurdist',
    name: 'Histoire - Absurdiste Bilingue',
    description: 'Une histoire absurde qui fait rire puis réfléchir',
    language: 'fr',
    category: 'story',
    content: 'Écris une histoire absurde sur {{sujet}} qui commence par {{début}} et se termine par {{fin}}. Inclure des moments de {{chaos}} et de {{révélation}}. Code-switching français/anglais autorisé.',
    variables: ['sujet', 'début', 'fin', 'chaos', 'révélation'],
    culturalContext: 'French absurdism, bilingual creativity, Jean Morphius style',
  },
  {
    id: 'fr-reflection-creative',
    name: 'Réflexion - Chaos Créatif',
    description: 'Une réflexion sur le chaos créatif et la beauté du désordre',
    language: 'fr',
    category: 'reflection',
    content: 'Réfléchis sur comment {{chaos_type}} a créé de la beauté dans ta vie. Partage comment {{méthode}} t\'a aidé à trouver l\'ordre dans le désordre.',
    variables: ['chaos_type', 'méthode'],
    culturalContext: 'French philosophy, creative chaos, artistic expression',
  },
  
  // Arabic Templates
  {
    id: 'ar-educational-wisdom',
    name: 'تعليمي - الحكمة القديمة',
    description: 'محتوى تعليمي عن الحكمة القديمة والوحدة',
    language: 'ar',
    category: 'educational',
    content: 'اشرح {{مفهوم}} في سياق {{سياق}}. ركز على كيف يتعلق بـ {{اتصال}} ولماذا {{أهمية}}. استخدم أمثلة من {{ثقافة}}.',
    variables: ['مفهوم', 'سياق', 'اتصال', 'أهمية', 'ثقافة'],
    culturalContext: 'Islamic wisdom, Middle Eastern culture, respectful integration',
  },
  
  // Spanish Templates
  {
    id: 'es-story-community',
    name: 'Historia - Comunidad y Unidad',
    description: 'Una historia sobre comunidad y restauración de la unidad',
    language: 'es',
    category: 'story',
    content: 'Escribe una historia sobre {{comunidad}} que muestra cómo {{desafío}} fue superado a través de {{método}}. Enfócate en la unidad y la restauración de {{tabla}}.',
    variables: ['comunidad', 'desafío', 'método', 'tabla'],
    culturalContext: 'Latin American community values, unity, restoration',
  },
  
  // German Templates
  {
    id: 'de-educational-systematic',
    name: 'Bildungsinhalt - Systematisches Denken',
    description: 'Systematischer Bildungsinhalt über Struktur und Ordnung',
    language: 'de',
    category: 'educational',
    content: 'Erkläre {{konzept}} im Kontext von {{kontext}}. Fokussiere auf die systematische Struktur und wie {{verbindung}} funktioniert. Warum ist {{wichtigkeit}} wichtig?',
    variables: ['konzept', 'kontext', 'verbindung', 'wichtigkeit'],
    culturalContext: 'German systematic thinking, structured approach, precision',
  },
  
  // Chinese Templates
  {
    id: 'zh-reflection-harmony',
    name: '反思 - 和谐与平衡',
    description: '关于和谐、平衡和统一的反思',
    language: 'zh',
    category: 'reflection',
    content: '反思{{主题}}如何影响你生活中的和谐。分享{{方法}}如何帮助你找到平衡，以及为什么{{重要性}}对统一很重要。',
    variables: ['主题', '方法', '重要性'],
    culturalContext: 'Chinese philosophy, harmony, balance, unity',
  },
  
  // Japanese Templates
  {
    id: 'ja-story-journey',
    name: '物語 - 内なる旅',
    description: '内なる旅と変容についての物語',
    language: 'ja',
    category: 'story',
    content: '{{キャラクター}}というキャラクターの{{始まり}}から{{終わり}}への内なる旅を描く物語を書いてください。{{挑戦}}の瞬間と{{突破}}の瞬間を含めてください。',
    variables: ['キャラクター', '始まり', '終わり', '挑戦', '突破'],
    culturalContext: 'Japanese storytelling, inner journey, transformation',
  },
  
  // Korean Templates
  {
    id: 'ko-lyric-emotion',
    name: '가사 - 감정과 진동',
    description: '감정과 진동에 관한 가사',
    language: 'ko',
    category: 'lyric',
    content: '{{주제}}에 대한 가사를 작성하세요. {{톤}}과 {{분위기}}를 강조하고, 진동과 감정의 연결을 표현하세요.',
    variables: ['주제', '톤', '분위기'],
    culturalContext: 'Korean emotional expression, vibration, feeling',
  },
];

export function getTemplatesByLanguage(language: SupportedLanguage): RegionalTemplate[] {
  return REGIONAL_TEMPLATES.filter(t => t.language === language);
}

export function getTemplatesByCategory(category: RegionalTemplate['category']): RegionalTemplate[] {
  return REGIONAL_TEMPLATES.filter(t => t.category === category);
}

export function getTemplateById(id: string): RegionalTemplate | undefined {
  return REGIONAL_TEMPLATES.find(t => t.id === id);
}
