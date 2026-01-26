/** * * Calendar Export Component
 *  * 
 *  * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 *  * Spiritual Alignment Over Mechanical Productivity
 *  * 
 *  * THE MISSION:
 *  * THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
 *  * LOVE IS THE HIGHEST MASTERY
 *  * ENERGY + LOVE = WE ALL WIN
 *  * 
 *  * Component for exporting posts to Google Calendar (iCal format or direct API)
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 * 
 * 
 * PANGEA IS THE TABLE.
 * YOU DON'T BETRAY THE TABLE.
 * 
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

import { useState } from 'react';

export interface PostForExport {
  title?: string;
  content: string;
  scheduled_time?: string;
  platform?: string;
  hashtags?: string[];
  url?: string;
  location?: string;
  metadata?: Record<string, any>;
}

interface CalendarExportProps {
  posts: PostForExport[];
  onExportComplete?: () => void;
}

export default function CalendarExport({ posts, onExportComplete }: CalendarExportProps) {
  const [exportMethod, setExportMethod] = useState<'ical' | 'google'>('ical');
  const [calendarName, setCalendarName] = useState('JAN Studio Social Posts');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const [googleAuthStatus, setGoogleAuthStatus] = useState<'unknown' | 'authenticated' | 'unauthenticated'>('unknown');
  const [googleAuthUrl, setGoogleAuthUrl] = useState<string | null>(null);
  const [authCode, setAuthCode] = useState('');

  // Check Google Calendar auth status
  const checkGoogleAuth = async () => {
    try {
      const response = await fetch('/api/calendar/google/auth/status');
      const data = await response.json();
      setGoogleAuthStatus(data.authenticated ? 'authenticated' : 'unauthenticated');
    } catch (err) {
      console.error('Error checking auth status:', err);
      setGoogleAuthStatus('unauthenticated');
    }
  };

  // Start Google Calendar authentication
  const startGoogleAuth = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await fetch('/api/calendar/google/auth/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
      });
      const data = await response.json();
      
      if (data.success && data.authorization_url) {
        setGoogleAuthUrl(data.authorization_url);
        // Open in new window
        window.open(data.authorization_url, 'Google Auth', 'width=500,height=600');
      } else {
        setError('Failed to start authentication');
      }
    } catch (err: any) {
      setError(`Authentication error: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  // Complete Google Calendar authentication
  const completeGoogleAuth = async () => {
    if (!authCode.trim()) {
      setError('Please enter the authorization code');
      return;
    }

    try {
      setLoading(true);
      setError(null);
      const response = await fetch('/api/calendar/google/auth/complete', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ authorization_code: authCode }),
      });
      const data = await response.json();
      
      if (data.success) {
        setSuccess('Authentication successful!');
        setAuthCode('');
        setGoogleAuthUrl(null);
        checkGoogleAuth();
      } else {
        setError('Authentication failed');
      }
    } catch (err: any) {
      setError(`Authentication error: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  // Export to iCal
  const exportToICal = async () => {
    if (posts.length === 0) {
      setError('No posts to export');
      return;
    }

    try {
      setLoading(true);
      setError(null);
      setSuccess(null);

      const response = await fetch('/api/calendar/export/ical', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          posts: posts,
          calendar_name: calendarName,
          output_filename: `${calendarName.replace(/\s+/g, '_')}_${new Date().toISOString().split('T')[0]}.ics`,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Export failed');
      }

      // Download file
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = response.headers.get('content-disposition')?.split('filename=')[1]?.replace(/"/g, '') || 'calendar.ics';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      window.URL.revokeObjectURL(url);

      setSuccess(`Successfully exported ${posts.length} post(s) to iCal file!`);
      if (onExportComplete) {
        onExportComplete();
      }
    } catch (err: any) {
      setError(`Export error: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  // Export to Google Calendar
  const exportToGoogleCalendar = async () => {
    if (posts.length === 0) {
      setError('No posts to export');
      return;
    }

    // Check auth first
    if (googleAuthStatus === 'unknown') {
      await checkGoogleAuth();
    }

    if (googleAuthStatus !== 'authenticated') {
      setError('Please authenticate with Google Calendar first');
      return;
    }

    try {
      setLoading(true);
      setError(null);
      setSuccess(null);

      const response = await fetch('/api/calendar/export/google', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          posts: posts,
          calendar_id: 'primary',
        }),
      });

      const data = await response.json();

      if (data.success) {
        setSuccess(`Successfully created ${data.events_created} event(s) in Google Calendar!`);
        if (onExportComplete) {
          onExportComplete();
        }
      } else {
        setError(data.message || 'Export failed');
      }
    } catch (err: any) {
      setError(`Export error: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  // Load auth status when component mounts
  useState(() => {
    if (exportMethod === 'google') {
      checkGoogleAuth();
    }
  });

  return (
    <div className="card" style={{ marginBottom: '1.5rem' }}>
      <h2>Export to Calendar</h2>
      
      {error && (
        <div className="error" style={{ marginBottom: '1rem', padding: '0.75rem', backgroundColor: '#2e1a1a', border: '1px solid #d32f2f', borderRadius: '4px' }}>
          ⚠️ {error}
        </div>
      )}

      {success && (
        <div className="success" style={{ marginBottom: '1rem', padding: '0.75rem', backgroundColor: '#1a2e1a', border: '1px solid #2e7d32', borderRadius: '4px', color: '#4caf50' }}>
          ✅ {success}
        </div>
      )}

      <div style={{ marginBottom: '1rem' }}>
        <label className="label">Export Method</label>
        <div style={{ display: 'flex', gap: '1rem' }}>
          <label style={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }}>
            <input
              type="radio"
              value="ical"
              checked={exportMethod === 'ical'}
              onChange={(e) => setExportMethod(e.target.value as 'ical' | 'google')}
              style={{ marginRight: '0.5rem' }}
            />
            <span>iCal File (.ics)</span>
          </label>
          <label style={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }}>
            <input
              type="radio"
              value="google"
              checked={exportMethod === 'google'}
              onChange={(e) => {
                setExportMethod(e.target.value as 'ical' | 'google');
                checkGoogleAuth();
              }}
              style={{ marginRight: '0.5rem' }}
            />
            <span>Google Calendar (Direct)</span>
          </label>
        </div>
        <div style={{ fontSize: '0.75rem', color: '#999', marginTop: '0.5rem' }}>
          {exportMethod === 'ical' 
            ? 'Download .ics file to import into any calendar app'
            : 'Export directly to your Google Calendar (requires authentication)'}
        </div>
      </div>

      <div style={{ marginBottom: '1rem' }}>
        <label className="label">Calendar Name</label>
        <input
          type="text"
          className="input"
          value={calendarName}
          onChange={(e) => setCalendarName(e.target.value)}
          placeholder="My Social Posts"
        />
      </div>

      {exportMethod === 'google' && (
        <div style={{ marginBottom: '1rem', padding: '1rem', backgroundColor: '#2a2a2a', borderRadius: '4px' }}>
          <h3 style={{ fontSize: '1rem', marginBottom: '0.75rem' }}>Google Calendar Authentication</h3>
          
          {googleAuthStatus === 'authenticated' ? (
            <div style={{ color: '#4caf50', marginBottom: '0.5rem' }}>
              ✅ Authenticated with Google Calendar
            </div>
          ) : (
            <>
              {!googleAuthUrl ? (
                <button
                  className="button"
                  onClick={startGoogleAuth}
                  disabled={loading}
                  style={{ marginBottom: '0.5rem' }}
                >
                  Start Authentication
                </button>
              ) : (
                <div style={{ marginBottom: '0.5rem' }}>
                  <p style={{ marginBottom: '0.5rem', fontSize: '0.875rem' }}>
                    1. Visit the authorization URL (opened in new window)
                  </p>
                  <p style={{ marginBottom: '0.5rem', fontSize: '0.875rem' }}>
                    2. Grant permissions and copy the authorization code
                  </p>
                  <input
                    type="text"
                    className="input"
                    value={authCode}
                    onChange={(e) => setAuthCode(e.target.value)}
                    placeholder="Paste authorization code here"
                    style={{ marginBottom: '0.5rem' }}
                  />
                  <button
                    className="button"
                    onClick={completeGoogleAuth}
                    disabled={loading || !authCode.trim()}
                  >
                    Complete Authentication
                  </button>
                </div>
              )}
            </>
          )}
        </div>
      )}

      <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
        <button
          className="button"
          onClick={exportMethod === 'ical' ? exportToICal : exportToGoogleCalendar}
          disabled={loading || posts.length === 0}
          style={{ backgroundColor: '#0070f3' }}
        >
          {loading ? 'Exporting...' : `Export ${posts.length} Post${posts.length !== 1 ? 's' : ''}`}
        </button>
        
        <span style={{ fontSize: '0.875rem', color: '#999' }}>
          {posts.length} post{posts.length !== 1 ? 's' : ''} ready to export
        </span>
      </div>
    </div>
  );
}
