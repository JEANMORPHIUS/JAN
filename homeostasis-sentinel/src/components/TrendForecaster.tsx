/** * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
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

import React from 'react';
import { HealthMetrics, TrendForecast } from '../types';
import { forecastVisionClarityMovingAverage } from '../utils/trendForecaster';
import { checkHardDeckKillSwitch } from '../utils/biologicalLogic';

interface TrendForecasterProps {
  metrics: HealthMetrics[];
}

export const TrendForecaster: React.FC<TrendForecasterProps> = ({ metrics }) => {
  const forecast = forecastVisionClarityMovingAverage(metrics);

  if (!forecast) {
    return (
      <div className="trend-forecaster">
        <h3 className="section-title">Trend Forecaster: 12-Hour Pre-Alert</h3>
        <div className="no-data-message">
          Insufficient data for prediction. Need at least 3 data points.
        </div>
      </div>
    );
  }

  const alertClassMap = {
    none: 'alert-none',
    caution: 'alert-caution',
    warning: 'alert-warning',
    critical: 'alert-critical'
  };

  const trendIconMap = {
    improving: '↗️',
    declining: '↘️',
    stable: '→'
  };

  const alertMessages = {
    none: 'No immediate concerns',
    caution: 'Monitor closely',
    warning: 'Approaching Hard-Deck threshold',
    critical: 'CRITICAL: Immediate intervention recommended'
  };

  const killSwitch = checkHardDeckKillSwitch(forecast.predictedVisionClarity);

  return (
    <div className="trend-forecaster">
      <h3 className="section-title">Trend Forecaster: 12-Hour Pre-Alert</h3>
      <p className="section-subtitle">
        Predictive analysis to alert before hitting physical "Hard-Deck"
      </p>

      {killSwitch.isBreach && (
        <div className="kill-switch-alert">
          <div className="kill-switch-content">
            <div className="kill-switch-icon">🚨</div>
            <div className="kill-switch-text">
              <div className="kill-switch-title">CRITICAL SYSTEM BREACH</div>
              <div className="kill-switch-message">{killSwitch.alert}</div>
            </div>
          </div>
        </div>
      )}

      {killSwitch.alert && !killSwitch.isBreach && (
        <div className="kill-switch-warning">
          {killSwitch.alert}
        </div>
      )}

      <div className={`forecast-card ${alertClassMap[forecast.alertLevel]}`}>
        <div className="forecast-header">
          <div className="forecast-prediction">
            <div className="prediction-label">Predicted Vision Clarity</div>
            <div className="prediction-value">{forecast.predictedVisionClarity.toFixed(1)}/10</div>
            <div className="prediction-trend">
              <span className="trend-icon">{trendIconMap[forecast.trend]}</span>
              <span className="trend-label">{forecast.trend.toUpperCase()}</span>
            </div>
          </div>

          <div className="forecast-metrics">
            <div className="forecast-metric">
              <div className="metric-label">Confidence</div>
              <div className="metric-value">{forecast.confidence}%</div>
            </div>
            <div className="forecast-metric">
              <div className="metric-label">Horizon</div>
              <div className="metric-value">{forecast.hoursAhead}h</div>
            </div>
          </div>
        </div>

        <div className={`forecast-alert alert-${forecast.alertLevel}`}>
          <div className="alert-icon">
            {forecast.alertLevel === 'critical' && '🚨'}
            {forecast.alertLevel === 'warning' && '⚠️'}
            {forecast.alertLevel === 'caution' && '⚡'}
            {forecast.alertLevel === 'none' && '✅'}
          </div>
          <div className="alert-message">
            <strong>{alertMessages[forecast.alertLevel]}</strong>
            {forecast.alertLevel !== 'none' && (
              <span className="alert-detail">
                {' '}Predicted value {forecast.predictedVisionClarity.toFixed(1)} approaches threshold.
              </span>
            )}
          </div>
        </div>

        {forecast.alertLevel !== 'none' && (
          <div className="forecast-recommendation">
            <strong>Recommendation:</strong> Consider proactive intervention (flush, mechanical clearance, or loop adjustment) before reaching predicted threshold.
          </div>
        )}
      </div>
    </div>
  );
};

