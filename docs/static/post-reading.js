// Post reading enhancements:
// 1. Scroll progress bar
// 2. Auto-generate table of contents from headings

(function () {
  // --- Scroll progress ---
  const progressBar = document.querySelector('.scroll-progress');
  if (progressBar) {
    window.addEventListener('scroll', function () {
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const scrolled = window.scrollY;
      const progress = docHeight > 0 ? (scrolled / docHeight) * 100 : 0;
      progressBar.style.width = progress + '%';
    }, { passive: true });
  }

  // --- Table of contents ---
  const tocContainer = document.getElementById('post-toc-list');
  const article = document.querySelector('.post-reading');
  if (tocContainer && article) {
    const headings = article.querySelectorAll('h2, h3');
    if (headings.length < 2) {
      // Hide TOC if there aren't enough headings
      const tocWrapper = document.querySelector('.post-toc');
      if (tocWrapper) tocWrapper.style.display = 'none';
      return;
    }

    headings.forEach(function (heading, index) {
      // Assign an ID if missing
      if (!heading.id) {
        heading.id = 'section-' + index;
      }

      var li = document.createElement('li');
      if (heading.tagName === 'H3') {
        li.className = 'toc-h3';
      }
      var a = document.createElement('a');
      a.href = '#' + heading.id;
      a.textContent = heading.textContent;
      li.appendChild(a);
      tocContainer.appendChild(li);
    });
  }
})();
