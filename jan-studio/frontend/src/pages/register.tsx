/**
 * Register Page - The Invitation
 * "Every miracle needs a home base. Claim your space in the community, mate."
 *
 * Philosophy: Identity Over Data - Treat every user as a sacred key
 */

import { useState } from 'react';
import { useRouter } from 'next/router';
import { useAuth } from '../contexts/AuthContext';
import Link from 'next/link';
import Head from 'next/head';

export default function RegisterPage() {
  const router = useRouter();
  const { register, isAuthenticated } = useAuth();
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  // Redirect if already authenticated
  if (isAuthenticated) {
    router.push('/dashboard');
    return null;
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError('');

    // Client-side validation with Duygu Adami messages
    if (username.length < 3) {
      setError('A bit more, mate. At least 3 characters for your name.');
      return;
    }

    if (password.length < 8) {
      setError('Strengthen your key: needs at least 8 characters.');
      return;
    }

    if (!/[A-Z]/.test(password)) {
      setError('Strengthen your key: needs at least one uppercase letter.');
      return;
    }

    if (!/[a-z]/.test(password)) {
      setError('Strengthen your key: needs at least one lowercase letter.');
      return;
    }

    if (!/[0-9]/.test(password)) {
      setError('Strengthen your key: needs at least one number.');
      return;
    }

    if (password !== confirmPassword) {
      setError("Keys don't match, mate. Try again?");
      return;
    }

    setLoading(true);

    try {
      await register(username, email, password);
      // Success - redirect to dashboard
      router.push('/dashboard');
    } catch (err: any) {
      // Error already translated to Duygu Adami in auth.ts
      setError(err.message || "Something's not quite right. Give it another try?");
    } finally {
      setLoading(false);
    }
  }

  return (
    <>
      <Head>
        <title>Join the Community | JAN Studio</title>
        <meta name="description" content="Claim your space in the community" />
      </Head>

      <div style={styles.container}>
        <div style={styles.card}>
          {/* Icon */}
          <div style={styles.icon}>🕊️</div>

          {/* Headline */}
          <h1 style={styles.title}>Join the Circle.</h1>

          {/* Sub-headline */}
          <p style={styles.subtitle}>
            Every miracle needs a home base. Claim your space in the community, mate.
          </p>

          {/* Error message */}
          {error && (
            <div style={styles.error}>
              {error}
            </div>
          )}

          {/* Registration form */}
          <form onSubmit={handleSubmit} style={styles.form}>
            <div style={styles.field}>
              <label htmlFor="username" style={styles.label}>
                How should we call you? (Name)
              </label>
              <input
                id="username"
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
                style={styles.input}
                placeholder="karasahin"
                minLength={3}
                maxLength={30}
                autoComplete="username"
                autoFocus
              />
            </div>

            <div style={styles.field}>
              <label htmlFor="email" style={styles.label}>
                Your Identity (for login)
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
              />
            </div>

            <div style={styles.field}>
              <label htmlFor="password" style={styles.label}>
                Your Secret Word (keep this safe)
              </label>
              <input
                id="password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                style={styles.input}
                placeholder="••••••••"
                autoComplete="new-password"
              />
            </div>

            <div style={styles.field}>
              <label htmlFor="confirmPassword" style={styles.label}>
                Confirm Your Secret Word
              </label>
              <input
                id="confirmPassword"
                type="password"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                required
                style={styles.input}
                placeholder="••••••••"
                autoComplete="new-password"
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              style={loading ? { ...styles.button, ...styles.buttonDisabled } : styles.button}
            >
              {loading ? 'Preparing your sanctuary...' : 'STEP INSIDE'}
            </button>
          </form>

          {/* Footer */}
          <div style={styles.footer}>
            <p style={styles.footerText}>
              Already have an account?{' '}
              <Link href="/login" style={styles.link}>
                The door is here →
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
    maxWidth: '480px',
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
  },
};
