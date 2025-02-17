# Description: This file contains the model for the questions table in the database.

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() # Base class for the model

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True) # Primary key
    name = Column(String, nullable=False)
    score = Column(Integer, nullable=False)


class Question(Base): # Model for the questions table
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True) # Primary key
    question = Column(String, nullable=False)
    choice_a = Column(String, nullable=False)
    choice_b = Column(String, nullable=False)
    choice_c = Column(String, nullable=False)
    choice_d = Column(String, nullable=False)
    correct_answer = Column(String, nullable=False) # The correct answer to the question (a, b, c, or d)