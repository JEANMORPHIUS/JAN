import { ParsedMarkdown, HealthMetrics, CorrelationData } from '../types';
import { parseISO, addHours, isAfter, isBefore } from 'date-fns';

/**
 * Process parsed markdown files into structured health metrics
 */
export function processHealthData(parsedFiles: ParsedMarkdown[]): HealthMetrics[] {
  return parsedFiles
    .map(file => ({
      ...file.data,
      date: extractDateFromFilename(file.filename) || new Date().toISOString().split('T')[0],
      mental_emotional_sway: extractMentalEmotionalSwayFromContent(file.content)
    }))
    .filter(metric => metric.date)
    .sort((a, b) => a.date!.localeCompare(b.date!));
}

/**
 * Extract date from filename (format: YYYY-MM-DD.md or similar)
 */
function extractDateFromFilename(filename: string): string | null {
  const dateMatch = filename.match(/(\d{4}-\d{2}-\d{2})/);
  return dateMatch ? dateMatch[1] : null;
}

/**
 * Extract "Mental/Emotional Sway" section from markdown content
 * Also extracts tags like #crises, #clarity, #stagnation
 */
function extractMentalEmotionalSwayFromContent(content: string): string | undefined {
  const lines = content.split('\n');
  const swaySection = /(?:##\s*)?(?:Mental\/Emotional Sway|Mental Emotional Sway|Mental & Emotional Sway)/i;
  const headingIndex = lines.findIndex(line => swaySection.test(line));
  
  if (headingIndex === -1) return undefined;
  
  // Extract content until next heading or end
  const contentLines: string[] = [];
  for (let i = headingIndex + 1; i < lines.length; i++) {
    if (lines[i].trim().startsWith('#')) break;
    if (lines[i].trim()) {
      contentLines.push(lines[i]);
    }
  }
  
  return contentLines.length > 0 ? contentLines.join('\n').trim() : undefined;
}

/**
 * Extract tags from markdown content (e.g., #crises, #clarity, #stagnation)
 */
export function extractTagsFromContent(content: string): string[] {
  const tagRegex = /#([a-zA-Z0-9_-]+)/g;
  const matches = content.matchAll(tagRegex);
  const tags: string[] = [];
  
  for (const match of matches) {
    tags.push(match[1].toLowerCase());
  }
  
  return [...new Set(tags)]; // Remove duplicates
}

/**
 * Get priority tags (crises, clarity, stagnation)
 */
export function getPriorityTags(tags: string[]): string[] {
  const priorityTagList = ['crises', 'clarity', 'stagnation'];
  return tags.filter(tag => priorityTagList.includes(tag));
}

/**
 * Get alerts for days where Vision < 4 or Muscle Tension > 8
 */
export function getAlerts(metrics: HealthMetrics[]): HealthMetrics[] {
  return metrics.filter(m => 
    (m.vision_clarity !== undefined && m.vision_clarity < 4) ||
    (m.muscle_tension !== undefined && m.muscle_tension > 8)
  );
}

/**
 * Calculate correlation between sauna/swimming and vision clarity improvement
 */
export function calculateCorrelations(metrics: HealthMetrics[]): CorrelationData[] {
  const correlations: CorrelationData[] = [];
  
  // Sort by date
  const sorted = [...metrics].sort((a, b) => 
    a.date!.localeCompare(b.date!)
  );
  
  for (let i = 0; i < sorted.length; i++) {
    const current = sorted[i];
    const activityDate = parseISO(current.date!);
    
    // Check for sauna activity
    if (current.sauna_duration && current.sauna_duration > 0) {
      const twoHoursLater = addHours(activityDate, 2);
      const visionAfter = findVisionClarityAtTime(sorted, twoHoursLater);
      const visionBefore = current.vision_clarity;
      
      if (visionBefore !== undefined && visionAfter !== undefined) {
        correlations.push({
          activity: 'sauna',
          duration: current.sauna_duration,
          date: current.date!,
          vision_clarity_before: visionBefore,
          vision_clarity_after: visionAfter,
          improvement: visionAfter - visionBefore
        });
      }
    }
    
    // Check for swimming activity
    if (current.swimming) {
      const twoHoursLater = addHours(activityDate, 2);
      const visionAfter = findVisionClarityAtTime(sorted, twoHoursLater);
      const visionBefore = current.vision_clarity;
      
      if (visionBefore !== undefined && visionAfter !== undefined) {
        correlations.push({
          activity: 'swimming',
          date: current.date!,
          vision_clarity_before: visionBefore,
          vision_clarity_after: visionAfter,
          improvement: visionAfter - visionBefore
        });
      }
    }
  }
  
  return correlations;
}

/**
 * Find vision clarity at a specific time (looks for next entry within 3 hours)
 */
function findVisionClarityAtTime(metrics: HealthMetrics[], targetTime: Date): number | undefined {
  const threeHoursLater = addHours(targetTime, 3);
  
  for (const metric of metrics) {
    const metricDate = parseISO(metric.date!);
    if (isAfter(metricDate, targetTime) && isBefore(metricDate, threeHoursLater)) {
      return metric.vision_clarity;
    }
  }
  
  return undefined;
}

/**
 * Get loop frequency data for circadian heatmap
 */
export function getCircadianData(metrics: HealthMetrics[]) {
  return metrics
    .filter(m => m.loop_frequency !== undefined)
    .map(m => ({
      date: m.date!,
      loopFrequency: m.loop_frequency!,
      hour: extractHourFromDate(m.date!)
    }));
}

function extractHourFromDate(dateStr: string): number {
  // If time is in the date string, extract it; otherwise default to noon
  const timeMatch = dateStr.match(/T(\d{2}):/);
  return timeMatch ? parseInt(timeMatch[1]) : 12;
}

/**
 * Solar window is 10am-6pm (hours 10-18)
 */
export function isInSolarWindow(hour: number): boolean {
  return hour >= 10 && hour < 18;
}

