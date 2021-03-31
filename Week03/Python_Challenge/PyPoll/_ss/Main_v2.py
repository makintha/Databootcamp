# Module for DOS command
import os
# Module for reading CSV files
import csv
from collections import Counter

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'Resources', 'election_data.csv')
       
# Variable definition
Election_Result = {'Name': [], 'Vote': {}, 'Pct':{}}

# Read through CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header 
    csv_header = next(csvreader)

    # Loop through and take out the vote result   
    Votes=[]
    for row in csvreader:
        # Collect the votes
        Votes.append(row[2])
        if row[2] not in Election_Result['Name']:
            Election_Result['Name'].append(row[2])
            Election_Result['Vote'][f'{row[2]}']=[]
            Election_Result['Pct'][f'{row[2]}']=[]

# Filling in the Dictionary with Candidate Name, Number of vote and percentage vote of each Candidate
for i, Candidate in enumerate(Election_Result['Name']):
        Total_votes = len(Votes)
        Election_Result['Vote'][f'{Candidate}'] = Votes.count(f'{Candidate}')
        each_cand_vote = Votes.count(f'{Candidate}')
        percentage = round(each_cand_vote / Total_votes * 100)
        Election_Result['Pct'][f'{Candidate}'] = (f'{percentage: .3f}%')

# Finding Winner based on the maximum vote
# Start of maximum vote
l = 0
# Start of Winner Name
winner = "Me"
for i, Candidate in enumerate(Election_Result['Name']):
    if Election_Result['Vote'][f'{Candidate}'] > l:
        l = Election_Result['Vote'][f'{Candidate}']
        winner = Candidate

# print to Terminal
print(f'Election Results')
print(f'-------------------------------------')
print(f'Total Votes : {Total_votes}')
print(f'-------------------------------------')

for i, Name in enumerate(Election_Result['Pct']):

    print(f"{Election_Result['Name'][i]}: {Election_Result['Pct'][f'{Name}']} ({Election_Result['Vote'][f'{Name}']})")

print(f'-------------------------------------')
print(f'Winner : {winner}')
print(f'-------------------------------------')

# Print to file

# Create Analysis Directory to Save Output
outpath = os.path.join(dirname,'Analysis')
os.makedirs(outpath, exist_ok=True)

# outpath = os.path.join(dirname, 'Analysis', 'election_data.csv')
output = open(f'{outpath}\out_pypoll.txt','w')
output.write(f'Election Results \n')
output.write(f'------------------------------------- \n')
output.write(f'Total Votes : {Total_votes} \n')
output.write(f'------------------------------------- \n')
# print(Election_Result)
for i, Name in enumerate(Election_Result['Pct']):

    output.write(f"{Election_Result['Name'][i]}: {Election_Result['Pct'][f'{Name}']} ({Election_Result['Vote'][f'{Name}']}) \n")

output.write(f'------------------------------------- \n')
output.write(f'Winner : {winner} \n')
output.write(f'------------------------------------- \n')
output.close()


