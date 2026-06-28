from pathlib import Path
import argparse
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT / "pytorch-CycleGAN-and-pix2pix"

parser = argparse.ArgumentParser()
parser.add_argument("--dataset", default="horse2zebra", help="Example: horse2zebra, apple2orange, summer2winter_yosemite")
args = parser.parse_args()

if not REPO.exists():
    raise SystemExit("Repo not found. First run: python scripts/setup_cyclegan_repo.py")

script = REPO / "datasets" / "download_cyclegan_dataset.sh"
if not script.exists():
    raise SystemExit("Dataset download script not found in official repo.")

if sys.platform.startswith("win"):
    print("On Windows, this script requires Git Bash or WSL for the .sh downloader.")
    print("Trying through bash. If this fails, open Git Bash and run:")
    print(f"cd {REPO.as_posix()} && bash ./datasets/download_cyclegan_dataset.sh {args.dataset}")
    subprocess.run(["bash", str(script), args.dataset], cwd=REPO, check=True)
else:
    subprocess.run(["bash", str(script), args.dataset], cwd=REPO, check=True)

print("Dataset download complete.")
