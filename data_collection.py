# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 15:31:18 2023

@author: Tevet
"""

import kayak_scraper as ks
import pandas as pd

departure_city = 'TLV'
destination_city = 'BKK'
start_date = '2023-01-01'
end_date = '2023-06-01'

flight_search = ks.get_flights(departure_city, destination_city, start_date, end_date)