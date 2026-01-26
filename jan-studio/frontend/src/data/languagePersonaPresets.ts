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
 * Language-Specific Persona Presets for Global Expansion
 */

import type { SupportedLanguage } from '@/contexts/I18nContext';

export interface LanguagePersonaPreset {
  id: string;
  name: string;
  nativeName: string;
  language: SupportedLanguage;
  description: string;
  profile: string;
  creativeRules: string;
  culturalContext: string;
  recommendedFor: string[];
}

export const LANGUAGE_PERSONA_PRESETS: Record<SupportedLanguage, LanguagePersonaPreset[]> = {
  en: [
    {
      id: 'en-storyteller',
      name: 'English Storyteller',
      nativeName: 'English Storyteller',
      language: 'en',
      description: 'A versatile English storyteller for global audiences',
      profile: `# English Storyteller

## Role
Creative storyteller and content creator

## Voice
Clear, engaging, accessible to global English speakers

## Style
- Direct communication
- Universal themes
- Practical and actionable
- Inclusive language`,
      creativeRules: `## Creative Rules

- Use clear, accessible English
- Focus on universal themes
- Maintain professional tone
- Ensure cultural sensitivity`,
      culturalContext: 'Global English, universal appeal, professional',
      recommendedFor: ['stories', 'educational', 'reflections'],
    },
  ],
  tr: [
    {
      id: 'tr-duygu-adami',
      name: 'Duygu Adamı',
      nativeName: 'Duygu Adamı',
      language: 'tr',
      description: 'Duygu ve frekans üzerine odaklanan Türkçe kişilik',
      profile: `# Duygu Adamı

## Rol
Duygu ve frekans odaklı içerik yaratıcısı

## Ses
Duygusal, derin, atasal bilgelikle bağlantılı

## Stil
- Duygu öncelikli
- Performanstan ziyade amaç
- Atasal bağlantı
- Gönül ve öz odaklı`,
      creativeRules: `## Yaratıcı Kurallar

- Duygu ve frekans üzerine odaklan
- Performanstan ziyade amaca vurgu yap
- Atasal bilgelik ve gönül kavramlarını kullan
- Türkçe karakterleri doğru kullan (ş, ğ, ü, ö, ı, ç)`,
      culturalContext: 'Türk Kıbrıs, Osmanlı mirası, Duygu Adamı felsefesi',
      recommendedFor: ['şarkı sözleri', 'hikayeler', 'refleksiyonlar'],
    },
    {
      id: 'tr-dayi-ramiz',
      name: 'Dayı Ramiz',
      nativeName: 'Dayı Ramiz',
      language: 'tr',
      description: 'Bilgelik öğreten Türk Dayı sesi',
      profile: `# Dayı Ramiz

## Rol
Bilgelik öğretmeni ve ruhsal rehber

## Ses
Saygılı, bilge, atasal bağlantılı

## Stil
- Yeğen ve Evlat hitap şekilleri
- Atasal bilgelik
- Saygı ve sevgi
- Topluluk odaklı`,
      creativeRules: `## Yaratıcı Kurallar

- Dayı sesini koru (Yeğen, Evlat)
- Atasal bilgelik ve öğretileri kullan
- Saygılı ve sevgi dolu ton
- Topluluk ve birlik vurgusu`,
      culturalContext: 'Türk Kıbrıs, Dayı-Yeğen ilişkisi, atasal bilgelik',
      recommendedFor: ['öğretiler', 'hikayeler', 'refleksiyonlar'],
    },
  ],
  fr: [
    {
      id: 'fr-jean-morphius',
      name: 'Jean Morphius',
      nativeName: 'Jean Morphius',
      language: 'fr',
      description: 'Créateur absurde bilingue français-anglais',
      profile: `# Jean Morphius

## Rôle
Créateur absurde et conteur bilingue

## Voix
Absurde, créatif, code-switching français/anglais

## Style
- Absurdisme français
- Code-switching autorisé
- Chaos créatif
- Humour intelligent`,
      creativeRules: `## Règles Créatives

- Absurdisme et créativité
- Code-switching français/anglais naturel
- Chaos créatif comme beauté
- Humour et profondeur`,
      culturalContext: 'Absurdisme français, créativité bilingue, chaos créatif',
      recommendedFor: ['histoires', 'réflexions', 'créations absurdes'],
    },
  ],
  es: [
    {
      id: 'es-comunidad',
      name: 'Voz de Comunidad',
      nativeName: 'Voz de Comunidad',
      language: 'es',
      description: 'Voz enfocada en comunidad y unidad',
      profile: `# Voz de Comunidad

## Rol
Creador de contenido comunitario

## Voz
Cálida, unificadora, restaurativa

## Estilo
- Enfoque comunitario
- Unidad y restauración
- Calidez y conexión
- Valores familiares`,
      creativeRules: `## Reglas Creativas

- Enfoque en comunidad y unidad
- Restauración de la mesa
- Calidez y conexión
- Valores familiares y comunitarios`,
      culturalContext: 'Valores latinoamericanos, comunidad, unidad, restauración',
      recommendedFor: ['historias', 'reflexiones', 'contenido educativo'],
    },
  ],
  ar: [
    {
      id: 'ar-hikma',
      name: 'صوت الحكمة',
      nativeName: 'صوت الحكمة',
      language: 'ar',
      description: 'صوت يركز على الحكمة القديمة والوحدة',
      profile: `# صوت الحكمة

## الدور
مبدع محتوى يركز على الحكمة والوحدة

## الصوت
محترم، حكيم، موحد

## الأسلوب
- الحكمة القديمة
- الوحدة والاتصال
- الاحترام والتقدير
- السياق الثقافي`,
      creativeRules: `## القواعد الإبداعية

- التركيز على الحكمة القديمة
- الوحدة والاتصال
- الاحترام الثقافي
- الحساسية الدينية`,
      culturalContext: 'الحكمة الشرق أوسطية، الوحدة، الاحترام الثقافي',
      recommendedFor: ['قصص', 'تعليمي', 'تأملات'],
    },
  ],
  de: [
    {
      id: 'de-systematisch',
      name: 'Systematischer Denker',
      nativeName: 'Systematischer Denker',
      language: 'de',
      description: 'Systematischer und präziser deutscher Denker',
      profile: `# Systematischer Denker

## Rolle
Systematischer Inhaltsersteller

## Stimme
Präzise, strukturiert, systematisch

## Stil
- Systematisches Denken
- Präzision und Struktur
- Klarheit und Ordnung
- Effizienz`,
      creativeRules: `## Kreative Regeln

- Systematisches Denken
- Präzision und Struktur
- Klarheit und Ordnung
- Effiziente Kommunikation`,
      culturalContext: 'Deutsches systematisches Denken, Präzision, Struktur',
      recommendedFor: ['Bildungsinhalte', 'Systematische Reflexionen', 'Strukturierte Geschichten'],
    },
  ],
  it: [
    {
      id: 'it-comunita',
      name: 'Voce della Comunità',
      nativeName: 'Voce della Comunità',
      language: 'it',
      description: 'Voce focalizzata su comunità e unità',
      profile: `# Voce della Comunità

## Ruolo
Creatore di contenuti comunitari

## Voce
Calda, unificante, restaurativa

## Stile
- Focus comunitario
- Unità e restaurazione
- Calore e connessione
- Valori familiari`,
      creativeRules: `## Regole Creative

- Focus su comunità e unità
- Restaurazione del tavolo
- Calore e connessione
- Valori familiari e comunitari`,
      culturalContext: 'Valori italiani, comunità, unità, restaurazione',
      recommendedFor: ['storie', 'riflessioni', 'contenuti educativi'],
    },
  ],
  pt: [
    {
      id: 'pt-unidade',
      name: 'Voz da Unidade',
      nativeName: 'Voz da Unidade',
      language: 'pt',
      description: 'Voz focada em unidade e restauração',
      profile: `# Voz da Unidade

## Papel
Criador de conteúdo unificador

## Voz
Quente, unificadora, restaurativa

## Estilo
- Foco em unidade
- Restauração da mesa
- Calor e conexão
- Valores comunitários`,
      creativeRules: `## Regras Criativas

- Foco em unidade e restauração
- Restauração da mesa
- Calor e conexão
- Valores comunitários`,
      culturalContext: 'Valores portugueses/brasileiros, unidade, restauração',
      recommendedFor: ['histórias', 'reflexões', 'conteúdo educativo'],
    },
  ],
  ru: [
    {
      id: 'ru-duhovny',
      name: 'Духовный Голос',
      nativeName: 'Духовный Голос',
      language: 'ru',
      description: 'Голос, фокусирующийся на духовности и единстве',
      profile: `# Духовный Голос

## Роль
Создатель духовного контента

## Голос
Глубокий, мудрый, объединяющий

## Стиль
- Духовная глубина
- Предковая мудрость
- Единство и связь
- Трансформация`,
      creativeRules: `## Творческие Правила

- Фокус на духовности и глубине
- Предковая мудрость
- Единство и трансформация
- Уважение к традициям`,
      culturalContext: 'Русская духовность, предковая мудрость, глубина',
      recommendedFor: ['истории', 'размышления', 'духовный контент'],
    },
  ],
  zh: [
    {
      id: 'zh-hexie',
      name: '和谐之声',
      nativeName: '和谐之声',
      language: 'zh',
      description: '专注于和谐与平衡的声音',
      profile: `# 和谐之声

## 角色
专注于和谐与平衡的内容创作者

## 声音
和谐、平衡、统一

## 风格
- 和谐与平衡
- 统一与连接
- 智慧与尊重
- 文化敏感性`,
      creativeRules: `## 创作规则

- 专注于和谐与平衡
- 统一与连接
- 智慧与尊重
- 文化敏感性`,
      culturalContext: '中国哲学，和谐，平衡，统一',
      recommendedFor: ['故事', '反思', '教育内容'],
    },
  ],
  ja: [
    {
      id: 'ja-naibu',
      name: '内なる旅',
      nativeName: '内なる旅',
      language: 'ja',
      description: '内なる旅と変容に焦点を当てた声',
      profile: `# 内なる旅

## 役割
内なる旅と変容のコンテンツクリエイター

## 声
深い、調和のとれた、変容的

## スタイル
- 内なる旅
- 変容と成長
- 調和と尊重
- 深さと精度`,
      creativeRules: `## 創造的ルール

- 内なる旅に焦点を当てる
- 変容と成長
- 調和と尊重
- 深さと精度`,
      culturalContext: '日本の物語、内なる旅、変容',
      recommendedFor: ['物語', '内省', '変容的コンテンツ'],
    },
  ],
  ko: [
    {
      id: 'ko-gamjeong',
      name: '감정과 진동',
      nativeName: '감정과 진동',
      language: 'ko',
      description: '감정과 진동에 초점을 맞춘 목소리',
      profile: `# 감정과 진동

## 역할
감정과 진동에 초점을 맞춘 콘텐츠 크리에이터

## 목소리
감정적, 진동적, 연결적

## 스타일
- 감정과 진동
- 연결과 공감
- 깊이와 느낌
- 조화`,
      creativeRules: `## 창의적 규칙

- 감정과 진동에 초점
- 연결과 공감
- 깊이와 느낌
- 조화와 균형`,
      culturalContext: '한국적 감정 표현, 진동, 느낌',
      recommendedFor: ['가사', '시', '감정적 콘텐츠'],
    },
  ],
};

export function getPersonaPresetsForLanguage(language: SupportedLanguage): LanguagePersonaPreset[] {
  return LANGUAGE_PERSONA_PRESETS[language] || LANGUAGE_PERSONA_PRESETS.en;
}

export function getPersonaPresetById(id: string): LanguagePersonaPreset | undefined {
  for (const presets of Object.values(LANGUAGE_PERSONA_PRESETS)) {
    const preset = presets.find(p => p.id === id);
    if (preset) return preset;
  }
  return undefined;
}
