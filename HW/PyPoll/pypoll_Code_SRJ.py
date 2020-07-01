#import modules
import os
import csv
#defining path
csv_path = os.path.join("Resources", "election_data.csv")
output = ""
with open(csv_path) as csv_file:
    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')
    #printing header for output
    output ="Election Results\n-------------------------\n"
    next(csv_reader)
     #number of votes
    row_count = sum(1 for row in csv_file)
    output = output +"Total Votes: " + str(row_count)+"\n-------------------------\n"
#finds the unique candidates and puts them in a list    
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    Candidate = {}
    for row in csv_reader:
        if row[2] not in Candidate:
            Candidate[row[2]]=0             

Candidate.pop('Candidate')
#print(Candidate)
#finds the number of votes for each candidate
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    next(csv_reader)
    winner = ""
    most = 0
    for row in csv_reader:
        Candidate[row[2]] = Candidate[row[2]] + 1
    for key in Candidate:
        per = (Candidate[key]/row_count)*100 
        output = output + key + " " + "{:.2f}".format(per) + "% (" + str(Candidate[key])+ ") votes \n"
        if most < Candidate[key]:
            most = Candidate[key]
            winner = key
    output = output +"\n-------------------------\nThe winner is: " + winner
    print(output)
file1 = open("myresults.txt","w") 
file1.write(output)
file1.close()