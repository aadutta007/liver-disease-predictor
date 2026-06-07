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

---

## 🛠️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/liver-disease-predictor.git
cd liver-disease-predictor
2. Install dependencies
bash
pip install -r requirements.txt
3. Run the Streamlit app
bash
streamlit run app.py
The app will open in your browser at http://localhost:8501.

📁 Project Structure
text
.
├── app.py                    # Streamlit web application
├── liver_model_final.pkl     # Trained LightGBM model
├── scaler_final.pkl          # MinMaxScaler for feature scaling
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
📝 Input Features
Feature	Description
Age	Patient's age (years)
Gender	Male / Female
Total Bilirubin	mg/dL
Direct Bilirubin	mg/dL
Alkaline Phosphatase	IU/L
ALT (SGPT)	IU/L
AST (SGOT)	IU/L
Total Proteins	g/dL
Albumin	g/dL
A/G Ratio	Albumin/Globulin ratio
🎯 Example Test Cases
Case	Age	Gender	TB	DB	Alk Phos	ALT	AST	TP	Alb	A/G	Expected Output
Healthy	17	Male	0.9	0.3	202	22	19	7.4	4.1	1.2	✅ Low Risk
Liver Disease	62	Male	10.9	5.5	699	64	100	7.5	3.2	0.74	⚠️ High Risk
🧪 Technologies Used
Python 3.12

LightGBM – Gradient boosting framework

Scikit-learn – Preprocessing & evaluation

SMOTE – Handling class imbalance

Streamlit – Web interface

Streamlit Cloud – Deployment

📌 Disclaimer
⚠️ This tool is for educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical concerns.

👨‍💻 Author
Your Name – GitHub Profile

🙏 Acknowledgements
UCI Machine Learning Repository for the ILPD dataset

Streamlit for easy deployment

📄 License
MIT License – free to use and modify for educational purposes.
