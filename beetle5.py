import random

min = 1
max = 6

roll1 = "yes"
beet = []
beet2 = []
count = 0

flag = False
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
                flag = True
            else:
                beet.append("body")
                print("rolled 1,beetle body added")
                print(beet)
                flag = False

            if flag:
                if beet2[0] == "body":
                    print("already added")
                else:
                    beet2.append("body")
                    print("rolled 1,beetle body added")
                    print(beet2)
                    flag = False

            if beet[0] == "body":
                print("already added")

            else:
                beet2.append("body")
                print("rolled 1,beetle body added")
                print(beet2)
                continue

        if roll == 2 and len(beet) == 1:
            if "head" in beet:
                print("already there")
            else:
                beet.append("head")
                print("rolled 2,beetle head added")
                print(beet)
        elif roll == 2 and len(beet) == 0:
            print("No body is there")
        elif roll == 3 and len(beet) >= 2:
            if "antenna" in beet:
                print("antenna is already there")
            else:
                print("rolled 3,beetle antenna added")
                beet.append("antenna")
                print(beet)

        elif roll == 4 and len(beet) >= 2:
            if "eyes" in beet:
                print("eyes are already there")
            else:
                print("rolled 4,beetle eyes added")
                beet.append("eyes")
                print(beet)

        elif roll == 5 and len(beet) >= 2:
            if "mouth" in beet:
                print("mouth is already there")
            else:
                print("rolled 5,beetle mouth added")
                beet.append("mouth")
                print(beet)
        elif roll == 6 and len(beet) >= 2:
            if "legs" in beet:
                print("legs are already there")
            else:
                print("rolled 6,beetle legs are added")
                beet.append("legs")
                print(beet)
        if len(beet) == 6:
            print("YOU WON THE GAME IN", count, "TRIES")
            break
