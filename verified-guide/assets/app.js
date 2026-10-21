// Koreatrip1 — tiny helpers (no dependencies)
(function () {
  // Mark the current nav item
  var path = location.pathname.replace(/index\.html$/, '');
  document.querySelectorAll('.nav a').forEach(function (a) {
    var href = a.getAttribute('href') || '';
    var target = href.replace(/index\.html$/, '').split('#')[0];
    if (target && (path.endsWith(target) || (target === './' && path.endsWith('/')))) {
      a.classList.add('active');
    }
  });

  // Highlight today's trip day (trip runs 2026-11-01 .. 2026-11-09, KST)
  try {
    var kst = new Date(new Date().toLocaleString('en-US', { timeZone: 'Asia/Seoul' }));
    var start = new Date(2026, 10, 1); // Nov 1, 2026 = Day 1 arrival in Seoul
    var diff = Math.floor((kst - start) / 86400000);
    var dayNo = diff + 1;
    if (dayNo >= 1 && dayNo <= 9) {
      var el = document.querySelector('[data-trip-day="' + dayNo + '"]');
      if (el) {
        el.classList.add('today');
        var tag = document.createElement('span');
        tag.className = 'b b-v';
        tag.textContent = 'TODAY';
        el.appendChild(document.createTextNode(' '));
        el.appendChild(tag);
      }
      var banner = document.getElementById('today-banner');
      if (banner) {
        banner.style.display = 'block';
        banner.innerHTML = '<strong>📍 Today is Day ' + dayNo + ' of the trip (Korea time).</strong> ' +
          '<a href="days/day' + dayNo + '.html">Open today\'s plan →</a>';
      }
    }
  } catch (e) { /* non-fatal */ }

  var y = document.getElementById('yr');
  if (y) y.textContent = new Date().getFullYear();
})();
