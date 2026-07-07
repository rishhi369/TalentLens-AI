from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_PATH = BASE_DIR / "datasets" / "UpdatedResumeDataSet.csv"

MODEL_DIR = BASE_DIR / "models"

MODEL_PATH = MODEL_DIR / "resume_classifier.pkl"

VECTORIZER_PATH = MODEL_DIR / "tfidf_vectorizer.pkl"

ENCODER_PATH = MODEL_DIR / "label_encoder.pkl"