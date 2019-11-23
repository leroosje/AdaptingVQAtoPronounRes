import csv

i = 1
file = open("UTDallasDataset.txt", "r")
formattedfile = file.read().splitlines()

with open("UTDallasSpecialFeatureCSV.csv", "w", encoding='UTF8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["Question String", "Pronoun", "Split1", "Split2", "Option1", "Option2"])
    for line in formattedfile:
        if i % 5 == 1:
            question = line
        if i % 5 == 2:
            pronoun = line
        if i % 5 == 3:
            answerchoices = line
        if i % 5 == 0: #Totally arbitrary condition to print questions.

            split1, split2 = question.split(" " + pronoun, 1)
            answer1, answer2 = answerchoices.split(",")
            row1 = [question, pronoun, split1, pronoun + split2, answer1, answer2]

            writer.writerow(row1)
        i += 1




