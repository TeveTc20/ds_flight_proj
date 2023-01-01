# Data Science Flight ticket prices:Project overview
* Created a tool that estimates flight tickets for desired destinations to help people search good price ticket for their trip.
* Scraped over 1000 flights from kayak using python and selenium.
* Engineered features from the text of each flight to quantify the value airlines put on their flights.
* Optimized Linear, Lasso, and Random Forest Regressors using to reach the best model.

# Code and Resources Used
**Python Version:** 3.9.12
**Packages:** pandas , numpy , matplotlib , seaborn , selenium , sklearn

# Web Scraping
scraped over 1000 flights from kayak.com. With each flight, we got the following:
* Airline name
* Source city
* Destination city
* Duration
* Total stops
* Date
* Departure time
* Arrival time
* Price(in EUROS)

# Date Cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:
* Converte date data to datetime and making new columns that will represent year,month and day.
* Change duration ,Departure time and Arrival time to show only the hour.
* Change Total stops to show only number.
* Taking only the first airline if there is comma between them.
* Removing EURO sign.
* Converting object values columns to int.

# EDA
I looked at the distributions of the data and the value counts for the various categorical variables

# Model Building
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 33%.

I tried three different models and evaluated them using Mean Squared Error and r2 Score . I chosed them because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

I tried three different models:
* **Multiple Linear Regression -** Base for the model.
* **Random Forest -** with the sparsity associated with the data, I thought that this would be a good fit.
* **Lasso Regression -** Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.

# Model Performance
The Random Forest model far outperformed the other approaches on the test and validation sets.
* **Random Forest -** r2 Score = 0.7
* **Multiple Linear Regression-** r2 Score = 0.41
* **Lasso Regression -** r2 Score = 0.25
