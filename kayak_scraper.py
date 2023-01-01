# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import numpy as np
from tqdm import tqdm

def get_flights(source,destination,start_dates,end_dates):
    chromedriver_path = 'C:\Windows\chromedriver_win32\chromedriver.exe'

    driver = webdriver.Chrome(chromedriver_path)

    sources = source
    destinations = destination
    print("\nRoute:")
    print(f"{source} => {destination}")
        

    start_date = np.datetime64(start_dates)
    end_date = np.datetime64(end_dates)
    days = end_date - start_date
    num_days = days.item().days

    def get_airlines(soup):
        airline = []
        airlines = soup.find_all('span',class_='codeshares-airline-names',text=True)
        for i in airlines:
            airline.append(i.text)

        return airline
        
    def get_total_stops(soup):
        stops_list = []
        stops = soup.find_all('div',class_='section stops')

        for i in stops:
            for j in i.find_all('span',class_='stops-text'):
                   stops_list.append(j.text)
        
        return stops_list

    def get_price(soup):
        prices = []
        price = soup.find_all('div',class_='Flights-Results-FlightPriceSection right-alignment sleek')

        for i in price:
            for j in i.find_all('span', class_='price-text'):
                prices.append(j.text)
        
        return prices

    def get_duration(soup):
        duration_list = []
        duration = soup.find_all('div' , class_='section duration allow-multi-modal-icons')
        for i in duration:
            for j in i.find_all('div',class_='top'):
                duration_list.append(j.text)
        
        return duration_list
    
    def get_dep_time(soup):
        dep_list = []
        dep = soup.find_all('div',class_='section times')
        for i in dep:
            for j in i.find_all('span',class_='depart-time base-time'):
                dep_list.append(j.text)
        return dep_list
    
    def get_arr_time(soup):
        arr_list = []
        arr = soup.find_all('div',class_='section times')
        for i in arr:
            for j in i.find_all('span',class_='arrival-time base-time'):
                arr_list.append(j.text)
        return arr_list

    for i in range(1):
        column_names = ["Airline", "Source", "Destination","Duration" ,"Total stops","Date","Departure time","Arrival time","Price"]
        df = pd.DataFrame(columns = column_names)
        for j in tqdm(range(num_days+1)):
            
            # close and open driver every 10 days to avoid captcha
            if j % 10 == 0:
                driver.quit()
                driver = webdriver.Chrome(chromedriver_path)
                
                
            url = f"https://www.kayak.nl/flights/{sources}-{destinations}/{start_date+j}"
            driver.get(url)
            sleep(10)
            
            if j % 10 == 0:
                popup_window = '//div[@class = "dDYU-close dDYU-mod-variant-default dDYU-mod-size-default"]'
                driver.find_element_by_xpath(popup_window).click()
        
            
        
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            airlines = get_airlines(soup)
            total_stops = get_total_stops(soup)
            prices = get_price(soup)
            duration = get_duration(soup)
            departure = get_dep_time(soup)
            arrival = get_arr_time(soup)
            df = df.append(pd.DataFrame({
                'Airline': airlines,
                'Duration': duration,
                'Total stops' : total_stops,
                'Date' : start_date+j,
                'Departure time' : departure,
                'Arrival time' : arrival,
                'Price' : prices
                                        }))
            
        df['Source'] = sources
        df['Destination'] = destinations
        df = df.replace('\n','', regex=True)
        df = df.reset_index(drop = True)
        
        # save data as csv file for each route
        df.to_csv(f'{sources}_{destinations}.csv',index=False)
        print(f"Succesfully saved {sources} => {destinations} route as {sources}_{destinations}.csv ")
        
    driver.quit()
    