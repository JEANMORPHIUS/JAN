import type { Metadata } from 'next'
import './globals.css'
import Navigation from '@/components/Navigation'
import Footer from '@/components/Footer'

export const metadata: Metadata = {
  title: 'ATILOK LTD | Reliability in Motion — Heavy-Duty Truck Parts',
  description: 'Delivering the essential components that strengthen Britain\'s logistics backbone. Trusted bridge connecting British reliability with Turkish manufacturing excellence.',
  keywords: 'truck parts, lorry parts, heavy-duty parts, B2B parts supplier, UK truck parts, commercial vehicle parts',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en-GB">
      <body>
        <Navigation />
        <main className="min-h-screen">
          {children}
        </main>
        <Footer />
      </body>
    </html>
  )
}
