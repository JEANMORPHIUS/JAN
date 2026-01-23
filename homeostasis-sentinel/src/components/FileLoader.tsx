import React, { useRef, useState } from 'react';
import { ParsedMarkdown } from '../types';
import { readMarkdownFilesFromInput, readMarkdownFilesFromDirectory } from '../utils/fileReader';

interface FileLoaderProps {
  onFilesLoaded: (files: ParsedMarkdown[]) => void;
}

export const FileLoader: React.FC<FileLoaderProps> = ({ onFilesLoaded }) => {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleFileSelect = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const files = event.target.files;
    if (!files || files.length === 0) return;

    setLoading(true);
    setError(null);

    try {
      const parsedFiles = await readMarkdownFilesFromInput(files);
      onFilesLoaded(parsedFiles);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load files');
    } finally {
      setLoading(false);
    }
  };

  const handleDirectorySelect = async () => {
    setLoading(true);
    setError(null);

    try {
      const parsedFiles = await readMarkdownFilesFromDirectory();
      onFilesLoaded(parsedFiles);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Directory selection not supported or failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="file-loader">
      <div className="loader-content">
        <h2 className="loader-title">Homeostasis Sentinel</h2>
        <p className="loader-subtitle">
          Track your transition into a zero-food, circadian-synced protocol
        </p>
        
        <div className="loader-options">
          <div className="loader-option">
            <button
              className="load-button primary"
              onClick={handleDirectorySelect}
              disabled={loading}
            >
              {loading ? 'Loading...' : 'Select Obsidian_Vault Folder'}
            </button>
            <p className="option-note">(Chrome/Edge only - uses File System Access API)</p>
          </div>
          
          <div className="loader-divider">
            <span>OR</span>
          </div>
          
          <div className="loader-option">
            <input
              ref={fileInputRef}
              type="file"
              multiple
              accept=".md"
              onChange={handleFileSelect}
              style={{ display: 'none' }}
            />
            <button
              className="load-button secondary"
              onClick={() => fileInputRef.current?.click()}
              disabled={loading}
            >
              {loading ? 'Loading...' : 'Select Markdown Files'}
            </button>
            <p className="option-note">Select multiple .md files from your Obsidian vault</p>
          </div>
        </div>

        {error && (
          <div className="loader-error">
            {error}
          </div>
        )}
      </div>
    </div>
  );
};

