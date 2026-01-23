import React, { useMemo } from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';
import { Bar } from 'react-chartjs-2';
import { HealthMetrics, CorrelationData } from '../types';
import { calculateCorrelations } from '../utils/dataProcessor';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

interface CorrelationEngineProps {
  metrics: HealthMetrics[];
}

export const CorrelationEngine: React.FC<CorrelationEngineProps> = ({ metrics }) => {
  const correlations = useMemo(() => calculateCorrelations(metrics), [metrics]);

  const saunaCorrelations = correlations.filter(c => c.activity === 'sauna');
  const swimmingCorrelations = correlations.filter(c => c.activity === 'swimming');

  const saunaData = {
    labels: saunaCorrelations.map(c => {
      const date = new Date(c.date);
      return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
    }),
    datasets: [
      {
        label: 'Vision Clarity Before',
        data: saunaCorrelations.map(c => c.vision_clarity_before ?? 0),
        backgroundColor: 'rgba(59, 130, 246, 0.6)',
        borderColor: 'rgb(59, 130, 246)',
        borderWidth: 1
      },
      {
        label: 'Vision Clarity After (2h)',
        data: saunaCorrelations.map(c => c.vision_clarity_after ?? 0),
        backgroundColor: 'rgba(34, 197, 94, 0.6)',
        borderColor: 'rgb(34, 197, 94)',
        borderWidth: 1
      },
      {
        label: 'Improvement',
        data: saunaCorrelations.map(c => c.improvement ?? 0),
        backgroundColor: 'rgba(236, 72, 153, 0.6)',
        borderColor: 'rgb(236, 72, 153)',
        borderWidth: 1
      }
    ]
  };

  const swimmingData = {
    labels: swimmingCorrelations.map(c => {
      const date = new Date(c.date);
      return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
    }),
    datasets: [
      {
        label: 'Vision Clarity Before',
        data: swimmingCorrelations.map(c => c.vision_clarity_before ?? 0),
        backgroundColor: 'rgba(59, 130, 246, 0.6)',
        borderColor: 'rgb(59, 130, 246)',
        borderWidth: 1
      },
      {
        label: 'Vision Clarity After (2h)',
        data: swimmingCorrelations.map(c => c.vision_clarity_after ?? 0),
        backgroundColor: 'rgba(34, 197, 94, 0.6)',
        borderColor: 'rgb(34, 197, 94)',
        borderWidth: 1
      },
      {
        label: 'Improvement',
        data: swimmingCorrelations.map(c => c.improvement ?? 0),
        backgroundColor: 'rgba(236, 72, 153, 0.6)',
        borderColor: 'rgb(236, 72, 153)',
        borderWidth: 1
      }
    ]
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: true,
        labels: {
          color: '#9ca3af'
        }
      },
      tooltip: {
        backgroundColor: 'rgba(17, 24, 39, 0.95)',
        titleColor: '#e5e7eb',
        bodyColor: '#d1d5db',
        borderColor: '#374151',
        borderWidth: 1
      }
    },
    scales: {
      x: {
        grid: {
          color: 'rgba(55, 65, 81, 0.5)'
        },
        ticks: {
          color: '#9ca3af'
        }
      },
      y: {
        grid: {
          color: 'rgba(55, 65, 81, 0.3)'
        },
        ticks: {
          color: '#9ca3af'
        },
        title: {
          display: true,
          text: 'Vision Clarity Score',
          color: '#9ca3af'
        }
      }
    }
  };

  const avgSaunaImprovement = saunaCorrelations.length > 0
    ? saunaCorrelations.reduce((sum, c) => sum + (c.improvement ?? 0), 0) / saunaCorrelations.length
    : 0;

  const avgSwimmingImprovement = swimmingCorrelations.length > 0
    ? swimmingCorrelations.reduce((sum, c) => sum + (c.improvement ?? 0), 0) / swimmingCorrelations.length
    : 0;

  return (
    <div className="correlation-engine">
      <h3 className="section-title">Activity Correlation Analysis</h3>
      <p className="section-subtitle">
        Vision Clarity changes 2 hours post-activity (Sauna & Swimming)
      </p>
      
      <div className="correlation-summary">
        <div className="summary-card">
          <div className="summary-label">Avg Sauna Improvement</div>
          <div className={`summary-value ${avgSaunaImprovement > 0 ? 'positive' : avgSaunaImprovement < 0 ? 'negative' : ''}`}>
            {avgSaunaImprovement > 0 ? '+' : ''}{avgSaunaImprovement.toFixed(2)}
          </div>
          <div className="summary-count">({saunaCorrelations.length} sessions)</div>
        </div>
        <div className="summary-card">
          <div className="summary-label">Avg Swimming Improvement</div>
          <div className={`summary-value ${avgSwimmingImprovement > 0 ? 'positive' : avgSwimmingImprovement < 0 ? 'negative' : ''}`}>
            {avgSwimmingImprovement > 0 ? '+' : ''}{avgSwimmingImprovement.toFixed(2)}
          </div>
          <div className="summary-count">({swimmingCorrelations.length} sessions)</div>
        </div>
      </div>

      {saunaCorrelations.length > 0 && (
        <div className="correlation-chart">
          <h4 className="chart-subtitle">Sauna Sessions</h4>
          <div className="chart-wrapper">
            <Bar data={saunaData} options={chartOptions} />
          </div>
        </div>
      )}

      {swimmingCorrelations.length > 0 && (
        <div className="correlation-chart">
          <h4 className="chart-subtitle">Swimming Sessions</h4>
          <div className="chart-wrapper">
            <Bar data={swimmingData} options={chartOptions} />
          </div>
        </div>
      )}

      {correlations.length === 0 && (
        <div className="no-data-message">
          No activity data available for correlation analysis.
        </div>
      )}
    </div>
  );
};

