# %% (CELL 0)
# AR model and plot
# Modules to be used (pip install for sklearn)

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime

# %% (CELL 1)
# Set the file name and path to where you have stored the data

filename = 'streamflow_week8.txt'  # Change the week streamflow to 7
filepath = os.path.join('data/', filename)  # ** MODIFY it to your path **
print("This is your current location: ", os.getcwd())
print("Is this path correct?", filepath)

# %% Read the data into a pandas dataframe
# (CELL 2)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime', 'flow',
                            'code'], parse_dates=['datetime']
                     )

# Expand dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).dayofweek
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# %% (CELL 3)
# Q1. AR model that you ended up building
# 1st step: Arrays to build model
wkly_flow_mean = data.resample("W", on='datetime').mean()  # Flow to weekly

# (1) Prediction variables
wkly_flow_mean['flow_tm1'] = wkly_flow_mean['flow'].shift(1)  # Flow lag 1week
wkly_flow_mean['flow_tm2'] = wkly_flow_mean['flow'].shift(2)  # Flow lag 2weeks

# 2nd step: Identify trainning and testing data (only 2019 and 2020 data)
no_weeks = wkly_flow_mean["flow"].size  # Number of weeks up to date

# (3) Trainning data (about 1 year and a half data)
# LC - you could set 60 and 20 as variables based on dates?
train_weeks = wkly_flow_mean[no_weeks-60:no_weeks-20][['flow', 'flow_tm1',
                                                      'flow_tm2']]
# (3) Testing data (last 5 months of 2020)
test_weeks = wkly_flow_mean[no_weeks-20:][['flow', 'flow_tm1', 'flow_tm2']]

# 3rd step. Estimate the AR model variables
# LC - This could be a good setp to put in a function. 
reg_model = LinearRegression()
x_val_model = test_weeks['flow_tm1'].values.reshape(-1, 1)  # Testing values
y_val_model = test_weeks['flow'].values  # Testing values
reg_model.fit(x_val_model, y_val_model)  # Fit linear model
coeff_det = np.round(reg_model.score(x_val_model, y_val_model))  # r^2
b = np.round(reg_model.intercept_, 2)  # Intercept
m = np.round(reg_model.coef_, 2)  # Slope

# Intercept and the slope (Final equation) y=mx+b
print('Final equation is y = :', m[:1], 'x + ', b)

# 4th step prediction with model
# Predict the model response for a  given flow value
predi_train = reg_model.predict(train_weeks['flow_tm1'].values.reshape(-1, 1))
predi_test = reg_model.predict(test_weeks['flow_tm1'].values.reshape(-1, 1))

# Alternative to calcualte this yourself like this:
alter_precit = reg_model.intercept_ + reg_model.coef_ * train_weeks['flow_tm1']

# %% Cell 4
# Q2. Provide an analysis of your final model performance.
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

# LC - Great funciton and nice documentation!
# Next time try defining your functions up top
# also check inot the instructions on docstrings for how they should be formatted. 

def week_prediction_all(flow, m, b, week_pred, end, prev_wks):
    """This function needs the stream flow data (flow), the intersection
    and slope values from AR model (m, b), and range of weeks you want to
    consider for weekly forecast (prev_wks and end). To indicate the week
    to forecast include the week number (week_pred = 1 or week_pred = 2)
    We are using the mean value of the data range you select - the standard
    deviation of the same data range """

    flow_range_value = flow['flow'][no_weeks-prev_wks:no_weeks-end].mean() - 0.3*flow[
                       'flow'][no_weeks - prev_wks:no_weeks-end].std()  # flow range mean - std
    prediction = b + m * flow_range_value
    print('Week', week_pred, 'forecast using model is:', prediction)
    return prediction

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
begining_week_ly = 1523  # start week year 1990
ending_week_ly = 1510  # end week year 1990
dates_weeks_range = wkly_flow_mean['flow'][no_weeks-begining_week_ly:
                                           no_weeks-ending_week_ly]


# Decide how many previous weeks you want to consider
# We are using last year data to estimate this year
# We chose this year beacuse it seems to get good values
# with the current conditions of dryness
begining_week_ly = 648  # start week year 2008
ending_week_ly = 635  # end week year 2008
dates_weeks_range = wkly_flow_mean['flow'][no_weeks-begining_week_ly:
                                           no_weeks-ending_week_ly]


wk_prd = np.zeros(16)
# wk_prd = []
# LC- nice work doing this in a for loop!
for i in range(1,17):
       wk_prd = week_prediction_all(flow=wkly_flow_mean, m=m, b=b,
                                    prev_wks=begining_week_ly, end=ending_week_ly, week_pred=i)
       begining_week_ly = begining_week_ly+1
       ending_week_ly = ending_week_ly +1



# %%
