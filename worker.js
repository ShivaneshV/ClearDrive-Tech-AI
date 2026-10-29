export default {
  async fetch(request, env, ctx) {
    let backend = env.BACKEND_URL || "https://footage-inputs-decrease-smart.trycloudflare.com";

    // 1. Dynamically read active live tunnel URL from GitHub
    try {
      const res = await fetch("https://raw.githubusercontent.com/ShivaneshV/ClearDrive-Tech-AI/main/tunnel_url.txt?t=" + Date.now(), {
        headers: { "User-Agent": "ClearDriveWorker/1.0" },
        cf: { cacheTtl: 0 }
      });
      if (res.ok) {
        const text = (await res.text()).trim();
        if (text.startsWith("https://")) {
          backend = text;
        }
      }
    } catch (e) {
      // Fall back to default backend URL
    }

    const url = new URL(request.url);
    const targetUrl = new URL(url.pathname + url.search, backend);

    const newHeaders = new Headers(request.headers);
    try {
      newHeaders.set("Host", new URL(backend).host);
      newHeaders.set("X-Forwarded-Host", url.host);
    } catch (e) {}

    const reqInit = {
      method: request.method,
      headers: newHeaders,
      redirect: "follow"
    };

    if (request.method !== "GET" && request.method !== "HEAD" && request.body) {
      reqInit.body = request.body;
      reqInit.duplex = "half";
    }

    try {
      const response = await fetch(targetUrl.toString(), reqInit);
      // Catch DNS errors (Cloudflare 530 / Error 1016) or offline backend gateways
      if (response.status >= 500 || response.status === 530) {
        throw new Error("Backend offline or tunnel expired");
      }
      return response;
    } catch (err) {
      // Graceful Cockpit Standby Card if local live tunnel is currently paused
      const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ClearDrive AI - Cloudflare Edge Gateway</title>
  <style>
    body { background: #070b14; color: #e2e8f0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; display: flex; align-items: center; justify-content: center; min-height: 100vh; margin: 0; padding: 20px; }
    .card { background: #0f172a; border: 1px solid #1e293b; border-radius: 16px; padding: 36px; max-width: 600px; width: 100%; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5); }
    .title { color: #38bdf8; font-size: 24px; font-weight: 800; margin: 0 0 8px 0; letter-spacing: -0.5px; }
    .badge { display: inline-block; background: #0284c7; color: white; padding: 4px 10px; border-radius: 9999px; font-size: 11px; font-weight: 700; text-transform: uppercase; margin-bottom: 20px; }
    .status-box { background: #1e293b; border-left: 4px solid #38bdf8; padding: 14px 18px; border-radius: 0 8px 8px 0; margin-bottom: 24px; }
    .status-text { font-size: 14px; color: #cbd5e1; margin: 0; }
    .instructions { font-size: 14px; color: #94a3b8; line-height: 1.6; }
    code { background: #070b14; padding: 3px 8px; border-radius: 4px; color: #7dd3fc; font-family: monospace; font-size: 13px; }
    .features { list-style: none; padding: 0; margin: 20px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
    .feature-item { background: #141e33; padding: 10px; border-radius: 8px; font-size: 12px; color: #93c5fd; border: 1px solid #1e3a5f; }
  </style>
</head>
<body>
  <div class="card">
    <div class="badge">Cloudflare Edge Gateway</div>
    <h1 class="title">🚗 ClearDrive AI Omni-Vision Cockpit</h1>
    <div class="status-box">
      <p class="status-text">⚡ <strong>Edge Gateway Active:</strong> Ready to connect to live automotive vision stream.</p>
    </div>
    <p class="instructions">To connect this permanent Cloudflare URL to the live workstation with hardware webcams and sub-50ms glass-to-glass perception:</p>
    <p class="instructions">Run <code>.\\Launch_Cloudflare_Live.bat</code> in your ClearDrive directory.</p>
    <div class="features">
      <div class="feature-item">✓ Nebius Token Factory Bridge</div>
      <div class="feature-item">✓ NVIDIA Nemotron-3.5 VL</div>
      <div class="feature-item">✓ 3-Camera Live Selector</div>
      <div class="feature-item">✓ 8-Mode HUD Visual Matrix</div>
    </div>
  </div>
</body>
</html>`;
      return new Response(html, {
        status: 200,
        headers: { "Content-Type": "text/html; charset=utf-8" }
      });
    }
  }
};
