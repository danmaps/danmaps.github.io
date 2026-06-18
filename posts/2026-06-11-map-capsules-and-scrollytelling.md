---
title: Map capsules and scrollytelling for GIS workflow writeups
date: 2026-06-11
tags:
  - Draft
  - GIS
  - AI
  - mapping
  - workflow
layout: rich
---

I keep coming back to the same problem when writing technical GIS posts:

- static screenshots are fast to publish
- but they hide the spatial decision points
- and readers miss the *why* behind each map state

So this post is a first pass at a reusable structure:

1. a compact map capsule embed
2. a scrollytelling sequence that updates map state as you read

## Reusable map capsule

This map is rendered with a generic `map-embed` container and data attributes for center, zoom, marker, and route.

<div
  class="map-embed"
  data-center="28.5383,-81.3792"
  data-zoom="11"
  data-marker="28.5383,-81.3792"
  data-popup="Example focus area"
  data-route="28.527,-81.39;28.533,-81.372;28.545,-81.361;28.553,-81.374"
></div>

<p class="map-note">Capsule maps work well for one idea: a route, boundary, or focal point.</p>

## Scrollytelling walkthrough: field edit QA

A common workflow: inspect suspect edits, check nearby context, then lock in the final corrected location.

<div class="map-story" id="field-edit-story">
  <div
    class="map-embed"
    id="field-edit-map"
    data-center="28.5383,-81.3792"
    data-zoom="11"
  ></div>

  <div class="map-steps" id="field-edit-steps">
    <section class="map-step is-active" data-center="28.545,-81.39" data-zoom="12" tabindex="0">
      <h4>1) Review the incoming points</h4>
      <p>Start broad and inspect the newest field updates in context.</p>
    </section>

    <section class="map-step" data-center="28.533,-81.372" data-zoom="14" tabindex="0">
      <h4>2) Zoom to dense edits</h4>
      <p>Focus on clusters where a minor offset can impact routing quality.</p>
    </section>

    <section class="map-step" data-center="28.553,-81.374" data-zoom="15" tabindex="0">
      <h4>3) Confirm final corrected location</h4>
      <p>Move to the accepted location and verify alignment with nearby streets.</p>
    </section>
  </div>
</div>

<script>
(function () {
  function toLatLng(value, fallback) {
    if (!window.DanMapEmbed) return fallback;
    return window.DanMapEmbed.parseLatLng(value, fallback);
  }

  function setActive(steps, activeStep) {
    steps.forEach(function (step) {
      step.classList.toggle('is-active', step === activeStep);
    });
  }

  function initStory() {
    var mapEl = document.getElementById('field-edit-map');
    if (!mapEl || !window.DanMapEmbed) return;

    var embed = window.DanMapEmbed.create(mapEl, { routeColor: '#34d399' });
    if (!embed) return;

    var referenceRoute = L.polyline([
      [28.545, -81.39],
      [28.54, -81.381],
      [28.533, -81.372],
      [28.542, -81.365],
      [28.553, -81.374]
    ], { color: '#f59e0b', weight: 4, opacity: 0.85 }).addTo(embed.map);

    var steps = Array.from(document.querySelectorAll('#field-edit-steps .map-step'));

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var step = entry.target;
        var center = toLatLng(step.dataset.center, [28.5383, -81.3792]);
        var zoom = Number(step.dataset.zoom || 12);
        setActive(steps, step);
        embed.setView(center, zoom);
      });
    }, { threshold: 0.65 });

    steps.forEach(function (step) {
      observer.observe(step);
      step.addEventListener('focus', function () {
        var center = toLatLng(step.dataset.center, [28.5383, -81.3792]);
        var zoom = Number(step.dataset.zoom || 12);
        setActive(steps, step);
        embed.setView(center, zoom);
      });
    });

    if (referenceRoute.getBounds().isValid()) {
      embed.map.fitBounds(referenceRoute.getBounds(), { padding: [18, 18] });
    }
  }

  document.addEventListener('DOMContentLoaded', initStory);
})();
</script>

## Why this format is useful

- It keeps the post readable without sending readers to a separate app.
- It makes map state transitions explicit.
- It gives me a reusable pattern for future route, parcel, and QA writeups.

Next step is extending the same component for side-by-side compare maps and small decision matrix callouts.

