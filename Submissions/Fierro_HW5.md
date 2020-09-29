# Lourdes Fierro. September 21, 2020. Assignment 4

___
## Grade
3/3 - Nice job!!
___

## Analysis
1. Include discussion of the quantitative analysis that lead to your prediction. This can include any analysis you complete but must include at least two histograms and some quantitative discussion of flow quantiles that helped you make your decision.
- Weekly forecast: I check the minimum value for this week and last week in all the data (since 1989). I also checked at the mean from last week and I compared that with the minimum from all time. This gave an idea about hoy dry this year is compared to others. From this point I just guess that the value for week 1 and week 2 should be between the min from all time and the first quartile, being much more closer to the min that to the quartile. I repeated the same process for all weeks. Not sure if this procedure is  better, but at least it was easier than previous weeks :D.


2. Provide a summary of the data frames properties.
- Column names: agency_cd, site_no, datetime, flow, code, year, month, day
- Index: It has a total of 11592 elements (RangeIndex(start=0, stop=11592, step=1)
- Data types of the columns:

|   Object  | Data Type |
|  :-----:  |     :-:   |
|  site_no  |   int64   |
| datetime  |   object  |
|   flow    |   float64 |
|   code    |   object  |
|   year    |   int64   |
|   month   |   int64   |
|    day    |   int64   |

3. Provide a summary of the flow column including the min, mean, max, standard deviation and quartiles.

- The min value from the flow data is:  19.0
- The mean value from the flow data is:  345.6304606625259
- The max value from the flow data is:  63400.0
- The standard deviation value from the flow data is:  1410.8329680586044
- The 1st quartile (25%) is:  93.7 he 2nd quartile (50%) is:  158.0 , and the 3rd quartile (75%) is:  216.0

4. Provide the same information but on a monthly basis. (Note: you should be able to do this with one or two lines of code)


| month | count |   mean     |      std    |  min  |    25%  |    50% |     75%  |  max    |
| :---: | :---: |   :---:    |    :---:    | :---: |  :---:  |  :---: |   :---:  |  :---:  |
| 1     | 992.0 | 706.320565 | 2749.153983 | 158.0 | 202.000 | 219.50 |  292.00  | 63400.0 |
| 2     | 904.0 | 925.252212 | 3348.821197 | 136.0 | 201.000 | 244.00 |  631.00  | 61000.0 |
| 3     | 992.0 | 941.731855 | 1645.803872 |  97.0 | 179.000 | 387.50 | 1060.00  | 30500.0 |
| 4     | 960.0 | 301.240000 |  548.140912 |  64.9 | 112.000 | 142.00 |  214.50  | 4690.0  |
| 5     | 992.0 | 105.442339 |   50.774743 |  46.0 | 77.975  | 92.95  | 118.00   | 546.0   |
| 6     | 960.0 |  65.998958 |   28.966451 |  22.1 |  49.225 |  60.50 |   77.00  | 481.0   |
| 7     | 992.0 |  95.571472 |   83.512343 |  19.0 |  53.000 |  70.90 |  110.00  | 1040.0  |
| 8     | 992.0 | 164.354133 |  274.464099 |  29.6 |  76.075 | 114.00 |  170.25  | 5360.0  |
| 9     | 956.0 | 172.688808 |  286.776478 |  36.6 |  88.075 | 120.00 |  171.25  | 5590.0  |
| 10    | 961.0 | 146.168991 |  111.779072 |  69.9 | 107.000 | 125.00 |  153.00  | 1910.0  |
| 11    | 930.0 | 205.105376 |  235.673534 | 117.0 | 156.000 | 175.00 |  199.00  | 4600.0  |
| 12    | 961.0 | 337.097815 | 1097.280926 | 155.0 | 191.000 | 204.00 |  228.00  | 28700.0 |

5. Provide a table with the 5 highest and 5 lowest flow values for the period of record. Include the date, month and flow values in your summary.

- Lowest Values:

| agency_cd | site_no       |   datetime  | flow | code | year | month | day |
|   :---:   |    :---:      |    :---:    | :---:| :---:| :---:| :---: |:---:|
| 8582      | USGS  9506000 | 2012-07-01  | 19.0 |   A  | 2012 |   7   |  1  |
| 8583      | USGS  9506000 | 2012-07-02  | 20.1 |   A  | 2012 |   7   |  2  |
| 8581      | USGS  9506000 | 2012-06-30  | 22.1 |   A  | 2012 |   6   | 30  |
| 8580      | USGS  9506000 | 2012-06-29  | 22.5 |   A  | 2012 |   6   | 29  |
| 8584      | USGS  9506000 | 2012-07-03  | 23.4 |   A  | 2012 |   7   |  3  |
| 8933      | USGS  9506000 | 2013-06-17  | 24.8 |   A  | 2013 |   6   | 17  |

- Highest Values:

|agency_cd |  site_no      |  datetime  |   flow   |code | year | month | day|
|   :---:  |    :---:      |    :---:   | :---:    |:---:| :---:| :---: |:--:|
| 1468     | USGS  9506000 | 1993-01-08 | 63400.0  | A:e | 1993 |    1  |  8 |
| 1511     | USGS  9506000 | 1993-02-20 | 61000.0  |  A  | 1993 |    2  | 20 |
| 2236     | USGS  9506000 | 1995-02-15 | 45500.0  |  A  | 1995 |    2  | 15 |
| 5886     | USGS  9506000 | 2005-02-12 | 35600.0  |  A  | 2005 |    2  | 12 |
| 2255     | USGS  9506000 | 1995-03-06 | 30500.0  |  A  | 1995 |    3  |  6 |
| 5842     | USGS  9506000 | 2004-12-30 | 28700.0  |  A  | 2004 |   12  | 30 |


6. Find the highest and lowest flow values for every month of the year (i.e. you will find 12 maxes and 12 mins) and report back what year these occurred in.

|      Min      |       Max       |   Month  |
|  (year,flow)  |   (year,flow)   |   :---:  |
|     :---:     |      :---:      |   :---:  |
| (2003, 158.0) |  (1993, 63400.0)|     1    |
| (1991, 136.0) |  (1993, 61000.0)|     2    |
| (1989, 97.0)  |  (1995, 30500.0)|     3    |
| (2018, 64.9)  |  (1991, 4690.0) |     4    |
| (2004, 46.0)  |  (1992, 546.0)  |     5    |
| (2012, 22.1)  |  (1992, 481.0)  |     6    |
| (2012, 19.0)  |  (2006, 1040.0) |     7    |
| (2019, 29.6)  |  (1992, 5360.0) |     8    |
| (2020, 36.6)  |  (2004, 5590.0) |     9    |
| (2012, 69.9)  |  (2010, 1910.0) |    10    |
| (2016, 117.0) |  (2004, 4600.0) |    11    |
| (2012, 155.0) |  (2004, 28700.0)|    12    |

7. Provide a list of historical dates with flows that are within 10% of your week 1 forecast value. If there are none than increase the %10 window until you have at least one other value and report the date and the new window you used

| agency_cd | site_no       |   datetime  | flow | code | year | month | day |
|   :---:   |    :---:      |    :---:    | :---:| :---:| :---:| :---: |:---:|
| 126   | USGS  9506000|  1989-05-07 | 80.0  |  A  | 1989   |     5  |    7|  
|143   |     USGS  9506000 | 1989-05-24 | 73.0  |  A  | 1989   |     5  |   24|  
|144    |    USGS  9506000 | 1989-05-25 | 68.0  |  A  | 1989   |     5  |   25|  
|145    |    USGS  9506000 | 1989-05-26 | 70.0  |  A  | 1989   |     5  |  26|  
|146    |    USGS  9506000 | 1989-05-27 | 77.0  |  A  | 1989   |     5  |   27|  
|...     |    ...      ... |        ... |  ... | ...  |  ...  |    ...  |  ...|  
|11466   |   USGS  9506000 | 2020-05-24 | 71.5 |   A  |  2020   |     5 |    24|  
|11467   |   USGS  9506000 | 2020-05-25 | 75.8  |  A |   2020   |     5 |    25|  
|11468   |   USGS  9506000 | 2020-05-26 | 74.1  |  A |   2020   |     5 |   26|  
|11469   |   USGS  9506000 | 2020-05-27 | 71.2  |  A |   2020   |     5 |    27|  
|11532  |    USGS  9506000 | 2020-07-29 | 71.3  |  P |   2020  |      7 |    29|  
