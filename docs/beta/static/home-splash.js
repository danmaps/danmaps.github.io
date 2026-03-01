(() => {
  const body = document.body;
  if (!body || !body.classList.contains('home')) {
    return;
  }

  const canvas = document.getElementById('home-splash');
  if (!canvas) {
    return;
  }

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (prefersReducedMotion.matches) {
    canvas.style.opacity = '0.15';
    return;
  }

  const gl = canvas.getContext('webgl', { alpha: true, antialias: true });
  if (!gl) {
    canvas.style.opacity = '0.25';
    return;
  }

  const vertexShaderSource = `
    attribute vec2 position;
    varying vec2 vUv;
    void main() {
      vUv = position * 0.5 + 0.5;
      gl_Position = vec4(position, 0.0, 1.0);
    }
  `;

  const fragmentShaderSource = `
    precision mediump float;
    uniform vec2 u_resolution;
    uniform float u_time;
    uniform vec2 u_mouse;
    uniform float u_intensity;
    varying vec2 vUv;

    float noise(vec2 p) {
      return sin(p.x) * sin(p.y);
    }

    void main() {
      vec2 uv = (gl_FragCoord.xy / u_resolution.xy) * 2.0 - 1.0;
      float time = u_time * 0.3;

      float angle = atan(uv.y, uv.x);
      float radius = length(uv);

      float swirl = sin(3.0 * angle + time) + cos(6.0 * radius - time * 2.0);
      float waves = noise(uv * 4.0 + time) + noise(uv * 2.0 - time * 0.5);

      float combined = swirl * 0.6 + waves * 0.4;
      combined += (u_mouse.x - 0.5) * 0.5;

      vec3 color = vec3(
        0.15 + 0.55 * sin(combined + 0.0 + u_mouse.x),
        0.2 + 0.45 * sin(combined + 2.0 + u_mouse.y),
        0.3 + 0.55 * cos(combined + 4.0 - u_mouse.x)
      );

      float vignette = smoothstep(1.35, 0.15, radius);
      float depthMask = smoothstep(0.0, 0.5, vUv.y) * 0.8 + 0.2;

      vec3 finalColor = color * vignette * depthMask * u_intensity;
      float alpha = vignette * 0.65;

      gl_FragColor = vec4(finalColor, alpha);
    }
  `;

  function compileShader(type, source) {
    const shader = gl.createShader(type);
    gl.shaderSource(shader, source);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
      console.error(gl.getShaderInfoLog(shader));
      gl.deleteShader(shader);
      return null;
    }
    return shader;
  }

  function createProgram(vertexShader, fragmentShader) {
    const program = gl.createProgram();
    gl.attachShader(program, vertexShader);
    gl.attachShader(program, fragmentShader);
    gl.linkProgram(program);
    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
      console.error(gl.getProgramInfoLog(program));
      gl.deleteProgram(program);
      return null;
    }
    return program;
  }

  const vertexShader = compileShader(gl.VERTEX_SHADER, vertexShaderSource);
  const fragmentShader = compileShader(gl.FRAGMENT_SHADER, fragmentShaderSource);

  if (!vertexShader || !fragmentShader) {
    canvas.style.opacity = '0.2';
    return;
  }

  const program = createProgram(vertexShader, fragmentShader);
  if (!program) {
    canvas.style.opacity = '0.2';
    return;
  }

  const positionLocation = gl.getAttribLocation(program, 'position');
  const resolutionLocation = gl.getUniformLocation(program, 'u_resolution');
  const timeLocation = gl.getUniformLocation(program, 'u_time');
  const mouseLocation = gl.getUniformLocation(program, 'u_mouse');
  const intensityLocation = gl.getUniformLocation(program, 'u_intensity');

  const positionBuffer = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
  gl.bufferData(
    gl.ARRAY_BUFFER,
    new Float32Array([
      -1, -1,
      1, -1,
      -1, 1,
      -1, 1,
      1, -1,
      1, 1
    ]),
    gl.STATIC_DRAW
  );

  const mouse = { x: 0.5, y: 0.5 };
  window.addEventListener('pointermove', (event) => {
    mouse.x = event.clientX / window.innerWidth;
    mouse.y = 1 - event.clientY / window.innerHeight;
  });

  function resizeCanvas() {
    const dpr = window.devicePixelRatio || 1;
    const displayWidth = Math.floor(window.innerWidth * dpr);
    const displayHeight = Math.floor(window.innerHeight * dpr);

    if (canvas.width !== displayWidth || canvas.height !== displayHeight) {
      canvas.width = displayWidth;
      canvas.height = displayHeight;
    }
  }

  window.addEventListener('resize', resizeCanvas, { passive: true });
  resizeCanvas();

  let rafId = null;
  let startTime = performance.now();

  function drawFrame(now) {
    resizeCanvas();
    gl.viewport(0, 0, gl.canvas.width, gl.canvas.height);

    gl.useProgram(program);
    gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
    gl.enableVertexAttribArray(positionLocation);
    gl.vertexAttribPointer(positionLocation, 2, gl.FLOAT, false, 0, 0);

    gl.uniform2f(resolutionLocation, gl.canvas.width, gl.canvas.height);
    gl.uniform1f(timeLocation, (now - startTime) * 0.001);
    gl.uniform2f(mouseLocation, mouse.x, mouse.y);
    gl.uniform1f(intensityLocation, 0.75);

    gl.drawArrays(gl.TRIANGLES, 0, 6);

    rafId = requestAnimationFrame(drawFrame);
  }

  function start() {
    if (rafId === null) {
      startTime = performance.now();
      rafId = requestAnimationFrame(drawFrame);
    }
  }

  function stop() {
    if (rafId !== null) {
      cancelAnimationFrame(rafId);
      rafId = null;
    }
  }

  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      stop();
    } else if (!prefersReducedMotion.matches) {
      start();
    }
  });

  const motionListener = (event) => {
    if (event.matches) {
      stop();
      canvas.style.opacity = '0.15';
    } else {
      canvas.style.opacity = '0.55';
      start();
    }
  };

  if (prefersReducedMotion.addEventListener) {
    prefersReducedMotion.addEventListener('change', motionListener);
  } else if (prefersReducedMotion.addListener) {
    prefersReducedMotion.addListener(motionListener);
  }

  start();
})();
