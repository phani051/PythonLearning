height = float(input("enter height in meters: "))
weight = input("enter weight in kilograms: ")
bmi = (int(weight)/float(height)**2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5 < bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 <= bmi < 30:
    print (f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 <= bmi <35:
    print (f"Your BMI is {bmi}, you are obese.")
elif 35 <= bmi:
    print (f"Your BMI is {bmi}, you are clinically obese.")   