/** * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
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

'use client'

import { useState } from 'react'
import Link from 'next/link'
import { Lock, Mail, Truck } from 'lucide-react'

export default function Login() {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  })

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // In production, this would authenticate with your backend
    console.log('Login attempt:', formData)
    // Redirect to client dashboard
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }))
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full">
        {/* Logo */}
        <div className="text-center mb-8">
          <Link href="/" className="inline-flex items-center space-x-3">
            <div className="bg-navy p-3 rounded-lg">
              <Truck className="h-8 w-8 text-copper" />
            </div>
            <div>
              <h1 className="text-3xl font-heading font-bold text-navy">ATILOK</h1>
              <p className="text-sm text-steel font-body">Client Portal</p>
            </div>
          </Link>
        </div>

        {/* Login Card */}
        <div className="bg-white rounded-lg shadow-xl p-8">
          <h2 className="text-3xl font-heading font-bold text-navy mb-2 text-center">
            Client Login
          </h2>
          <p className="text-steel font-body text-center mb-8">
            Access your account to view orders, quotes, and account information
          </p>

          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label htmlFor="email" className="block text-sm font-heading font-semibold text-navy mb-2">
                Email Address
              </label>
              <div className="relative">
                <Mail className="absolute left-4 top-1/2 transform -translate-y-1/2 text-steel h-5 w-5" />
                <input
                  type="email"
                  id="email"
                  name="email"
                  required
                  value={formData.email}
                  onChange={handleChange}
                  className="w-full pl-12 pr-4 py-3 border-2 border-steel-light rounded-lg focus:border-copper focus:outline-none font-body"
                  placeholder="your.email@company.co.uk"
                />
              </div>
            </div>

            <div>
              <label htmlFor="password" className="block text-sm font-heading font-semibold text-navy mb-2">
                Password
              </label>
              <div className="relative">
                <Lock className="absolute left-4 top-1/2 transform -translate-y-1/2 text-steel h-5 w-5" />
                <input
                  type="password"
                  id="password"
                  name="password"
                  required
                  value={formData.password}
                  onChange={handleChange}
                  className="w-full pl-12 pr-4 py-3 border-2 border-steel-light rounded-lg focus:border-copper focus:outline-none font-body"
                  placeholder="Enter your password"
                />
              </div>
            </div>

            <div className="flex items-center justify-between">
              <label className="flex items-center">
                <input
                  type="checkbox"
                  className="w-4 h-4 text-copper border-steel-light rounded focus:ring-copper"
                />
                <span className="ml-2 text-sm text-steel font-body">Remember me</span>
              </label>
              <Link href="/forgot-password" className="text-sm text-copper hover:text-copper-dark font-body">
                Forgot password?
              </Link>
            </div>

            <button
              type="submit"
              className="btn-primary w-full"
            >
              Sign In
            </button>
          </form>

          <div className="mt-6 text-center">
            <p className="text-steel font-body text-sm">
              Don't have an account?{' '}
              <Link href="/contact" className="text-copper hover:text-copper-dark font-semibold">
                Contact us to get started
              </Link>
            </p>
          </div>
        </div>

        {/* Security Note */}
        <div className="mt-6 text-center">
          <p className="text-xs text-steel font-body">
            Secure login protected by industry-standard encryption
          </p>
        </div>
      </div>
    </div>
  )
}
