import random   # rock paper scissors game

# Generate computer's choice
computer_choice = random.randint(1, 3)

# Get user's choice
user_choice = int(input("""Enter a number: 
1 for rock
2 for paper
3 for scissors
"""))

# Display choices
choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
print(f"Computer chose: {choices[computer_choice]}")
print(f"You chose: {choices[user_choice]}")

# Determine the result
if computer_choice == user_choice:
    print("It's a tie!")
elif (computer_choice == 1 and user_choice == 3) or \
     (computer_choice == 2 and user_choice == 1) or \
     (computer_choice == 3 and user_choice == 2):
    print("Computer wins!")
else:
    print("You win!")
