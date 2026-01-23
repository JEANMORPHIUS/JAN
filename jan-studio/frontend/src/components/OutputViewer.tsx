import { useState } from 'react';
import { GenerationResult } from './GenerationForm';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

interface OutputViewerProps {
  result: GenerationResult;
  personaName: string;
  onEditPersona?: () => void;
  onRegenerate?: () => void;
}

export default function OutputViewer({ result, personaName, onEditPersona, onRegenerate }: OutputViewerProps) {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    if (result.content) {
      navigator.clipboard.writeText(result.content);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  const handleDownload = () => {
    if (!result.content) return;

    const blob = new Blob([result.content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `generated-content-${new Date().toISOString().slice(0, 10)}.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  if (!result.success) {
    return (
      <div className="card">
        <h2>Generation Failed</h2>
        <div className="error" style={{ marginTop: '1rem' }}>
          {result.error || 'Unknown error occurred'}
        </div>
        {onRegenerate && (
          <button className="button" onClick={onRegenerate} style={{ marginTop: '1rem' }}>
            Try Again
          </button>
        )}
      </div>
    );
  }

  return (
    <div className="card">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <h2>Generated Content</h2>
        <div style={{ display: 'flex', gap: '0.5rem' }}>
          <button
            className="button"
            onClick={handleCopy}
            style={{ padding: '0.5rem 1rem', fontSize: '0.875rem' }}
          >
            {copied ? '✓ Copied' : 'Copy'}
          </button>
          <button
            className="button"
            onClick={handleDownload}
            style={{ padding: '0.5rem 1rem', fontSize: '0.875rem', backgroundColor: '#2e7d32' }}
          >
            Download
          </button>
        </div>
      </div>

      {result.validation && (
        <div style={{
          marginBottom: '1rem',
          padding: '1rem',
          backgroundColor: result.validation.valid ? '#1a2e1a' : '#2e1a1a',
          border: `1px solid ${result.validation.valid ? '#2e7d32' : '#d32f2f'}`,
          borderRadius: '4px',
        }}>
          <div style={{ display: 'flex', alignItems: 'center', marginBottom: '0.5rem' }}>
            <span style={{
              fontSize: '1.25rem',
              marginRight: '0.5rem',
            }}>
              {result.validation.valid ? '✅' : '❌'}
            </span>
            <strong>
              Validation: {result.validation.valid ? 'Passed' : 'Failed'}
            </strong>
          </div>

          {result.validation.violations.length > 0 && (
            <div style={{ marginTop: '0.75rem' }}>
              <div style={{ fontWeight: 600, marginBottom: '0.5rem', color: '#d32f2f' }}>
                Violations ({result.validation.violations.length}):
              </div>
              <ul style={{ marginLeft: '1.5rem', fontSize: '0.875rem' }}>
                {result.validation.violations.map((violation, idx) => (
                  <li key={idx} style={{ marginBottom: '0.25rem' }}>{violation}</li>
                ))}
              </ul>
            </div>
          )}

          {result.validation.warnings.length > 0 && (
            <div style={{ marginTop: '0.75rem' }}>
              <div style={{ fontWeight: 600, marginBottom: '0.5rem', color: '#ff9800' }}>
                Warnings ({result.validation.warnings.length}):
              </div>
              <ul style={{ marginLeft: '1.5rem', fontSize: '0.875rem' }}>
                {result.validation.warnings.map((warning, idx) => (
                  <li key={idx} style={{ marginBottom: '0.25rem' }}>{warning}</li>
                ))}
              </ul>
            </div>
          )}

          {result.validation.checks_performed && (
            <div style={{ marginTop: '0.75rem', fontSize: '0.875rem' }}>
              <div style={{ fontWeight: 600, marginBottom: '0.5rem' }}>Checks Performed:</div>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem' }}>
                {Object.entries(result.validation.checks_performed).map(([check, performed]) => (
                  <span
                    key={check}
                    style={{
                      padding: '0.25rem 0.5rem',
                      backgroundColor: performed ? '#1a2e1a' : '#2a2a2a',
                      border: `1px solid ${performed ? '#2e7d32' : '#666'}`,
                      borderRadius: '4px',
                      fontFamily: 'monospace',
                      fontSize: '0.75rem',
                    }}
                  >
                    {performed ? '✓' : '✗'} {check}
                  </span>
                ))}
              </div>
            </div>
          )}

          {!result.validation.valid && onEditPersona && (
            <div style={{ marginTop: '1rem', paddingTop: '1rem', borderTop: '1px solid #333' }}>
              <button
                className="button"
                onClick={onEditPersona}
                style={{ backgroundColor: '#ff9800' }}
              >
                Edit Persona Rules
              </button>
              <div style={{ fontSize: '0.75rem', color: '#999', marginTop: '0.5rem' }}>
                Some rules failed validation. Edit the persona to fix them.
              </div>
            </div>
          )}
        </div>
      )}

      {result.rules_applied && result.rules_applied.length > 0 && (
        <div style={{
          marginBottom: '1rem',
          padding: '0.75rem',
          backgroundColor: '#1a1a2a',
          border: '1px solid #333',
          borderRadius: '4px',
          fontSize: '0.875rem',
        }}>
          <div style={{ fontWeight: 600, marginBottom: '0.5rem' }}>Rules Applied:</div>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem' }}>
            {result.rules_applied.map((rule, idx) => (
              <span
                key={idx}
                style={{
                  padding: '0.25rem 0.5rem',
                  backgroundColor: '#0a0a1a',
                  border: '1px solid #444',
                  borderRadius: '4px',
                  fontFamily: 'monospace',
                  fontSize: '0.75rem',
                }}
              >
                {rule}
              </span>
            ))}
          </div>
        </div>
      )}

      <div style={{
        border: '1px solid #333',
        borderRadius: '4px',
        padding: '1.5rem',
        backgroundColor: '#0a0a0a',
        minHeight: '200px',
        maxHeight: '600px',
        overflowY: 'auto',
      }}>
        {result.content ? (
          <div style={{ fontFamily: 'monospace', whiteSpace: 'pre-wrap', lineHeight: '1.6' }}>
            <ReactMarkdown remarkPlugins={[remarkGfm]}>
              {result.content}
            </ReactMarkdown>
          </div>
        ) : (
          <div style={{ color: '#666', fontStyle: 'italic' }}>No content generated</div>
        )}
      </div>

      <div style={{ marginTop: '1rem', fontSize: '0.75rem', color: '#666' }}>
        Generated: {new Date(result.timestamp).toLocaleString()} | Persona: {personaName}
      </div>
    </div>
  );
}

