print("SIMPLE COMPOUND INTEREST CALCULATOR")
principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate: "))
time = int(input("Enter Number of year: "))

for year in range(1, time):
    amount = principal * (1 + rate) ** time
    print(f'{time:>2} Your interest is: {amount:>10.2f}')
