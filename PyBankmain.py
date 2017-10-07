#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The total amount of revenue gained over the entire period
#The average change in revenue between months over the entire period
#The greatest increase in revenue (date and amount) over the entire period
#The greatest decrease in revenue (date and amount) over the entire period

import os
import csv

budget_data_1 = os.path.join("/Users/michaeldurst/Documents/GW_Data/resources/budget_data_1.csv")

budget_data_2 = os.path.join("/Users/michaeldurst/Documents/GW_Data/resources/budget_data_2.csv")

months1 = []
revenue1 = []
months2 = []
revenue2 = []

with open(budget_data_1, newline"") as cvsfile:
    csvreader = csv.reader(csvfile, delimeter=",")
    
    total_revenue = 0
    total_months = 0

    for row in csvreader:
        total_revenue += row[1]
        total_months += 1
        



#date

# 1 big loop
#load data, loop for how long the file is(count)months=0 total months + 1
#in  the same for loop, sum of revenue, revenue = 0, revenue= revnue + int of column
#put each column into its own list
#month 0 corresponds to revenue 0 when you set to lists

    
        
#Total Months
        #totalMonths = int(budget_data_1[1])

#Total Revenue
        #totalRevenue = int(budget_data_1[1])