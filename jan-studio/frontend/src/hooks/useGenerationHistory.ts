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
 * React Query hooks for generation history
 */

import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { getGenerationHistory, saveToHistory, clearHistory } from '@/api/generation';

export function useGenerationHistory() {
  return useQuery({
    queryKey: ['generation-history'],
    queryFn: getGenerationHistory,
    staleTime: 1 * 60 * 1000, // 1 minute
  });
}

export function useSaveToHistory() {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: saveToHistory,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['generation-history'] });
    },
  });
}

export function useClearHistory() {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: clearHistory,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['generation-history'] });
    },
  });
}
