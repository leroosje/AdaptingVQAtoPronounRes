import sys
import select

i = 1
file = open("UTDallasDataset.txt", "r")
formattedfile = file.read().splitlines()

for line in formattedfile:
    if i % 5 == 3:
        answerchoices = line
        print(str(answerchoices))
        print(str(answerchoices))

    i += 1

