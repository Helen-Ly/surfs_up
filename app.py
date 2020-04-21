# Import our dependencies
import datetime as dt
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#--------------------
# Set up the database
#--------------------

# Set up database engine for the Flask application
engine = create_engine('sqlite:///hawaii.sqlite') # Allows us access/query the db

# Reflect the db into our classes
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect = True)

# Save our references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

#-------------
# Set up Flask
#-------------

# Create a Flask application called 'app'
app = Flask(__name__)

# Define our welcome route
@app.route('/')

# Display f-strings as a reference to all of our other routes
# When creating routes, we follow the naming convention /api/v1.0/ + route name
# v1.0 signifies version 1 of our application
def welcome():
    return( 
    '''
    Welcome to the Climate Analysis API! <br>
    Available Routes: <br>
    /api/v1.0/precipitation <br>
    /api/v1.0/stations <br>
    /api/v1.0/tobs <br>
    /api/v1.0/temp/start/end <br>
    ''')

# Create precipitation Route
@app.route('/api/v1.0/precipitation')

# Create precipitation function
def precipitation():

    # Add code that calculates the date one year ago from the most recent date in db
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)

    # Add query to get the date and precipitation from the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()

    # Use jsonify() to format our results into a JSON structured file
    precip = {date:prcp for date,prcp in precipitation}

    # Return jsonify(precip)
    return jsonify(precip)

# Create stations route
@app.route('/api/v1.0/stations')

# Create stations functions
def stations():

    # Add query to get all stations in our db
    results = session.query(Station.station).all()

    # Convert our unraveled results into a list
    stations = list(np.ravel(results))

    return jsonify(stations)

# Create temperature observations route
@app.route('/api/v1.0/tobs')

# Create tobs function
def temp_monthly():

    # Add code that calculates the date one year ago from the most recent date in db
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)

    # Query the primary station for all the tobs from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
            filter(Measurement.date >= prev_year).all()

    # Unravel results into a one-dimensional array and convert to a list
    temps = list(np.ravel(results))
    
    return jsonify(results)

# Create statistics route
@app.route('/api/v1.0/temp/<start>')
@app.route('/api/v1.0/temp/<start>/<end>')

# Create stats function with start and end parameters
def stats(start = None, end = None):

    # Create list with min, max, and avg
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # Add if-not statement, the * indicates there are multiple results for this query
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
    
    # Create query to get our stats data
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    
    # Unravel results and convert to a list
    temps = list(np.ravel(results))
    
    return jsonify(temps)