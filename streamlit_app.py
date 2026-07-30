import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.express as px
import plotly.graph_objects as go
import joblib
from io import BytesIO
from PIL import Image

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Exoplanet Classification Dashboard",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background-color:#0E1117;
}

.block-container{
    padding-top:1rem;
}

h1,h2,h3,h4{
    color:white;
}

.metric-card{
    background:#1E1E1E;
    padding:15px;
    border-radius:12px;
    text-align:center;
    box-shadow:0px 0px 8px rgba(255,255,255,0.05);
}

.metric-title{
    color:#BBBBBB;
    font-size:18px;
}

.metric-value{
    color:#00E5FF;
    font-size:32px;
    font-weight:bold;
}

.footer{
    text-align:center;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🪐 Exoplanet Dashboard")

st.sidebar.markdown("---")

st.sidebar.header("Model")

st.sidebar.success("XGBoost Classifier")

st.sidebar.header("Dataset")

st.sidebar.info("NASA Kepler KOI")

st.sidebar.header("Prediction Classes")

st.sidebar.write("✅ CONFIRMED")

st.sidebar.write("🟡 CANDIDATE")

st.sidebar.write("❌ FALSE POSITIVE")

st.sidebar.markdown("---")

st.sidebar.header("Developer")

st.sidebar.write("Immani Pavan Sai Krishna")

st.sidebar.write("Machine Learning Project")

# -----------------------------
# Title
# -----------------------------
st.title("🪐 Exoplanet Classification Dashboard")

st.write(
"""
Predict whether a **Kepler Object of Interest**
is

- ✅ Confirmed Planet
- 🟡 Candidate
- ❌ False Positive

using a trained **XGBoost Machine Learning Model**.
"""
)

st.markdown("---")

# -----------------------------
# KPI Cards
# -----------------------------
col1,col2,col3,col4=st.columns(4)

with col1:

    st.markdown("""
    <div class='metric-card'>
    <div class='metric-title'>Accuracy</div>
    <div class='metric-value'>94.46%</div>
    </div>
    """,unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class='metric-card'>
    <div class='metric-title'>Algorithm</div>
    <div class='metric-value'>XGBoost</div>
    </div>
    """,unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class='metric-card'>
    <div class='metric-title'>Features</div>
    <div class='metric-value'>20</div>
    </div>
    """,unsafe_allow_html=True)

with col4:

    st.markdown("""
    <div class='metric-card'>
    <div class='metric-title'>Classes</div>
    <div class='metric-value'>3</div>
    </div>
    """,unsafe_allow_html=True)

st.markdown("---")

# -----------------------------
# Model Information
# -----------------------------
with st.expander("📋 Model Information",expanded=True):

    info=pd.DataFrame({

        "Property":[
            "Algorithm",
            "Dataset",
            "Accuracy",
            "Features",
            "Classes",
            "Deployment"
        ],

        "Value":[
            "XGBoost",
            "NASA Kepler KOI",
            "94.46%",
            "Top 20",
            "3",
            "FastAPI + Streamlit"
        ]

    })

    st.dataframe(
        info,
        use_container_width=True,
        hide_index=True
    )

st.markdown("---")

# -----------------------------
# Upload Dataset
# -----------------------------
st.header("📂 Upload Dataset")

uploaded_file=st.file_uploader(

    "Upload CSV",

    type=["csv"]

)

# -----------------------------
# Dataset Preview
# -----------------------------
if uploaded_file is not None:

    df=pd.read_csv(uploaded_file)

    st.success("Dataset Uploaded Successfully!")

    tab1,tab2,tab3=st.tabs(

        [

            "Preview",

            "Statistics",

            "Columns"

        ]

    )

    with tab1:

        st.subheader("Dataset Preview")

        st.dataframe(

            df.head(),

            use_container_width=True

        )

    with tab2:

        st.subheader("Dataset Statistics")

        c1,c2,c3=st.columns(3)

        c1.metric("Rows",df.shape[0])

        c2.metric("Columns",df.shape[1])

        c3.metric("Missing Values",df.isnull().sum().sum())

        st.dataframe(

            df.describe(),

            use_container_width=True

        )

    with tab3:

        st.subheader("Columns")

        st.write(list(df.columns))

    st.markdown("---")

    # -----------------------------
    # Prediction Button
    # -----------------------------
    if st.button(

        "🚀 Predict Exoplanets",

        use_container_width=True

    ):

        with st.spinner(

            "Connecting to FastAPI..."

        ):

            uploaded_file.seek(0)

            files={

                "file":(

                    uploaded_file.name,

                    uploaded_file,

                    "text/csv"

                )

            }

            try:

                response=requests.post(

                    "http://127.0.0.1:8000/predict",

                    files=files

                )

                if response.status_code==200:

                    result=response.json()

                    predictions=result["predictions"]

                    df["Prediction"]=predictions

                    st.session_state["predictions"]=df

                    st.success("Prediction Completed!")

                else:

                    st.error(response.json()["detail"])

            except Exception:

                st.error(

                    "Cannot connect to FastAPI.\n\nRun:\n\nuvicorn app:app --reload"

                )# ============================================================
# PART 2
# Results Dashboard
# ============================================================

if "predictions" in st.session_state:

    result_df = st.session_state["predictions"]

    st.markdown("---")

    st.header("📊 Prediction Dashboard")

    # ===========================================
    # Metrics
    # ===========================================

    total = len(result_df)

    confirmed = (result_df["Prediction"] == "CONFIRMED").sum()

    candidate = (result_df["Prediction"] == "CANDIDATE").sum()

    false_positive = (result_df["Prediction"] == "FALSE POSITIVE").sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Planets", total)

    c2.metric("Confirmed", confirmed)

    c3.metric("Candidate", candidate)

    c4.metric("False Positive", false_positive)

    st.markdown("---")

    # ===========================================
    # Prediction Table
    # ===========================================

    st.subheader("🔍 Prediction Results")

    st.dataframe(
        result_df,
        use_container_width=True,
        height=450
    )

    st.markdown("---")

    # ===========================================
    # Summary Data
    # ===========================================

    summary = (
        result_df["Prediction"]
        .value_counts()
        .rename_axis("Class")
        .reset_index(name="Count")
    )

    col1, col2 = st.columns(2)

    # ===========================================
    # Summary Table
    # ===========================================

    with col1:

        st.subheader("📋 Prediction Summary")

        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True
        )

    # ===========================================
    # Pie Chart
    # ===========================================

    with col2:

        st.subheader("🥧 Prediction Distribution")

        fig = px.pie(
            summary,
            names="Class",
            values="Count",
            hole=0.45
        )

        fig.update_traces(
            textposition="inside",
            textinfo="percent+label"
        )

        fig.update_layout(
            height=420,
            showlegend=True
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    # ===========================================
    # Bar Chart
    # ===========================================

    st.subheader("📈 Prediction Counts")

    fig2 = px.bar(
        summary,
        x="Class",
        y="Count",
        text="Count"
    )

    fig2.update_traces(
        textposition="outside"
    )

    fig2.update_layout(
        height=500
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.markdown("---")

    # ===========================================
    # Prediction Percentages
    # ===========================================

    st.subheader("📊 Prediction Percentages")

    percentage_df = summary.copy()

    percentage_df["Percentage"] = (
        percentage_df["Count"]
        / percentage_df["Count"].sum()
        * 100
    ).round(2)

    st.dataframe(
        percentage_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # ===========================================
    # Confidence Section
    # ===========================================

    st.subheader("🎯 Prediction Confidence")

    st.info(
        """
The current FastAPI endpoint returns only the predicted class.

To display confidence values such as:

• CONFIRMED — 98.6%

• FALSE POSITIVE — 99.2%

• CANDIDATE — 91.4%

modify your FastAPI backend to use:

model.predict_proba()

instead of only

model.predict()

We'll add that in the FastAPI update later.
"""
    )

    st.markdown("---")

    # ===========================================
    # Download Button
    # ===========================================

    csv = result_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Predictions CSV",
        data=csv,
        file_name="predictions.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.markdown("---")

    # ===========================================
    # Quick Insights
    # ===========================================

    st.subheader("💡 Quick Insights")

    majority = summary.iloc[0]["Class"]

    majority_count = summary.iloc[0]["Count"]

    st.success(
        f"""
Most predicted class:

**{majority}**

Total Predictions:

**{majority_count}**
"""
    )