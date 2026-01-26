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
 * Export Options Component
 */

import { useState } from 'react';

interface ExportOptionsProps {
  content: string;
  filename?: string;
  onClose?: () => void;
}

type ExportFormat = 'txt' | 'md' | 'html' | 'json';

export default function ExportOptions({ content, filename = 'export', onClose }: ExportOptionsProps) {
  const [format, setFormat] = useState<ExportFormat>('md');
  const [includeMetadata, setIncludeMetadata] = useState(true);

  const handleExport = () => {
    let exportContent = content;
    let mimeType = 'text/plain';
    let extension = format;

    if (format === 'html') {
      exportContent = `<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>${filename}</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 800px; margin: 0 auto; padding: 2rem; line-height: 1.6; }
    pre { background: #f5f5f5; padding: 1rem; border-radius: 4px; overflow-x: auto; }
  </style>
</head>
<body>
  <pre>${content.replace(/</g, '&lt;').replace(/>/g, '&gt;')}</pre>
</body>
</html>`;
      mimeType = 'text/html';
    } else if (format === 'json') {
      exportContent = JSON.stringify({
        content,
        exported_at: new Date().toISOString(),
        format: 'markdown',
      }, null, 2);
      mimeType = 'application/json';
    } else if (format === 'md') {
      mimeType = 'text/markdown';
    } else {
      mimeType = 'text/plain';
    }

    if (includeMetadata) {
      const metadata = `\n\n---\nExported: ${new Date().toLocaleString()}\nFormat: ${format.toUpperCase()}\n---\n`;
      if (format !== 'json') {
        exportContent += metadata;
      }
    }

    const blob = new Blob([exportContent], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${filename}.${extension}`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);

    if (onClose) {
      onClose();
    }
  };

  return (
    <div className="card">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <h2>Export Content</h2>
        {onClose && (
          <button
            className="button"
            onClick={onClose}
            aria-label="Close export options"
          >
            Close
          </button>
        )}
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
        <div>
          <label style={{ display: 'block', marginBottom: '0.5rem', fontSize: '0.875rem' }}>
            Export Format
          </label>
          <select
            className="input"
            value={format}
            onChange={(e) => setFormat(e.target.value as ExportFormat)}
            style={{ width: '100%' }}
            aria-label="Select export format"
          >
            <option value="md">Markdown (.md)</option>
            <option value="txt">Plain Text (.txt)</option>
            <option value="html">HTML (.html)</option>
            <option value="json">JSON (.json)</option>
          </select>
        </div>

        <div>
          <label style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', cursor: 'pointer' }}>
            <input
              type="checkbox"
              checked={includeMetadata}
              onChange={(e) => setIncludeMetadata(e.target.checked)}
            />
            <span style={{ fontSize: '0.875rem' }}>Include metadata (export date, format)</span>
          </label>
        </div>

        <button
          className="button"
          onClick={handleExport}
          style={{ width: '100%', backgroundColor: '#2e7d32' }}
          aria-label={`Export as ${format.toUpperCase()}`}
        >
          Export as {format.toUpperCase()}
        </button>
      </div>
    </div>
  );
}
