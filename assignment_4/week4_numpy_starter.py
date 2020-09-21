# Starter code for Homework 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week4.txt'
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

# Make a numpy array of this data
flow_data = data[['year', 'month','day', 'flow']].to_numpy()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Starter Code
# Count the number of values with flow > 600 and month ==7
flow_count = np.sum((flow_data[:,3] > 600) & (flow_data[:,1]==9))

# this gives a list of T/F where the criteria are met
(flow_data[:,3] > 600) & (flow_data[:,1]==9)

# this give the flow values where that criteria is met
flow_pick = flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==9), 3]

# this give the year values where that criteria is met
year_pic = flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==9), 0]

# this give the all rows  where that criteria is met
all_pic = flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==9), ]

# Calculate the average flow for these same criteria 
flow_mean = np.mean(flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==9),3])

print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")

# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=15)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
plt.hist(flow_data[:,3], bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# Get the quantiles of flow
# Two different approaches ---  you should get the same answer
# just using the flow column
flow_quants1 = np.quantile(flow_data[:,3], q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants1)
# Or computing on a colum by column basis 
flow_quants2 = np.quantile(flow_data, q=[0,0.1, 0.5, 0.9], axis=0)
# and then just printing out the values for the flow column
print('Method two flow quantiles:', flow_quants2[:,3])
# %% Q2. Data type

# print(type(flow_data[:,1]))
print(flow_data.ndim) # the number of dimensions
print(flow_data.shape[0]) # the size of each dimension
print(flow_data.size) # the total size of the array
print("dtype:", flow_data[:,0].dtype)

# %% Weekly Forecast
# this give the flow values week 1 and sedt criteria
av_week1 = []
av_pweek1 = []
m_sp_wk1 = []

star_d = 22
end_d = 28
mon = 11

flow_week1 = flow_data[(flow_data[:,0] == 2019) & (flow_data[:,1]==mon) & (flow_data[:,2]>=star_d) & (flow_data[:,2]<=end_d), 3]
print(flow_week1)
print(np.mean(flow_data[(flow_data[:,0] == 2019) & (flow_data[:,1]==mon) & (flow_data[:,2]>=star_d) & (flow_data[:,2]<=end_d), 3]))
av_week1=(np.mean(flow_data[(flow_data[:,0] == 2019) & (flow_data[:,1]==mon) & (flow_data[:,2]>=star_d) & (flow_data[:,2]<=end_d), 3]))

flow_week1_sp = flow_data[(flow_data[:,1]==mon) & (flow_data[:,2]>=(star_d-7)) & (flow_data[:,2]<=(star_d-1)), 3]
print(flow_week1_sp)

# flow_pweek1 = flow_data[(flow_data[:,0] == 2020) & (flow_data[:,1]==9) & (flow_data[:,2]<=19) & (flow_data[:,2]>=13), 3]
#av_pweek1 = flow_data[(flow_data[:,0] == 2019) & (flow_data[:,1]==9) & (flow_data[:,2]>=27) & (flow_data[:,2]<=30), 3]
#print(av_pweek1)

# print(np.mean(flow_data[(flow_data[:,0] == 2019) & (flow_data[:,1]==9) & (flow_data[:,2]<=19) & (flow_data[:,2]>=13), 3]))
av_pweek1 = (np.mean(flow_data[(flow_data[:,0] == 2019) & (flow_data[:,1]==mon) & (flow_data[:,2]<=end_d) & (flow_data[:,2]>=star_d), 3]))
print("mean",av_pweek1)


# % Weekly Forecast
# this give the flow values week 1

 # Count the number of values with flow > 600 and month ==7
fll_ct_sp = np.sum(flow_week1_sp > av_pweek1)

# this gives a list of T/F where the criteria are met
# (flow_data[:,3] > 600) & (flow_data[:,1]==9)

# this give the flow values where that criteria is met
fl_pick_so = flow_data[(flow_data[:,3] > av_pweek1) & (flow_data[:,1]==mon), 3]

# this give the year values where that criteria is met
year_pic = flow_data[(flow_data[:,3] > av_pweek1) & (flow_data[:,1]==mon), 0]

# this give the all rows  where that criteria is met
all_pic = flow_data[(flow_data[:,3] > av_pweek1) & (flow_data[:,1]==mon), ]

# Calculate the average flow for these same criteria 
flow_mean_sp = np.mean(flow_data[(flow_data[:,3] > av_pweek1) & (flow_data[:,1]==mon),3])

std_sp = np.std(flow_data[(flow_data[:,3] >= av_pweek1) & (flow_data[:,1]==mon) & (flow_data[:,0]<=2019) & (flow_data[:,0]>=2005),3])
# % Make a histogram of data
# %
print("Flow meets this critera", fll_ct_sp, " times")
print('And has an average value of', flow_mean_sp, "when this is true")
print('And has a standard deviation value of', std_sp, "when this is true")


# Use the linspace  funciton to create a set  of evenly spaced bins
mybins_sp = np.linspace(0, 900, num=10)
# another example using the max flow to set the upper limit for the bins
# mybins_sp = np.linspace(0, np.max(flow_week1_sp), num=15) 
#Plotting the histogram
plt.hist(flow_week1_sp, bins = mybins_sp)
plt.title('Streamflow September 27-30 since 1989')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
plt.savefig('week_test.png')

# Get the quantiles of flow
# Two different approaches ---  you should get the same answer
# just using the flow column
flow_quants1 = np.quantile(flow_week1_sp, q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants1)
# Or computing on a colum by column basis 
flow_quants2 = np.quantile(flow_week1_sp, q=[0,0.1, 0.5, 0.9], axis=0)
# and then just printing out the values for the flow column
print('Method two flow quantiles:', flow_quants2)

# %% Q3. 
av_1 = 68
av_2 = 80

sp_flow_all = flow_data[(flow_data[:,1]==9) & (flow_data[:,0]>=2010), 3]
gr_fl_sp_wk1 = np.sum((sp_flow_all > av_1) )
per_flow_1 = 100*(gr_fl_sp_wk1/len(sp_flow_all))

gr_fl_sp_wk2 = np.sum((sp_flow_all > av_2) )
per_flow_2 = 100*(gr_fl_sp_wk2/len(sp_flow_all))

print("Times daily value is greater than my mean:",gr_fl_sp_wk1,"from a total of: ",len(sp_flow_all),"times.")
print("Percentage",per_flow_1)

print("Times daily value is greater than my mean:",gr_fl_sp_wk2,"from a total of: ",len(sp_flow_all),"times.")
print("Percentage",per_flow_2)

# %% Q5

fl_1_sp = flow_data[(flow_data[:,1]==9) & (flow_data[:,2]>=1) & (flow_data[:,2]<=15), 3]
fl_2_sp = flow_data[(flow_data[:,1]==9) & (flow_data[:,2]>=16) & (flow_data[:,2]<=30), 3]


# Use the linspace  funciton to create a set  of evenly spaced bins
mybins_sp = np.linspace(0, 1000, num=10)
# another example using the max flow to set the upper limit for the bins
# mybins_sp = np.linspace(0, np.max(flow_week1_sp), num=15) 
#Plotting the histogram
plt.hist(fl_1_sp, bins = mybins_sp)
plt.title('Streamflow September 1-15 since 1989')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
plt.savefig('sepu1.png')
# %%
plt.hist(fl_2_sp, bins = mybins_sp)
plt.title('Streamflow September 16-30 since 1989')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')
plt.savefig('sepu2.png')

# %%
