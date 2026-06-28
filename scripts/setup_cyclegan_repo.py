from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT / "pytorch-CycleGAN-and-pix2pix"
URL = "https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix.git"

if REPO.exists():
    print("Repository already exists:", REPO)
    sys.exit(0)

print("Cloning official CycleGAN/pix2pix repository...")
subprocess.run(["git", "clone", URL, str(REPO)], check=True)
print("Done:", REPO)
print("Next: python scripts/download_dataset.py --dataset horse2zebra")
