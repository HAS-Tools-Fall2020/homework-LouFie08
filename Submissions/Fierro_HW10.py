# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime
import os
import json  # conda install json
import urllib.request as req   # conda install urllib3
import urllib
import dataretrieval.nwis as nwis

# %% Declare some functions

def week_prediction_all(flow, m, b, week_pred, end, prev_wks):
    """This function needs the stream flow data (flow), the intersection
    and slope values from AR model (m, b), and range of weeks you want to
    consider for weekly forecast (prev_wks and end). To indicate the week
    to forecast include the week number (week_pred = 1 or week_pred = 2)
    We are using the mean value of the data range you select - the standard
    deviation of the same data range """

    flow_range_value = flow['flow'][no_weeks-prev_wks:no_weeks-end].mean() - 0.3*flow[
                       'flow'][no_weeks - prev_wks:no_weeks-end].std()  # flow range mean - std
    prediction = (b + m * flow_range_value)*(1) # dryness of this year
    print('Week', week_pred, 'forecast using model is:', prediction)
    return prediction


def lin_reg_mod(test_weeks):
       """Linear Regression Model. 
       test weeks = streamflow laged 1 week (x values)
       test weeks = streamflow (y values) """
       reg_model = LinearRegression()
       x_val_model = test_weeks['flow_tm1'].values.reshape(-1, 1)  # Testing values
       y_val_model = test_weeks['flow'].values  # Testing values
       reg_model.fit(x_val_model, y_val_model)  # Fit linear model
       coeff_det = np.round(reg_model.score(x_val_model, y_val_model))  # r^2
       b = np.round(reg_model.intercept_, 2)  # Intercept
       m = np.round(reg_model.coef_, 2)  # Slope
       # Intercept and the slope (Final equation) y=mx+b
       print('Final equation is y = :', m[:1], 'x + ', b)
       return(b,m,reg_model,coeff_det)


# %% Mesonet Example -
# Here are some helpful links for getting started


# 1st Create the URL for the rest API. Insert token
mytoken = 'demotoken'  #'1d19af97b43a4513afcb23a1ffa2c447'

# This is the base url that will be the start our final url
base_url = "http://api.mesowest.net/v2/stations/timeseries"

# Specific arguments for the data that we want
args = {
    'start': '199701010000',
    'end': '202010310000',
    'obtimezone': 'UTC',
    'vars': 'precip_accum',  # Accumulated Precipitation
    'stids': 'QVDA3',  # Verde river station
    'units': 'precip|mm',
    'token': mytoken}

# Arguments and paste them together
# into a string for the api
apiString = urllib.parse.urlencode(args)
print(apiString)

# add the API string to the base_url
fullUrl = base_url + '?' + apiString
print(fullUrl)

# Request data (API response)
response = req.urlopen(fullUrl)

# Read this data (complete format)
responseDict = json.loads(response.read())

# This creates a dictionary for you (format:)
# https://developers.synopticdata.com/mesonet/v2/getting-started/
# Keys (main elements of dictionary)
responseDict.keys()
# You can inspect sub elements by looking up any of the keys in the dictionary
responseDict['UNITS']
# Each key links to differnt data structures
# For example 'UNITS is another dictionary'
type(responseDict['UNITS'])
responseDict['UNITS'].keys()
responseDict['UNITS']['position']

# where as STATION is a list 
type(responseDict['STATION'])
# If we grab the first element of the list that is a dictionary
type(responseDict['STATION'][0])

# And these are its keys
responseDict['STATION'][0].keys()

# Long story short we can get to the data we want like this: 
dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
preciC = responseDict['STATION'][0]['OBSERVATIONS']['precip_accum_set_1']
# Now we can combine this into a pandas dataframe
data_prc = pd.DataFrame({'Precipitation': preciC}, index=pd.to_datetime(dateTime))

# Now convert this to daily data using resample
data_prc_daily = data_prc.resample('D').mean()
# Weekly data precipitation
prc_mean = data_prc.resample('W').mean()

#%% Plot precip data

fig, ax = plt.subplots(nrows=1, ncols=1, squeeze=True)
ax.plot(prc_mean.index, prc_mean["Precipitation"], color='red',
        linestyle='--', label='Observed')
ax.set(title=" Precipitation since 2000", xlabel="Date", ylabel="Precipitation [mm/week]",yscale='log')
ax.legend()
fig.savefig("Historical_precip.png")  # Save figure

# %% Streamflow section
# Set the file name and path to where you have stored the data
# adjust path as necessary

station_id = '09506000'
start_date = '1989-01-01'
end_date = '2020-10-31'

data_flow_day = nwis.get_record(sites=station_id, service='dv',
                          start=start_date, end=end_date,
                          parameterCd='00060')
data_flow_day.columns = ['flow', 'code', 'site_no']
# Rename columns
data_flow_day.index = data_flow_day.index.strftime('%Y-%m-%d')
# Make index a recognized datetime format instead of string
# data_flow_day.index = data_flow_day.index.strftime('%Y-%m-%d')
# %% Read the data into a pandas dataframe
# Expand dates to year month day
data_flow_day['datetime'] = pd.to_datetime(data_flow_day.index)
data_flow_day['year'] = pd.DatetimeIndex(data_flow_day['datetime']).year
data_flow_day['month'] = pd.DatetimeIndex(data_flow_day['datetime']).month
data_flow_day['day'] = pd.DatetimeIndex(data_flow_day['datetime']).dayofweek
data_flow_day['dayofweek'] = pd.DatetimeIndex(data_flow_day['datetime']).dayofweek

# %% AR model that you ended up building
# 1st step: Arrays to build model
wkly_flow_mean = data_flow_day.resample("W", on='datetime').mean()  # Flow to weekly
# %%
# (1) Prediction variables
wkly_flow_mean['flow_tm1'] = wkly_flow_mean['flow'].shift(1)  # Flow lag 1week
wkly_flow_mean['flow_tm2'] = wkly_flow_mean['flow'].shift(2)  # Flow lag 2weeks

# 2nd step: Identify trainning and testing data (only 2019 and 2020 data)
no_weeks = wkly_flow_mean["flow"].size  # Number of weeks up to date

# (3) Trainning data (about 1 year and a half data)
# LC - you could set 60 and 20 as variables based on dates?
# Still thinking how to do this
train_weeks = wkly_flow_mean[no_weeks-70:no_weeks-20][['flow', 'flow_tm1',
                                                      'flow_tm2']]
# (3) Testing data (last 5 months of 2020)
test_weeks = wkly_flow_mean[no_weeks-20:][['flow', 'flow_tm1', 'flow_tm2']]

# 3rd step. Estimate the AR model variables
# Function onlye requires data to train model
b, m, reg_model, coeff_det = lin_reg_mod(test_weeks)

# 4th step prediction with model
# Predict the model response for a  given flow value
predi_train = reg_model.predict(train_weeks['flow_tm1'].values.reshape(-1, 1))
predi_test = reg_model.predict(test_weeks['flow_tm1'].values.reshape(-1, 1))

# Alternative to calcualte this yourself like this:
alter_precit = reg_model.intercept_ + reg_model.coef_ * train_weeks['flow_tm1']

# %% Final model performance analysis
# historical vs predicted streamflow (x axis range limited)
# Test values

# Graphical outputs supporting decisions made with model (historical data)
fig, ax = plt.subplots(nrows=1, ncols=1, squeeze=True)
ax.plot(wkly_flow_mean.index, wkly_flow_mean["flow"], color='red',
        linestyle='--', label='Observed')
ax.set(title=" Flow since 1989", xlabel="Date", ylabel="Avg Flow [cfs]",
       yscale='log')
ax.legend()
fig.savefig("Historical.png")  # Save figure

fig, ax = plt.subplots()
ax.plot(test_weeks['flow'], 'o', color='red', label='observed')
ax.plot(test_weeks.index, predi_test, color='blue', linestyle='--',
        label='simulated')
ax.set(title="Streamflow Test weeks", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]")
ax.set_xticklabels(test_weeks.index, rotation=45, ha="right")
ax.legend()
fig.set_size_inches(5, 3)
fig.savefig("Observed_simulated_Flow.png")

# Scatter plot test weeks vs AR model
# Test streamflow values
fig, ax = plt.subplots()
ax.scatter(test_weeks['flow_tm1'], test_weeks['flow'], marker='p',
           color='blueviolet', label='observations')
ax.set(title="Streamflow Test weeks", xlabel='flow t-1', ylabel='flow t')
ax.plot(np.sort(test_weeks['flow_tm1']), np.sort(predi_test), label='AR model')
ax.fill_between(np.sort(test_weeks['flow_tm1']), np.sort(predi_test) -
                coeff_det*np.sort(predi_test), np.sort(predi_test) +
                coeff_det*np.sort(predi_test), alpha=0.3)
ax.legend()
fig.set_size_inches(5, 3)
fig.savefig("Scatter.png")

# Observed vs simulated flow
fig, ax = plt.subplots()
ax.plot(train_weeks['flow'], 'o', color='blue', label='observed')
ax.plot(train_weeks.index, predi_train, color='red', linestyle='--',
        label='simulated')
ax.set(title="Streamflow Trainning Data", xlabel="Date",
       ylabel="Weekly Avg Flow [cfs]")
ax.legend()
fig.set_size_inches(5, 3)
fig.savefig("Observed_simulated_Flow_hst.png")

# %% Cell 5
#  Q3. provide discussion on what you actually used for your forecast.
# Weekly prediction
# b, m, end, no_weeks:

# Decide how many previous weeks you want to consider
begining_week = 13  # start week
ending_week = 0  # end week

print("Regression based 1 and 2 week forecasts")
wk1_pre = week_prediction_all(flow=wkly_flow_mean, m=m, b=b,
                          prev_wks=begining_week, end=ending_week, week_pred=1)
wk2_pre = week_prediction_all(flow=wkly_flow_mean, m=m, b=b,
                          prev_wks=begining_week, end=ending_week, week_pred=2)

# Decide how many previous weeks you want to consider
# We are using last year data to estimate this year
# We chose this year beacuse it seems to get good values
# with the current conditions of dryness
# values need to substract 1 each week (if you keep using this )
begining_week_ly = 1522  # start week year 1990
ending_week_ly = 1509  # end week year 1990
dates_weeks_range = wkly_flow_mean['flow'][no_weeks-begining_week_ly:
                                           no_weeks-ending_week_ly]


# Decide how many previous weeks you want to consider
# We are using last year data to estimate this year
# We chose this year beacuse it seems to get good values
# with the current conditions of dryness
#begining_week_ly = 647  # start week year 2008
#ending_week_ly = 634  # end week year 2008
begining_week_ly = 22  # start week year 2020
ending_week_ly = 9  # end week year 2020
dates_weeks_range = wkly_flow_mean['flow'][no_weeks-begining_week_ly:
                                           no_weeks-ending_week_ly]


wk_prd = np.zeros(16)

for i in range(1,17):
       wk_prd = week_prediction_all(flow=wkly_flow_mean, m=m, b=b,
                                    prev_wks=begining_week_ly, end=ending_week_ly, week_pred=i)
       begining_week_ly = begining_week_ly+1
       ending_week_ly = ending_week_ly +1

# This week won't include precip data set in AR model,
# However, in the historical plot it is seen a huge decrease
# in precip since 2014. Therefore I substract 10 to mostly all
# strm predictions from AR model
# %% Use this to run the whole code