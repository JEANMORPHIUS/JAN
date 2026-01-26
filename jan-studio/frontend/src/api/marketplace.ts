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

import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface Persona {
  id: number;
  name: string;
  author_name?: string;
  description?: string;
  category?: string;
  downloads: number;
  rating: number;
  rating_count: number;
  version: string;
  created_at: string;
}

export interface PersonaDetail {
  persona: Persona;
  files: Array<{
    id: number;
    file_path: string;
    file_content: string;
    version: string;
  }>;
  ratings: Array<{
    id: number;
    username?: string;
    rating: number;
    comment?: string;
    created_at: string;
  }>;
}

// Browse personas
export async function getPersonas(params?: {
  category?: string;
  status?: string;
  limit?: number;
  offset?: number;
  sort_by?: string;
}): Promise<Persona[]> {
  const response = await api.get('/api/marketplace/personas', { params });
  return response.data;
}

// Get persona details
export async function getPersonaDetails(personaId: number): Promise<PersonaDetail> {
  const response = await api.get(`/api/marketplace/personas/${personaId}`);
  return response.data;
}

// Submit persona
export async function submitPersona(data: {
  name: string;
  author_username: string;
  author_email: string;
  description: string;
  category?: string;
  files: Array<{ path: string; content: string }>;
}): Promise<void> {
  await api.post('/api/marketplace/personas', data);
}

// Download persona
export async function downloadPersona(
  personaId: number,
  userId?: number,
  username?: string
): Promise<{ persona: Persona; files: any[] }> {
  const response = await api.post(`/api/marketplace/personas/${personaId}/download`, {
    user_id: userId,
    username,
  });
  return response.data;
}

// Rate persona
export async function ratePersona(
  personaId: number,
  rating: number,
  comment?: string,
  userId?: number,
  username?: string
): Promise<void> {
  await api.post(`/api/marketplace/personas/${personaId}/rate`, {
    user_id: userId,
    username,
    rating,
    comment,
  });
}

// Get categories
export async function getCategories(): Promise<string[]> {
  const response = await api.get('/api/marketplace/categories');
  return response.data;
}

