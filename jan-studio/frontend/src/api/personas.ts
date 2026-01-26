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

export interface PersonaFile {
  name: string;
  content: string;
}

// Get list of all personas
export async function getPersonas(): Promise<string[]> {
  try {
    const response = await api.get('/api/jan/personas');
    return response.data || [];
  } catch (err) {
    console.error('Failed to get personas:', err);
    return [];
  }
}

// Create a new persona
export async function createPersona(name: string): Promise<void> {
  await api.post('/api/jan/personas', { name });
}

// Get list of files for a persona
export async function getPersonaFiles(personaName: string): Promise<string[]> {
  const response = await api.get(`/api/jan/personas/${personaName}/files`);
  return response.data;
}

// Get content of a specific file
export async function getPersonaFile(
  personaName: string,
  fileName: string
): Promise<string> {
  const response = await api.get(`/api/jan/personas/${personaName}/files/${fileName}`);
  return response.data;
}

// Save content to a file
export async function savePersonaFile(
  personaName: string,
  fileName: string,
  content: string
): Promise<void> {
  await api.put(`/api/jan/personas/${personaName}/files/${fileName}`, { content });
}

// Delete a persona
export async function deletePersona(personaName: string): Promise<void> {
  await api.delete(`/api/jan/personas/${personaName}`);
}

