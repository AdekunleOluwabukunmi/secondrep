# name = input("welcome to my project learning game, What is your name?: ")
# print(f'welcome {name} to my game')
# task1 = input("will you like to run or jump (run/jump): ").lower()
# if task1 == "run":
#     print("you ran and got to drink what: ")
# elif task1 == 'jump':
#     print('you jump and need to raise your legs')
# else:
#     print('wrong input you lose!')


import logging
write = ['cat', 'Dog', 'goat']
for w in write:
    print(len(w))

logging.warning("cancel it!")


def sss(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

sf = sss(418)
print(sf)

def eee(name):
    print(f"john {name}")
eee("tim")

for i in range(4):
    print(4/2)

year = 2016
event = 'Referendum'
f'Results of the {year} {event}'

s= "hello world"

print(str(s))

class student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
        
stu = student("jim", "law", 3.1)

print(stu.gpa)

import random
print("Welcome to my game")
p = input("Do you want to play (Yes/No)? ").lower()
if p == "yes":
    print("let Go!")
elif p != "no":
    print("wrong input.Try again late")
    quit()
else:
    print("Thanks for trying my game")
    quit()
option = ["up", "middle", "down"]
g = input("UP or DOWN? ").lower()
randnum = random.randint(0, 2)
comp = option[randnum]
if g in option:
     print("start")
if g == "up" and comp == "up":
    print(f"You win the bottle spin {comp}")
elif g == "down" and comp == "down":
    print(f"You win! the bottle spin {comp}")   
else:
        print(f"You Lose, The bottle spin to {comp}")



pas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234!£$%^&*?~/#¬_-"
passrad = random.randint(0, 8)
j = pas[passrad]
print(f"this is your password: {j} ")
#pas.random() 

