/**
 * Heritage Screen
 * 7 Wonders, Seven Pillars, and Heritage Meridian System
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  FlatList,
  TouchableOpacity,
  ActivityIndicator,
  Alert,
  Button,
  RefreshControl,
} from 'react-native';
import { useNavigation } from '@react-navigation/native';
import type { NativeStackNavigationProp } from '@react-navigation/native-stack';
import { getWonders } from '../api/wonders';
import { getPillars } from '../api/heritage';
import type { Wonder } from '../api/wonders';
import PillarsScreen from './PillarsScreen';
import { loadWonders, saveWonders, getSyncStatus, isDataStale } from '../utils/offlineStorage';
import NetInfo from '@react-native-community/netinfo';

export default function HeritageScreen() {
  const navigation = useNavigation();
  const [wonders, setWonders] = useState<Wonder[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'wonders' | 'pillars'>('wonders');
  const [isOffline, setIsOffline] = useState(false);
  const [syncStatus, setSyncStatus] = useState<any>(null);
  const [refreshing, setRefreshing] = useState(false);

  useEffect(() => {
    checkNetworkAndLoad();
  }, [activeTab]);

  const checkNetworkAndLoad = async () => {
    const netInfo = await NetInfo.fetch();
    setIsOffline(!netInfo.isConnected);

    if (activeTab === 'wonders') {
      await loadWondersData();
    }
  };

  const loadWondersData = async () => {
    try {
      setLoading(true);
      
      // Try to load from offline storage first
      const offlineData = await loadWonders();
      if (offlineData && offlineData.length > 0) {
        setWonders(offlineData);
        setSyncStatus(await getSyncStatus());
      }

      // Try to fetch from API if online
      const netInfo = await NetInfo.fetch();
      if (netInfo.isConnected) {
        try {
          const data = await getWonders();
          setWonders(data);
          await saveWonders(data); // Cache for offline
          setSyncStatus(await getSyncStatus());
        } catch (apiError) {
          console.error('API error, using offline data:', apiError);
          // Keep offline data if API fails
        }
      }
    } catch (error) {
      console.error('Error loading wonders:', error);
      if (wonders.length === 0) {
        Alert.alert('Error', 'Failed to load wonders. Please check your connection.');
      }
    } finally {
      setLoading(false);
    }
  };

  const handleRefresh = async () => {
    setRefreshing(true);
    await loadWondersData();
    setRefreshing(false);
  };

  const renderWonder = ({ item }: { item: Wonder }) => (
    <TouchableOpacity
      style={styles.card}
      onPress={() => {
        navigation.navigate('WonderDetail' as never, {
          wonderId: item.wonder_id,
          wonder: item, // Pre-load data for faster display
        } as never);
      }}
    >
      <Text style={styles.cardTitle}>{item.name}</Text>
      <Text style={styles.cardLocation}>{item.location}</Text>
      <View style={styles.cardFooter}>
        <Text style={styles.resonance}>
          Resonance: {(item.field_resonance * 100).toFixed(0)}%
        </Text>
        <Text style={styles.type}>{item.wonder_type}</Text>
      </View>
    </TouchableOpacity>
  );

  if (loading) {
    return (
      <View style={styles.center}>
        <ActivityIndicator size="large" color="#e94560" />
        <Text style={styles.loadingText}>Loading heritage data...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      {/* Offline Indicator */}
      {isOffline && (
        <View style={styles.offlineBanner}>
          <Text style={styles.offlineText}>📡 Offline Mode - Showing cached data</Text>
        </View>
      )}
      {/* Tab Switcher */}
      <View style={styles.tabContainer}>
        <TouchableOpacity
          style={[styles.tab, activeTab === 'wonders' && styles.activeTab]}
          onPress={() => setActiveTab('wonders')}
        >
          <Text style={[styles.tabText, activeTab === 'wonders' && styles.activeTabText]}>
            7 Wonders
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.tab, activeTab === 'pillars' && styles.activeTab]}
          onPress={() => setActiveTab('pillars')}
        >
          <Text style={[styles.tabText, activeTab === 'pillars' && styles.activeTabText]}>
            Seven Pillars
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={styles.mapButton}
          onPress={() => navigation.navigate('HeritageMap' as never)}
        >
          <Text style={styles.mapButtonText}>🗺️ Map</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={styles.mapButton}
          onPress={() => navigation.navigate('NearbySites' as never)}
        >
          <Text style={styles.mapButtonText}>📍 Nearby</Text>
        </TouchableOpacity>
      </View>

      {/* Content */}
      {activeTab === 'wonders' ? (
        <FlatList
          data={wonders}
          renderItem={renderWonder}
          keyExtractor={(item) => item.wonder_id}
          contentContainerStyle={styles.list}
          refreshControl={
            <RefreshControl
              refreshing={refreshing}
              onRefresh={handleRefresh}
              tintColor="#e94560"
            />
          }
          ListEmptyComponent={
            <View style={styles.center}>
              <Text style={styles.emptyText}>No wonders found</Text>
            </View>
          }
        />
      ) : (
        <PillarsScreen />
      )}
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
  tabContainer: {
    flexDirection: 'row',
    backgroundColor: '#1a1a2e',
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderBottomWidth: 1,
    borderBottomColor: '#16213e',
    alignItems: 'center',
  },
  tab: {
    flex: 1,
    paddingVertical: 12,
    alignItems: 'center',
    borderRadius: 8,
    marginHorizontal: 4,
  },
  activeTab: {
    backgroundColor: '#16213e',
  },
  tabText: {
    color: '#8b8b9e',
    fontSize: 16,
    fontWeight: '500',
  },
  activeTabText: {
    color: '#e94560',
    fontWeight: 'bold',
  },
  mapButton: {
    marginLeft: 8,
    paddingHorizontal: 12,
    paddingVertical: 8,
    backgroundColor: '#16213e',
    borderRadius: 6,
  },
  mapButtonText: {
    color: '#fff',
    fontSize: 14,
    fontWeight: '600',
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
  cardTitle: {
    color: '#fff',
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  cardLocation: {
    color: '#8b8b9e',
    fontSize: 14,
    marginBottom: 12,
  },
  cardFooter: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  resonance: {
    color: '#e94560',
    fontSize: 14,
    fontWeight: '600',
  },
  type: {
    color: '#8b8b9e',
    fontSize: 12,
    textTransform: 'uppercase',
  },
  emptyText: {
    color: '#8b8b9e',
    fontSize: 16,
  },
  comingSoon: {
    color: '#8b8b9e',
    fontSize: 16,
    fontStyle: 'italic',
  },
  offlineBanner: {
    backgroundColor: '#f59e0b',
    padding: 8,
    alignItems: 'center',
  },
  offlineText: {
    color: '#fff',
    fontSize: 14,
    fontWeight: '600',
  },
});
