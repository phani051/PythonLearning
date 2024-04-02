# 1st input: enter height in meters e.g: 1.65
height = input("enter height in meters: ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("enter weight in kilograms: ")
bmi = int(int(weight)/float(height)**2)
print("BMI is: "+str(bmi))