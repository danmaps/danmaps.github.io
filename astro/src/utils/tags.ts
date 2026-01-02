import { slugifyTag } from './slug';

export type TagLink = {
  name: string;
  slug: string;
  href: string;
};

export const buildTagLink = (tag: string): TagLink | null => {
  const slug = slugifyTag(tag);
  if (!slug) {
    return null;
  }

  return {
    name: tag,
    slug,
    href: `${import.meta.env.BASE_URL}tags/${slug}/`,
  };
};

export const tagHref = (tag: string) => buildTagLink(tag)?.href ?? '#';
