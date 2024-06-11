# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:09:24 2023

@author: MHUZAIFA
"""

#%% A script for doing data cleaning such as smoothing operation using techniques
# like moving average, low pass filtering etc.

# Umer Huzaifa
# August 21, 2023

import pandas as pd
import matplotlib.pyplot as plt

data_raw_pass = pd.read_csv('data/AirPassengers.csv',delimiter=',')

data_raw_pass.columns = ['Year-Month', 'Number']

data_raw_pass.index = pd.Series(data_raw_pass.iloc[:,0]) 


data_raw_pass['Smooth0.5']= data_raw_pass['Number'].ewm(alpha=0.6).mean()

# data_passengers.plot()

fig, axes = plt.subplots(nrows = 2, ncols = 2)

axes[0,0].plot(data_raw_pass['Number'])
axes[0,0].set_title('Raw Passengers Over the Years')

axes[0,0].plot(data_raw_pass['Smooth0.5'])
plt.show()


