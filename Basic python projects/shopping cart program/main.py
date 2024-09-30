foods = []
prices = []
total = 0

while True:
    food = str(input("Enter the food you want : "))
    if (food.lower() == 'q'):
        break
    else:
        price = float(input(f"enter the price of a {food}: ₹ "))
        foods.append(food)
        prices.append(price)

print("\nFood Menu:")
print("-" * 30)  # Separator line

for food, price in zip(foods, prices):
        print(f"{food:<20} {price:.2f}")

for price in prices:
    total = total + price

print("-" * 30)  # Separator line
print(f"total amount is : {total}")

print(f"\n{total}₹ is the total amount of bill you have to pay : ")