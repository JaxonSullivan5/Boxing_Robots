from scoreboardClass import Scores
from time import sleep

score=Scores(26, 19, 13, 21, 20, 16, 12)

x=0

while True:
        sleep(1)
        if x>=9:
                x=0
                score.update(int(x))
        else:
                x=x+1
                score.update(int(x))
