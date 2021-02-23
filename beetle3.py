import random

min = 1
max = 6

roll1 = ""
beet = []
beet2 = []
count = 0
flag = False

while True:

    roll1 = input("LETS ROLL THE DIE")
    if roll1 == "no" or roll1 == "n" or roll1 == "N":
        print("------GAME ENDS-------")
        break
    if roll1 == "yes" or roll1 == "y" or roll1 == 'Y':
        print("_______________________________________")
        print("Rolling the dices...")
        print("_______________________________________")
        roll = random.randint(min, max)
        count = count + 1
        print("________________________________________")
        print("Random value is....", roll)
        print("_________________________________________")
        if roll == 1:
            if len(beet) >= 0:
                if "body" in beet:
                    print("BODY ALREADY THERE")
                    flag = True
                else:
                    beet.append("body")
                    print("CONGRATS! BODY ADDED")
                    #print("congrats try next move!!!")
                    #print(beet)
                    flag = False
            if len(beet2) >= 0:
                if flag:
                    if "body" in beet2:
                        print("already added in 2nd list")
                        flag = True
                    else:

                        beet2.append("body")
                        print("CONGRATS! BODY ADDED TO 2ND LIST")
                        print("beet2:", beet2)
                        flag = False
                        continue
        if roll == 2:
            if len(beet) >= 1:
                if "head" in beet:
                    print("head already there")
                    flag = True
                else:
                    beet.append("head")
                    print("CONGRATS! HEAD ADDED")
                    #print(beet)
                    flag = False
            if len(beet2) >= 1:
                if flag:
                    if "head" in beet2:
                        print("already added")
                        flag = True
                    else:
                        beet2.append("head")
                        print("CONGRATS! ADDED HEAD TO 2ND LIST")
                        print("beet2:", beet2)
                        flag = False
                        continue
        elif roll == 2 and len(beet) == 0:
            print("No body is there")

        if roll == 3:
            if len(beet) <= 1:
                print("BAD LUCK!! :(  TRY AGAIN")
            if len(beet) >= 2:
                if "antenna" in beet:
                    print("antenna is already there")
                    flag = True
                else:

                    beet.append("antenna")
                    print("CONGRATS! ADDED ANTENNA")
                    #print(beet)
                    flag = False
            if len(beet2) >= 2:
                if flag:
                    if "antenna" in beet2:
                        print("antenna already added")
                        flag = True
                    else:
                        beet2.append("antenna")
                        print("CONGRATS! ANTENNA ADDED TO 2ND LIST")
                        print("beet2:", beet2)
                        flag = False
                        continue
        elif roll == 4:
            if len(beet) <= 1:
                print("BAD LUCK! :( TRY AGAIN!")
            if len(beet) >= 2:
                if "eyes" in beet:
                    print("eyes are already there")
                    flag = True
                else:

                    beet.append("eyes")
                    print("CONGRATS! ADDED EYES")
                    #print(beet)
                    flag = False
                if len(beet2) >= 2:
                    if flag:
                        if "eyes" in beet2:
                            print("already added")
                            flag = True
                        else:

                            beet2.append("eyes")
                            print("CONGRATS! EYES ADDED TO 2ND LIST")
                            print("beet2:", beet2)
                            flag = False
                            continue

        elif roll == 5:
            if len(beet) <= 1:
                print("BAD LUCK! :( TRY AGAIN!")
            if len(beet) >= 2:
                if "mouth" in beet:
                    print("mouth is already there")
                    flag = True
                else:

                    beet.append("mouth")
                    print("CONGRATS! ADDED MOUTH")
                    #print(beet)
                    flag = False
            if len(beet2) >= 2:
                if flag:
                    if "mouth" in beet2:
                        print("already added")
                        flag = True
                    else:
                        print("CONGRATS! MOUTH ADDED TO 2ND LIST")
                        beet2.append("mouth")
                        print("beet2:", beet2)
                        flag = False
                        continue

        elif roll == 6:
            if len(beet) <= 1:
                print("BAD LUCK! :( TRY AGAIN!")
            if len(beet) >= 2:
                if "legs" in beet:
                    print("legs are already there")
                    flag = True
                else:

                    beet.append("legs")
                    print("CONGRATS! ADDED LEGS")
                    #print(beet)
                    flag = False
            if len(beet2) >= 2:
                if flag:
                    if "legs" in beet2:
                        print("already added")
                        flag = True
                    else:
                        beet2.append("legs")
                        print("CONGRATS! LEGS ADDED TO 2ND LIST")
                        print("beet2:", beet2)
                        flag = False
                        continue

        # else:
        # print("bad luck")
        print("---------------RESUlTS--------------")
        print("beet :", beet)
        print("beet2 :", beet2)
        print("_____________________________________")
        if len(beet) == 6 and len(beet2) == 6:
            print("YOU WON THE GAME IN", count, "TRIES")
            break
