print("Election Results")
print("--------------------------------------------------------------")

# 1) Calculate the total number of votes cast

# Import Modules
import os
import csv

# Set the path to election_data csv file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the csv file
with open(csvpath, encoding='utf') as csvfile:

    # Use csvreader to specify delimiter and variable that holds csv contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the header row
    csv_header = next(csvreader)

    # Increment a counter for each row (each row represents a vote)
    num_votes = 0

    # create a list for candidates and dictionary to compile votes per candidate
    candidates = []
    vote_count = {}

    # loop through each row and add to counter
    for row in csvreader:
        # add the total number of votes
        num_votes += 1

        # conditional statement to add total votes per unique candidate       
        if row[2] not in vote_count:
            vote_count[row[2]] = 0
        vote_count[row[2]] = vote_count[row[2]] + 1

    # print the value of total votes    
    print(f"Total Votes: {num_votes}")
    
    print("--------------------------------------------------------------")

# 2) Calculate the list of candidates who received votes
# 3) Calculate the percentage of votes each candidate won
# 4) Calculate the total number of votes each candidate won

    # list comprehension for each candidate with percentage votes tally  
    candidates = [{row : round(vote_count[row]/num_votes * 100, 3)} for row in vote_count]   
    
    # removing 1st item from the candidates list
    candidate1 = candidates.pop()
    # retrieving 1st key:value pair
    for i, j in candidate1.items():
        print(f"{i}: {j}% ({vote_count[i]})")
    
    # removing next item from the candidates list
    candidate2 = candidates.pop()
    # retrieving next key:value pair
    for i, j in candidate2.items():
        print(f"{i}: {j}% ({vote_count[i]})")

    # removing last item from the candidates list
    candidate3 = candidates.pop()
    # retrieving last key:value pair
    for i, j in candidate3.items():
        print(f"{i} {j}% ({vote_count[i]})") 
    
    print("--------------------------------------------------------------")
    
# 5) Calculate the winner of the election based on popular vote
   
    # retrieving the election winner
    for i, j in candidate2.items():
        
        # print the election winner
        print(f"Winner: {i}")
    
#--------------------------------------------------------------------------------
# to export a text file with script results:
# type python main.py > main.txt on GitBash