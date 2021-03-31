# Module for DOS command
import os
# Module for reading CSV files
import csv
from collections import Counter

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname,'employee_data.csv')

# List abbreviation of US States
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# Variable definition
Employee = {'ID': {}}
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header 
    csv_header = next(csvreader)
    # print(csv_header)
    IDs=[]
    for row in csvreader:
        Employee['ID'][f'{row[0]}']={}
        IDs.append(row[0])

        # Filling the Dictionary
        # First and Last Name
        Employee['ID'][f'{row[0]}']['First Name']=((row[1].split(" ")[0]))
        Employee['ID'][f'{row[0]}']['Last Name']=((row[1].split(" ")[1]))

        # DOB
        dob=row[2].split('-')
        Employee['ID'][f'{row[0]}']['DOB'] = (f'{dob[1]}/{dob[2]}/{dob[0]}')
        # SSN
        ssn=row[3].split('-')
        Employee['ID'][f'{row[0]}']['SSN'] = (f'***-**-{ssn[2]}')
        # State
        Employee['ID'][f'{row[0]}']['State'] = us_state_abbrev[f'{row[4]}']


    # print(Employee['ID']['650'], len(Employee['ID']))

# Print to file
# Create Analysis Directory to Save Output
outpath = os.path.join(dirname,'Analysis')
os.makedirs(outpath, exist_ok=True)

output = open(f'{outpath}\out_pyboss.csv','w')

output.write(f'Emp ID,First Name,Last Name,DOB,SSN,State\n')
for i in range(len(IDs)):
    # print(Employee['ID'][ID[i]]['First Name'])
    output.write(f'{IDs[i]},{Employee["ID"][IDs[i]]["First Name"]},{Employee["ID"][IDs[i]]["Last Name"]},{Employee["ID"][IDs[i]]["DOB"]},{Employee["ID"][IDs[i]]["SSN"]},{Employee["ID"][IDs[i]]["State"]}\n')
output.close()



