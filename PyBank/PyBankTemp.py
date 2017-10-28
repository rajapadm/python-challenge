import os

filepath=os.path.join('raw_data','budget_data_1.csv')

date=[]
revenue=[]

import csv
with open(filepath, newline='') as csvfile:
    
    csvreader=csv.reader(csvfile,delimiter=',')
    
    next(csvreader,None)
    print("Financial Analysis")
    print("------------------------------")
    row_count = sum(1 for row in csvreader)
    print(f"Total Months:  {row_count}")
    
    for row in csvreader:
        date.append(row[0])
        revenue.append(row[1])
    print(revenue)