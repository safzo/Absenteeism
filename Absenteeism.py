#importing relevant libraries
import pandas as pd

#Loading the data
raw_csv_data = pd.read_csv('Absenteeism_data.csv')

#Checking to see what the data looks like
raw_csv_data
type(raw_csv_data)

#Always create a copy of the OG data to prevent accidental manipulation
df = raw_csv_data.copy()

#Changing view/display of rows and columns of a table as required
pd.options.display.max_columns = None
pd.options.display.max_columns = None

#Displaying different data types
display(df)
df.info()




#Dropping a column from the copied DataFrame
df = df.drop(['ID'], axis = 1)

#Analyzing the Reasons for Absence
df['Reason for Absence'].min()
df['Reason for Absence'].max()
pd.unique(df['Reason for Absence']) #Another syntax: df['Reason for Absence'].unique()
len(df['Reason for Absence'].unique())
sorted(df['Reason for Absence'].unique()) #Here we find that once of the category is missing i.e. 20





#Obtaining dummies from a single feature
reason_columns = pd.get_dummies(df['Reason for Absence'])

#If the sum of the numbers of a row returns higher than 1, it means the employee was absent for more than 1 reason, and that's not possible for this scenario (assumption)
reason_columns['check'] = reason_columns.sum(axis = 1) #checking if check adds up to 1 (expected) along the entire row

#checking if check returns 700, and not less (missing values), or more (more than 1 reason of Absence)
reason_columns['check'].sum(axis = 0)
reason_columns['check'].unique()

#Drop the check column after use to prevent discrepancy while analyzing
reason_columns = reason_columns.drop(['check'], axis = 1)

#Drop Reason 0 to avoid potential multicollinearity issues
reason_columns = pd.get_dummies(df['Reason for Absence'], drop_first = True)




#Classifying various reasons for Absence and grouping them
reason_type_1 = reason_columns.loc[:,1:14].max(axis = 1)
reason_type_2 = reason_columns.loc[:,15:17].max(axis = 1)
reason_type_3 = reason_columns.loc[:,18:21].max(axis = 1)
reason_type_4 = reason_columns.loc[:,22:].max(axis = 1)

#Concatinating them into the DataFrame
df = pd.concat([df, reason_type_1, reason_type_2, reason_type_3, reason_type_4], axis = 1)

#Renaming the column names from numericals to strings, and dropping Reasons for Absence column to avoid multicollinearity 
df.columns.values
df = df.drop(['Reason for Absence'], axis = 1)
column_names = ['Date', 'Transportation Expense','Distance to Work', 'Age', 'Daily Work Load Average','Body Mass Index', 'Education', 'Children', 'Pets','Absenteeism Time in Hours', 'Reason_1', 'Reason_2', 'Reason_3', 'Reason_4']
df.columns = column_names
df.head()

#Re-Ordering columns
column_names_reordered = ['Reason_1', 'Reason_2', 'Reason_3', 'Reason_4', 'Date', 'Transportation Expense','Distance to Work', 'Age', 'Daily Work Load Average','Body Mass Index', 'Education', 'Children', 'Pets','Absenteeism Time in Hours']  
df = df[column_names_reordered]
df.head()



 
#Creating a checkpoint
df_reason_mod = df.copy()

#Converting all values in the Date column from str to timestamp
#Don't forget to use the format syntax, to make sure months and dates are not accidentally switched up
type(df_reason_mod['Date'][0])
df_reason_mod['Date'] = pd.to_datetime(df_reason_mod['Date'], format = '%d/%m/%Y')




#Extracting the Month value from Date and making a new Month column in the DataFrame
list_months = []
for i in range(df_reason_mod.shape[0]):
    list_months.append(df_reason_mod['Date'][i].month)
len(list_months)
df_reason_mod['Month Value'] = list_months
df_reason_mod.head(20)

#Extracting the Day of the Week from the "Date" Column
df_reason_mod['Date'][699].weekday()
df_reason_mod['Date'][699]






