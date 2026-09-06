from pathlib import Path

import pypdfium2 as pdfium


PDF_DIR = Path(r"C:\Users\micha\Desktop\Wiki\work\richmond_qa_20260905\pdf")
OUT_DIR = Path(r"C:\Users\micha\Desktop\Wiki\work\richmond_qa_20260905\pdfium_pages_final4")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for pdf_path in sorted(PDF_DIR.glob("*.pdf")):
        target = OUT_DIR / pdf_path.stem
        target.mkdir(parents=True, exist_ok=True)
        document = pdfium.PdfDocument(str(pdf_path))
        for index, page in enumerate(document):
            image = page.render(scale=2.0).to_pil()
            image.save(target / f"page-{index + 1}.png")
        print(f"RENDERED\t{pdf_path.name}\tpages={len(document)}")


if __name__ == "__main__":
    main()
