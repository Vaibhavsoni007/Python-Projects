# temperature converter 
def temperature_converter():
    temperature = float(input("Enter the temperature : "))
    unit = str(input("Enter the unit here K for kelvin , F for fahrenheit and C for celsius : "))

    if(unit == "K"):
        K = temperature
        C = K - 273.15
        F = ((9/5)*C)+32

        print(f"{C:.2f}°C")
        print(f"{F:.2f}°F")

    elif(unit == 'C'):
        C = temperature
        K = C + 273.15
        F = ((9/5)*C)+32

        print(f"{K:.2f}°K")
        print(f"{F:.2f}°F")

    elif(unit == 'F'):
        F = temperature
        C = (F-32)*(5/9)
        K = C + 273.15

        print(f"{K:.2f}°K")
        print(f"{C:.2f}°C")

temperature_converter()      # calling temperature_converter function 

