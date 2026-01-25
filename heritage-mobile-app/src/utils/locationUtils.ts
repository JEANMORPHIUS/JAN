/**
 * Location Utilities
 * GPS, distance calculation, and nearby sites
 */

/**
 * Calculate distance between two coordinates using Haversine formula
 * Returns distance in kilometers
 */
export const calculateDistance = (
  lat1: number,
  lon1: number,
  lat2: number,
  lon2: number
): number => {
  const R = 6371; // Earth's radius in kilometers
  
  const dLat = toRadians(lat2 - lat1);
  const dLon = toRadians(lon2 - lon1);
  
  const a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(toRadians(lat1)) *
      Math.cos(toRadians(lat2)) *
      Math.sin(dLon / 2) *
      Math.sin(dLon / 2);
  
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  const distance = R * c;
  
  return distance;
};

/**
 * Calculate bearing (direction) from point 1 to point 2
 * Returns bearing in degrees (0-360)
 */
export const calculateBearing = (
  lat1: number,
  lon1: number,
  lat2: number,
  lon2: number
): number => {
  const lat1Rad = toRadians(lat1);
  const lat2Rad = toRadians(lat2);
  const dLon = toRadians(lon2 - lon1);
  
  const y = Math.sin(dLon) * Math.cos(lat2Rad);
  const x =
    Math.cos(lat1Rad) * Math.sin(lat2Rad) -
    Math.sin(lat1Rad) * Math.cos(lat2Rad) * Math.cos(dLon);
  
  let bearing = Math.atan2(y, x);
  bearing = toDegrees(bearing);
  bearing = (bearing + 360) % 360;
  
  return bearing;
};

/**
 * Format distance for display
 */
export const formatDistance = (distanceKm: number): string => {
  if (distanceKm < 1) {
    return `${Math.round(distanceKm * 1000)}m`;
  } else if (distanceKm < 100) {
    return `${distanceKm.toFixed(1)}km`;
  } else {
    return `${Math.round(distanceKm)}km`;
  }
};

/**
 * Get direction name from bearing
 */
export const getDirectionName = (bearing: number): string => {
  const directions = [
    'N', 'NNE', 'NE', 'ENE',
    'E', 'ESE', 'SE', 'SSE',
    'S', 'SSW', 'SW', 'WSW',
    'W', 'WNW', 'NW', 'NNW'
  ];
  const index = Math.round(bearing / 22.5) % 16;
  return directions[index];
};

/**
 * Find nearby sites within a radius
 */
export interface NearbySite {
  id: string;
  name: string;
  type: 'wonder' | 'pillar';
  distance: number;
  bearing: number;
  coordinates: {
    lat: number;
    lon: number;
  };
  resonance: number;
}

export const findNearbySites = (
  userLat: number,
  userLon: number,
  sites: Array<{
    id: string;
    name: string;
    type: 'wonder' | 'pillar';
    coordinates: { lat: number; lon: number };
    resonance: number;
  }>,
  radiusKm: number = 100
): NearbySite[] => {
  const nearby: NearbySite[] = [];
  
  for (const site of sites) {
    const distance = calculateDistance(
      userLat,
      userLon,
      site.coordinates.lat,
      site.coordinates.lon
    );
    
    if (distance <= radiusKm) {
      const bearing = calculateBearing(
        userLat,
        userLon,
        site.coordinates.lat,
        site.coordinates.lon
      );
      
      nearby.push({
        id: site.id,
        name: site.name,
        type: site.type,
        distance,
        bearing,
        coordinates: site.coordinates,
        resonance: site.resonance,
      });
    }
  }
  
  // Sort by distance
  nearby.sort((a, b) => a.distance - b.distance);
  
  return nearby;
};

/**
 * Helper functions
 */
const toRadians = (degrees: number): number => {
  return degrees * (Math.PI / 180);
};

const toDegrees = (radians: number): number => {
  return radians * (180 / Math.PI);
};
