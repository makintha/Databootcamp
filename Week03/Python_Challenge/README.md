# Python Challenge

## 1. Background
In this homework we are tasked to use `python` codes to do the following:
* pypoll - To count and summarize the poll results (`main_pypoll.py`)
* pybank - To calculate the monthly profit/loss for a bank(`main_pybank.py`)
* pyboss - To store and employee data in a certain way (`main_pyboss.py`)
* pyparagprah - To read and count words, sentences metrics in paragraphs (`main_pyparagraph.py`)

## 2. Solution
4-off `python` codes have been created to solve the given problem. The file is name with the following naming format:
`prefix_main_respected problem`, e.g. for pypoll it will be `main_pypoll.py`,etc.

When the `pyton` code executed, it will print the result to terminal as well will print to output file. The naming format is as follows: `out_respected problem`. The extensions are *.txt, except for pyboss, *.csv. The output file will be stored inside `Analysis` folder for the respective problem

Note that for the pyparagraph problem, when the sample paragraph is executed, it will return total words of 120 instead of 122 as mention in the task. When this paragraph is pasted to **Microsoft Words** it will also return 120.

## 3. Result
### pypoll
```
Election Results 
------------------------------------- 
Total Votes : 3521001 
------------------------------------- 
Khan:  63.000% (2218231) 
Correy:  20.000% (704200) 
Li:  14.000% (492940) 
O'Tooley:  3.000% (105630) 
------------------------------------- 
Winner : Khan 
------------------------------------- 
```

### pybank
```
Total Months : 86 
Total  : $ 38382578 
Average Change: -2315.12 
Greatest Increase in Profits : Feb-2012 ($ 1926159) 
Greatest Decrease in Profits : Sep-2013 ($ -2196167)
```

### pyboss
```
Emp ID,First Name,Last Name,DOB,SSN,State
232,John,Mathews,02/24/1991,***-**-9165,ND
533,Nathan,Moore,11/19/1978,***-**-7469,ME
256,Amanda,Douglas,01/08/1990,***-**-6961,ID
189,Heather,Andrews,08/11/1976,***-**-1797,VT
284,Daniel,Hernandez,07/22/1976,***-**-7473,CO
```

### pyparagraph
```
Paragraph Analysis 
--------------------------------- 
Approximate Word Count 120 
Approximate Sentence Count 5 
Average Letter Count: 4.6 
Average Sentence Length: 24.0 
```