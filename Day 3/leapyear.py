year = int(input("Enter the year to check: "))

# if year %4 == 0 & year % 400 == 0 & year % 100 != 0:
#     print (f"{year} is leap year.")    
# else:
#     print(f"{year} is not leap year.")

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print ( "Leap year")
        else:
            print ( "Not leap year")
    else:
        print ( "Leap year")
else:
    print ( "Not leap year")