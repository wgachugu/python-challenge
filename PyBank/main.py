print("Financial Analysis")
print("--------------------------------------------------------------")

# 1) Calculate the total number of months included in the dataset
# Import Modules
import os
import csv

# Set the path to budget_data csv file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the csv file
with open(csvpath, encoding='utf') as csvfile:

    # Use csvreader to specify delimiter and variable that holds csv contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Increment a counter for each row (each row represents a month)
    num_months = 0

    # skip the header row
    csv_header = next(csvreader)
    
    # create list for profit/loss column
    column1 = []
    
    # create list for changes in profit/loss column
    column2 = []

    # create list for date column
    column0 = []

    # create counter for summing values in column1 list
    sum_column1 = 0
    
    # create counter for summing values in column2 list
    sum_column2 = 0

    # loop through each row and add to counter
    for row in csvreader:
        num_months += 1
        column1.append(int(row[1]))
        # also append dates onto column0 list
        column0.append(row[0])
    # print the value of total months    
    print(f"Total Months: {num_months}")

    # print the list with dates
    # print(column0)
#---------------------------------------------------------------

# 2) Calculate the net total amount of profit/losses over the entire period
   
   # Sum the values of the profit/loss 
    for i in column1:
        sum_column1 = sum_column1 + i

    print (f"Total: ${sum_column1}")
#---------------------------------------------------------------

# 3) Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes

    # Subtract the values of the profit/loss items and append to column2 list
    
    for i in range(len(column1)):
        if i > 0:
            change = column1[i] - column1[i-1]
            column2.append(change)
    
    # Calculate the average change by summing column2 and dividing by count of column2 items
    for i in column2:
        sum_column2 = sum_column2 + i
    print("Average Change: $" + str(round(sum_column2 / len(column2),2)))
#---------------------------------------------------------------

# 4) Calculate the greatest increase in profits (date and amount) over the entire period

    max_change = max(column2)
    max_index = column2.index(max_change)

    # add 1 to max_index in output below since we skipped the first item in conditional statement of part 3 above
    print(f"Greatest Increase in Profits: {column0[max_index+1]} (${max_change})")
#---------------------------------------------------------------

# 5) Calculate the greatest decrease in profits (date and amount) over the entire period

    min_change = min(column2)
    min_index = column2.index(min_change)
    
    # add 1 to min_index in output below since we skipped the first item in conditional statement of part 3 above
    print(f"Greatest Decrease in Profits: {column0[min_index+1]} (${min_change})")
#---------------------------------------------------------------

# to export a text file with script results:
# type python main.py > main.txt on GitBash