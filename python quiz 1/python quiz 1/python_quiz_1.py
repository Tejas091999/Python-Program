print("WELCOME TO THE QUIZ!!")
player = input("Do you want to play quiz: ").lower()
if player == "yes":
    print("okay let's goo!!")
elif player == "no":
    quit()
score = 0
question1 =  input("What does CPU stands for: ").lower()
if question1 == "central processing unit":
    print("You're correct!!")
    score+=1
else:
    print("You're wrong!!")
question2 = input("What does RAM stand for: ")
if question2 == "random access memory":
    print("You're correct!!")
    score+=1
else:
    print("You're wrong!!")
print(score)

