# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 20:25:54 2023

@author: Tevet
"""

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

df = pd.read_csv('Flights_data_cleaned.csv')

# Choose relevant 
df_model = df.drop(['Source','Destination','Year'],axis = 1)

# Get dummy data
df_dum = pd.get_dummies(df_model)

# Train test split
X = df_dum.drop('Price' , axis = 1)
y = df_dum.Price

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=1/3,random_state= 5)

# Multiple linear regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error ,r2_score

lm = LinearRegression()
lm.fit(X_train,y_train)
pred = lm.predict(X_test)

print('MSE for multiple linear regression : ' ,mean_squared_error(pred,y_test))
print('R^2 for multiple linear regression : ',r2_score(y_test, pred))

# Random forest
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators=100)
rf.fit(X_train,y_train)

pred = rf.predict(X_test)

print('MSE for random forest : ' ,mean_squared_error(pred,y_test))
print('R^2 for random forest : ',r2_score(y_test, pred))

# Lasso
from sklearn.linear_model import Lasso
lasso = Lasso()
lasso.fit(X_train,y_train)

pred = lasso.predict(X_test)

print('MSE for Lasso : ' ,mean_squared_error(pred,y_test))
print('R^2 for Lasso : ',r2_score(y_test, pred))
     
# test ensembles
tpred_lm = lm.predict(X_test)
tpred_rf = rf.predict(X_test)
tpred_lasso = lasso.predict(X_test)

mean_absolute_error(y_test,tpred_lm)
mean_absolute_error(y_test,tpred_rf)
mean_absolute_error(y_test,tpred_lasso)

mean_absolute_error(y_test,(tpred_lm+tpred_rf)/2)

