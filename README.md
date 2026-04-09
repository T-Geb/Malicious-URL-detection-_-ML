# Malicious URL Detection Tool - Using Machine Learning

## About

This project is a machine learning-based URL classification tool that predicts the safety of URLs, classifying them as:

- Benign
- Phishing
- Defacement
- Malware

Exploratory data analysis was performed to identify meaningful signals in raw URL strings, which were then transformed into structural and lexical features for model training.

## Dataset

- Source: [Malicious URLs Dataset on Kaggle](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)
- A trimmed version of the dataset is used after identifying and removing a mislabeled portion of the original data sourced from PhishStorm, where phishing and benign labels were mistakenly swapped.

## Manual Feature Engineering

Features were manually extracted to capture structural patterns in URLs, targeting length and character characteristics, HTTPS and domain properties, and suspicious keyword patterns.

## Model Selection

Three classification models were trained and evaluated:

- Random Forest
- HistGradientBoosting
- Logistic Regression

Random Forest was selected as the final model based on its overall accuracy and balanced performance across all four URL classes.

## Setup Instructions To Run In Local Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 src/main.py
```

