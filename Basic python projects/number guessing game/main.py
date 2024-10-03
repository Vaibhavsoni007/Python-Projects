import random   # number guessing game

lowest_number = 1
highest_number = 10
count = 1

answer = random.randint(lowest_number, highest_number)
your_number = int(input(f"Enter a guessed number between {lowest_number} and {highest_number}: "))

def continues():
    global count  # Make count global to modify it inside the function
    global your_number  # Make your_number global to modify it inside the loop
    
    while True:
        if your_number == answer:
            print(f"Yes, {answer} is the number! You guessed it in {count} tries.")
            break
        else:
            print("Wrong guess, try again.")
            count += 1
            your_number = int(input(f"Enter a guessed number between {lowest_number} and {highest_number}: "))

# Check if the guessed number is within the range
if not (lowest_number <= your_number <= highest_number):
    print(f"Please enter a number between {lowest_number} and {highest_number}.")
else:
    # Loop until the correct guess is made
    continues()
