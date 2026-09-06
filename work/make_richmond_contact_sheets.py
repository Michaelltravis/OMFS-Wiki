from pathlib import Path
import re

from PIL import Image, ImageDraw


ROOT = Path(r"C:\Users\micha\Desktop\Wiki\work\richmond_qa_20260905\pdfium_pages_final4")
OUT = Path(r"C:\Users\micha\Desktop\Wiki\work\richmond_qa_20260905\contact_sheets_final4")


def page_number(path: Path) -> int:
    match = re.search(r"(\d+)$", path.stem)
    return int(match.group(1)) if match else 0


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for folder in sorted(path for path in ROOT.iterdir() if path.is_dir()):
        pages = sorted(folder.glob("page-*.png"), key=page_number)
        thumbs = []
        for page in pages:
            image = Image.open(page).convert("RGB")
            width = 820
            height = round(image.height * width / image.width)
            thumbs.append((page_number(page), image.resize((width, height))))
        cols = 2
        gutter = 28
        label_h = 34
        rows = (len(thumbs) + cols - 1) // cols
        cell_h = max(img.height for _, img in thumbs) + label_h
        sheet = Image.new("RGB", (cols * 820 + (cols + 1) * gutter, rows * cell_h + (rows + 1) * gutter), "#D8D8D8")
        draw = ImageDraw.Draw(sheet)
        for index, (number, image) in enumerate(thumbs):
            row, col = divmod(index, cols)
            x = gutter + col * (820 + gutter)
            y = gutter + row * cell_h
            draw.text((x, y), f"Page {number}", fill="black")
            sheet.paste(image, (x, y + label_h))
        out_path = OUT / f"{folder.name}_contact.png"
        sheet.save(out_path, optimize=True)
        print(out_path)


if __name__ == "__main__":
    main()
