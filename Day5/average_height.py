# Input a Python list of student heights
test = "151 145 179"
student_heights = test.split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total = 0
number_of_students = 0
for height in student_heights:
  total += height
  number_of_students += 1

average = total / number_of_students
print(f"toal height = {average}")
print(f"number of students = {number_of_students}")
print(f"average height = {average}")