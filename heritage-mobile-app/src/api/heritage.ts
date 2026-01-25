/**
 * Heritage Meridian API Calls
 * 7 Wonders + Seven Pillars + Heritage Meridian System
 */

import apiClient from './client';

export interface Pillar {
  pillar_id: string;
  name: string;
  ancient_name: string;
  coordinates: {
    lat: number;
    lon: number;
  };
  country: string;
  field_resonance: number;
  original_function: string;
  modern_distortion: string;
  spiritual_significance: string;
  meridian_connections: string[];
}

export interface Meridian {
  meridian_id: string;
  name: string;
  description: string;
  sites: string[];
  function: string;
}

/**
 * Get all Seven Pillars
 */
export const getPillars = async (): Promise<Pillar[]> => {
  try {
    const response = await apiClient.get('/api/heritage-meridian/pillars');
    return response.data.pillars || response.data;
  } catch (error) {
    console.error('Error fetching pillars:', error);
    throw error;
  }
};

/**
 * Get single pillar
 */
export const getPillar = async (pillarId: string): Promise<Pillar> => {
  try {
    const response = await apiClient.get(`/api/heritage-meridian/pillars/${pillarId}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching pillar ${pillarId}:`, error);
    throw error;
  }
};

/**
 * Get all meridians
 */
export const getMeridians = async (): Promise<Meridian[]> => {
  try {
    const response = await apiClient.get('/api/heritage-meridian/meridians');
    return response.data.meridians || response.data;
  } catch (error) {
    console.error('Error fetching meridians:', error);
    throw error;
  }
};

/**
 * Get network health
 */
export const getNetworkHealth = async (): Promise<any> => {
  try {
    const response = await apiClient.get('/api/heritage-meridian/network-health');
    return response.data;
  } catch (error) {
    console.error('Error fetching network health:', error);
    throw error;
  }
};
