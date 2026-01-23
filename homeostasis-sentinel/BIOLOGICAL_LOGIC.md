# Biological Logic Implementation

This document describes the biological logic integrated into the Homeostasis Sentinel dashboard for T1D/urine therapy protocol tracking.

## 1. Acidosis Risk Predictor ("Sway" Logic)

### Purpose
In T1D, the absence of insulin leads to ketone production (acid). When the blood becomes acidic, the nervous system "sways."

### Trigger Conditions
- `muscle_tension > 7` AND `vision_clarity < 5` for **more than two consecutive data points**

### Action
- Display high-priority "SYSTEM ACIDIC" warning
- Severity levels: Low (2 days), Medium (2-3 days), High (4+ days)

### Recommendation Engine
- **Flush recommended**: Increased pure water/alkaline hydration
- **Avoid Loop re-integration** until muscle tension drops below 5

### Implementation
- Function: `detectAcidosisRisk()` in `src/utils/biologicalLogic.ts`
- Component: Integrated into `BiologicHardDeck.tsx` and `BiologicalAlerts.tsx`

---

## 2. Osmotic Pressure Coefficient

### Purpose
Vision blur in T1D is usually caused by glucose-induced swelling of the eye lens (osmotic pressure).

### Logic
- Calculate delta (Δ) between `loop_frequency` and `vision_clarity`
- Formula: `Δ = loop_frequency - vision_clarity`

### Insight
If `loop_frequency` is high but `vision_clarity` is decreasing, the "Loop" is likely re-introducing too much glucose for the current activity level to burn.

### Trigger
- `loop_frequency > 6` AND vision declining AND `Δ > 2`

### Action
- Display "MECHANICAL CLEARANCE REQUIRED" alert
- Recommendation: Swim/Sauna/Movement to clear glucose-induced osmotic pressure

### Implementation
- Function: `calculateOsmoticPressure()` in `src/utils/biologicalLogic.ts`
- Component: Displayed in `BiologicalAlerts.tsx`

---

## 3. Enhanced Circadian Compliance Scoring

### Purpose
Re-ingesting melatonin-heavy "night urine" during solar peak or glucose-heavy "day urine" during repair phase (night) disrupts the Suprachiasmatic Nucleus (SCN).

### Logic
- Penalize `circadian_sync_score` if `loop_frequency` increments occur **outside 08:00 - 20:00** range
- Penalty: **-5 points per violation**
- Minimum adjusted score: 0

### Solar Window
- **Target window**: 10 AM - 6 PM (10:00 - 18:00)
- **Compliance window**: 08:00 - 20:00 (8 AM - 8 PM)

### Implementation
- Function: `calculateEnhancedCircadianScore()` in `src/utils/biologicalLogic.ts`
- Component: Displayed in `BiologicalAlerts.tsx`

---

## 4. Trend Forecaster

### Purpose
Predict `vision_clarity` for the next 12 hours to provide a "pre-alert" before hitting the physical "Hard-Deck."

### Method
- Uses **moving average** with trend analysis on last 3 days of data
- Calculates confidence based on data variance
- Determines trend: improving, declining, or stable

### Alert Levels
- **None**: Predicted value ≥ 5
- **Caution**: Predicted value < 5
- **Warning**: Predicted value < 4
- **Critical**: Predicted value < 3

### Implementation
- Function: `forecastVisionClarityMovingAverage()` in `src/utils/trendForecaster.ts`
- Component: `TrendForecaster.tsx`

---

## 5. Project Journal Tag Parsing

### Priority Tags
The system prioritizes these tags in journal entries:
- `#crises` - Critical events or issues
- `#clarity` - Moments of clear insight or improvement
- `#stagnation` - Periods of no progress or stuck states

### Implementation
- Functions: `extractTagsFromContent()` and `getPriorityTags()` in `src/utils/dataProcessor.ts`
- Component: `ProjectJournal.tsx` displays priority tags with special styling

---

## Integration

All biological logic is integrated into the dashboard:

1. **BiologicalAlerts** component (top of dashboard)
   - Shows active alerts for acidosis, osmotic pressure, and circadian violations

2. **TrendForecaster** component
   - Provides 12-hour prediction with alert levels

3. **BiologicHardDeck** component
   - Enhanced with acidosis risk alerts

4. **ProjectJournal** component
   - Enhanced with tag parsing and priority tag display

---

## Usage Notes

### Data Requirements
- Minimum 3 data points for trend forecasting
- Consecutive data points needed for acidosis detection
- Date/time information needed for circadian compliance (if available)

### Alert Hierarchy
1. **Critical**: Acidosis risk (high severity) OR Trend forecast critical
2. **Warning**: Acidosis risk (medium) OR Osmotic clearance required OR Trend forecast warning
3. **Caution**: Trend forecast caution OR Circadian violations

---

**Last Updated**: 2025-01-13

