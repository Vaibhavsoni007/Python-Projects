foods = []
quantities = []
prices = []
total = 0

# Collecting data from the user
while True:
    food = input("Enter the food item you want (or 'q' to quit): ")
    if food.lower() == 'q':
        break
    else:
        try:
            quantity = int(input(f"Enter the quantity of {food}: "))
            price = float(input(f"Enter the price of one {food}: ₹ "))
            foods.append(food)
            quantities.append(quantity)
            prices.append(price * quantity)  # Storing the total price for the given quantity
        except ValueError:
            print("Please enter valid quantity and price.")

# Displaying the formatted output
print("\nFood Menu:")
print("-" * 50)  # Separator line
print(f"{'Food Item':<20} {'Quantity':<10} {'Price (₹)':<10}")
print("-" * 50)

# Printing each food item with its quantity and total price
for food, quantity, price in zip(foods, quantities, prices):
    print(f"{food:<20} {quantity:<10} ₹{price:.2f}")

# Calculating the total
total = sum(prices)

print("-" * 50)
print(f"{'Total':<30} ₹{total:.2f}")
print(f"\n₹{total:.2f} is the total amount of bill you have to pay.")
