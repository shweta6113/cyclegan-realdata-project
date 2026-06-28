from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT / "pytorch-CycleGAN-and-pix2pix"

parser = argparse.ArgumentParser()
parser.add_argument("--dataset", default="horse2zebra")
args = parser.parse_args()

path = REPO / "datasets" / args.dataset
if not path.exists():
    raise SystemExit(f"Dataset folder not found: {path}\nRun: python scripts/download_dataset.py --dataset {args.dataset}")

print("Dataset folder:", path)
for sub in ["trainA", "trainB", "testA", "testB"]:
    folder = path / sub
    count = len(list(folder.glob("*"))) if folder.exists() else 0
    print(f"{sub:7s}: {'FOUND' if folder.exists() else 'MISSING'} | files: {count}")
