import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/learning_model.pkl")

# Sample student
student = pd.DataFrame([{
    "python": 4,
    "sql": 2,
    "math": 3,
    "study_hours": 2,
    "quiz_score": 55,
    "projects_completed": 1
}])

# Predict learning level
prediction = model.predict(student)

print("Predicted Learning Level:", prediction[0])