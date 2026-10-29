import os
import sys

# Add project root directory to sys.path so app, engine, dehaze, etc. are importable
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Expose Flask WSGI application instance for Vercel Serverless Function runtime
from app import app
