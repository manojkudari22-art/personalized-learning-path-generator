def generate_learning_path(level, goal):
    goal = goal.lower()

    if "python" in goal:
        topics = {
            "Beginner": [
                "Python Basics",
                "Variables and Data Types",
                "Conditions and Loops",
                "Functions",
                "Lists and Dictionaries",
                "Mini Project"
            ],
            "Intermediate": [
                "Object-Oriented Programming",
                "File Handling",
                "Exception Handling",
                "Modules and Packages",
                "APIs",
                "Python Project"
            ],
            "Advanced": [
                "Advanced Python",
                "Decorators and Generators",
                "Testing",
                "Performance Optimization",
                "FastAPI/Flask",
                "Advanced Project"
            ]
        }

    elif "data" in goal:
        topics = {
            "Beginner": [
                "Python Basics",
                "NumPy",
                "Pandas",
                "Data Cleaning",
                "Basic Statistics",
                "Data Analysis Project"
            ],
            "Intermediate": [
                "Advanced Pandas",
                "Statistics",
                "Data Visualization",
                "SQL",
                "Exploratory Data Analysis",
                "Data Analysis Project"
            ],
            "Advanced": [
                "Advanced SQL",
                "Machine Learning",
                "Feature Engineering",
                "Model Evaluation",
                "Advanced Visualization",
                "End-to-End Data Project"
            ]
        }

    else:
        topics = {
            "Beginner": [
                "Fundamentals",
                "Basic Concepts",
                "Practice Exercises",
                "Mini Project"
            ],
            "Intermediate": [
                "Intermediate Concepts",
                "Problem Solving",
                "Practical Exercises",
                "Intermediate Project"
            ],
            "Advanced": [
                "Advanced Concepts",
                "Real-World Problems",
                "Advanced Practice",
                "Advanced Project"
            ]
        }

    selected_topics = topics.get(level, topics["Beginner"])

    return selected_topics