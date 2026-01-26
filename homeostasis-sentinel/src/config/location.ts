/** * * LOCATION CONFIGURATION
 *  *
 *  * Purpose: Store user location for accurate astronomical calculations
 *  * Foundation: "Man and Earth live symbiotically" - require user's actual location
 *  *
 *  * Locations serve the communities:
 *  * - London (8 communities)
 *  * - North Cyprus (Turkish Cypriot community)
 *  * - Cyprus (Turkish + Greek communities)
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

export interface LocationConfig {
  /** Display name */
  name: string;
  /** Latitude (degrees) */
  latitude: number;
  /** Longitude (degrees) */
  longitude: number;
  /** IANA timezone identifier */
  timezone: string;
  /** Description for user */
  description?: string;
}

/**
 * Preset locations for communities
 */
export const PRESET_LOCATIONS: Record<string, LocationConfig> = {
  london: {
    name: 'London, UK',
    latitude: 51.5074,
    longitude: -0.1278,
    timezone: 'Europe/London',
    description: '8 communities: Turkish, Kurdish, Cypriot, North London Muslim, East London Muslim, West London Turkish, South London Mixed, Central London Professional'
  },
  northCyprus: {
    name: 'North Cyprus',
    latitude: 35.1856,
    longitude: 33.3823,
    timezone: 'Asia/Nicosia',
    description: 'Turkish Cypriot community'
  },
  cyprus: {
    name: 'Cyprus',
    latitude: 35.1264,
    longitude: 33.4299,
    timezone: 'Asia/Nicosia',
    description: 'Turkish and Greek communities'
  },
  istanbul: {
    name: 'Istanbul, Turkey',
    latitude: 41.0082,
    longitude: 28.9784,
    timezone: 'Europe/Istanbul',
    description: 'Turkish community, ancestral homeland'
  }
};

/**
 * Default location (London)
 * Honors primary community: 8 London communities
 */
export const DEFAULT_LOCATION = PRESET_LOCATIONS.london;

/**
 * Load location from localStorage or use default
 */
export function loadLocation(): LocationConfig {
  try {
    const stored = localStorage.getItem('homeostasis_location');
    if (stored) {
      const parsed = JSON.parse(stored);
      // Validate it's a valid location
      if (parsed.latitude && parsed.longitude && parsed.timezone) {
        return parsed;
      }
    }
  } catch (e) {
    console.warn('Failed to load location from storage, using default', e);
  }

  return DEFAULT_LOCATION;
}

/**
 * Save location to localStorage
 */
export function saveLocation(location: LocationConfig): void {
  try {
    localStorage.setItem('homeostasis_location', JSON.stringify(location));
  } catch (e) {
    console.error('Failed to save location to storage', e);
  }
}

/**
 * Get location by name
 */
export function getLocationByName(name: string): LocationConfig | undefined {
  return Object.values(PRESET_LOCATIONS).find(loc => loc.name === name);
}

/**
 * Check if using custom location (not in presets)
 */
export function isCustomLocation(location: LocationConfig): boolean {
  return !Object.values(PRESET_LOCATIONS).some(
    preset => preset.name === location.name
  );
}
