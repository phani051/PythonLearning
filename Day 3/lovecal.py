print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ").upper() # What is your name?
name2 = input("What is their name? ").upper() # What is their name?

name1_count = len(name1)
name2_count = len(name2)

true = ["T","R","U","E"]
love = ["L","O","V","E"]

true_count = 0
love_count = 0

for a in range(0,name1_count):
    if name1[a] in true:
        true_count += 1
    if name1[a] in love:
        love_count +=1
for a in range (0,name2_count):
    if name2[a] in true:
        true_count += 1
    if name2[a] in love:
        love_count +=1
        
Love_score = int(str(true_count) + str(love_count))
        
print(Love_score)

if Love_score < 10 or Love_score > 90:
    print(f"Your score is {Love_score}, you go together like coke and mentos.")
elif 40 < Love_score < 50:
    print(f"Your score is {Love_score}, you are alright together.")
else:
    print (f"Your score is {Love_score}.")