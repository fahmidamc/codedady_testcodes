import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(min, max))
    print(random.randint(min, max))

    roll_again = input("Roll the dices again?")

    no = random.randint(1, 6)

if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
if no == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
if no == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")

if no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
if no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
if no == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")

        import random

        min = 1
        max = 6

        roll_again = "yes"

        while True:
                if roll_again == "yes" or roll_again == "y":
                        print("Rolling the dices...")
                        value = random.randint(min, max)
                        print("Random value is....", value)
                        if value == 1:
                                print("BEETLE BODY ADDED!")

                                if value == 2:
                                        print("BEETLE HEAD ADDED!")

                                        if value == 3:
                                                print("BEETLE ANTENNA ADDED!")


                elif roll_again == "no":
                        print("idle dice")
                break



