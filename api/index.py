import os
import sys

# Crucial AWS Lambda / Vercel Serverless environment fixes for Read-Only Filesystem
os.environ["YOLO_CONFIG_DIR"] = "/tmp/Ultralytics"
os.environ["ULTRALYTICS_CONFIG_DIR"] = "/tmp/Ultralytics"
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib"
os.environ["TORCH_HOME"] = "/tmp/torch"
os.environ["HOME"] = "/tmp"
os.environ["XDG_CONFIG_HOME"] = "/tmp"
os.environ["XDG_CACHE_HOME"] = "/tmp"

# Add project root directory to sys.path so app, engine, dehaze, etc. are importable
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

try:
    os.chdir(ROOT_DIR)
except Exception:
    pass

# Graceful fallback for optional media libraries in headless serverless environments
try:
    import mediapipe
except Exception:
    import types
    sys.modules['mediapipe'] = types.ModuleType('mediapipe')
    sys.modules['mediapipe.tasks'] = types.ModuleType('mediapipe.tasks')
    sys.modules['mediapipe.tasks.python'] = types.ModuleType('mediapipe.tasks.python')
    sys.modules['mediapipe.tasks.python.vision'] = types.ModuleType('mediapipe.tasks.python.vision')

# Expose Flask WSGI application instance with diagnostic error boundary
try:
    from app import app
    # Explicitly wire templates and static assets relative to root directory
    app.template_folder = os.path.join(ROOT_DIR, "templates")
    app.static_folder = os.path.join(ROOT_DIR, "static")
except Exception as _init_err:
    import traceback
    _init_tb = traceback.format_exc()
    print(f"[ClearDrive Serverless Startup Error]:\n{_init_tb}")
    from flask import Flask, make_response
    app = Flask(__name__)
    
    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def _serverless_diagnostic(path):
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>ClearDrive AI - Serverless Diagnostic</title>
  <style>
    body {{ background: #0b0f19; color: #e2e8f0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, monospace; padding: 40px 20px; max-width: 900px; margin: 0 auto; }}
    h1 {{ color: #38bdf8; font-size: 24px; margin-bottom: 8px; }}
    .badge {{ display: inline-block; background: #dc2626; color: white; padding: 4px 10px; border-radius: 4px; font-size: 12px; font-weight: bold; margin-bottom: 20px; }}
    pre {{ background: #1e293b; padding: 20px; border-radius: 8px; color: #fca5a5; font-size: 13px; line-height: 1.5; overflow-x: auto; border: 1px solid #334155; }}
    .info {{ color: #94a3b8; font-size: 14px; margin-top: 20px; line-height: 1.6; }}
    .footer {{ margin-top: 30px; border-top: 1px solid #1e293b; padding-top: 15px; color: #64748b; font-size: 12px; }}
  </style>
</head>
<body>
  <h1>🚗 ClearDrive AI : Omni-Vision Edge Platform</h1>
  <div class="badge">SERVERLESS COLD START DIAGNOSTIC</div>
  <p class="info">The serverless container encountered an initialization exception during module import:</p>
  <pre>{_init_tb}</pre>
  <p class="info">
    💡 <strong>Hackathon Live Note:</strong> Hardware dashcam inputs (USB Port 1, Laptop Cam, Mobile Cam) require local DirectShow drivers. For full 30 FPS glass-to-glass demonstration with judges, launch <code>.\\Launch_Cloudflare_Live.bat</code>.
  </p>
  <div class="footer">ClearDrive AI · Powered by Nebius AI Studio & NVIDIA Nemotron</div>
</body>
</html>"""
        return make_response(html, 200)
