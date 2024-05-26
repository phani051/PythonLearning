#TODO: Create a letter using starting_letter.txt

with open("./input/Letters/starting_letter.txt") as letterfile:
    letter = letterfile.read()
print(letter)

with open("./input/Names/invited_names.txt") as namesfile:
    names = namesfile.read().splitlines()
print(names)

for i in names:
    i_letter = letter.replace("[name]", i)
    with open(f'./output/ReadyToSend/{i}_letter.txt', 'w') as finalletter:
        finalletter.write(i_letter)


