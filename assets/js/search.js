/* Local assets only. Pagefind supplies keyboard-accessible native form controls. */
(() => {
  const target = document.querySelector('#search');
  const status = document.querySelector('#search-status');
  if (!target) return;
  try {
    if (!window.PagefindUI) throw new Error('Search bundle unavailable');
    const ui = new PagefindUI({element: '#search', bundlePath: target.dataset.bundle,
      baseUrl: target.dataset.bundle.replace(/pagefind\/$/, ''),
      showImages: false, showSubResults: false, resetStyles: false,
      translations: {placeholder: 'Search SIGCSE'},
      processResult: result => {
        result.meta.Category = result.meta.category;
        result.meta['Record type'] = result.meta.record_type === 'Conference legacy' ? 'Conference archive' : result.meta.record_type;
        delete result.meta.category;
        delete result.meta.record_type;
        return result;
      }});
    status.textContent = '';
    const query = new URLSearchParams(location.search).get('q');
    if (query) ui.triggerSearch(query.slice(0, 200));
  } catch (error) {
    status.textContent = 'Search could not load. Please reload the page or use the browse links below.';
  }
})();
