import os
import csv
bank_path=os.path.join("PyBank","Resources", "budget_data.csv")
with open(bank_path) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    for row in csvreader:
        print(row)