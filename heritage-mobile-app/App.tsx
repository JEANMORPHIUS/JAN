/**
 * JAN Ecosystem Mobile App
 * Main App Entry Point
 * 
 * Mission: THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
 */

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { StatusBar } from 'expo-status-bar';

// Screens (to be created)
import HeritageScreen from './src/screens/HeritageScreen';
import EntitiesScreen from './src/screens/EntitiesScreen';
import ProjectsScreen from './src/screens/ProjectsScreen';
import ChannelsScreen from './src/screens/ChannelsScreen';
import SystemsScreen from './src/screens/SystemsScreen';

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <StatusBar style="auto" />
      <Tab.Navigator
        screenOptions={{
          headerStyle: {
            backgroundColor: '#1a1a2e',
          },
          headerTintColor: '#fff',
          headerTitleStyle: {
            fontWeight: 'bold',
          },
          tabBarStyle: {
            backgroundColor: '#1a1a2e',
            borderTopColor: '#16213e',
          },
          tabBarActiveTintColor: '#e94560',
          tabBarInactiveTintColor: '#8b8b9e',
        }}
      >
        <Tab.Screen 
          name="Heritage" 
          component={HeritageScreen}
          options={{
            title: 'Heritage & Wonders',
            tabBarLabel: 'Heritage',
          }}
        />
        <Tab.Screen 
          name="Entities" 
          component={EntitiesScreen}
          options={{
            title: 'Entities',
            tabBarLabel: 'Entities',
          }}
        />
        <Tab.Screen 
          name="Projects" 
          component={ProjectsScreen}
          options={{
            title: 'Projects',
            tabBarLabel: 'Projects',
          }}
        />
        <Tab.Screen 
          name="Channels" 
          component={ChannelsScreen}
          options={{
            title: 'Channels',
            tabBarLabel: 'Channels',
          }}
        />
        <Tab.Screen 
          name="Systems" 
          component={SystemsScreen}
          options={{
            title: 'Systems',
            tabBarLabel: 'Systems',
          }}
        />
      </Tab.Navigator>
    </NavigationContainer>
  );
}
