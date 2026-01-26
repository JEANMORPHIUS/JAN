/** * * LIGHTHOUSE DASHBOARD
 *  * The Miracle-At-A-Glance Interface
 *  *
 *  * Philosophy: "Energy + Love = We All Win"
 *  * Design: High-Frequency Simplicity
 *  *
 *  * Three Sections:
 *  * 1. The Pulse - Your current status
 *  * 2. The Next Step - One clear action
 *  * 3. The Community Feed - Right spirits winning together
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

import { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import Head from 'next/head';
import { useAuth } from '../../contexts/AuthContext';
import { initConnectionDetection } from '../../utils/connectionDetector';
import { getPersonalizedGreeting } from '../../utils/greetings';
import { 
  checkUserVibration, 
  checkContentVibration, 
  updateUserVibration,
  type UserVibration,
  type VibrationCheckResult
} from '../../utils/vibrationCheck';

// Import Lighthouse CSS
import '../../styles/lighthouse.css';

interface PulseData {
  goal: string;
  progress: number;
  status: string;
  sacredWeight: 'High' | 'Medium' | 'Low';
}

interface NextStepData {
  task: string;
  description: string;
  file?: string;
  action: string;
}

interface FeedItem {
  id: string;
  entity: string;
  action: string;
  content: string;
  timestamp: Date;
}

export default function Dashboard() {
  const router = useRouter();
  const { user, isAuthenticated } = useAuth();
  const [greeting, setGreeting] = useState<string>('');
  const [pulseData, setPulseData] = useState<PulseData | null>(null);
  const [nextStep, setNextStep] = useState<NextStepData | null>(null);
  const [communityFeed, setCommunityFeed] = useState<FeedItem[]>([]);
  const [loading, setLoading] = useState(true);

  // Initialize connection detection on mount
  useEffect(() => {
    initConnectionDetection();
  }, []);

  // Generate greeting on mount
  useEffect(() => {
    setGreeting(getPersonalizedGreeting(user?.username));
  }, [user]);

  // Redirect to login if not authenticated
  useEffect(() => {
    if (!isAuthenticated) {
      router.push('/login?redirect=/dashboard');
    }
  }, [isAuthenticated, router]);

  // Load dashboard data
  useEffect(() => {
    if (isAuthenticated) {
      loadDashboardData();
      
      // Spiral Form: Rapid updates for high activity
      // Poll for updates every 30 seconds (can be optimized with WebSocket later)
      const updateInterval = setInterval(() => {
        loadDashboardData();
      }, 30000); // 30 seconds
      
      return () => clearInterval(updateInterval);
    }
  }, [isAuthenticated]);

  async function loadDashboardData() {
    try {
      // DIGITAL ALCHEMY: Check user vibration
      if (user?.id) {
        const vibration = checkUserVibration(user.id.toString(), 'dashboard');
        setUserVibration(vibration);
        
        // Update vibration for accessing dashboard (aligned interaction)
        updateUserVibration(user.id.toString(), 'dashboard_access', true);
      }
      
      // Load Module 1: The Sovereign Soul data
      // Spiral Form: Rapid updates - this can be replaced with API call later
      const moduleData = await import('../../data/module1_sovereign_soul.json');
      const module = moduleData.default || moduleData;
      
      // DIGITAL ALCHEMY: Check content vibration
      const contentVib = checkContentVibration(module);
      setContentVibration(contentVib);

      // Set Pulse Data from Module
      setPulseData({
        goal: module.module.title + ': ' + module.module.subtitle,
        progress: 0,
        status: 'Ready to Begin',
        sacredWeight: module.module.sacredWeight as 'High' | 'Medium' | 'Low',
      });

      // Set Next Step from Module
      if (module.nextSteps && module.nextSteps.length > 0) {
        const nextStepData = module.nextSteps[0];
        setNextStep({
          task: nextStepData.task,
          description: nextStepData.description,
          file: nextStepData.file || undefined,
          action: nextStepData.action,
        });
      }

      // Set Community Feed from Module
      if (module.communityFeed && module.communityFeed.length > 0) {
        const feedItems = module.communityFeed.map((item: any, index: number) => ({
          id: item.id || `feed-${index}`,
          entity: item.entity,
          action: item.action,
          content: item.content,
          timestamp: parseTimestamp(item.timestamp),
        }));
        setCommunityFeed(feedItems);
      }

      setLoading(false);
    } catch (error) {
      console.error('Failed to load dashboard data:', error);
      // Fallback to default data if JSON load fails
      setPulseData({
        goal: 'The Sovereign Soul: Identifying Your Light',
        progress: 0,
        status: 'Ready to Begin',
        sacredWeight: 'High',
      });
      setNextStep({
        task: 'Write down one "Holy Ambition"',
        description: 'Listen, mate, before we get into the technicals, we gotta anchor your spirit.',
        file: undefined,
        action: 'Begin Your Journey',
      });
      setLoading(false);
    }
  }

  function parseTimestamp(timestamp: string): Date {
    // Parse relative timestamps like "just now", "5 minutes ago", etc.
    if (timestamp === 'just now') {
      return new Date();
    }
    
    const minutesMatch = timestamp.match(/(\d+)\s*minutes?\s*ago/);
    if (minutesMatch) {
      return new Date(Date.now() - parseInt(minutesMatch[1]) * 60 * 1000);
    }
    
    const hoursMatch = timestamp.match(/(\d+)\s*hours?\s*ago/);
    if (hoursMatch) {
      return new Date(Date.now() - parseInt(hoursMatch[1]) * 60 * 60 * 1000);
    }
    
    return new Date();
  }

  function formatTimeAgo(date: Date): string {
    const seconds = Math.floor((new Date().getTime() - date.getTime()) / 1000);

    if (seconds < 60) return `${seconds}s ago`;
    if (seconds < 3600) return `${Math.floor(seconds / 60)}m ago`;
    if (seconds < 86400) return `${Math.floor(seconds / 3600)}h ago`;
    return `${Math.floor(seconds / 86400)}d ago`;
  }

  function handleStartTask() {
    // DIGITAL ALCHEMY: Track interaction as Note of Intent
    if (user?.id && nextStep) {
      updateUserVibration(user.id.toString(), `task_start_${nextStep.task}`, true);
    }
    
    // TODO: Navigate to task or open in IDE
    console.log('Starting task:', nextStep?.task);
    alert(`Task started: ${nextStep?.task}\n\nFile: ${nextStep?.file}`);
  }

  if (!isAuthenticated) {
    return null; // Will redirect to login
  }

  if (loading) {
    return (
      <div style={{ padding: '2rem', textAlign: 'center' }}>
        <p>Loading your lighthouse...</p>
      </div>
    );
  }

  return (
    <>
      <Head>
        <title>Dashboard | JAN Studio</title>
        <meta name="description" content="Your Lighthouse Dashboard" />
      </Head>

      <a href="#main-content" className="skip-link">
        Skip to main content
      </a>

      <main id="main-content" className="lighthouse-dashboard">
        {/* Greeting */}
        <h1 className="lighthouse-greeting">{greeting}</h1>

        {/* Section 1: The Pulse */}
        {pulseData && (
          <section className="lighthouse-pulse" aria-label="Current Status">
            <h2>The Pulse</h2>
            <div className="pulse-content">
              <div className="pulse-goal">{pulseData.goal}</div>

              <div className="pulse-status">
                <div className="pulse-progress-bar" role="progressbar" aria-valuenow={pulseData.progress} aria-valuemin={0} aria-valuemax={100}>
                  <div
                    className="pulse-progress-fill"
                    style={{ width: `${pulseData.progress}%` }}
                  />
                </div>
                <div className="pulse-percentage">{pulseData.progress}%</div>
              </div>

              <div className="pulse-meta">
                <div className="pulse-meta-item">
                  <span className="pulse-meta-label">Status</span>
                  <span className="pulse-meta-value">{pulseData.status}</span>
                </div>
                <div className="pulse-meta-item">
                  <span className="pulse-meta-label">Sacred Weight</span>
                  <span className={`pulse-meta-value ${pulseData.sacredWeight === 'High' ? 'sacred' : ''}`}>
                    {pulseData.sacredWeight}
                  </span>
                </div>
              </div>
            </div>
          </section>
        )}

        {/* Section 2: The Next Step */}
        {nextStep && (
          <section className="lighthouse-next-step" aria-label="Next Action">
            <h2>The Next Step</h2>
            <div className="next-step-content">
              <div className="next-step-task">{nextStep.task}</div>

              {nextStep.description && (
                <p className="next-step-description">{nextStep.description}</p>
              )}

              {nextStep.file && (
                <code className="next-step-file">{nextStep.file}</code>
              )}

              <button
                className="next-step-cta"
                onClick={handleStartTask}
                aria-label={`Start task: ${nextStep.task}`}
              >
                {nextStep.action}
              </button>
            </div>
          </section>
        )}

        {/* Section 3: The Community Feed */}
        <section className="lighthouse-community-feed" aria-label="Community Activity">
          <h2>The Community Feed</h2>

          {communityFeed.length > 0 ? (
            <ul className="feed-list" role="list">
              {communityFeed.map((item) => (
                <li key={item.id} className="feed-item">
                  <span className="feed-item-entity">{item.entity}</span>
                  {' '}
                  <span className="feed-item-action">{item.action}</span>
                  {' '}
                  <span className="feed-item-content">{item.content}</span>
                  <time className="feed-item-time" dateTime={item.timestamp.toISOString()}>
                    {formatTimeAgo(item.timestamp)}
                  </time>
                </li>
              ))}
            </ul>
          ) : (
            <div className="feed-empty">
              <p>No community activity yet</p>
              <p>Be the first to share your work 🕊️</p>
            </div>
          )}
        </section>
      </main>
    </>
  );
}
