import math

# I have lower cased the input below, for my program to recognise all valid entires:
calculation = (input("""Which calculations would you like to perfrom? \n\nInvestment - to calculate the amount of interest you'll earn on your investment \nBond - to calculate the amount you'll have to pay on a home loan\n
Enter either "investment" or "bond" from the menu above to proceed: """))
calculation = calculation.lower()

# I have created a nested statememnt to allow the selection of "simple" or "compound" interest within the investment if statement.
# I have also applied an error message below incase the user inputs anything besides "simple" or "compound".
if calculation == "investment":
    amount = float(input("How much will you be depositing? "))
    interest_rate = float(input("What is the interest rate? "))
    interest_rate = interest_rate / 100
    years = float(input("In years, how long are you planning on investing? "))
    interest_type = input("Would you like to opt for 'simple' or 'compound' interest? ")
    interest_type = interest_type.lower()
    if interest_type == "simple":
        simple_interest = amount * (1 + (interest_rate) * years)
        print(f"The simple interest you will accumilate in addition to your investment is: £{simple_interest:.2f}")
    elif interest_type == "compound":
        compound_interest = amount * math.pow((1 + interest_rate), years)
        print(f"The compound interest you will accumilate in addition to your investment is: £{compound_interest:.2f}")
    else:
        print("You have not entered the correct details, please enter either 'simple' or 'compound'.")

# A final error message was placed below incase all else fails as the user did not enter "investment" or "bond".
elif calculation == "bond":
    house_value = float(input("Please enter the present value of the house: "))
    interest_rate = float(input("What is the interest rate? "))
    interest_rate = (interest_rate / 100) /12
    months = int(input("In months, how long are you planning on investing? "))
    repayment = (interest_rate * house_value) / (1- (1 + interest_rate) ** (-1 * months))
    print(f"The amount you will need to repay each month is: £{repayment:.2f}")
else:
    print("You have entered the incorrect details, please enter either 'investment' or 'bond'.")


