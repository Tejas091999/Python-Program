print("WELCOME TO LOGIN CHECKUP!!")
mylist = ["Ram","Rahul","Shaam","Tejas"]
name = input("What is your name: ")
while True:
    if name in mylist:
        print("Welcome to the Website!!")
        user = input("Do you want to remove?")
        if user == "yes":
            print("You're name is removed!")
            mylist.remove(name)
            break
        elif user == "no":
            print("NOT removed!!")
            break

    else:
        user = input("Do you want to add your name? ")
        if user == "yes":
            mylist.append(name)
            print("You're Added!!")
            print("Welcome to Website.")
            break
        elif user == "no":
            print("Comeback later.")
            break
print("Thank you for visiting website!")
print(mylist)