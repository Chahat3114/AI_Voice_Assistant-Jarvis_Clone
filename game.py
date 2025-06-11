import random
options = ["rock", "paper", "scissors"]
user_input = input("Enter your choice: ").lower()
computer = random.choice(options)

print("You choose:", user_input)
print("Computer choose:", computer)

if user_input == computer:
    print("It is tie!")

elif user_input == "rock":
    if computer == "scissors":
        print("You win!")
    else:
        print("Computer wins!")

elif user_input == "paper":
    if computer == "rock":
        print("You win!")
    else:
        print("Computer wins!")

elif user_input == "scissors":
    if computer == "paper":
        print("You win!")
    else:
        print("Computer wins!")

else:
    print("Invalid output !")