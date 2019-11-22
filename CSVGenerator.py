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

with open("UTDallasCSV.csv", "w", encoding='UTF8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["Knowledge Base", "Question", "Option 1", "Option 2", "Actual Answer", "Bit Representation", "Opt1", "Opt2"])
    for line in formattedfile:
        if i % 5 == 1:
            question = line
        if i % 5 == 2:
            pronoun = line
            print(pronoun)
            print(question)
            clause = question[question.index(" " + pronoun) + len(" " + pronoun):-1]
        if i % 5 == 3:
            answerchoices = line
        if i % 5 == 4:
            answer = line
        if i % 5 == 0: #Totally arbitrary condition to print questions.
            q1 = "What does " + pronoun + " refer to?"
            q2 = "What" + clause + "?"

            answer1, answer2 = answerchoices.split(',')
            option1a = pronoun + " refers to " + answer1
            option2a = pronoun + " refers to " + answer2

            option1b = answer1 + clause
            option2b = answer2 + clause

            if answer == answer1:
                answerbit = "0"
            if answer == answer2:
                answerbit = "1"

            row1 = [question, q1, option1a, option2a, answer, answerbit, answer1, answer2]
            row2 = [question, q2, option1b, option2b, answer, answerbit, answer1, answer2]

            j = 0
            for item in row1:
                filteredstring = ""
                for word in item.split():
                    if not word.lower() == "the":
                        filteredstring = filteredstring + word.lower() + " "
                row1[j] = filteredstring
                j += 1 #sorry for the java-ism, not an expert in python

            j = 0
            for item in row2:
                filteredstring = ""
                for word in item.split():
                    if not word.lower() == "the":
                        filteredstring = filteredstring + word.lower() + " "
                row2[j] = filteredstring
                j += 1  # sorry for the java-ism, not an expert in python

            writer.writerow(row1)
            writer.writerow(row2)
        i += 1




