# Real-Data CycleGAN Project

This project uses the official PyTorch CycleGAN/pix2pix GitHub repository and real image datasets such as `horse2zebra`.

The full CycleGAN repository, pretrained weights, and datasets are **not included inside this zip** because they are large. The scripts in `scripts/` clone/download them for you.

## Setup in VS Code

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

On Mac/Linux:

```bash
source .venv/bin/activate
```

## Clone official repo

```bash
python scripts/setup_cyclegan_repo.py
```

## Download real dataset

```bash
python scripts/download_dataset.py horse2zebra
```

## Option 1: test pretrained model

```bash
python scripts/test_cyclegan.py horse2zebra
```

## Option 2: train on real images

```bash
python scripts/train_cyclegan.py horse2zebra
```

## Outputs

CycleGAN writes generated images and HTML result pages inside the cloned repository's `results/` folder.

## Resume wording

You can say you reproduced the official PyTorch CycleGAN/pix2pix pipeline using the real `horse2zebra` dataset after running the official dataset download script.
