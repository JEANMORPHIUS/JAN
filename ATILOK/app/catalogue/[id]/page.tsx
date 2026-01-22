import { notFound } from 'next/navigation'
import Link from 'next/link'
import { ArrowLeft, ShoppingCart, Package, CheckCircle } from 'lucide-react'
import { products, productCategories, getProductBySku } from '@/data/products'

export default function ProductDetail({ params }: { params: { id: string } }) {
  const product = products.find(p => p.id === params.id)

  if (!product) {
    notFound()
  }

  const category = productCategories.find(cat => cat.id === product.category)

  return (
    <div className="min-h-screen">
      {/* Breadcrumb */}
      <section className="bg-gray-50 py-4">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center space-x-2 text-sm font-body text-steel">
            <Link href="/" className="hover:text-copper transition-smooth">Home</Link>
            <span>/</span>
            <Link href="/catalogue" className="hover:text-copper transition-smooth">Catalogue</Link>
            <span>/</span>
            <span className="text-navy font-semibold">{product.name}</span>
          </div>
        </div>
      </section>

      {/* Product Detail */}
      <section className="py-12 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <Link 
            href="/catalogue"
            className="inline-flex items-center text-steel hover:text-copper mb-6 font-body transition-smooth"
          >
            <ArrowLeft className="h-4 w-4 mr-2" />
            Back to Catalogue
          </Link>

          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
            {/* Product Image */}
            <div className="relative">
              <div className="aspect-square bg-steel-dark rounded-lg flex items-center justify-center">
                <Package className="h-32 w-32 text-steel-light opacity-50" />
              </div>
              <p className="text-center text-steel text-sm mt-4 font-body">
                High-resolution product photography placeholder
              </p>
            </div>

            {/* Product Info */}
            <div>
              <div className="mb-4">
                <span className="inline-block bg-navy text-white text-sm font-heading font-semibold px-4 py-2 rounded">
                  {category?.name || 'Uncategorised'}
                </span>
              </div>

              <p className="text-copper font-heading font-semibold mb-2">
                {product.sku}
              </p>

              <h1 className="text-4xl font-heading font-bold text-navy mb-6">
                {product.name}
              </h1>

              <div className="mb-6">
                <p className="text-3xl font-heading font-bold text-navy mb-2">
                  £{product.price.toFixed(2)}
                </p>
                <p className="text-steel font-body">
                  Minimum Order Quantity: {product.minOrder} unit{product.minOrder !== 1 ? 's' : ''}
                </p>
              </div>

              <div className={`inline-flex items-center px-4 py-2 rounded-full mb-6 ${
                product.inStock 
                  ? 'bg-green-100 text-green-800' 
                  : 'bg-red-100 text-red-800'
              }`}>
                <CheckCircle className="h-5 w-5 mr-2" />
                <span className="font-heading font-semibold">
                  {product.inStock ? 'In Stock' : 'Out of Stock'}
                </span>
              </div>

              <div className="mb-8">
                <h3 className="text-xl font-heading font-bold text-navy mb-4">
                  Product Description
                </h3>
                <p className="text-steel font-body leading-relaxed">
                  {product.description}
                </p>
              </div>

              {product.specifications && product.specifications.length > 0 && (
                <div className="mb-8">
                  <h3 className="text-xl font-heading font-bold text-navy mb-4">
                    Technical Specifications
                  </h3>
                  <ul className="space-y-2">
                    {product.specifications.map((spec, idx) => (
                      <li key={idx} className="flex items-start text-steel font-body">
                        <span className="text-copper mr-3 mt-1">•</span>
                        <span>{spec}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              <div className="flex flex-col sm:flex-row gap-4">
                <Link 
                  href={`/contact?product=${product.sku}`}
                  className="btn-primary flex items-center justify-center"
                >
                  <ShoppingCart className="h-5 w-5 mr-2" />
                  Request a Quote
                </Link>
                <Link 
                  href="/contact"
                  className="btn-outline flex items-center justify-center"
                >
                  Bulk Order Inquiry
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Related Products */}
      <section className="py-12 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-heading font-bold text-navy mb-8">
            Related Products
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {products
              .filter(p => p.category === product.category && p.id !== product.id)
              .slice(0, 3)
              .map(related => (
                <Link 
                  key={related.id}
                  href={`/catalogue/${related.id}`}
                  className="bg-white rounded-lg shadow-md hover:shadow-xl transition-smooth p-6"
                >
                  <p className="text-sm text-copper font-heading font-semibold mb-2">
                    {related.sku}
                  </p>
                  <h3 className="text-lg font-heading font-bold text-navy mb-2">
                    {related.name}
                  </h3>
                  <p className="text-steel font-body text-sm line-clamp-2 mb-4">
                    {related.description}
                  </p>
                  <p className="text-xl font-heading font-bold text-navy">
                    £{related.price.toFixed(2)}
                  </p>
                </Link>
              ))}
          </div>
        </div>
      </section>
    </div>
  )
}
