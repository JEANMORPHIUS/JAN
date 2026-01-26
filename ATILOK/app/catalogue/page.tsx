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
import { Search, ShoppingCart, FileText, Package } from 'lucide-react'
import { products, productCategories, Product } from '@/data/products'

export default function Catalogue() {
  const [selectedCategory, setSelectedCategory] = useState<string>('all')
  const [searchTerm, setSearchTerm] = useState('')

  const filteredProducts = products.filter(product => {
    const matchesCategory = selectedCategory === 'all' || product.category === selectedCategory
    const matchesSearch = 
      product.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      product.sku.toLowerCase().includes(searchTerm.toLowerCase()) ||
      product.description.toLowerCase().includes(searchTerm.toLowerCase())
    return matchesCategory && matchesSearch
  })

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-navy via-navy-light to-navy-dark text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 className="text-5xl lg:text-6xl font-heading font-bold mb-6">
            Product Catalogue
          </h1>
          <p className="text-xl text-steel-light font-body max-w-3xl">
            Browse our comprehensive range of heavy-duty truck and lorry parts. 
            Every component engineered to OEM standards and backed by ATILOK quality assurance.
          </p>
        </div>
      </section>

      {/* Search and Filter Section */}
      <section className="bg-white py-8 sticky top-20 z-40 shadow-md">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col md:flex-row gap-4">
            {/* Search Bar */}
            <div className="flex-1 relative">
              <Search className="absolute left-4 top-1/2 transform -translate-y-1/2 text-steel h-5 w-5" />
              <input
                type="text"
                placeholder="Search by part name, SKU, or description..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full pl-12 pr-4 py-3 border-2 border-steel-light rounded-lg focus:border-copper focus:outline-none font-body"
              />
            </div>

            {/* Category Filter */}
            <div className="flex gap-2 overflow-x-auto pb-2">
              <button
                onClick={() => setSelectedCategory('all')}
                className={`px-6 py-3 rounded-lg font-heading font-semibold whitespace-nowrap transition-smooth ${
                  selectedCategory === 'all'
                    ? 'bg-navy text-white'
                    : 'bg-gray-100 text-steel hover:bg-gray-200'
                }`}
              >
                All Categories
              </button>
              {productCategories.map(cat => (
                <button
                  key={cat.id}
                  onClick={() => setSelectedCategory(cat.id)}
                  className={`px-6 py-3 rounded-lg font-heading font-semibold whitespace-nowrap transition-smooth ${
                    selectedCategory === cat.id
                      ? 'bg-navy text-white'
                      : 'bg-gray-100 text-steel hover:bg-gray-200'
                  }`}
                >
                  {cat.name}
                </button>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Products Grid */}
      <section className="py-12 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          {filteredProducts.length === 0 ? (
            <div className="text-center py-16">
              <Package className="h-16 w-16 text-steel mx-auto mb-4 opacity-50" />
              <p className="text-xl text-steel font-body">No products found matching your criteria.</p>
            </div>
          ) : (
            <>
              <div className="mb-6">
                <p className="text-steel font-body">
                  Showing {filteredProducts.length} product{filteredProducts.length !== 1 ? 's' : ''}
                </p>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {filteredProducts.map(product => (
                  <ProductCard key={product.id} product={product} />
                ))}
              </div>
            </>
          )}
        </div>
      </section>
    </div>
  )
}

function ProductCard({ product }: { product: Product }) {
  const category = productCategories.find(cat => cat.id === product.category)

  return (
    <div className="bg-white rounded-lg shadow-md hover:shadow-xl transition-smooth overflow-hidden">
      {/* Product Image Placeholder */}
      <div className="h-48 bg-steel-dark flex items-center justify-center">
        <Package className="h-16 w-16 text-steel-light opacity-50" />
      </div>

      <div className="p-6">
        {/* Category Badge */}
        <div className="mb-3">
          <span className="inline-block bg-navy text-white text-xs font-heading font-semibold px-3 py-1 rounded">
            {category?.name || 'Uncategorised'}
          </span>
        </div>

        {/* SKU */}
        <p className="text-sm text-copper font-heading font-semibold mb-2">
          {product.sku}
        </p>

        {/* Product Name */}
        <h3 className="text-xl font-heading font-bold text-navy mb-3">
          {product.name}
        </h3>

        {/* Description */}
        <p className="text-steel font-body text-sm mb-4 line-clamp-3">
          {product.description}
        </p>

        {/* Specifications Preview */}
        {product.specifications && product.specifications.length > 0 && (
          <div className="mb-4">
            <p className="text-xs text-steel-dark font-heading font-semibold mb-2">Key Specifications:</p>
            <ul className="text-xs text-steel font-body space-y-1">
              {product.specifications.slice(0, 2).map((spec, idx) => (
                <li key={idx} className="flex items-start">
                  <span className="text-copper mr-2">•</span>
                  <span>{spec}</span>
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Price and Actions */}
        <div className="border-t border-gray-200 pt-4">
          <div className="flex items-center justify-between mb-4">
            <div>
              <p className="text-2xl font-heading font-bold text-navy">
                £{product.price.toFixed(2)}
              </p>
              <p className="text-xs text-steel font-body">
                Min. Order: {product.minOrder} unit{product.minOrder !== 1 ? 's' : ''}
              </p>
            </div>
            <div className={`px-3 py-1 rounded-full text-xs font-heading font-semibold ${
              product.inStock 
                ? 'bg-green-100 text-green-800' 
                : 'bg-red-100 text-red-800'
            }`}>
              {product.inStock ? 'In Stock' : 'Out of Stock'}
            </div>
          </div>

          <div className="flex gap-2">
            <Link 
              href={`/catalogue/${product.id}`}
              className="flex-1 btn-outline text-center py-2 text-sm"
            >
              <FileText className="h-4 w-4 inline mr-2" />
              Details
            </Link>
            <Link 
              href={`/contact?product=${product.sku}`}
              className="flex-1 btn-primary text-center py-2 text-sm"
            >
              <ShoppingCart className="h-4 w-4 inline mr-2" />
              Quote
            </Link>
          </div>
        </div>
      </div>
    </div>
  )
}
