def Calculate_intrest(principal, rate, time):
    Simple_Interest = (principal * rate * time) / 100
    return Simple_Interest


result = Calculate_intrest(1000, 5, 2)
print(f"The simple interest for a principal amount of ${1000:,.2f} \
                at an interest rate of {5}% over a period of \
                {2} years is: ${result:,.2f}")