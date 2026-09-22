import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

print("Starting model training...")


# Load dataset
data = pd.read_csv("data/learning_data.csv")

print("Dataset loaded successfully!")
print("Number of records:", len(data))


# Features
features = [
    "python",
    "sql",
    "math",
    "study_hours",
    "quiz_score",
    "projects_completed"
]

X = data[features]
y = data["learning_level"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Create ML model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train model
model.fit(X_train, y_train)

print("Model trained successfully!")


# Prediction
predictions = model.predict(X_test)


# Evaluation metrics
accuracy = accuracy_score(y_test, predictions)

precision = precision_score(
    y_test,
    predictions,
    average="weighted",
    zero_division=0
)

recall = recall_score(
    y_test,
    predictions,
    average="weighted",
    zero_division=0
)

f1 = f1_score(
    y_test,
    predictions,
    average="weighted",
    zero_division=0
)


# Print evaluation results
print("\nModel Evaluation")
print("----------------")
print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1 Score :", f1)


# Classification report
print("\nClassification Report")
print("---------------------")

print(
    classification_report(
        y_test,
        predictions,
        zero_division=0
    )
)


# Confusion matrix
print("Confusion Matrix")
print("----------------")

print(
    confusion_matrix(
        y_test,
        predictions
    )
)


# Save trained model
joblib.dump(
    model,
    "models/learning_model.pkl"
)

print("\nModel saved successfully!")
print("File: models/learning_model.pkl")