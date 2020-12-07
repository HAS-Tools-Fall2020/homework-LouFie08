# %% Import libraries

import os
import math
import numpy as np
import pandas as pd
import dataretrieval.nwis as nwis
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
import datetime
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import minmax_scale
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import QuantileTransformer
from sklearn.preprocessing import PowerTransformer
from sklearn.datasets import fetch_california_housing
from sklearn import metrics
import json 
import urllib.request as req
import urllib
from eval_functions import getstrm_wbs
from eval_functions import add_yymmdd
from eval_functions import mono_reg_mod
from eval_functions import flow_predic_mono
from eval_functions import week_prediction_all
from eval_functions import down_map_var
from eval_functions import extractmasonet
from eval_functions import assemble_data_masonet
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import contextily as ctx
from shapely.geometry import Point
import geopandas as gpd
import fiona
import matplotlib as mpl
from netCDF4 import Dataset
import xarray as xr
import rioxarray
import fiona
import shapely
import time

# %% Define trainning period
station_id = '09506000'  # Streamflow station
trainstart = '2016-01-01'  # Start date to train AR model
trainend = '2019-12-31'  # end date to train AR model
lag = 2  # No. of weeks to consider for lag 
end_date = '2020-12-05'  # yyyy-mm-dd (changes each week)
forecast_week_1_2 = ['2020-12-06','2020-12-13']

# %% Streamflow section
# Get streamflow from website using getstrm_wbs function

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
# forecast_week_1_2 = ['2020-11-09','2020-11-16']
print(flow_predic_mono(b, m, 2, week_before_flow, forecast_week_1_2), '\n')


# %% 16 week forecast taking previous 12 weeks mean before week to forecast
no_weeks = flow_weekly['log_flow'].size  # Number of weeks up to date
begining_week_ly = 80  # start week year 2008 30 653
ending_week_ly = 63  # end week year 2008 12 640 66
dates_weeks_range = flow_weekly['log_flow'][no_weeks-begining_week_ly:
                                           no_weeks-ending_week_ly] 

wk_prd = np.zeros(16)
for i in range(1,17):
       wk_prd = week_prediction_all(flow=flow_weekly, m=m, b=b,
                                    prev_wks=begining_week_ly, end=ending_week_ly, week_pred=i)
       begining_week_ly = begining_week_ly+1
       ending_week_ly = ending_week_ly +1


