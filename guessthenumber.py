import random

max_of_range = input("Enter the top of range: ")

if max_of_range.isdigit():
    max_of_range = int(max_of_range)

    if max_of_range <=0:
        print("please enter a positive integer: ")
        quit()
else:
    print("Try again but this time, type a number!")
    quit()
random_number = random.randint(0,max_of_range)
guesses = 0
while True:
    guesses+=1
    user_guess = input("Enter the number that you want to guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Try again with a number!")
        continue

    if user_guess == random_number:
        print("you've got it right, it is",random_number)
        break
    elif user_guess < random_number:
        print("Try with a larger number")
    else:
        print("Try with a smaller number")

print("the total number of guesses taken is",guesses)