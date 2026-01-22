import { Factory, CheckCircle, Truck, Package, Shield, ArrowRight } from 'lucide-react'

export default function SupplyChain() {
  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-navy via-navy-light to-navy-dark text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 className="text-5xl lg:text-6xl font-heading font-bold mb-6">
            Our Supply Chain
          </h1>
          <p className="text-xl text-steel-light font-body max-w-3xl">
            From Turkish manufacturing excellence through rigorous quality control to UK distribution— 
            see how we ensure every component meets the highest standards.
          </p>
        </div>
      </section>

      {/* Supply Chain Flow */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="relative">
            {/* Flow Visualization */}
            <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
              {/* Step 1: Manufacturing */}
              <div className="relative">
                <div className="bg-navy text-white p-8 rounded-lg shadow-lg text-center h-full">
                  <div className="bg-copper w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6">
                    <Factory className="h-10 w-10 text-white" />
                  </div>
                  <h3 className="text-2xl font-heading font-bold mb-4">
                    Turkish Manufacturing
                  </h3>
                  <p className="text-steel-light font-body">
                    Partner facilities in Turkey with proven track records in heavy-duty component manufacturing. 
                    Precision engineering to OEM specifications.
                  </p>
                </div>
                <div className="hidden md:block absolute top-1/2 -right-4 transform -translate-y-1/2 z-10">
                  <ArrowRight className="h-8 w-8 text-copper" />
                </div>
              </div>

              {/* Step 2: Quality Control */}
              <div className="relative">
                <div className="bg-steel text-white p-8 rounded-lg shadow-lg text-center h-full">
                  <div className="bg-copper w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6">
                    <CheckCircle className="h-10 w-10 text-white" />
                  </div>
                  <h3 className="text-2xl font-heading font-bold mb-4">
                    Quality Assurance
                  </h3>
                  <p className="text-steel-light font-body">
                    Multi-stage inspection process. Every component tested against specifications. 
                    Documentation and certification verified.
                  </p>
                </div>
                <div className="hidden md:block absolute top-1/2 -right-4 transform -translate-y-1/2 z-10">
                  <ArrowRight className="h-8 w-8 text-copper" />
                </div>
              </div>

              {/* Step 3: Logistics */}
              <div className="relative">
                <div className="bg-steel text-white p-8 rounded-lg shadow-lg text-center h-full">
                  <div className="bg-copper w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6">
                    <Truck className="h-10 w-10 text-white" />
                  </div>
                  <h3 className="text-2xl font-heading font-bold mb-4">
                    Secure Logistics
                  </h3>
                  <p className="text-steel-light font-body">
                    Protected transit from manufacturing to UK distribution centres. 
                    Tracked shipments with full chain of custody documentation.
                  </p>
                </div>
                <div className="hidden md:block absolute top-1/2 -right-4 transform -translate-y-1/2 z-10">
                  <ArrowRight className="h-8 w-8 text-copper" />
                </div>
              </div>

              {/* Step 4: UK Distribution */}
              <div className="relative">
                <div className="bg-navy text-white p-8 rounded-lg shadow-lg text-center h-full">
                  <div className="bg-copper w-20 h-20 rounded-full flex items-center justify-center mx-auto mb-6">
                    <Package className="h-10 w-10 text-white" />
                  </div>
                  <h3 className="text-2xl font-heading font-bold mb-4">
                    UK Distribution
                  </h3>
                  <p className="text-steel-light font-body">
                    Final quality check and inventory management in UK facilities. 
                    Ready for dispatch to fleet operators and repair centres.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Quality Standards */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-4xl font-heading font-bold text-navy mb-12 text-center">
            Quality Standards & Assurance
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white p-8 rounded-lg shadow-md">
              <Shield className="h-12 w-12 text-copper mb-4" />
              <h3 className="text-xl font-heading font-bold text-navy mb-4">
                OEM Specifications
              </h3>
              <p className="text-steel font-body">
                All components manufactured to original equipment manufacturer specifications. 
                No compromises on material quality or dimensional accuracy.
              </p>
            </div>

            <div className="bg-white p-8 rounded-lg shadow-md">
              <CheckCircle className="h-12 w-12 text-copper mb-4" />
              <h3 className="text-xl font-heading font-bold text-navy mb-4">
                Multi-Stage Testing
              </h3>
              <p className="text-steel font-body">
                Components undergo material testing, dimensional verification, and functional 
                validation before approval for shipment.
              </p>
            </div>

            <div className="bg-white p-8 rounded-lg shadow-md">
              <Package className="h-12 w-12 text-copper mb-4" />
              <h3 className="text-xl font-heading font-bold text-navy mb-4">
                Full Documentation
              </h3>
              <p className="text-steel font-body">
                Every shipment includes certificates of conformity, material test reports, 
                and traceability documentation for your records.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Partnership Approach */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="bg-gradient-to-r from-navy to-navy-light text-white rounded-lg p-12">
            <h2 className="text-4xl font-heading font-bold mb-6">
              Our Partnership Approach
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div>
                <h3 className="text-2xl font-heading font-semibold mb-4 text-copper">
                  Manufacturing Partners
                </h3>
                <p className="text-steel-light font-body mb-4">
                  We work exclusively with Turkish manufacturers who have demonstrated:
                </p>
                <ul className="space-y-2 font-body text-steel-light">
                  <li className="flex items-start">
                    <span className="text-copper mr-2">•</span>
                    <span>Proven track record in heavy-duty component production</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-copper mr-2">•</span>
                    <span>ISO 9001 certification and quality management systems</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-copper mr-2">•</span>
                    <span>Commitment to continuous improvement and innovation</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-copper mr-2">•</span>
                    <span>Transparency in processes and material sourcing</span>
                  </li>
                </ul>
              </div>
              <div>
                <h3 className="text-2xl font-heading font-semibold mb-4 text-copper">
                  Your Benefits
                </h3>
                <p className="text-steel-light font-body mb-4">
                  This approach ensures you receive:
                </p>
                <ul className="space-y-2 font-body text-steel-light">
                  <li className="flex items-start">
                    <span className="text-copper mr-2">•</span>
                    <span>Consistent quality across all orders and product lines</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-copper mr-2">•</span>
                    <span>Competitive pricing through direct relationships</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-copper mr-2">•</span>
                    <span>Reliable supply chain with predictable lead times</span>
                  </li>
                  <li className="flex items-start">
                    <span className="text-copper mr-2">•</span>
                    <span>Single point of accountability in the UK</span>
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

