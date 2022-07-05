def invest(amount, rate, years):
    simple_interest = (amount * rate * years) / 100
    return simple_interest


principal = float(input("Enter Amount: "))
rate = float(input("Enter Rate: "))
year = int(input("Enter year: "))

invest(principal, rate, year)
for year in range(1, year):
    year = year + 1
    for principal in range(1, int(principal)):
        principal = principal + 1
        print(f" Years {year}: ${principal:2f}")