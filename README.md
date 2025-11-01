# Image-Captioning-Generation

### This AI project was developed as part of the Data Mining course by Hoang Anh Thu and Nguyen Thuy Dung 

## The goal of this project is to build an image captioning model that automatically generates descriptive sentences for images by combining Convolutional Neural Networks (CNNs) and Long Short-Term Memory (LSTM) networks.

# 🚀 Project Results

## Final Code (Improved Process): <insert link>
Includes data augmentation (flipping, cropping, brightness adjustment) to improve model generalization and prevent overfitting
Also implements an updated workflow to avoid data leakage by splitting the dataset before augmentation and fitting the tokenizer only on training captions
Overview of the update process: https://github.com/AnhThuHoang0518/Image-Captioning-Generation/blob/main/PIPELINE_RESTRUCTURE.md

## Original Code (Baseline): (https://github.com/AnhThuHoang0518/Image-Captioning-Generation/blob/main/baseline.ipynb)
Early version of the pipeline without data augmentation or structural improvements

# Reference
This project was inspired by the Image Captioning tutorial on: https://github.com/Sajid030/image-caption-generator/blob/master/image-captioner.ipynb
