'''Import random module
create a card deck
give user 2 random cards and reveal
give delar 2 random cards and only reveal one card.
Ask user to HIT or STAND
----------------
If STAND, reveal dealer cards, if dealer cards are less than 17 add the cards
If dealer card value is higher 21 and BUST and if dealer cards are higher thn 17 and higher than user, dealer wins.
If the dealer cards is beween 17 and 21 but lower than the user, user wins.
-------------

If HIT, add one more random card to user and check for value and if higher than 21 BUST if not ask for HIT or STAND

'''
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = random.sample(cards, 2)
dealer_cards = random.sample(cards, 2)

# print (f"You Won! \nUser cards:{user_cards}, {sum(user_cards)}\nDealer cards:{dealer_cards}, {sum(dealer_cards)}")

def win_check():
    if sum(user_cards) > sum(dealer_cards) and sum(user_cards) < 21:
        return True
    elif sum(dealer_cards) > 21:
        return True
    elif sum(dealer_cards) > sum(user_cards) and sum(dealer_cards) < 21:
        return False
    elif sum(dealer_cards) == sum(user_cards):
        return (f"Draw! \nUser cards:{user_cards}, {sum(user_cards)}\nDealer cards:{dealer_cards}, {sum(dealer_cards)}")

    else:
        return False

print(user_cards)
print(dealer_cards)
gameon = True

while gameon:

    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computers first card: {dealer_cards[0]}")

    hit_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while hit_card == 'y':
        user_cards.append(random.choice(cards))
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        # if win_check():
        #     print("You Win")
        #     print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        #     print(f"Dealer cards: {dealer_cards}, current score: {sum(dealer_cards)}")
        result = win_check()
        if result == False:
            hit_card = 'n'
            print (f"You lost! \nUser cards:{user_cards}, {sum(user_cards)}\nDealer cards:{dealer_cards}, {sum(dealer_cards)}")
            break
        else:
            hit_card = input("Type 'y' to get another card, type 'n' to pass: ")
        # print(win_check())
    else:
        while sum(dealer_cards) < 17:
            dealer_cards.append(random.choice(cards))

        result = win_check()
        if result == True:
            print (f"You Won! \nUser cards:{user_cards}, {sum(user_cards)}\nDealer cards:{dealer_cards}, {sum(dealer_cards)}")
        elif result == False:
            print (f"You Lost! \nUser cards:{user_cards}, {sum(user_cards)}\nDealer cards:{dealer_cards}, {sum(dealer_cards)}")
        else:
            print (f"Draw! \nUser cards:{user_cards}, {sum(user_cards)}\nDealer cards:{dealer_cards}, {sum(dealer_cards)}")

    gameon = False
