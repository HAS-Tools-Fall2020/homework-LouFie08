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
2. Verify that you are working in */Code_Review1* folder on your computer.
2. This file is divided into cells which you will need to run. I suggest you to run each cell separately, and in the order they are stablished. There is a number for each cell located in the comment section.
3. Run cell 0 and cell 1 to make sure streamflow file is located in the correct directory.
4. Run the rest of the code.
5. The values based in the regression model are in variables: wk1_pre and wk2_pre. You can also find them printed in the interactive screen if you are using VS Code. Enter these values in the space below in the the correct section.
5. The values to submit for this week forecast assignment are wk1_pre_ly and wk2_pre_ly. You can also find them printed in the interactive screen if you are using VS Code. Enter these values in the space below in the the correct section.

## Update week 7 entries
1. Go to [forecast entries](https://github.com/HAS-Tools-Fall2020/forecasting/tree/master/forecast_entries) folder and update fierro.csv entries for 1week and 2week in the 10/12/20 row.
2. Open [fierro.csv](https://github.com/HAS-Tools-Fall2020/forecasting/blob/master/forecast_entries/fierro.csv) file and check that the values for *1week* and *2week* are there and match with the results.

# Review of the py code
1. Follow the instructions in the code review rubric. You can find it in the [starter codes](https://github.com/HAS-Tools-Fall2020/Course_Materials/blob/master/Assignments/Starter_Codes/code_review_rubric.md) folder.
2. Using the rubric mentioned in 1. of this part, feel free to provide as many feebdback as you want :).
3. Use the section below to write your feedback and answer the questions.

### Forecast values

* Week 1 forecast regression based:
* Week 2 forecast regression based:

* Week 1 forecast submission values:
* Week 2 forecast submission values:



### Code Review
Use this section to complete and write the feedback review
1. Is the script easy to read and understand?
 - Are variables and functions named descriptively when useful?
 - Are the comments helpful?
 - Can you run the script on your own easily?
 - Are the doc-strings useful?

2. Does the code follow PEP8 style consistently?
 - If not are there specific instances where the script diverges from this style?

3. Is the code written succinctly and efficiently?
 - Are there superfluous code sections?
 - Is the use of functions appropriate?
 - Is the code written elegantly without decreasing readability?
