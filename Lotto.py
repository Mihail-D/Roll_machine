import time
import random

arr = [x for x in range(1, 46)]
bets = []
ball = 0

t_end = time.time() + 30

while ball < 6:
    while time.time() < t_end:
        random.shuffle(arr)
        roll = random.choice(arr)

    bets.append(roll)
    arr.remove(roll)
    ball += 1
    t_end = time.time() + 30
    print("Шар", ball, " - ", roll)

bets.sort()
print(bets)
