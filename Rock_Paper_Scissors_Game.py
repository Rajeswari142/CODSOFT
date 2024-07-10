# Python program for Rock-Paper-Scissors Game.

import random

choices = ['rock', 'paper', 'scissors']

print("Welcome to Rock, Paper, Scissors Game! ")
print("You will be playing against the computer. ")
print("The rules are simple: ")
print("Rock beats Scissors, Scissors beats Paper, Paper beats Rock. ")
print("Good luck! ")

user_wins = 0
computer_wins = 0
draws = 0

while True:
    user_choice = input("Choose Rock, or Paper, or Scissors: ").lower()
    if user_choice == 'quit':
          break
    if user_choice not in choices:
          print("Invalid choice. Please try again. ")
          continue
    computer_choice = random.choice(choices)
    print(f"You choose: {user_choice}" )
    print(f"Computer choose: {computer_choice}" )

    if user_choice == computer_choice:
            print("It's a tie! ")
            draws += 1
    elif(user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'scissors' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'rock'): 
            print("You win! ")
            user_wins += 1
    else:
            print("You lose! ")
            computer_wins += 1

            print (f"You: {user_wins} - Computer: {computer_wins} - Draws: {draws}")

            play_again = input("Do you want to play another round?  (yes/no): ").lower()
            if play_again != 'yes':
                break

            print("Game Over! Thanks for playing! ")
            print(f"Final score: You - {user_wins}, Computer - {computer_wins}, Draws - {draws}")
             
            if user_wins > computer_wins:
                print("Overall Winner: You! ")
            elif user_wins < computer_wins:
                print("Overall Winner: Computer! ")
            else:
                print("Overall Winner: It's a tie! ")
