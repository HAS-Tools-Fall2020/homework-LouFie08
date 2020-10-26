# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import json
import urllib.request as req
import urllib
 #For this to run you will first need to install the following: 
 # conda install urllib3
 # conda install json

# %%
# Mesonet Example -
#Here are some helpful links for getting started
#https: // developers.synopticdata.com/about/station-variables/
#https: // developers.synopticdata.com/mesonet/explorer/

# First Create the URL for the rest API
# Insert your token here
mytoken = 'demotoken'#'1d19af97b43a4513afcb23a1ffa2c447'

# This is the base url that will be the start our final url
base_url = "http://api.mesowest.net/v2/stations/timeseries"

# Specific arguments for the data that we want
args = {
    'start': '199701010000',
    'end': '202010260000',
    'obtimezone': 'UTC',
    #'vars': 'air_temp',
    'vars':'precip_accum',
    #'vars':'air_temp,precip_accum',
    #'precip':'1', # gives derived precip
    'stids': 'QVDA3', # Verde river
    #'units': 'temp|C',
    #'units': 'temp|C,precip|mm',
    'units': 'precip|mm',
    'token': mytoken}

# Takes your arguments and paste them together
# into a string for the api
# (Note you could also do this by hand, but this is better)
apiString = urllib.parse.urlencode(args)
#apiString = apiString.replace('%2C', ',')
print(apiString)

# add the API string to the base_url
fullUrl = base_url + '?' + apiString
print(fullUrl)

# Now we are ready to request the data
# this just gives us the API response... not very useful yet
response = req.urlopen(fullUrl)

# What we need to do now is read this data
# The complete format of this 
responseDict = json.loads(response.read())

# This creates a dictionary for you 
# The complete format of this dictonary is descibed here: 
# https://developers.synopticdata.com/mesonet/v2/getting-started/
#Keys shows you the main elements of your dictionary
responseDict.keys()
# You can inspect sub elements by looking up any of the keys in the dictionary
responseDict['UNITS']
#Each key in the dictionary can link to differnt data structures
#For example 'UNITS is another dictionary'
type(responseDict['UNITS'])
responseDict['UNITS'].keys()
responseDict['UNITS']['position']
#responseDict['UNITS']['precip_accumulated']

#where as STATION is a list 
type(responseDict['STATION'])
# If we grab the first element of the list that is a dictionary
type(responseDict['STATION'][0])

# And these are its keys
responseDict['STATION'][0].keys()

# Long story short we can get to the data we want like this: 
dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
preciC = responseDict['STATION'][0]['OBSERVATIONS']['precip_accum_set_1']
data = pd.DataFrame({'Precipitation': preciC}, index=pd.to_datetime(dateTime))
data_daily = data.resample('D').mean()
#%% 
# airT = responseDict['STATION'][0]['OBSERVATIONS']['air_temp_set_1']

# preciC = responseDict['STATION'][0]['OBSERVATIONS']['precip_accum_set_1']

# Now we can combine this into a pandas dataframe
data = pd.DataFrame({'Temperature': airT}, index=pd.to_datetime(dateTime))
#data = pd.DataFrame({'Precipitation': preciC}, index=pd.to_datetime(dateTime))
# Now convert this to daily data using resample
data_daily = data.resample('D').mean()
#data_daily = data_prc.resample('D').mean()


# %%
# Daymet Example:
# You can get Daymet data for a single pixle from this site:
#https: // daymet.ornl.gov/single-pixel/ 
# You can also experiment with their API Here: 
# https: // daymet.ornl.gov/single-pixel/api  

# Example reading it as a json file
url = "https://daymet.ornl.gov/single-pixel/api/data?lat=34.9455&lon=-113.2549"  \
       "&vars=prcp&start=1984-08-14&end=2014-10-18&format=json"
response = req.urlopen(url)
# Look at the kesy and use this to grab out the data
responseDict = json.loads(response.read())
responseDict['data'].keys()
year = responseDict['data']['year']
yearday = responseDict['data']['yday']
precip = responseDict['data']['prcp (mm/day)']

#make a dataframe from the data
data = pd.DataFrame({'year': year,
                     'yearday': yearday, "precip": precip})


#Example accessing it as a csv
url = "https://daymet.ornl.gov/single-pixel/api/data?lat=34.9455&lon=-113.2549" \
       "&vars=prcp&years=&format=csv"
data = pd.read_table(url, delimiter=',', skiprows=6)


# %%
