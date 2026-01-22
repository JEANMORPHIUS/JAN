import { Shield, Target, Users, Award } from 'lucide-react'

export default function About() {
  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-navy via-navy-light to-navy-dark text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 className="text-5xl lg:text-6xl font-heading font-bold mb-6">
            Why ATILOK Exists
          </h1>
          <p className="text-xl text-steel-light font-body max-w-3xl">
            We exist to bridge the gap between exceptional manufacturing capability and the reliability 
            standards that British commercial vehicle operators require. Our mission is simple: 
            keep Britain's logistics moving.
          </p>
        </div>
      </section>

      {/* Story Section */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-4xl font-heading font-bold text-navy mb-6">
                Our Story
              </h2>
              <div className="space-y-4 text-steel font-body text-lg leading-relaxed">
                <p>
                  ATILOK LTD was founded on a simple observation: British fleet operators needed reliable 
                  access to high-quality heavy-duty parts, and Turkish manufacturers had the engineering 
                  capability to produce them to exacting standards. The missing piece was a bridge—a company 
                  that understood both sides.
                </p>
                <p>
                  We established our UK presence to provide the accountability, warranty service, and 
                  technical support that British operators expect. Simultaneously, we built deep relationships 
                  with Turkish manufacturing partners who share our commitment to precision and quality.
                </p>
                <p>
                  Today, ATILOK serves as that trusted bridge. We don't just move parts from point A to point B. 
                  We ensure every component meets our rigorous quality standards, carries proper documentation, 
                  and is backed by our commitment to your operational success.
                </p>
              </div>
            </div>
            <div className="relative h-96 bg-steel-dark rounded-lg flex items-center justify-center">
              <div className="text-center text-steel-light">
                <Shield className="h-24 w-24 mx-auto mb-4 opacity-50" />
                <p className="font-body">About Us Image: Industrial Heritage</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Values Section */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-4xl font-heading font-bold text-navy mb-12 text-center">
            Our Core Values
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div className="bg-white p-6 rounded-lg shadow-md text-center">
              <div className="bg-copper w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <Shield className="h-8 w-8 text-white" />
              </div>
              <h3 className="text-xl font-heading font-bold text-navy mb-3">
                Reliability
              </h3>
              <p className="text-steel font-body">
                Every component we supply is tested, documented, and guaranteed. Your fleet's uptime depends on our quality.
              </p>
            </div>

            <div className="bg-white p-6 rounded-lg shadow-md text-center">
              <div className="bg-copper w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <Target className="h-8 w-8 text-white" />
              </div>
              <h3 className="text-xl font-heading font-bold text-navy mb-3">
                Precision
              </h3>
              <p className="text-steel font-body">
                We understand that "close enough" isn't acceptable. Every part must meet exact specifications.
              </p>
            </div>

            <div className="bg-white p-6 rounded-lg shadow-md text-center">
              <div className="bg-copper w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <Users className="h-8 w-8 text-white" />
              </div>
              <h3 className="text-xl font-heading font-bold text-navy mb-3">
                Partnership
              </h3>
              <p className="text-steel font-body">
                We're not just a supplier—we're your partner in keeping operations running smoothly.
              </p>
            </div>

            <div className="bg-white p-6 rounded-lg shadow-md text-center">
              <div className="bg-copper w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <Award className="h-8 w-8 text-white" />
              </div>
              <h3 className="text-xl font-heading font-bold text-navy mb-3">
                Excellence
              </h3>
              <p className="text-steel font-body">
                Continuous improvement in our processes, relationships, and service delivery.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* UK Accountability Section */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="bg-navy text-white rounded-lg p-12">
            <h2 className="text-4xl font-heading font-bold mb-6">
              UK Accountability, Global Capability
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div>
                <h3 className="text-2xl font-heading font-semibold mb-4 text-copper">
                  Why UK-Based Matters
                </h3>
                <ul className="space-y-3 font-body text-steel-light">
                  <li className="flex items-start">
                    <span className="text-copper mr-2">•</span>
                    <span>Local warranty and support services you can trust</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-copper mr-2">•</span>
                    <span>Direct accountability under UK commercial law</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-copper mr-2">•</span>
                    <span>Understanding of British fleet operations and requirements</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-copper mr-2">•</span>
                    <span>Responsive customer service in your time zone</span>
                  </li>
                </ul>
              </div>
              <div>
                <h3 className="text-2xl font-heading font-semibold mb-4 text-copper">
                  Our Global Advantage
                </h3>
                <ul className="space-y-3 font-body text-steel-light">
                  <li className="flex items-start">
                    <span className="text-copper mr-2">•</span>
                    <span>Direct relationships with Turkish manufacturing partners</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-copper mr-2">•</span>
                    <span>Quality control processes that exceed industry standards</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-copper mr-2">•</span>
                    <span>Competitive pricing without compromising on quality</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-copper mr-2">•</span>
                    <span>Scalable supply chain for bulk and urgent orders</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
