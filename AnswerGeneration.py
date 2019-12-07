import sys
import select

i = 1
file = open("UTDallasDataset.txt", "r")
formattedfile = file.read().splitlines()

for line in formattedfile:
    if i % 5 == 4:
        answer = line
        print(str(answer))
        print(str(answer))

    i += 1

