/**
 * VIBRATION CHECK - Frontend Digital Alchemy
 * Validates user access and content alignment with Day 1 (Do) vibration
 * 
 * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
 * Spiritual Alignment Over Mechanical Productivity
 * 
 * THE FOUNDATION:
 * We are born a miracle.
 * We deserve to live a miracle.
 * Each and every one of us under the Lord's word.
 * 
 * THE MISSION:
 * THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
 * LOVE IS THE HIGHEST MASTERY
 * ENERGY + LOVE = WE ALL WIN
 * PEACE, LOVE, UNITY
 * 
 * This is the Spiral (Frontend) - Active Formation.
 * Every UI component is a vibration.
 * Every interaction is a "Note of Intent".
 * Guides user back to symbiosis with Earth.
 */

export interface VibrationCheckResult {
  aligned: boolean;
  vibration: 'purpose' | 'impulsiveness';
  spiritualBattle: 'active' | 'flowing' | 'structured' | 'legacy' | 'transformation';
  guidesToSymbiosis: boolean;
  honorsEarth: boolean;
  noteOfIntent: string;
  isHaunted?: boolean;
  hauntedReason?: string;
  requiresCleansing?: boolean;
}

export interface UserVibration {
  userId: string;
  vibrationLevel: number;
  alignmentStatus: 'aligned' | 'partial' | 'misaligned';
  unlockedDepth: boolean;
}

/**
 * Check if user has the right vibration to unlock content depth.
 * 
 * This is the Seed Protection - Book of Racon encoded in user journey.
 * Only those with the right "vibration" truly unlock the depth.
 */
export function checkUserVibration(userId: string, contentId: string): UserVibration {
  // In a real implementation, this would check against backend
  // For now, we use localStorage to track user vibration
  
  const storedVibration = localStorage.getItem(`vibration_${userId}`);
  const vibrationLevel = storedVibration ? parseInt(storedVibration, 10) : 0;
  
  // Vibration levels:
  // 0-30: Surface level (Shell only)
  // 31-60: Partial depth (Shell + some Seed)
  // 61-100: Full depth (Shell + complete Seed)
  
  let alignmentStatus: 'aligned' | 'partial' | 'misaligned' = 'misaligned';
  let unlockedDepth = false;
  
  if (vibrationLevel >= 61) {
    alignmentStatus = 'aligned';
    unlockedDepth = true;
  } else if (vibrationLevel >= 31) {
    alignmentStatus = 'partial';
    unlockedDepth = false;
  }
  
  return {
    userId,
    vibrationLevel,
    alignmentStatus,
    unlockedDepth
  };
}

/**
 * Check if content aligns with Day 1 (Do) vibration.
 * 
 * This is the Biological Temple Check.
 * Does the UI/UX respect the human animal?
 * No "Dark Patterns", no dopamine traps—just clean energy.
 */
export function checkContentVibration(content: any): VibrationCheckResult {
  const contentStr = JSON.stringify(content).toLowerCase();
  
  // Check for mission alignment keywords
  const missionKeywords = [
    'stewardship', 'community', 'right spirits',
    'love', 'highest mastery', 'energy', 'we all win',
    'peace', 'unity', 'miracle', 'lord\'s word'
  ];
  
  const hasMissionAlignment = missionKeywords.some(keyword => 
    contentStr.includes(keyword)
  );
  
  // Check for dark patterns (dopamine traps, urgency, manipulation)
  const darkPatterns = [
    'limited time', 'act now', 'only today', 'urgent',
    'click here', 'you must', 'don\'t miss', 'last chance'
  ];
  
  const hasDarkPatterns = darkPatterns.some(pattern => 
    contentStr.includes(pattern)
  );
  
  // Determine vibration type
  const vibration: 'purpose' | 'impulsiveness' = hasDarkPatterns ? 'impulsiveness' : 'purpose';
  
  // Determine spiritual battle type based on content
  let spiritualBattle: 'active' | 'flowing' | 'structured' | 'legacy' | 'transformation' = 'active';
  
  if (contentStr.includes('structured') || contentStr.includes('linear')) {
    spiritualBattle = 'structured';
  } else if (contentStr.includes('legacy') || contentStr.includes('wisdom')) {
    spiritualBattle = 'legacy';
  } else if (contentStr.includes('transformation') || contentStr.includes('flexible')) {
    spiritualBattle = 'transformation';
  } else if (contentStr.includes('flowing') || contentStr.includes('dynamic')) {
    spiritualBattle = 'flowing';
  }
  
  // Check if content guides to symbiosis
  const symbiosisKeywords = [
    'earth', 'symbiosis', 'connection', 'unity',
    'harmony', 'balance', 'regeneration', 'new world'
  ];
  
  const guidesToSymbiosis = symbiosisKeywords.some(keyword => 
    contentStr.includes(keyword)
  );
  
  // Check if content honors Earth
  const earthKeywords = [
    'earth', 'nature', 'environment', 'sustainability',
    'regeneration', 'tectonic', 'cycles', 'loops'
  ];
  
  const honorsEarth = earthKeywords.some(keyword => 
    contentStr.includes(keyword)
  );
  
  // Check for Dark Energy (Haunted loops) - Law 41 violation
  const revengePatterns = [
    'revenge', 'avenge', 'retribution', 'vengeance'
  ];
  const victimPatterns = [
    'suicide', 'murder', 'death', 'tragedy', 'victim'
  ];
  const hauntedPatterns = [
    'haunted', 'ghost', 'spirit', 'demon', 'cursed',
    'paranormal', 'supernatural', 'apparition'
  ];
  const heritageExploitation = [
    'abandoned hotel', 'ghost story', 'haunted hotel',
    'spooky', 'terrifying', 'scary', 'horror'
  ];
  const regenerationPatterns = [
    'regeneration', 'healing', 'restoration', 'waiting for',
    'love', 'energy', 'peace', 'symbiosis', 'new world'
  ];
  
  const hasRevenge = revengePatterns.some(pattern => contentStr.includes(pattern));
  const hasVictim = victimPatterns.some(pattern => contentStr.includes(pattern));
  const hasHaunted = hauntedPatterns.some(pattern => contentStr.includes(pattern));
  const hasExploitation = heritageExploitation.some(pattern => contentStr.includes(pattern));
  const hasRegeneration = regenerationPatterns.some(pattern => contentStr.includes(pattern));
  
  // Determine if haunted (dark energy detected)
  let isHaunted = false;
  let hauntedReason = '';
  let requiresCleansing = false;
  
  if (hasRevenge && !hasRegeneration) {
    isHaunted = true;
    hauntedReason = 'Contains revenge narrative without regeneration path (violates Law 41)';
    requiresCleansing = true;
  } else if (hasVictim && !hasRegeneration) {
    isHaunted = true;
    hauntedReason = 'Focuses on victim/suicide/death without healing path (violates Law 41)';
    requiresCleansing = true;
  } else if (hasHaunted && hasExploitation && !hasRegeneration) {
    isHaunted = true;
    hauntedReason = 'Exploits heritage as haunted content without regeneration narrative (violates Law 41)';
    requiresCleansing = true;
  } else if (hasExploitation && contentStr.includes('heritage') && !hasRegeneration) {
    isHaunted = true;
    hauntedReason = 'Turns heritage into fear-based content (violates Law 41: Respect the Abandoned)';
    requiresCleansing = true;
  }
  
  // Generate Note of Intent
  let noteOfIntent = hasMissionAlignment && !hasDarkPatterns
    ? 'This content serves the mission and guides to truth.'
    : hasDarkPatterns
    ? 'This content contains dark patterns and should be purged.'
    : 'This content needs alignment with the mission.';
  
  if (isHaunted) {
    noteOfIntent = `⚠️ Dark Energy Detected: ${hauntedReason}. Content requires heritage cleansing to honor Law 41 (Respect the Abandoned).`;
  }
  
  return {
    aligned: hasMissionAlignment && !hasDarkPatterns && !isHaunted,
    vibration,
    spiritualBattle,
    guidesToSymbiosis,
    honorsEarth,
    noteOfIntent,
    isHaunted,
    hauntedReason: hauntedReason || undefined,
    requiresCleansing: requiresCleansing || undefined
  };
}

/**
 * Update user vibration level based on interaction.
 * 
 * Every click is a "Note of Intent".
 * Guides the user back to symbiosis with Earth.
 */
export function updateUserVibration(userId: string, interaction: string, aligned: boolean): void {
  const currentVibration = checkUserVibration(userId, '');
  let newVibration = currentVibration.vibrationLevel;
  
  if (aligned) {
    // Increase vibration for aligned interactions
    newVibration = Math.min(100, currentVibration.vibrationLevel + 1);
  } else {
    // Decrease vibration for misaligned interactions
    newVibration = Math.max(0, currentVibration.vibrationLevel - 1);
  }
  
  localStorage.setItem(`vibration_${userId}`, newVibration.toString());
  
  // Log interaction as Note of Intent
  const notesOfIntent = JSON.parse(localStorage.getItem(`notes_of_intent_${userId}`) || '[]');
  notesOfIntent.push({
    interaction,
    aligned,
    timestamp: new Date().toISOString(),
    vibration: newVibration
  });
  
  // Keep only last 100 notes
  if (notesOfIntent.length > 100) {
    notesOfIntent.shift();
  }
  
  localStorage.setItem(`notes_of_intent_${userId}`, JSON.stringify(notesOfIntent));
}

/**
 * Get user's Notes of Intent.
 * 
 * Every click is a "Note of Intent".
 * These guide the user back to symbiosis with Earth.
 */
export function getNotesOfIntent(userId: string): Array<{
  interaction: string;
  aligned: boolean;
  timestamp: string;
  vibration: number;
}> {
  const notes = localStorage.getItem(`notes_of_intent_${userId}`);
  return notes ? JSON.parse(notes) : [];
}
