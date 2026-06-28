
# CycleGAN Real Data Project

A PyTorch implementation of CycleGAN for unpaired image-to-image translation — learning visual transformations between two image domains without requiring matched training pairs.

## Problem Solved

Collecting paired image datasets is often impractical. You may have two visually distinct collections of images, but no exact before-and-after correspondence between them.

CycleGAN solves this by learning the mapping between two domains using **unpaired data** — it understands the structural and stylistic differences between the datasets and transfers appearance while preserving content.

## Technical Overview

The model is built around two generator–discriminator pairs trained simultaneously:

- **Generator A→B** learns to translate images from Domain A into the style of Domain B
- **Generator B→A** learns the reverse mapping
- **Discriminators** evaluate whether generated images are indistinguishable from real ones in each domain

Training is governed by three losses:

| Loss | Purpose |
|---|---|
| Adversarial | Generated images should look realistic to the discriminator |
| Cycle consistency | Translating A→B→A should recover the original image |
| Identity | Passing a Domain B image through Generator A→B should leave it unchanged |

This combination allows the model to learn meaningful visual translations without pixel-level supervision.

## Project Structure

    A[Raw Image Datasets] --> B[Dataset Preparation]

    B --> C[Domain A\ntrainA / testA]
    B --> D[Domain B\ntrainB / testB]

    C --> E[CycleGAN Model]
    D --> E

    E --> F[Generator A→B]
    E --> G[Generator B→A]
    E --> H[Discriminator A]
    E --> I[Discriminator B]

    F --> J[Generated Domain B Images]
    G --> K[Generated Domain A Images]

    J --> L[Result Visualisation & Analysis]
    K --> L


## Repository Layout

cyclegan-realdata-project/
├── data/              # Raw input images
├── datasets/          # Prepared train/test splits per domain
├── models/            # Generator and discriminator architectures
├── options/           # Training and testing configuration
├── scripts/           # Helper and preprocessing scripts
├── util/              # Visualisation and utility functions
├── checkpoints/       # Saved model weights
└── results/           # Generated output images

Each dataset follows the structure:

datasets/<name>/
├── trainA/
├── trainB/
├── testA/
└── testB/
