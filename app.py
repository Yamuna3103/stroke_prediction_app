import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="🧠 Stroke Prediction App", layout="centered")

st.title("🧠 Stroke Prediction App")
st.image(
    "stroke_prediction.jpg",
    use_container_width=True
)
st.write("Enter patient details to predict stroke risk")

patient_name = st.text_input("Patient Name")


@st.cache_resource
def load_model():
    return joblib.load("stroke_prediction_model.pkl")

model = load_model()


gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", min_value=1, max_value=120, value=30)

hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])

ever_married = st.selectbox("Ever Married", ["Yes", "No"])
work_type = st.selectbox(
    "Work Type",
    ["Private", "Self-employed", "Govt_job", "children", "Never_worked"]
)

Residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])

avg_glucose_level = st.number_input(
    "Average Glucose Level", min_value=50.0, max_value=300.0, value=100.0
)

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)

smoking_status = st.selectbox(
    "Smoking Status",
    ["formerly smoked", "never smoked", "smokes", "Unknown"]
)


input_data = pd.DataFrame([{
    "gender": gender,
    "age": age,
    "hypertension": hypertension,
    "heart_disease": heart_disease,
    "ever_married": ever_married,
    "work_type": work_type,
    "Residence_type": Residence_type,
    "avg_glucose_level": avg_glucose_level,
    "bmi": bmi,
    "smoking_status": smoking_status
}])


if st.button("Predict Stroke Risk"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Stroke")
    else:
        st.success("✅ Low Risk of Stroke")
