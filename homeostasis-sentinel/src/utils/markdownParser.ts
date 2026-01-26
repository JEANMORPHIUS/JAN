import { ParsedMarkdown, HealthMetrics } from '../types';

/** * * Parse frontmatter from markdown content (browser-compatible)
 *  * Supports YAML frontmatter between --- delimiters
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
function parseFrontmatter(content: string): { data: Record<string, any>; body: string } {
  const frontmatterRegex = /^---\s*\n([\s\S]*?)\n---\s*\n([\s\S]*)$/;
  const match = content.match(frontmatterRegex);

  if (!match) {
    return { data: {}, body: content };
  }

  const frontmatterText = match[1];
  const body = match[2];

  // Simple YAML parser for key-value pairs
  const data: Record<string, any> = {};
  const lines = frontmatterText.split('\n');

  for (const line of lines) {
    const colonIndex = line.indexOf(':');
    if (colonIndex === -1) continue;

    const key = line.substring(0, colonIndex).trim();
    let value: any = line.substring(colonIndex + 1).trim();

    // Remove quotes if present
    if ((value.startsWith('"') && value.endsWith('"')) ||
        (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }

    // Parse boolean
    if (value === 'true' || value === 'True') value = true;
    else if (value === 'false' || value === 'False') value = false;
    // Parse number
    else if (!isNaN(Number(value)) && value !== '') value = Number(value);

    data[key] = value;
  }

  return { data, body };
}

/**
 * Extract health metrics from frontmatter
 */
function extractHealthMetrics(data: Record<string, any>): Partial<HealthMetrics> {
  return {
    vision_clarity: parseNumber(data.vision_clarity),
    muscle_tension: parseNumber(data.muscle_tension),
    loop_frequency: parseNumber(data.loop_frequency),
    sauna_duration: parseNumber(data.sauna_duration),
    circadian_sync_score: parseNumber(data.circadian_sync_score),
    swimming: data.swimming === true || data.swimming === 'true' || data.swimming === 'yes',
    blood_glucose: parseNumber(data.blood_glucose),
    glucose_time: typeof data.glucose_time === 'string' ? data.glucose_time : undefined,
    breath_quality: parseNumber(data.breath_quality),
    urine_color: parseNumber(data.urine_color),
    water_intake: parseNumber(data.water_intake),
    ketones: parseNumber(data.ketones),
    mental_emotional_sway: extractMentalEmotionalSway(data)
  };
}

function parseNumber(value: any): number | undefined {
  if (value === undefined || value === null || value === '') return undefined;
  const num = typeof value === 'string' ? parseFloat(value) : Number(value);
  return isNaN(num) ? undefined : num;
}

function extractMentalEmotionalSway(data: Record<string, any>): string | undefined {
  return data['mental_emotional_sway'] || data['Mental/Emotional Sway'] || data['mental_emotional_sway'];
}

/**
 * Parse markdown content and extract frontmatter
 */
export function parseMarkdownContent(content: string, filename: string): ParsedMarkdown {
  const { data, body } = parseFrontmatter(content);
  return {
    data: extractHealthMetrics(data),
    content: body,
    filename
  };
}

