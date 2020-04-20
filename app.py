# Import dependencies
from flask import Flask # Enables access to Flask

# Create a new flask app instance
# 'instance' refers to a singular version of something
app = Flask(__name__)

# Create our first flask route
# Defining our starting point (also known as the root)
@app.route('/') # forward slash denotes we want to put our data at the root of our routes

# Create function called 'hello world'
def hello_world():
    return 'Hello world'

# Set the environment variable to the name of our flask file
# Write the following below in Anaconda powershell
# export FLASK_APP = app.py # MAC users
# $env: FLASK_APP = 'app.py' #Windows users

# Skill Drill: create another route
@app.route('/weather')
def weather_today():
    return 'The weather today is sunny.'