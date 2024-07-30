#Quiz game
print("Welcome to my quiz game")
q = input("Do you want to play?(Yes,No) ")
if q.lower() == 'yes':
    print("Welcome to the game")
else:
    quit()
score = 0
ans = input("What do Bukunmi mean? ").lower() 
if ans == "bless me":
    print("correct!")
    score += 1
else:
    print("incorrect")
    
ans = input("what does PSU stand for? ").lower() 
if ans == "power supply":
    print("correct!")
    score += 1
else:
    print("incorrect")
    

ans = input("meaning of CPU? ").lower() 
if ans == "computer processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect")
    
ans = input("meaning of USB? ").lower() 
if ans == "universal serial bus":
    print("correct!")
    score += 1
else:
    print("incorrect")

print(f"You got {score} marks" )

# second project

import random

a = input("Input a number: ")
if a.isdigit():
    a = int(a)
    if a <= 0:
        print("type a number greater than 0 next time")
        quit()
else:
    print("Print a number next time")

rand = random.randint(0,a)

while True:
    user = input("Make a guess: ")
    if user.isdigit():
        user = int(user)
    else:
        print("Print a number next time")
        continue
    if user == rand:
        print("You got it")
        break
    else:
        if user > rand:
            print("You are above the number")
        else:
            print("you are below the number")