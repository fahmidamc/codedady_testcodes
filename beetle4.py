import random

throws = 0
sixes = 0
fives = 0
fours = 0
threes = 0
twos = 0
ones = 0
reach = 50
total = 0
question = input ("Play Yes/No")
if question == "Yes":
    question = True
else:
    question = False
while total < reach and question:
    roll = random.randint(1, 6)
    throws += 1
    total += roll
    if roll == 6:
        sixes += 1
    elif roll == 5:
        fives += 1
    elif roll == 4:
        fours += 1
    elif roll == 3:
        threes += 1
    elif roll == 2:
        twos += 1
    elif roll == 1:
        ones += 1
    else:
        print("Try again later")
if question:
    print("Total throws : ", throws)
    print("Total : ", total)
    print("Total 6's : ", sixes)
    print("Total 5's : ", fives)
    print("Total 4's : ", fours)
    print("Total 3's : ", threes)
    print("Total 2's : ", twos)
    print("Total 1's : ", ones)
else:
    print("Your Loss!")