
# logic variables
variable name | type | default value | description | function
---|---|---|---|---
turns|int|0|counts the number of turns that the user has taken so far | main
won|bool|false|indicates if user guessed correctly | main
word|str|NA|random 5-letter word from dictionary where all letters are different | main
guess|str|NA|user-input guess for the word | main
result|str|NA|checkWord returns positions of incorrect and correct letters | main
playAgain|str|false|user-input 'yes' or 'no' to replay after winning or losing | main
guessWord|str|NA|see guess|checkWord
masterWord|str|NA|see word|checkWord
guessResult|str|""|see result|checkWord
index|int|0|index for each letter in guess|checkWord


# print variables
variable name|value
---|---
welcomeMessage|I am thinking of a 5-letter word. Can you guess it in 6 tries?
wrongLengthError|Please enter a 5 letter word.
nonWordError|Word not found in dictionary.
tryAgainMessage|Not quite right...try again! Here's how you guessed:
congratsMessage|You got it - well done!
sorryMessage|Sorry, that's not correct! Here's the word I was thinking of:
playAgainMessage|Would you like to play again?
