import csv #importing csv library to be able to execute the code
with open('sales.csv', 'r') as csv_file: #how to read the file
    spreadsheet = csv.DictReader(csv_file) #how to read the file
   sales = [] #first step in creating the sales list
   for row in spreadsheet: #how to read the file
       sales_list = int(row['sales']) #second step in creating the sales list
       sales.append(sales_list) #this is the list for sales each month
       print(sales_list) #printing out the sales for each month
   for row in spreadsheet:
        sales_highest = row['sales']
        sales.append(sales_highest)
        lowest_sales = min(sales)
        highest_sales = max(sales)

total_sales = sum(sales) #this doesn't work because of int/str
print('The total amount of sales across the months is £{}'.format(total_sales))



for i in range(len(months) - 1):
        current_month = months[i]
        next_month = months[i + 1]

        current_sales = monthly_sales[current_month]
        next_sales = monthly_sales[next_month]

        percentage_change = ((next_sales - current_sales) / current_sales) * 100
21941866
        print(f'Monthly percentage change from {current_month} to {next_month}: {percentage_change:.2f}%')



#extension tasks
#months with highest and lowest sales, average sales
#export to spreadsheet, download pyexcel or pandas
#change dataset eg. amazon sales

import csv

with open('sales.csv', 'r') as csv_file: #this reads the csv file downloaded
    spreadsheet = csv.DictReader(csv_file) #this also reads the file
    sales = [] #creating a sales list for later

    for row in spreadsheet: #looping through the rows in the csv to exctract sales data
        sales_list = int((row['sales']))
        sales.append(sales_list) #adding sales to the sales list

    total_sales = sum(sales) #extended tasks
    lowest_sales = min(sales)
    highest_sales = max(sales)
    average = sum(sales) / len(sales)

    print(f'The total amount of sales across the months is £{total_sales}')
    print(f'Highest Sales: {highest_sales}')
    print(f'Lowest Sales: {lowest_sales}')
    print(f'Average Sales:{rounded_average}')


#import pandas as pd #this is where i tried to write the data as an excel file but didn't really work as don't want to use import csv and import pandas
#read_file_product = pd.read_csv (r'C:\Users\ebony\PycharmProjects\pythonProject\cfg-python\venv\sales_data_sample.csv')
#read_file_product.to_excel (r'C:\Users\ebony\PycharmProjects\pythonProject\cfg-python\venv\sales2.xlsx', index = 'none', header = 'true')
