import random

min = 1
max = 6

roll_again = "yes"
flag = True

while True:
    body = False
    head = False
    antenna = False
    eye = False
    mouth = False
    leg = False
    roll_again = input("Lets roll the die")
    if roll_again == "yes" or roll_again == "y":
        print("Rolling the dices...")
        roll = random.randint(min, max)
        print("Random value is....", roll)

        if roll == 1 and not body:

            body = True
            print("roll 1,beetle body added")
            continue
        else:
            print("bad luck!!,roll again")
            pass

        if roll == 2 and not body:
            print("roll again,want to add beetle body first")



