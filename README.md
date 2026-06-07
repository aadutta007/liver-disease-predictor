# 🫀 Liver Disease Risk Prediction

## SDG 3 – Good Health & Well-being

A machine learning web application that predicts the risk of liver disease using clinical blood test parameters. Built with **LightGBM**, **Streamlit**, and deployed on Streamlit Cloud.

---

## 📌 Problem Statement

Liver disease often goes undetected until serious complications arise. This tool provides an **early risk assessment** based on routine liver function tests, helping users take preventive action and consult a doctor if needed.

---

## 🧠 Model Performance

| Metric           | Value      |
|-----------------|------------|
| **Accuracy**     | **84%+**   |
| Algorithm        | LightGBM   |
| Techniques       | SMOTE, Data Augmentation, MinMax Scaling |
| Dataset          | Indian Liver Patient Dataset (UCI) |

> Achieved through hyperparameter tuning and handling class imbalance.

---

## 📊 Dataset

- **Name:** Indian Liver Patient Dataset (ILPD)
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/ILPD+(Indian+Liver+Patient+Dataset))
- **Samples:** 583 patient records
- **Features:** 10 clinical parameters (age, gender, bilirubin, enzymes, proteins, albumin, A/G ratio)
- **Target:** 1 = Liver Disease, 0 = No Disease

---

## 🚀 Live Demo

👉 [Click here to try the app](https://liver-disease-predictor-aadutta-special007.streamlit.app/)
