import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

import joblib

from utils.cleaner import clean_resume
from src.config import *

model = joblib.load(MODEL_PATH)

vectorizer = joblib.load(VECTORIZER_PATH)

encoder = joblib.load(ENCODER_PATH)


def predict_role(text):

    cleaned = clean_resume(text)

    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)

    role = encoder.inverse_transform(prediction)[0]

    return role