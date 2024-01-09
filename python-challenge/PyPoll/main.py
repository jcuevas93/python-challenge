import os
import csv

# path
election_data = os.path.join("Resources", "election_data.csv")
output_folder_path = "analysis"
output_file_path = os.path.join(output_folder_path, "election_analysis.txt")

total_votes = 0
candidates = {}

# create analysis folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# read in csv    
with open(election_data) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")

    # Read through each row of data
    for row in csv_reader:
        # Calculate total number of votes
        total_votes += 1
        candidate = row["Candidate"]
        # create candidate as key and tally up votes
        try:
            candidates[candidate] += 1
        except KeyError:
            candidates[candidate] = 1          

# Generate summary
summary = "Election Results \n"
summary += "--------------------\n"
summary += f"Total Votes: {total_votes}\n"
summary += "--------------------\n"
winner = ""
max_votes = 0
for candidate, votes in candidates.items():
    vote_percentage = round(votes/total_votes * 100, 3)
    candidate_summary = f"{candidate} : {vote_percentage}% ({votes})\n\n"
    summary += candidate_summary

    if votes > max_votes:
        max_votes = votes
        winner = candidate

summary += "--------------------\n"
summary += f"Winner: {winner}\n"
summary += "--------------------\n"
print(summary)

# Write the analysis results to a text file in the 'analysis' folder
with open(output_file_path, "w") as txt_file:
    txt_file.write(summary)
