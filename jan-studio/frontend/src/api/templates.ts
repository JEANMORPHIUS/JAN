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

export interface Template {
  name: string;
  description?: string;
  category?: string;
  created_at: string;
  file_count: number;
  persona_name?: string;
}

export interface TemplateData {
  name: string;
  description?: string;
  category?: string;
  created_at: string;
  persona_data: {
    name: string;
    files: { [key: string]: string };
  };
}

// Get list of all templates
export async function getTemplates(): Promise<Template[]> {
  try {
    const response = await api.get('/api/templates/list');
    return response.data || [];
  } catch (err) {
    console.error('Failed to get templates:', err);
    return [];
  }
}

// Get template details
export async function getTemplate(templateName: string): Promise<TemplateData> {
  const response = await api.get(`/api/templates/${templateName}`);
  return response.data;
}

// Create persona from template
export async function instantiateTemplate(
  templateName: string,
  personaName: string,
  overwrite: boolean = false
): Promise<void> {
  await api.post('/api/templates/instantiate', {
    template_name: templateName,
    persona_name: personaName,
    overwrite,
  });
}

// Save persona as template
export async function savePersonaAsTemplate(
  personaName: string,
  templateName: string,
  description?: string
): Promise<void> {
  await api.post('/api/templates/save-from-persona', null, {
    params: {
      persona_name: personaName,
      template_name: templateName,
      description,
    },
  });
}

// Create template from data
export async function createTemplate(
  templateName: string,
  personaData: any,
  description?: string,
  category?: string
): Promise<void> {
  await api.post('/api/templates/create', {
    template_name: templateName,
    persona_data: personaData,
    description,
    category,
  });
}

// Delete template
export async function deleteTemplate(templateName: string): Promise<void> {
  await api.delete(`/api/templates/${templateName}`);
}

