/* Optional progressive enhancement: all itinerary information is visible without JavaScript. */
(() => {
  document.querySelectorAll('[data-filter-group]').forEach((group) => {
    const table = group.nextElementSibling;
    if (!table) return;
    const rows = Array.from(table.querySelectorAll('tbody tr[data-city]'));
    const count = group.querySelector('.filter-count');
    group.querySelectorAll('button[data-filter]').forEach((button) => {
      button.addEventListener('click', () => {
        const city = button.dataset.filter;
        group.querySelectorAll('button[data-filter]').forEach((item) => {
          item.setAttribute('aria-pressed', String(item === button));
        });
        let shown = 0;
        rows.forEach((row) => {
          row.hidden = city !== 'all' && row.dataset.city !== city;
          if (!row.hidden) shown += 1;
        });
        if (count) count.textContent = `Showing ${shown} ${city === 'all' ? '' : city + ' '}place${shown === 1 ? '' : 's'}`;
      });
    });
  });

  const menu = document.querySelector('.mobile-menu');
  if (menu) {
    menu.querySelectorAll('a').forEach((anchor) => anchor.addEventListener('click', () => { menu.open = false; }));
    menu.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        menu.open = false;
        menu.querySelector('summary')?.focus();
      }
    });
  }
})();
