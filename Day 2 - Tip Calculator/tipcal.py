print ("Welcome to tip calculator")
bill = float(input("What was the total bill? "))
no_of_people = float(input("How many people to split the bill? "))
tip_percent = float(input ("What percentage tip would you like to give? 10, 12, or 15? "))
tip = ((bill/no_of_people)/100)*tip_percent
each_person = round((bill/no_of_people)+tip, 2)
print ("Each person should pay: " + str(each_person))