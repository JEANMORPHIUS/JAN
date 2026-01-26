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

import { useState, useEffect } from 'react'
import { useSearchParams } from 'next/navigation'
import { Mail, Phone, MapPin, Send, Package } from 'lucide-react'

export default function Contact() {
  const searchParams = useSearchParams()
  const productSku = searchParams.get('product')
  
  const [formData, setFormData] = useState({
    name: '',
    company: '',
    email: '',
    phone: '',
    productSku: productSku || '',
    quantity: '',
    message: '',
    inquiryType: 'quote'
  })

  const [submitted, setSubmitted] = useState(false)

  useEffect(() => {
    if (productSku) {
      setFormData(prev => ({ ...prev, productSku: productSku }))
    }
  }, [productSku])

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // In production, this would send to your backend API
    console.log('Form submitted:', formData)
    setSubmitted(true)
    setTimeout(() => setSubmitted(false), 5000)
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    setFormData(prev => ({
      ...prev,
      [e.target.name]: e.target.value
    }))
  }

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-navy via-navy-light to-navy-dark text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 className="text-5xl lg:text-6xl font-heading font-bold mb-6">
            Get in Touch
          </h1>
          <p className="text-xl text-steel-light font-body max-w-3xl">
            Request a quote, inquire about bulk orders, or speak with our team about your specific requirements.
          </p>
        </div>
      </section>

      {/* Contact Section */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-12">
            {/* Contact Information */}
            <div>
              <h2 className="text-3xl font-heading font-bold text-navy mb-8">
                Contact Information
              </h2>
              <div className="space-y-6">
                <div className="flex items-start space-x-4">
                  <div className="bg-navy p-3 rounded-lg">
                    <MapPin className="h-6 w-6 text-copper" />
                  </div>
                  <div>
                    <h3 className="font-heading font-semibold text-navy mb-1">Address</h3>
                    <p className="text-steel font-body">
                      United Kingdom<br />
                      ATILOK LTD
                    </p>
                  </div>
                </div>

                <div className="flex items-start space-x-4">
                  <div className="bg-navy p-3 rounded-lg">
                    <Mail className="h-6 w-6 text-copper" />
                  </div>
                  <div>
                    <h3 className="font-heading font-semibold text-navy mb-1">Email</h3>
                    <a href="mailto:info@atilok.co.uk" className="text-steel hover:text-copper font-body transition-smooth">
                      info@atilok.co.uk
                    </a>
                  </div>
                </div>

                <div className="flex items-start space-x-4">
                  <div className="bg-navy p-3 rounded-lg">
                    <Phone className="h-6 w-6 text-copper" />
                  </div>
                  <div>
                    <h3 className="font-heading font-semibold text-navy mb-1">Phone</h3>
                    <a href="tel:+44" className="text-steel hover:text-copper font-body transition-smooth">
                      +44 (0) XXX XXX XXXX
                    </a>
                  </div>
                </div>
              </div>

              <div className="mt-8 p-6 bg-gray-50 rounded-lg">
                <h3 className="font-heading font-semibold text-navy mb-3">Business Hours</h3>
                <p className="text-steel font-body text-sm">
                  Monday - Friday: 8:00 AM - 6:00 PM GMT<br />
                  Saturday: 9:00 AM - 1:00 PM GMT<br />
                  Sunday: Closed
                </p>
              </div>
            </div>

            {/* Contact Form */}
            <div className="lg:col-span-2">
              <h2 className="text-3xl font-heading font-bold text-navy mb-8">
                Request a Quote
              </h2>

              {submitted && (
                <div className="mb-6 p-4 bg-green-100 border border-green-400 text-green-800 rounded-lg">
                  <p className="font-body">Thank you! Your inquiry has been submitted. We'll be in touch shortly.</p>
                </div>
              )}

              <form onSubmit={handleSubmit} className="space-y-6">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label htmlFor="name" className="block text-sm font-heading font-semibold text-navy mb-2">
                      Full Name *
                    </label>
                    <input
                      type="text"
                      id="name"
                      name="name"
                      required
                      value={formData.name}
                      onChange={handleChange}
                      className="w-full px-4 py-3 border-2 border-steel-light rounded-lg focus:border-copper focus:outline-none font-body"
                    />
                  </div>

                  <div>
                    <label htmlFor="company" className="block text-sm font-heading font-semibold text-navy mb-2">
                      Company Name *
                    </label>
                    <input
                      type="text"
                      id="company"
                      name="company"
                      required
                      value={formData.company}
                      onChange={handleChange}
                      className="w-full px-4 py-3 border-2 border-steel-light rounded-lg focus:border-copper focus:outline-none font-body"
                    />
                  </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label htmlFor="email" className="block text-sm font-heading font-semibold text-navy mb-2">
                      Email Address *
                    </label>
                    <input
                      type="email"
                      id="email"
                      name="email"
                      required
                      value={formData.email}
                      onChange={handleChange}
                      className="w-full px-4 py-3 border-2 border-steel-light rounded-lg focus:border-copper focus:outline-none font-body"
                    />
                  </div>

                  <div>
                    <label htmlFor="phone" className="block text-sm font-heading font-semibold text-navy mb-2">
                      Phone Number *
                    </label>
                    <input
                      type="tel"
                      id="phone"
                      name="phone"
                      required
                      value={formData.phone}
                      onChange={handleChange}
                      className="w-full px-4 py-3 border-2 border-steel-light rounded-lg focus:border-copper focus:outline-none font-body"
                    />
                  </div>
                </div>

                <div>
                  <label htmlFor="inquiryType" className="block text-sm font-heading font-semibold text-navy mb-2">
                    Inquiry Type *
                  </label>
                  <select
                    id="inquiryType"
                    name="inquiryType"
                    required
                    value={formData.inquiryType}
                    onChange={handleChange}
                    className="w-full px-4 py-3 border-2 border-steel-light rounded-lg focus:border-copper focus:outline-none font-body"
                  >
                    <option value="quote">Request Quote</option>
                    <option value="bulk">Bulk Order Inquiry</option>
                    <option value="technical">Technical Support</option>
                    <option value="general">General Inquiry</option>
                  </select>
                </div>

                {formData.productSku && (
                  <div>
                    <label htmlFor="productSku" className="block text-sm font-heading font-semibold text-navy mb-2">
                      Product SKU
                    </label>
                    <div className="flex items-center space-x-2">
                      <Package className="h-5 w-5 text-copper" />
                      <input
                        type="text"
                        id="productSku"
                        name="productSku"
                        value={formData.productSku}
                        onChange={handleChange}
                        className="flex-1 px-4 py-3 border-2 border-steel-light rounded-lg focus:border-copper focus:outline-none font-body"
                        placeholder="e.g., ATL-ENG-001"
                      />
                    </div>
                  </div>
                )}

                <div>
                  <label htmlFor="quantity" className="block text-sm font-heading font-semibold text-navy mb-2">
                    Quantity
                  </label>
                  <input
                    type="number"
                    id="quantity"
                    name="quantity"
                    min="1"
                    value={formData.quantity}
                    onChange={handleChange}
                    className="w-full px-4 py-3 border-2 border-steel-light rounded-lg focus:border-copper focus:outline-none font-body"
                    placeholder="Enter quantity"
                  />
                </div>

                <div>
                  <label htmlFor="message" className="block text-sm font-heading font-semibold text-navy mb-2">
                    Message *
                  </label>
                  <textarea
                    id="message"
                    name="message"
                    required
                    rows={6}
                    value={formData.message}
                    onChange={handleChange}
                    className="w-full px-4 py-3 border-2 border-steel-light rounded-lg focus:border-copper focus:outline-none font-body resize-none"
                    placeholder="Please provide details about your requirements..."
                  />
                </div>

                <button
                  type="submit"
                  className="btn-primary w-full flex items-center justify-center"
                >
                  <Send className="h-5 w-5 mr-2" />
                  Submit Inquiry
                </button>
              </form>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
