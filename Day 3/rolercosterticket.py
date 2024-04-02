print("Welcome to the RolerCoster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the RolerCoster :)")
    age = int(input("What is your age? "))
    if age < 12:
        print("Chile ticket rates are Rs 5")
        bill = 5
    elif age <= 18:
        print("Youth tickets are Rs 7")
        bill = 7
    elif age >= 45 & age <= 50:
        print("You ride for Free :))")
        bill = 0
    else:
        print("Adult tickets are Rs 12")
        bill = 12
    need_photo = input("Do you want a photo taken? Y or N: ").lower()
    if need_photo == 'y':
        bill += 3 
        print(f"Your ticket place is {bill}")
    else:
        print(f"Your ticket place is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
    