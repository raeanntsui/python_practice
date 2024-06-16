# Input a list of student scores
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
current_highest = 0
for score in student_scores:
  if score > current_highest:
    current_highest = score
    print(f"Score is {score}")
    print(f"Current highest score is {current_highest}")

print(f"The highest score in the class is: {current_highest}")