import hangman_art
import hangman_words
import random
choosen_word = random.choice(hangman_words.word_list)

blank_list = []

print(hangman_art.logo)
#Create blanks
for i in choosen_word:
    blank_list.append("_")

blanks = ' '.join(blank_list)
print(f'Word = {blanks}')

current_userguess = blank_list
life_count = 0
while "_" in current_userguess:
    guess = input("Guess a letter: ").lower()
    count = 0
    
    if life_count < 7:
        
        if guess in choosen_word:        
            for letter in choosen_word:
                if guess == letter:
                    current_userguess[count] = letter
                count += 1
            
        else:
            print(hangman_art.stages[(-(1+life_count))])
            print("you have loast a life")
            life_count += 1
        blanks = ' '.join(current_userguess)
        print(f'Word = {blanks}')
        if ''.join(current_userguess) == choosen_word:
            print("You Win!!")
    else:
       print("You have lost the game!!!!")
       current_userguess = ['+']

    
# Revela the answer
print(f'The word is {choosen_word}')