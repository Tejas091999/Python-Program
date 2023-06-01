print("Welcome To Results")
name=input("What is your name: ")
roll_no=int(input("What is your roll no: "))
subjects=["Maths","Science","Social Science"]
marks_maths=int(input("enter your marks: "))
marks_science=int(input("enter your marks: "))    
marks_social=int(input("enter your marks: "))
if subjects=="Maths":
    if marks_maths<50:
            print("You need to study hard")
    else:
            print("You're good to goo! ")
elif subjects=="Science":
        if marks_science<50:
            print("You need to sttudy more hard")
        else:
            print("You are going good!! ")
elif subjects=="Social Science":
        if marks_social<50:
            print("This is also difficult subject")
        else:
            print("You are great!!")
elif marks_maths>50 and marks_science and marks_social>50:
    average=(marks_social+marks_maths+marks_science)/3
    if average > 45:
        print("You're passed!!")
    else:
        print("You have to really work hard.")
