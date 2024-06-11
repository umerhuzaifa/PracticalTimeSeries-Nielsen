# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 12:47:01 2023

@author: MHUZAIFA
"""

import pandas as pd
import math as math
import plotly as px
import matplotlib.pyplot as plt

# date time range
time_range = pd.date_range(start = '1990 May 12', end='2023 August 20', freq = 'Y')

pd.DataFrame()
# A simple data container using Pandas
data_example = pd.Series([x**2 for x in range(1, 6)])
data_example.index = [x for x in range(1, 6)]


# angle_range = [-math.pi:math.pi/10:math.pi]

angle_range = pd.Series([-math.pi+math.pi/10*x for x in range(0, 21)])
sinusoidal_data = pd.Series([math.cos(x) for x in angle_range])

fig, axes = plt.subplots(nrows=3, ncols=1)


# data_example.plot(ax = axes[0])

axes[0].plot(data_example)

axes[1].plot(angle_range)
sinusoidal_data.plot(x=angle_range, ax = axes[2])
# axes[2].plot(angle_range,sinusoidal_data)
# axes[2].plot()

# sinusoidal_data.plot()
# px.plot(sinusoidal_data)

# angle_range.plot(ax = axes[2])


# plt.show()


