/** * * Nearby Sites Screen
 *  * GPS-based "Find nearby heritage sites" feature
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
  FlatList,
  TouchableOpacity,
  ActivityIndicator,
  Alert,
  RefreshControl,
} from 'react-native';
import * as Location from 'expo-location';
import { getWonders } from '../api/wonders';
import { getPillars } from '../api/heritage';
import { findNearbySites, formatDistance, getDirectionName } from '../utils/locationUtils';
import type { Wonder } from '../api/wonders';
import type { Pillar } from '../api/heritage';
import type { NearbySite } from '../utils/locationUtils';

export default function NearbySitesScreen() {
  const [nearbySites, setNearbySites] = useState<NearbySite[]>([]);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [userLocation, setUserLocation] = useState<{ lat: number; lon: number } | null>(null);
  const [locationError, setLocationError] = useState<string | null>(null);
  const [radius, setRadius] = useState(100); // km

  useEffect(() => {
    requestLocationAndLoad();
  }, []);

  const requestLocationAndLoad = async () => {
    try {
      setLoading(true);
      setLocationError(null);

      // Request location permissions
      const { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== 'granted') {
        setLocationError('Location permission denied');
        setLoading(false);
        return;
      }

      // Get current location
      const location = await Location.getCurrentPositionAsync({
        accuracy: Location.Accuracy.Balanced,
      });

      const coords = {
        lat: location.coords.latitude,
        lon: location.coords.longitude,
      };
      setUserLocation(coords);

      // Load sites and find nearby
      await loadNearbySites(coords);
    } catch (error) {
      console.error('Error getting location:', error);
      setLocationError('Failed to get location');
      Alert.alert('Error', 'Could not determine your location. Please enable location services.');
    } finally {
      setLoading(false);
    }
  };

  const loadNearbySites = async (userCoords: { lat: number; lon: number }) => {
    try {
      const [wonders, pillars] = await Promise.all([
        getWonders(),
        getPillars(),
      ]);

      // Combine all sites
      const allSites = [
        ...wonders.map((w: Wonder) => ({
          id: w.wonder_id,
          name: w.name,
          type: 'wonder' as const,
          coordinates: w.coordinates,
          resonance: w.field_resonance,
        })),
        ...pillars.map((p: Pillar) => ({
          id: p.pillar_id,
          name: p.name,
          type: 'pillar' as const,
          coordinates: p.coordinates,
          resonance: p.field_resonance,
        })),
      ];

      // Find nearby sites
      const nearby = findNearbySites(
        userCoords.lat,
        userCoords.lon,
        allSites,
        radius
      );

      setNearbySites(nearby);
    } catch (error) {
      console.error('Error loading nearby sites:', error);
      Alert.alert('Error', 'Failed to load heritage sites');
    }
  };

  const onRefresh = async () => {
    setRefreshing(true);
    if (userLocation) {
      await loadNearbySites(userLocation);
    } else {
      await requestLocationAndLoad();
    }
    setRefreshing(false);
  };

  const renderSite = ({ item }: { item: NearbySite }) => (
    <TouchableOpacity
      style={styles.card}
      onPress={() => {
        Alert.alert(
          item.name,
          `${item.type === 'wonder' ? 'Wonder' : 'Pillar'}\n` +
          `Distance: ${formatDistance(item.distance)}\n` +
          `Direction: ${getDirectionName(item.bearing)}\n` +
          `Resonance: ${(item.resonance * 100).toFixed(0)}%`
        );
      }}
    >
      <View style={styles.cardHeader}>
        <Text style={styles.cardTitle}>{item.name}</Text>
        <View style={styles.typeBadge}>
          <Text style={styles.typeText}>
            {item.type === 'wonder' ? 'Wonder' : 'Pillar'}
          </Text>
        </View>
      </View>
      <View style={styles.cardDetails}>
        <View style={styles.detailRow}>
          <Text style={styles.detailLabel}>Distance:</Text>
          <Text style={styles.detailValue}>{formatDistance(item.distance)}</Text>
        </View>
        <View style={styles.detailRow}>
          <Text style={styles.detailLabel}>Direction:</Text>
          <Text style={styles.detailValue}>{getDirectionName(item.bearing)}</Text>
        </View>
        <View style={styles.detailRow}>
          <Text style={styles.detailLabel}>Resonance:</Text>
          <Text style={[styles.detailValue, styles.resonanceValue]}>
            {(item.resonance * 100).toFixed(0)}%
          </Text>
        </View>
      </View>
    </TouchableOpacity>
  );

  if (loading) {
    return (
      <View style={styles.center}>
        <ActivityIndicator size="large" color="#e94560" />
        <Text style={styles.loadingText}>Finding nearby heritage sites...</Text>
        {locationError && (
          <Text style={styles.errorText}>{locationError}</Text>
        )}
      </View>
    );
  }

  if (locationError) {
    return (
      <View style={styles.center}>
        <Text style={styles.errorText}>{locationError}</Text>
        <TouchableOpacity
          style={styles.retryButton}
          onPress={requestLocationAndLoad}
        >
          <Text style={styles.retryButtonText}>Retry</Text>
        </TouchableOpacity>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Nearby Heritage Sites</Text>
        {userLocation && (
          <Text style={styles.headerSubtitle}>
            Within {radius}km of your location
          </Text>
        )}
      </View>

      {/* Radius Selector */}
      <View style={styles.radiusContainer}>
        <Text style={styles.radiusLabel}>Search Radius:</Text>
        <View style={styles.radiusButtons}>
          {[50, 100, 200, 500].map((r) => (
            <TouchableOpacity
              key={r}
              style={[styles.radiusButton, radius === r && styles.radiusButtonActive]}
              onPress={() => {
                setRadius(r);
                if (userLocation) {
                  loadNearbySites(userLocation);
                }
              }}
            >
              <Text style={[styles.radiusButtonText, radius === r && styles.radiusButtonTextActive]}>
                {r}km
              </Text>
            </TouchableOpacity>
          ))}
        </View>
      </View>

      {/* List */}
      <FlatList
        data={nearbySites}
        renderItem={renderSite}
        keyExtractor={(item) => item.id}
        contentContainerStyle={styles.list}
        refreshControl={
          <RefreshControl
            refreshing={refreshing}
            onRefresh={onRefresh}
            tintColor="#e94560"
          />
        }
        ListEmptyComponent={
          <View style={styles.emptyContainer}>
            <Text style={styles.emptyText}>No heritage sites found within {radius}km</Text>
            <Text style={styles.emptySubtext}>
              Try increasing the search radius
            </Text>
          </View>
        }
      />
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
    padding: 32,
  },
  loadingText: {
    color: '#8b8b9e',
    marginTop: 16,
    fontSize: 16,
  },
  errorText: {
    color: '#ef4444',
    marginTop: 16,
    fontSize: 16,
    textAlign: 'center',
  },
  retryButton: {
    marginTop: 24,
    paddingHorizontal: 24,
    paddingVertical: 12,
    backgroundColor: '#e94560',
    borderRadius: 8,
  },
  retryButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  header: {
    padding: 20,
    backgroundColor: '#1a1a2e',
    borderBottomWidth: 1,
    borderBottomColor: '#16213e',
  },
  headerTitle: {
    color: '#fff',
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  headerSubtitle: {
    color: '#8b8b9e',
    fontSize: 14,
  },
  radiusContainer: {
    padding: 16,
    backgroundColor: '#1a1a2e',
    borderBottomWidth: 1,
    borderBottomColor: '#16213e',
  },
  radiusLabel: {
    color: '#8b8b9e',
    fontSize: 14,
    marginBottom: 12,
  },
  radiusButtons: {
    flexDirection: 'row',
    gap: 8,
  },
  radiusButton: {
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 6,
    backgroundColor: '#16213e',
  },
  radiusButtonActive: {
    backgroundColor: '#e94560',
  },
  radiusButtonText: {
    color: '#8b8b9e',
    fontSize: 14,
    fontWeight: '500',
  },
  radiusButtonTextActive: {
    color: '#fff',
    fontWeight: 'bold',
  },
  list: {
    padding: 16,
  },
  card: {
    backgroundColor: '#1a1a2e',
    borderRadius: 12,
    padding: 16,
    marginBottom: 12,
    borderWidth: 1,
    borderColor: '#16213e',
  },
  cardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  cardTitle: {
    color: '#fff',
    fontSize: 20,
    fontWeight: 'bold',
    flex: 1,
  },
  typeBadge: {
    paddingHorizontal: 12,
    paddingVertical: 4,
    borderRadius: 6,
    backgroundColor: '#16213e',
  },
  typeText: {
    color: '#e94560',
    fontSize: 12,
    fontWeight: '600',
    textTransform: 'uppercase',
  },
  cardDetails: {
    gap: 8,
  },
  detailRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  detailLabel: {
    color: '#8b8b9e',
    fontSize: 14,
  },
  detailValue: {
    color: '#fff',
    fontSize: 14,
    fontWeight: '600',
  },
  resonanceValue: {
    color: '#e94560',
  },
  emptyContainer: {
    padding: 32,
    alignItems: 'center',
  },
  emptyText: {
    color: '#8b8b9e',
    fontSize: 16,
    marginBottom: 8,
  },
  emptySubtext: {
    color: '#8b8b9e',
    fontSize: 14,
    fontStyle: 'italic',
  },
});
