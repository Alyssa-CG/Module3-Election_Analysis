# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")
# Initialize a total vote counter.
total_votes = 0

# Create a list for the counties.
county_names = []
# Create a dictionary where key is county and value is votes for that county.
county_votes = {}
# Create a string to hold county with largest turnout.
largest_turnout_county = ""
largest_turnout_count = 0
largest_turnout_percentage = 0

# Declare a variable to represent number of votes a county received.
county_vote_count = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
        # Check for county name and add to list
        county = row [1]
        if county not in county_names:
            county_names.append(county)
            county_votes[county] = 0
        # Increase county votes
        county_votes[county] += 1         
        
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #Print header for county votes to terminal and text file (could have also included above).
    print(f"County Votes:")
    txt_file.write(f"County_Votes:")

    # Get and print voter turnout results.
    for county in county_votes:
        countyvotes = county_votes[county]
        countyvotes_percentage = float(countyvotes) / float(total_votes) * 100
        county_results = (f"\n{county}:{countyvotes_percentage:.1f}% ({countyvotes:,})")

        # Print results to terminal and text file.
        print (county_results)
        txt_file.write(county_results)

        # Determine the county with the largest turnout.
        # Three if statements used as per instruction but as percentage is not printed/written, 
        # the same output can be generated without including the percentage below.
        if (countyvotes > largest_turnout_count) and (countyvotes_percentage > largest_turnout_percentage):
            largest_turnout_county = county
            largest_turnout_count = countyvotes
            largest_turnout_percentage = countyvotes_percentage
    
    #Print summary to terminal and text file.
    largest_county_summary=(
        f"\n\n-------------------------"
        f"\nLargest County Turnout: {largest_turnout_county}"
        f"\n-------------------------\n")
    print(largest_county_summary)   
    txt_file.write(largest_county_summary)

    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    
    
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
       