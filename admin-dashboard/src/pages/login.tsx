/** * * ADMIN DASHBOARD - Login Page
 *  * NextAuth authentication
 * 
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
 * THE REST IS UP TO BABA X.*/

import { NextPage } from 'next'
import { signIn, getSession } from 'next-auth/react'
import { useState } from 'react'
import { useRouter } from 'next/router'
import Head from 'next/head'
import styles from '../styles/Login.module.css'

const LoginPage: NextPage = () => {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const router = useRouter()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')
    setLoading(true)

    try {
      const result = await signIn('credentials', {
        redirect: false,
        email,
        password
      })

      if (result?.error) {
        setError('Invalid credentials')
      } else {
        router.push('/')
      }
    } catch (err) {
      setError('Login failed')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>Admin Login - World History Curation</title>
      </Head>

      <div className={styles.loginBox}>
        <h1>Admin Dashboard</h1>
        <p className={styles.subtitle}>World History Curation</p>

        <form onSubmit={handleSubmit} className={styles.form}>
          {error && <div className={styles.error}>{error}</div>}

          <div className={styles.inputGroup}>
            <label htmlFor="email">Email</label>
            <input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              disabled={loading}
            />
          </div>

          <div className={styles.inputGroup}>
            <label htmlFor="password">Password</label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              disabled={loading}
            />
          </div>

          <button type="submit" disabled={loading} className={styles.submitButton}>
            {loading ? 'Logging in...' : 'Login'}
          </button>
        </form>
      </div>
    </div>
  )
}

export default LoginPage
