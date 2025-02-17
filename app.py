# Description: This file contains the main code for the Flask application. 
# # It creates a Flask app, connects to the database, and defines the routes for the application. 
# The index route displays the questions, and the submit route checks the user's answers and displays the results.

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Question, User

app = Flask(__name__)

engine = create_engine("sqlite:///questions.sqlite", echo=True) # Create an engine to connect to the database
Base.metadata.create_all(engine) # Create the tables in the database
Session = sessionmaker(bind=engine) # Create a session class
session = Session() # Create a session object

@app.route("/") 
def index():
    '''Display the questions on the index page'''
    questions = session.query(Question).all()
    return render_template("index.html", questions=questions)

@app.route("/submit", methods=["POST"])
def submit():
    '''Check the user's answers and display the results'''
    name = request.form.get("name") #Gets the username from the form
    score = 0
    total_score = 0
    results = []
    for question in session.query(Question).all():
        question_id = question.id
        user_answer = request.form.get(f"{question_id}")
        total_score += 1
        if user_answer and question.correct_answer.lower() == user_answer.lower():
            results.append((question.question, "Correct!"))
            score += 1
        else:
            results.append((question.question, "Incorrect!"))

    user = User(name=name, score=score)
    session.add(user)
    session.commit()

    return render_template("results.html", results=results, name=name, score=score, total_score=total_score) 

if __name__ == "__main__":
    app.run(debug=True)