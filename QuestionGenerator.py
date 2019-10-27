#NOTES:
#This script generates question from the UT-Dallas Dataset.
#It makes line specific adjustments to generate the correct data; it will NOT work on general datasets
#Given a sentence, it will generate two questions:
#--------------"What does <pronoun> refer to?"
#--------------"What <clause>?"
#--------------FOR EXAMPLE: "The bee landed on the flower because it had pollen."
#--------------"What does it refer to?"
#--------------"What had pollen?"
#These question will be output to a text file, with each question on a seperate line.
#No white space between question pairs.

import sys
import select

i = 1
file = open("UTDallasDataset.txt", "r")
formattedfile = file.read().splitlines()

for line in formattedfile:
    if i % 5 == 1:
        question = line
    if i % 5 == 2:
        pronoun = line
        clause = question[question.index(pronoun) + len(pronoun):-1]
    if i % 5 == 3: #Totally arbitrary condition to print questions.
        print("What does " + pronoun + " refer to?")
        print("What" + clause + "?")
    i += 1

