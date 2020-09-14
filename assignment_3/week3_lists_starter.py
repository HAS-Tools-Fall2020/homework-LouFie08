# Start code for assignment 3
# this code sets up the lists you will need for your homework
# and provides some examples of operations that will be helpful to you

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week3.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

#make lists of the data
flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Here is some starter code to illustrate some things you might like to do
# Modify this however you would like to do your homework. 
# From here on out you should use only the lists created in the last block:
# flow, date, yaer, month and day

# Calculating some basic properites
print("The min flow value in record is ",min(flow))
print("The max flow value in record is ",max(flow))
print("The mean flow value in all the data is ", np.mean(flow))
print("The std deviation value in all the data is ", np.std(flow))
# %%
# Making and empty list that I will use to store
# index values I'm interested in
ilist = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
for i in range(len(flow)):
        if flow [i] > 600 and month[i] == 9: # September
                ilist.append(i)

# see how many times the criteria was met by checking the length
# of the index list that was generated
print(len(ilist))

# Alternatively I could have  written the for loop I used 
# above to  create ilist like this
ilist2 = [i for i in range(len(flow)) if flow[i] > 600 and month[i]==9] # September
print(len(ilist2))

# Grabbing out the data that met the criteria
# This  subset of data is just the elements identified 
# in the ilist
subset = [flow[j] for j in ilist]

# %% Weekly data
# Create empty list for weekly data
mflow = []
mday = []
wflow = []

# Loop data per month
for j in range(len(flow)):
        # if month [j] == 9 and year[j] <= 2019 and year[j] >= 2015: # September
        if month [j] == 9 and year[j] == 2019 : # September
                mflow.append(flow[j])
                mday.append(day[j])

# Print montlhy flow
# print(mflow)

# Loop data per week
for k in range(len(mflow)):
        # if mday [k] >= 13 and mday[k] <= 19: # September
        if mday [k] >= 20 and mday[k] <= 26: # September
                wflow.append(mflow[k])

# Print montlhy flow
print(wflow)

# Calculating some basic properites
print("The min flow value in the week is ",min(wflow))
print("The max flow value in the week is ",max(wflow))
print("The mean flow value for the week is ", np.mean(wflow))
print("The std deviation value for the week is ", np.std(wflow))

f_week1 = 43.5
f_week2 = 57.5

# %% Variables information Q1
#  
t_f = type(flow[1])
l_f = len(flow)
print(t_f)
print(l_f)

t_y = type(year[1])
l_y = len(year)
print(t_y)
print(l_y)

t_m = type(month[1])
l_m = len(month)
print(t_m)
print(l_m)

t_d = type(day[1])
l_d = len(day)
print(t_d)
print(l_d)


# %% Percentage for daily flow above my estimation
# Making and empty list that I will use to store
# index values I'm interested in
w1_seplist = []
t_sep = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
for l in range(len(flow)):
        if flow [l] >= f_week2 and month[l] == 9: # September
                w1_seplist.append(l)

# Total of days in september for the total data period

for m in range(len(flow)):
        if month[m] == 9: # September
                t_sep.append(l)

# see how many times the criteria was met by checking the length
# of the index list that was generated
w1_per = (len(w1_seplist)/len(t_sep))*100
print("The percentage where the daily flow in September is greater than my prediction is",w1_per)
print("The total number of times where the daily flow in September is greater than my prediction is ",len(w1_seplist))



# %% Question 3

# Making and empty list that I will use to store
# index values I'm interested in
w1_seplist_2000 = []
t_sep_2000 = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
for n in range(len(flow)):
        if flow [n] >= f_week2 and month[n] == 9 and year[n] >= 2000: # September
                w1_seplist_2000.append(n)

# Total of days in september for the total data period

for o in range(len(flow)):
        if month[o] == 9 and year[o] >= 2000: # September
                t_sep_2000.append(o)

# see how many times the criteria was met by checking the length
# of the index list that was generated
w1_per_2000 = (len(w1_seplist_2000)/len(t_sep_2000))*100
print("The percentage where the daily flow in September (after year 2000) is greater than my prediction is",w1_per_2000)
print("The total number of times where the daily flow in September (after year 2000) is greater than my prediction is ",len(w1_seplist_2000))

# %% Question 4

# Making and empty list that I will use to store
# index values I'm interested in
msp_1 = []
ysp_1 = []
wflow_sp_1 = []
msp_2 = []
ysp_2 = []
wflow_sp_2 = []

# Loop data per month
for p in range(len(flow)):
        # if month [j] == 9 and year[j] <= 2019 and year[j] >= 2015: # September
        if month [p] == 12 and year[p] == 2012 : # September
                msp_1.append(flow[p])
                ysp_1.append(day[p])
                msp_2.append(flow[p])
                ysp_2.append(day[p])

# Print montlhy flow
# print(mflow)

# Loop data per week
for o in range(len(msp_1)):
        # if mday [k] >= 13 and mday[k] <= 19: # September
        if ysp_2 [o] >= 6 and ysp_2[o] <= 12: # September
                wflow_sp_1.append(msp_1[o])
        if ysp_1 [o] >= 1 and ysp_1[o] <= 5: # September
                wflow_sp_2.append(msp_2[o])

# Calculating some basic properites
print("The min flow value in the week is ",min(wflow_sp_1))
print("The max flow value in the week is ",max(wflow_sp_1))
print("The mean flow value for the week is ", np.mean(wflow_sp_1))
print("The std deviation value for the week is ", np.std(wflow_sp_1))

print("The min flow value in the week is ",min(wflow_sp_2))
print("The max flow value in the week is ",max(wflow_sp_2))
print("The mean flow value for the week is ", np.mean(wflow_sp_2))
print("The std deviation value for the week is ", np.std(wflow_sp_2))

# %%
