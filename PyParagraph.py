#Approximate word count
#Approximate sentence count
#Approximate letter count (per word)
#Average sentence length (in words)

import os
import csv
import re

read_paragraph1 = "1"
# Run the code so long as the user wants to manage the systm
while manage_system == "1":
    # Take users input
    action_item = input("What csv file would you like to view today? (1)PyParagraph? or (2)PyParagraph?")
    if action_item == "1":

        file = "Pyparagraph_1.txt"

        num_words = 0
        num_sentences = 0
        num_letters = 0
        avg_sentenence_len = 0 

    with open(file, 'r') as file:
    for line in file:
        wordsList = line.split()
        num_sentences += 1
        num_words += len(wordsList)
        num_letters += len(line)

    print(num_letters, num_sentences, num_words)
    
