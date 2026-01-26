/** * * 7 Wonders API Calls
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
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

import apiClient from './client';

export interface Wonder {
  wonder_id: string;
  name: string;
  location: string;
  coordinates: {
    lat: number;
    lon: number;
  };
  field_resonance: number;
  wonder_type: string;
  original_function: string;
  modern_distortion: string;
  spiritual_significance: string;
  heritage_meridian_connection: string;
  meridian_connections: string[];
  cultural_heritage: string;
  year_built: string;
  time_period: string;
  already_in_system?: boolean;
  pillar_id?: string;
  seat_id?: string;
}

export interface WondersResponse {
  wonders: Wonder[];
  total: number;
}

/**
 * Get all 7 Wonders
 */
export const getWonders = async (): Promise<Wonder[]> => {
  try {
    const response = await apiClient.get('/api/7-wonders/list');
    return response.data.wonders || response.data;
  } catch (error) {
    console.error('Error fetching wonders:', error);
    throw error;
  }
};

/**
 * Get single wonder by ID
 */
export const getWonder = async (wonderId: string): Promise<Wonder> => {
  try {
    const response = await apiClient.get(`/api/7-wonders/${wonderId}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching wonder ${wonderId}:`, error);
    throw error;
  }
};

/**
 * Get wonder's field resonance
 */
export const getWonderResonance = async (wonderId: string): Promise<number> => {
  try {
    const response = await apiClient.get(`/api/7-wonders/${wonderId}/resonance`);
    return response.data.resonance || response.data.field_resonance;
  } catch (error) {
    console.error(`Error fetching resonance for ${wonderId}:`, error);
    throw error;
  }
};

/**
 * Get wonder's meridian connections
 */
export const getWonderConnections = async (wonderId: string): Promise<string[]> => {
  try {
    const response = await apiClient.get(`/api/7-wonders/${wonderId}/meridian-connections`);
    return response.data.connections || response.data.meridian_connections || [];
  } catch (error) {
    console.error(`Error fetching connections for ${wonderId}:`, error);
    throw error;
  }
};
