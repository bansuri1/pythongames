file = open("sgb-words.txt", "r")

# all five letter words
fiveLetter = []
for line in file:
    fiveLetter.append(line.strip())

file.close()

# all five letter words with unique letters
uqfiveLetter = []
for word in fiveLetter:
    if len(word) == len(set(word)):
        uqfiveLetter.append(word)
