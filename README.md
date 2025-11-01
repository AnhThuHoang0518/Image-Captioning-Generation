# Image Captioning Generation

Automatically generate descriptive sentences for images by combining Convolutional Neural Networks (CNNs) and Long Short-Term Memory (LSTM) networks.

This AI project was developed as part of the Data Mining course by Hoang Anh Thu and Nguyen Thuy Dung.

---

## Table of Contents
- [Overview](#overview)
- [Reference](#reference)
- [Key Improvements](#key-improvements)
- [Artifacts](#artifacts)
- [How to Run](#how-to-run)
- [Results](#results)
- [Acknowledgments](#acknowledgments)

---

## Overview
The goal of this project is to build an image captioning model that learns visual features from images and generates natural-language descriptions. The approach follows an encoder–decoder paradigm:
- A CNN encoder extracts high-level visual representations.
- An LSTM decoder generates captions token by token from the encoded features.

This repository includes both a baseline implementation and an improved training pipeline designed to enhance generalization and prevent data leakage.

---

## Reference
This project was inspired by the Image Captioning tutorial:
- [Image Caption Generator Tutorial](https://github.com/Sajid030/image-caption-generator/blob/master/image-captioner.ipynb)

---

## Key Improvements
The improved process introduces stronger training hygiene and generalization:
- Data augmentation:
  - Horizontal flipping
  - Random cropping
  - Brightness adjustment
- Leakage prevention:
  - Split the dataset into train/validation/test before applying augmentation
  - Fit the tokenizer only on training captions

For a detailed walkthrough of the updated workflow, see:
- Overview of the update process: [PIPELINE_RESTRUCTURE.md](https://github.com/AnhThuHoang0518/Image-Captioning-Generation/blob/main/PIPELINE_RESTRUCTURE.md)

---

## Artifacts
- Updated Pipeline (Improved Process): See [Pipeline Restructure](https://github.com/AnhThuHoang0518/Image-Captioning-Generation/blob/main/PIPELINE_RESTRUCTURE.md)
- Original Code (Baseline): [baseline.ipynb](https://github.com/AnhThuHoang0518/Image-Captioning-Generation/blob/main/baseline.ipynb)

---

## How to Run
1. Clone this repository.
2. Open the provided notebooks in your preferred environment (e.g., Jupyter or Colab).
3. Follow the instructions within the notebooks and in [PIPELINE_RESTRUCTURE.md](https://github.com/AnhThuHoang0518/Image-Captioning-Generation/blob/main/PIPELINE_RESTRUCTURE.md) for data preparation, training, and evaluation.
4. Review generated captions and compare baseline vs. improved pipeline behavior.


---

## Results
- The improved pipeline leverages data augmentation and strict dataset splitting to enhance robustness and avoid leakage.
- Qualitative examples and comparisons are available within the slide and notebooks.

---

## Acknowledgments
- Course: Data Mining
- Authors: Hoang Anh Thu and Nguyen Thuy Dung
