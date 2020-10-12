# Code Review Week 7
## Instructions to run Fierro_HW7.py

### Getting the data
1. Download the streamflow data using the [USGS website](https://waterdata.usgs.gov/nwis/dv/?site_no=09506000&agency_cd=USGS).
2. In order to download the data insert as begin date: *1989-01-01* and for the end date *10-10-2020*.
3. For the output format select Tab-separated. Then click the *go* box.
4. The streamflow data is going to be displayed in a different page. Right click in this new page and save the file as *streamflow_week7.txt*.
5. Once the data file is on your computer, save it in the data folder located in *homework-LouFie08/Submissions/Code_Review1/data*

### How to run  Fierro_HW7.py code
1. Open Fierro_HW7.py script in your favorite text editor, but I recommend you to do it on VS Code.
2. Verify that you are working in */Code_Review1* folder on your computer, and that the streamflow data file is *streamflow_week7.txt*
3. This file is divided into cells which you will need to run. I suggest you to run each cell separately, and in the order they are stablished. There is a number for each cell located in the comment section.
4. Run cell 0 and cell 1 to make sure streamflow file is located in the correct directory.
5. Run the rest of the code.
6. The values based in the regression model are in variables: wk1_pre and wk2_pre. You can also find them printed in the interactive screen if you are using VS Code. Enter these values in the space below in the the correct section.
7. The values to submit for this week forecast assignment are wk1_pre_ly and wk2_pre_ly. You can also find them printed in the interactive screen if you are using VS Code. Enter these values in the space below in the the correct section.

Note: The script also produces plots for the historical flow, the train flow and test data used in the regresssion model, and a scatter plot.

### Update week 7 entries
1. Go to [forecast entries](https://github.com/HAS-Tools-Fall2020/forecasting/tree/master/forecast_entries) folder and update fierro.csv entries for 1week and 2week in the 10/12/20 row.
2. Open [fierro.csv](https://github.com/HAS-Tools-Fall2020/forecasting/blob/master/forecast_entries/fierro.csv) file and check that the values for *1week* and *2week* are there and match with the results.

### Review of the py code
1. Follow the instructions in the code review rubric. You can find it in the [starter codes](https://github.com/HAS-Tools-Fall2020/Course_Materials/blob/master/Assignments/Starter_Codes/code_review_rubric.md) folder.
2. Using the rubric mentioned in 1. of this part, feel free to provide as many feebdback as you want :).
3. Use the *Code Review* section below to write your feedback and answer the questions.

### Forecast values

* Week 1 forecast regression based: 45.57 cfs
* Week 2 forecast regression based: 46.41 cfs

* Week 1 forecast submission values: 58.91 cfs
* Week 2 forecast submission values: 63.00 cfs



### Code Review
Use this section to complete and write the feedback review
1. Is the script easy to read and understand?
 - Are variables and functions named descriptively when useful?
    * Variables are labeled very intuitively and follow lower case naming conventions.
 - Are the comments helpful?
    * Code comments are helpful and it was clear where the user needed to change an input. I like that you labeled each cell with a cell number to make it easy to not miss a cell when you run the script.
 - Can you run the script on your own easily?
    * I was able to run the script with no issues and produce the desired output. However, I think both sets of predictions made at the end of the script are based on the AR model (just a different range of input data), so I'm wondering why you produced two different sets of forecasts.
 - Are the doc-strings useful?
    * The docstring is very useful in understanding your function inputs. The only part I was not clear about was why the input to your prediction is the mean minus standard deviation of the chosen range. Some additional explanation of your statistical approach in the docstring would have been helpful.

2. Does the code follow PEP8 style consistently?
 - If not are there specific instances where the script diverges from this style?
    * Generally, great job following PEP8 standards. Some portions of script in CELL 3 are labeled (3rd Step) while other parts are labeled (3); following a consistent numeric sequencing would be helpful. Also, just a few lines of code go over the 79 column recommendation (ex: rows 136-137) and the comments are cutoff when viewing the script in a split screen with the python interactive window. I think following the 79 column recommendation does improve readability. Also, datetime was imported but not used.

3. Is the code written succinctly and efficiently?
 - Are there superfluous code sections?
    * The variable alter_precit wasn't used so it could have been deleted. I would recommend removing timestamps from x-axis labels of second figure. Also, you establish 2 time lags (flow_tm1 and flow_tm2), but your final AR model equation only has 1 slope, so I was unclear on whether the model was built off 1 or 2 time lags.
 - Is the use of functions appropriate?
    * Your function seems very useful since you use it a few times in your code, so you've avoided repeating the same block of code and use a function instead.
 - Is the code written elegantly without decreasing readability?
    * Still not exactly sure what elegant code is (since I'm a beginner and am sure my code isn't elegant!), but your code was written in a format and level that I could follow along with. Looks great!

* Readability: 3/3
* Style: 3/3
* Code Efficiency: 3/3
