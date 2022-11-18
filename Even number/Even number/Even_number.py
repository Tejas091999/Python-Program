print("WELCOME TO CHECK THE EVEN NUMBER")
user = input("Do you want to check the number:(yes/no)")
if user == "yes":
    num = int(input("Please enter your number: "))
    if num % 2 == 0:
        print("The number is even!")
    else:
        print("The number is not even!")
elif user == "no":
    exit()