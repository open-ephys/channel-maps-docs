import csv
import xml.etree.ElementTree as ET
from pathlib import Path

def load_mapping(csv_path: Path) -> dict:
    """Load placeholder→new label mapping from a CSV with 2 rows."""
    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if len(rows) < 2:
        raise ValueError(f"{csv_path} must contain at least 2 rows (placeholders + new labels)")
    placeholders, new_labels = rows[0], rows[1]
    return dict(zip(placeholders, new_labels))

def apply_mapping(svg_path: Path, csv_path: Path, output_dir: Path):
    """Apply one CSV mapping to an SVG and save a new file."""
    tree = ET.parse(svg_path)
    root = tree.getroot()
    ns = {"svg": "http://www.w3.org/2000/svg"}

    mapping = load_mapping(csv_path)

    for text in root.findall(".//svg:text", ns):
        content = "".join(text.itertext()).strip()
        if content in mapping:
            text.text = mapping[content]

    output_dir.mkdir(parents=True, exist_ok=True)

    # Output filename is based on CSV stem
    out_name = f"{csv_path.stem}.svg"
    out_path = output_dir / out_name

    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"Updated {svg_path.name} with {csv_path.name} → {out_path}")

def main(root_dir: str, output_dir: str):
    root_dir = Path(root_dir)
    output_dir = Path(output_dir)

    csv_files = list(root_dir.rglob("*.csv"))

    for svg_path in root_dir.rglob("*.svg"):
        stem = svg_path.stem  # "xxx" from "xxx.svg"

        # Find CSVs whose stem ends with "-xxx"
        matching_csvs = [c for c in csv_files if c.stem.endswith(f"-{stem}")]
        if not matching_csvs:
            continue

        for csv_path in matching_csvs:
            apply_mapping(svg_path, csv_path, output_dir)

if __name__ == "__main__":
    # Example: process everything under current directory and write outputs to ./output
    main(root_dir=".", output_dir="./output")
