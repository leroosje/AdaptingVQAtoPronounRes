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
file = open("WinogradChallenge.txt", "r")
formattedfile = file.read().splitlines()

with open("WinogradChallengeCSV.csv", "w", encoding='UTF8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["Knowledge Base", "Question", "Option 1", "Option 2", "Actual Answer", "Bit Representation"])
    for line in formattedfile:
        if i % 7 == 1:
            question = line
        if i % 7 == 2:
            clause = line
            clause = clause[9:]
            pronoun = clause.split()[0]
        if i % 7 == 3:
            answer1 = line
        if i % 7 == 4:
            answer2 = line
        if i % 7 == 5:
            correctanswer = line
            correctanswer = line[16:]
            if correctanswer == 'A':
                answer = answer1
                answerbit = 0
            if correctanswer == 'B':
                answer = answer2
                answerbit = 1
        if i % 7 == 0: #Totally arbitrary condition to print questions.
            q1 = "What does " + pronoun + " refer to?"
            q2 = "What" + clause[len(pronoun):] + "?"

            option1 = pronoun + " refers to " + answer1
            option2 = pronoun + " refers to " + answer2

            if answer == answer1:
                answerbit = "0"
            if answer == answer2:
                answerbit = "1"

            row1 = [question, q1, option1, option2, answer, answerbit]
            row2 = [question, q2, option1, option2, answer, answerbit]

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




