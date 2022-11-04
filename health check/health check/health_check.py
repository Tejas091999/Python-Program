import random
normal = 20
health = random.randint(0,100)
difficulty = random.randint(1,3)
total_health = health + normal
new_health = (total_health/difficulty)
print(health)
print(difficulty)
print(new_health)
if new_health >= 80:
    print("You're perfect!!")
elif 50 < new_health < 80:
    print("You can still do it better!!")
else:
    print("You need medication")
print("Get well soon!!")

