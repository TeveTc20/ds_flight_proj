# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 00:04:00 2023

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
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=1/3,random_state= 4)

# Multiple linear regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error ,r2_score

lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm,X_train,y_train, scoring='neg_mean_absolute_error', cv= 3))

# Lasso
from sklearn.linear_model import Lasso
lm_l = Lasso(alpha=.13)
lm_l.fit(X_train,y_train)
np.mean(cross_val_score(lm_l,X_train,y_train, scoring='neg_mean_absolute_error', cv= 3))

alpha = []
error = []

for i in range(1,100):
    alpha.append(i/100)
    lml = Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lml,X_train,y_train, scoring='neg_mean_absolute_error', cv= 3)))
    
plt.plot(alpha,error)

err = tuple(zip(alpha,error))
df_err = pd.DataFrame(err, columns = ['alpha','error'])
df_err[df_err.error == max(df_err.error)]

# Random forest
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

np.mean(cross_val_score(rf,X_train,y_train,scoring = 'neg_mean_absolute_error', cv= 3))
# tune models GridSearchCV
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,10), 'max_depth':[3,6,9]}

gs = GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error',refit = 'r2',cv=3,verbose = 4)
gs.fit(X_train,y_train)

print(gs.best_score_)
print(gs.best_estimator_)     
# test ensembles
tpred_lm = lm.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

mean_absolute_error(y_test,tpred_lm)
mean_absolute_error(y_test,tpred_lml)
mean_absolute_error(y_test,tpred_rf)

mean_absolute_error(y_test,(tpred_lm+tpred_rf)/2)