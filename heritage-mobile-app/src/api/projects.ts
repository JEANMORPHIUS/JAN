/** * * Projects API Calls
 *  * All 4 business projects
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

export interface Project {
  project_id: string;
  name: string;
  type: 'business_project';
  description: string;
  ecommerce?: boolean;
  products?: any[];
  videos?: any[];
  production?: any;
  inventory?: any;
}

/**
 * Get all projects
 */
export const getProjects = async (): Promise<Project[]> => {
  try {
    const response = await apiClient.get('/api/publishing-house/projects');
    return response.data.projects || response.data;
  } catch (error) {
    console.error('Error fetching projects:', error);
    throw error;
  }
};

/**
 * Get project by ID
 */
export const getProject = async (projectId: string): Promise<Project> => {
  try {
    const response = await apiClient.get(`/api/publishing-house/projects/${projectId}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching project ${projectId}:`, error);
    throw error;
  }
};

/**
 * Get project products (for e-commerce projects)
 */
export const getProjectProducts = async (projectId: string): Promise<any[]> => {
  try {
    const response = await apiClient.get(`/api/publishing-house/projects/${projectId}/products`);
    return response.data.products || response.data;
  } catch (error) {
    console.error(`Error fetching products for ${projectId}:`, error);
    throw error;
  }
};

/**
 * Get project videos
 */
export const getProjectVideos = async (projectId: string): Promise<any[]> => {
  try {
    const response = await apiClient.get(`/api/publishing-house/projects/${projectId}/videos`);
    return response.data.videos || response.data;
  } catch (error) {
    console.error(`Error fetching videos for ${projectId}:`, error);
    throw error;
  }
};
