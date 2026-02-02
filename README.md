# 🧠 Stroke Prediction App

A simple **Streamlit web application** that predicts the risk of stroke using a **pre-trained Machine Learning model**. The app allows users to enter patient details, displays stroke awareness imagery, and returns a prediction result in an easy-to-understand format.

---

## 🚀 Live Demo

Deployed on **Streamlit Cloud**:

> 🔗 *(https://yamuna3103-stroke-prediction-app-app-kkxaim.streamlit.app/)*

---

## ✨ Features

* 👤 Patient name input
* 🖼️ Stroke awareness image display
* 🧠 Stroke risk prediction using ML model (`.pkl`)
* ⚡ Fast and lightweight Streamlit UI
* ☁️ Deployed via GitHub + Streamlit Cloud

---

## 🗂️ Project Structure

```
stroke_prediction_app/
│── app.py                      # Main Streamlit app
│── requirements.txt            # Python dependencies
│── stroke_prediction_model.pkl # Trained ML model
│── stroke.jpg                  # Stroke awareness image
│── README.md                   # Project documentation
```

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **scikit-learn**
* **NumPy**
* **joblib**

---

## ▶️ Run Locally

1. Clone the repository:

```bash
git clone https://github.com/Yamuna3103/stroke_prediction_app.git
cd stroke_prediction_app
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push project to GitHub
2. Go to 👉 [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **New App**
4. Select:

   * Repository: `stroke_prediction_app`
   * Branch: `main`
   * Main file: `app.py`
5. Click **Deploy 🚀**

---

## 📌 Notes

* Ensure `scikit-learn` is spelled correctly in `requirements.txt`
* The `.pkl` model must be trained using the same library versions
* All files should be in the repository root

---

## 🙌 Author

**Yamuna Sk**
Data Science | Machine Learning | Streamlit

---

## ⭐ Acknowledgement

This project is created for learning and demonstration purposes in Machine Learning model deployment.

If you found this useful, don’t forget to ⭐ the repository!
