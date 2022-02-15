import random

def print_result(player, computer):
    
    print("You played: " + player)
    print("The computer played: " + computer)

def rock(computer):
    
    if computer == "paper":
        print("\nYou lose.")
    else:
        print("\nYou win!")

def paper(computer):
    
    if computer == "rock":
        print("\nYou win!")
    else:
        print("\nYou lose.")

def scissors(computer):
    
    if computer == "rock":
        print("\nYou lose.")
    else:
        print("You win!")

while True:
    player_choices = ["rock","paper","scissors"]
    computer_choices = ["rock","paper","scissors"]
    play_again = None

    computer = random.choice(computer_choices)

    player = None

    while player not in player_choices:
        player = input("Rock, Paper, Scissors?: ").lower()

    if player == computer:
        print_result(player, computer)
        print("\nTie!")

    elif player == "rock":
        print_result(player, computer)
        rock(computer)

    elif player == "paper":
        print_result(player, computer)
        paper(computer)

    elif player == "scissors":
        print_result(player, computer)
        scissors(computer)

    while play_again not in ("y","yes","no","n"):
        play_again = input("Play again? (y,yes,n,no): ").lower()

    if play_again == "y" or play_again == "yes":
        continue

    else:
        break
    
print("Bye, thanks for playing!")