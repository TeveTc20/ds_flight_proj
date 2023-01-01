# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 16:44:48 2023

@author: Tevet
"""

import pandas as pd

df = pd.read_csv('TLV_BKK.csv')

##Converte date date to datetime
df['Date'] = pd.to_datetime(df['Date'] , format = '%Y/%m/%d')

##Add year month and day columns
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df.drop('Date',axis = 1 , inplace = True)

##Change duration to show only hour
df['Duration']= df['Duration'].str[:2]
df['Duration']= df['Duration'].str.replace('u','')

##Change totalstops to show only num
df['Total stops'] = df['Total stops'].str[:1]
df['Total stops'] = df['Total stops'].str.replace('d', '0')

##Change Departure time and Arrival time to show only hour
df['Departure time']= df['Departure time'].str[:2]
df['Arrival time']= df['Arrival time'].str[:2]
df['Departure time']= df['Departure time'].str.replace(':','')
df['Arrival time']= df['Arrival time'].str.replace(':','')

##Taking only the first airline if there is comma between them
df['Airline'] = df['Airline'].apply(lambda x : x.split(',')[0])
df['Airline'] = df['Airline'].str.replace('Meerdere maatschappijen','Multiple companies')

##Removing EURO sign
df['Price'] = df['Price'].apply(lambda x : x.split('€')[1])
df['Price'] = df['Price'].str.strip()

##Converting object values columns to int
df['Duration'] = df['Duration'].apply(pd.to_numeric)
df['Total stops'] = df['Total stops'].apply(pd.to_numeric)
df['Departure time'] = df['Departure time'].apply(pd.to_numeric)
df['Arrival time'] = df['Arrival time'].apply(pd.to_numeric)
df['Price'] = df['Price'].apply(pd.to_numeric)

df.to_csv('Flights_data_cleaned.csv',index=False)