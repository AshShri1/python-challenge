import os
import csv

import re


numWords = 0
numLines = 0
numChars = 0

avgLetterCount = 0
avgSentenceCount = 0
avgSentenceLength = 0

paragraphTxt = []


paragraphCSV = os.path.join('raw_data', 'paragraph_2.txt')

#open paragraph file
with open(paragraphCSV, 'r') as csvFile:
    for row in csvFile:
        #count words
        words =row.split()
        numWords += len(words)

        #split the paragraph by full stop to count the sentence count
        numLines = numLines + len(row.split('.')) - 1

        numChars += len(row)

# calculate average letter and sentence length
avgLetterCount = numChars / numWords
avgSentenceLength = numWords / numLines

#print the counts and averages
print("Approximately Word Count : " + str(numWords))
print("Approximately Sentence Count : " + str(numLines))
print("Average Letter Count : " + str(avgLetterCount))
print ("Average Sentence Length : " + str(avgSentenceLength))
