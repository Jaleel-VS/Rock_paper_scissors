#Rock paper scissors game
import random

user_selection = input("Rock (R), Paper (P) or Scissors (S): \n")
computer_selection = random.choice(["R", "P", "S"])


while user_selection != ("R" or "S" or "P"):
    print("Please make a valid selection!!")
    user_selection = input("Rock (R), Paper (P) or Scissors (S): \n")


print(f"Your choice was {user_selection}")
print(f"The ai's choice was {computer_selection}")
print("_________________________________")
if user_selection == computer_selection:
    print("Match is a tie")
else:
    if user_selection == "S" and computer_selection == "P":
        print("You won!")
    if user_selection == "P" and computer_selection == "S":
        print("You lost :(")
    if user_selection == "R" and computer_selection == "S":
        print("You win!")
    if user_selection == "R" and computer_selection == "P":
        print("You lost :(")
    if user_selection == "S" and computer_selection == "R":
        print("You lost :(")
    if user_selection == "P" and computer_selection == "R":
        print("You won!")

