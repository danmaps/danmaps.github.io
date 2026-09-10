// Same-origin, source-checked resize messages. No global map state.
(() => {
  const frames = [...document.querySelectorAll("iframe[data-tinygis]")];
  window.addEventListener("message", (event) => {
    if (
      event.origin !== window.location.origin ||
      event.data?.type !== "tinygis:height"
    )
      return;
    const frame = frames.find((item) => item.contentWindow === event.source);
    const height = event.data.height;
    if (!frame || !Number.isFinite(height) || height < 100 || height > 4000)
      return;
    frame.style.height = `${Math.ceil(height) + 4}px`;
  });
})();
