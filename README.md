# 🫀 Liver Disease Risk Prediction  
### SDG 3 – Good Health & Well-being

A **machine learning web application** that predicts the **risk of liver disease** using routine clinical blood test parameters.  
Built using **LightGBM**, **Streamlit**, and deployed on **Streamlit Cloud**.

---

## 📌 Problem Statement

Liver disease often remains **undiagnosed until advanced stages**, leading to severe complications and increased mortality.  
This application provides an **early risk assessment** based on common liver function test results, enabling timely medical consultation and preventive care.

---

## 🧠 Model Performance

| Metric        | Value |
|--------------|-------|
| **Accuracy** | **84%+** |
| Algorithm    | LightGBM |
| Techniques   | SMOTE, Data Augmentation, MinMax Scaling |
| Dataset      | Indian Liver Patient Dataset (ILPD) |

> Performance achieved through **class imbalance handling** and **hyperparameter tuning**.

---

## 📊 Dataset

- **Name:** Indian Liver Patient Dataset (ILPD)
- **Source:** :contentReference[oaicite:0]{index=0}
- **Total Samples:** 583
- **Features:** 10 clinical parameters  
- **Target Variable:**  
  - `1` → Liver Disease  
  - `0` → No Liver Disease  

---

## 🚀 Live Demo

👉 :contentReference[oaicite:1]{index=1}

---

## 🛠️ How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/liver-disease-predictor.git
cd liver-disease-predictor
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Streamlit App
streamlit run app.py

The application will open in your browser at:
http://localhost:8501

📁 Project Structure
.
├── app.py                    # Streamlit web application
├── liver_model_final.pkl     # Trained LightGBM model
├── scaler_final.pkl          # MinMaxScaler for preprocessing
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
A/G Ratio	Albumin / Globulin ratio
🎯 Example Test Cases
Case	Age	Gender	TB	DB	Alk Phos	ALT	AST	TP	Alb	A/G	Output
Healthy	17	Male	0.9	0.3	202	22	19	7.4	4.1	1.2	✅ Low Risk
Liver Disease	62	Male	10.9	5.5	699	64	100	7.5	3.2	0.74	⚠️ High Risk
🧪 Technologies Used
Python 3.12
LightGBM
Scikit-learn
SMOTE
Streamlit
Streamlit Cloud
📌 Disclaimer

⚠️ This application is intended for educational and academic purposes only.
It is not a substitute for professional medical diagnosis or treatment.
Always consult a qualified healthcare professional for medical concerns.

👨‍💻 Author

Your Name
GitHub: https://github.com/your-username

🙏 Acknowledgements
UCI Machine Learning Repository for providing the dataset
Streamlit Official Website for seamless web app deployment
📄 License

This project is licensed under the MIT License — free to use and modify for educational purposes.
