/** * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
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

import { useState, useEffect } from 'react';
import { getPersonas } from '@/api/personas';
import { generateContent } from '@/api/generation';
import PromptTemplates from './PromptTemplates';
import { useKeyboardShortcuts } from '@/hooks/useKeyboardShortcuts';
import { retryWithBackoff, getUserFriendlyError } from '@/utils/errorHandling';
import { useI18n } from '@/contexts/I18nContext';
import { detectLanguage, suggestLanguage } from '@/utils/languageDetection';
import { detectLanguage, suggestLanguage } from '@/utils/languageDetection';

interface GenerationFormProps {
  onGenerate: (result: GenerationResult) => void;
  onProgress?: (progress: number) => void;
}

export interface GenerationRequest {
  persona: string;
  prompt: string;
  output_type: string;
  options?: {
    length?: string;
    temperature?: number;
    language?: string;
    [key: string]: any;
  };
}

export interface GenerationResult {
  success: boolean;
  content?: string;
  persona?: string;
  prompt?: string;
  output_type?: string;
  validation?: {
    valid: boolean;
    violations: string[];
    warnings: string[];
    checks_performed: { [key: string]: boolean };
  };
  rules_applied?: string[];
  error?: string;
  timestamp: string;
}

const OUTPUT_TYPES = [
  { value: 'text', label: 'Text', description: 'General text content' },
  { value: 'story', label: 'Story', description: 'Short story or narrative' },
  { value: 'lyrics', label: 'Lyrics', description: 'Song lyrics' },
  { value: 'music', label: 'Music', description: 'Music prompt (Suno)' },
  { value: 'tts', label: 'TTS', description: 'Text-to-speech script' },
  { value: 'explanation', label: 'Explanation', description: 'Educational content' },
] as const;

export default function GenerationForm({ onGenerate, onProgress }: GenerationFormProps) {
  const { t, language, setLanguage } = useI18n();
  const [personas, setPersonas] = useState<string[]>([]);
  const [formData, setFormData] = useState<GenerationRequest>({
    persona: '',
    prompt: '',
    output_type: 'text',
    options: {
      language: language, // Include language in options
    },
  });
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);
  const [error, setError] = useState<string | null>(null);
  const [showTemplates, setShowTemplates] = useState(false);
  const [languageSuggestion, setLanguageSuggestion] = useState<{ lang: string; confidence: number } | null>(null);
  
  // Update language in formData when language changes
  useEffect(() => {
    setFormData(prev => ({
      ...prev,
      options: {
        ...prev.options,
        language: language,
      },
    }));
  }, [language]);
  
  // Detect language from prompt input
  useEffect(() => {
    if (formData.prompt.trim().length > 10) {
      const suggestion = suggestLanguage(formData.prompt, language);
      if (suggestion) {
        const detection = detectLanguage(formData.prompt);
        if (detection && detection.confidence > 0.5) {
          setLanguageSuggestion({
            lang: detection.language,
            confidence: detection.confidence,
          });
        } else {
          setLanguageSuggestion(null);
        }
      } else {
        setLanguageSuggestion(null);
      }
    } else {
      setLanguageSuggestion(null);
    }
  }, [formData.prompt, language]);
  
  // Keyboard shortcuts
  useKeyboardShortcuts([
    {
      key: 'Enter',
      ctrlKey: true,
      callback: () => {
        if (!loading && formData.persona && formData.prompt.trim()) {
          handleGenerate();
        }
      },
      description: 'Generate content',
    },
    {
      key: 's',
      ctrlKey: true,
      callback: () => {
        setShowTemplates(!showTemplates);
      },
      description: 'Toggle templates',
    },
  ]);

  useEffect(() => {
    loadPersonas();
  }, []);

  const loadPersonas = async () => {
    try {
      const data = await getPersonas();
      setPersonas(data);
      if (data.length > 0 && !formData.persona) {
        setFormData({ ...formData, persona: data[0] });
      }
    } catch (err) {
      console.error('Failed to load personas:', err);
    }
  };

  const handleGenerate = async () => {
    if (!formData.persona || !formData.prompt.trim()) {
      setError('Persona and prompt are required');
      return;
    }

    try {
      setLoading(true);
      setError(null);
      setProgress(0);
      setProgress(0);

      // Simulate progress (in real implementation, this would come from the API)
      const progressInterval = setInterval(() => {
        setProgress((prev) => {
          if (prev >= 90) {
            clearInterval(progressInterval);
            return 90;
          }
          return prev + 10;
        });
      }, 200);

      if (onProgress) {
        onProgress(0);
      }

      const result = await retryWithBackoff(
        () => generateContent(formData),
        3,
        1000
      );

      clearInterval(progressInterval);
      setProgress(100);

      if (onProgress) {
        onProgress(100);
      }

      // Add persona and prompt to result
      const resultWithContext = {
        ...result,
        persona: formData.persona,
        prompt: formData.prompt,
        output_type: formData.output_type,
      };

      // Save to history
      try {
        const { saveToHistory } = await import('@/api/generation');
        await saveToHistory(resultWithContext);
      } catch (err) {
        console.error('Failed to save to history:', err);
      }

      onGenerate(resultWithContext);
    } catch (err: any) {
      const errorMessage = getUserFriendlyError(err);
      setError(errorMessage);
      setProgress(0);
      if (onProgress) {
        onProgress(0);
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>{t('generate_content')}</h2>

      {error && (
        <div className="error" style={{ marginBottom: '1rem' }} role="alert" aria-live="assertive">
          {error}
        </div>
      )}

      <div style={{ marginBottom: '1.5rem' }}>
        <label className="label">
          {t('persona')} <span style={{ color: '#d32f2f' }}>*</span>
        </label>
        <select
          className="input"
          value={formData.persona}
          onChange={(e) => setFormData({ ...formData, persona: e.target.value })}
          disabled={loading}
          aria-label={t('select_persona')}
          aria-required="true"
        >
          <option value="">{t('select_persona')}...</option>
          {personas.map((persona) => (
            <option key={persona} value={persona}>
              {persona}
            </option>
          ))}
        </select>
      </div>

      <div style={{ marginBottom: '1.5rem' }}>
        <label className="label">
          {t('output_type')}
        </label>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '0.75rem' }}>
          {OUTPUT_TYPES.map((type) => (
            <div
              key={type.value}
              onClick={() => !loading && setFormData({ ...formData, output_type: type.value })}
              role="button"
              tabIndex={loading ? -1 : 0}
              aria-label={`Select ${type.label} output type`}
              aria-pressed={formData.output_type === type.value}
              onKeyDown={(e) => {
                if ((e.key === 'Enter' || e.key === ' ') && !loading) {
                  e.preventDefault();
                  setFormData({ ...formData, output_type: type.value });
                }
              }}
              style={{
                padding: '0.75rem',
                border: formData.output_type === type.value ? '2px solid #0070f3' : '1px solid #333',
                borderRadius: '4px',
                cursor: loading ? 'not-allowed' : 'pointer',
                backgroundColor: formData.output_type === type.value ? '#1a1a1a' : '#0a0a0a',
                opacity: loading ? 0.5 : 1,
                transition: 'all 0.2s',
                outline: '2px solid transparent',
                outlineOffset: '2px',
              }}
              onFocus={(e) => {
                e.currentTarget.style.outline = '2px solid #0070f3';
              }}
              onBlur={(e) => {
                e.currentTarget.style.outline = '2px solid transparent';
              }}
            >
              <div style={{ fontWeight: 600, marginBottom: '0.25rem', fontSize: '0.875rem' }}>
                {type.label}
              </div>
              <div style={{ fontSize: '0.75rem', color: '#999' }}>
                {type.description}
              </div>
            </div>
          ))}
        </div>
      </div>

      <div style={{ marginBottom: '1.5rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
          <label className="label">
            {t('prompt')} <span style={{ color: '#d32f2f' }}>*</span>
          </label>
          <button
            className="button"
            onClick={() => setShowTemplates(!showTemplates)}
            style={{ padding: '0.5rem 1rem', fontSize: '0.875rem' }}
            aria-label={t('show_templates')}
          >
            {showTemplates ? t('hide') : t('show')} {t('templates')}
          </button>
        </div>
        
        {showTemplates && (
          <div style={{ marginBottom: '1rem' }}>
            <PromptTemplates
              persona={formData.persona}
              onSelect={(template) => {
                setFormData({ ...formData, prompt: template.content });
                setShowTemplates(false);
              }}
              onClose={() => setShowTemplates(false)}
            />
          </div>
        )}
        
        <textarea
          className="textarea"
          value={formData.prompt}
          onChange={(e) => setFormData({ ...formData, prompt: e.target.value })}
          placeholder={t('prompt_placeholder')}
          disabled={loading}
          style={{ minHeight: '200px', fontFamily: 'inherit' }}
          aria-label={t('prompt_input')}
          aria-required="true"
          aria-describedby="prompt-char-count"
        />
        <div id="prompt-char-count" style={{ fontSize: '0.75rem', color: '#666', marginTop: '0.25rem' }} aria-live="polite">
          {formData.prompt.length} {t('characters')}
        </div>
        {languageSuggestion && languageSuggestion.lang !== language && (
          <div style={{
            marginTop: '0.75rem',
            padding: '0.75rem',
            backgroundColor: '#1a1a2a',
            border: '1px solid #0070f3',
            borderRadius: '4px',
            fontSize: '0.875rem',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
          }}>
            <span>
              🌍 {t('language_detected')}: <strong>{languageSuggestion.lang.toUpperCase()}</strong> ({Math.round(languageSuggestion.confidence * 100)}% {t('confidence')})
            </span>
            <button
              type="button"
              onClick={() => {
                setLanguage(languageSuggestion.lang as any);
                setLanguageSuggestion(null);
              }}
              style={{
                padding: '0.25rem 0.75rem',
                fontSize: '0.75rem',
                backgroundColor: '#0070f3',
                border: 'none',
                borderRadius: '4px',
                color: '#fff',
                cursor: 'pointer',
              }}
            >
              {t('switch_language')}
            </button>
          </div>
        )}
      </div>

      {loading && (
        <div style={{ marginBottom: '1rem' }} aria-live="polite" aria-busy="true">
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
            <span className="loading">{t('generating')}...</span>
            <span style={{ fontSize: '0.875rem', color: '#999' }}>{progress}%</span>
          </div>
          <div 
            role="progressbar"
            aria-valuenow={progress}
            aria-valuemin={0}
            aria-valuemax={100}
            aria-label="Generation progress"
            style={{
              width: '100%',
              height: '8px',
              backgroundColor: '#333',
              borderRadius: '4px',
              overflow: 'hidden',
            }}
          >
            <div style={{
              width: `${progress}%`,
              height: '100%',
              backgroundColor: '#0070f3',
              transition: 'width 0.3s',
            }} />
          </div>
        </div>
      )}

      <button
        className="button"
        onClick={handleGenerate}
        disabled={loading || !formData.persona || !formData.prompt.trim()}
        style={{ width: '100%' }}
        aria-label={t('generate_content')}
        aria-busy={loading}
      >
        {loading ? `${t('generating')}...` : `${t('generate_content')} (Ctrl+Enter)`}
      </button>
    </div>
  );
}

