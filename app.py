from flask import Flask, render_template, request, session
import joblib
import pandas as pd

from recommender import generate_learning_path


app = Flask(__name__)

# Secret key for session
app.secret_key = "personalized-learning-path-secret"


# Load trained ML model
model = joblib.load("models/learning_model.pkl")


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Dashboard page
@app.route("/dashboard")
def dashboard():

    # Check whether student data exists
    if "student_data" not in session:
        return render_template(
            "dashboard.html",
            goal="No data",
            level="Not available",
            learning_path=[]
        )

    data = session["student_data"]

    return render_template(
        "dashboard.html",
        goal=data["goal"],
        level=data["level"],
        learning_path=data["learning_path"],
        python=data["python"],
        sql=data["sql"],
        math=data["math"],
        study_hours=data["study_hours"],
        quiz_score=data["quiz_score"],
        projects_completed=data["projects_completed"]
    )


# Generate personalized learning path
@app.route("/generate", methods=["POST"])
def generate():

    # Get student information
    goal = request.form["goal"]

    python_skill = int(request.form["python"])
    sql_skill = int(request.form["sql"])
    math_skill = int(request.form["math"])

    study_hours = int(request.form["study_hours"])
    quiz_score = int(request.form["quiz_score"])
    projects_completed = int(request.form["projects_completed"])


    # Create student DataFrame
    student = pd.DataFrame([{
        "python": python_skill,
        "sql": sql_skill,
        "math": math_skill,
        "study_hours": study_hours,
        "quiz_score": quiz_score,
        "projects_completed": projects_completed
    }])


    # Machine Learning prediction
    prediction = model.predict(student)

    learning_level = prediction[0]


    # Generate personalized learning path
    learning_path = generate_learning_path(
        learning_level,
        goal
    )


    # Store actual student data in session
    session["student_data"] = {
        "goal": goal,
        "level": learning_level,
        "learning_path": learning_path,
        "python": python_skill,
        "sql": sql_skill,
        "math": math_skill,
        "study_hours": study_hours,
        "quiz_score": quiz_score,
        "projects_completed": projects_completed
    }


    # Display result page
    return render_template(
        "result.html",
        goal=goal,
        level=learning_level,
        learning_path=learning_path,
        python=python_skill,
        sql=sql_skill,
        math=math_skill,
        study_hours=study_hours,
        quiz_score=quiz_score,
        projects_completed=projects_completed
    )


# Run Flask application
if __name__ == "__main__":
    app.run(debug=True)