name = input("What is your name? ")
print(f"welcome, {name} to the adventure!")

ans = input("You are on the road, it has come to an end and you can go left or right. which way will you like to go? ").lower()

if ans =="left":
    ans = input("You come to a river, you can walk around to or swim across? Type  walk around and swim to swim across: ")
    if ans =="swim":
        print("You swam across and were eaten by an alligator.")
    elif ans == "walk":
        print("You walked for many miles, ran out of water and you lost the name ")    
    else:
        print("Not a vaild option. You Lose.")


elif ans == "right":
    ans = input("You come to a bridge, it looks wobby, do you like to cross it or headback (cross or back)")
    if ans =="back":
        print("You go back and lose.")
    elif ans == "cross":
        ans = input("You coss the bridge and meet a stranger.Do you talk to them (yes/no): ")
    
        if ans =="yes":
            print("You talk to the stranger and gave you gold, you win!")
    
        elif ans == "no":
            print("you ignore the stranger and tehy are offended. you lose!")  
        
        else:
            print("invaild input")  
        

    
    
    else:
        print("Not a vaild option. You Lose.")
else:
    print("Not a vaild option. You Lose.")