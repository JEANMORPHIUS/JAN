/**
 * Spiritual Codebase Hacker Integration
 * Auto-embedded system-wide integration
 * 
 * This module provides access to the Spiritual Codebase Hacker API
 */

const HACKER_API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface HackLoopRequest {
  loop_type: string;
  stimulus: string;
  expected_reaction: string;
  hack_action?: string;
}

export interface GeneticEditRequest {
  loop_type: string;
  generational_pattern: string;
  edit_command?: string;
}

export interface StealthModeRequest {
  noise_refused: string[];
  frequency_aligned?: string;
}

export const hackLoop = async (request: HackLoopRequest) => {
  const response = await fetch(`${HACKER_API_BASE}/api/spiritual-codebase-hacker/hack-loop`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(request)
  });
  return response.json();
};

export const performGeneticEdit = async (request: GeneticEditRequest) => {
  const response = await fetch(`${HACKER_API_BASE}/api/spiritual-codebase-hacker/genetic-edit`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(request)
  });
  return response.json();
};

export const activateStealthMode = async (request: StealthModeRequest) => {
  const response = await fetch(`${HACKER_API_BASE}/api/spiritual-codebase-hacker/stealth-mode`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(request)
  });
  return response.json();
};

export const HACKER_AVAILABLE = true;
