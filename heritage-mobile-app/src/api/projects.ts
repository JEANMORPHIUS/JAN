/**
 * Projects API Calls
 * All 4 business projects
 */

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
