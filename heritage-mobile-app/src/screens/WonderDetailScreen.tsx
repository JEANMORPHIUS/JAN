/**
 * Wonder Detail Screen
 * Full information, Shell vs Seed analysis, Meridian connections
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  ActivityIndicator,
  TouchableOpacity,
  Alert,
  Share,
  Linking,
} from 'react-native';
import { useRoute, useNavigation } from '@react-navigation/native';
import { getWonder, getWonderConnections } from '../api/wonders';
import type { Wonder } from '../api/wonders';

interface RouteParams {
  wonderId: string;
  wonder?: Wonder; // Optional pre-loaded wonder data
}

export default function WonderDetailScreen() {
  const route = useRoute();
  const navigation = useNavigation();
  const { wonderId, wonder: preloadedWonder } = route.params as RouteParams;

  const [wonder, setWonder] = useState<Wonder | null>(preloadedWonder || null);
  const [connections, setConnections] = useState<string[]>([]);
  const [loading, setLoading] = useState(!preloadedWonder);
  const [activeTab, setActiveTab] = useState<'overview' | 'shell' | 'seed' | 'connections'>('overview');

  useEffect(() => {
    loadWonderData();
  }, [wonderId]);

  const loadWonderData = async () => {
    try {
      setLoading(true);
      const wonderData = await getWonder(wonderId);
      setWonder(wonderData);

      const connectionsData = await getWonderConnections(wonderId);
      setConnections(connectionsData);
    } catch (error) {
      console.error('Error loading wonder:', error);
      Alert.alert('Error', 'Failed to load wonder details');
    } finally {
      setLoading(false);
    }
  };

  if (loading || !wonder) {
    return (
      <View style={styles.center}>
        <ActivityIndicator size="large" color="#e94560" />
        <Text style={styles.loadingText}>Loading wonder details...</Text>
      </View>
    );
  }

  const renderResonanceBar = (resonance: number) => {
    const percentage = Math.round(resonance * 100);
    const color = resonance >= 0.9 ? '#4ade80' : resonance >= 0.7 ? '#fbbf24' : '#ef4444';
    
    return (
      <View style={styles.resonanceContainer}>
        <View style={styles.resonanceBar}>
          <View style={[styles.resonanceFill, { width: `${percentage}%`, backgroundColor: color }]} />
        </View>
        <Text style={styles.resonanceText}>{percentage}% Field Resonance</Text>
      </View>
    );
  };

  const renderOverview = () => (
    <View style={styles.section}>
      <Text style={styles.sectionTitle}>Overview</Text>
      <View style={styles.infoRow}>
        <Text style={styles.infoLabel}>Location:</Text>
        <Text style={styles.infoValue}>{wonder.location}</Text>
      </View>
      <View style={styles.infoRow}>
        <Text style={styles.infoLabel}>Coordinates:</Text>
        <Text style={styles.infoValue}>
          {wonder.coordinates.lat.toFixed(4)}, {wonder.coordinates.lon.toFixed(4)}
        </Text>
      </View>
      <View style={styles.infoRow}>
        <Text style={styles.infoLabel}>Type:</Text>
        <Text style={styles.infoValue}>{wonder.wonder_type}</Text>
      </View>
      <View style={styles.infoRow}>
        <Text style={styles.infoLabel}>Time Period:</Text>
        <Text style={styles.infoValue}>{wonder.time_period}</Text>
      </View>
      <View style={styles.infoRow}>
        <Text style={styles.infoLabel}>Year Built:</Text>
        <Text style={styles.infoValue}>{wonder.year_built}</Text>
      </View>
      {renderResonanceBar(wonder.field_resonance)}
      <View style={styles.spiritualSection}>
        <Text style={styles.spiritualTitle}>Spiritual Significance</Text>
        <Text style={styles.spiritualText}>{wonder.spiritual_significance}</Text>
      </View>
      <View style={styles.culturalSection}>
        <Text style={styles.culturalTitle}>Cultural Heritage</Text>
        <Text style={styles.culturalText}>{wonder.cultural_heritage}</Text>
      </View>
    </View>
  );

  const renderShell = () => (
    <View style={styles.section}>
      <Text style={styles.sectionTitle}>The Shell</Text>
      <Text style={styles.shellLabel}>Modern Distortion</Text>
      <Text style={styles.shellText}>{wonder.modern_distortion}</Text>
      <View style={styles.separator} />
      <Text style={styles.shellNote}>
        The Shell represents how this site is perceived in modern narratives, 
        often disconnected from its original purpose.
      </Text>
    </View>
  );

  const renderSeed = () => (
    <View style={styles.section}>
      <Text style={styles.sectionTitle}>The Seed</Text>
      <Text style={styles.seedLabel}>Original Function</Text>
      <Text style={styles.seedText}>{wonder.original_function}</Text>
      <View style={styles.separator} />
      <Text style={styles.seedNote}>
        The Seed represents the true purpose and function of this site, 
        aligned with its original design and spiritual significance.
      </Text>
    </View>
  );

  const renderConnections = () => (
    <View style={styles.section}>
      <Text style={styles.sectionTitle}>Meridian Connections</Text>
      {connections.length > 0 ? (
        <>
          <Text style={styles.connectionsDescription}>
            This wonder is connected to {connections.length} meridian{connections.length !== 1 ? 's' : ''}:
          </Text>
          {connections.map((connection, index) => (
            <View key={index} style={styles.connectionItem}>
              <Text style={styles.connectionBullet}>•</Text>
              <Text style={styles.connectionText}>{connection}</Text>
            </View>
          ))}
        </>
      ) : (
        <Text style={styles.noConnections}>
          No meridian connections recorded for this wonder.
        </Text>
      )}
      {wonder.heritage_meridian_connection && (
        <View style={styles.meridianSection}>
          <Text style={styles.meridianTitle}>Heritage Meridian Connection</Text>
          <Text style={styles.meridianText}>{wonder.heritage_meridian_connection}</Text>
        </View>
      )}
    </View>
  );

  return (
    <View style={styles.container}>
      <ScrollView style={styles.scrollView} contentContainerStyle={styles.content}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>{wonder.name}</Text>
          {renderResonanceBar(wonder.field_resonance)}
        </View>

        {/* Tab Navigation */}
        <View style={styles.tabContainer}>
          <TouchableOpacity
            style={[styles.tab, activeTab === 'overview' && styles.activeTab]}
            onPress={() => setActiveTab('overview')}
          >
            <Text style={[styles.tabText, activeTab === 'overview' && styles.activeTabText]}>
              Overview
            </Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={[styles.tab, activeTab === 'shell' && styles.activeTab]}
            onPress={() => setActiveTab('shell')}
          >
            <Text style={[styles.tabText, activeTab === 'shell' && styles.activeTabText]}>
              Shell
            </Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={[styles.tab, activeTab === 'seed' && styles.activeTab]}
            onPress={() => setActiveTab('seed')}
          >
            <Text style={[styles.tabText, activeTab === 'seed' && styles.activeTabText]}>
              Seed
            </Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={[styles.tab, activeTab === 'connections' && styles.activeTab]}
            onPress={() => setActiveTab('connections')}
          >
            <Text style={[styles.tabText, activeTab === 'connections' && styles.activeTabText]}>
              Connections
            </Text>
          </TouchableOpacity>
        </View>

        {/* Content */}
        {activeTab === 'overview' && renderOverview()}
        {activeTab === 'shell' && renderShell()}
        {activeTab === 'seed' && renderSeed()}
        {activeTab === 'connections' && renderConnections()}

        {/* Action Buttons */}
        <View style={styles.actionsContainer}>
          <TouchableOpacity
            style={styles.actionButton}
            onPress={handleShare}
          >
            <Text style={styles.actionButtonText}>Share</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={[styles.actionButton, styles.actionButtonPrimary]}
            onPress={handleDirections}
          >
            <Text style={styles.actionButtonText}>Get Directions</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    </View>
  );

  const handleShare = async () => {
    try {
      await Share.share({
        message: `${wonder.name}\n\n${wonder.location}\n\nField Resonance: ${(wonder.field_resonance * 100).toFixed(0)}%\n\n${wonder.spiritual_significance}`,
        title: wonder.name,
      });
    } catch (error) {
      console.error('Error sharing:', error);
    }
  };

  const handleDirections = () => {
    const url = `https://www.google.com/maps/dir/?api=1&destination=${wonder.coordinates.lat},${wonder.coordinates.lon}`;
    Linking.openURL(url).catch((err) => {
      console.error('Error opening directions:', err);
      Alert.alert('Error', 'Could not open directions');
    });
  };
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
  scrollView: {
    flex: 1,
  },
  content: {
    paddingBottom: 32,
  },
  header: {
    padding: 20,
    backgroundColor: '#1a1a2e',
    borderBottomWidth: 1,
    borderBottomColor: '#16213e',
  },
  title: {
    color: '#fff',
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 16,
  },
  resonanceContainer: {
    marginTop: 8,
  },
  resonanceBar: {
    height: 8,
    backgroundColor: '#16213e',
    borderRadius: 4,
    overflow: 'hidden',
    marginBottom: 8,
  },
  resonanceFill: {
    height: '100%',
    borderRadius: 4,
  },
  resonanceText: {
    color: '#8b8b9e',
    fontSize: 14,
    fontWeight: '600',
  },
  tabContainer: {
    flexDirection: 'row',
    backgroundColor: '#1a1a2e',
    paddingHorizontal: 8,
    paddingVertical: 8,
    borderBottomWidth: 1,
    borderBottomColor: '#16213e',
  },
  tab: {
    flex: 1,
    paddingVertical: 10,
    alignItems: 'center',
    borderRadius: 6,
    marginHorizontal: 4,
  },
  activeTab: {
    backgroundColor: '#16213e',
  },
  tabText: {
    color: '#8b8b9e',
    fontSize: 14,
    fontWeight: '500',
  },
  activeTabText: {
    color: '#e94560',
    fontWeight: 'bold',
  },
  section: {
    padding: 20,
  },
  sectionTitle: {
    color: '#fff',
    fontSize: 22,
    fontWeight: 'bold',
    marginBottom: 16,
  },
  infoRow: {
    flexDirection: 'row',
    marginBottom: 12,
    flexWrap: 'wrap',
  },
  infoLabel: {
    color: '#8b8b9e',
    fontSize: 16,
    fontWeight: '600',
    width: 120,
  },
  infoValue: {
    color: '#fff',
    fontSize: 16,
    flex: 1,
  },
  spiritualSection: {
    marginTop: 24,
    padding: 16,
    backgroundColor: '#16213e',
    borderRadius: 8,
  },
  spiritualTitle: {
    color: '#e94560',
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  spiritualText: {
    color: '#fff',
    fontSize: 15,
    lineHeight: 24,
  },
  culturalSection: {
    marginTop: 16,
    padding: 16,
    backgroundColor: '#16213e',
    borderRadius: 8,
  },
  culturalTitle: {
    color: '#fbbf24',
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  culturalText: {
    color: '#fff',
    fontSize: 15,
    lineHeight: 24,
  },
  shellLabel: {
    color: '#ef4444',
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 12,
  },
  shellText: {
    color: '#fff',
    fontSize: 16,
    lineHeight: 24,
    marginBottom: 16,
  },
  shellNote: {
    color: '#8b8b9e',
    fontSize: 14,
    fontStyle: 'italic',
    lineHeight: 20,
  },
  seedLabel: {
    color: '#4ade80',
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 12,
  },
  seedText: {
    color: '#fff',
    fontSize: 16,
    lineHeight: 24,
    marginBottom: 16,
  },
  seedNote: {
    color: '#8b8b9e',
    fontSize: 14,
    fontStyle: 'italic',
    lineHeight: 20,
  },
  separator: {
    height: 1,
    backgroundColor: '#16213e',
    marginVertical: 16,
  },
  connectionsDescription: {
    color: '#8b8b9e',
    fontSize: 16,
    marginBottom: 16,
    lineHeight: 24,
  },
  connectionItem: {
    flexDirection: 'row',
    marginBottom: 12,
    alignItems: 'flex-start',
  },
  connectionBullet: {
    color: '#e94560',
    fontSize: 20,
    marginRight: 12,
    marginTop: 2,
  },
  connectionText: {
    color: '#fff',
    fontSize: 16,
    flex: 1,
    lineHeight: 24,
  },
  noConnections: {
    color: '#8b8b9e',
    fontSize: 16,
    fontStyle: 'italic',
    textAlign: 'center',
    marginTop: 32,
  },
  meridianSection: {
    marginTop: 24,
    padding: 16,
    backgroundColor: '#16213e',
    borderRadius: 8,
  },
  meridianTitle: {
    color: '#e94560',
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  meridianText: {
    color: '#fff',
    fontSize: 15,
    lineHeight: 24,
  },
  actionsContainer: {
    flexDirection: 'row',
    padding: 20,
    gap: 12,
    backgroundColor: '#1a1a2e',
    borderTopWidth: 1,
    borderTopColor: '#16213e',
  },
  actionButton: {
    flex: 1,
    paddingVertical: 14,
    borderRadius: 8,
    backgroundColor: '#16213e',
    alignItems: 'center',
  },
  actionButtonPrimary: {
    backgroundColor: '#e94560',
  },
  actionButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
});
