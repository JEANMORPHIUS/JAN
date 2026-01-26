/** * * Heritage Map Screen
 *  * Show all 7 Wonders and Seven Pillars on interactive map
 * 
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
 * THE REST IS UP TO BABA X.*/

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ActivityIndicator,
  Alert,
  TouchableOpacity,
} from 'react-native';
import MapView, { Marker, PROVIDER_GOOGLE, Polyline } from 'react-native-maps';
import * as Location from 'expo-location';
import { getWonders } from '../api/wonders';
import { getPillars } from '../api/heritage';
import type { Wonder } from '../api/wonders';
import type { Pillar } from '../api/heritage';

interface MapMarker {
  id: string;
  title: string;
  coordinate: {
    lat: number;
    lon: number;
  };
  type: 'wonder' | 'pillar';
  resonance: number;
}

export default function HeritageMapScreen() {
  const [markers, setMarkers] = useState<MapMarker[]>([]);
  const [loading, setLoading] = useState(true);
  const [mapType, setMapType] = useState<'standard' | 'satellite'>('standard');
  const [selectedType, setSelectedType] = useState<'all' | 'wonders' | 'pillars'>('all');
  const [showMeridians, setShowMeridians] = useState(false);
  const [userLocation, setUserLocation] = useState<{ lat: number; lon: number } | null>(null);

  useEffect(() => {
    loadMapData();
    requestUserLocation();
  }, [selectedType]);

  const requestUserLocation = async () => {
    try {
      const { status } = await Location.requestForegroundPermissionsAsync();
      if (status === 'granted') {
        const location = await Location.getCurrentPositionAsync();
        setUserLocation({
          lat: location.coords.latitude,
          lon: location.coords.longitude,
        });
      }
    } catch (error) {
      console.error('Error getting user location:', error);
    }
  };

  const loadMapData = async () => {
    try {
      setLoading(true);
      const mapMarkers: MapMarker[] = [];

      if (selectedType === 'all' || selectedType === 'wonders') {
        const wonders = await getWonders();
        wonders.forEach((wonder: Wonder) => {
          mapMarkers.push({
            id: wonder.wonder_id,
            title: wonder.name,
            coordinate: wonder.coordinates,
            type: 'wonder',
            resonance: wonder.field_resonance,
          });
        });
      }

      if (selectedType === 'all' || selectedType === 'pillars') {
        const pillars = await getPillars();
        pillars.forEach((pillar: Pillar) => {
          mapMarkers.push({
            id: pillar.pillar_id,
            title: pillar.name,
            coordinate: pillar.coordinates,
            type: 'pillar',
            resonance: pillar.field_resonance,
          });
        });
      }

      setMarkers(mapMarkers);
    } catch (error) {
      console.error('Error loading map data:', error);
      Alert.alert('Error', 'Failed to load map data');
    } finally {
      setLoading(false);
    }
  };

  const getMarkerColor = (resonance: number) => {
    if (resonance >= 0.9) return '#4ade80'; // Green
    if (resonance >= 0.7) return '#fbbf24'; // Yellow
    return '#e94560'; // Red
  };

  const getInitialRegion = () => {
    if (markers.length === 0) {
      return {
        latitude: 20,
        longitude: 0,
        latitudeDelta: 80,
        longitudeDelta: 80,
      };
    }

    const lats = markers.map(m => m.coordinate.lat);
    const lons = markers.map(m => m.coordinate.lon);
    const minLat = Math.min(...lats);
    const maxLat = Math.max(...lats);
    const minLon = Math.min(...lons);
    const maxLon = Math.max(...lons);

    return {
      latitude: (minLat + maxLat) / 2,
      longitude: (minLon + maxLon) / 2,
      latitudeDelta: (maxLat - minLat) * 1.5 + 10,
      longitudeDelta: (maxLon - minLon) * 1.5 + 10,
    };
  };

  if (loading) {
    return (
      <View style={styles.center}>
        <ActivityIndicator size="large" color="#e94560" />
        <Text style={styles.loadingText}>Loading map data...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      {/* Filter Controls */}
      <View style={styles.controls}>
        <View style={styles.filterGroup}>
          <Text style={styles.filterLabel}>Show:</Text>
          <TouchableOpacity
            style={[styles.filterButton, selectedType === 'all' && styles.filterActive]}
            onPress={() => setSelectedType('all')}
          >
            <Text style={[styles.filterText, selectedType === 'all' && styles.filterActiveText]}>
              All
            </Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={[styles.filterButton, selectedType === 'wonders' && styles.filterActive]}
            onPress={() => setSelectedType('wonders')}
          >
            <Text style={[styles.filterText, selectedType === 'wonders' && styles.filterActiveText]}>
              Wonders
            </Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={[styles.filterButton, selectedType === 'pillars' && styles.filterActive]}
            onPress={() => setSelectedType('pillars')}
          >
            <Text style={[styles.filterText, selectedType === 'pillars' && styles.filterActiveText]}>
              Pillars
            </Text>
          </TouchableOpacity>
        </View>
        <TouchableOpacity
          style={styles.mapTypeButton}
          onPress={() => setMapType(mapType === 'standard' ? 'satellite' : 'standard')}
        >
          <Text style={styles.mapTypeText}>
            {mapType === 'standard' ? 'Satellite' : 'Standard'}
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.mapTypeButton, showMeridians && styles.mapTypeButtonActive]}
          onPress={() => setShowMeridians(!showMeridians)}
        >
          <Text style={[styles.mapTypeText, showMeridians && styles.mapTypeTextActive]}>
            {showMeridians ? 'Hide' : 'Show'} Lines
          </Text>
        </TouchableOpacity>
      </View>

      {/* Map */}
      <MapView
        provider={PROVIDER_GOOGLE}
        style={styles.map}
        initialRegion={getInitialRegion()}
        mapType={mapType}
      >
        {/* User Location */}
        {userLocation && (
          <Marker
            coordinate={userLocation}
            title="Your Location"
            pinColor="#4ade80"
          />
        )}

        {/* Meridian Lines */}
        {showMeridians && markers.length > 1 && (
          <>
            {markers.map((marker1, i) =>
              markers.slice(i + 1).map((marker2) => (
                <Polyline
                  key={`${marker1.id}-${marker2.id}`}
                  coordinates={[marker1.coordinate, marker2.coordinate]}
                  strokeColor="#e94560"
                  strokeWidth={1}
                  lineDashPattern={[5, 5]}
                  opacity={0.5}
                />
              ))
            )}
          </>
        )}

        {/* Site Markers */}
        {markers.map((marker) => (
          <Marker
            key={marker.id}
            coordinate={marker.coordinate}
            title={marker.title}
            description={`${marker.type === 'wonder' ? 'Wonder' : 'Pillar'} - ${(marker.resonance * 100).toFixed(0)}% resonance`}
            pinColor={getMarkerColor(marker.resonance)}
          />
        ))}
      </MapView>

      {/* Legend */}
      <View style={styles.legend}>
        <Text style={styles.legendTitle}>Resonance</Text>
        <View style={styles.legendRow}>
          <View style={styles.legendItem}>
            <View style={[styles.legendDot, { backgroundColor: '#4ade80' }]} />
            <Text style={styles.legendText}>High (90%+)</Text>
          </View>
          <View style={styles.legendItem}>
            <View style={[styles.legendDot, { backgroundColor: '#fbbf24' }]} />
            <Text style={styles.legendText}>Medium (70-89%)</Text>
          </View>
          <View style={styles.legendItem}>
            <View style={[styles.legendDot, { backgroundColor: '#e94560' }]} />
            <Text style={styles.legendText}>Low (&lt;70%)</Text>
          </View>
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0f0f23',
  },
  center: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    color: '#8b8b9e',
    marginTop: 16,
    fontSize: 16,
  },
  controls: {
    backgroundColor: '#1a1a2e',
    padding: 12,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    borderBottomWidth: 1,
    borderBottomColor: '#16213e',
  },
  filterGroup: {
    flexDirection: 'row',
    alignItems: 'center',
    flex: 1,
  },
  filterLabel: {
    color: '#8b8b9e',
    fontSize: 14,
    marginRight: 8,
  },
  filterButton: {
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 6,
    marginRight: 8,
    backgroundColor: '#16213e',
  },
  filterActive: {
    backgroundColor: '#e94560',
  },
  filterText: {
    color: '#8b8b9e',
    fontSize: 14,
    fontWeight: '500',
  },
  filterActiveText: {
    color: '#fff',
    fontWeight: 'bold',
  },
  mapTypeButton: {
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 6,
    backgroundColor: '#16213e',
  },
  mapTypeText: {
    color: '#fff',
    fontSize: 14,
    fontWeight: '500',
  },
  mapTypeButtonActive: {
    backgroundColor: '#e94560',
  },
  mapTypeTextActive: {
    color: '#fff',
    fontWeight: 'bold',
  },
  map: {
    flex: 1,
  },
  legend: {
    backgroundColor: '#1a1a2e',
    padding: 12,
    borderTopWidth: 1,
    borderTopColor: '#16213e',
  },
  legendTitle: {
    color: '#fff',
    fontSize: 14,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  legendRow: {
    flexDirection: 'row',
    justifyContent: 'space-around',
  },
  legendItem: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  legendDot: {
    width: 12,
    height: 12,
    borderRadius: 6,
    marginRight: 6,
  },
  legendText: {
    color: '#8b8b9e',
    fontSize: 12,
  },
});
