/**
 * Entities Screen
 * 11 Entities: 5 Creative Personas + 4 Business Projects + 2 Governance
 */

import React from 'react';
import {
  View,
  Text,
  StyleSheet,
} from 'react-native';

export default function EntitiesScreen() {
  return (
    <View style={styles.container}>
      <View style={styles.center}>
        <Text style={styles.title}>Entities</Text>
        <Text style={styles.subtitle}>11 Entities</Text>
        <Text style={styles.comingSoon}>Coming soon...</Text>
        <Text style={styles.description}>
          5 Creative Personas{'\n'}
          4 Business Projects{'\n'}
          2 Governance
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
