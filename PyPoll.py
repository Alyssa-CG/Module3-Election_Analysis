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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    # reader comes from csv module. 
    file_reader = csv.reader(election_data)

    # Print the header row. Next() lets us skip first row and return next item in list.
    headers = next(file_reader)
    print(headers)