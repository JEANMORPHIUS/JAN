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

interface GlucoseTrendProps {
  metrics: HealthMetrics[];
}

export const GlucoseTrend: React.FC<GlucoseTrendProps> = ({ metrics }) => {
  const glucoseData = metrics
    .filter(m => m.blood_glucose !== undefined)
    .sort((a, b) => a.date!.localeCompare(b.date!));

  if (glucoseData.length === 0) {
    return (
      <div className="glucose-trend">
        <h3 className="section-title">Blood Glucose Trends</h3>
        <div className="no-data-message">
          No glucose readings available. Add "blood_glucose" (mg/dL) to your markdown frontmatter.
        </div>
      </div>
    );
  }

  const labels = glucoseData.map(m => {
    const date = new Date(m.date!);
    const timeStr = m.glucose_time ? ` ${m.glucose_time}` : '';
    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' }) + timeStr;
  });

  const glucoseValues = glucoseData.map(m => m.blood_glucose ?? null);

  // Alert thresholds for T1D
  const highThreshold = 180; // mg/dL
  const lowThreshold = 70; // mg/dL
  const criticalLow = 54; // mg/dL

  // Highlight alert points
  const alertPoints = glucoseData.map((m, idx) => {
    const glucose = m.blood_glucose ?? 0;
    return (glucose > highThreshold || glucose < lowThreshold) ? idx : null;
  }).filter(idx => idx !== null) as number[];

  const data = {
    labels,
    datasets: [
      {
        label: 'Blood Glucose (mg/dL)',
        data: glucoseValues,
        borderColor: 'rgb(59, 130, 246)',
        backgroundColor: 'rgba(59, 130, 246, 0.1)',
        fill: true,
        tension: 0.4,
        pointRadius: (context: any) => {
          return alertPoints.includes(context.dataIndex) ? 6 : 3;
        },
        pointBackgroundColor: (context: any) => {
          const idx = context.dataIndex;
          const glucose = glucoseData[idx].blood_glucose ?? 0;
          if (glucose < criticalLow) return 'rgb(239, 68, 68)';
          if (glucose < lowThreshold) return 'rgb(251, 146, 60)';
          if (glucose > highThreshold) return 'rgb(239, 68, 68)';
          return 'rgb(59, 130, 246)';
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
        text: 'Blood Glucose Trends (Finger Prick Readings)',
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
        min: Math.max(0, Math.min(...glucoseValues.filter(v => v !== null) as number[]) - 20),
        max: Math.max(...glucoseValues.filter(v => v !== null) as number[]) + 20,
        title: {
          display: true,
          text: 'Glucose (mg/dL)',
          color: '#9ca3af'
        },
        grid: {
          color: 'rgba(55, 65, 81, 0.3)'
        },
        ticks: {
          color: '#9ca3af'
        }
      }
    },
    annotation: {
      annotations: [
        {
          type: 'line',
          yMin: highThreshold,
          yMax: highThreshold,
          borderColor: 'rgba(239, 68, 68, 0.5)',
          borderWidth: 2,
          borderDash: [5, 5],
          label: {
            content: 'High (180)',
            enabled: true
          }
        },
        {
          type: 'line',
          yMin: lowThreshold,
          yMax: lowThreshold,
          borderColor: 'rgba(251, 146, 60, 0.5)',
          borderWidth: 2,
          borderDash: [5, 5],
          label: {
            content: 'Low (70)',
            enabled: true
          }
        }
      ]
    }
  };

  const latestGlucose = glucoseData[glucoseData.length - 1].blood_glucose ?? 0;
  const highReadings = glucoseData.filter(m => (m.blood_glucose ?? 0) > highThreshold).length;
  const lowReadings = glucoseData.filter(m => (m.blood_glucose ?? 0) < lowThreshold).length;

  return (
    <div className="glucose-trend">
      <div className="chart-container">
        <div className="chart-wrapper">
          <Line data={data} options={options} />
        </div>
        
        <div className="glucose-summary">
          <div className="glucose-stat">
            <div className="stat-label">Latest Reading</div>
            <div className={`stat-value ${latestGlucose > highThreshold ? 'high' : latestGlucose < lowThreshold ? 'low' : 'normal'}`}>
              {latestGlucose} mg/dL
            </div>
          </div>
          {highReadings > 0 && (
            <div className="glucose-alert">
              <span className="alert-icon">⚠️</span>
              {highReadings} reading(s) above 180 mg/dL
            </div>
          )}
          {lowReadings > 0 && (
            <div className="glucose-alert low">
              <span className="alert-icon">⚠️</span>
              {lowReadings} reading(s) below 70 mg/dL
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

