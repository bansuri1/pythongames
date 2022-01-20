from words import fiveLetter, uqfiveLetter
import random

# global variables

welcomeMessage = "I am thinking of a 5-letter word. Can you guess it in 6 tries?"
wrongLengthError = "Please enter a 5-letter word."
nonWordError = "Word not found in dictionary."
tryAgainMessage = "Not quite right...try again! Here's how you guessed:"
congratsMessage = "You got it - well done!"
sorryMessage = "Sorry, that's not correct! Here's the word I was thinking of:"
playAgainMessage = "Would you like to play again?"
turnsMessage = "Number of tries remaining: "


def checkWord(masterWord, guessWord):
    index = 0
    guessResult = ""

    for letter in guessWord:
        if letter in masterWord:
            if index == masterWord.find(letter):
                guessResult += "G"
            elif guessWord.count(letter) > 1:
                guessResult += "R"
            else:
                guessResult += "Y"
        else:
            guessResult += "R"
        index += 1

    return guessResult


while True:
    print(welcomeMessage)
    turns = 0
    won = False
    word = random.choice(uqfiveLetter)
    #print(word)

    while turns < 6:
        while True:
            guess = (input("Enter guess> ")).lower()
            #print(turns)
            if len(guess) != 5:
                print(wrongLengthError)
            elif guess not in fiveLetter:
                print(nonWordError)
            else:
                break
        turns += 1
        result = checkWord(word, guess)
        if result == "GGGGG":
            won = True
            break
        else:
            print(tryAgainMessage)
            print(result)
            print(turnsMessage + str((6-turns)))

    if won == True:
        print(congratsMessage)
    else:
        print(sorryMessage)
        print(word)

    print(playAgainMessage)
    playAgain = input("Yes/No: ")

    if playAgain == "No":
        break
