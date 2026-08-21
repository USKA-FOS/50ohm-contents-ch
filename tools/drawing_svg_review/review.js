"use strict";

const state = {
  drawings: [],
  index: 0,
  zoom: 100,
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
  error: document.querySelector("#error"),
};

const languages = ["de", "fr", "it"];

function currentDrawing() {
  return state.drawings[state.index];
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

function render() {
  const drawing = currentDrawing();
  if (!drawing) {
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
    image.onload = () => {
      image.hidden = false;
      error.hidden = true;
    };
    image.onerror = () => {
      image.hidden = true;
      error.hidden = false;
    };
    image.src = `/drawing/${language}/${encodeURIComponent(drawing)}.${language}.svg`;
  }

  const hash = `#${encodeURIComponent(drawing)}`;
  if (window.location.hash !== hash) {
    window.history.replaceState(null, "", hash);
  }
  prefetch(state.index + 1);
}

function prefetch(index) {
  const drawing = state.drawings[index];
  if (!drawing) {
    return;
  }
  for (const language of languages) {
    const image = new Image();
    image.src = `/drawing/${language}/${encodeURIComponent(drawing)}.${language}.svg`;
  }
}

function navigate(delta) {
  const nextIndex = Math.min(
    state.drawings.length - 1,
    Math.max(0, state.index + delta),
  );
  if (nextIndex !== state.index) {
    state.index = nextIndex;
    render();
  }
}

function selectFromHash() {
  const requested = decodeURIComponent(window.location.hash.slice(1));
  const index = state.drawings.indexOf(requested);
  if (index >= 0 && index !== state.index) {
    state.index = index;
    render();
  }
}

function bindEvents() {
  elements.previous.addEventListener("click", () => navigate(-1));
  elements.next.addEventListener("click", () => navigate(1));
  elements.select.addEventListener("change", () => {
    state.index = state.drawings.indexOf(elements.select.value);
    render();
  });
  elements.zoom.addEventListener("input", () => setZoom(elements.zoom.value));
  elements.zoomOut.addEventListener("click", () => setZoom(state.zoom - 10));
  elements.zoomIn.addEventListener("click", () => setZoom(state.zoom + 10));
  window.addEventListener("hashchange", selectFromHash);
  window.addEventListener("keydown", (event) => {
    if (event.target instanceof HTMLSelectElement || event.target instanceof HTMLInputElement) {
      return;
    }
    if (event.key === "ArrowLeft") {
      navigate(-1);
    } else if (event.key === "ArrowRight") {
      navigate(1);
    }
  });
}

async function initialize() {
  bindEvents();
  setZoom(state.zoom);
  try {
    const response = await fetch("/api/drawings", { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const payload = await response.json();
    if (!Array.isArray(payload.drawings) || payload.drawings.length === 0) {
      throw new Error("Aucun dessin trilingue disponible.");
    }
    state.drawings = payload.drawings;
    for (const drawing of state.drawings) {
      const option = document.createElement("option");
      option.value = drawing;
      option.textContent = drawing;
      elements.select.append(option);
    }
    const requested = decodeURIComponent(window.location.hash.slice(1));
    const requestedIndex = state.drawings.indexOf(requested);
    state.index = requestedIndex >= 0 ? requestedIndex : 0;
    render();
  } catch (error) {
    elements.error.textContent = `Chargement impossible : ${error.message}`;
    elements.error.hidden = false;
  }
}

initialize();
