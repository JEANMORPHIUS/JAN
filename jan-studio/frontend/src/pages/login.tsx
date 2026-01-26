/** * * Login Page - The Return
 *  * "The manor's been quiet without you. Ready to pick up where we left off?"
 *  *
 *  * Philosophy: Identity Over Data - Treat every user as a sacred key
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
import { useRouter } from 'next/router';
import { useAuth } from '../contexts/AuthContext';
import Link from 'next/link';
import Head from 'next/head';

export default function LoginPage() {
  const router = useRouter();
  const { login, isAuthenticated } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const redirect = router.query.redirect as string || '/dashboard';

  // Redirect if already authenticated
  if (isAuthenticated) {
    router.push(redirect);
    return null;
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      await login(email, password);
      // Success - redirect to intended page
      router.push(redirect);
    } catch (err: any) {
      // Error already translated to Duygu Adami in auth.ts
      setError(err.message || "The key didn't quite turn, mate. Give it another go.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <>
      <Head>
        <title>Login | JAN Studio</title>
        <meta name="description" content="Welcome back to the community" />
      </Head>

      <div style={styles.container}>
        <div style={styles.card}>
          {/* Icon */}
          <div style={styles.icon}>🕊️</div>

          {/* Headline */}
          <h1 style={styles.title}>Welcome back, brother.</h1>

          {/* Sub-headline */}
          <p style={styles.subtitle}>
            The manor's been quiet without you. Ready to pick up where we left off?
          </p>

          {/* Error message */}
          {error && (
            <div style={styles.error}>
              {error}
            </div>
          )}

          {/* Login form */}
          <form onSubmit={handleSubmit} style={styles.form}>
            <div style={styles.field}>
              <label htmlFor="email" style={styles.label}>
                Your Identity
              </label>
              <input
                id="email"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                style={styles.input}
                placeholder="email@example.com"
                autoComplete="email"
                autoFocus
              />
            </div>

            <div style={styles.field}>
              <label htmlFor="password" style={styles.label}>
                Your Key
              </label>
              <input
                id="password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                style={styles.input}
                placeholder="••••••••"
                autoComplete="current-password"
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              style={loading ? { ...styles.button, ...styles.buttonDisabled } : styles.button}
            >
              {loading ? 'Preparing your sanctuary...' : 'OPEN THE DOOR'}
            </button>
          </form>

          {/* Footer */}
          <div style={styles.footer}>
            <p style={styles.footerText}>
              New to the community?{' '}
              <Link href="/register" style={styles.link}>
                Step inside →
              </Link>
            </p>
          </div>
        </div>
      </div>
    </>
  );
}

const styles: { [key: string]: React.CSSProperties } = {
  container: {
    minHeight: '100vh',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    padding: '20px',
  },
  card: {
    backgroundColor: 'white',
    borderRadius: '12px',
    padding: '48px',
    boxShadow: '0 20px 60px rgba(0, 0, 0, 0.3)',
    width: '100%',
    maxWidth: '440px',
  },
  icon: {
    textAlign: 'center',
    fontSize: '48px',
    marginBottom: '24px',
  },
  title: {
    fontSize: '28px',
    fontWeight: '700',
    marginBottom: '12px',
    textAlign: 'center',
    color: '#1a1a1a',
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
  },
  subtitle: {
    fontSize: '16px',
    lineHeight: '1.5',
    marginBottom: '32px',
    textAlign: 'center',
    color: '#666',
  },
  error: {
    backgroundColor: '#fee',
    color: '#c33',
    padding: '14px',
    borderRadius: '8px',
    marginBottom: '24px',
    fontSize: '14px',
    lineHeight: '1.5',
    borderLeft: '4px solid #c33',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
    gap: '20px',
  },
  field: {
    display: 'flex',
    flexDirection: 'column',
    gap: '8px',
  },
  label: {
    fontSize: '14px',
    fontWeight: '600',
    color: '#333',
  },
  input: {
    padding: '14px',
    border: '2px solid #e0e0e0',
    borderRadius: '8px',
    fontSize: '16px',
    outline: 'none',
    transition: 'border-color 150ms',
  },
  button: {
    padding: '16px',
    background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    color: 'white',
    border: 'none',
    borderRadius: '8px',
    fontSize: '16px',
    fontWeight: '700',
    cursor: 'pointer',
    marginTop: '12px',
    textTransform: 'uppercase',
    letterSpacing: '0.5px',
    transition: 'transform 150ms, box-shadow 150ms',
  },
  buttonDisabled: {
    background: '#ccc',
    cursor: 'not-allowed',
    transform: 'none',
  },
  footer: {
    marginTop: '32px',
    paddingTop: '24px',
    borderTop: '1px solid #e0e0e0',
    textAlign: 'center',
  },
  footerText: {
    fontSize: '14px',
    color: '#666',
  },
  link: {
    color: '#667eea',
    textDecoration: 'none',
    fontWeight: '600',
    transition: 'color 150ms',
    cursor: 'pointer',
  },
};
