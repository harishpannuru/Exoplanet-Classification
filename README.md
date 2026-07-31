# 🌌 Exoplanet Classification using Machine Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python">
  <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit">
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn">
  <img src="https://img.shields.io/badge/XGBoost-Model-yellowgreen">
  <img src="https://img.shields.io/github/license/harishpannuru/Exoplanet-Classification">
</p>

## 📌 Overview

This project classifies exoplanets using Machine Learning based on astronomical features. It includes:

- 📊 Exploratory Data Analysis (EDA)
- 🧹 Data Cleaning & Preprocessing
- 🤖 Machine Learning Model Training
- 📈 Model Evaluation
- 🌐 Interactive Streamlit Web Application
- ⚡ FastAPI Backend
- 💾 Saved Models for Prediction

---

# 🚀 Features

- Interactive Streamlit Interface
- FastAPI Backend
- Data Cleaning & Missing Value Handling
- Feature Engineering
- Feature Selection
- Hyperparameter Optimization
- Model Training
- Prediction on New Data
- Saved Model using Joblib

---

# 🛠 Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- XGBoost

### Data Analysis

- Pandas
- NumPy
- Matplotlib
- Plotly
- YData Profiling

### Backend

- FastAPI

### Frontend

- Streamlit

---

# 📂 Project Structure

```text
Exoplanet-Classification/
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   └── 02_Model_Training.ipynb
│
├── data/
│
├── streamlit_app.py
├── app.py
│
├── model.joblib
├── target_mapping.joblib
├── training_columns.joblib
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/harishpannuru/Exoplanet-Classification.git
cd Exoplanet-Classification
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

## Start the Streamlit App

```bash
streamlit run streamlit_app.py
```

The application will open at:

```text
http://localhost:8501
```

---

## Run FastAPI Backend (Optional)

```bash
uvicorn app:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🧠 Machine Learning Pipeline

The project follows the complete Machine Learning workflow:

- Data Collection
- Data Cleaning
- Missing Value Handling
- Exploratory Data Analysis
- Feature Engineering
- Feature Selection
- Model Training
- Hyperparameter Optimization
- Model Evaluation
- Prediction

---

# 💾 Saved Models

| File | Description |
|------|-------------|
| model.joblib | Trained Machine Learning Model |
| target_mapping.joblib | Target Label Mapping |
| training_columns.joblib | Feature Column Information |

---

# 📈 Model Performance

| Metric | Score |
|--------|------:|
| Accuracy | **94.56%** |
| Precision | - |
| Recall | - |
| F1 Score | - |

---

# 📸 Screenshots

## 🏠 Home Page

_Add screenshot here_

```
images/home.png
```

---

## 🔮 Prediction Page

_Add screenshot here_

```
images/predict.png
```

---

## ✅ Prediction Result

_Add screenshot here_

```
images/result.png
```

---

# 📦 Requirements

Major libraries used:

- Streamlit
- FastAPI
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Plotly
- Matplotlib
- Joblib
- YData Profiling

---

# 🚀 Future Improvements

- Deep Learning Models
- Explainable AI (SHAP)
- Model Comparison Dashboard
- Cloud Deployment
- Docker Support
- CI/CD Pipeline
- REST API Enhancements

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 👥 Authors

### Harish Pannuru
- Machine Learning Enthusiast
- GitHub: **https://github.com/harishpannuru**

### Pavan
- Project Collaborator
- Contributed to the development of the Exoplanet Classification project.

---

# 🤝 Acknowledgements

This project was collaboratively developed by **Harish Pannuru** and **Pavan** as part of a Machine Learning project.

---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

It helps support future open-source Machine Learning projects.

---

<p align="center">
Made with ❤️ by <b>Harish Pannuru</b> and <b>Pavan</b><br>
Python • Machine Learning • FastAPI • Streamlit
</p>