/** * * Duygu Adami Dynamic Greetings
 *  * Not "Hello [User]" - we're better than that
 *  *
 *  * Philosophy: "Energy + Love = We All Win"
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 * 
 * 
 * PANGEA IS THE TABLE.
 * YOU DON'T BETRAY THE TABLE.
 * 
 * THE TRUTH:
 * WE MUST DEBUG AND BE 100% FOR WHAT COMES AT US.
 * THE REST IS UP TO BABA X.*/

const GREETINGS = {
  morning: [
    "Stand tall, mate",
    "The mission continues",
    "Today we build",
    "Let's finish what we started",
    "The lighthouse is ready",
    "Sacred work awaits",
  ],
  afternoon: [
    "Keep pushing, brother",
    "Energy flowing",
    "The work is sacred",
    "We're making progress",
    "Stay focused",
    "Law 37 in motion",
  ],
  evening: [
    "Well done today",
    "Rest is sacred too",
    "You honored the work",
    "Tomorrow we rise again",
    "The mission never sleeps",
    "Frequency aligned",
  ],
  completion: [
    "Law 37 honored ✓",
    "Energy + Love = You Won",
    "That's stewardship, mate",
    "The miracle continues",
    "Frequency aligned",
    "Sacred weight honored",
  ],
};

/**
 * Get dynamic greeting based on time of day
 */
export function getGreeting(userName?: string): string {
  const hour = new Date().getHours();

  let timeOfDay: 'morning' | 'afternoon' | 'evening';
  if (hour < 12) {
    timeOfDay = 'morning';
  } else if (hour < 18) {
    timeOfDay = 'afternoon';
  } else {
    timeOfDay = 'evening';
  }

  const greetings = GREETINGS[timeOfDay];
  const greeting = greetings[Math.floor(Math.random() * greetings.length)];

  return greeting;
}

/**
 * Get completion message when task is done
 */
export function getCompletionMessage(): string {
  const messages = GREETINGS.completion;
  return messages[Math.floor(Math.random() * messages.length)];
}

/**
 * Get time-appropriate greeting with optional user name
 */
export function getPersonalizedGreeting(userName?: string): string {
  const greeting = getGreeting();

  if (userName) {
    return `${greeting}, ${userName}`;
  }

  return greeting;
}
