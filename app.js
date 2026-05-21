const statusLabels = {
  validated: "Validated",
  bounded_repair_plan: "Bounded plan",
  blocked: "Blocked",
  review_pending: "Review pending",
  superseded: "Superseded",
};

const titleByCase = {
  "case-001": "Memory consolidation boundary",
  "case-002": "Stale task next-event pattern",
  "case-003": "Fleet rule-sync payload limit",
};

const state = {
  filter: "all",
  ledger: null,
};

function formatGeneratedAt(value) {
  if (!value) return "Unknown";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return date.toLocaleDateString("en", {
    year: "numeric",
    month: "short",
    day: "numeric",
  });
}

function setText(id, value) {
  const element = document.getElementById(id);
  if (element) element.textContent = value;
}

function caseTitle(entry) {
  return titleByCase[entry.case_id] || entry.problem_class;
}

function listItems(items, limit) {
  return items
    .slice(0, limit)
    .map((item) => `<li>${escapeHtml(item)}</li>`)
    .join("");
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function renderSummary(ledger) {
  const cases = ledger.cases || [];
  const validated = cases.filter((entry) => entry.status === "validated").length;
  const bounded = cases.filter((entry) => entry.status === "bounded_repair_plan").length;

  setText("case-count", String(cases.length));
  setText("validated-count", String(validated));
  setText("bounded-count", String(bounded));
  setText("generated-at", formatGeneratedAt(ledger.generated_at));
}

function renderCases() {
  const target = document.getElementById("case-list");
  if (!target || !state.ledger) return;

  const cases = state.ledger.cases || [];
  const visible =
    state.filter === "all"
      ? cases
      : cases.filter((entry) => entry.status === state.filter);

  if (!visible.length) {
    target.innerHTML = '<div class="empty-state">No public cases match this status.</div>';
    return;
  }

  target.innerHTML = visible
    .map((entry) => {
      const label = statusLabels[entry.status] || entry.status;
      return `
        <article class="case-card">
          <div class="case-card-header">
            <div class="case-meta">
              <span>${escapeHtml(entry.case_id)}</span>
              <span class="status-pill ${escapeHtml(entry.status)}">${escapeHtml(label)}</span>
            </div>
            <h3>${escapeHtml(caseTitle(entry))}</h3>
          </div>
          <div class="case-body">
            <div class="case-block">
              <strong>Problem</strong>
              <p>${escapeHtml(entry.problem_class)}</p>
            </div>
            <div class="case-block">
              <strong>Decision</strong>
              <p>${escapeHtml(entry.observer_decision)}</p>
            </div>
            <div class="case-block">
              <strong>Repair</strong>
              <p>${escapeHtml(entry.repair)}</p>
            </div>
            <div class="case-block">
              <strong>Validation</strong>
              <ul>${listItems(entry.validation || [], 3)}</ul>
            </div>
            <div class="case-block">
              <strong>Anti-signals</strong>
              <ul>${listItems(entry.anti_signals || [], 2)}</ul>
            </div>
          </div>
        </article>
      `;
    })
    .join("");
}

function setActiveFilter(filter) {
  state.filter = filter;
  document.querySelectorAll(".filter").forEach((button) => {
    button.classList.toggle("is-active", button.dataset.filter === filter);
  });
  renderCases();
}

async function loadLedger() {
  const response = await fetch("examples/self-iteration-ledger.json", {
    cache: "no-store",
  });
  if (!response.ok) {
    throw new Error(`Ledger request failed: ${response.status}`);
  }
  return response.json();
}

document.querySelectorAll(".filter").forEach((button) => {
  button.addEventListener("click", () => setActiveFilter(button.dataset.filter || "all"));
});

loadLedger()
  .then((ledger) => {
    state.ledger = ledger;
    renderSummary(ledger);
    renderCases();
  })
  .catch((error) => {
    const target = document.getElementById("case-list");
    if (target) {
      target.innerHTML = `<div class="empty-state">${escapeHtml(error.message)}</div>`;
    }
  });
