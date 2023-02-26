print("Welcome to the practise")
name=input("What is your name: ")
info=[]
info.append(name)
while True:
    age=input("What is your age:")
    if age.isdigit():
        print("You're good to go..")
        info.append(age)
        break
    else:
        print("Age is always a number")
while True:
    gender=input("What is your gender:")
    if gender=="male":
        print("You're Handsome")
        info.append(gender)
        break
    elif gender=="female":
        print("You're Beautiful")
        info.append(gender)
        break
    else:
        print("Gender can be male or female")
while True:
    contact=input("What is your contact:")
    if contact.isdigit():
        print("Go ahead and submit it")
        if len(contact)==10:
            print("You're good to goo..")
            info.append(contact)
            break
        else:
            print("Please enter a valid 10 digit number")
    else:
        print("Contact number is always a digits..")
print(info)