/** * * Entities API Calls
 *  * All 11 entities: 5 Creative Personas + 4 Business Projects + 2 Governance
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

// Creative Personas
export interface CreativePersona {
  entity_id: string;
  name: string;
  handle: string;
  type: 'creative_persona';
  voice: string;
  content: any[];
  social_media: {
    platform: string;
    handle: string;
    url: string;
  }[];
}

// Business Projects
export interface BusinessProject {
  project_id: string;
  name: string;
  type: 'business_project';
  description: string;
  ecommerce?: boolean;
  products?: any[];
  videos?: any[];
}

// Governance
export interface GovernanceEntity {
  entity_id: string;
  name: string;
  type: 'governance';
  description: string;
  functions: string[];
}

export type Entity = CreativePersona | BusinessProject | GovernanceEntity;

/**
 * Get all entities
 */
export const getAllEntities = async (): Promise<Entity[]> => {
  try {
    const response = await apiClient.get('/api/publishing-house/entities');
    return response.data.entities || response.data;
  } catch (error) {
    console.error('Error fetching entities:', error);
    throw error;
  }
};

/**
 * Get entity by ID
 */
export const getEntity = async (entityId: string): Promise<Entity> => {
  try {
    const response = await apiClient.get(`/api/publishing-house/entities/${entityId}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching entity ${entityId}:`, error);
    throw error;
  }
};

/**
 * Get entity content
 */
export const getEntityContent = async (entityId: string): Promise<any[]> => {
  try {
    const response = await apiClient.get(`/api/publishing-house/entities/${entityId}/content`);
    return response.data.content || response.data;
  } catch (error) {
    console.error(`Error fetching content for ${entityId}:`, error);
    throw error;
  }
};

/**
 * Get entity social media
 */
export const getEntitySocialMedia = async (entityId: string): Promise<any[]> => {
  try {
    const response = await apiClient.get(`/api/publishing-house/entities/${entityId}/social-media`);
    return response.data.social_media || response.data;
  } catch (error) {
    console.error(`Error fetching social media for ${entityId}:`, error);
    throw error;
  }
};
