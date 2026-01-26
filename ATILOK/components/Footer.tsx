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

import Link from 'next/link'
import { Truck, Mail, Phone, MapPin } from 'lucide-react'

export default function Footer() {
  return (
    <footer className="bg-navy text-white mt-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* Brand Section */}
          <div className="col-span-1 md:col-span-2">
            <div className="flex items-center space-x-3 mb-4">
              <div className="bg-copper p-2 rounded-lg">
                <Truck className="h-6 w-6 text-white" />
              </div>
              <div>
                <h3 className="text-2xl font-heading font-bold">ATILOK LTD</h3>
                <p className="text-steel-light text-sm font-body">Reliability in Motion</p>
              </div>
            </div>
            <p className="text-steel-light font-body mb-4 max-w-md">
              Delivering the essential components that strengthen Britain's logistics backbone. 
              The trusted bridge connecting British reliability with Turkish manufacturing excellence.
            </p>
            <p className="text-steel-light text-sm font-body">
              Anatolia to Albion — Quality Assured
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="font-heading font-semibold mb-4">Quick Links</h4>
            <ul className="space-y-2 font-body">
              <li>
                <Link href="/about" className="text-steel-light hover:text-copper transition-smooth">
                  About Us
                </Link>
              </li>
              <li>
                <Link href="/catalogue" className="text-steel-light hover:text-copper transition-smooth">
                  Product Catalogue
                </Link>
              </li>
              <li>
                <Link href="/supply-chain" className="text-steel-light hover:text-copper transition-smooth">
                  Supply Chain
                </Link>
              </li>
              <li>
                <Link href="/contact" className="text-steel-light hover:text-copper transition-smooth">
                  Contact Us
                </Link>
              </li>
            </ul>
          </div>

          {/* Contact Info */}
          <div>
            <h4 className="font-heading font-semibold mb-4">Contact</h4>
            <ul className="space-y-3 font-body text-steel-light">
              <li className="flex items-start space-x-2">
                <MapPin className="h-5 w-5 text-copper mt-0.5 flex-shrink-0" />
                <span>United Kingdom</span>
              </li>
              <li className="flex items-start space-x-2">
                <Mail className="h-5 w-5 text-copper mt-0.5 flex-shrink-0" />
                <a href="mailto:info@atilok.co.uk" className="hover:text-copper transition-smooth">
                  info@atilok.co.uk
                </a>
              </li>
              <li className="flex items-start space-x-2">
                <Phone className="h-5 w-5 text-copper mt-0.5 flex-shrink-0" />
                <a href="tel:+44" className="hover:text-copper transition-smooth">
                  +44 (0) XXX XXX XXXX
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t border-steel-dark mt-8 pt-8 text-center">
          <p className="text-steel-light text-sm font-body">
            © {new Date().getFullYear()} ATILOK LTD. All rights reserved. | 
            <Link href="/terms" className="ml-1 hover:text-copper transition-smooth">Terms & Conditions</Link> | 
            <Link href="/privacy" className="ml-1 hover:text-copper transition-smooth">Privacy Policy</Link>
          </p>
        </div>
      </div>
    </footer>
  )
}
