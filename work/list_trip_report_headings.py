from pathlib import Path
from docx import Document


ROOT = Path(r"C:\Users\micha\Downloads\OneDrive_2026-09-05\Completed Trip Reports")

for path in sorted(ROOT.rglob("*.docx")):
    if "mack" in path.name.lower() or path.name.startswith("~$"):
        continue
    print(f"\n===== {path.name} =====")
    doc = Document(path)
    for p in doc.paragraphs:
        text = p.text.strip()
        style = p.style.name if p.style else ""
        if text and ("heading" in style.lower() or text.lower().startswith((
            "overall observations",
            "notable risks",
            "notable opportunities",
            "items to consider",
            "additional notes",
            "pre-visit due diligence",
            "network and cybersecurity",
            "strategic risks",
            "recommended actions",
            "housekeeping",
        ))):
            print(f"{style}: {text}")
