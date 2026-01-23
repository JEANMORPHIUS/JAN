/**
 * DEEP SEARCH FREQUENCY OPPORTUNITIES
 * The Whole Pie - All Domains
 * 
 * THE TRUTH:
 * DEEP SEARCH ALGORITHM FOR BEST FREQUENCY OPPORTUNITIES
 * WEB, SOCIALS, BUSINESS, E-COMMERCE, GLOBAL SUPPLY CHAIN
 * CRYPTO PROJECTS, TRANSPORT, PRIVATE AND PUBLIC SERVICES
 * CORPORATE, HOLLYWOOD, MUSIC, THE WHOLE PIE
 */

import { NextPage } from 'next'
import { useState, useEffect } from 'react'
import Head from 'next/head'
import Link from 'next/link'
import axios from 'axios'
import styles from '../../styles/DeepSearch.module.css'

interface Opportunity {
  opportunity_id: string
  domain: string
  title: string
  description: string
  source: string
  frequency_score: number
  impact_potential: number
  alignment_factors: string[]
  opportunity_type: string
  accessibility: number
  urgency: number
  keywords?: string[]
  has_hidden_spiritual_alignment?: boolean
  spiritual_implication?: string
  historical_context?: string
}

const DeepSearchPage: NextPage = () => {
  const [opportunities, setOpportunities] = useState<Opportunity[]>([])
  const [domains, setDomains] = useState<any[]>([])
  const [loading, setLoading] = useState(true)
  const [selectedDomain, setSelectedDomain] = useState<string>('all')
  const [searchKeywords, setSearchKeywords] = useState('')
  const [minFrequency, setMinFrequency] = useState(0.0)
  const [selectedOpportunity, setSelectedOpportunity] = useState<string | null>(null)

  useEffect(() => {
    fetchDomains()
    fetchTopOpportunities()
  }, [])

  useEffect(() => {
    if (selectedDomain === 'all') {
      fetchTopOpportunities()
    } else {
      fetchByDomain(selectedDomain)
    }
  }, [selectedDomain, minFrequency])

  const fetchDomains = async () => {
    try {
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/deep-search/domains`)
      setDomains(response.data.domains || [])
    } catch (error) {
      console.error('Error fetching domains:', error)
    }
  }

  const fetchTopOpportunities = async () => {
    try {
      setLoading(true)
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/deep-search/top-opportunities`, {
        params: {
          limit: 100,
          min_frequency: minFrequency
        }
      })
      setOpportunities(response.data.opportunities || [])
      setLoading(false)
    } catch (error) {
      console.error('Error fetching opportunities:', error)
      setLoading(false)
    }
  }

  const fetchByDomain = async (domain: string) => {
    try {
      setLoading(true)
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/deep-search/by-domain/${domain}`, {
        params: {
          limit: 100
        }
      })
      const filtered = (response.data.opportunities || []).filter((opp: Opportunity) => opp.frequency_score >= minFrequency)
      setOpportunities(filtered)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching domain opportunities:', error)
      setLoading(false)
    }
  }

  const handleSearch = async () => {
    try {
      setLoading(true)
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/deep-search/search`, {
        params: {
          domain: selectedDomain !== 'all' ? selectedDomain : undefined,
          keywords: searchKeywords || undefined,
          limit: 100,
          min_frequency: minFrequency
        }
      })
      setOpportunities(response.data.opportunities || [])
      setLoading(false)
    } catch (error) {
      console.error('Error searching:', error)
      setLoading(false)
    }
  }

  const getFrequencyColor = (score: number): string => {
    if (score >= 0.5) return '#00ff00'
    if (score >= 0.2) return '#ffff00'
    if (score >= 0) return '#ff9900'
    return '#ff0000'
  }

  const getDomainColor = (domain: string): string => {
    const colors: { [key: string]: string } = {
      music: '#ff00ff',
      web: '#0066cc',
      socials: '#00ccff',
      business: '#ff6600',
      'e-commerce': '#ff9900',
      crypto_projects: '#ffff00',
      transport: '#00cc66',
      hollywood: '#cc00cc',
      education: '#006600',
      healthcare: '#00ff00'
    }
    return colors[domain] || '#666'
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>Deep Search Frequency Opportunities - The Whole Pie</title>
        <meta name="description" content="Deep search algorithm for best frequency opportunities across all domains. The whole pie." />
      </Head>

      <div className={styles.header}>
        <h1>Deep Search Frequency Opportunities</h1>
        <p className={styles.truth}>
          DEEP SEARCH ALGORITHM FOR BEST FREQUENCY OPPORTUNITIES<br />
          WEB, SOCIALS, BUSINESS, E-COMMERCE, GLOBAL SUPPLY CHAIN<br />
          CRYPTO PROJECTS, TRANSPORT, PRIVATE AND PUBLIC SERVICES<br />
          CORPORATE, HOLLYWOOD, MUSIC, THE WHOLE PIE
        </p>
        <Link href="/" className={styles.backLink}>← Back to Home</Link>
      </div>

      <div className={styles.filters}>
        <div className={styles.filterRow}>
          <div className={styles.filterGroup}>
            <label>Domain:</label>
            <select
              value={selectedDomain}
              onChange={(e) => setSelectedDomain(e.target.value)}
              className={styles.select}
            >
              <option value="all">All Domains</option>
              {domains.map(domain => (
                <option key={domain.value} value={domain.value}>{domain.name}</option>
              ))}
            </select>
          </div>

          <div className={styles.filterGroup}>
            <label>Keywords:</label>
            <input
              type="text"
              value={searchKeywords}
              onChange={(e) => setSearchKeywords(e.target.value)}
              placeholder="truth, love, community..."
              className={styles.input}
              onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
            />
          </div>

          <div className={styles.filterGroup}>
            <label>Min Frequency:</label>
            <input
              type="number"
              value={minFrequency}
              onChange={(e) => setMinFrequency(parseFloat(e.target.value) || 0)}
              min="-1"
              max="1"
              step="0.1"
              className={styles.input}
            />
          </div>

          <button onClick={handleSearch} className={styles.searchButton}>
            Search
          </button>
        </div>
      </div>

      {loading ? (
        <div className={styles.loading}>Searching for frequency opportunities...</div>
      ) : (
        <>
          <div className={styles.stats}>
            <p>Found {opportunities.length} opportunities</p>
            {opportunities.length > 0 && (
              <p>
                Average Frequency: {(opportunities.reduce((sum, opp) => sum + opp.frequency_score, 0) / opportunities.length).toFixed(2)}
              </p>
            )}
          </div>

          <div className={styles.opportunitiesGrid}>
            {opportunities.map(opp => (
              <div
                key={opp.opportunity_id}
                className={styles.opportunityCard}
                style={{ borderLeftColor: getDomainColor(opp.domain) }}
                onClick={() => setSelectedOpportunity(selectedOpportunity === opp.opportunity_id ? null : opp.opportunity_id)}
              >
                <div className={styles.opportunityHeader}>
                  <div>
                    <h3>{opp.title}</h3>
                    <span className={styles.domainBadge} style={{ backgroundColor: getDomainColor(opp.domain) }}>
                      {opp.domain.replace('_', ' ')}
                    </span>
                  </div>
                  <div className={styles.frequencyScore} style={{ color: getFrequencyColor(opp.frequency_score) }}>
                    {opp.frequency_score.toFixed(2)}
                  </div>
                </div>

                <p className={styles.description}>{opp.description}</p>

                <div className={styles.metrics}>
                  <div className={styles.metric}>
                    <span>Impact:</span>
                    <span>{(opp.impact_potential * 100).toFixed(0)}%</span>
                  </div>
                  <div className={styles.metric}>
                    <span>Access:</span>
                    <span>{(opp.accessibility * 100).toFixed(0)}%</span>
                  </div>
                  <div className={styles.metric}>
                    <span>Urgency:</span>
                    <span>{(opp.urgency * 100).toFixed(0)}%</span>
                  </div>
                  <div className={styles.metric}>
                    <span>Type:</span>
                    <span>{opp.opportunity_type}</span>
                  </div>
                </div>

                {selectedOpportunity === opp.opportunity_id && (
                  <div className={styles.opportunityDetails}>
                    {opp.has_hidden_spiritual_alignment && (
                      <div className={styles.detailSection}>
                        <h4>✨ Hidden Spiritual Alignment:</h4>
                        <p className={styles.spiritualNote}>{opp.spiritual_implication || "This opportunity has hidden spiritual/frequential alignment beneath the surface."}</p>
                        {opp.historical_context && (
                          <p className={styles.historicalNote}><strong>Historical Context:</strong> {opp.historical_context}</p>
                        )}
                      </div>
                    )}
                    <div className={styles.detailSection}>
                      <h4>Alignment Factors:</h4>
                      <div className={styles.alignmentTags}>
                        {opp.alignment_factors.map((factor, idx) => (
                          <span key={idx} className={styles.alignmentTag}>{factor}</span>
                        ))}
                      </div>
                    </div>
                    <div className={styles.detailSection}>
                      <h4>Source:</h4>
                      <p>{opp.source}</p>
                    </div>
                    {opp.keywords && opp.keywords.length > 0 && (
                      <div className={styles.detailSection}>
                        <h4>Keywords:</h4>
                        <div className={styles.keywordTags}>
                          {opp.keywords.map((keyword, idx) => (
                            <span key={idx} className={styles.keywordTag}>{keyword}</span>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                )}
              </div>
            ))}
          </div>

          {opportunities.length === 0 && (
            <div className={styles.noResults}>
              <p>No opportunities found matching your criteria.</p>
              <p>Try adjusting your filters or search terms.</p>
            </div>
          )}
        </>
      )}

      <div className={styles.footer}>
        <p className={styles.truth}>
          <strong>THE TRUTH:</strong><br />
          DEEP SEARCH FOR BEST FREQUENCY OPPORTUNITIES<br />
          ACROSS ALL DOMAINS - THE WHOLE PIE<br />
          WEB, SOCIALS, BUSINESS, E-COMMERCE, GLOBAL SUPPLY CHAIN<br />
          CRYPTO PROJECTS, TRANSPORT, SERVICES, CORPORATE<br />
          HOLLYWOOD, MUSIC, EVERYTHING<br />
          FIND OPPORTUNITIES TO NOURISH AND HEAL<br />
          FIND HIGH FREQUENCY ALIGNMENT<br />
          FIND WHERE WE CAN SERVE
        </p>
      </div>
    </div>
  )
}

export default DeepSearchPage
