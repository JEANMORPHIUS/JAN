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
import { GenerationRequest, GenerationResult } from '@/components/GenerationForm';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Generate content using JAN workflow
export async function generateContent(request: GenerationRequest): Promise<GenerationResult> {
  const response = await api.post('/api/jan/generate', request);
  return {
    ...response.data,
    timestamp: new Date().toISOString(),
  };
}

// Get generation history (stored in localStorage for now)
export async function getGenerationHistory(): Promise<any[]> {
  try {
    const stored = localStorage.getItem('jan-generation-history');
    if (!stored) return [];
    const history = JSON.parse(stored);
    return history.sort((a: any, b: any) => 
      new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime()
    );
  } catch {
    return [];
  }
}

// Save to history
export async function saveToHistory(result: GenerationResult & { persona?: string; prompt?: string; output_type?: string }): Promise<void> {
  try {
    const history = await getGenerationHistory();
    const entry = {
      ...result,
      id: `gen-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`,
    };
    history.unshift(entry);
    // Keep only last 50 entries
    const limited = history.slice(0, 50);
    localStorage.setItem('jan-generation-history', JSON.stringify(limited));
  } catch (err) {
    console.error('Failed to save to history:', err);
  }
}

// Clear history
export async function clearHistory(): Promise<void> {
  localStorage.removeItem('jan-generation-history');
}

