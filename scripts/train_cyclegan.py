from pathlib import Path
import argparse
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT / "pytorch-CycleGAN-and-pix2pix"

parser = argparse.ArgumentParser()
parser.add_argument("--dataset", default="horse2zebra")
parser.add_argument("--name", default="horse2zebra_demo")
parser.add_argument("--epochs", type=int, default=5, help="Small demo: 1-5. Serious run: 100+")
parser.add_argument("--batch-size", type=int, default=1)
parser.add_argument("--gpu-ids", default="-1", help="Use -1 for CPU, 0 for first GPU")
args = parser.parse_args()

if not REPO.exists():
    raise SystemExit("Repo not found. First run: python scripts/setup_cyclegan_repo.py")

dataroot = f"./datasets/{args.dataset}"
cmd = [
    sys.executable, "train.py",
    "--dataroot", dataroot,
    "--name", args.name,
    "--model", "cycle_gan",
    "--batch_size", str(args.batch_size),
    "--n_epochs", str(args.epochs),
    "--n_epochs_decay", "0",
    "--display_id", "-1",
    "--gpu_ids", args.gpu_ids,
]

print("Running:")
print(" ".join(cmd))
subprocess.run(cmd, cwd=REPO, check=True)
print("Training finished.")
