/**
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
 * THE REST IS UP TO BABA X.
 * 
 * Loading State Component
 */

interface LoadingStateProps {
  message?: string;
  progress?: number;
  size?: 'small' | 'medium' | 'large';
}

export default function LoadingState({ 
  message = 'Loading...', 
  progress,
  size = 'medium' 
}: LoadingStateProps) {
  const sizeStyles = {
    small: { width: '20px', height: '20px', borderWidth: '2px' },
    medium: { width: '40px', height: '40px', borderWidth: '3px' },
    large: { width: '60px', height: '60px', borderWidth: '4px' },
  };
  
  const style = sizeStyles[size];
  
  return (
    <div 
      className="loading-container"
      style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '2rem',
        gap: '1rem',
      }}
      role="status"
      aria-live="polite"
      aria-busy="true"
    >
      <div
        className="spinner"
        style={{
          width: style.width,
          height: style.height,
          border: `${style.borderWidth} solid #333`,
          borderTop: `${style.borderWidth} solid #0070f3`,
          borderRadius: '50%',
          animation: 'spin 1s linear infinite',
        }}
        aria-hidden="true"
      />
      {message && (
        <div style={{ color: '#999', fontSize: '0.875rem' }}>
          {message}
        </div>
      )}
      {progress !== undefined && (
        <div
          role="progressbar"
          aria-valuenow={progress}
          aria-valuemin={0}
          aria-valuemax={100}
          style={{
            width: '100%',
            maxWidth: '200px',
            height: '4px',
            backgroundColor: '#333',
            borderRadius: '2px',
            overflow: 'hidden',
          }}
        >
          <div
            style={{
              width: `${progress}%`,
              height: '100%',
              backgroundColor: '#0070f3',
              transition: 'width 0.3s ease',
            }}
          />
        </div>
      )}
      <style jsx>{`
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
}
