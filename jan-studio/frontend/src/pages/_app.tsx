/** * DEVELOPMENT PHILOSOPHY: THE CHOSEN ONE
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

import type { AppProps } from 'next/app';
import '../styles/globals.css';
import '../styles/easy_eyes_design_system.css';
import '../styles/markdown-editor.css';
import '../styles/lighthouse.css';
import { AuthProvider } from '../contexts/AuthContext';
import CursorFix from '../components/CursorFix';

export default function App({ Component, pageProps }: AppProps) {
  return (
    <AuthProvider>
      <CursorFix />
      <Component {...pageProps} />
    </AuthProvider>
  );
}

