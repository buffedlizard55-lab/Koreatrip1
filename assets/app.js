/* Korea trip site — renders pages from data/trip.json and data/sources.json.
   No external libraries. Every value shown comes from the data file. */
(function () {
  "use strict";

  var DATA = null;
  var SOURCES = null;

  function esc(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  }

  function pill(status) {
    var cls = {
      "Verified": "s-verified",
      "Corrected": "s-corrected",
      "Partially verified": "s-partial",
      "Unverified": "s-unverified",
      "Calculated": "s-calculated"
    }[status] || "s-unverified";
    return '<span class="pill ' + cls + '">' + esc(status) + "</span>";
  }

  function srcLink(row) {
    var label = row.source_role === "Confirms" ? "Official source" : "Check here";
    return '<a href="' + esc(row.source_url) + '" target="_blank" rel="noopener">' + label + "</a>" +
      '<div class="sub">' + esc(row.source_name) + "</div>";
  }

  function verifiedCell(row) {
    if (!row.verified) {
      return '<span class="blank">Not verified — left blank</span>';
    }
    return esc(row.verified);
  }

  function dayLabel(d) {
    if (d === "Trip") return "Trip";
    var day = DATA.days.filter(function (x) { return x.day === d; })[0];
    return "Day " + d + (day ? " · " + day.date.split(" ")[0] + " " + day.date.split(" ")[1] + " " + day.date.split(" ")[2] : "");
  }

  function rowsTable(rows, opts) {
    opts = opts || {};
    if (!rows.length) return '<p class="lede">No entries match.</p>';
    var head = "<thead><tr><th>Day</th><th>Category</th><th>Item</th><th>As written in brief</th><th>Verified value (official)</th><th>Status</th><th>Source</th></tr></thead>";
    var body = rows.map(function (r) {
      var flag = r.flag ? ' <span class="flag">⚑ FLAG</span>' : "";
      var note = r.note ? '<div class="sub">' + esc(r.note) + "</div>" : "";
      return "<tr>" +
        '<td data-label="Day">' + esc(r.day === "Trip" ? "All" : r.day) + "</td>" +
        '<td data-label="Category">' + esc(r.category) + "</td>" +
        '<td data-label="Item"><strong>' + esc(r.item) + "</strong>" + flag + note + "</td>" +
        '<td data-label="As written">' + esc(r.submitted) + "</td>" +
        '<td data-label="Verified value">' + verifiedCell(r) + "</td>" +
        '<td data-label="Status">' + pill(r.status) + "</td>" +
        '<td data-label="Source">' + srcLink(r) + "</td>" +
        "</tr>";
    }).join("");
    return '<div class="tablewrap"><table>' + head + "<tbody>" + body + "</tbody></table></div>";
  }

  function countBy(rows, key) {
    var c = {};
    rows.forEach(function (r) { c[r[key]] = (c[r[key]] || 0) + 1; });
    return c;
  }

  function flaggedCount() {
    return DATA.rows.filter(function (r) { return r.flag; }).length;
  }

  function setCount(id, n) {
    var el = document.getElementById(id);
    if (el) el.textContent = n;
  }

  /* ---------- Pages ---------- */

  function renderIndex() {
    var rows = DATA.rows;
    var st = countBy(rows, "status");
    setCount("n-entries", rows.length);
    setCount("n-verified", (st["Verified"] || 0));
    setCount("n-partial", (st["Partially verified"] || 0) + (st["Corrected"] || 0));
    setCount("n-unverified", (st["Unverified"] || 0));
    setCount("n-flags", flaggedCount());
    setCount("n-irr", DATA.irregularities.length);
    var high = DATA.irregularities.filter(function (i) { return i.severity === "High"; });
    var top = DATA.irregularities.slice(0, 5);
    var html = "";
    html += '<div class="notice bad"><strong>' + high.length + " high-priority issue(s):</strong> " +
      high.map(function (i) { return esc(i.issue); }).join(" ") +
      ' <a href="flagged.html">See all flagged items →</a></div>';
    html += "<h2>Days at a glance</h2>";
    html += '<div class="tablewrap"><table><thead><tr><th>Day</th><th>Date</th><th>Plan</th><th>Flags</th></tr></thead><tbody>';
    DATA.days.forEach(function (d) {
      var n = rows.filter(function (r) { return r.day === d.day && r.flag; }).length;
      html += "<tr>" +
        '<td data-label="Day"><a href="itinerary.html#day-' + d.day + '">Day ' + d.day + "</a></td>" +
        '<td data-label="Date">' + esc(d.date) + "</td>" +
        '<td data-label="Plan">' + esc(d.title) + "</td>" +
        '<td data-label="Flags">' + (n ? '<span class="flag">⚑ ' + n + "</span>" : "—") + "</td></tr>";
    });
    html += "</tbody></table></div>";
    html += "<h2>Top flagged items</h2>";
    html += '<div class="tablewrap"><table><thead><tr><th>Severity</th><th>Where</th><th>Issue</th><th>Source</th></tr></thead><tbody>';
    top.forEach(function (i) {
      html += "<tr>" +
        '<td data-label="Severity"><span class="sev-' + esc(i.severity) + '">' + esc(i.severity) + "</span></td>" +
        '<td data-label="Where">' + esc(i.where) + "</td>" +
        '<td data-label="Issue">' + esc(i.issue) + "</td>" +
        '<td data-label="Source"><a href="' + esc(i.source_url) + '" target="_blank" rel="noopener">' + esc(i.source_name) + "</a></td></tr>";
    });
    html += "</tbody></table></div>";
    document.getElementById("main-body").innerHTML = html;
  }

  function renderItinerary() {
    var html = "";
    DATA.days.forEach(function (d) {
      var rows = DATA.rows.filter(function (r) { return r.day === d.day; });
      var flags = rows.filter(function (r) { return r.flag; }).length;
      html += '<section class="day" id="day-' + d.day + '">';
      html += "<header><div><span class=\"date\">Day " + d.day + " · " + esc(d.label) + "</span>" +
        '<div class="title">' + esc(d.title) + "</div></div>" +
        '<div class="sub" style="color:var(--muted);font-size:13px">' + esc(d.city) + " · " + rows.length + " entries" + (flags ? " · ⚑ " + flags + " flagged" : "") + "</div></header>";
      html += '<div class="body">';
      if (!rows.length) {
        html += '<p class="lede" style="padding:8px">No entries for this day in the brief.</p>';
      } else {
        html += rowsTable(rows);
      }
      html += "</div></section>";
    });
    var extra = DATA.rows.filter(function (r) { return r.day === "Trip"; });
    if (extra.length) {
      html += '<section class="day"><header><div><span class="date">Trip-wide checks</span></div></header><div class="body">' + rowsTable(extra) + "</div></section>";
    }
    document.getElementById("main-body").innerHTML = html;
  }

  function renderEntries() {
    var rows = DATA.rows.slice();
    var state = { q: "", status: "", cat: "", flagOnly: false };
    var cats = Array.from(new Set(rows.map(function (r) { return r.category; }))).sort();
    var stats = Array.from(new Set(rows.map(function (r) { return r.status; })));
    var toolbar = '<div class="toolbar">' +
      '<input id="q" type="search" placeholder="Search items, notes, sources…" aria-label="Search">' +
      '<select id="fs" aria-label="Status"><option value="">All statuses</option>' + stats.map(function (s) { return "<option>" + esc(s) + "</option>"; }).join("") + "</select>" +
      '<select id="fc" aria-label="Category"><option value="">All categories</option>' + cats.map(function (c) { return "<option>" + esc(c) + "</option>"; }).join("") + "</select>" +
      '<label><input id="ff" type="checkbox"> Flagged only</label>' +
      '<span class="count" id="cnt"></span></div>';
    document.getElementById("main-body").innerHTML = toolbar + '<div id="tbl"></div>';
    function apply() {
      var out = rows.filter(function (r) {
        if (state.status && r.status !== state.status) return false;
        if (state.cat && r.category !== state.cat) return false;
        if (state.flagOnly && !r.flag) return false;
        if (state.q) {
          var hay = (r.item + " " + r.submitted + " " + r.verified + " " + r.note + " " + r.source_name + " " + r.category).toLowerCase();
          if (hay.indexOf(state.q.toLowerCase()) === -1) return false;
        }
        return true;
      });
      document.getElementById("tbl").innerHTML = rowsTable(out);
      document.getElementById("cnt").textContent = out.length + " of " + rows.length + " rows";
    }
    document.getElementById("q").addEventListener("input", function (e) { state.q = e.target.value; apply(); });
    document.getElementById("fs").addEventListener("change", function (e) { state.status = e.target.value; apply(); });
    document.getElementById("fc").addEventListener("change", function (e) { state.cat = e.target.value; apply(); });
    document.getElementById("ff").addEventListener("change", function (e) { state.flagOnly = e.target.checked; apply(); });
    apply();
  }

  function renderFiltered(predicate, emptyText) {
    var rows = DATA.rows.filter(predicate);
    var html = "<p class=\"lede\">" + rows.length + " entries. " + "Blank “Verified value” means no official source confirmed the entry.</p>";
    html += rows.length ? rowsTable(rows) : '<p class="lede">' + esc(emptyText) + "</p>";
    document.getElementById("main-body").innerHTML = html;
  }

  function renderTransit() {
    renderFiltered(function (r) { return r.category === "Transit" || r.topic === "Airport bus" || r.topic === "Airport train"; }, "No transit entries.");
  }

  function renderHours() {
    renderFiltered(function (r) { return r.is_hours === true; }, "No hours entries.");
  }

  function renderFlagged() {
    var rows = DATA.rows.filter(function (r) { return r.flag; });
    var html = '<div class="notice bad"><strong>For your review after go-live.</strong> These items are published, not blocking. Each has a source link. Blank = not verified.</div>';
    html += "<h2>Irregularities in the brief (" + DATA.irregularities.length + ")</h2>";
    html += '<div class="tablewrap"><table><thead><tr><th>ID</th><th>Severity</th><th>Where</th><th>Issue</th><th>Suggested action</th><th>Source</th></tr></thead><tbody>';
    DATA.irregularities.forEach(function (i) {
      html += "<tr>" +
        '<td data-label="ID">' + esc(i.id) + "</td>" +
        '<td data-label="Severity"><span class="sev-' + esc(i.severity) + '">' + esc(i.severity) + "</span></td>" +
        '<td data-label="Where">' + esc(i.where) + "</td>" +
        '<td data-label="Issue">' + esc(i.issue) + "</td>" +
        '<td data-label="Suggested action">' + esc(i.action) + "</td>" +
        '<td data-label="Source"><a href="' + esc(i.source_url) + '" target="_blank" rel="noopener">' + esc(i.source_name) + "</a></td></tr>";
    });
    html += "</tbody></table></div>";
    html += "<h2>Flagged table rows (" + rows.length + ")</h2>";
    html += rowsTable(rows);
    document.getElementById("main-body").innerHTML = html;
  }

  function renderSources() {
    var html = '<p class="lede">Every link used on this site. “Official” means a government, tourism agency, operator or venue website. Press and calculated items are labeled as such.</p>';
    html += '<div class="tablewrap"><table><thead><tr><th>Source</th><th>Type</th><th>Used for</th><th>Link</th></tr></thead><tbody>';
    SOURCES.forEach(function (s) {
      html += "<tr>" +
        '<td data-label="Source">' + esc(s.name) + "</td>" +
        '<td data-label="Type">' + esc(s.type) + "</td>" +
        '<td data-label="Used for">' + esc(s.used_for) + "</td>" +
        '<td data-label="Link"><a href="' + esc(s.url) + '" target="_blank" rel="noopener">Open</a></td></tr>';
    });
    html += "</tbody></table></div>";
    document.getElementById("main-body").innerHTML = html;
  }

  var PAGES = {
    index: renderIndex,
    itinerary: renderItinerary,
    entries: renderEntries,
    transit: renderTransit,
    hours: renderHours,
    flagged: renderFlagged,
    sources: renderSources
  };

  function boot() {
    var page = document.body.getAttribute("data-page");
    var base = document.body.getAttribute("data-base") || ".";
    Promise.all([
      fetch(base + "/data/trip.json").then(function (r) { return r.json(); }),
      fetch(base + "/data/sources.json").then(function (r) { return r.json(); })
    ]).then(function (res) {
      DATA = res[0];
      SOURCES = res[1];
      var stamp = document.getElementById("asof");
      if (stamp) stamp.textContent = DATA.meta.as_of;
      PAGES[page]();
    }).catch(function (err) {
      document.getElementById("main-body").innerHTML = '<div class="notice bad">Could not load data: ' + esc(err) + "</div>";
    });
  }

  document.addEventListener("DOMContentLoaded", boot);
})();
