import random
tpe = input("Type a number: ")

if tpe.isdigit():
    tpe = int(tpe)

    if tpe <= 0:
        print("please type a number larger than 0 next time.")
        quit()
else:
    print("please type a number next time")
    quit()

r = random.randint(1, tpe)
g = 0
while True:

    g += 1
    ug = input("Make a guess: ")

    if ug.isdigit():
        ug = int(ug)

    else:
        print("please type a number next time")
        continue
    if ug == r:
        print("you got it")
        break
    elif ug > r:
            print("you are above the number")
    else:
        print("You are below the number")
print(f'you got it in {g} guesses')
