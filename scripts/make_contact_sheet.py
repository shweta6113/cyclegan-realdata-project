from pathlib import Path
import argparse
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT / "pytorch-CycleGAN-and-pix2pix"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="horse2zebra_demo")
parser.add_argument("--phase", default="test_latest")
parser.add_argument("--max-rows", type=int, default=8)
parser.add_argument("--image-size", type=int, default=160)
args = parser.parse_args()

images_dir = REPO / "results" / args.name / args.phase / "images"
if not images_dir.exists():
    raise SystemExit(f"Images folder not found: {images_dir}\nRun testing first.")

# Match common CycleGAN output names by stem prefix.
real_A_files = sorted(images_dir.glob("*real_A*"))[:args.max_rows]
if not real_A_files:
    raise SystemExit("No real_A images found. Check results folder.")

columns = ["real_A", "fake_B", "rec_A", "real_B", "fake_A", "rec_B"]
cell = args.image_size
label_h = 24
sheet = Image.new("RGB", (cell*len(columns), (cell+label_h)*(len(real_A_files)+1)), "white")
draw = ImageDraw.Draw(sheet)

for c, label in enumerate(columns):
    draw.text((c*cell + 8, 5), label, fill=(0, 0, 0))

for r, real_A in enumerate(real_A_files):
    base = real_A.name.replace("real_A", "{}")
    for c, label in enumerate(columns):
        candidate = images_dir / base.format(label)
        if not candidate.exists():
            continue
        img = Image.open(candidate).convert("RGB")
        img.thumbnail((cell, cell))
        x = c*cell + (cell-img.width)//2
        y = (r+1)*(cell+label_h) + (cell-img.height)//2
        sheet.paste(img, (x, y))

out_path = OUT / f"contact_sheet_{args.name}.jpg"
sheet.save(out_path, quality=95)
print("Saved:", out_path)
