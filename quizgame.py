#this is a quiz game

print("Welcome to my computer quiz game")
#just made a comment for github purpose
playing = input("Do you want to play the game? ")
if playing.lower() != "yes":
    quit()
else:
    print("welcome, let's play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower()=="central processing unit":
    print("Correct")
    score+=1
else:
    print("you are wrong")

answer = input("What does GPU stand for? ")
if answer.lower()=="graphical processing unit":
    print("Correct")
    score+=1
else:
    print("you are wrong")

answer = input("What does RAM stand for? ")
if answer.lower()=="random access memory":
    print("Correct")
    score+=1
else:
    print("you are wrong")

print("you got a score of "+ str(score) + " out of 3")

