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
import { Menu, X, Truck } from 'lucide-react'

export default function Navigation() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <nav className="bg-white shadow-md sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-20">
          {/* Logo */}
          <Link href="/" className="flex items-center space-x-3 group">
            <div className="bg-navy p-2 rounded-lg group-hover:bg-navy-light transition-smooth">
              <Truck className="h-6 w-6 text-copper" />
            </div>
            <div>
              <h1 className="text-2xl font-heading font-bold text-navy">ATILOK</h1>
              <p className="text-xs text-steel font-body">Reliability in Motion</p>
            </div>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-8">
            <Link href="/" className="text-navy hover:text-copper font-body font-medium transition-smooth">
              Home
            </Link>
            <Link href="/about" className="text-navy hover:text-copper font-body font-medium transition-smooth">
              About Us
            </Link>
            <Link href="/catalogue" className="text-navy hover:text-copper font-body font-medium transition-smooth">
              Catalogue
            </Link>
            <Link href="/supply-chain" className="text-navy hover:text-copper font-body font-medium transition-smooth">
              Supply Chain
            </Link>
            <Link href="/contact" className="btn-primary">
              Request Quote
            </Link>
            <Link href="/login" className="text-steel hover:text-navy font-body font-medium transition-smooth">
              Client Login
            </Link>
          </div>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="md:hidden text-navy hover:text-copper transition-smooth"
            aria-label="Toggle menu"
          >
            {isOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
          </button>
        </div>

        {/* Mobile Navigation */}
        {isOpen && (
          <div className="md:hidden pb-4 space-y-3 animate-slide-in">
            <Link href="/" className="block text-navy hover:text-copper font-body font-medium py-2">
              Home
            </Link>
            <Link href="/about" className="block text-navy hover:text-copper font-body font-medium py-2">
              About Us
            </Link>
            <Link href="/catalogue" className="block text-navy hover:text-copper font-body font-medium py-2">
              Catalogue
            </Link>
            <Link href="/supply-chain" className="block text-navy hover:text-copper font-body font-medium py-2">
              Supply Chain
            </Link>
            <Link href="/contact" className="block btn-primary text-center">
              Request Quote
            </Link>
            <Link href="/login" className="block text-steel hover:text-navy font-body font-medium py-2">
              Client Login
            </Link>
          </div>
        )}
      </div>
    </nav>
  )
}
