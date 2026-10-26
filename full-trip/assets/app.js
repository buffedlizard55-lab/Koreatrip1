/* Full-trip renderer — no framework, no network. */
(function () {
  const D = window.FULLTRIP;
  if (!D) return;
  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const badge = (s) => {
    const m = { v: ["v", "Verified"], p: ["p", "Partially verified"], u: ["u", "Unverified"], c: ["c", "Conflict"] };
    const b = m[s] || m.u;
    return `<span class="badge ${b[0]}">${b[1]}</span>`;
  };
  const srcLink = (k) => {
    const s = D.sources[k];
    if (!s) return "";
    return `<a href="${esc(s[1])}" target="_blank" rel="noopener">${esc(s[0])} ↗</a>`;
  };
  const valOrBlank = (v) => (v ? esc(v) : `<span class="blank">— not confirmed</span>`);

  function dayStepsHTML(day) {
    return day.steps.map((s) => `
      <div class="step">
        <div class="time">${esc(s.time)}</div>
        <h3>${esc(s.title)} ${badge(s.status)}</h3>
        <p>${esc(s.plan)}</p>
        <div class="facts">
          <p><strong>Confirmed:</strong> ${s.facts ? esc(s.facts) : '<span class="blank">— nothing confirmed from an official source</span>'}</p>
          <p class="src"><strong>Source:</strong> ${srcLink(s.src)}</p>
        </div>
        ${s.note ? `<p><small class="note">⚑ ${esc(s.note)}</small></p>` : ""}
      </div>`).join("");
  }

  /* ---- Day page (?day=N) ---- */
  if ($("daydetail")) {
    const q = parseInt(new URLSearchParams(location.search).get("day"), 10);
    const day = D.days.find((d) => d.n === q) || D.days[0];
    document.title = `Day ${day.n} — ${day.title} · Korea 16-day trip`;
    $("chips").innerHTML = D.days.map((d) =>
      `<a href="day.html?day=${d.n}" class="${d.n === day.n ? "on" : ""}" ${d.n === day.n ? 'aria-current="true"' : ""}>Day ${d.n}</a>`).join("");
    const prev = D.days.find((d) => d.n === day.n - 1), next = D.days.find((d) => d.n === day.n + 1);
    $("daydetail").innerHTML = `
      <p class="time" style="color:var(--brand);font-weight:800;letter-spacing:.06em;text-transform:uppercase;font-size:.8rem">Day ${day.n} · ${esc(day.dow)} ${esc(day.date)}</p>
      <h1>${esc(day.title)}</h1>
      <p class="lede">Sleeping: <strong>${esc(day.base)}</strong> · 2 adult travelers</p>
      ${day.alert ? `<div class="alert ${day.n === 3 ? "crit" : "warn"}"><strong>Heads up —</strong> ${esc(day.alert)}</div>` : ""}
      ${dayStepsHTML(day)}
      <div class="prevnext">
        <span>${prev ? `<a class="btn ghost" href="day.html?day=${prev.n}">← Day ${prev.n}: ${esc(prev.title)}</a>` : ""}</span>
        <span>${next ? `<a class="btn" href="day.html?day=${next.n}">Day ${next.n}: ${esc(next.title)} →</a>` : ""}</span>
      </div>`;
  }

  /* ---- All-days (print) page ---- */
  if ($("alldays")) {
    $("alldays").innerHTML = D.days.map((day) => `
      <section class="card"><h2>Day ${day.n} · ${esc(day.dow)} ${esc(day.date)} — ${esc(day.title)}</h2>
      <p><small class="note">Base: ${esc(day.base)}</small></p>
      ${day.alert ? `<div class="alert warn">${esc(day.alert)}</div>` : ""}${dayStepsHTML(day)}</section>`).join("");
  }

  /* ---- Dashboard ---- */
  if ($("daygrid")) {
    $("daygrid").innerHTML = D.days.map((d) => `
      <a class="daytile" href="day.html?day=${d.n}">
        <span class="dn">Day ${d.n} · ${esc(d.dow.slice(0, 3))} ${esc(d.date.replace(", 2026", ""))}</span>
        <span class="dt">${esc(d.title)}</span>
        <span class="dd">${esc(d.base.split(",")[0])}</span>
      </a>`).join("");
    const steps = D.days.reduce((a, d) => a + d.steps.length, 0);
    $("stats").innerHTML = [
      [D.days.length, "Trip days (Nov 1–16, 2026)"],
      [steps, "Itinerary steps checked"],
      [D.venues.length, "Venues & stays tabled"],
      [Object.keys(D.sources).length, "Official sources linked"],
      [D.flags.length, "Flags for your review"]
    ].map(([n, l]) => `<div class="stat"><b>${n}</b><span>${l}</span></div>`).join("");
    // "Today" helper: works during the trip itself.
    const now = new Date(); now.setHours(0, 0, 0, 0);
    const start = new Date(2026, 10, 1); // Nov 1, 2026
    const idx = Math.floor((now - start) / 864e5) + 1;
    if (idx >= 1 && idx <= 16) {
      const t = $("todaybox");
      const d = D.days[idx - 1];
      t.innerHTML = `<div class="alert ok"><strong>Today is Day ${d.n} — ${esc(d.title)}.</strong> <a href="day.html?day=${d.n}">Open today’s plan →</a></div>`;
      document.querySelectorAll(".daytile")[idx - 1].classList.add("today");
    }
  }

  /* ---- Venues table ---- */
  if ($("venuetable")) {
    const render = (rows) => {
      $("venuetable").innerHTML = `<table class="resp"><thead><tr>
        <th>Venue</th><th>Category</th><th>Day</th><th>Confirmed hours</th><th>Closed</th><th>Confirmed admission</th><th>Status</th><th>Official source</th><th>Note</th></tr></thead><tbody>${
        rows.map((v) => `<tr><td data-label="Venue"><strong>${esc(v[0])}</strong></td><td data-label="Category">${esc(v[1])}</td><td data-label="Day">${esc(v[2])}</td><td data-label="Hours">${valOrBlank(v[3])}</td><td data-label="Closed">${valOrBlank(v[4])}</td><td data-label="Admission">${valOrBlank(v[5])}</td><td data-label="Status">${badge(v[6])}</td><td data-label="Source">${srcLink(v[7])}</td><td data-label="Note">${esc(v[8])}</td></tr>`).join("") || '<tr><td colspan="9">No matches. Clear the search.</td></tr>'
        }</tbody></table>`;
    };
    render(D.venues);
    $("vsearch").addEventListener("input", (e) => {
      const q = e.target.value.toLowerCase();
      render(D.venues.filter((v) => v.join(" ").toLowerCase().includes(q)));
    });
  }

  /* ---- Transport table ---- */
  if ($("transporttable")) {
    $("transporttable").innerHTML = `<table class="resp"><thead><tr><th>Leg</th><th>Day</th><th>Route</th><th>Confirmed time / fare</th><th>Status</th><th>Official source</th><th>Note</th></tr></thead><tbody>${
      D.transport.map((t) => `<tr><td data-label="Leg"><strong>${esc(t[0])}</strong></td><td data-label="Day">${esc(t[1])}</td><td data-label="Route">${esc(t[2])}</td><td data-label="Confirmed">${valOrBlank(t[3])}</td><td data-label="Status">${badge(t[4])}</td><td data-label="Source">${srcLink(t[5])}</td><td data-label="Note">${esc(t[6])}</td></tr>`).join("")
      }</tbody></table>`;
  }

  /* ---- Flagged table ---- */
  if ($("flagtable")) {
    $("flagtable").innerHTML = `<table class="resp"><thead><tr><th>ID</th><th>Type</th><th>Finding (needs your decision / recheck)</th><th>Source to review</th></tr></thead><tbody>${
      D.flags.map((f) => `<tr><td data-label="ID"><strong>${esc(f[0])}</strong></td><td data-label="Type">${esc(f[1])}</td><td data-label="Finding">${esc(f[2])}</td><td data-label="Source">${srcLink(f[3])}</td></tr>`).join("")
      }</tbody></table>`;
  }

  /* ---- Sources table ---- */
  if ($("sourcetable")) {
    const rows = Object.entries(D.sources).map(([k, v], i) =>
      `<tr><td data-label="#"><strong>S${String(i + 1).padStart(2, "0")}</strong></td><td data-label="Source">${esc(v[0])}</td><td data-label="URL"><a href="${esc(v[1])}" target="_blank" rel="noopener">${esc(v[1])}</a></td></tr>`).join("");
    $("sourcetable").innerHTML = `<table class="resp"><thead><tr><th>#</th><th>Official source</th><th>URL (checked ${esc(D.checked)})</th></tr></thead><tbody>${rows}</tbody></table>`;
  }
})();
