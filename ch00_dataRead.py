# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:39:27 2023

@author: MHUZAIFA
"""

#%%
# A script file for practising reading ahe data files 
# in CSV file format or txt file formats

# Umer Huzaifa 
# August 18, 2023


import pandas as pd

import matplotlib.pyplot as plt


fig, axes = plt.subplots(nrows=2, ncols = 3, figsize=(12, 8))


data_passengers = pd.read_csv('data/AirPassengers.csv')

data_passengers.index = pd.Series(data_passengers.iloc[:,0]) 


# data_passengers.plot()


axes[0, 0].plot(data_passengers.iloc[:,0], data_passengers.iloc[:,1])
axes[0,0].set_title('Passengers Over the Years')

data_donation = pd.read_csv('data/donations.csv')
axes[0, 1].plot(data_donation.iloc[:,2], data_donation.iloc[:,0])
axes[0,1].set_title('Donations Per User')

data_emails = pd.read_csv('data/emails.csv')

axes[0, 2].plot(data_emails.iloc[:,1], data_emails.iloc[:,0])
axes[0,2].set_title('Emails Opened Per User')

data_unrate = pd.read_csv('data/UNRATE.csv')
axes[1, 0].plot(data_unrate.iloc[:,0], data_unrate.iloc[:,1])
axes[1, 0].set_title('Unemployment Rate Every Year')

data_yearJoined = pd.read_csv('data/year_joined.csv')
axes[1, 1].plot(data_yearJoined.iloc[:,0], data_yearJoined.iloc[:,2])
axes[1, 1].set_title('Members Joining Every Year')
axes[1, 2].plot(data_yearJoined.iloc[:,0], data_yearJoined.iloc[:,1])
axes[1, 2].set_title('Membership Status')
plt.show()

