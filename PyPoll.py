#Need to retreive the following information:
#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote
#Path to file: Resources/election_results.csv
#Macintosh HD/Users/alyssa/Documents/Bootcamp/Module 3- Python/Election_Analysis/Resources/election_results.csv

#Add dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")


# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialise the total votes, BEFORE the file is opened
total_votes=0

# Declare a new list
candidate_options = []

# Declare new dictionary
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    # reader comes from csv module. 
    file_reader = csv.reader(election_data)

    # Print the header row. Next() lets us skip first row and return next item in list.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        
        # Print the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:         
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate]
    # 3. Calculate the percentage of votes.
    vote_percentage = int(votes) / int(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate}: received {vote_percentage:.1f}% of the vote.")

    # To do: print out each candidate's name, vote count, and percentage # of votes to the terminal.
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate  

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

