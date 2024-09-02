import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0', // listen on all network interfaces
    port: 5173, // you can change this to any port you prefer
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src')
    }
  }
  base: '/static/dist/',  // specify a prefix path for all assets this is dependent on Django for now
})
