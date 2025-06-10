import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import UnoCSS from 'unocss/vite';
// import unocssConfig from './uno.config.ts';

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(), UnoCSS()],
})
