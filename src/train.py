import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

from sklearn.metrics import accuracy_score

from utils.cleaner import clean_resume
from src.config import *

print("=" * 60)
print("TalentLens AI Model Training")
print("=" * 60)

df = pd.read_csv(DATASET_PATH)

print("Original Shape:", df.shape)

df = df.drop_duplicates()

print("After Removing Duplicates:", df.shape)

df["Resume"] = df["Resume"].apply(clean_resume)

encoder = LabelEncoder()

y = encoder.fit_transform(df["Category"])

vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)

X = vectorizer.fit_transform(df["Resume"])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

models = {

    "Logistic Regression": LogisticRegression(max_iter=1000),

    "Linear SVM": LinearSVC(),

    "Naive Bayes": MultinomialNB()

}

best_model = None

best_accuracy = 0

for name, model in models.items():

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    print(f"{name}: {accuracy:.4f}")

    if accuracy > best_accuracy:

        best_accuracy = accuracy

        best_model = model

joblib.dump(best_model, MODEL_PATH)

joblib.dump(vectorizer, VECTORIZER_PATH)

joblib.dump(encoder, ENCODER_PATH)

print()

print("=" * 60)

print("Best Accuracy:", best_accuracy)

print("Model Saved Successfully")

print("=" * 60)