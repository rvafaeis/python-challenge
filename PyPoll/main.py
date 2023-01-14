import os
import csv
poll_path=os.path.join("PyPoll","Resources", "election_data.csv")
with open(poll_path) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    for row in csvreader:
        print(row)