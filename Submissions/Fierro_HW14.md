# Week 14. Lourdes Fierro

1. What is the paper or project you picked? Include a title, a link the the paper and a 1-2 sentence summary of what its about.
- Title: Drivers and impacts of the most extreme marine heatwaves events ([link to article](https://www.nature.com/articles/s41598-020-75445-3)). 
- Summary: The article is about applyin a heatwave framework in a marine approach to analyse a global sea surface temperature product and identify extreme events, based on intensity, duration and spatial extent. In the article it is identified common points between marine heatwave characteristics and seasonality, links to the El Niño-Southern Oscillation, triggering processes and impacts on ocean productivity. They also identify that the most intense events occur in summer, in cases where climatological oceanic mixed layers are shallow and winds are weak. They also have a tendency to coincide with reduced chlorophyll-a concentration at low and mid-latitudes

2. What codes and/or data are associated with this paper? Provide any link to the codes and datasets and a 1-2 sentence summary of what was included with the paper (i.e. was it a github repo? A python package?A database? Where was it stored and how?)
- Codes: A MHW was defined to occur when the local SST exceeded the seasonally varying 90th percentile threshold (hereafter ‘PC90’) for at least 5 days ([MHW code](https://github.com/ecjoliver/MHW_Drivers)). Python and MATLAB codes for processing raw SST data, analysing and plotting datasets and most extremes MHW characteristics ([complete code](https://github.com/alexsengupta/ExtremeExtremes.git)).
- Data set: 30-year climatological period of 1983–2012 (inclusive) SST data from the NOAA 1/4° daily Optimum Interpolation Sea Surface Temperature v2.049 ([SST data](https://https://www.ncdc.noaa.gov/oisst)).

3. Summarize your experience trying to understand the repo: Was their readme helpful? How was their organization? What about documentation within the code itself?

The readme was helpful just to understand which files need to be used, however it does not has instructions on what file should be run first and where should the data be dowloaded. Overall, I think the readme file could be more descriptive. I really like the organization of the files name, they are self-explanatory and the important script files have a good organization and explanation.

4. Summarize your experience trying to work with their repo: What happened? Where you successful? Why or why not?

I needed more time to get the data, install some libraries and to completely figure the code out, but I liked the overall way it was  documented. I think I might be able to get something with more time.

5. Summarize your experience working with the data associated with this research. Could you access the data? Where was it? Did it have a DOI? What format was it in?

I was able to access the SST data (I think), which is the mentioned website ( I used the search bar, since the link provided is the main website, not the data link). The data was on ncfiles. I'm not sure the data has a DOI.

6. Did this experience teach you anything about your own repo or projects? Things you might start or stop doing?
I discovered that the way my functions and code are documented can be highly improved. Also, I can be more specific with the documentation in my code and included a direct link of the data. The readme file I consider it can be an instructions document on how to reproduce any project, step by step, so the person that wants to reproduce the work can do it smoothly.
