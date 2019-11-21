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
import csv
import sys
import select

i = 1
file = open("UTDallasDataset.txt", "r")
formattedfile = file.read().splitlines()

with open("UTDallasSpecialFeatureCSV.csv", "w", encoding='UTF8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["Question String", "Pronoun", "Split1", "Split2"])
    for line in formattedfile:
        if i % 5 == 1:
            question = line
        if i % 5 == 2:
            pronoun = line
        if i % 5 == 0: #Totally arbitrary condition to print questions.

            split1, split2 = question.split(" " + pronoun, 1)

            row1 = [question, pronoun, split1, pronoun + split2]

            writer.writerow(row1)
        i += 1




