<div align="center">



\# 🌌 Exoplanet Classification using Machine Learning



\### Predicting Exoplanet Candidates from NASA Kepler Mission Data



An end-to-end Machine Learning project that classifies exoplanet candidates using astronomical observations from the NASA Kepler Mission. The project covers \*\*data preprocessing, feature engineering, model training, model serialization, and deployment through an interactive Streamlit web application.\*\*



!\[Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)

!\[Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)

!\[Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red?logo=streamlit)

!\[License](https://img.shields.io/badge/License-MIT-green)



</div>



\---



\# 📖 Overview



The discovery of exoplanets is one of the most exciting fields in modern astronomy. Large astronomical surveys such as NASA's Kepler Mission generate massive amounts of observational data, making manual classification difficult.



This project leverages Machine Learning techniques to automate the classification of exoplanet candidates based on their observed characteristics.



The project includes:



\- 📊 Exploratory Data Analysis

\- 🧹 Data Cleaning \& Feature Engineering

\- 🤖 Machine Learning Model Training

\- 💾 Model Serialization using Joblib

\- 🌐 Interactive Streamlit Application

\- 📈 Real-time Predictions



\---



\# ✨ Features



\- ✅ End-to-End Machine Learning Pipeline

\- ✅ Data Preprocessing

\- ✅ Feature Engineering

\- ✅ Trained Classification Model

\- ✅ Interactive Prediction Interface

\- ✅ Fast Predictions using Joblib Models

\- ✅ Clean Project Structure

\- ✅ Easily Extendable



\---



\# 📂 Project Structure



```text

Exoplanet-Classification

│

├── data/

│   ├── KOI\_Cumulative\_clean.csv

│   └── cleaned\_koi.csv

│

├── notebooks/

│   ├── 01\_EDA.ipynb

│   ├── 02\_Model\_Training.ipynb

│   └── Preprocessing.ipynb

│

├── model.joblib

├── target\_mapping.joblib

├── training\_columns.joblib

│

├── app.py

├── streamlit\_app.py

│

├── requirements.txt

├── README.md

└── .gitignore

```



\---



\# 🔬 Workflow



```text

NASA Kepler Dataset

&#x20;         │

&#x20;         ▼

&#x20;Data Cleaning

&#x20;         │

&#x20;         ▼

&#x20;Feature Engineering

&#x20;         │

&#x20;         ▼

&#x20;Model Training

&#x20;         │

&#x20;         ▼

&#x20;Model Evaluation

&#x20;         │

&#x20;         ▼

&#x20;Save Model (.joblib)

&#x20;         │

&#x20;         ▼

&#x20;Streamlit Web App

&#x20;         │

&#x20;         ▼

&#x20;Real-time Exoplanet Prediction

```



\---



\# 📊 Dataset



This project uses the \*\*NASA Kepler Exoplanet Candidate Dataset\*\*, which contains observational measurements collected by the Kepler Space Telescope.



The dataset contains numerous astrophysical features describing candidate planets that are used to predict their classification.



\---



\# 🛠 Tech Stack



\### Programming Language



\- Python



\### Data Analysis



\- Pandas

\- NumPy



\### Machine Learning



\- Scikit-learn

\- XGBoost

\- CatBoost



\### Visualization



\- Matplotlib

\- Plotly



\### Deployment



\- Streamlit



\### Model Serialization



\- Joblib



\---



\# ⚙ Installation



\## Clone Repository



```bash

git clone https://github.com/harishpannuru/Exoplanet-Classification.git



cd Exoplanet-Classification

```



\---



\## Create Virtual Environment



Windows



```bash

python -m venv .venv



.venv\\Scripts\\activate

```



Linux / macOS



```bash

python3 -m venv .venv



source .venv/bin/activate

```



\---



\## Install Dependencies



```bash

pip install -r requirements.txt

```



\---



\# ▶ Run the Application



```bash

streamlit run streamlit\_app.py

```



Open your browser:



```

http://localhost:8501

```



\---



\# 🧠 Machine Learning Pipeline



The pipeline consists of the following stages:



\- Missing Value Handling

\- Data Cleaning

\- Feature Selection

\- Feature Engineering

\- Model Training

\- Hyperparameter Optimization

\- Model Evaluation

\- Prediction



\---



\# 📁 Saved Models



The repository includes trained models for direct inference.



| File | Description |

|------|-------------|

| model.joblib | Trained Machine Learning Model |

| target\_mapping.joblib | Target Label Encoder |

| training\_columns.joblib | Feature Column Information |



\---



\# 📈 Model Performance



| Metric | Value |

|--------|-------|

| Accuracy | \*\*(Add your best accuracy here)\*\* |

| Precision | - |

| Recall | - |

| F1 Score | - |



\---



\# 📸 Screenshots



\## Home Page



> Add Screenshot



```

images/home.png

```



\---



\## Prediction Page



> Add Screenshot



```

images/predict.png

```



\---



\## Prediction Result



> Add Screenshot



```

images/result.png

```



\---



\# 🚀 Future Improvements



\- Deep Learning Models

\- Explainable AI (SHAP)

\- Hyperparameter Optimization

\- Model Comparison Dashboard

\- Cloud Deployment

\- REST API Integration

\- Docker Support



\---



\# 🤝 Contributing



Contributions are welcome.



1\. Fork the repository

2\. Create a new feature branch



```bash

git checkout -b feature-name

```



3\. Commit changes



```bash

git commit -m "Added new feature"

```



4\. Push



```bash

git push origin feature-name

```



5\. Open a Pull Request



\---



\# 👨‍💻 Author



\## PAvan



 Machine Learning Enthusiast



GitHub:



https://github.com/harishpannuru



\---



\# ⭐ If you like this project



Give this repository a ⭐ on GitHub if you found it useful.



It motivates me to build more open-source Machine Learning projects.



\---



<div align="center">



\### ⭐ Thank you for visiting ⭐



Made with ❤️ using Python, Machine Learning and Streamlit



</div>

