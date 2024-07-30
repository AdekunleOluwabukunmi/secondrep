import random
userwin = 0
comwin = 0
option = ["rock","paper","scissors"]

while True:
    userinput = input("Type: Rock/paper/scissors or q to quit: ").lower()
    if userinput == "q":
        break
    if  userinput not in option:
        continue
    ran_num = random.randint(0,2)
    com_pic = option[ran_num]
    print(f"computer picked {com_pic}. ")
    if userinput == "rock" and com_pic =="scissor":
        print("you win!")
        userwin += 1
    elif userinput == "paper" and com_pic =="rock":
        print("you win!")
        userwin += 1
    elif userinput == "scissor" and com_pic =="paper":
        print("you win!")
        userwin += 1
    else:
        print("you lose")
        comwin += 1
print(f"you won {userwin} times")
print(f"computer won {comwin} times")
print("Goodbye!")