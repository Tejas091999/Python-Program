user=input("Do you want to take this survey: ")
while True:
    if user=="yes":
        name=input("What is your name: ")
        age=int(input("What is your age: "))
        gender=input("What is your gender: ")
        city=input("What is your location: ")
        name_list=[]
        age_list=[]
        gender_list=[]
        city_list=[]
        name_list.append(name)
        age_list.append(age)
        gender_list.append(gender)
        city_list.append(city)
        print(name_list)
        print(age_list)
        print(gender_list)
        print(city_list)
        print("Thank you for taking this survey")
    elif user=="no":
        quit