# Image Captioning Generation

Automatically generate descriptive sentences for images by combining Convolutional Neural Networks (CNNs) and Long Short-Term Memory (LSTM) networks.

This AI project was developed as part of the Data Mining course by Hoang Anh Thu and Nguyen Thuy Dung.

---

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Reference](#reference)
- [Suggest For Improvements](#suggest-for-improvements)
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

## Suggest For Improvements
- Data augmentation:
  - Horizontal flipping
  - Random cropping
  - Brightness adjustment
- Leakage prevention:
  - Split the dataset into train/validation/test before applying augmentation
  - Fit the tokenizer only on training captions
- BiLSTM → GRU:
  - Faster training and lower memory usage

For a detailed of the workflow, see: [SUGGEST_FOR_IMPROVEMENT.md](https://github.com/AnhThuHoang0518/Image-Captioning-Generation/blob/main/SUGGEST_FOR_IMPROVEMENT.md)

---

## Artifacts
- Our Code (Baseline): [icg.ipynb](https://github.com/AnhThuHoang0518/Image-Captioning-Generation/blob/main/icg.ipynb)
- Idea for Data Augmentation: [data_augmentation_eg.png](https://github.com/AnhThuHoang0518/Image-Captioning-Generation/blob/main/data_augmentation_eg.png)
- Model Architecture Suggestion: [model_suggestion.png](https://github.com/AnhThuHoang0518/Image-Captioning-Generation/blob/main/model_suggestion.png)

---

## How to Run
1. Clone this repository.
2. Open the provided notebooks in your preferred environment (e.g., Jupyter or Colab).
3. Download the Flickr8k dataset from Kaggle
4. Apply the proposed improvements to enable comparison with the baseline implementation.


## Results
- Our retrained model achieved slightly better performance compared to the reference implementation.
- Further improvement ideas have been proposed to enhance the model’s captioning capabilities even more.

---

## Acknowledgments
- Course: Data Mining
- Authors: Hoang Anh Thu and Nguyen Thuy Dung
