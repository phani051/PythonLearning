from art import logo
from art import vs
from game_data import data
import random
import os


alist = list(random.choice(data).values())
blist = list(random.choice(data).values())
while alist == blist:
    blist = list(random.choice(data).values())


def win_check(user_answer):
    if alist[1] > blist[1]:
        return user_answer == 'a'
    else:
        return user_answer == 'b'

print(logo)
def game():
    
    global alist
    global blist
    alist = blist
    blist = list(random.choice(data).values())
    print(f"Compare A: {alist[0]},{alist[1]} {alist[2]} from {alist[3]}  ")
    print(vs)
    print(f"Compare B: {blist[0]},{blist[1]} {blist[2]}, {blist[3]}")
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    return win_check(user_answer)


result = game()
score = 1
if result == False:
    print("Lost in First try!!")
else:
    while result:
        os.system('cls')
        print(logo)
        print(f"You are right! Current score is {score}")
        result = game()
        if result == True:
            print('Correct')
            score += 1
        else:
            print('You lost!')
    else:
        print(f"Sorry final score is {score}")
