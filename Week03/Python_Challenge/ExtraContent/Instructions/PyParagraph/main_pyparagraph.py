# Module for DOS command
import os
# Module for reading CSV files
import re

# import numpy


# Input file name that you want to analyse
fname = input(f'What is the filename you want to analyse?')

# Open directory
dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, 'raw_data', fname)

f = open(filepath, encoding='utf-8')
para = f.read()
f.close()
print(para)

# RegEx Pattern
sentence_pattern = ("(?<=[.!?]) +")
word_pattern = ('\s')

# Get words in the paragraph as list by splitting any white spaces
words = re.split(word_pattern, para)

# Calculate Average Letter Count
len_letter = [len(word) for word in words]
avg_letter = round(sum(len_letter)/len(len_letter),1)

# Get sentences in the paragraph as list by splitting [.!?] 
sentences = re.split(sentence_pattern, para)

# Calculate Average Sentence Count
len_sentence = [len(sentence.split(' ')) for sentence in sentences]
avg_sentence = round(sum(len_sentence)/len(len_sentence),1)

print(f'Paragraph Analysis')
print(f'---------------------------------')
print(f'Approximate Word Count {len(words)}')
print(f'Approximate Sentence Count {len(sentences)}')
print(f'Average Letter Count: {avg_letter}')
print(f'Average Sentence Length: {avg_sentence}')

# Print to file
# Create Analysis Directory to Save Output
outpath = os.path.join(dirname,'Analysis')
os.makedirs(outpath, exist_ok=True)

# Open the file for write and write result
output = open(f'{outpath}\out_pyparagraph.txt','w')
output.write('Paragraph Analysis \n')
output.write('--------------------------------- \n')
output.write(f'Approximate Word Count {len(words)} \n')
output.write(f'Approximate Sentence Count {len(sentences)} \n')
output.write(f'Average Letter Count: {avg_letter} \n')
output.write(f'Average Sentence Length: {avg_sentence} \n')
output.close()
