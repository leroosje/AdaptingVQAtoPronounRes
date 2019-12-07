import csv
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

i = 1
file = open("WinogradChallenge.txt", "r")
formattedfile = file.read().splitlines()

with open("WinogradChallengeCSV.csv", "w", encoding='UTF8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["Knowledge Base", "Question", "Option 1", "Option 2", "Actual Answer", "Bit Representation", "Opt1", "Opt2"])
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




