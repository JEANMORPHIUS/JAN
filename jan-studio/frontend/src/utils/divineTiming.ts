/**
 * DIVINE TIMING UTILITIES
 * Kronos, Chyros, and Moed Logic
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 */

import { TimingType, TimingWindow, ActivationWindow, MoedAppointment } from '../types/divineTiming';

/**
 * Distinguish between Kronos (clock time) and Chyros (divine timing windows)
 */
export function getTimingType(date: Date = new Date()): TimingType {
  // Chyros windows are specific divine timing moments
  // For now, we'll use a simple heuristic - can be enhanced with actual spiritual timing data
  const hour = date.getHours();
  const day = date.getDay();
  
  // Moed (appointed times) - specific divine appointments
  // Chyros - divine timing windows (often feel urgent, celebratory)
  // Kronos - regular clock time
  
  // Example: Morning hours (6-9) and evening (18-21) might be Chyros windows
  if ((hour >= 6 && hour <= 9) || (hour >= 18 && hour <= 21)) {
    return 'chyros';
  }
  
  // Specific days or times could be Moed
  // This is a placeholder - actual Moed times would come from spiritual calendar
  return 'kronos';
}

/**
 * Create 72-hour activation window
 */
export function create72HourWindow(startDate: Date): ActivationWindow {
  const endDate = new Date(startDate);
  endDate.setHours(endDate.getHours() + 72);
  
  const now = new Date();
  const elapsed = now.getTime() - startDate.getTime();
  const total = 72 * 60 * 60 * 1000; // 72 hours in milliseconds
  const progress = Math.min(100, Math.max(0, (elapsed / total) * 100));
  
  const currentDay = Math.floor((elapsed / (24 * 60 * 60 * 1000))) + 1;
  
  return {
    startDate,
    endDate,
    type: '72_hour',
    currentDay: Math.min(3, currentDay),
    progress
  };
}

/**
 * Create 40-day transition tracker
 */
export function create40DayWindow(startDate: Date): ActivationWindow {
  const endDate = new Date(startDate);
  endDate.setDate(endDate.getDate() + 40);
  
  const now = new Date();
  const elapsed = now.getTime() - startDate.getTime();
  const total = 40 * 24 * 60 * 60 * 1000; // 40 days in milliseconds
  const progress = Math.min(100, Math.max(0, (elapsed / total) * 100));
  
  const currentDay = Math.floor((elapsed / (24 * 60 * 60 * 1000))) + 1;
  
  return {
    startDate,
    endDate,
    type: '40_day',
    currentDay: Math.min(40, currentDay),
    progress
  };
}

/**
 * Check if current time is within a Moed (appointed time)
 */
export function isMoedTime(date: Date, appointments: MoedAppointment[]): boolean {
  const now = date.getTime();
  return appointments.some(appt => {
    const apptTime = new Date(appt.scheduledTime).getTime();
    const window = 15 * 60 * 1000; // 15 minute window
    return Math.abs(now - apptTime) < window && !appt.completed;
  });
}

/**
 * Get time remaining in activation window
 */
export function getTimeRemaining(window: ActivationWindow): {
  hours: number;
  minutes: number;
  seconds: number;
  isActive: boolean;
} {
  const now = new Date();
  const end = window.endDate.getTime();
  const current = now.getTime();
  
  if (current >= end) {
    return { hours: 0, minutes: 0, seconds: 0, isActive: false };
  }
  
  const remaining = end - current;
  const hours = Math.floor(remaining / (1000 * 60 * 60));
  const minutes = Math.floor((remaining % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((remaining % (1000 * 60)) / 1000);
  
  return { hours, minutes, seconds, isActive: true };
}

/**
 * Check if Day 21 identity shift milestone reached
 */
export function checkIdentityShift(activationStart: Date): {
  reached: boolean;
  daysRemaining: number;
  progress: number;
} {
  const now = new Date();
  const elapsed = now.getTime() - activationStart.getTime();
  const daysElapsed = Math.floor(elapsed / (24 * 60 * 60 * 1000));
  const daysRemaining = Math.max(0, 21 - daysElapsed);
  const progress = Math.min(100, (daysElapsed / 21) * 100);
  
  return {
    reached: daysElapsed >= 21,
    daysRemaining,
    progress
  };
}

/**
 * Format time for display with Chyros urgency
 */
export function formatChyrosTime(date: Date): string {
  const hours = date.getHours();
  const minutes = date.getMinutes();
  const ampm = hours >= 12 ? 'PM' : 'AM';
  const displayHours = hours % 12 || 12;
  return `${displayHours}:${minutes.toString().padStart(2, '0')} ${ampm}`;
}
