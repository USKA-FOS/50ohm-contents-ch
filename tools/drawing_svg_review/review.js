"use strict";

const state = {
  allDrawings: [], drawings: [], details: {}, index: 0, zoom: 100,
  filter: "all", reviewId: "", feedbackUrl: "",
};

const elements = {
  previous: document.querySelector("#previous"),
  next: document.querySelector("#next"),
  select: document.querySelector("#drawing-select"),
  position: document.querySelector("#position"),
  zoom: document.querySelector("#zoom"),
  zoomOut: document.querySelector("#zoom-out"),
  zoomIn: document.querySelector("#zoom-in"),
  zoomValue: document.querySelector("#zoom-value"),
  filterAll: document.querySelector("#filter-all"),
  filterTranslated: document.querySelector("#filter-translated"),
  feedback: document.querySelector("#feedback"),
  error: document.querySelector("#error"),
};

const languages = ["de", "fr", "it"];

function currentDrawing() {
  return state.drawings[state.index];
}

function isFullyTranslated(stem) {
  const availability = state.details[stem]?.availability ?? {};
  return availability.fr === true && availability.it === true;
}

function setZoom(value) {
  const min = Number(elements.zoom.min);
  const max = Number(elements.zoom.max);
  state.zoom = Math.min(max, Math.max(min, Number(value)));
  elements.zoom.value = String(state.zoom);
  elements.zoomValue.value = `${state.zoom}%`;
  document.documentElement.style.setProperty("--drawing-width", `${state.zoom}%`);
  elements.zoomOut.disabled = state.zoom <= min;
  elements.zoomIn.disabled = state.zoom >= max;
}

function drawingAssetUrl(stem, language) {
  const availability = state.details[stem]?.availability ?? {};
  if (language === "de" || availability[language] === true) {
    return `${language}/${encodeURIComponent(stem)}.${language}.svg`;
  }
  return `de/${encodeURIComponent(stem)}.de.svg`;
}

function buildFeedbackUrl(stem) {
  const detail = state.details[stem];
  if (!state.feedbackUrl || !state.reviewId || !detail?.canonical_id) return "";
  const url = new URL(state.feedbackUrl, window.location.href);
  url.searchParams.set("context", "drawing_review");
  url.searchParams.set("review_id", state.reviewId);
  url.searchParams.set("drawing", stem);
  url.searchParams.set("canonical_id", detail.canonical_id);
  url.searchParams.set("lang", "fr");
  return url.toString();
}

function render() {
  const drawing = currentDrawing();
  if (!drawing) {
    elements.position.textContent = "0 / 0";
    elements.previous.disabled = true;
    elements.next.disabled = true;
    elements.feedback.hidden = true;
    return;
  }
  elements.select.value = drawing;
  elements.position.textContent = `${state.index + 1} / ${state.drawings.length}`;
  elements.previous.disabled = state.index === 0;
  elements.next.disabled = state.index === state.drawings.length - 1;
  document.title = `Dessin ${drawing} - Revue`;

  for (const language of languages) {
    const image = document.querySelector(`#image-${language}`);
    const error = document.querySelector(`#error-${language}`);
    error.hidden = true;
    image.hidden = false;
    image.alt = `Dessin ${drawing}, ${language.toUpperCase()}`;
    image.onload = () => { image.hidden = false; error.hidden = true; };
    image.onerror = () => { image.hidden = true; error.hidden = false; };
    image.src = drawingAssetUrl(drawing, language);
    if (language !== "de") {
      document.querySelector(`#fallback-${language}`).hidden =
        state.details[drawing]?.availability?.[language] !== false;
    }
  }

  const feedbackUrl = buildFeedbackUrl(drawing);
  elements.feedback.hidden = !feedbackUrl;
  elements.feedback.href = feedbackUrl || "#";
  const hash = `#${encodeURIComponent(drawing)}`;
  if (window.location.hash !== hash) window.history.replaceState(null, "", hash);
  prefetch(state.index + 1);
}

function rebuildSelect() {
  elements.select.replaceChildren();
  for (const drawing of state.drawings) {
    const option = document.createElement("option");
    option.value = drawing;
    option.textContent = drawing;
    elements.select.append(option);
  }
}

function applyFilter(filter) {
  const previous = currentDrawing();
  state.filter = filter;
  state.drawings = filter === "translated"
    ? state.allDrawings.filter(isFullyTranslated)
    : [...state.allDrawings];
  state.index = Math.max(0, state.drawings.indexOf(previous));
  elements.filterAll.classList.toggle("is-active", filter === "all");
  elements.filterTranslated.classList.toggle("is-active", filter === "translated");
  elements.filterAll.setAttribute("aria-pressed", String(filter === "all"));
  elements.filterTranslated.setAttribute("aria-pressed", String(filter === "translated"));
  rebuildSelect();
  render();
}

function prefetch(index) {
  const drawing = state.drawings[index];
  if (!drawing) return;
  for (const language of languages) {
    const image = new Image();
    image.src = drawingAssetUrl(drawing, language);
  }
}

function navigate(delta) {
  const nextIndex = Math.min(state.drawings.length - 1, Math.max(0, state.index + delta));
  if (nextIndex !== state.index) { state.index = nextIndex; render(); }
}

function selectFromHash() {
  const requested = decodeURIComponent(window.location.hash.slice(1));
  const index = state.drawings.indexOf(requested);
  if (index >= 0 && index !== state.index) { state.index = index; render(); }
}

function bindEvents() {
  elements.previous.addEventListener("click", () => navigate(-1));
  elements.next.addEventListener("click", () => navigate(1));
  elements.select.addEventListener("change", () => {
    state.index = state.drawings.indexOf(elements.select.value);
    render();
  });
  elements.filterAll.addEventListener("click", () => applyFilter("all"));
  elements.filterTranslated.addEventListener("click", () => applyFilter("translated"));
  elements.zoom.addEventListener("input", () => setZoom(elements.zoom.value));
  elements.zoomOut.addEventListener("click", () => setZoom(state.zoom - 10));
  elements.zoomIn.addEventListener("click", () => setZoom(state.zoom + 10));
  window.addEventListener("hashchange", selectFromHash);
  window.addEventListener("keydown", (event) => {
    if (event.target instanceof HTMLSelectElement || event.target instanceof HTMLInputElement) return;
    if (event.key === "ArrowLeft") navigate(-1);
    else if (event.key === "ArrowRight") navigate(1);
  });
}

async function initialize() {
  bindEvents();
  setZoom(state.zoom);
  try {
    const response = await fetch("manifest.json", { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const payload = await response.json();
    if (!payload.drawings || typeof payload.drawings !== "object") {
      throw new Error("Manifeste de revue invalide.");
    }
    state.details = payload.drawings;
    state.allDrawings = Object.keys(payload.drawings);
    state.reviewId = payload.review_id ?? "";
    state.feedbackUrl = payload.feedback_url ?? "";
    state.drawings = [...state.allDrawings];
    const requested = decodeURIComponent(window.location.hash.slice(1));
    state.index = Math.max(0, state.drawings.indexOf(requested));
    rebuildSelect();
    render();
  } catch (error) {
    elements.error.textContent = `Chargement impossible : ${error.message}`;
    elements.error.hidden = false;
  }
}

initialize();
