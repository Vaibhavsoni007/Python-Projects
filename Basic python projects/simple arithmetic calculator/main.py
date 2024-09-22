# simple arithmetic calculator 
def calculator():
    op = str(input("""enter the operator :
    +     for addition
    -     for subtraction
    *     for multiplication
    /     for division"""))

    if(op == '+'):
        print(f"the addition of {num1} and {num2} is : {num1+num2:.2f}")
    elif(op == '-'):
        print(f"the subtraction of {num1} and {num2} is : {num1-num2:.2f}")
    elif(op == '*'):
        print(f"the multiplication of {num1} and {num2} is : {num1*num2:.2f}")
    elif(op == '/'):
        print(f"the division of {num1} and {num2} is : {(num1/num2):.2f}")

num1 = float(input("enter number 1 : "))
num2 = float(input("enter number 2 : "))
calculator()
