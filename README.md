# Absenteeism
This repo consists of a business case study to determine how likely an employee is to be absent during a workday.

The goal was to develop a model that would predict the probability of an individual being excessively absent from work. The model used in this case study is a logistic regression model. After preprocessing the data, training the ML model, and testing it on an unseen dataset, Tableau was used to analyze three separate dependencies between the inputs of this model.

Here's some more detailed information about the dataset:

## General Information
The dataset contains 700 entries (rows) and 12 features (columns). There are no missing values in any of the columns, which is excellent for immediate analysis.

## Here's a breakdown of the data types for each feature:

###### float64: 1 column (Daily Work Load Average)

###### int64: 10 columns (ID, Reason for Absence, Transportation Expense, Distance to Work, Age, Body Mass Index, Education, Children, Pets, Absenteeism Time in Hours)

###### object: 1 column (Date) - This indicates that the 'Date' column is currently stored as a string and would need to be converted to a datetime object for proper time-series analysis.

## Unique Values for Key Categorical/ID Features:

###### ID: 
There are 34 unique employee IDs, ranging from 1 to 36. This indicates some IDs might be missing from the sequence (e.g., ID 4, 35 are not present based on the output).

###### Reason for Absence: 
There are 28 unique reasons for absence. The value 0 also appears, which might indicate "no specific reason" or another category. Reasons are coded numerically (e.g., 1, 2, ..., 28).

###### Education:
1: (Most common)
2:
3:
4: These likely correspond to different levels of education (e.g., 1 for high school, 4 for a doctorate).

###### Children:
0: (Most common)
1:
2:
3:
4: This represents the number of children an employee has.

###### Pets:
0: (Most common)
1:
2:
4:
5:
8: This represents the number of pets an employee has.

###### Date Column:
The Date column is currently stored as an object (string) type. Its values are in DD/MM/YYYY format (e.g., 07/07/2015). For any time-based analysis or feature engineering (like extracting day of the week, month, year), this column would need to be converted to a proper datetime format.
