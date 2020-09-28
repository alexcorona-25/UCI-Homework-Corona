#importing the plugins
import os
import csv

#Creating path for our electoin data file
csvpath = os.path.join('Resources', 'election_data.csv')

#Creating varibales and list to hold the candidate name and votes
total_votes = 0
candidate = []
vote_per_candidate = []

#Opening and Reading the CSV file
with open(csvpath) as election:
    csvreader=csv.reader(election, delimiter=',')
    
    #Skip Header for Row Count
    csv_headr = next(csvreader)
 
    for row in csv.reader(election):
    #Append the value found for months and profits to the new varibales list created
        total_votes += 1
    # stating row 2 is where the candidates name is location
        candidate_location= (row[2])
    #Finding the repition of a candidates name and increasing the value of 1 every time it reappears
        if candidate_location in candidate:
           candidate_index = candidate.index(candidate_location)
           vote_per_candidate[candidate_index] = vote_per_candidate[candidate_index] +1
       #Appending any new name to the index and adding a vote of 1
        else:
            candidate.append(candidate_location)
            vote_per_candidate.append(1)
#Finding the percentage of each candidate and the name
percent = []
max_vote = vote_per_candidate[0]
max_index = 0
#calulating the percentange using V as the place holder value
for v in range(len(candidate)):
    vote_percentage = round(vote_per_candidate[v]/total_votes * 100, 2)
    percent.append(vote_percentage)
# # Running through the loop and finding the greatest value (Max vote winner)
    if vote_per_candidate[v] > max_vote:
        max_vote = vote_per_candidate[v]
        max_index = v
#Finding the election winner
election_winner = candidate[max_index]

#printing the values onto the terminal       
print(f"Election Resluts")
print(f"-----------------------------------")
print(f"Total votes: {total_votes}")
print(f"-----------------------------------")
for v in range(len(candidate)):
    print(f" {candidate[v]} : {percent[v]}% ({vote_per_candidate[v]})")
print(f"-------------------------------------")
print(f"Election Winner: {election_winner.upper()}")

#Creating a text file with the results printed
csvpath = os.path.join('Analysis', 'election_data_summary.txt')
with open(csvpath,"w") as file:
    # Write methods to print to Financial_Analysis_Summary 
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total votes: {total_votes}")
    file.write("\n")
    for v in range(len(candidate)):
        file.write(f" {candidate[v]} : {percent[v]}% ({vote_per_candidate[v]})")
    file.write("\n")
    file.write(f"Election Winner: {election_winner.upper()}")
    file.write("\n")