# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

high_score = 0

for a in student_scores:
  if a > high_score:
    high_score = a
print (f"The highest score in the class is: {high_score}")


#input: 78 65 89 86 55 91 64 89