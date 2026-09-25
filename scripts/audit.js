// Rendered-page audit for a built brand-book.html. Paste this function into any browser
// tool that can evaluate JavaScript on the open page (Playwright, Chrome DevTools, the
// console). Run it at 1440, 1180, 900 and 390 px wide. Every list must come back empty.
async () => {
  await document.fonts.ready;
  const pages = [...document.querySelectorAll('.page')];
  // [data-intentional] marks the one logo that is small on purpose (the misuse tile)
  const texty = [...document.querySelectorAll('body *')].filter(e => !e.closest('[data-intentional]') &&
    [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()));
  const minW = ((window.BRAND || {}).logo || {}).minWidthPx || 96;
  return {
    pages: pages.length,
    horizontalScroll: document.documentElement.scrollWidth > innerWidth,
    // layout boxes only: glyph ink that pokes into the margin is not an overflow
    overflowingPages: pages.map((p, i) => {
      const b = p.querySelector('.body'); if (!b) return null;
      const r = b.getBoundingClientRect();
      const out = [...b.querySelectorAll('*')].some(e => {
        const q = e.getBoundingClientRect();
        return q.height && (q.bottom > r.bottom + 1 || q.right > r.right + 1);
      });
      return out ? i + 1 : null;
    }).filter(Boolean),
    clippedText: [...document.querySelectorAll('.spec, .t-hero, .t-display')]
      .filter(e => e.scrollWidth > e.clientWidth + 1).map(e => e.textContent.trim().slice(0, 40)),
    textUnder12px: texty.filter(e => parseFloat(getComputedStyle(e).fontSize) < 12)
      .map(e => e.textContent.trim().slice(0, 40)),
    italics: texty.filter(e => getComputedStyle(e).fontStyle !== 'normal')
      .map(e => e.textContent.trim().slice(0, 40)),
    logosBelowMinimum: [...document.querySelectorAll('.logo:not([data-intentional])')]
      .filter(e => e.getBoundingClientRect().width < minW - 0.5).length,
    fontsFailed: [...new Set([...document.fonts].filter(f => f.status === 'error').map(f => f.family))],
  };
}
