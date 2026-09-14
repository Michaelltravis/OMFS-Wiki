"""Render the flagged pages from a coverage.json report to 300-DPI PNGs, so
Stage 1 page-repair agents have a visual reference even though pdf_to_verbatim.py
only auto-renders image-only pages (renders/ is otherwise empty for text pages).

Usage:
    python work/render_flagged_pages.py raw/<file>.pdf <slug> verbatim/<slug>/coverage.json

Writes verbatim/<slug>/renders/pNNNN.png for every page coverage.json marks flagged.
Safe to re-run after a repair pass with a fresh coverage.json (only renders
whatever is still flagged at that point).
"""
import sys, json, os
import fitz

pdf_path = sys.argv[1]
slug = sys.argv[2]
pages_json = sys.argv[3]  # verbatim/<slug>/coverage.json

with open(pages_json, 'r', encoding='utf-8') as f:
    cov = json.load(f)

flagged = [p['page'] for p in cov['per_page'] if p.get('flagged')]
doc = fitz.open(pdf_path)
out_dir = os.path.join('verbatim', slug, 'renders')
os.makedirs(out_dir, exist_ok=True)
zoom = 300 / 72
mat = fitz.Matrix(zoom, zoom)
for pno in flagged:
    page = doc[pno - 1]
    pix = page.get_pixmap(matrix=mat)
    render_path = os.path.join(out_dir, f"p{pno:04d}.png")
    pix.save(render_path)
print(f"rendered {len(flagged)} pages to {out_dir}")
