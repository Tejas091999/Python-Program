import random
def roll_dice():
    user = input("Do you want roll dice: ").lower()
    if user == "yes":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        result = dice1 + dice2
        print(dice1)
        print(dice2)
        print(result)
        if result < 6 :
            print("You can do it better!!")
        else:
            print("You're going places!!")
    else:
        quit()
roll_dice()