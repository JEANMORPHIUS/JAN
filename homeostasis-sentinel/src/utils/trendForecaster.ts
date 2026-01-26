import { HealthMetrics, TrendForecast } from '../types';
import { parseISO, addHours } from 'date-fns';

/** * * Simple linear regression for trend forecasting
 *  * Predicts vision_clarity for the next 12 hours based on last 3 days
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
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/
export function forecastVisionClarity(metrics: HealthMetrics[]): TrendForecast | null {
  const sorted = [...metrics]
    .filter(m => m.vision_clarity !== undefined)
    .sort((a, b) => a.date!.localeCompare(b.date!));
  
  if (sorted.length < 3) {
    return null; // Need at least 3 data points
  }
  
  // Get last 3 days of data
  const recentData = sorted.slice(-3);
  
  // Simple linear regression: y = mx + b
  const n = recentData.length;
  const xValues = recentData.map((_, idx) => idx);
  const yValues = recentData.map(m => m.vision_clarity!);
  
  // Calculate means
  const xMean = xValues.reduce((sum, x) => sum + x, 0) / n;
  const yMean = yValues.reduce((sum, y) => sum + y, 0) / n;
  
  // Calculate slope (m)
  let numerator = 0;
  let denominator = 0;
  for (let i = 0; i < n; i++) {
    numerator += (xValues[i] - xMean) * (yValues[i] - yMean);
    denominator += (xValues[i] - xMean) ** 2;
  }
  
  const slope = denominator !== 0 ? numerator / denominator : 0;
  const intercept = yMean - slope * xMean;
  
  // Predict next value (x = n, which is 3 for the 4th day)
  const predictedValue = slope * n + intercept;
  
  // Calculate confidence based on data spread
  const variance = yValues.reduce((sum, y) => sum + (y - yMean) ** 2, 0) / n;
  const stdDev = Math.sqrt(variance);
  const confidence = Math.max(0, Math.min(100, 100 - (stdDev * 10))); // Inverse relationship
  
  // Determine trend
  let trend: 'improving' | 'declining' | 'stable' = 'stable';
  if (slope > 0.3) trend = 'improving';
  else if (slope < -0.3) trend = 'declining';
  
  // Determine alert level
  let alertLevel: 'none' | 'caution' | 'warning' | 'critical' = 'none';
  if (predictedValue < 3) alertLevel = 'critical';
  else if (predictedValue < 4) alertLevel = 'warning';
  else if (predictedValue < 5) alertLevel = 'caution';
  
  return {
    predictedVisionClarity: Math.max(0, Math.min(10, predictedValue)), // Clamp to 0-10
    confidence: Math.round(confidence),
    trend,
    hoursAhead: 12,
    alertLevel
  };
}

/**
 * Moving average with 6-hour window (refined for T1D zero-food protocol)
 * Uses last 6 hours of data instead of 3 days for more responsive predictions
 */
export function forecastVisionClarityMovingAverage(metrics: HealthMetrics[]): TrendForecast | null {
  const sorted = [...metrics]
    .filter(m => m.vision_clarity !== undefined)
    .sort((a, b) => a.date!.localeCompare(b.date!));

  if (sorted.length < 2) {
    return null;
  }

  // Get last 6 hours of data (or all available if less than 6 hours)
  const now = parseISO(sorted[sorted.length - 1].date!);
  const sixHoursAgo = new Date(now.getTime() - 6 * 60 * 60 * 1000);
  
  const recentData = sorted.filter(m => {
    const date = parseISO(m.date!);
    return date >= sixHoursAgo;
  });

  if (recentData.length < 2) {
    // Fallback to last 3 data points if 6-hour window has insufficient data
    const fallback = sorted.slice(-3);
    if (fallback.length < 2) return null;
    return calculateForecast(fallback);
  }

  return calculateForecast(recentData);
}

function calculateForecast(data: HealthMetrics[]): TrendForecast {
  const values = data.map(m => m.vision_clarity!);

  // Simple moving average with trend
  const avg = values.reduce((sum, v) => sum + v, 0) / values.length;
  const trend = values[values.length - 1] - values[0];

  // Weighted prediction (last value has more weight)
  const predictedValue = (avg * 0.6) + (values[values.length - 1] * 0.4) + (trend * 0.5);

  // Calculate variance for confidence
  const variance = values.reduce((sum, v) => sum + (v - avg) ** 2, 0) / values.length;
  const stdDev = Math.sqrt(variance);
  const confidence = Math.max(0, Math.min(100, 100 - (stdDev * 15)));

  let trendDirection: 'improving' | 'declining' | 'stable' = 'stable';
  if (trend > 0.5) trendDirection = 'improving';
  else if (trend < -0.5) trendDirection = 'declining';

  let alertLevel: 'none' | 'caution' | 'warning' | 'critical' = 'none';
  if (predictedValue < 3) alertLevel = 'critical';
  else if (predictedValue < 4) alertLevel = 'warning';
  else if (predictedValue < 5) alertLevel = 'caution';

  return {
    predictedVisionClarity: Math.max(0, Math.min(10, predictedValue)),
    confidence: Math.round(confidence),
    trend: trendDirection,
    hoursAhead: 12,
    alertLevel
  };
}

