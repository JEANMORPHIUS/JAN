/** * * Resonance Bar Component
 *  * Visual field resonance indicator
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

import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

interface ResonanceBarProps {
  resonance: number;
  showLabel?: boolean;
  height?: number;
}

export default function ResonanceBar({
  resonance,
  showLabel = true,
  height = 8,
}: ResonanceBarProps) {
  const percentage = Math.round(resonance * 100);
  
  const getColor = () => {
    if (resonance >= 0.9) return '#4ade80'; // Green
    if (resonance >= 0.7) return '#fbbf24'; // Yellow
    return '#e94560'; // Red
  };

  return (
    <View style={styles.container}>
      <View style={[styles.bar, { height }]}>
        <View
          style={[
            styles.fill,
            {
              width: `${percentage}%`,
              backgroundColor: getColor(),
              height,
            },
          ]}
        />
      </View>
      {showLabel && (
        <Text style={styles.label}>{percentage}%</Text>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  bar: {
    flex: 1,
    backgroundColor: '#16213e',
    borderRadius: 4,
    overflow: 'hidden',
  },
  fill: {
    borderRadius: 4,
  },
  label: {
    color: '#8b8b9e',
    fontSize: 14,
    fontWeight: '600',
    minWidth: 45,
    textAlign: 'right',
  },
});
