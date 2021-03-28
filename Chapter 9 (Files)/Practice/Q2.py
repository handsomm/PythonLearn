# The game() function in a programm lets a user play a game and returns the score as an integer. You need to read a file 'hiscore.txt' which is either blank or contains the previous hi-score. You need to write a programm to update the hiscore whenever game() breaks the hiscore.
import random

def game():
    n = random.randint(1, 50)
    return n

score = game()
with open("highscore.txt") as f:
    highscore = f.read()

if highscore == '':
    with open("highscore.txt", 'w') as f:
        f.write(str(score))

if int(highscore) < score:
    with open("highscore.txt", 'w') as f:
        f.write(str(score))