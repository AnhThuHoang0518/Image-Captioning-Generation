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

## Key Improvements cần chuyển thành Suggest For Improvements
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
- Our Code (Baseline): [baseline.ipynb](https://github.com/AnhThuHoang0518/Image-Captioning-Generation/blob/main/baseline.ipynb)

---

## How to Run
1. Clone this repository.
2. Open the provided notebooks in your preferred environment (e.g., Jupyter or Colab).
3. Download the Flickr8k dataset from Kaggle
4. Có thể tiếp tục làm Improvements để compare vs baseline


## Results
- Code của chúng tôi có kết quả tốt hơn so với reference 1 chút khi train lại model.
- Có ý tưởng để làm thêm improvement để cải thiện capabilities hơn nx

---

## Acknowledgments
- Course: Data Mining
- Authors: Hoang Anh Thu and Nguyen Thuy Dung
