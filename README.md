[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18234699)
# Trivia
This is a simple trivia app for learning the basics of SQL Alchemy.

Work through the following sections in order:
1. [Walkthrough](#walkthrough)
2. [Your Task](#your-task)
3. [Challenge](#challenge)

## Walkthrough 

Have a look through all the files to get an idea of how it goes together. 

### 1. index.html
Using html and jinja that we're familiar with, this page displays the questions as a form, designed to submit via POST to the url assosiated with the submit route. 

### 2. results.html
This page lets you know how you did. 

### 3. models.py
Here we define the `question` class, which extends from the `base` class that we imported (this is an OOP approach). Look at what has been imported here, and see where each bit has been used in defining the structure of a question in our database. 

### 4. init_db.py
At the top, we import a few tools, as well as the `models` we defined. 

We create the database, add the table, and create a `session` object. This may seem like a lot, but it will become more familiar with time. Read through the code to get an idea of what it does:

```python
engine = create_engine("sqlite:///questions.sqlite", echo=True) # Create an engine that connects to the database file questions.sqlite
Base.metadata.create_all(engine) # Create the tables in the database
Session = sessionmaker(bind=engine) # Create a session class that is bound to the engine
session = Session() # Create a session object
```

We then make a list of questions, add them to the session object, and commit our changes.

### 5. app.py

After our imports and defining our app, you'll notice the same boilerplate for linking to the database and creating a session. 

In out routes, we are now using `session.query(Question).all()` to grab all the questions in the `questions` table. 

Everything else is pretty straigtforward. 

Go ahead and run `init_db.py` to create and populate the databse, then fire up your flask app to see if everything is working. 


## Your Task 
Lets record the score from each attempt and create a high score page. This is not using user accounts or anything fancy - more like a simple pinball-machine stile high schore page.

### 1. Getting the user's name

Let's start by giving the user somewhere to add their name with their attempt. 

```html
<div>
    <label for="name">Enter your name:</label>
    <input type="text" id="name" name="name" required>
</div>
```
This will provide an input like this:

<div>
    <label for="name">Enter your name:</label>
    <input type="text" id="name" name="name" required>
</div>

### 2. Giving us somewhere to store it

Jump into the `models.py` file, and add a new `class` called `User`, that extends from `Base` in the same way that the `Question` class does already.

Using the `Question` class as a template, add a `tablename` (users), an `id` column, a `name` column and a `score` column. 

### 3. Update app.py
`app.py` will need access to the new model:
```python
#app.py
from models import Base, Question, User
```
In the `submit()` route, you will need to get the user's name from the POST request, and initialise a `score` variable:
```python
name = request.form.get("name")
score = 0
```

Inside your `for` loop, increment your score for each question that is answered correctly:
```python 
score += 1 
```

And most importantly, store the attempt in the database! 

We will create a new user object (using the `User` class we imported earlier), add the user to the session, and then commit our change to the database. 

```python
# Create a new User object
user = User(name=name, score=score) 
# Add the user to the session
session.add(user) 
# Commit the changes to the database
session.commit() 
```

### 4. Display the results!
Show the results of this attempt by rendering the template:

```python
return render_template("results.html", name=name, score=score)
```
Addinng something like this in `results.html`:
```html

    <h1>Results</h1>
    <p>Thank you, {{ name }}!</p>
    <p>Your score: {{ score }}</p>
    <a href="{{ url_for('index') }}">Try Again</a>
```

## Challenge

Once you have this working, your next challenges are:
1. Add a leaderboard! (You'll probably want more questions)
2. Add functionality to delete anyone below the top 10 high scores to avoid the database growing too big.
3. Implement the ability to add new questions into the quiz app! 
