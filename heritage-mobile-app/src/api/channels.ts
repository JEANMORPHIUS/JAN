/** * * Channels API Calls
 *  * 3 Channels: Professional, Creator, Educational
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

import apiClient from './client';

export interface Channel {
  channel_id: string;
  name: string;
  type: 'professional' | 'creator' | 'educational';
  description: string;
  target_audience: string[];
  features: string[];
  content?: any[];
}

/**
 * Get all channels
 */
export const getChannels = async (): Promise<Channel[]> => {
  try {
    const response = await apiClient.get('/api/channel-collaboration/channels');
    return response.data.channels || response.data;
  } catch (error) {
    console.error('Error fetching channels:', error);
    throw error;
  }
};

/**
 * Get channel by ID
 */
export const getChannel = async (channelId: string): Promise<Channel> => {
  try {
    const response = await apiClient.get(`/api/channel-collaboration/channels/${channelId}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching channel ${channelId}:`, error);
    throw error;
  }
};

/**
 * Get channel content
 */
export const getChannelContent = async (channelId: string): Promise<any[]> => {
  try {
    const response = await apiClient.get(`/api/channel-collaboration/channels/${channelId}/content`);
    return response.data.content || response.data;
  } catch (error) {
    console.error(`Error fetching content for channel ${channelId}:`, error);
    throw error;
  }
};
