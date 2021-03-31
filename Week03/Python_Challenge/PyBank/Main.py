# Module for DOS command
import os
# Module for reading CSV files
import csv
dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'Resources', 'budget_data.csv')

# print(dirname)

Date, PL = [], []
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Loop through looking for the video
    for row in csvreader:
        Date.append(row[0])
        PL.append(row[1])

# Data clean-up, remove the header
Date.remove(Date[0])
PL.remove(PL[0])

# Convert PL string to integer
PL = [int(i) for i in PL]

# Total Number of months
Total_Months = len(PL)
print(f'Total Months : {Total_Months}')
# Total sum P/L
Total_PL = sum(PL)
print(f'Total  : $ {Total_PL}')

PL_change=[]
# Finding Change
for i in range(len(PL)-1):
    PL_change.append(PL[i+1]-PL[i])

# Average Change
avg_PL = sum(PL_change)/len(PL_change)
print('Average Change: %.2f' %avg_PL)

# Finding max/min P/L
max_PL = max(PL_change)
in_max = PL_change.index(max_PL)
min_PL = min(PL_change)
in_min = PL_change.index(min_PL)
print(f'Greatest Increase in Profits : {Date[in_max+1]}' + f' ($ {max_PL})')
print(f'Greatest Decrease in Profits : {Date[in_min+1]}' + f' ($ {min_PL})')


# Print to file

# Create Analysis Directory to Save Output
outpath = os.path.join(dirname,'Analysis')
os.makedirs(outpath, exist_ok=True)

# Open the file for write and write result
output = open(f'{outpath}\out_pybank.txt','w')
output.write(f'Total Months : {Total_Months} \n')
output.write(f'Total  : $ {Total_PL} \n')
output.write('Average Change: %.2f \n' %avg_PL)
output.write(f'Greatest Increase in Profits : {Date[in_max+1]}' + f' ($ {max_PL}) \n')
output.write(f'Greatest Decrease in Profits : {Date[in_min+1]}' + f' ($ {min_PL})')
output.close()

# Pypoll
