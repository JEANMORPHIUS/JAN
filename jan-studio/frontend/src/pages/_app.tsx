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

