from pathlib import Path
from pypdf import PdfReader


PDF = Path(r"C:\Users\micha\Desktop\Richmond\20260803150224418 FINAL_City of Richmond RFP-8-3-26.pdf")
reader = PdfReader(PDF)

for index in range(len(reader.pages)):
    text = reader.pages[index].extract_text() or ""
    if index in {7, 27} or any(term in text for term in (
        "12-point",
        "12 point",
        "corrective maintenance",
        "less than $5,000",
        "exceeding $5,000",
        "December 31",
        "June 1",
        "June 30",
        "30 days after the renewal",
        "screenings and grit",
        "stormwater debris",
        "sodium bisulfate",
        "blockage",
        "owned equipment",
    )):
        print(f"\n===== PDF PAGE {index + 1} =====\n")
        print(text)
