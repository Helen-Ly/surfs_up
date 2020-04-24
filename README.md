# Surfs Up

In this project, we ran a few analysis to look at the temperature and precipitation from our weather stations in Oahu. We wanted to get a better idea of the temperature and location to support our business venture of opening a surf and ice cream shop business.

Before going to our meeting with our investors, we thought it would be beneficial to show a seasonal analysis to ensure that our business will sustain itself all year round.

1. Collected temperature observations from all years and all stations for the month of June.
2. Collected temperature observations from all years and all stations for the month of December.
3. Identified key statistical data for June and December using the *describe()* function.

## Resources

  - Data Source: hawaii.sqlite
  - Software: Python 3.7.6, Jupyter Lab 1.2.6, Visual Studio Code 1.43.0
  - Library: Pandas, NumPy, Matplotlib.pyplot, Datetime, Sqlalchemy, Flask

## Summary

**Note:** A detailed summary is provided in the *climate_analysis.ipynb* file.

|    |June tobs|      |December tobs|
|----|---------|------|-------------|
|count| 1700.000000| |1517.000000|
|mean| 74.944118| |71.041529|
|std| 3.257417| |3.745920|
|min| 64.000000| |56.000000|
|25%| 73.000000| |69.000000|
|50%| 75.000000| |71.000000|
|75%| 77.000000| |74.000000|
|max| 85.000000| |83.000000|

As we see above, the temperature difference is around 3-4 degrees Farenheit apart. A Key thing to note is that the standard deviations between the two months are very close.

After collecting these statistics, we wanted to recommend a few questions for further analysis. 

1. Does the temperature fluctuate? If so, how often? Does the temperature affect if the customer will buy ice cream or not?
2. What is the weather like? Sunny, cloudy, rainy? Does this happen all day, or is it intermittent?
3. What is the location of the shop? On the street or on the beach?
4. What is the structure like? Will their be seating or a patio?

All these questions will lead us to the bigger question, how will this affect our customers? As a result, this will help us develop a strong and convincing presentation to our investors as we will cover all aspects of the business and an all year round understanding of how the business will run.

## Usage

**Note:** Please ensure you have all the required and updated softwares on your computer.

1. Download the following files into the same folder for the project.

  - hawaii.sqlite
  - climate_analysis.ipynb
  - app.py
  
2. In your Anaconda prompt, activate your development environment and navigate to the folder holding the above files and run Jupyter Lab or Jupyter Notebook.
3. Ensure that you have the required libraries installed, such as *sqlalchemy*. In not, open another Anaconda terminal and install the library within your development environment.
4. Please ensure that you are running Jupyter Lab/Notebook in your folder holding the files. If not, you will need to changing the path to the *hawaii.sqlite* file.
5. If you would like to try the Flask webpage, open *app.py* in Visual Studio Code. Ensure you have Flask installed. In not, follow step #3, and type "pip install Flask".
6. In your Anaconda prompt (inside your development environment), navigate to the project folder and type "python app.py".
7. This will run the file and provide you with a URL. Copy and paste it into your browser. You can copy and paste the paths in the homepage to the end of your URL to access the data.
8. The last path will provide you with data if you input dates in place of the "start" and "end" in the following format without quotations, YYYY-MM-DD.
