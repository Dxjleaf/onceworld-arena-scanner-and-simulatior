import numpy as np

# ============================================================
# End-user config for arena detection
# ============================================================
# Edit this file only.
# - Tesseract override is optional.

# Optional OCR override.
# If Tesseract is already in PATH, keep this as None.
# Example:
# TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
TESSERACT_CMD = None

# Anchor multi-scale search
# Scale multipliers for anchor template matching.
# Wider range = more robust to emulator/window size changes, but slower.
# Narrower range = faster, but can miss anchors if UI scale changes.
ANCHOR_SCALES = np.linspace(0.75, 1.35, 13)

# Detection thresholds
# Minimum template-match score to accept an anchor hit.
# Raise to reduce false anchors; lower if anchors are missed.
ANCHOR_THRESHOLD = 0.72
