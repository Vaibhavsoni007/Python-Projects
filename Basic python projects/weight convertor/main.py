def Weight_Calculator():
    weight = float(input("Enter your weight here :"))
    unit = str(input("Enter your unit here that is K or P (kilogram or pounds ):"))

    if(unit == 'K'):
        weight = weight * 2.205
        unit = "P"
      
        
    elif(unit == 'P'):
        weight = weight / 2.205
        unit = "K"
       
    print(f"{weight:.2f} {unit} is the weight ")

     
Weight_Calculator()  