/**
 * Core Systems API Calls
 * All 13 systems from Pulse
 */

import apiClient from './client';

export interface System {
  system_id: string;
  name: string;
  description: string;
  status: 'active' | 'inactive' | 'maintenance';
  endpoints: string[];
  data?: any;
}

/**
 * Get all systems
 */
export const getAllSystems = async (): Promise<System[]> => {
  try {
    const response = await apiClient.get('/api/pulse/systems');
    return response.data.systems || response.data;
  } catch (error) {
    console.error('Error fetching systems:', error);
    throw error;
  }
};

/**
 * Get system by ID
 */
export const getSystem = async (systemId: string): Promise<System> => {
  try {
    const response = await apiClient.get(`/api/pulse/systems/${systemId}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching system ${systemId}:`, error);
    throw error;
  }
};

/**
 * Get system status
 */
export const getSystemStatus = async (systemId: string): Promise<string> => {
  try {
    const response = await apiClient.get(`/api/pulse/systems/${systemId}/status`);
    return response.data.status || 'unknown';
  } catch (error) {
    console.error(`Error fetching status for ${systemId}:`, error);
    throw error;
  }
};

// System-specific API calls
export const getWorldHistory = async () => {
  return apiClient.get('/api/world-history/timeline');
};

export const getFrequentialEvents = async () => {
  return apiClient.get('/api/frequential-events/events');
};

export const getDeepSearch = async (domain?: string) => {
  const url = domain 
    ? `/api/deep-search/by-domain/${domain}`
    : '/api/deep-search/domains';
  return apiClient.get(url);
};

export const getNourishmentHive = async () => {
  return apiClient.get('/api/nourishment-hive/resources');
};

export const getSeedToMovement = async () => {
  return apiClient.get('/api/seed-to-movement/seeds');
};

export const getSpiritualContracts = async () => {
  return apiClient.get('/api/spiritual-contracts/contracts');
};

export const getHistoricalAligned = async () => {
  return apiClient.get('/api/historical-aligned-individuals/individuals');
};

export const getIndustries = async () => {
  return apiClient.get('/api/industry-explorer/industries');
};

export const getSIYEMIntegration = async () => {
  return apiClient.get('/api/siyem/integration');
};

export const getBanking = async () => {
  return apiClient.get('/api/financial/banking');
};

export const getFinancialControls = async () => {
  return apiClient.get('/api/financial/controls');
};

export const getAlignedInvestments = async () => {
  return apiClient.get('/api/aligned-investments/investments');
};

export const getFreeWill = async () => {
  return apiClient.get('/api/free-will/status');
};
