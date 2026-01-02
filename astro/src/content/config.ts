import { defineCollection, z } from 'astro:content';

const tagSchema = z
  .string()
  .trim()
  .min(2, { message: 'Tags must be at least 2 characters' })
  .max(32, { message: 'Tags must be 32 characters or fewer' })
  .transform((tag) => tag.toLowerCase());

const posts = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string().optional(),
    date: z.coerce.date().optional(),
    description: z.string().optional(),
    tags: z
      .preprocess((value) => {
        if (!value) return [];
        if (Array.isArray(value)) return value;
        if (typeof value === 'string') return [value];
        return [];
      }, z.array(tagSchema))
      .default([]),
  }),
});

export const collections = { posts };
