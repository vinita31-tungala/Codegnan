'''Introduction to Data Analytics
---> It is a process of collecting,cleaning,transforming and analyzing data to discover useful information,inform conclusions and support decision making.
Imp steps:
1.Data Collection - Like Excel,PDf,csv,SQL,API,Web Scraping,Audios,Videos,Images,Social Media,IoT Devices
2.Data Cleaning - It is a process of removing or correcting inaccurate,corrupted,incorrect,duplicate or incomplete data within a dataset.
3.Data Processing - It is a process of transforming raw data into a meaningful format for analysis.
4.Data Analysis - It is a process of inspecting,cleaning and modeling data to discover useful information,inform conclusions and support decision making.
5.Data Visualization - It is a process of representing data in a graphical or pictorial format to help users understand the significance of data and identify patterns, trends and insights.'''
#Numpy - It is a python library used for numerical calculations,working with arrays and matrices and performing mathematical operations on them.
'''import numpy as np
marks=np.array([10,20,30,40,50])
marks=marks+5
print(marks)'''

'''import numpy as np
marks=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(marks)
print(marks.shape)
print(marks.ndim)
print(marks.size)
print(marks.dtype)
print(marks[0][0])
print(marks[0][1])
print(marks[0][2])
print(marks[1][0])
print(marks[1][1])
print(marks[1][2])
print(marks[2][0])
print(marks[2][1])
print(marks[2][2])
print(marks[0:2,1:3])
# [0:2] --> rows 0 and 1
# [1:3] --> columns 1 and 2'''

#[0,1][0,2][1,1][1,2]
# Creating Special Arrays
#1.np.zeros() - Creates an array filled with zeros.
'''import numpy as np
a=np.zeros(5)
a=np.ones(5)
print(a)
b=np.zeros((2,3))
print(b)

#2. np.arange() - Similar to python range
import numpy as np
c=np.arange(1,10)
print(c)'''

# 3. array()
'''import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
# Arithmetic Operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# Comparison Operators
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)'''

#Mathematical Functions
'''import numpy as np
marks=np.array([10,20,30,40,50])
#sum() - It returns the sum of all elements in the array.
print(np.sum(marks))
#Average() - It returns the average of all elements in the array.
print(np.mean(marks))
#Median() - It returns the median of all elements in the array.
print(np.median(marks))
#max() - It returns the maximum value in the array.
print(np.max(marks))
#min() - It returns the minimum value in the array.
print(np.min(marks))
#std() - It returns the standard deviation of all elements in the array.
print(np.std(marks))
#var() - It returns the variance of all elements in the array.
print(np.var(marks))'''

#2-D Arrays
'''import numpy as np
marks=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(np.sum(marks,axis=0))  #column wise sum
print(np.sum(marks,axis=1)) ''' #row wise sum

#Reshaping Arrays
'''import numpy as np
a=np.array([1,2,3,4,5,6])
b=a.reshape(2,3)  #(2,3) means 2 rows and 3 columns
print(b)'''

# Pandas - Used for structured data analysis and manipulation. It provides data structures like Series and DataFrame for handling tabular data.
# Eg: CSV files,Excel files,SQL databases,JSON files
# Syntax - import pandas as pd
# Series - It is a one-dimensional labeled array capable of holding any data type.
# iloc - represents position
# loc - represents label
'''import pandas as pd
marks=pd.Series([10,20,30,40,50])
print(marks[0])
print(marks.iloc[1])'''   # to track the position of the element

'''import pandas as pd
marks=pd.Series([10,20,30],index=["apple","banana","carrot"])
print(marks.loc["carrot"])'''

'''import pandas as pd
marks=pd.Series([10,20,30])
print(marks+5)
print(marks-5)
print(marks*5)
print(marks/5)
'''
# Data Frame - It is a two-dimensional labeled data structure with columns of potentially different types. It is similar to a spreadsheet or SQL table.
'''import pandas as pd
data={"Name":["Vinita","Indu","Likki"],"Age":[25,30,35],"City":["Delhi","Mumbai","Bangalore"]}
df=pd.DataFrame(data)
print(df)
print(df["Name"])
print(df[["Name","Age"]])
print(df.iloc[1])
# Accessing specific data using loc and iloc
print(df.loc[2])  # Accessing row by label
print(df.iloc[0])'''

# Reading CSV files
import pandas as pd
df=pd.read_csv("C:\\Users\\tunga\\Downloads\\python\\day-1\\olist_order_payments_dataset.csv")
'''print(df.head())
print(df.tail())
print(df.shape)
print(df.describe())
print(df.info())
print(df.size)'''
# Data Cleaning - It is a process of removing or correcting inaccurate,corrupted,incorrect,duplicate or incomplete data within a dataset.
# Finding missing values
'''print(df.isnull())
print(df.isnull().sum())'''
# Removing Missing Rows
'''df=df.dropna()
print(df)
# Filling the values
df['payment_value']=df['payment_value'].fillna(0)
print(df['payment_value'])
df['payment_value']=df['payment_value'].fillna(df['payment_value'].mean())'''
# Duplicate Data
'''print(df.duplicated())
print(df.drop_duplicates())'''
# Changing Column names
'''df=df.rename(columns={"payment_type":"payment_typ"})
print(df.head())'''
# Filtering of data
result=df[df["payment_value">100]]
print(result)




