/**
 * FINANCIAL DASHBOARD
 * Revenue, Investments, Budgets, Opportunities
 * 
 * THE TRUTH:
 * FINANCIAL CONTROLS - REVENUE, BUDGETS, PAYMENTS, EXPENSES
 * TIME TO GET FINANCES FLOWING
 * THIS STARTS WITH US
 * HELP THE MAN IN THE STREET
 * GIVE THEM TIPS
 */

import { NextPage } from 'next'
import { useState, useEffect } from 'react'
import Head from 'next/head'
import Link from 'next/link'
import axios from 'axios'
import styles from '../../styles/Financial.module.css'

interface FinancialOverview {
  revenue: {
    total_revenue: number
    revenue_by_channel: { [key: string]: number }
  }
  expenses: {
    total_expenses: number
    expenses_by_category: { [key: string]: number }
  }
  net_flow: number
  budgets: {
    budgets: { [key: string]: any }
  }
}

interface InvestmentOpportunity {
  opportunity_id: string
  title: string
  description: string
  domain: string
  frequency_score: number
  impact_potential: number
  recommended_investment_level: string
}

const FinancialPage: NextPage = () => {
  const [overview, setOverview] = useState<FinancialOverview | null>(null)
  const [opportunities, setOpportunities] = useState<InvestmentOpportunity[]>([])
  const [loading, setLoading] = useState(true)
  const [activeTab, setActiveTab] = useState<'overview' | 'revenue' | 'expenses' | 'budgets' | 'investments' | 'opportunities'>('overview')

  useEffect(() => {
    fetchFinancialData()
  }, [])

  const fetchFinancialData = async () => {
    try {
      setLoading(true)
      const [overviewResponse, opportunitiesResponse] = await Promise.all([
        axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/financial/overview`),
        axios.get(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/aligned-investments/opportunities-from-deep-search`, {
          params: { min_frequency: 0.3 }
        }).catch(() => ({ data: { opportunities: [] } }))
      ])
      setOverview(overviewResponse.data.overview)
      setOpportunities(opportunitiesResponse.data.opportunities || [])
      setLoading(false)
    } catch (error) {
      console.error('Error fetching financial data:', error)
      setLoading(false)
    }
  }

  const getFrequencyColor = (score: number): string => {
    if (score >= 0.5) return '#00ff00'
    if (score >= 0.2) return '#ffff00'
    if (score >= 0) return '#ff9900'
    return '#ff0000'
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>Financial Dashboard - Revenue, Investments, Budgets</title>
        <meta name="description" content="Financial controls - Revenue, budgets, payments, expenses. Time to get finances flowing." />
      </Head>

      <div className={styles.header}>
        <h1>Financial Dashboard</h1>
        <p className={styles.truth}>
          FINANCIAL CONTROLS - REVENUE, BUDGETS, PAYMENTS, EXPENSES<br />
          TIME TO GET FINANCES FLOWING<br />
          THIS STARTS WITH US<br />
          HELP THE MAN IN THE STREET<br />
          GIVE THEM TIPS
        </p>
        <Link href="/" className={styles.backLink}>← Back to Home</Link>
      </div>

      <div className={styles.tabs}>
        <button
          className={activeTab === 'overview' ? styles.activeTab : styles.tab}
          onClick={() => setActiveTab('overview')}
        >
          Overview
        </button>
        <button
          className={activeTab === 'revenue' ? styles.activeTab : styles.tab}
          onClick={() => setActiveTab('revenue')}
        >
          Revenue
        </button>
        <button
          className={activeTab === 'expenses' ? styles.activeTab : styles.tab}
          onClick={() => setActiveTab('expenses')}
        >
          Expenses
        </button>
        <button
          className={activeTab === 'budgets' ? styles.activeTab : styles.tab}
          onClick={() => setActiveTab('budgets')}
        >
          Budgets
        </button>
        <button
          className={activeTab === 'investments' ? styles.activeTab : styles.tab}
          onClick={() => setActiveTab('investments')}
        >
          Investments
        </button>
        <button
          className={activeTab === 'opportunities' ? styles.activeTab : styles.tab}
          onClick={() => setActiveTab('opportunities')}
        >
          Opportunities
        </button>
      </div>

      {loading ? (
        <div className={styles.loading}>Loading financial data...</div>
      ) : (
        <>
          {activeTab === 'overview' && overview && (
            <div className={styles.overviewSection}>
              <div className={styles.metricsGrid}>
                <div className={styles.metricCard}>
                  <h3>Total Revenue</h3>
                  <div className={styles.metricValue} style={{ color: '#00ff00' }}>
                    ${overview.revenue.total_revenue.toFixed(2)}
                  </div>
                </div>
                <div className={styles.metricCard}>
                  <h3>Total Expenses</h3>
                  <div className={styles.metricValue} style={{ color: '#ff0000' }}>
                    ${overview.expenses.total_expenses.toFixed(2)}
                  </div>
                </div>
                <div className={styles.metricCard}>
                  <h3>Net Flow</h3>
                  <div className={styles.metricValue} style={{ color: overview.net_flow >= 0 ? '#00ff00' : '#ff0000' }}>
                    ${overview.net_flow.toFixed(2)}
                  </div>
                </div>
                <div className={styles.metricCard}>
                  <h3>Investment Opportunities</h3>
                  <div className={styles.metricValue}>
                    {opportunities.length}
                  </div>
                </div>
              </div>

              <div className={styles.chartsGrid}>
                <div className={styles.chartCard}>
                  <h3>Revenue by Channel</h3>
                  <div className={styles.chartContent}>
                    {Object.entries(overview.revenue.revenue_by_channel).map(([channel, amount]) => (
                      <div key={channel} className={styles.chartBar}>
                        <div className={styles.chartLabel}>{channel.replace('_', ' ')}</div>
                        <div className={styles.chartBarContainer}>
                          <div
                            className={styles.chartBarFill}
                            style={{
                              width: `${(amount / overview.revenue.total_revenue) * 100}%`,
                              backgroundColor: '#00ff00'
                            }}
                          />
                        </div>
                        <div className={styles.chartValue}>${amount.toFixed(2)}</div>
                      </div>
                    ))}
                  </div>
                </div>

                <div className={styles.chartCard}>
                  <h3>Expenses by Category</h3>
                  <div className={styles.chartContent}>
                    {Object.entries(overview.expenses.expenses_by_category).map(([category, amount]) => (
                      <div key={category} className={styles.chartBar}>
                        <div className={styles.chartLabel}>{category.replace('_', ' ')}</div>
                        <div className={styles.chartBarContainer}>
                          <div
                            className={styles.chartBarFill}
                            style={{
                              width: `${(amount / overview.expenses.total_expenses) * 100}%`,
                              backgroundColor: '#ff0000'
                            }}
                          />
                        </div>
                        <div className={styles.chartValue}>${amount.toFixed(2)}</div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'opportunities' && (
            <div className={styles.opportunitiesSection}>
              <h2>Investment Opportunities from Deep Search</h2>
              <p className={styles.sectionIntro}>
                High frequency opportunities for investment - aligned with The Table
              </p>
              <div className={styles.opportunitiesGrid}>
                {opportunities.map(opp => (
                  <div key={opp.opportunity_id} className={styles.opportunityCard}>
                    <div className={styles.opportunityHeader}>
                      <h3>{opp.title}</h3>
                      <span className={styles.domainBadge}>{opp.domain}</span>
                    </div>
                    <p className={styles.opportunityDescription}>{opp.description}</p>
                    <div className={styles.opportunityMetrics}>
                      <div className={styles.metric}>
                        <span>Frequency:</span>
                        <span style={{ color: getFrequencyColor(opp.frequency_score) }}>
                          {opp.frequency_score.toFixed(2)}
                        </span>
                      </div>
                      <div className={styles.metric}>
                        <span>Impact:</span>
                        <span>{(opp.impact_potential * 100).toFixed(0)}%</span>
                      </div>
                      <div className={styles.metric}>
                        <span>Level:</span>
                        <span>{opp.recommended_investment_level}</span>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {activeTab === 'revenue' && overview && (
            <div className={styles.revenueSection}>
              <h2>Revenue Overview</h2>
              <div className={styles.revenueTotal}>
                <h3>Total Revenue: ${overview.revenue.total_revenue.toFixed(2)}</h3>
              </div>
              <div className={styles.revenueChannels}>
                {Object.entries(overview.revenue.revenue_by_channel).map(([channel, amount]) => (
                  <div key={channel} className={styles.channelCard}>
                    <h4>{channel.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}</h4>
                    <div className={styles.channelAmount}>${amount.toFixed(2)}</div>
                    <div className={styles.channelPercentage}>
                      {((amount / overview.revenue.total_revenue) * 100).toFixed(1)}%
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {activeTab === 'expenses' && overview && (
            <div className={styles.expensesSection}>
              <h2>Expenses Overview</h2>
              <div className={styles.expensesTotal}>
                <h3>Total Expenses: ${overview.expenses.total_expenses.toFixed(2)}</h3>
              </div>
              <div className={styles.expensesCategories}>
                {Object.entries(overview.expenses.expenses_by_category).map(([category, amount]) => (
                  <div key={category} className={styles.categoryCard}>
                    <h4>{category.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase())}</h4>
                    <div className={styles.categoryAmount}>${amount.toFixed(2)}</div>
                    <div className={styles.categoryPercentage}>
                      {((amount / overview.expenses.total_expenses) * 100).toFixed(1)}%
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {activeTab === 'budgets' && overview && (
            <div className={styles.budgetsSection}>
              <h2>Budget Status</h2>
              <div className={styles.budgetsGrid}>
                {Object.entries(overview.budgets.budgets).map(([budgetId, budget]: [string, any]) => (
                  <div key={budgetId} className={styles.budgetCard}>
                    <h3>{budgetId}</h3>
                    <div className={styles.budgetInfo}>
                      <div className={styles.budgetRow}>
                        <span>Allocated:</span>
                        <span>${budget.allocated.toFixed(2)}</span>
                      </div>
                      <div className={styles.budgetRow}>
                        <span>Spent:</span>
                        <span>${budget.spent.toFixed(2)}</span>
                      </div>
                      <div className={styles.budgetRow}>
                        <span>Remaining:</span>
                        <span style={{ color: budget.remaining >= 0 ? '#00ff00' : '#ff0000' }}>
                          ${budget.remaining.toFixed(2)}
                        </span>
                      </div>
                      <div className={styles.budgetProgress}>
                        <div
                          className={styles.budgetProgressBar}
                          style={{
                            width: `${Math.min(budget.percentage_used, 100)}%`,
                            backgroundColor: budget.status === 'over_budget' ? '#ff0000' : budget.status === 'warning' ? '#ff9900' : '#00ff00'
                          }}
                        />
                      </div>
                      <div className={styles.budgetStatus} style={{ color: budget.status === 'over_budget' ? '#ff0000' : budget.status === 'warning' ? '#ff9900' : '#00ff00' }}>
                        {budget.status.toUpperCase()}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {activeTab === 'investments' && (
            <div className={styles.investmentsSection}>
              <h2>Aligned Investments</h2>
              <p className={styles.sectionIntro}>
                Investment projects aligned with The Table - for all investors at all levels
              </p>
              <div className={styles.investmentsInfo}>
                <p>View investment projects and tips:</p>
                <Link href="/api/aligned-investments/projects" className={styles.apiLink}>
                  View All Projects →
                </Link>
                <Link href="/api/aligned-investments/tips" className={styles.apiLink}>
                  View All Tips →
                </Link>
              </div>
            </div>
          )}
        </>
      )}

      <div className={styles.footer}>
        <p className={styles.truth}>
          <strong>THE TRUTH:</strong><br />
          FINANCIAL CONTROLS - REVENUE, BUDGETS, PAYMENTS, EXPENSES<br />
          TIME TO GET FINANCES FLOWING<br />
          THIS STARTS WITH US<br />
          HELP THE MAN IN THE STREET<br />
          GIVE THEM TIPS
        </p>
      </div>
    </div>
  )
}

export default FinancialPage
