// Cycles the accented hero word through a list of actions with a smooth fade.
(function () {
  const el = document.getElementById("home-hero-rotator");
  if (!el) return;

  const words = (el.dataset.words || "")
    .split(",")
    .map((w) => w.trim())
    .filter(Boolean);
  if (words.length < 2) return;

  const reduceMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;

  const HOLD_MS = 2200; // time each word stays fully visible
  let index = 0;

  // Reserve horizontal space for the widest word so the headline doesn't reflow.
  const measure = document.createElement("span");
  measure.setAttribute("aria-hidden", "true");
  const cs = getComputedStyle(el);
  Object.assign(measure.style, {
    position: "absolute",
    visibility: "hidden",
    whiteSpace: "nowrap",
    font: cs.font,
    fontWeight: cs.fontWeight,
    letterSpacing: cs.letterSpacing,
  });
  document.body.appendChild(measure);
  let widest = 0;
  for (const w of words) {
    measure.textContent = w;
    widest = Math.max(widest, measure.getBoundingClientRect().width);
  }
  measure.remove();
  el.style.display = "inline-block";
  el.style.minWidth = Math.ceil(widest) + "px";

  el.classList.add("is-rotating");

  if (reduceMotion) {
    // No motion: just swap the text on a slower cadence.
    setInterval(() => {
      index = (index + 1) % words.length;
      el.textContent = words[index];
    }, HOLD_MS + 800);
    return;
  }

  function next() {
    el.classList.add("is-swapping"); // fade + lift out
    const onOut = (e) => {
      if (e.propertyName !== "opacity") return;
      el.removeEventListener("transitionend", onOut);
      index = (index + 1) % words.length;
      el.textContent = words[index];
      // Force reflow so the incoming transition restarts cleanly.
      void el.offsetWidth;
      el.classList.remove("is-swapping"); // fade + settle in
    };
    el.addEventListener("transitionend", onOut);
  }

  let timer = setInterval(next, HOLD_MS);

  // Pause cycling when the tab is hidden to save cycles.
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) {
      clearInterval(timer);
    } else {
      timer = setInterval(next, HOLD_MS);
    }
  });
})();
