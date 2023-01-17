import os
import csv
poll_path=os.path.join("PyPoll","Resources", "election_data.csv")
with open(poll_path) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)

    votes=[]
    candidates={}

    for row in csvreader:
        votes.append(row[2])

    total_number_of_votes=len(votes)
    total_candidates=list(candidates)
    
    for cand in votes:
        if candidates.get(cand):
            candidates[cand] += 1
        else:
            candidates[cand] = 1

    print("Election Results")
    print("------------")
    print(f"Total Votes: {total_number_of_votes}")
    print("------------")
    for cand, votes in candidates.items():
        print(f"{cand}: {round((votes/total_number_of_votes) *100,3) }% ({votes})")
    print("------------")
    print(f"Winner: {max(candidates, key=candidates.get)}")

output_file = os.path.join("PyPoll", "Analysis", "Election_Results_Summary.txt")

with open(output_file,"w") as file:

# Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results\n")
    file.write("------------\n")
    file.write(f"Total Votes: {total_number_of_votes}\n")
    file.write("------------\n")
    for cand, votes in candidates.items():
        file.write(f"{cand}: {round((votes/total_number_of_votes) *100,3) }% ({votes})\n")
    file.write("------------\n")
    file.write(f"Winner: {max(candidates, key=candidates.get)}")
