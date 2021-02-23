import random

min = 1
max = 6

roll_again = "yes"
beet = []
count = 0

while True:
    roll_again = input("Lets roll the die")
    if roll_again == "yes" or roll_again == "y" or roll_again == 'Y':
        print("Rolling the dices...")
        roll = random.randint(min, max)
        count = count + 1
        print("Random value is....", roll)

        if roll == 1 and len(beet) == 0:
            if "body" in beet:
                print("already added")

            else:
                beet.append("body")
                print("rolled 1,beetle body added")
                print(beet)

                while True:
                    r = input("let us make second roll")
                    if r == "yes" or r == 'y' or r == 'Y':
                        roll2 = random.randint(min, max)
                        print("Random value is....", roll2)
                        if roll2 == roll:
                            print("body added to beet")
                            beet.append("body")
                            print(beet)
                        else:
                            print("try again")
                        if len(beet) == 2:
                            break
        if roll == 2 and len(beet) >= 2:
            if "head" in beet:
                print("already there")
            else:
                beet.append("head")
                print("rolled 2,beetle head added")
                print(beet)
                while True:
                    r = input("let us make second roll")
                    if r == "yes" or r == 'y' or r == 'Y':
                        roll2 = random.randint(min, max)
                        print("Random value of second roll....", roll2)
                        if roll2 == roll:
                            print("head added to beet")
                            beet.append("head")
                            print(beet)
                        else:
                            print("try again")
                        if len(beet) == 4:
                            break
        elif roll == 2 and len(beet) == 0:
            print("No body is there")
        elif roll == 3 and len(beet) >= 4:
            if "antenna" in beet:
                print("antenna is already there")
            else:
                print("rolled 3,beetle antenna added")
                beet.append("antenna")
                print(beet)
                while True:
                    r = input("let us make second roll")
                    if r == "yes" or r == 'y' or r == 'Y':
                        roll2 = random.randint(min, max)
                        print("Random value of second roll....", roll2)
                        if roll2 == roll:
                            print("antenna added to beet")
                            beet.append("antenna")
                            print(beet)
                        else:
                            print("try again")
                        if len(beet):
                            break
        elif roll == 4 and len(beet) >= 4:
            if "eyes" in beet:
                print("eyes are already there")
            else:
                print("rolled 4,beetle eyes added")
                beet.append("eyes")
                print(beet)
                while True:
                    r = input("let us make second roll")
                    if r == "yes" or r == 'y' or r == 'Y':
                        roll2 = random.randint(min, max)
                        print("Random value of second roll....", roll2)
                        if roll2 == roll:
                            print(" eyes added to beet")
                            beet.append("eyes")
                            print(beet)

                        else:
                            print("try again")
                        if len(beet) :
                            break
        elif roll == 5 and len(beet) >= 4:
            if "mouth" in beet:
                print("mouth is already there")
            else:
                print("rolled 5,beetle mouth added")
                beet.append("mouth")
                print(beet)
                while True:
                    r = input("let us make second roll")
                    if r == "yes" or r == 'y' or r == 'Y':
                        roll2 = random.randint(min, max)
                        print("Random value of second roll....", roll2)
                        if roll2 == roll:
                            print("mouth added to beet")
                            beet.append("mouth")
                            print(beet)
                        else:
                            print("try again")
                        if len(beet) <= 12 :
                            break
        elif roll == 6 and len(beet) >= 4:
            if "legs" in beet:
                print("legs are already there")
            else:
                print("rolled 6,beetle legs are added")
                beet.append("legs")
                print(beet)
                while True:
                    r = input("let us make second roll")
                    if r == "yes" or r == 'y' or r == 'Y':
                        roll2 = random.randint(min, max)
                        print("Random value of second roll....", roll2)
                        if roll2 == roll:
                            print("legs added to beet")
                            beet.append("legs")
                            print(beet)

                        else:
                            print("try again")
                        if len(beet) <= 12:
                            break

    else:
        print("bad luck")

        if len(beet) == 6:
            print("YOU WON THE GAME IN", count, "TRIES")
            break
