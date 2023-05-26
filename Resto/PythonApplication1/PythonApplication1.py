print("Welcome To Resto")
customer=input("Do you want to eat here: ")
total_balance=int(input("How much money do you have: "))
co_price=450
in_price=500
it_price=500
th_price=650
menu=["Conitental","Indian","Italian","Thai"]
item=input("What do you want to eat: ")
mylist=[]
while True:
    if customer=="yes":
       if item=="Conitental":
                balance=total_balance-co_price
                print(balance)
                mylist.append(item)
       elif item=="Indian":
                balance=total_balance-in_price
                print(balance)
                mylist.append(item)
       elif item=="Italian":
                balance=total_balance-it_price
                print(balance)
                mylist.append(item)
       elif item=="Thai":
                balance=total_balance-th_price
                print(balance)
                mylist.append(item)
    user=input("Do you want to add another item: ")
    if user=="yes":
        print("Tejas")
    elif user=="no":
        print(balance)
        break
    elif customer=="no":
        print("Please do visit again!!!")
        break
