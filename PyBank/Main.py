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
  
 # Obtain the max and min of the the montly profit change list
    max_increase_value = max(changes)
    max_decrease_value = min(changes)

# Correlate max and min to the proper month using month list and index from max and min
# plus 1 at the end since month associated with change is the + 1 month or next month
    max_increase_month = months[changes.index(max(changes)) + 1]
    max_decrease_month = months[changes.index(min(changes)) + 1]

# Print Statement
# Print Statement
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_number_of_months}")
print(f"Total Profits: ${total_profits}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Greatest Increase in Profits: {max_increase_month} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${(str(max_decrease_value))})")
#Financial Summary
output_file = os.path.join("PyBank", "Analysis", "Financial_Analysis_Summary.txt")
with open(output_file,"w") as file:
  # Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------\n")      
    file.write(f"Total Months: {total_number_of_months}\n")
    file.write(f"Total Profits:${total_profits}\n")
    file.write(f"Average Change: ${round(average_change,2)}\n")
    file.write(f"Greatest Increase in Profits: {max_increase_month} (${(str(max_increase_value))})\n")
    file.write(f"Greatest Decrease in Profits: {max_decrease_month} (${(str(max_decrease_value))})\n")