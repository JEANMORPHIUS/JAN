/**
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
 * THE REST IS UP TO BABA X.
 * 
 * React Query hooks for personas
 */

import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { getPersonas, createPersona, deletePersona, getPersonaFiles } from '@/api/personas';
import type { PersonaInfo } from '@/api/personas';

export function usePersonas() {
  return useQuery({
    queryKey: ['personas'],
    queryFn: async () => {
      const personaNames = await getPersonas();
      const details = await Promise.all(
        personaNames.map(async (name) => {
          try {
            const files = await getPersonaFiles(name);
            return {
              name,
              fileCount: files.length,
              ruleCount: files.filter(f => f.includes('rules') || f.includes('profile')).length,
            } as PersonaInfo;
          } catch {
            return { name, fileCount: 0, ruleCount: 0 } as PersonaInfo;
          }
        })
      );
      return details;
    },
  });
}

export function useCreatePersona() {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: createPersona,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['personas'] });
    },
  });
}

export function useDeletePersona() {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: deletePersona,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['personas'] });
    },
  });
}
