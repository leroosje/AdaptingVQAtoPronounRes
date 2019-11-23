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
import random
from nltk.corpus import names
import nltk

nltk.download('names')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def gender_features(word):
    return {'name': word}

labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                 [(name, 'female') for name in names.words('female.txt')])
random.shuffle(labeled_names)

featuresets = [(gender_features(n), gender)
               for (n, gender) in labeled_names]

train_set, test_set = featuresets, featuresets
classifier = nltk.NaiveBayesClassifier.train(train_set)

i = 1
file = open("UTDallasDataset.txt", "r")
formattedfile = file.read().splitlines()

with open("UTDallasCSVGenderFeature.csv", "w", encoding='UTF8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["Knowledge Base", "Question", "Option 1", "Option 2", "Actual Answer", "Bit Representation", "Opt1GenderFeature", "Opt2GenderFeature"])
    for line in formattedfile:
        if i % 5 == 1:
            question = line
        if i % 5 == 2:
            pronoun = line
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

            pronoungender = classifier.classify(gender_features(pronoun))
            opt1gender = classifier.classify(gender_features(answer1))
            opt2gender = classifier.classify(gender_features(answer2))

            if pronoungender == opt1gender:
                answer1gender = "1"
            else:
                answer1gender = "0"
            if pronoungender == opt2gender:
                answer2gender = "1"
            else:
                answer2gender = "0"

            row1 = [question, q1, option1a, option2a, answer, answerbit, answer1, answer2, answer1gender, answer2gender]
            row2 = [question, q2, option1b, option2b, answer, answerbit, answer1, answer2, answer1gender, answer2gender]

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

i = 1
file = open("WinogradChallenge.txt", "r")
formattedfile = file.read().splitlines()

with open("WinogradChallengeCSVGenderFeature.csv", "w", encoding='UTF8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["Knowledge Base", "Question", "Option 1", "Option 2", "Actual Answer", "Bit Representation", "Opt1", "Opt2", "Opt1Gender", "Opt2Gender"])
    for line in formattedfile:
        if i % 7 == 1:
            question = line
        if i % 7 == 2:
            clause = line
            clause = clause[9:]
            tokenized = nltk.word_tokenize(clause)
            pospairs = nltk.pos_tag(tokenized)
            for pair in pospairs:
                if pair[1] == "PRP":
                    pronoun = pair[0]
                if pair[1] == "PRP$":
                    pronoun = pair[0]
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
            if correctanswer == 'A.':
                answer = answer1
                answerbit = 0
            if correctanswer == 'B':
                answer = answer2
                answerbit = 1
            if correctanswer == 'B.':
                answer = answer2
                answerbit = 1
        if i % 7 == 0: #Totally arbitrary condition to print questions.
            q1 = "What does " + pronoun + " refer to?"
            q2 = "What" + clause[len(pronoun):] + "?"

            option1a = pronoun + " refers to " + answer1
            option2a = pronoun + " refers to " + answer2

            option1b = answer1 + clause[len(pronoun):]
            option2b = answer2 + clause[len(pronoun):]

            if answer == answer1:
                answerbit = "0"
            if answer == answer2:
                answerbit = "1"

            pronoungender = classifier.classify(gender_features(pronoun))
            opt1gender = classifier.classify(gender_features(answer1))
            opt2gender = classifier.classify(gender_features(answer2))

            if pronoungender == opt1gender:
                answer1gender = "1"
            else:
                answer1gender = "0"
            if pronoungender == opt2gender:
                answer2gender = "1"
            else:
                answer2gender = "0"

            row1 = [question, q1, option1a, option2a, answer, answerbit, answer1, answer2, answer1gender, answer2gender]
            row2 = [question, q2, option1b, option2b, answer, answerbit, answer1, answer2, answer1gender, answer2gender]

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






