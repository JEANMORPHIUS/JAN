/**
 * JAN Ecosystem Mobile App
 * Main App Entry Point
 * 
 * Mission: THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
 */

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { StatusBar } from 'expo-status-bar';

// Screens
import HeritageScreen from './src/screens/HeritageScreen';
import WonderDetailScreen from './src/screens/WonderDetailScreen';
import HeritageMapScreen from './src/screens/HeritageMapScreen';
import NearbySitesScreen from './src/screens/NearbySitesScreen';
import EntitiesScreen from './src/screens/EntitiesScreen';
import ProjectsScreen from './src/screens/ProjectsScreen';
import ChannelsScreen from './src/screens/ChannelsScreen';
import SystemsScreen from './src/screens/SystemsScreen';

const Tab = createBottomTabNavigator();
const Stack = createNativeStackNavigator();

// Heritage Stack (for detail screens)
function HeritageStack() {
  return (
    <Stack.Navigator
      screenOptions={{
        headerStyle: {
          backgroundColor: '#1a1a2e',
        },
        headerTintColor: '#fff',
        headerTitleStyle: {
          fontWeight: 'bold',
        },
      }}
    >
      <Stack.Screen 
        name="HeritageList" 
        component={HeritageScreen}
        options={{ title: 'Heritage & Wonders' }}
      />
      <Stack.Screen 
        name="WonderDetail" 
        component={WonderDetailScreen}
        options={{ title: 'Wonder Details' }}
      />
      <Stack.Screen 
        name="HeritageMap" 
        component={HeritageMapScreen}
        options={{ title: 'Heritage Map' }}
      />
      <Stack.Screen 
        name="NearbySites" 
        component={NearbySitesScreen}
        options={{ title: 'Nearby Sites' }}
      />
    </Stack.Navigator>
  );
}

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
          component={HeritageStack}
          options={{
            headerShown: false,
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
