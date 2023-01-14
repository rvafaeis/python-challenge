import os
import csv
bank_path=os.path.join("PyBank","Resources", "budget_data.csv")
with open(bank_path) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    months=[]
    profits=[]
    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))
    total_number_of_months=len(months)
    total_profits=sum(profits)
    changes=[]
    for i in range(1,len(profits)):
        changes.append(profits[i]-profits[i-1])
    average_change=sum(changes)/len(changes)
    
        
        