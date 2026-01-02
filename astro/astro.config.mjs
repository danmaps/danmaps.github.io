import { defineConfig } from 'astro/config';
import path from 'node:path';

export default defineConfig({
  site: 'https://danmaps.github.io',
  base: '/beta',
  outDir: '../build/beta',
  trailingSlash: 'always',
  vite: {
    resolve: {
      alias: {
        post: path.resolve('./src/layouts/post.astro'),
      },
    },
  },
});
