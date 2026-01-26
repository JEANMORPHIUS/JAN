/** * * Seven Pillars Screen
 *  * Display all Seven Pillars with network health
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
} from 'react-native';
import { getPillars, getNetworkHealth } from '../api/heritage';
import type { Pillar } from '../api/heritage';

export default function PillarsScreen() {
  const [pillars, setPillars] = useState<Pillar[]>([]);
  const [networkHealth, setNetworkHealth] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      setLoading(true);
      const [pillarsData, healthData] = await Promise.all([
        getPillars(),
        getNetworkHealth(),
      ]);
      setPillars(pillarsData);
      setNetworkHealth(healthData);
    } catch (error) {
      console.error('Error loading pillars:', error);
      Alert.alert('Error', 'Failed to load pillars data. Please check your connection.');
    } finally {
      setLoading(false);
    }
  };

  const getHealthColor = (health: string) => {
    switch (health) {
      case 'excellent':
        return '#4ade80';
      case 'good':
        return '#fbbf24';
      case 'moderate':
        return '#f59e0b';
      default:
        return '#ef4444';
    }
  };

  const renderNetworkHealth = () => {
    if (!networkHealth) return null;

    return (
      <View style={styles.healthCard}>
        <Text style={styles.healthTitle}>Network Health</Text>
        <View style={styles.healthRow}>
          <View style={styles.healthIndicator}>
            <View
              style={[
                styles.healthDot,
                { backgroundColor: getHealthColor(networkHealth.health) },
              ]}
            />
            <Text style={styles.healthStatus}>
              {networkHealth.health.toUpperCase()}
            </Text>
          </View>
          <View style={styles.healthStats}>
            <Text style={styles.healthLabel}>Average Resonance:</Text>
            <Text style={styles.healthValue}>
              {(networkHealth.average_resonance * 100).toFixed(0)}%
            </Text>
          </View>
        </View>
        <Text style={styles.healthNodes}>
          {networkHealth.total_nodes} nodes active
        </Text>
      </View>
    );
  };

  const renderPillar = ({ item }: { item: Pillar }) => (
    <TouchableOpacity
      style={styles.card}
      onPress={() => {
        Alert.alert(
          item.name,
          `Ancient Name: ${item.ancient_name}\n\n${item.spiritual_significance}`
        );
      }}
    >
      <View style={styles.cardHeader}>
        <Text style={styles.cardTitle}>{item.name}</Text>
        <Text style={styles.ancientName}>{item.ancient_name}</Text>
      </View>
      <Text style={styles.cardLocation}>{item.country}</Text>
      <View style={styles.cardFooter}>
        <View style={styles.resonanceContainer}>
          <View style={styles.resonanceBar}>
            <View
              style={[
                styles.resonanceFill,
                {
                  width: `${(item.field_resonance * 100).toFixed(0)}%`,
                  backgroundColor: item.field_resonance >= 0.9 ? '#4ade80' : '#e94560',
                },
              ]}
            />
          </View>
          <Text style={styles.resonance}>
            {(item.field_resonance * 100).toFixed(0)}%
          </Text>
        </View>
      </View>
    </TouchableOpacity>
  );

  if (loading) {
    return (
      <View style={styles.center}>
        <ActivityIndicator size="large" color="#e94560" />
        <Text style={styles.loadingText}>Loading pillars...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      {renderNetworkHealth()}
      <FlatList
        data={pillars}
        renderItem={renderPillar}
        keyExtractor={(item) => item.pillar_id}
        contentContainerStyle={styles.list}
        ListEmptyComponent={
          <View style={styles.center}>
            <Text style={styles.emptyText}>No pillars found</Text>
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
  },
  loadingText: {
    color: '#8b8b9e',
    marginTop: 16,
    fontSize: 16,
  },
  healthCard: {
    backgroundColor: '#1a1a2e',
    margin: 16,
    padding: 16,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#16213e',
  },
  healthTitle: {
    color: '#fff',
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 12,
  },
  healthRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  healthIndicator: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  healthDot: {
    width: 12,
    height: 12,
    borderRadius: 6,
    marginRight: 8,
  },
  healthStatus: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  healthStats: {
    alignItems: 'flex-end',
  },
  healthLabel: {
    color: '#8b8b9e',
    fontSize: 14,
  },
  healthValue: {
    color: '#e94560',
    fontSize: 18,
    fontWeight: 'bold',
  },
  healthNodes: {
    color: '#8b8b9e',
    fontSize: 14,
    marginTop: 4,
  },
  list: {
    padding: 16,
    paddingTop: 0,
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
    marginBottom: 8,
  },
  cardTitle: {
    color: '#fff',
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  ancientName: {
    color: '#e94560',
    fontSize: 14,
    fontStyle: 'italic',
  },
  cardLocation: {
    color: '#8b8b9e',
    fontSize: 14,
    marginBottom: 12,
  },
  cardFooter: {
    marginTop: 8,
  },
  resonanceContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  resonanceBar: {
    flex: 1,
    height: 6,
    backgroundColor: '#16213e',
    borderRadius: 3,
    overflow: 'hidden',
    marginRight: 12,
  },
  resonanceFill: {
    height: '100%',
    borderRadius: 3,
  },
  resonance: {
    color: '#e94560',
    fontSize: 14,
    fontWeight: '600',
    minWidth: 50,
    textAlign: 'right',
  },
  emptyText: {
    color: '#8b8b9e',
    fontSize: 16,
  },
});
