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
import { ArrowRight, Shield, Globe, Wrench } from 'lucide-react'

export default function Home() {
  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative bg-gradient-to-br from-navy via-navy-light to-navy-dark text-white py-20 lg:py-32">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div className="animate-fade-in">
              <h1 className="text-5xl lg:text-6xl font-heading font-bold mb-6 leading-tight">
                Reliability in Motion
              </h1>
              <p className="text-xl lg:text-2xl text-steel-light mb-4 font-body">
                Delivering the essential components that strengthen Britain's logistics backbone.
              </p>
              <p className="text-lg text-steel-light mb-8 font-body">
                The trusted bridge connecting British reliability and service with Turkish manufacturing excellence.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <Link href="/catalogue" className="btn-primary inline-flex items-center justify-center">
                  Browse Catalogue
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Link>
                <Link href="/about" className="btn-outline border-white text-white hover:bg-white hover:text-navy inline-flex items-center justify-center">
                  Our Story
                </Link>
              </div>
            </div>
            <div className="relative h-96 lg:h-[500px] bg-steel-dark rounded-lg flex items-center justify-center">
              {/* Placeholder for hero image - trucks in highway/logistics context */}
              <div className="text-center text-steel-light">
                <Wrench className="h-24 w-24 mx-auto mb-4 opacity-50" />
                <p className="font-body">Hero Image: Trucks in Highway Context</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Brand Statement */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-3xl mx-auto">
            <h2 className="text-4xl font-heading font-bold text-navy mb-6">
              Anatolia to Albion
            </h2>
            <p className="text-lg text-steel font-body leading-relaxed">
              ATILOK LTD stands as the trusted bridge between Turkish manufacturing excellence and British 
              commercial vehicle operators. We combine precision engineering from Anatolia with the reliability 
              and accountability standards that British fleet operators demand. Every component we supply carries 
              the weight of our commitment to quality, service, and the uninterrupted flow of Britain's logistics network.
            </p>
          </div>
        </div>
      </section>

      {/* Value Propositions */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-xl transition-smooth">
              <div className="bg-navy w-16 h-16 rounded-lg flex items-center justify-center mb-6">
                <Shield className="h-8 w-8 text-copper" />
              </div>
              <h3 className="text-2xl font-heading font-bold text-navy mb-4">
                UK Accountability
              </h3>
              <p className="text-steel font-body">
                Based in the United Kingdom, we provide local support, warranty service, and accountability 
                that fleet operators trust. Your success is our responsibility.
              </p>
            </div>

            <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-xl transition-smooth">
              <div className="bg-navy w-16 h-16 rounded-lg flex items-center justify-center mb-6">
                <Globe className="h-8 w-8 text-copper" />
              </div>
              <h3 className="text-2xl font-heading font-bold text-navy mb-4">
                Global Reach
              </h3>
              <p className="text-steel font-body">
                Leveraging Turkish manufacturing capabilities with British quality standards, we deliver 
                components that meet OEM specifications at competitive prices.
              </p>
            </div>

            <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-xl transition-smooth">
              <div className="bg-navy w-16 h-16 rounded-lg flex items-center justify-center mb-6">
                <Wrench className="h-8 w-8 text-copper" />
              </div>
              <h3 className="text-2xl font-heading font-bold text-navy mb-4">
                Technical Precision
              </h3>
              <p className="text-steel font-body">
                Every part in our catalogue is engineered to exact specifications. We understand that 
                downtime costs money, and reliability is non-negotiable.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 bg-navy text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-4xl font-heading font-bold mb-6">
            Ready to Strengthen Your Fleet?
          </h2>
          <p className="text-xl text-steel-light mb-8 font-body max-w-2xl mx-auto">
            Explore our comprehensive catalogue of heavy-duty truck and lorry parts, or speak with our 
            team about your specific requirements.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link href="/catalogue" className="btn-primary inline-flex items-center justify-center">
              View Catalogue
              <ArrowRight className="ml-2 h-5 w-5" />
            </Link>
            <Link href="/contact" className="btn-outline border-white text-white hover:bg-white hover:text-navy inline-flex items-center justify-center">
              Request a Quote
            </Link>
          </div>
        </div>
      </section>
    </div>
  )
}
