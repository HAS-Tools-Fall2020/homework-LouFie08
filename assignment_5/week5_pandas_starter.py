# Example solution for HW 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week6.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# filepath = '../Assignments/Solutions/data/streamflow_week1.txt'

# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Sorry no more helpers past here this week, you are on your own now :) 
# Hints - you will need the functions: describe, info, groupby, sort, head and tail.

# %% Q1. Data frames properties.
cn = data.columns # Column names
print(cn)
idx = data.index # index
print(idx)
dt = data.dtypes
print(dt)
# %% Q2. min, mean, max, standard deviation and quartiles.

des = data.iloc[:,3].describe() # To get description of the dataframe
print("The min value from the flow data is: ",des["min"])
print("The mean value from the flow data is: ",des["mean"])
print("The max value from the flow data is: ",des["max"])
print("The standard deviation value from the flow data is: ",des["std"])
print("The 1st quartile (25%) is: ",des["25%"],"he 2nd quartile (50%) is: ",des["50%"], ", and the 3rd quartile (75%) is: ",des["75%"])

# %% Q3. same information but on a monthly basis
d_m = data.groupby(["month"])[["flow"]].describe()
print(d_m)

# %% Q4. 5 highest and 5 lowest flow values for the period of record. 
# Include the date, month and flow values in your summary.
no = 6
min_max = data.sort_values(by="flow",ascending=True)
print(min_max[0:no:1])
max_min = data.sort_values(by="flow",ascending=False)
print(max_min[0:no:1])

# %% Q5. Find the highest and lowest flow values for every month of the year 
# (i.e. you will find 12 maxes and 12 mins) and report back what year these occurred in
# January
J_sf_min = data[data["month"]==1].sort_values(by="flow",ascending=True)
m_min = J_sf_min.iloc[0]['year'],J_sf_min.iloc[0]['flow']
m_max = J_sf_min.iloc[-1]['year'],J_sf_min.iloc[-1]['flow']
print(m_min,m_max)

# February
F_sf_min = data[data["month"]==2].sort_values(by="flow",ascending=True)
m_min = F_sf_min.iloc[0]['year'],F_sf_min.iloc[0]['flow']
m_max = F_sf_min.iloc[-1]['year'],F_sf_min.iloc[-1]['flow']
print(m_min,m_max)

# March
M_sf_min = data[data["month"]==3].sort_values(by="flow",ascending=True)
m_min = M_sf_min.iloc[0]['year'],M_sf_min.iloc[0]['flow']
m_max = M_sf_min.iloc[-1]['year'],M_sf_min.iloc[-1]['flow']
print(m_min,m_max)

# April
Ap_sf_min = data[data["month"]==4].sort_values(by="flow",ascending=True)
m_min = Ap_sf_min.iloc[0]['year'],Ap_sf_min.iloc[0]['flow']
m_max = Ap_sf_min.iloc[-1]['year'],Ap_sf_min.iloc[-1]['flow']
print(m_min,m_max)

# May
Ma_sf_min = data[data["month"]==5].sort_values(by="flow",ascending=True)
m_min = Ma_sf_min.iloc[0]['year'],Ma_sf_min.iloc[0]['flow']
m_max = Ma_sf_min.iloc[-1]['year'],Ma_sf_min.iloc[-1]['flow']
print(m_min,m_max)

# June
Jn_sf_min = data[data["month"]==6].sort_values(by="flow",ascending=True)
m_min = Jn_sf_min.iloc[0]['year'],Jn_sf_min.iloc[0]['flow']
m_max = Jn_sf_min.iloc[-1]['year'],Jn_sf_min.iloc[-1]['flow']
print(m_min,m_max)

# July
Jl_sf_min = data[data["month"]==7].sort_values(by="flow",ascending=True)
m_min = Jl_sf_min.iloc[0]['year'],Jl_sf_min.iloc[0]['flow']
m_max = Jl_sf_min.iloc[-1]['year'],Jl_sf_min.iloc[-1]['flow']
print(m_min,m_max)

# August
Ag_sf_min = data[data["month"]==8].sort_values(by="flow",ascending=True)
m_min = Ag_sf_min.iloc[0]['year'],Ag_sf_min.iloc[0]['flow']
m_max = Ag_sf_min.iloc[-1]['year'],Ag_sf_min.iloc[-1]['flow']
print(m_min,m_max)

# September
Sp_sf_min = data[data["month"]==9].sort_values(by="flow",ascending=True)
m_min = Sp_sf_min.iloc[0]['year'],Sp_sf_min.iloc[0]['flow']
m_max = Sp_sf_min.iloc[-1]['year'],Sp_sf_min.iloc[-1]['flow']
print(m_min,m_max)

# October
Oc_sf_min = data[data["month"]==10].sort_values(by="flow",ascending=True)
m_min = Oc_sf_min.iloc[0]['year'],Oc_sf_min.iloc[0]['flow']
m_max = Oc_sf_min.iloc[-1]['year'],Oc_sf_min.iloc[-1]['flow']
print(m_min,m_max)

# November
Nv_sf_min = data[data["month"]==11].sort_values(by="flow",ascending=True)
m_min = Nv_sf_min.iloc[0]['year'],Nv_sf_min.iloc[0]['flow']
m_max = Nv_sf_min.iloc[-1]['year'],Nv_sf_min.iloc[-1]['flow']
print(m_min,m_max)

# December
Dc_sf_min = data[data["month"]==12].sort_values(by="flow",ascending=True)
m_min = Dc_sf_min.iloc[0]['year'],Dc_sf_min.iloc[0]['flow']
m_max = Dc_sf_min.iloc[-1]['year'],Dc_sf_min.iloc[-1]['flow']
print(m_min,m_max)

# %% Q6. Provide a list of historical dates with flows that are within 10%
# of your week 1 forecast value. If there are none than increase the 
# %10 window until you have at least one other value and report the
# date and the new window you used

WK_1_pd = 73
WK_2_pd = 68
pr = .10

F_pc = data[(data["flow"]<=WK_1_pd*(1+pr)) & (data["flow"]>=WK_1_pd*(1-pr))]
print(F_pc)
# %% Forecast Weeks 1 and 2

# last weak values
l_w = data[(data["month"]==9) &  (data["day"]>=20) & (data["day"]<=26) & (data["year"]==2020)]
print(l_w.describe())

l_w_all = data[(data["month"]==9) &  (data["day"]>=20) & (data["day"]<=26)]
print(l_w_all.describe())

week_1_1 = data[(data["month"]==9) & (data["day"]>=27)]
week_1_2 = data[(data["month"]==10) & (data["day"]<=3)]
print(week_1_1.describe())
print(week_1_2.describe())

week_2 = data[(data["month"]==10) & (data["day"]>=4) & (data["day"]<=10)]
print(week_2.describe())
# %% Forecast Seasonal
w1 = data[(data["month"]==8) & (data["day"]>=22) & (data["day"]<=29)]
print(w1.describe())
wk1_pr = 57.8

w2 = data[(data["month"]==9) & (data["day"]>=1) & (data["day"]<=5)]
print(w2.describe())
wk2_pr = 55.5

w3 = data[(data["month"]==9) & (data["day"]>=6) & (data["day"]<=12)]
print(w3.describe())
wk3_pr = 56.5

w4 = data[(data["month"]==9) & (data["day"]>=13) & (data["day"]<=19)]
print(w4.describe())
wk4_pr = 57.5

w5 = data[(data["month"]==9) & (data["day"]>=20) & (data["day"]<=26)]
print(w5.describe())
wk5_pr = 60.2

w6 = data[(data["month"]==9) & (data["day"]>=27) & (data["day"]<=30)]
print(w6.describe())
wk6_pr = 77.5

w7 = data[(data["month"]==10) & (data["day"]>=4) & (data["day"]<=10)]
print(w7.describe())
wk7_pr = 74

w8 = data[(data["month"]==10) & (data["day"]>=11) & (data["day"]<=17)]
print(w8.describe())
wk8_pr = 83.5

w9 = data[(data["month"]==10) & (data["day"]>=18) & (data["day"]<=24)]
print(w9.describe())
wk9_pr = 80.5

w10 = data[(data["month"]==10) & (data["day"]>=25) & (data["day"]<=31)]
print(w10.describe())
wk10_pr = 89.5

w11 = data[(data["month"]==11) & (data["day"]>=1) & (data["day"]<=7)]
print(w11.describe())
wk11_pr = 125.5

w12 = data[(data["month"]==11) & (data["day"]>=8) & (data["day"]<=14)]
print(w12.describe())
wk12_pr = 135.5

w13 = data[(data["month"]==11) & (data["day"]>=15) & (data["day"]<=21)]
print(w13.describe())
wk13_pr = 142.8

w14 = data[(data["month"]==11) & (data["day"]>=22) & (data["day"]<=28)]
print(w14.describe())
wk14_pr = 150.5

w15 = data[(data["month"]==12) & (data["day"]>=1) & (data["day"]<=5)]
print(w15.describe())
wk15_pr = 168.5

w16 = data[(data["month"]==12) & (data["day"]>=6) & (data["day"]<=12)]
print(w16.describe())
wk16_pr = 174.3
# %%
