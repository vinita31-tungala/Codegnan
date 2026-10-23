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
'''result=df[df["payment_value">100]]
print(result)
'''
#1. Web Scraping - It is the process of automatically collecting information from websites using a program
#Where is web scraping used?
# Collecting products data
# Gathering job listing
# Collecting publicly available research data

#  2.Request Module - The request library allows python to send HTTP requests to websites and receive their responses.
# 200 - Request Successful
# 201 - Created
# 301 - Redirect
# 403 - Access forbidden
# 404 - Page not found
# 500 - Server Error

# Sending request to website
'''import requests
url="https://www.brandforce.com/"
response=requests.get(url)
print(response.status_code)
print(response.text)'''

# Add basic error handling
'''import requests
url="https://www.brandforce.com/"
try:
    response=requests.get(url,timeout=10)
    response.raise_for_status()
    print(response.text)
except requests.RequestException as error:
    print("Request Failed:",error)'''

# BeautifulSoup:
# Requests download the HTML, but we need a convinent way to find a particular elements inside it.that's where BeautifulSoup helps.
'''from bs4 import BeautifulSoup
html="""
<html>
<head>
<title>Hi</title>
</head>
<body>
<p>How are you Vinita</p>
<h1>Good</h1>
</body>
</html>"""
soup=BeautifulSoup(html,"html.parser")  #parser-like compiler
print(soup.title)
print(soup.title.get_text())   #get_text - the text inside the tags(text) is printed
print(soup.p.get_text())
print(soup.h1.get_text())

# Important BeautifulSoup Methods
# 1.find() - Finds the first matching element
soup.find("p")
# 2.find_all() - Finds all matching elements
soup.find_all("p")
# 3.get_text() - Extract text
# 4.get() - Extracts an attribute
link=soup.find("a")
print(link.get("href"))'''

# Extracting Website data

'''import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Extract page title
title = soup.title.get_text(strip=True) if soup.title else "Title not found"

# Extract heading safely
h1 = soup.find("h1")

if h1:
    heading = h1.get_text(strip=True)
else:
    heading = "Heading not found"

print("Page Title:", title)
print("Heading:", heading)'''

'''import requests
from bs4 import BeautifulSoup

url = "https://theuselessweb.com"

response = requests.get(url, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
links=soup.find_all("a")
for link in links:
    text=link.get_text(strip=True)
    url=link.get("href")
    print("Link Text:",text)
    print("URL:",url)'''

# Email Automation
'''import smtplib
from email.message import EmailMessage
# EmailMessage() - Creates an email message
sender="tungalavinita@gmail.com"
password=""# app password which is generated using two-step verification is written within the quotes
receiver="vinitatungala@gmail.com"
msg=EmailMessage()
msg["Subject"]="Preparation Email"
msg["From"]=sender
msg["To"]=receiver
msg.set_content("Hello.This is a preparation email using python")
# Attacha PDF or Word Document
file_path=r"C:\\Users\\tunga\\Downloads\\hp_resume.pdf"
with open(file_path,"rb") as file:
    file_data=file.read()
msg.add_attachment(
    file_data,
    maintype="application",
    subtype="pdf",
    filename="hp_resume.pdf"
)
with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
# SMTP_SSL - Connects to Gmails's SMTP server using port 465
    server.login(sender,password)
    #login() - Log in using your email and app password
    server.send_message(msg)
    #send_message() - Sends the email
print("Email Sent Successfully")'''

# Virtual Assistant Program
'''import datetime
import webbrowser
print("Hello! I'm your Virtual Assistant.")
while True:
    command=input("\n How may I help you").lower()
    if "hello" in command or "hi" in command:
        print("Hello Vinita! How are you?")
    elif "time" in command:
        time=datetime.datetime.now().strftime("%I:%M%p")
        print("Current time is:",time)
    elif "date" in command:
        date=datetime.datetime.now().strftime("%d-%m-%Y")
        print("Today's date is:",date)
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        print("Opening Google...")
    elif "your_name" in command:
        print("I'm your Python Virtual Assistant")
    elif "exit" in command or "bye" in command:
        print("Googdbye! Have a nice day")
        break
    else:
        print("Sorry,I didn't understand the command")'''

#Time Complexity - It analyzes the amount or time grows as input size grows
# 1)Constant Time(Accessing index value): O(1)  -- Fastest time Complexity
# 2)Linear Time : O(n)  -- Accessing every value(Code contains "for loop" means time complexity is O(n))---Linear Search(Sequence method)
# Example code:
'''nums=[10,20,30,40]
for num in nums:
    print(nums)'''
# 3)Logarithmic Time: O(log n)---Binary Search(Divide and Conquer technique)
# 4)Quadratic time: O(n^2)---Nested loop(Eg:Selection sort & Insertion sort)
# 5)Linearthmic time: (n log n)--(Eg:Merge sort)
# 6)Exponential time:O(2^n)---(Eg:Fibonacci series)
# 7)Factorial:O(N!)  ---(Eg:Travelling Salesman Problem)---(Fastest to lowest)

#Space Complexity - It analyze memory needs for an algorithm as input grows
# 1) Constant Auxillary Space - O(1) --Creating a variable and assigning value to it.
# 2) Linear Auxiliary Space - O(n) --"Creating separate list means "O(n)"
'''nums=[1,2,3,4,5]
square=[]
for num in nums:
    square.append(num*num)
print(square)'''         #Output:[1,4,9,16,25]
# 3) Quadratic Auxiliary Space - O(n^2)---(Eg:Matrix)
'''def create_matrix(n):
    matrix=[]
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(0)
        matrix.append(row)
    return matrix
print(create_matrix(3))  '''   #Output:[[0,0,0],[0,0,0],[0,0,0]]













