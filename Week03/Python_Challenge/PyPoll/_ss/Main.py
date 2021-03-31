# Module for DOS command
import os
# Module for reading CSV files
import csv
from collections import Counter

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'Resources', 'Test.csv')

def group_list(lst):
      
    return list(zip(Counter(lst).keys(), Counter(lst).values()))
      

Vote ={}
Percentage={}
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Loop through looking for the video
    
    Poll=[]
    for row in csvreader:
        Poll.append(row[2])
        if row[2] not in Vote:
            Vote[f'{row[2]}']=[]
            Percentage[f'{row[2]}']=[]
            # Candidate.append(row[2])
    
    for i, Candidate in enumerate(Vote):
        Vote[f'{Candidate}'] = Poll.count(f'{Candidate}')
        # pct
print(Vote)


