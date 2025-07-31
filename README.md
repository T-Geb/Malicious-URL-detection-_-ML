# Malicious URL Detection Tool - Using Machine Learning
> Created for the Computer Science Capstone at Western Governors University (WGU).

## About
This project is a machine learning-based URL classification tool that predicts the safety of URLS. It identifies threats such as phishing, defacement, and malware using structural and text-based URL features.

## Features

- Classifies URLs into four categories: benign, phishing, defacement, or malware

## Usage

The tool runs in a Jupyter notebook and includes a simple input form for entering a URL or selecting from a sample list.

## Dataset

- Source: [Malicious URLs Dataset on Kaggle](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)
- A trimmed version of the dataset is used in this project

## Custom Feature Engineering

- Manually extracted features to identify structural patterns in URLs

## Model Selection

Three classification models were tested:
- Random Forest
- HistGradientBoosting
- Logistic Regression

The final model was Random Forest, chosen for its overall accuracy and balanced performance across all URL classes.

##  Run in Google Colab
- [Click here to access the notebook in Google Colab](https://colab.research.google.com/drive/1HjcVR8857J4YFjuRF7JmNzJgZcLJoqk2?usp=sharing) to test the tool.
- Click Runtime > Run all to execute the notebook.
- The input form appears near the bottom.