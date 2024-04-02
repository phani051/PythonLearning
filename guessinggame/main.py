import random
from art import logo

print (logo)
answer = random.randrange(0,100)
print(answer)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
def play_game(attempts):
    attempts = int(attempts)
    status = [answer]
    game_continue = True
    while game_continue and attempts >= 1:
        print(f"You have {attempts} attempts")
        user_guess = input("make a guess: ")
        if int(user_guess) == answer:
            game_continue = False
            print("You won")
            break
        else:
            attempts -= 1
            if int(user_guess) > status[-1]:
                print("Too High")
            elif int(user_guess) < status[-1]:
                print("Too low")
    else:
        print("You lost")

if difficulty == 'easy':
    play_game(10)           
    
elif difficulty == 'hard':
    play_game(5)
    

    