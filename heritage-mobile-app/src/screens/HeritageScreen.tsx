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
} from 'react-native';
import { useNavigation } from '@react-navigation/native';
import { getWonders } from '../api/wonders';
import { getPillars } from '../api/heritage';
import type { Wonder } from '../api/wonders';

export default function HeritageScreen() {
  const navigation = useNavigation();
  const [wonders, setWonders] = useState<Wonder[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'wonders' | 'pillars'>('wonders');

  useEffect(() => {
    loadData();
  }, [activeTab]);

  const loadData = async () => {
    try {
      setLoading(true);
      if (activeTab === 'wonders') {
        const data = await getWonders();
        setWonders(data);
      } else {
        // Load pillars
        const data = await getPillars();
        // TODO: Set pillars state when interface is defined
      }
    } catch (error) {
      console.error('Error loading heritage data:', error);
      Alert.alert('Error', 'Failed to load heritage data. Please check your connection.');
    } finally {
      setLoading(false);
    }
  };

  const renderWonder = ({ item }: { item: Wonder }) => (
    <TouchableOpacity
      style={styles.card}
      onPress={() => {
        // TODO: Navigate to wonder detail screen
        Alert.alert(item.name, `Field Resonance: ${item.field_resonance}`);
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
      </View>

      {/* Content */}
      {activeTab === 'wonders' ? (
        <FlatList
          data={wonders}
          renderItem={renderWonder}
          keyExtractor={(item) => item.wonder_id}
          contentContainerStyle={styles.list}
          ListEmptyComponent={
            <View style={styles.center}>
              <Text style={styles.emptyText}>No wonders found</Text>
            </View>
          }
        />
      ) : (
        <View style={styles.center}>
          <Text style={styles.comingSoon}>Seven Pillars view coming soon</Text>
        </View>
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
});
