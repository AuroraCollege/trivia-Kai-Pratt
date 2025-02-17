from sqlalchemy import create_engine # Import the create_engine function from the sqlalchemy module
from sqlalchemy.orm import sessionmaker # Import the sessionmaker function from the sqlalchemy.orm module
from models import Base, Question, User # Import the Base and Question classes from the models module
import os

if not os.path.exists("questions.sqlite"):
    engine = create_engine("sqlite:///questions.sqlite", echo=True) # Create an engine that connects to the database file questions.sqlite
    Base.metadata.create_all(engine) # Create the tables in the database
    Session = sessionmaker(bind=engine) # Create a session class that is bound to the engine
    session = Session() # Create a session object

    # Add some questions
    questions = [
        Question(
            question="What is the capital of France?",
            choice_a="Berlin",
            choice_b="Madrid",
            choice_c="Paris",
            choice_d="Rome",
            correct_answer="c"
        ),
        Question(
            question="What is 2 + 2?",
            choice_a="3",
            choice_b="4",
            choice_c="5",
            choice_d="6",
            correct_answer="b"
        ),
        Question(
            question="Who wrote 'To Kill a Mockingbird'?",
            choice_a="Mark Twain",
            choice_b="Harper Lee",
            choice_c="Ernest Hemingway",
            choice_d="F. Scott Fitzgerald",
            correct_answer="b"
        )
    ]

    session.add_all(questions) # Add the questions to the session
    session.commit() # Commit the changes to the database

else:
    print("Questions database already exists. Initialization skipped.")

if not os.path.exists("users.sqlite"):
    engine = create_engine("sqlite:///users.sqlite", echo=True) # Create an engine that connects to the database file users.sqlite
    Base.metadata.create_all(engine) # Create the tables in the database
else:
    print("Users database already exists. Initialization skipped.")