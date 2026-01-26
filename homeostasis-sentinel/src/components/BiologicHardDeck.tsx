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

import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler
} from 'chart.js';
import { Line } from 'react-chartjs-2';
import { HealthMetrics } from '../types';
import { detectAcidosisRisk } from '../utils/biologicalLogic';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler
);

interface BiologicHardDeckProps {
  metrics: HealthMetrics[];
}

export const BiologicHardDeck: React.FC<BiologicHardDeckProps> = ({ metrics }) => {
  const alerts = metrics.filter(m => 
    (m.vision_clarity !== undefined && m.vision_clarity < 4) ||
    (m.muscle_tension !== undefined && m.muscle_tension > 8)
  );

  const acidosisRisk = detectAcidosisRisk(metrics);

  const labels = metrics.map(m => {
    const date = new Date(m.date!);
    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
  });

  const visionData = metrics.map(m => m.vision_clarity ?? null);
  const tensionData = metrics.map(m => m.muscle_tension ?? null);

  // Highlight alert points
  const alertPoints = metrics.map((m, idx) => {
    const isAlert = (m.vision_clarity !== undefined && m.vision_clarity < 4) ||
                   (m.muscle_tension !== undefined && m.muscle_tension > 8);
    return isAlert ? idx : null;
  }).filter(idx => idx !== null) as number[];

  const data = {
    labels,
    datasets: [
      {
        label: 'Vision Clarity (1-10)',
        data: visionData,
        borderColor: 'rgb(59, 130, 246)',
        backgroundColor: 'rgba(59, 130, 246, 0.1)',
        yAxisID: 'y',
        fill: true,
        tension: 0.4,
        pointRadius: (context: any) => {
          return alertPoints.includes(context.dataIndex) ? 6 : 3;
        },
        pointBackgroundColor: (context: any) => {
          const idx = context.dataIndex;
          const metric = metrics[idx];
          if (metric.vision_clarity !== undefined && metric.vision_clarity < 4) {
            return 'rgb(239, 68, 68)';
          }
          return 'rgb(59, 130, 246)';
        }
      },
      {
        label: 'Muscle Tension (1-10)',
        data: tensionData,
        borderColor: 'rgb(236, 72, 153)',
        backgroundColor: 'rgba(236, 72, 153, 0.1)',
        yAxisID: 'y1',
        fill: true,
        tension: 0.4,
        pointRadius: (context: any) => {
          return alertPoints.includes(context.dataIndex) ? 6 : 3;
        },
        pointBackgroundColor: (context: any) => {
          const idx = context.dataIndex;
          const metric = metrics[idx];
          if (metric.muscle_tension !== undefined && metric.muscle_tension > 8) {
            return 'rgb(239, 68, 68)';
          }
          return 'rgb(236, 72, 153)';
        }
      }
    ]
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    interaction: {
      mode: 'index' as const,
      intersect: false,
    },
    plugins: {
      title: {
        display: true,
        text: 'Biologic Hard-Deck',
        color: '#e5e7eb',
        font: {
          size: 18,
          weight: '600' as const
        }
      },
      legend: {
        display: true,
        labels: {
          color: '#9ca3af',
          font: {
            size: 12
          }
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
          color: '#9ca3af',
          maxRotation: 45,
          minRotation: 45
        }
      },
      y: {
        type: 'linear' as const,
        display: true,
        position: 'left' as const,
        min: 0,
        max: 10,
        title: {
          display: true,
          text: 'Vision Clarity',
          color: '#9ca3af'
        },
        grid: {
          color: 'rgba(55, 65, 81, 0.3)'
        },
        ticks: {
          color: '#9ca3af'
        }
      },
      y1: {
        type: 'linear' as const,
        display: true,
        position: 'right' as const,
        min: 0,
        max: 10,
        title: {
          display: true,
          text: 'Muscle Tension',
          color: '#9ca3af'
        },
        grid: {
          drawOnChartArea: false,
        },
        ticks: {
          color: '#9ca3af'
        }
      }
    }
  };

  return (
    <div className="chart-container">
      <div className="chart-wrapper">
        <Line data={data} options={options} />
      </div>
      {alerts.length > 0 && (
        <div className="alert-summary">
          <p className="alert-count">
            <span className="alert-icon">⚠️</span>
            {alerts.length} alert{alerts.length !== 1 ? 's' : ''} detected (Vision &lt; 4 or Tension &gt; 8)
          </p>
        </div>
      )}

      {acidosisRisk.isActive && (
        <div className={`acidosis-alert alert-${acidosisRisk.severity}`}>
          <div className="acidosis-header">
            <span className="acidosis-icon">🚨</span>
            <strong>SYSTEM ACIDIC - "Sway" Detected</strong>
          </div>
          <div className="acidosis-details">
            <p>{acidosisRisk.consecutiveDays} consecutive day(s) with high tension (&gt;7) and low vision (&lt;5)</p>
            <p className="acidosis-recommendation">
              <strong>Action:</strong> {acidosisRisk.recommendation}
            </p>
          </div>
        </div>
      )}
    </div>
  );
};

