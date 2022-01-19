

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
