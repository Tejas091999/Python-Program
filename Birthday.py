import calendar
def predict_birth_day(year, month):
    weekday = calendar.weekday(year, month, 1)
    day_name = calendar.day_name[weekday]
    return day_name

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month (1-12): "))

day_of_birth = predict_birth_day(birth_year, birth_month)
print("You were born on a", day_of_birth + ".")
