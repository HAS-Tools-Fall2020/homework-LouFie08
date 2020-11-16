# %%
import os
import math
import numpy as np
import pandas as pd
import dataretrieval.nwis as nwis
import matplotlib.pyplot as plt
import datetime
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import json 
import urllib.request as req
import urllib
from eval_functions import getstrm_wbs
from eval_functions import add_yymmdd
from eval_functions import mono_reg_mod
from eval_functions import flow_predic_mono
from eval_functions import week_prediction_all
import contextily as ctx
from shapely.geometry import Point
import geopandas as gpd
import fiona
import matplotlib as mpl
from netCDF4 import Dataset
import xarray as xr
import rioxarray
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import geopandas as gpd
import fiona
import shapely


# %% Define trainning period
station_id = '09506000'  # Streamflow station
trainstart = '2016-01-01'  # Start date to train AR model
trainend = '2019-12-31'  # end date to train AR model
lag = 2  # No. of weeks to consider for lag 

# %% Streamflow section
# Get streamflow from website using getstrm_wbs function
end_date = '2020-11-14'  # yyyy-mm-dd (changes each week)

flow_data = getstrm_wbs(station_id,end_date)  # get strmflow data from website
flow_data_pd = add_yymmdd(flow_data)  # add year,month,day

flow_weekly = flow_data_pd.resample("W", on='datetime').mean()  # Add flow values to weekly
flow_weekly.insert(2, 'log_flow', np.log(flow_weekly['flow']), True)  # Natural log (fits the model better)


# %% Step 1: setup the arrays (to build the model)
# Autoregressive model (based on the lagged timeserie)

shifts = list(range(1, lag+1))
flow_weekly['log_flow_tm1'] = flow_weekly['log_flow'].shift(shifts[0])  # Lag 1week
flow_weekly['log_flow_tm2'] = flow_weekly['log_flow'].shift(shifts[1])  # Lag 2weeks

# %% Step 2: Pick time series portion to train model
print('Start training week: ', trainstart)
print('End training week: ', trainend)

# Dropping first two weeks (won't have lagged data) to go with them
train = flow_weekly[trainstart:trainend][['log_flow',
                                          'log_flow_tm1', 'log_flow_tm2']]
test = flow_weekly[trainend:][['log_flow',
                               'log_flow_tm1', 'log_flow_tm2']]


# %% Step 3 Fit AR model (linear regression model using sklearn, 1 var)
b, m, reg_model1, coeff_det1 = mono_reg_mod(train)


# %% Getting our two week predictions!
# Geting last weeks flow
week_before_flow = flow_weekly['log_flow'].tail(1)
print("Last weeks's flow was", math.exp(week_before_flow),'cfs!', '\n')

# Defining prediction weeks for our 2 week predic.
# These are the weeks we will be predicting for our 2 week predictions.
forecast_week_1_2 = ['2020-11-09','2020-11-16']
print(flow_predic_mono(b, m, 2, week_before_flow, forecast_week_1_2), '\n')


# %% 16 week forecast taking previous 12 weeks mean before week to forecast
no_weeks = flow_weekly['log_flow'].size  # Number of weeks up to date
begining_week_ly = 25  # start week year 2020
ending_week_ly = 12  # end week year 2020
dates_weeks_range = flow_weekly['log_flow'][no_weeks-begining_week_ly:
                                           no_weeks-ending_week_ly] 

wk_prd = np.zeros(16)
for i in range(1,17):
       wk_prd = week_prediction_all(flow=flow_weekly, m=m, b=b,
                                    prev_wks=begining_week_ly, end=ending_week_ly, week_pred=i)
       begining_week_ly = begining_week_ly+1
       ending_week_ly = ending_week_ly +1


# %% Plot streamflow

# This is the final graph function, to adjust for naming differences, the only
# change needed is to the parts before the for loop and defining data_mnth_i &
# flow_weekly_mnth_i in the for loop
data_mnth = flow_data_pd[flow_data_pd['month'] > 7]
flow_weekly_mnth = flow_weekly[flow_weekly['month'] > 7]
flow_quants_mnth = np.quantile(flow_weekly_mnth['flow'], q=[0, 0.5, 0.75, 0.9])
print('Method of flow quantiles for month ', data_mnth, ':', flow_quants_mnth)
print('For plots, Green is flow max above 75%, and Red is below 50%')
fig = plt.figure(figsize=(30, 10))
fig.subplots_adjust(hspace=0.6, wspace=0.4)

for i in range(1, 31):
    curr_yr = (i + 1990)
    flow_weekly_mnth_i = flow_weekly_mnth[flow_weekly_mnth['year'] ==
                                          curr_yr]
    data_mnth_i = data_mnth[data_mnth['year'] == curr_yr]
    ax = fig.add_subplot(3, 10, i)
    ax.set(title=("Streamflow in " + str(curr_yr)),
           ylabel="Weekly Avg Flow [cfs]", yscale='log')
    plt.xticks(rotation=45)
    if (np.max(flow_weekly_mnth_i['flow']) > flow_quants_mnth[2]):
        ax.plot(flow_weekly_mnth_i['flow'],
                '-g', label='Weekly Average')
        ax.plot(data_mnth_i['datetime'], data_mnth_i['flow'], color='grey',
                label='Daily Flow')
        ax.legend()
    elif (np.max(flow_weekly_mnth_i['flow']) < flow_quants_mnth[1]):
        ax.plot(flow_weekly_mnth_i['flow'],
                '-r', label='Weekly Average')
        ax.plot(data_mnth_i['datetime'], data_mnth_i['flow'], color='grey',
                label='Daily Flow')
        ax.legend()
    else:
        ax.plot(flow_weekly_mnth_i['flow'],
                '-b', label='Weekly Average')
        ax.plot(data_mnth_i['datetime'], data_mnth_i['flow'], color='grey', 
                label='Daily Flow')
        ax.legend()

# %% Netcdf data

data_path = os.path.join('../../data',
                         'Reanalysis_Precip.nc')

data_temp = os.path.join('../../data',
                         'Reanalysis_AirTemp.nc')
# Read in the dataset as an x-array
dataset = xr.open_dataset(data_path)
datatemp = xr.open_dataset(data_temp)

# %%
# We can inspect the metadata of the file like this:
metadata = dataset.attrs
metadata
# And we can grab out any part of it like this:
metadata['dataset_title']
metadata['history']

# we can also look at other  attributes like this
dataset.values
dataset.dims
dataset.coords

# Focusing on just the precip values
precip = dataset['prate']
temp = datatemp['air']

# Now to grab out data first lets look at spatail coordinates:
dataset['prate']['lat'].values.shape
datatemp['air']['lat'].values.shape

# The first 4 lat values
dataset['prate']['lat'].values
dataset['prate']['lon'].values
datatemp['air']['lat'].values
datatemp['air']['lon'].values

# Now looking at the time;
dataset["prate"]["time"].values
dataset["prate"]["time"].values.shape
datatemp["air"]["time"].values
datatemp["air"]["time"].values.shape


# Now lets take a slice: Grabbing data for just one point
lat = dataset["prate"]["lat"].values[0]
lon = dataset["prate"]["lon"].values[0]

lattemp = datatemp["air"]["lat"].values[0]
lontemp = datatemp["air"]["lon"].values[0]

print("Long, Lat values:", lon, lat)
one_point = dataset["prate"].sel(lat=lat,lon=lon)
one_point_temp = datatemp["air"].sel(lat=lat,lon=lon)
one_point.shape

# use x-array to plot timeseries
#one_point.plot.line()
precip_val = one_point.values

precip_val_temp = one_point_temp.values
#one_point_temp.plot.line()

# Make a nicer timeseries plot
f, ax = plt.subplots(figsize=(12, 6))
one_point.plot.line(hue='lat',
                    marker="o",
                    ax=ax,
                    color="grey",
                    markerfacecolor="blue",
                    markeredgecolor="blue")
ax.set(title="Time Series For a Single Lat / Lon Location Precipitation Rate")
f.savefig("preci.png")

f, ax = plt.subplots(figsize=(12, 6))
one_point_temp.plot.line(hue='lat',
                    marker="o",
                    ax=ax,
                    color="grey",
                    markerfacecolor="orange",
                    markeredgecolor="orange")
ax.set(title="Time Series For a Single Lat / Lon Location Air temperature")
f.savefig("temp.png")
# %%
#Convert to dataframe
precip = one_point.to_dataframe()
precip_wk = precip.resample("W", axis=0).mean()

tempair = one_point_temp.to_dataframe()
tempair_wk= tempair.resample("W", axis=0).mean()
# %%
