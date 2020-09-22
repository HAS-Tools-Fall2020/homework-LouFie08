# Lourdes Fierro. September 21, 2020. Assignment 4
___
### Grade
3/3 - great work! Next time try including the graphs with the atom plugin. I'm not sure why but I can't see them here.  
___

## Analysis
1. Include discussion of the quantitative analysis that lead to your prediction. This can include any analysis you complete but must include at least two histograms and some quantitative discussion of flow quantiles that helped you make your decision.
- Weekly forecast: My first step was to estimate the average flow for the precious week from this year. I compared this value with the  mean flow for this week through all time (30 years). The histogram helped me to identify which flow values are more common for this week. Since my mean value for last week was within the the second group of frequent values, I decided to still stay close to this value for my prediction. Finally, I used the quantiles to see which one was closer to my mean value. All this information helped me to decide my guess for both weeks. For week 2 forecast adn seasonal forecast, instead of using the weeks of this year (for obvious reasons :V), I used the average value from last year considering thst this year has been dryer.
* 1st week histogram:
![alt text](https://github.com/HAS-Tools-Fall2020/homework-LouFie08/tree/master/assignment_4/week1.png?raw=true)


* 2nd week histogram:
![alt text](https://github.com/HAS-Tools-Fall2020/homework-LouFie08/tree/master/assignment_4/week2.png?raw=true)


2. Describe the variable flow_data: What is it? What type of values is it composed of? What is are its dimensions, and total size?
- Flow data is a numpy array
- flow_data is composed of float64
- It has 2 dimensions, the first one with 11585 elements, and the second one has 4 elements.
- The total size is 46340.

3. How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?
- Prediction one week forecast: The percentage where the daily flow in September is greater than my prediction is 91.46469968387777 and the total number of times the daily flow is greater than my prediction is 868 times.
- Prediction two week forecast: The percentage where the daily flow in September is greater than my prediction is 83.9831401475237 and the total number of times the daily flow is greater than my prediction is 797 times.

4. How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)
- Daily flows in or before year 2000: For week one, the forecast value percentage is 98.33333333333333 and the total number of times is 354. For week two, the forecast value percentage is 92.77777777777779 and the total number of times is 334.
- daily flows in or after year 2000: For week one, the forecast value percentage is 85.57993730407524 and the total number of times is 273. For week two, the forecast value percentage is 77.74294670846395 and the total number of times is 248.

5. How does the daily flow generally change from the first half of September to the second?

The daily flow  value in the first half of September is usually higher than the second half, however there are a few years where this tendency is inverted (the first half flow value is lower than the second half of the month). I think the histogram helps to visualice the tendency.
