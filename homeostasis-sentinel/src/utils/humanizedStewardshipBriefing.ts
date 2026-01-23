/**
 * HUMANIZED STEWARDSHIP BRIEFING UTILITIES
 * Transform statistical reports into human stories of resilience and stewardship
 */

import { HumanizedWeeklyReport } from '../types/humanDignity';
import { 
  GlucoseStatistics, 
  CommunityStewardshipScores,
  WeeklyTruthReport 
} from '../types/stewardshipBriefing';
import { EarthAlignment } from '../types/earthAlignment';
import { humanizeWeeklyReport } from './humanDignity';
import { generateWeeklyTruthReport, aggregateWeeklyGlucose, aggregateCommunityStewardship, forecastEarthPhases } from './stewardshipBriefing';
import { HealthMetrics } from '../types';
import { ExternalSystemFailure } from '../types/pierreLogic';
import { startOfWeek, endOfWeek, format } from 'date-fns';

/**
 * Generate Humanized Weekly Report
 * Transform statistical reports into human stories of resilience and stewardship
 */
export function generateHumanizedWeeklyReport(
  metrics: HealthMetrics[],
  stewardshipScoresByPartner: Record<string, { stewardshipScore: number; isActive: boolean }>,
  redTapeEvents: ExternalSystemFailure[],
  weekStartDate: Date = startOfWeek(new Date())
): {
  technicalReport: WeeklyTruthReport;
  humanizedReport: HumanizedWeeklyReport;
} {
  // Generate technical report first
  const technicalReport = generateWeeklyTruthReport(
    metrics,
    stewardshipScoresByPartner,
    redTapeEvents,
    weekStartDate
  );

  // Extract data for humanization
  const glucoseStats = technicalReport.dataAggregation.glucoseStats;
  const communityStewardship = technicalReport.dataAggregation.stewardshipScores;
  const earthAlignment: EarthAlignment = technicalReport.dataAggregation.earthPhases.upcoming7Days[0] 
    ? {
        solar: {
          hour: new Date().getHours(),
          phase: technicalReport.dataAggregation.earthPhases.upcoming7Days[0].solarPhase === 'sunrise' ? 'sunrise' :
                 technicalReport.dataAggregation.earthPhases.upcoming7Days[0].solarPhase === 'sunset' ? 'sunset' :
                 technicalReport.dataAggregation.earthPhases.upcoming7Days[0].solarPhase === 'solar_peak' ? 'solar_peak' : 'night',
          inSolarWindow: true,
          hoursFromSunrise: 0,
          hoursFromSunset: 0,
          solarIntensity: technicalReport.dataAggregation.earthPhases.upcoming7Days[0].solarIntensity
        },
        seasonal: {
          season: 'winter', // Default, should be calculated
          dayOfYear: new Date().getDate(),
          daysFromSolsticeEquinox: 0,
          seasonalIntensity: 50
        },
        lunar: {
          phase: technicalReport.dataAggregation.earthPhases.upcoming7Days[0].lunarPhase === 'new_moon' ? 'new_moon' :
                 technicalReport.dataAggregation.earthPhases.upcoming7Days[0].lunarPhase === 'full_moon' ? 'full_moon' :
                 technicalReport.dataAggregation.earthPhases.upcoming7Days[0].lunarPhase === 'waxing' ? 'waxing' : 'waning',
          daysFromNewMoon: 0,
          lunarIntensity: technicalReport.dataAggregation.earthPhases.upcoming7Days[0].lunarIntensity
        },
        circadian: {
          scnSyncScore: 70,
          phase: 'active',
          hoursFromCircadianPeak: 0,
          earthRotationAlignment: 70
        },
        symbioticScore: (technicalReport.dataAggregation.earthPhases.upcoming7Days[0].solarIntensity + 
                         technicalReport.dataAggregation.earthPhases.upcoming7Days[0].lunarIntensity) / 2,
        timestamp: new Date().toISOString()
      }
    : {
        solar: { hour: 12, phase: 'solar_peak', inSolarWindow: true, hoursFromSunrise: 6, hoursFromSunset: 6, solarIntensity: 100 },
        seasonal: { season: 'winter', dayOfYear: 1, daysFromSolsticeEquinox: 0, seasonalIntensity: 50 },
        lunar: { phase: 'new_moon', daysFromNewMoon: 0, lunarIntensity: 0 },
        circadian: { scnSyncScore: 70, phase: 'active', hoursFromCircadianPeak: 0, earthRotationAlignment: 70 },
        symbioticScore: 70,
        timestamp: new Date().toISOString()
      };

  const totalReadings = metrics.filter(m => {
    const metricDate = new Date(m.date);
    return metricDate >= weekStartDate && metricDate < endOfWeek(weekStartDate);
  }).length;

  // Generate humanized report
  const humanizedReport = humanizeWeeklyReport(
    glucoseStats,
    communityStewardship,
    earthAlignment,
    totalReadings
  );

  return {
    technicalReport,
    humanizedReport
  };
}
