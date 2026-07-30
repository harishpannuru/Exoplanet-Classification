from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import joblib

# ==============================
# Create FastAPI App
# ==============================
app = FastAPI(
    title="Exoplanet Classification API",
    description="Predict whether a Kepler Object of Interest is CONFIRMED, CANDIDATE, or FALSE POSITIVE",
    
    version="1.0"
)

# ==============================
# Load Model
# ==============================
try:
    model = joblib.load("model.joblib")
    training_columns = joblib.load("training_columns.joblib")
    target_mapping = joblib.load("target_mapping.joblib")

    inverse_mapping = {v: k for k, v in target_mapping.items()}

except Exception as e:
    raise RuntimeError(f"Error loading model files: {e}")


# ==============================
# Home
# ==============================
@app.get("/")
def home():
    return {
        "message": "Welcome to the Exoplanet Classification API",
        "status": "Running",
        "model": "XGBoost",
        "accuracy": 0.9456,
        "best_iteration": 203
    }

# ==============================
# Health Check
# ==============================
@app.get("/health")
def health():
    return {"status": "Healthy"}


# ==============================
# Preprocessing Function
# ==============================
def preprocess(df):

    drop_cols = [
        "kepoi_name",
        "kepler_name",
        "koi_vet_stat",
        "koi_vet_date",
        "koi_disposition",
        "koi_disp_prov",
        "koi_comment",
        "koi_limbdark_mod",
        "koi_tce_delivname",
        "koi_quarters",
        "koi_trans_mod",
        "koi_datalink_dvr",
        "koi_datalink_dvs"
    ]

    df = df.drop(columns=drop_cols, errors="ignore")

    df = pd.get_dummies(
        df,
        columns=[
            "koi_fittype",
            "koi_parm_prov",
            "koi_sparprov"
        ],
        drop_first=True,
        dtype=int
    )

    # Match training columns
    df = df.reindex(columns=training_columns, fill_value=0)

    return df


# ==============================
# Prediction Endpoint
# ==============================
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:

        if not file.filename.endswith(".csv"):
            raise HTTPException(
                status_code=400,
                detail="Please upload a CSV file."
            )

        df = pd.read_csv(file.file)

        X = preprocess(df)

        pred = model.predict(X)

        pred_labels = [inverse_mapping[int(x)] for x in pred]

        df["Prediction"] = pred_labels

        # Save output
        df.to_csv("predictions.csv", index=False)

        return {
            "message": "Prediction completed successfully.",
            "total_records": len(df),
            "predictions": pred_labels
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ==============================
# Prediction Summary
# ==============================
@app.post("/predict-summary")
async def predict_summary(file: UploadFile = File(...)):

    try:

        df = pd.read_csv(file.file)

        X = preprocess(df)

        pred = model.predict(X)

        pred_labels = [inverse_mapping[int(x)] for x in pred]

        summary = pd.Series(pred_labels).value_counts()

        return {
            "total_records": len(pred_labels),
            "summary": summary.to_dict(),
            "percentage": (
                summary / len(pred_labels) * 100
            ).round(2).to_dict()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))