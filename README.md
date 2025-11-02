# Image Captioning Generation

Automatically generate descriptive sentences for images by combining Convolutional Neural Networks (CNNs) and Long Short-Term Memory (LSTM) networks.

This AI project was developed as part of the Data Mining course by Hoang Anh Thu and Nguyen Thuy Dung.

---

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
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

## Dataset
We use the Flickr8k dataset:
- Flickr8k dataset (Kaggle): [https://www.kaggle.com/datasets/adityajn105/flickr8k](https://www.kaggle.com/datasets/adityajn105/flickr8k)

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
- Updated Pipeline (Improved Process): [final_22_en.ipynb](https://github.com/AnhThuHoang0518/Image-Captioning-Generation/blob/main/final_22_en.ipynb)
- Original Code (Baseline): [baseline.ipynb](https://github.com/AnhThuHoang0518/Image-Captioning-Generation/blob/main/baseline.ipynb)

---

## How to Run
1. Clone this repository.
2. Open the provided notebooks in your preferred environment (e.g., Jupyter or Colab).
3. Download the Flickr8k dataset from Kaggle and follow the instructions within the notebooks and in [PIPELINE_RESTRUCTURE.md](https://github.com/AnhThuHoang0518/Image-Captioning-Generation/blob/main/PIPELINE_RESTRUCTURE.md) for data preparation.
4. Review generated captions and compare baseline vs. improved pipeline behavior.

---

## Translate Vietnamese to English (Notebooks)

This repository includes a tool to translate Vietnamese text in Jupyter notebooks to English. The tool translates markdown cells, comments, and docstrings while preserving the executable code logic.

### Installation

For better translation quality (optional):
```bash
pip install deep-translator
```

The script works without `deep-translator` by using a fallback dictionary, but translation quality will be limited to common ML/development terms.

### Usage

To translate a notebook:
```bash
python tools/translate_vi_en_notebook.py <input.ipynb> <output.ipynb>
```

Example:
```bash
python tools/translate_vi_en_notebook.py final_22.ipynb final_22_en.ipynb
```

### Notes

- The script translates markdown cells, comments (lines starting with `#`), and docstrings only.
- Code logic and executable statements remain unchanged.
- Identifier renaming uses a small safe mapping and should be extended cautiously if needed.
- When `deep-translator` is installed, the tool uses Google Translate for higher quality translations.
- Without `deep-translator`, the tool falls back to a built-in dictionary covering common ML and development terms.

---

## Results
- The improved pipeline leverages data augmentation and strict dataset splitting to enhance robustness and avoid leakage.
- Qualitative examples and comparisons are available within the slide and notebooks.

---

## Acknowledgments
- Course: Data Mining
- Authors: Hoang Anh Thu and Nguyen Thuy Dung
