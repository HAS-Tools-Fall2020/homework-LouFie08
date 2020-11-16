# Lourdes Fierro. 11/16/20
## Week 12

1. A brief summary of the how you chose to generate your forecast this week.
    I used last week's script since I liked the logaritmic approach we used. I adjusted it to get the streamflow data from this week, and use the same AR model :).
I loked at the precipitation rate for the 2020 year, as well as the air temperature at 2m height, however I'm unsure on how these values can be added into the AR model since the units are different. The precipitation data set was only used to get an idea if the streamflow predicted by the AR model makes sense depending on the precipittion value seen in this new data.

2. A description of the dataset you added
- What is the dataset? Why did you choose it?
This is the Precipitation rate data set and the air temperature at 2m height data. I choose them i order to get a sense about how much is raining and how warm is the enviroment.

- What is the spatial and temporal resolution and extent of the data ?
The temporal resolution is daily average and goes from January 1st, 2020 to November 13th, 2020. and the spatial resolution is a box of latitude 32N to 35N and longitude 248E to 251 E
- Where did you get the data from?
The data can be accessed from the Research Data Archive website.
- What was your approach to extracting and aggregating it into something useful to you?
The extraction was obtained in daily averages, and it was converted into weekly average. Both data sets were not included into the AR model, however it was used to corroborate if the AR model outputs where coeherent in the prediction.

- Add a plot. This can be a timeseries, map, histogram or any other plot that you think is a good summary of what you added.

![](/assignment_12/preci.png)

![](/assignment_12/temp.png)