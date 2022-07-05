import random

while True:
    options = ["rock","paper","scissors"]
    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("rock, paper or scisscors: ")

    if player == computer:
        print("computer's choice is", computer)
        print("player's choice is", player)
        print("It is a tie")
    elif player == "rock" :
        if computer == "scissors" :
            print("computer's choice is", computer)
            print("player's choice is", player)
            print("player wins")
        if computer == "paper":
            print("computer's choice is", computer)
            print("player's choice is", player)
            print("computer wins")
    elif player == "scissors":
        if computer == "rock":
            print("computer's choice is", computer)
            print("player's choice is", player)
            print("Computer wins")
        if computer == "paper":
            print("computer's choice is", computer)
            print("player's choice is", player)
            print("player wins")

    elif player == "paper":
        if computer == "rock":
            print("computer's choice is", computer)
            print("player's choice is", player)
            print("player wins")
        if computer == "scissors":
            print("computer's choice is", computer)
            print("player's choice is", player)
            print("computer wins")
    play_again = input("do you wanna play again? yes/no ")
    if play_again != "yes":
        break
print("bye")




