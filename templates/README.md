# Personalized Learning Path Generator Using Machine Learning

## 📌 Project Overview

The Personalized Learning Path Generator is a machine learning based web application that analyzes a student's skills and performance and generates a personalized learning path.

The system predicts the student's learning level using a Random Forest Classifier and then recommends suitable topics based on the predicted level and learning goal.

## 🎯 Objectives

- Analyze student skills and performance
- Predict the student's learning level
- Generate a personalized learning roadmap
- Provide the results through a web dashboard
- Help students identify suitable topics for improvement

## 🛠️ Technologies Used

- Python
- Machine Learning
- Scikit-learn
- Pandas
- Flask
- HTML
- CSS
- JavaScript
- SQLite (planned enhancement)

## 🤖 Machine Learning

The project uses a **Random Forest Classifier**.

### Input Features

- Python skill
- SQL skill
- Math skill
- Study hours per day
- Quiz score
- Projects completed

### Output

The model predicts one of:

- Beginner
- Intermediate
- Advanced

## 🔄 System Workflow

Student Input  
↓  
Data Preprocessing  
↓  
Random Forest ML Model  
↓  
Learning Level Prediction  
↓  
Recommendation Module  
↓  
Personalized Learning Path  
↓  
Web Dashboard

## 📂 Project Structure

```text
Personalized Learning Path Generator/
│
├── app.py
├── train_model.py
├── test_model.py
├── recommender.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── learning_data.csv
│
├── models/
│   └── learning_model.pkl
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── dashboard.html
│
└── static/
    └── style.css