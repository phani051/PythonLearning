from art import logo    
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




print(logo) 

def caesar(direction, text, shift):
    
    end_test = ""
    if direction == 'decode':
        shift = shift * -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            end_test += alphabet[new_position]
        else: end_test += char
    print(f"Here's the {direction}d result: {end_test}")
            


end_game = False

while not end_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(direction, text, shift)
    replay = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if replay == "no":
        end_game = True
        print("Goodbye")
    
    