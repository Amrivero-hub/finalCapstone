#Capstone Project
#import math
#Financial calculators: an investment calculator and a home loan repayment calculator

#Ask the user to choose which calculation they want to do
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
calculation = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if calculation == "investment" or calculation == "bond":
#if the choice is investment, plese enter the following
    if calculation== "investment":
        p = float(input("Enter the amount of money that you are depositing: "))
        r = float(input("Enter the interest rate (as a percentage): "))
        t = float(input("Enter the number of years you plan on investing: "))
        interest = input("Enter 'simple' or 'compound' interest: ")

        if interest == "simple" or interest == "compound":
            # If the interest is simple, call the simple_interest function and print the answer
            if interest=="simple":
                simple_interest=p*(1+(r/100)*t)
                print (simple_interest)

               # If the interest is compound, call the compound_interest function and print the answer         
            elif interest == "compound":
                compound_interest=p*pow((1+r/100),t)
                print (compound_interest)

            else:
                print ("Invalid interest type. Please choose 'simple' or 'compound'.")

#if the user selects bond, please enter the following
    elif calculation == "bond":
        house_value = float(input("Enter the present value of the house: "))
        interest= float(input("Enter the annual interest rate (as a percentage): ")) / 100
        months = int(input("Enter the number of months you plan to take to repay the bond: "))
        interest_rate = interest/ 12
            
    # Calculate the monthly repayment amount
        monthly_repayment = (house_value * interest_rate) / (1 - (1 + interest_rate) ** (-months))
        print(f"Monthly Repayment Amount: {monthly_repayment:.2f}")

    else:
        print("Invalid choice. Please enter 'investment' or 'bond'.")