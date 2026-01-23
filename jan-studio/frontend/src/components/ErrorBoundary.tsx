/**
 * Error Boundary Component
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 * 
 * Provides graceful error handling and recovery for the Creation Centre UI
 */

import React, { Component, ErrorInfo, ReactNode } from 'react';

interface Props {
  children: ReactNode;
  fallback?: ReactNode;
  onError?: (error: Error, errorInfo: ErrorInfo) => void;
}

interface State {
  hasError: boolean;
  error: Error | null;
  errorInfo: ErrorInfo | null;
}

export default class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = {
      hasError: false,
      error: null,
      errorInfo: null,
    };
  }

  static getDerivedStateFromError(error: Error): State {
    return {
      hasError: true,
      error,
      errorInfo: null,
    };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    this.setState({
      error,
      errorInfo,
    });

    // Log error
    console.error('ErrorBoundary caught an error:', error, errorInfo);

    // Call custom error handler if provided
    if (this.props.onError) {
      this.props.onError(error, errorInfo);
    }

    // You could also log to an error reporting service here
    // logErrorToService(error, errorInfo);
  }

  handleReset = () => {
    this.setState({
      hasError: false,
      error: null,
      errorInfo: null,
    });
  };

  handleReload = () => {
    window.location.reload();
  };

  render() {
    if (this.state.hasError) {
      // Custom fallback UI
      if (this.props.fallback) {
        return this.props.fallback;
      }

      // Default error UI
      return (
        <div
          style={{
            padding: '2rem',
            maxWidth: '800px',
            margin: '2rem auto',
            backgroundColor: '#1a1a1a',
            border: '2px solid #d32f2f',
            borderRadius: '8px',
          }}
          role="alert"
          aria-live="assertive"
        >
          <h2 style={{ color: '#d32f2f', marginBottom: '1rem' }}>
            ⚠️ Something went wrong
          </h2>
          
          <p style={{ color: '#e0e0e0', marginBottom: '1.5rem', lineHeight: '1.6' }}>
            An unexpected error occurred. This has been logged and we're working to fix it.
            You can try resetting the component or reloading the page.
          </p>

          {process.env.NODE_ENV === 'development' && this.state.error && (
            <details
              style={{
                marginBottom: '1.5rem',
                padding: '1rem',
                backgroundColor: '#0a0a0a',
                border: '1px solid #333',
                borderRadius: '4px',
              }}
            >
              <summary
                style={{
                  cursor: 'pointer',
                  color: '#999',
                  marginBottom: '0.5rem',
                  userSelect: 'none',
                }}
              >
                Error Details (Development)
              </summary>
              <pre
                style={{
                  color: '#d32f2f',
                  fontSize: '0.875rem',
                  overflow: 'auto',
                  whiteSpace: 'pre-wrap',
                  fontFamily: 'monospace',
                }}
              >
                {this.state.error.toString()}
                {this.state.errorInfo?.componentStack}
              </pre>
            </details>
          )}

          <div style={{ display: 'flex', gap: '1rem' }}>
            <button
              className="button"
              onClick={this.handleReset}
              style={{ backgroundColor: '#0070f3' }}
            >
              Try Again
            </button>
            <button
              className="button"
              onClick={this.handleReload}
              style={{ backgroundColor: '#666' }}
            >
              Reload Page
            </button>
            <button
              className="button"
              onClick={() => window.history.back()}
              style={{ backgroundColor: '#666' }}
            >
              Go Back
            </button>
          </div>

          <div style={{ marginTop: '1.5rem', paddingTop: '1.5rem', borderTop: '1px solid #333' }}>
            <p style={{ fontSize: '0.875rem', color: '#999', marginBottom: '0.5rem' }}>
              Need help? Contact support or check the documentation.
            </p>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}

/**
 * Hook for programmatic error reporting
 */
export function useErrorHandler() {
  const [error, setError] = React.useState<Error | null>(null);

  React.useEffect(() => {
    if (error) {
      throw error;
    }
  }, [error]);

  return React.useCallback((error: Error) => {
    setError(error);
  }, []);
}
