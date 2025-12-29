import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://danmaps.github.io',
  base: '/beta',
  outDir: '../build/beta',
  trailingSlash: 'always',
});
