/**
 * PUSH NOTIFICATION SYSTEM COMPONENT
 * 
 * NO DILLY DALLY - Real-time push notifications
 * WebSocket connection for immediate updates
 */

import { useState, useEffect, useRef } from 'react';
import styles from './PushNotificationSystem.module.css';

interface Notification {
  id: string;
  type: string;
  priority: string;
  title: string;
  message: string;
  data?: any;
  timestamp: string;
  action_url?: string;
}

interface PushNotificationSystemProps {
  apiBaseUrl?: string;
}

export default function PushNotificationSystem({ 
  apiBaseUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000' 
}: PushNotificationSystemProps) {
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [isConnected, setIsConnected] = useState(false);
  const [unreadCount, setUnreadCount] = useState(0);
  const wsRef = useRef<WebSocket | null>(null);
  const reconnectTimeoutRef = useRef<NodeJS.Timeout | null>(null);

  useEffect(() => {
    connectWebSocket();
    return () => {
      if (wsRef.current) {
        wsRef.current.close();
      }
      if (reconnectTimeoutRef.current) {
        clearTimeout(reconnectTimeoutRef.current);
      }
    };
  }, []);

  const connectWebSocket = () => {
    try {
      const wsUrl = apiBaseUrl.replace('http://', 'ws://').replace('https://', 'wss://') + '/api/push/ws';
      const ws = new WebSocket(wsUrl);
      
      ws.onopen = () => {
        console.log('Push notification system connected');
        setIsConnected(true);
        if (reconnectTimeoutRef.current) {
          clearTimeout(reconnectTimeoutRef.current);
        }
      };

      ws.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          
          if (data.type === 'notification') {
            const notification = data.notification as Notification;
            setNotifications(prev => [notification, ...prev]);
            setUnreadCount(prev => prev + 1);
            
            // Show browser notification if permission granted
            if ('Notification' in window && Notification.permission === 'granted') {
              new Notification(notification.title, {
                body: notification.message,
                icon: '/favicon.ico',
                tag: notification.id
              });
            }
          } else if (data.type === 'welcome') {
            console.log('Welcome message:', data.message);
            if (data.mission) {
              console.log('Mission:', data.mission);
            }
          }
        } catch (error) {
          console.error('Error parsing WebSocket message:', error);
        }
      };

      ws.onerror = (error) => {
        console.error('WebSocket error:', error);
        setIsConnected(false);
      };

      ws.onclose = () => {
        console.log('WebSocket disconnected, reconnecting...');
        setIsConnected(false);
        // Reconnect after 3 seconds
        reconnectTimeoutRef.current = setTimeout(() => {
          connectWebSocket();
        }, 3000);
      };

      wsRef.current = ws;
    } catch (error) {
      console.error('Error connecting WebSocket:', error);
      setIsConnected(false);
    }
  };

  const requestNotificationPermission = async () => {
    if ('Notification' in window && Notification.permission === 'default') {
      await Notification.requestPermission();
    }
  };

  const markAsRead = async (notificationId: string) => {
    try {
      const response = await fetch(`${apiBaseUrl}/api/push/notifications/${notificationId}/read`, {
        method: 'POST'
      });
      if (response.ok) {
        setNotifications(prev => 
          prev.map(n => n.id === notificationId ? { ...n, read: true } : n)
        );
        setUnreadCount(prev => Math.max(0, prev - 1));
      }
    } catch (error) {
      console.error('Error marking notification as read:', error);
    }
  };

  const clearNotifications = () => {
    setNotifications([]);
    setUnreadCount(0);
  };

  const getPriorityClass = (priority: string) => {
    switch (priority) {
      case 'critical': return styles.critical;
      case 'high': return styles.high;
      case 'medium': return styles.medium;
      default: return styles.low;
    }
  };

  return (
    <div className={styles.pushSystem}>
      <div className={styles.notificationBell} onClick={requestNotificationPermission}>
        <span className={styles.bellIcon}>🔔</span>
        {unreadCount > 0 && (
          <span className={styles.badge}>{unreadCount}</span>
        )}
        <span className={`${styles.statusIndicator} ${isConnected ? styles.connected : styles.disconnected}`} />
      </div>

      {notifications.length > 0 && (
        <div className={styles.notificationPanel}>
          <div className={styles.panelHeader}>
            <h3>Notifications ({unreadCount} unread)</h3>
            <button onClick={clearNotifications} className={styles.clearButton}>Clear All</button>
          </div>
          <div className={styles.notificationList}>
            {notifications.slice(0, 10).map((notification) => (
              <div
                key={notification.id}
                className={`${styles.notification} ${getPriorityClass(notification.priority)} ${notification.read ? styles.read : ''}`}
                onClick={() => {
                  markAsRead(notification.id);
                  if (notification.action_url) {
                    window.location.href = notification.action_url;
                  }
                }}
              >
                <div className={styles.notificationHeader}>
                  <strong>{notification.title}</strong>
                  <span className={styles.priorityBadge}>{notification.priority}</span>
                </div>
                <p className={styles.notificationMessage}>{notification.message}</p>
                <span className={styles.notificationTime}>
                  {new Date(notification.timestamp).toLocaleTimeString()}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
