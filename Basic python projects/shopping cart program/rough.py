def main():
    # Initialize an empty list to store food items and prices
    food_items = []
    prices = []

    # Get the number of food items from the user
    num_items = int(input("How many food items do you want to enter? "))

    # Collect food items and prices from the user
    for i in range(1, num_items + 1):
        food = input(f"Enter food item {i}: ")
        price = float(input(f"Enter price for {food}: "))  # Assuming prices are in decimal format
        food_items.append(food)
        prices.append(price)

    # Print the formatted output
    print("\nFood Menu:")
    print("-" * 30)  # Separator line

    for food, price in zip(food_items, prices):
        print(f"{food:<20} {price:.2f}")

if __name__ == "__main__":
    main()
