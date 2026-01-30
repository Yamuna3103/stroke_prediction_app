import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Stroke Prediction App", layout="centered")

st.title("🧠 Stroke Prediction App")

st.image(
    "stroke.png",
    caption="Stroke Awareness",
    use_container_width=True
)

st.write("Enter patient details to predict stroke risk")

@st.cache_resource
def load_model():
    return joblib.load("stroke_prediction_model.pkl")
patient_name = st.text_input("Patient Name")

model = load_model()

age = st.number_input("Age", min_value=0, max_value=120, value=45)
gender = st.selectbox("Gender", ["Male", "Female"])
hypertension = st.selectbox("Hypertension", ["No", "Yes"])
heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
avg_glucose = st.number_input("Average Glucose Level", value=100.0)
bmi = st.number_input("BMI", value=25.0)

gender = 1 if gender == "Male" else 0
hypertension = 1 if hypertension == "Yes" else 0
heart_disease = 1 if heart_disease == "Yes" else 0

input_data = np.array([[age, gender, hypertension, heart_disease, avg_glucose, bmi]])


if st.button("Predict Stroke"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Stroke")
    else:
        st.success("✅ Low Risk of Stroke")