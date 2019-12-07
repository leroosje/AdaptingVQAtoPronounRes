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

