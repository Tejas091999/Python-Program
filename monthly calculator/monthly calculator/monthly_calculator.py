


print("Welcome to monthly Calculator!")
def main():
    principal = int(input("Enter the loan taken: "))
    apr = float(input("Enter the annual interest: "))
    years = int(input("Enter the number of years: "))
    monthly_interest_rates = apr/1200
    months = years/12
    monthly_payments = principal*monthly_interest_rates/(1-(1+monthly_interest_rates)**(-months))
    print(monthly_payments)
main()