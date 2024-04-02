import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
randomout = random.randint(0,2)
compchoice = options[randomout]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if user_choice >=3 or user_choice < 0:
    print("Invalid value, you lost!")
else:
    print (options[user_choice])
    print("Computer Choice: ")
    print(compchoice)
 
    
    if user_choice == randomout:
        print("Draw")
    elif user_choice == 0 and randomout == 1:
        print("You loos")
    elif user_choice == 1 and randomout == 2:
        print("You loos")
    elif user_choice == 2 and randomout == 0:
        print("You loos")
    else:
        print ("You win")





