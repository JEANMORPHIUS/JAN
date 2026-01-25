/**
 * Systems Screen
 * 13 Core Systems
 */

import React from 'react';
import {
  View,
  Text,
  StyleSheet,
} from 'react-native';

export default function SystemsScreen() {
  return (
    <View style={styles.container}>
      <View style={styles.center}>
        <Text style={styles.title}>Systems</Text>
        <Text style={styles.subtitle}>13 Core Systems</Text>
        <Text style={styles.comingSoon}>Coming soon...</Text>
        <Text style={styles.description}>
          World History{'\n'}
          Frequential Events{'\n'}
          Deep Search (23 domains){'\n'}
          Nourishment Hive{'\n'}
          Seed to Movement{'\n'}
          Spiritual Contracts{'\n'}
          Historical Aligned{'\n'}
          Industries{'\n'}
          SIYEM Integration{'\n'}
          Banking & Finance{'\n'}
          Financial Controls{'\n'}
          Aligned Investments{'\n'}
          Free Will
        </Text>
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
    padding: 32,
  },
  title: {
    color: '#fff',
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  subtitle: {
    color: '#e94560',
    fontSize: 18,
    marginBottom: 24,
  },
  comingSoon: {
    color: '#8b8b9e',
    fontSize: 16,
    fontStyle: 'italic',
    marginBottom: 16,
  },
  description: {
    color: '#8b8b9e',
    fontSize: 14,
    textAlign: 'center',
    lineHeight: 24,
  },
});
