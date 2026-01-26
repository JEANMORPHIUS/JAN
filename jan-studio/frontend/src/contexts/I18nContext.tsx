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
 * I18N Context for Global Expansion
 */

'use client';

import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export type SupportedLanguage = 'en' | 'tr' | 'fr' | 'es' | 'ar' | 'de' | 'it' | 'pt' | 'ru' | 'zh' | 'ja' | 'ko';

export interface LanguageInfo {
  code: SupportedLanguage;
  name: string;
  nativeName: string;
  flag?: string;
  rtl?: boolean;
}

export const SUPPORTED_LANGUAGES: LanguageInfo[] = [
  { code: 'en', name: 'English', nativeName: 'English', flag: '🇬🇧' },
  { code: 'tr', name: 'Turkish', nativeName: 'Türkçe', flag: '🇹🇷' },
  { code: 'fr', name: 'French', nativeName: 'Français', flag: '🇫🇷' },
  { code: 'es', name: 'Spanish', nativeName: 'Español', flag: '🇪🇸' },
  { code: 'ar', name: 'Arabic', nativeName: 'العربية', flag: '🇸🇦', rtl: true },
  { code: 'de', name: 'German', nativeName: 'Deutsch', flag: '🇩🇪' },
  { code: 'it', name: 'Italian', nativeName: 'Italiano', flag: '🇮🇹' },
  { code: 'pt', name: 'Portuguese', nativeName: 'Português', flag: '🇵🇹' },
  { code: 'ru', name: 'Russian', nativeName: 'Русский', flag: '🇷🇺' },
  { code: 'zh', name: 'Chinese', nativeName: '中文', flag: '🇨🇳' },
  { code: 'ja', name: 'Japanese', nativeName: '日本語', flag: '🇯🇵' },
  { code: 'ko', name: 'Korean', nativeName: '한국어', flag: '🇰🇷' },
];

interface I18nContextType {
  language: SupportedLanguage;
  setLanguage: (lang: SupportedLanguage) => void;
  t: (key: string, params?: Record<string, string | number>) => string;
  languages: LanguageInfo[];
  isLoading: boolean;
}

const I18nContext = createContext<I18nContextType | undefined>(undefined);

const defaultTranslations: Record<string, Record<SupportedLanguage, string>> = {
  // Core Mission
  'pangea_is_table': {
    en: 'PANGEA IS THE TABLE. YOU DON\'T BETRAY THE TABLE.',
    tr: 'PANGEA MASA\'DIR. MASA\'YA İHANET ETMEZSİN.',
    fr: 'LA PANGÉE EST LA TABLE. VOUS NE TRAHISSEZ PAS LA TABLE.',
    es: 'PANGEA ES LA MESA. NO TRAICIONAS LA MESA.',
    ar: 'بانجيا هي الطاولة. أنت لا تخون الطاولة.',
    de: 'PANGEA IST DER TISCH. DU VERÄTST DEN TISCH NICHT.',
    it: 'LA PANGEA È IL TAVOLO. NON TRADISCI IL TAVOLO.',
    pt: 'PANGEA É A MESA. VOCÊ NÃO TRAI A MESA.',
    ru: 'ПАНГЕЯ - ЭТО СТОЛ. ВЫ НЕ ПРЕДАЕТЕ СТОЛ.',
    zh: '盘古大陆是桌子。你不背叛桌子。',
    ja: 'パンゲアはテーブルです。テーブルを裏切らない。',
    ko: '판게아는 테이블입니다. 테이블을 배신하지 않습니다.',
  },
  'the_mission': {
    en: 'THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS. LOVE IS THE HIGHEST MASTERY. ENERGY + LOVE = WE ALL WIN. PEACE, LOVE, UNITY.',
    tr: 'BU DOĞRU RUHLA STEWARDSHIP VE TOPLULUKTUR. SEVGİ EN YÜKSEK USTALIKTIR. ENERJİ + SEVGİ = HEPİMİZ KAZANIRIZ. BARIŞ, SEVGİ, BİRLİK.',
    fr: 'C\'EST LA GESTION ET LA COMMUNAUTÉ AVEC LES BONS ESPRITS. L\'AMOUR EST LA MAÎTRISE LA PLUS ÉLEVÉE. ÉNERGIE + AMOUR = NOUS TOUS GAGNONS. PAIX, AMOUR, UNITÉ.',
    es: 'ESTO ES ADMINISTRACIÓN Y COMUNIDAD CON LOS ESPÍRITUS CORRECTOS. EL AMOR ES LA MAESTRÍA MÁS ALTA. ENERGÍA + AMOR = TODOS GANAMOS. PAZ, AMOR, UNIDAD.',
    ar: 'هذه هي الإدارة والمجتمع مع الأرواح الصحيحة. الحب هو أعلى إتقان. الطاقة + الحب = جميعنا نفوز. السلام، الحب، الوحدة.',
    de: 'DAS IST VERWALTUNG UND GEMEINSCHAFT MIT DEN RICHTIGEN GEISTERN. LIEBE IST DIE HÖCHSTE MEISTERSCHAFT. ENERGIE + LIEBE = WIR ALLE GEWINNEN. FRIEDEN, LIEBE, EINHEIT.',
    it: 'QUESTO È AMMINISTRAZIONE E COMUNITÀ CON GLI SPIRITI GIUSTI. L\'AMORE È LA MAESTRIA PIÙ ALTA. ENERGIA + AMORE = TUTTI VINCIAMO. PACE, AMORE, UNITÀ.',
    pt: 'ISTO É ADMINISTRAÇÃO E COMUNIDADE COM OS ESPÍRITOS CERTOS. O AMOR É A MAESTRIA MAIS ALTA. ENERGIA + AMOR = TODOS GANHAMOS. PAZ, AMOR, UNIDADE.',
    ru: 'ЭТО УПРАВЛЕНИЕ И СООБЩЕСТВО С ПРАВИЛЬНЫМИ ДУХАМИ. ЛЮБОВЬ - ЭТО ВЫСШЕЕ МАСТЕРСТВО. ЭНЕРГИЯ + ЛЮБОВЬ = МЫ ВСЕ ВЫИГРЫВАЕМ. МИР, ЛЮБОВЬ, ЕДИНСТВО.',
    zh: '这是正确的精神管理和社区。爱是最高的掌握。能量 + 爱 = 我们都赢。和平，爱，团结。',
    ja: 'これは正しい精神による管理とコミュニティです。愛は最高の習熟度です。エネルギー + 愛 = 私たち全員が勝つ。平和、愛、統一。',
    ko: '이것은 올바른 정신으로 하는 관리와 커뮤니티입니다. 사랑은 가장 높은 숙련도입니다. 에너지 + 사랑 = 우리 모두가 이깁니다. 평화, 사랑, 통일.',
  },
  // UI Strings
  'creation_centre': {
    en: 'Creation Centre',
    tr: 'Yaratım Merkezi',
    fr: 'Centre de Création',
    es: 'Centro de Creación',
    ar: 'مركز الإبداع',
    de: 'Erstellungszentrum',
    it: 'Centro di Creazione',
    pt: 'Centro de Criação',
    ru: 'Центр Создания',
    zh: '创作中心',
    ja: '創作センター',
    ko: '창작 센터',
  },
  'personas': {
    en: 'Personas',
    tr: 'Kişilikler',
    fr: 'Personas',
    es: 'Personas',
    ar: 'الشخصيات',
    de: 'Personas',
    it: 'Personas',
    pt: 'Personas',
    ru: 'Персоны',
    zh: '角色',
    ja: 'ペルソナ',
    ko: '페르소나',
  },
  'generate_content': {
    en: 'Generate Content',
    tr: 'İçerik Oluştur',
    fr: 'Générer du Contenu',
    es: 'Generar Contenido',
    ar: 'إنشاء المحتوى',
    de: 'Inhalt Generieren',
    it: 'Genera Contenuto',
    pt: 'Gerar Conteúdo',
    ru: 'Создать Контент',
    zh: '生成内容',
    ja: 'コンテンツを生成',
    ko: '콘텐츠 생성',
  },
  'templates': {
    en: 'Templates',
    tr: 'Şablonlar',
    fr: 'Modèles',
    es: 'Plantillas',
    ar: 'القوالب',
    de: 'Vorlagen',
    it: 'Modelli',
    pt: 'Modelos',
    ru: 'Шаблоны',
    zh: '模板',
    ja: 'テンプレート',
    ko: '템플릿',
  },
  'search': {
    en: 'Search',
    tr: 'Ara',
    fr: 'Rechercher',
    es: 'Buscar',
    ar: 'بحث',
    de: 'Suchen',
    it: 'Cerca',
    pt: 'Pesquisar',
    ru: 'Поиск',
    zh: '搜索',
    ja: '検索',
    ko: '검색',
  },
  'create_new_persona': {
    en: 'Create New Persona',
    tr: 'Yeni Kişilik Oluştur',
    fr: 'Créer un Nouveau Persona',
    es: 'Crear Nueva Persona',
    ar: 'إنشاء شخصية جديدة',
    de: 'Neue Persona Erstellen',
    it: 'Crea Nuova Persona',
    pt: 'Criar Nova Persona',
    ru: 'Создать Новую Персону',
    zh: '创建新角色',
    ja: '新しいペルソナを作成',
    ko: '새 페르소나 만들기',
  },
  'loading': {
    en: 'Loading...',
    tr: 'Yükleniyor...',
    fr: 'Chargement...',
    es: 'Cargando...',
    ar: 'جارٍ التحميل...',
    de: 'Laden...',
    it: 'Caricamento...',
    pt: 'Carregando...',
    ru: 'Загрузка...',
    zh: '加载中...',
    ja: '読み込み中...',
    ko: '로딩 중...',
  },
  'create_and_manage_personas': {
    en: 'Create and manage JAN personas',
    tr: 'JAN kişiliklerini oluştur ve yönet',
    fr: 'Créer et gérer les personas JAN',
    es: 'Crear y gestionar personas JAN',
    ar: 'إنشاء وإدارة شخصيات JAN',
    de: 'JAN-Personas erstellen und verwalten',
    it: 'Crea e gestisci personas JAN',
    pt: 'Criar e gerenciar personas JAN',
    ru: 'Создавать и управлять персонами JAN',
    zh: '创建和管理 JAN 角色',
    ja: 'JANペルソナを作成および管理',
    ko: 'JAN 페르소나 생성 및 관리',
  },
  'view_personas': {
    en: 'View personas',
    tr: 'Kişilikleri görüntüle',
    fr: 'Voir les personas',
    es: 'Ver personas',
    ar: 'عرض الشخصيات',
    de: 'Personas anzeigen',
    it: 'Visualizza personas',
    pt: 'Ver personas',
    ru: 'Просмотр персон',
    zh: '查看角色',
    ja: 'ペルソナを表示',
    ko: '페르소나 보기',
  },
  'view_templates': {
    en: 'View templates',
    tr: 'Şablonları görüntüle',
    fr: 'Voir les modèles',
    es: 'Ver plantillas',
    ar: 'عرض القوالب',
    de: 'Vorlagen anzeigen',
    it: 'Visualizza modelli',
    pt: 'Ver modelos',
    ru: 'Просмотр шаблонов',
    zh: '查看模板',
    ja: 'テンプレートを表示',
    ko: '템플릿 보기',
  },
  'select_persona': {
    en: 'Select a persona',
    tr: 'Bir kişilik seç',
    fr: 'Sélectionner un persona',
    es: 'Seleccionar una persona',
    ar: 'اختر شخصية',
    de: 'Persona auswählen',
    it: 'Seleziona una persona',
    pt: 'Selecionar uma persona',
    ru: 'Выберите персону',
    zh: '选择一个角色',
    ja: 'ペルソナを選択',
    ko: '페르소나 선택',
  },
  'output_type': {
    en: 'Output Type',
    tr: 'Çıktı Türü',
    fr: 'Type de Sortie',
    es: 'Tipo de Salida',
    ar: 'نوع الإخراج',
    de: 'Ausgabetyp',
    it: 'Tipo di Output',
    pt: 'Tipo de Saída',
    ru: 'Тип Вывода',
    zh: '输出类型',
    ja: '出力タイプ',
    ko: '출력 유형',
  },
  'prompt': {
    en: 'Prompt',
    tr: 'İstem',
    fr: 'Invite',
    es: 'Solicitud',
    ar: 'المطالبة',
    de: 'Eingabeaufforderung',
    it: 'Prompt',
    pt: 'Solicitação',
    ru: 'Запрос',
    zh: '提示',
    ja: 'プロンプト',
    ko: '프롬프트',
  },
  'prompt_placeholder': {
    en: 'Enter your prompt here... Describe what you want to generate. Or use templates above.',
    tr: 'İsteminizi buraya girin... Oluşturmak istediğinizi açıklayın. Veya yukarıdaki şablonları kullanın.',
    fr: 'Entrez votre invite ici... Décrivez ce que vous voulez générer. Ou utilisez les modèles ci-dessus.',
    es: 'Ingrese su solicitud aquí... Describa lo que desea generar. O use las plantillas arriba.',
    ar: 'أدخل مطالبتك هنا... اشرح ما تريد إنشاؤه. أو استخدم القوالب أعلاه.',
    de: 'Geben Sie hier Ihre Eingabeaufforderung ein... Beschreiben Sie, was Sie generieren möchten. Oder verwenden Sie die Vorlagen oben.',
    it: 'Inserisci il tuo prompt qui... Descrivi cosa vuoi generare. O usa i modelli sopra.',
    pt: 'Digite sua solicitação aqui... Descreva o que deseja gerar. Ou use os modelos acima.',
    ru: 'Введите ваш запрос здесь... Опишите, что вы хотите создать. Или используйте шаблоны выше.',
    zh: '在此输入您的提示... 描述您想要生成的内容。或使用上面的模板。',
    ja: 'ここにプロンプトを入力... 生成したいものを説明してください。または上記のテンプレートを使用してください。',
    ko: '여기에 프롬프트를 입력하세요... 생성하고 싶은 것을 설명하세요. 또는 위의 템플릿을 사용하세요.',
  },
  'prompt_input': {
    en: 'Prompt input',
    tr: 'İstem girişi',
    fr: 'Saisie d\'invite',
    es: 'Entrada de solicitud',
    ar: 'إدخال المطالبة',
    de: 'Eingabeaufforderung',
    it: 'Input prompt',
    pt: 'Entrada de solicitação',
    ru: 'Ввод запроса',
    zh: '提示输入',
    ja: 'プロンプト入力',
    ko: '프롬프트 입력',
  },
  'characters': {
    en: 'characters',
    tr: 'karakter',
    fr: 'caractères',
    es: 'caracteres',
    ar: 'أحرف',
    de: 'Zeichen',
    it: 'caratteri',
    pt: 'caracteres',
    ru: 'символов',
    zh: '字符',
    ja: '文字',
    ko: '문자',
  },
  'generating': {
    en: 'Generating',
    tr: 'Oluşturuluyor',
    fr: 'Génération',
    es: 'Generando',
    ar: 'جارٍ الإنشاء',
    de: 'Generieren',
    it: 'Generazione',
    pt: 'Gerando',
    ru: 'Создание',
    zh: '生成中',
    ja: '生成中',
    ko: '생성 중',
  },
  'show': {
    en: 'Show',
    tr: 'Göster',
    fr: 'Afficher',
    es: 'Mostrar',
    ar: 'عرض',
    de: 'Anzeigen',
    it: 'Mostra',
    pt: 'Mostrar',
    ru: 'Показать',
    zh: '显示',
    ja: '表示',
    ko: '표시',
  },
  'hide': {
    en: 'Hide',
    tr: 'Gizle',
    fr: 'Masquer',
    es: 'Ocultar',
    ar: 'إخفاء',
    de: 'Ausblenden',
    it: 'Nascondi',
    pt: 'Ocultar',
    ru: 'Скрыть',
    zh: '隐藏',
    ja: '非表示',
    ko: '숨기기',
  },
  'show_templates': {
    en: 'Show prompt templates',
    tr: 'İstem şablonlarını göster',
    fr: 'Afficher les modèles d\'invite',
    es: 'Mostrar plantillas de solicitud',
    ar: 'عرض قوالب المطالبة',
    de: 'Eingabeaufforderungsvorlagen anzeigen',
    it: 'Mostra modelli prompt',
    pt: 'Mostrar modelos de solicitação',
    ru: 'Показать шаблоны запросов',
    zh: '显示提示模板',
    ja: 'プロンプトテンプレートを表示',
    ko: '프롬프트 템플릿 표시',
  },
};

export function I18nProvider({ children }: { children: ReactNode }) {
  const [language, setLanguageState] = useState<SupportedLanguage>('en');
  const [translations, setTranslations] = useState<Record<string, Record<SupportedLanguage, string>>>(defaultTranslations);
  const [isLoading, setIsLoading] = useState(false);

  // Load language preference from localStorage
  useEffect(() => {
    const saved = localStorage.getItem('jan-language-preference');
    if (saved && SUPPORTED_LANGUAGES.some(l => l.code === saved)) {
      setLanguageState(saved as SupportedLanguage);
    }
  }, []);

  // Load translations from API
  useEffect(() => {
    const loadTranslations = async () => {
      try {
        setIsLoading(true);
        const response = await axios.get(`${API_BASE_URL}/api/i18n/translations/${language}`);
        if (response.data && response.data.translations) {
          setTranslations(prev => ({
            ...prev,
            ...response.data.translations,
          }));
        }
      } catch (err) {
        console.warn('Failed to load translations from API, using defaults:', err);
      } finally {
        setIsLoading(false);
      }
    };

    loadTranslations();
  }, [language]);

  const setLanguage = (lang: SupportedLanguage) => {
    setLanguageState(lang);
    localStorage.setItem('jan-language-preference', lang);
    document.documentElement.lang = lang;
    const langInfo = SUPPORTED_LANGUAGES.find(l => l.code === lang);
    if (langInfo?.rtl) {
      document.documentElement.dir = 'rtl';
    } else {
      document.documentElement.dir = 'ltr';
    }
  };

  const t = (key: string, params?: Record<string, string | number>): string => {
    const translation = translations[key]?.[language] || translations[key]?.['en'] || key;
    
    if (params) {
      return Object.entries(params).reduce(
        (str, [paramKey, paramValue]) => str.replace(`{{${paramKey}}}`, String(paramValue)),
        translation
      );
    }
    
    return translation;
  };

  return (
    <I18nContext.Provider value={{ language, setLanguage, t, languages: SUPPORTED_LANGUAGES, isLoading }}>
      {children}
    </I18nContext.Provider>
  );
}

export function useI18n() {
  const context = useContext(I18nContext);
  if (!context) {
    throw new Error('useI18n must be used within I18nProvider');
  }
  return context;
}
