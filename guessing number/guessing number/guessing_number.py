from pickle import TRUE
import random
top_of_range = input("Enter the number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range < 0:
        print("Please neter the number gretaer than 0")
        quit()
else:
    print("Please enter the number next time")
random_number = random.randint(0,top_of_range)
while TRUE:
    user = input("Enter the number: ")
    if user.isdigit():
        user = int(user)
    else:
        print("Please neter the number next time")
        continue
    if user == random_number:
        print("You guessed it right!!")
    else:
        print("Please try again! ")