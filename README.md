Personalized Learning Path Generator

A web-based personalized learning path generator that helps learners build a structured learning journey based on their learning needs and interests.

The project combines a Python backend, a recommendation component, trained model/data files, and a simple web interface to generate and present personalized learning paths.

Features

🎯 Generate personalized learning paths

🤖 Recommendation/model-based learning suggestions

📚 Uses structured learning data from the project dataset

🌐 Web interface with HTML templates and CSS

📊 Includes model training and recommendation modules

🧪 Test files for the model and recommender components

🧩 Modular project structure for future improvements

Tech Stack

Python

Flask for the web application

HTML/CSS for the user interface

Machine Learning / Recommendation System for personalization

CSV for learning data

Git & GitHub for version control

Project Structure

Personalized Learning Path Generator/
│
├── app.py                  # Main Flask application
├── recommender.py          # Recommendation logic
├── train_model.py          # Model training
├── test_model.py           # Model tests
├── test_recommender.py     # Recommender tests
├── requirements.txt        # Python dependencies
│
├── data/
│   └── learning_data.csv   # Learning/resource dataset
│
├── models/                 # Trained model files
│
├── static/
│   └── style.css           # Stylesheet
│
├── templates/
│   ├── index.html          # Main page
│   ├── dashboard.html      # Dashboard
│   └── results.html        # Learning path/results page
│
├── .gitignore
└── LICENSE

How It Works

The application follows a simple workflow:

The learner provides their learning preferences or requirements.

The application processes the input.

The recommendation component uses the available learning data/model to identify relevant learning content.

A personalized learning path is generated.

The resulting path is displayed through the web interface.

Installation

1. Clone the repository

git clone https://github.com/manojkudari22-art/personalized-learning-path-generator.git
cd personalized-learning-path-generator

2. Create a virtual environment

Windows

python -m venv venv
venv\Scripts\activate

macOS/Linux

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

Running the Project

If the model needs to be trained or regenerated, run:

python train_model.py

Then start the web application:

python app.py

Open the local URL shown in the terminal, typically:

http://127.0.0.1:5000/

Testing

Run the model tests:

python test_model.py

Run the recommender tests:

python test_recommender.py

Dataset

The project uses data/learning_data.csv as its learning-resource dataset.

The dataset can be extended with additional learning resources and relevant attributes to improve the variety and usefulness of generated learning paths.

Future Improvements

Add user accounts and persistent learner profiles

Improve recommendation accuracy with additional learner feedback

Add progress tracking

Add learning-path difficulty levels

Integrate external course/resource APIs

Add more comprehensive automated tests

Improve the UI/UX and mobile responsiveness

Add analytics for learner progress and recommendations

License

This project is licensed under the MIT License. See the LICENSE file for details.

Author

Manoj Kumar

GitHub: https://github.com/manojkudari22-art
