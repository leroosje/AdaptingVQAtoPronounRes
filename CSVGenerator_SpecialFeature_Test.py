import csv

i = 1
file = open("WinogradChallenge.txt", "r")
formattedfile = file.read().splitlines()

with open("WinogradSpecialFeatureCSV.csv", "w", encoding='UTF8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["Question String", "Pronoun", "Split1", "Split2", "Option1", "Option2"])
    for line in formattedfile:
        if i % 7 == 1:
            question = line
        if i % 7 == 2:
            snippet = line[9:]
        if i % 7 == 3:
            answer1 = line
        if i % 7 == 4:
            answer2 = line
        if i % 7 == 0: #Totally arbitrary condition to print questions.
            print(question)
            print(snippet)
            split1, split2 = question.split(" " + snippet, 1)

            row1 = [question, snippet, split1, snippet + split2, answer1, answer2]

            writer.writerow(row1)
        i += 1




