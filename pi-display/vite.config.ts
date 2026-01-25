import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',
    // Disable sourcemaps in production for security
    sourcemap: process.env.NODE_ENV !== 'production',
    // Use terser for minification
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: process.env.NODE_ENV === 'production',
        drop_debugger: true,
      },
    },
    // Optimize chunk splitting
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
        },
      },
    },
    // Raspberry Pi has limited resources - optimize for smaller bundles
    chunkSizeWarningLimit: 500,
  },
  server: {
    port: 3000,
    // For Raspberry Pi deployment
    host: true,
  },
  // Optimize for production
  esbuild: {
    // Drop console in production
    drop: process.env.NODE_ENV === 'production' ? ['console', 'debugger'] : [],
  },
})
