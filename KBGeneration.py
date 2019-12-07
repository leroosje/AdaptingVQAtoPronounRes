
import sys
import select

i = 1
file = open("UTDallasDataset.txt", "r")
formattedfile = file.read().splitlines()

for line in formattedfile:
    if i % 5 == 1:
        knowledge = line
        print(str(knowledge))
        print(str(knowledge))

    i += 1

