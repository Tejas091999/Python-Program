import random
car_list=["BMW","MERCEDES","SUPRA"]
racer1=input("Which car would you like to drive1: ").upper()
racer2=random.choice(car_list)
print(racer1)
print(racer2)
if racer1==racer2:
    quit()
elif racer1!=racer2:
    if racer1=="BMW" and racer2=="MERCEDES":
        print("racer1 wins!!")
    elif racer1=="BMW" and racer2=="SUPRA":   
        print("racer2 wins!!")
    elif racer1=="MERCEDES" and racer2=="BMW":
        print("racer2 wins!!")
    elif racer1=="MERCEDES" and racer2=="SUPRA":
        print("racer2 wins!!")
    elif racer1=="SUPRA" and racer2=="BMW":
        print("racer1 wins")
    elif racer1=="SUPRA" and racer2=="MERCEDES":
        print("racer1 wins!!")
else:
    print("Please select car from list.")
