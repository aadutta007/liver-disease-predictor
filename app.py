import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('liver_model_final.pkl', 'rb'))
scaler = pickle.load(open('scaler_final.pkl', 'rb'))

st.set_page_config(page_title="Liver Disease Predictor", page_icon="🫀")
st.title("🫀 Liver Disease Risk Prediction")
st.markdown("#### SDG 3 – Good Health & Well-being")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 120, 58)
    gender = st.selectbox("Gender", ["Male", "Female"])
    total_bilirubin = st.number_input("Total Bilirubin (mg/dL)", 0.0, 20.0, 1.0)
    direct_bilirubin = st.number_input("Direct Bilirubin (mg/dL)", 0.0, 15.0, 0.4)
    alkaline_phosphatase = st.number_input("Alkaline Phosphatase (IU/L)", 0, 2000, 182)

with col2:
    alt = st.number_input("ALT (IU/L)", 0, 500, 14)
    ast = st.number_input("AST (IU/L)", 0, 500, 20)
    total_proteins = st.number_input("Total Proteins (g/dL)", 0.0, 15.0, 6.8)
    albumin = st.number_input("Albumin (g/dL)", 0.0, 10.0, 3.4)
    ag_ratio = st.number_input("A/G Ratio", 0.0, 5.0, 1.0)

gender_num = 1 if gender == "Male" else 0
features = np.array([[age, gender_num, total_bilirubin, direct_bilirubin,
                      alkaline_phosphatase, alt, ast, total_proteins,
                      albumin, ag_ratio]])
features_scaled = scaler.transform(features)

if st.button("🔍 Predict"):
    pred = model.predict(features_scaled)[0]
    prob = model.predict_proba(features_scaled)[0][1]
    if pred == 1:
        st.error(f"⚠️ High Risk of Liver Disease (probability {prob*100:.1f}%)")
    else:
        st.success(f"✅ Low Risk of Liver Disease (probability {prob*100:.1f}%)")
    st.info("Consult a doctor for medical advice.")

st.caption("⚠️ Educational purpose only – not a substitute for professional diagnosis.")