import math
def compund_interest_calculator():
    principle = float(input("enter the principle amount : "))
    rate = float(input("enter the interest rate : "))
    time = float(input("enter the time : "))

    if(principle==0 or rate==0 or time==0):
        print("None of the value of principle , rate or time can be zero or negative . please write the values again")

    compound_interest = principle * pow((1 + rate/100),time)
    print(f"the compound interest of the {principle}₹ amount is {compound_interest:.2f}₹")

compund_interest_calculator()
    